#!/usr/bin/env python3
"""Erzeugt die Excel-Erfassungsvorlage aus dem Datenfeldverzeichnis, eine Datei pro Sprache:

  docs/excel/DE.xlsx  (ebenso FR, IT, EN)

Blätter: Anleitung, Projekt, Audit Stufe I, Audit Stufe II, Bauteile alle Felder, Datenfelder, Auswahllisten.
Die Spalten der Audit-Blätter folgen data/core/audits/, die Auswahllisten den CSV-Dateien.
Die Dateien werden bei jedem Build neu erzeugt, Byte für Byte gleich, solange sich die Daten nicht ändern.

Aufruf:  python3 tools/build_excel.py   (wird auch von tools/build.py aufgerufen)
"""
import datetime
import io
import os
import re
import zipfile

from openpyxl import Workbook
from openpyxl.comments import Comment
from openpyxl.formatting.rule import FormulaRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter as col
from openpyxl.worksheet.datavalidation import DataValidation

import i18n
import swissinv
from i18n import T, XL
from swissinv import LANGS

ROOT = swissinv.ROOT
INK, PAPER, GREY, SOFT, MUTE, LINE, ACCENT = "15201B", "F3F4F0", "C9CEC4", "FBE3C8", "4A554F", "D5D8CF", "F28C28"
ROWS = 1000        # Zeilen mit Auswahllisten und Prüfungen
FORMULA_ROWS = 300  # Zeilen mit vorbereiteter Formel (z. B. eBKP-H Key)
FILL = {"dark": PatternFill("solid", fgColor=INK), "must": PatternFill("solid", fgColor=ACCENT), "grey": PatternFill("solid", fgColor=GREY),
        "": PatternFill("solid", fgColor=PAPER),
        "missing": PatternFill("solid", bgColor=SOFT, fgColor=SOFT)}
HEAD_FONT = {"dark": Font(bold=True, color="FFFFFF"), "must": Font(bold=True, color=INK), "grey": Font(bold=True, color=INK), "": Font(bold=True, color=INK)}
KEY_FONT = Font(name="Consolas", size=9, color=MUTE)
THIN = Side(style="thin", color=LINE)
BOX = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
WRAP = Alignment(wrap_text=True, vertical="top")


def ref(sheet, c, r1, r2):
    return "'%s'!$%s$%d:$%s$%d" % (sheet, col(c), r1, col(c), r2)


STYLE = {}  # Verpflichtung -> Darstellung (required: orange, sonst grau); aus data/core/vocabulary.yaml


def head(ws, row, c, text, obligation="", comment=None):
    cell = ws.cell(row, c, text)
    style = STYLE.get(obligation, obligation)
    cell.fill, cell.font, cell.border = FILL[style], HEAD_FONT[style], BOX
    cell.alignment = Alignment(wrap_text=True, vertical="center")
    if comment:
        cell.comment = Comment(comment, "Swiss Inv", width=320, height=140)
    return cell


class Book:
    def __init__(self, data, lang):
        self.data, self.lang, self.t, self.x = data, lang, T[lang], XL[lang]
        self.obl = swissinv.obligations(data)
        self.profiles = data["profiles"]
        STYLE.update({k: ("must" if v.get("required") else "grey") for k, v in data["obligations"].items()})
        # strengste Pflicht über alle Audit-Stufen, für Blätter, die mehreren Stufen dienen
        keys = {k for o in self.obl.values() for k in o}
        self.ob_max = {k: swissinv.strictest(data, self.obl, k) for k in keys}
        self.wb = Workbook()
        self.ranges = {}  # Auswahlliste -> (Bezug auf Bezeichnungen, Bezug auf Keys)

    def required(self, obligation):
        return bool(self.data["obligations"].get(obligation, {}).get("required"))

    def tr(self, d):
        return (d or {}).get(self.lang, "")

    def label(self, f):
        return "%s [%s]" % (self.tr(f["label"]), f["unit"]) if f.get("unit") else self.tr(f["label"])

    def note(self, f):
        """Text der Notiz am Spaltenkopf: Definition, Format und Pflicht je Audit-Stufe."""
        lines = [self.tr(f["definition"]), "", self.fmt(f)]
        if f["key"] in self.ob_max:
            ob = self.t["obligations"]
            lines.append(" · ".join("%s: %s" % (self.tr(p["label"]), ob.get(self.obl[p["profile"]].get(f["key"]), "–"))
                                    for p in self.profiles))
        return "\n".join(lines)

    def fmt(self, f):
        k = "%s_multi" % f["format"] if f.get("multiple") else f["format"]
        return self.t["formats"].get(k, f["format"])

    # ------------------------------------------------------------------ Auswahllisten
    def lists(self):
        ws = self.wb.create_sheet(self.x["sheets"]["lists"])
        c = 1
        for name, cl in self.data["lists"].items():
            if not cl["values"]:
                continue
            ws.cell(1, c, "%s (%s)" % (self.tr(cl["title"]), name)).font = Font(bold=True, size=12)
            for i, h in enumerate([self.t["key"], self.t["label"], self.t["definition"]]):
                head(ws, 2, c + i, h)
            for r, v in enumerate(cl["values"], start=3):
                k = ws.cell(r, c, str(v["key"]))
                k.number_format, k.font = "@", KEY_FONT
                ws.cell(r, c + 1, v[self.lang])
                ws.cell(r, c + 2, v["definition_" + self.lang]).alignment = WRAP
            last = len(cl["values"]) + 2
            self.ranges[name] = (ref(ws.title, c + 1, 3, last), ref(ws.title, c, 3, last))
            ws.column_dimensions[col(c)].width = 16
            ws.column_dimensions[col(c + 1)].width = 38
            ws.column_dimensions[col(c + 2)].width = 46
            ws.column_dimensions[col(c + 3)].width = 3
            c += 4
        ws.freeze_panes = "A3"

    # ------------------------------------------------------------------ Tabellen mit Datenfeldern
    def validations(self, ws, f, c, r1, r2):
        """Auswahlliste und Zellformat für eine Spalte. Eingaben werden nicht geprüft."""
        spec = self.data["formats"][f["format"]]
        if spec.get("list") and f.get("list") in self.ranges:
            labels, _ = self.ranges[f["list"]]
            dv = DataValidation(type="list", formula1=labels, allow_blank=True, showErrorMessage=True)
            if f.get("multiple"):
                dv.showErrorMessage, dv.prompt, dv.showInputMessage = False, self.x["multi"], True
            ws.add_data_validation(dv)
            dv.add("%s%d:%s%d" % (col(c), r1, col(c), r2))
        number_format = (spec.get("excel") or {}).get("number_format", "@")
        for r in range(r1, min(r2, r1 + FORMULA_ROWS) + 1):
            ws.cell(r, c).number_format = number_format

    def table(self, ws, top, fields, obligations=None, first_col=1, rows=ROWS, source=None):
        """Kopfzeile (Bezeichnung) und Auswahllisten. Gibt {key: Spalte} zurück.
        source: {key: (Blatt, Spalte)} - diese Spalten übernehmen den Wert aus einem früheren Blatt."""
        obligations = obligations or {}
        cols = {}
        for i, f in enumerate(fields):
            c = first_col + i
            cols[f["key"]] = c
            head(ws, top, c, self.label(f), obligations.get(f["key"], ""), self.note(f))
            width = (self.data["formats"][f["format"]].get("excel") or {}).get("width", 20)
            ws.column_dimensions[col(c)].width = max(width, ws.column_dimensions[col(c)].width or 0)
        r1, r2 = top + 1, top + rows
        by_key = {f["key"]: f for f in fields}
        for f in fields:
            c = cols[f["key"]]
            key = f["key"]
            # Paar Code/Bezeichnung einer externen Klassifikation mit Referenzauswahl (eBKP-H):
            # Bezeichnung als Vorschlagsliste, Code per Formel; andere Werte bleiben erlaubt.
            if key.endswith("Code") and f.get("list") in self.ranges and key[:-4] + "Label" in by_key:
                labels, keys = self.ranges[f["list"]]
                lc = cols[key[:-4] + "Label"]
                dv = DataValidation(type="list", formula1=labels, allow_blank=True, showErrorMessage=False)
                ws.add_data_validation(dv)
                dv.add("%s%d:%s%d" % (col(lc), r1, col(lc), r2))
                for r in range(r1, min(r2, r1 + FORMULA_ROWS - 1) + 1):
                    ws.cell(r, c, '=IFERROR(INDEX(%s,MATCH(%s%d,%s,0)),"")' % (keys, col(lc), r, labels))
                continue
            if key.endswith("Label") and key[:-5] + "Code" in by_key and by_key[key[:-5] + "Code"].get("list") in self.ranges:
                continue
            self.validations(ws, f, c, r1, r2)
        for key, (sheet, letter) in (source or {}).items():  # Wert aus dem früheren Blatt übernehmen
            if key not in cols or (key.endswith("Code") and key[:-4] + "Label" in by_key):
                continue  # der Code wird im Blatt selbst aus der Bezeichnung ermittelt
            name = "'%s'" % sheet.replace("'", "''")
            for r in range(r1, min(r2, r1 + FORMULA_ROWS - 1) + 1):
                cell = ws.cell(r, cols[key], '=IF(%s!%s%d="","",%s!%s%d)' % (name, letter, r, name, letter, r))
                if cell.number_format == "@":
                    cell.number_format = "General"
        return cols

    def component_sheet(self, name, fields, obligations, attachments=(), source=None):
        ws = self.wb.create_sheet(name)
        cols = self.table(ws, 1, fields, obligations, source=source)
        c = len(fields) + 1
        for a in attachments:  # Anhänge haben kein Datenfeld: Spalte für den Dateinamen
            head(ws, 1, c, "%s (%s)" % (self.tr(a["information"]), self.x["file"]), a.get("obligation", ""))
            ws.column_dimensions[col(c)].width = 34
            c += 1
        ws.row_dimensions[1].height = 36
        ws.freeze_panes = "B2"
        anchor = col(cols.get("name", 1))
        for f in fields:  # fehlende Muss-Angabe markieren, sobald die Zeile eine Bezeichnung hat
            if self.required(obligations.get(f["key"])) and f["key"] != "name":
                L = col(cols[f["key"]])
                ws.conditional_formatting.add("%s2:%s%d" % (L, L, ROWS + 1),
                                              FormulaRule(formula=['AND($%s2<>"",%s2="")' % (anchor, L)], fill=FILL["missing"]))
        return {k: (name, col(c)) for k, c in cols.items()}

    # ------------------------------------------------------------------ einzelne Blätter
    def guide(self):
        ws = self.wb.active
        ws.title = self.x["sheets"]["guide"]
        ws.column_dimensions["A"].width = 26
        ws.column_dimensions["B"].width = 110
        ws["A1"] = self.x["guide_title"]
        ws["A1"].font = Font(bold=True, size=18, color=INK)
        ws["A2"] = "%s %s" % (self.t["version"], self.data["version"])
        ws["A2"].font = Font(color=MUTE)
        r = 4
        for i, line in enumerate(self.x["guide"], start=1):
            ws.cell(r, 1, i).alignment = Alignment(horizontal="left", vertical="top")
            names = ", ".join("«%s»" % self.tr(p["label"]) for p in self.profiles)
            ws.cell(r, 2, line.replace("{v}", self.data["version"]).replace("{p}", names)).alignment = WRAP
            r += 1
        r += 1
        ws.cell(r, 1, self.x["legend"]).font = Font(bold=True)
        legend = [(self.t["obligations"][k], k) for k in self.data["obligations"]] + [(self.x["optional"], "")]
        for text, ob in legend:
            r += 1
            head(ws, r, 1, text, ob)
        r += 1
        cell = ws.cell(r, 1, self.x["missing"])
        cell.fill, cell.border = PatternFill("solid", fgColor=SOFT), BOX

    def project(self):
        ents = self.data["entities"]
        ws = self.wb.create_sheet(self.x["sheets"]["project"])
        ws["A1"] = self.tr(ents["project"]["title"])
        ws["A1"].font = Font(bold=True, size=14)
        plain = [f for f in ents["project"]["fields"] if f["format"] != "contact"]
        roles = [f for f in ents["project"]["fields"] if f["format"] == "contact"]
        r = 2
        for f in plain:
            head(ws, r, 1, self.label(f), self.ob_max.get(f["key"], ""), self.note(f))
            v = ws.cell(r, 2)
            v.border, v.number_format = BOX, "@"
            ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=4)
            if self.required(self.ob_max.get(f["key"])):
                ws.conditional_formatting.add("B%d" % r, FormulaRule(formula=['$B$%d=""' % r], fill=FILL["missing"]))
            r += 1
        r += 1
        ws.cell(r, 1, self.tr(ents["contact"]["title"])).font = Font(bold=True, size=14)
        r += 1
        head(ws, r, 1, self.x["role"])
        contact = ents["contact"]["fields"]
        cols = self.table(ws, r, contact, first_col=2, rows=len(roles))
        for i, role in enumerate(roles):
            rr = r + 1 + i
            head(ws, rr, 1, self.tr(role["label"]), self.ob_max.get(role["key"], ""), self.note(role))
            for c in cols.values():
                ws.cell(rr, c).border = BOX
            if self.required(self.ob_max.get(role["key"])):  # Pflicht-Beteiligte: Name darf nicht fehlen
                ws.conditional_formatting.add("B%d" % rr, FormulaRule(formula=['$B$%d=""' % rr], fill=FILL["missing"]))
        r += 1 + len(roles) + 1
        if "changeLog" in ents:
            ws.cell(r, 1, self.tr(ents["changeLog"]["title"])).font = Font(bold=True, size=14)
            r += 1
            self.table(ws, r, ents["changeLog"]["fields"], rows=8)
            for rr in range(r + 1, r + 9):
                for c in range(1, len(ents["changeLog"]["fields"]) + 1):
                    ws.cell(rr, c).border = BOX
            r += 1 + 8 + 1
        ws.cell(r, 1, self.tr(ents["donorBuilding"]["title"])).font = Font(bold=True, size=14)
        r += 1
        buildings = ents["donorBuilding"]["fields"]
        bcols = self.table(ws, r, buildings, self.ob_max, rows=50)
        r1, lastc = r + 1, col(len(buildings))
        for f in buildings:  # fehlende Muss-Angabe markieren, sobald die Zeile begonnen ist
            if self.required(self.ob_max.get(f["key"])):
                L = col(bcols[f["key"]])
                ws.conditional_formatting.add("%s%d:%s%d" % (L, r1, L, r1 + 49), FormulaRule(
                    formula=['AND(COUNTA($A%d:$%s%d)>0,%s%d="")' % (r1, lastc, r1, L, r1)], fill=FILL["missing"]))
        ws.column_dimensions["A"].width = 26

    def fields(self):
        ws = self.wb.create_sheet(self.x["sheets"]["fields"])
        t = self.t
        heads = [self.x["entity"], t["group"], t["key"], t["label"], t["format"], self.x["unit"], self.x["list"],
                 t["layer"]] + [self.tr(p["short"]) for p in self.profiles] + [t["definition"]]
        for c, h in enumerate(heads, start=1):
            head(ws, 1, c, h, "dark")
        r = 2
        for name, ent in self.data["entities"].items():
            for f in ent["fields"]:
                row = [self.tr(ent["title"]), self.tr(self.data["groups"].get(f["group"])), f["key"], self.tr(f["label"]),
                       self.fmt(f), f.get("unit", ""), f.get("list", ""), t["layers"][f["layer"]]]
                row += [t["obligations"].get(self.obl[p["profile"]].get(f["key"]), "") for p in self.profiles]
                row += [self.tr(f["definition"])]
                for c, v in enumerate(row, start=1):
                    cell = ws.cell(r, c, v)
                    cell.alignment = WRAP
                    if c == 3:
                        cell.font = KEY_FONT
                r += 1
        widths = [18, 20, 30, 30, 26, 10, 22, 14] + [13] * len(self.profiles) + [90]
        for c, w in enumerate(widths, start=1):
            ws.column_dimensions[col(c)].width = w
        ws.freeze_panes = "A2"
        ws.auto_filter.ref = "A1:%s%d" % (col(len(heads)), r - 1)

    # ------------------------------------------------------------------ alles zusammen
    def build(self):
        self.guide()
        self.lists()  # zuerst, damit die Bezüge für die Auswahllisten bekannt sind
        self.project()
        comp = self.data["entities"]["component"]["fields"]
        by_key = {f["key"]: f for f in comp}
        names, source = [], {}  # source: wo ein Datenfeld zuletzt erfasst wurde, damit spätere Blätter den Wert übernehmen
        for p in self.profiles:  # ein Blatt pro Audit-Profil in data/core/audits/
            keys = [k for r in p["requirements"] if r.get("entity", "component") == "component" for k in r.get("fields") or []]
            attach = [r for r in p["requirements"] if r.get("attachment")]
            names.append(self.tr(p["label"]))
            source.update(self.component_sheet(names[-1], [by_key[k] for k in dict.fromkeys(keys)], self.obl[p["profile"]], attach, source))
        self.component_sheet(self.x["sheets"]["all"], comp, self.ob_max, source=source)
        self.fields()
        sh = self.x["sheets"]
        order = [sh["guide"], sh["project"]] + names + [sh["all"], sh["fields"], sh["lists"]]
        self.wb._sheets.sort(key=lambda ws: order.index(ws.title))
        self.wb.active = 0
        return self.wb


FIXED = datetime.datetime(2000, 1, 1)


def save_reproducible(wb, path):
    """Speichert ohne Zeitstempel, damit ein Build ohne Datenänderung dieselbe Datei ergibt."""
    wb.properties.created = wb.properties.modified = FIXED
    buf = io.BytesIO()
    wb.save(buf)
    with zipfile.ZipFile(buf) as src, zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as dst:
        for item in src.infolist():
            info = zipfile.ZipInfo(item.filename, date_time=(2000, 1, 1, 0, 0, 0))
            info.compress_type, info.external_attr = zipfile.ZIP_DEFLATED, item.external_attr
            blob = src.read(item.filename)
            if item.filename == "docProps/core.xml":  # openpyxl trägt beim Speichern die aktuelle Zeit ein
                blob = re.sub(rb"(<dcterms:(?:created|modified)[^>]*>)[^<]*", rb"\g<1>2000-01-01T00:00:00Z", blob)
            dst.writestr(info, blob)


def main(data=None):
    data = data or swissinv.load()
    i18n.apply(data)
    os.makedirs(os.path.join(ROOT, "docs", "excel"), exist_ok=True)
    for lang in LANGS:
        path = os.path.join(ROOT, "docs", "excel", "%s.xlsx" % lang.upper())
        save_reproducible(Book(data, lang).build(), path)
        print("geschrieben:", swissinv.rel(path))


if __name__ == "__main__":
    main()
