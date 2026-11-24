#!/usr/bin/env python3
"""Erzeugt alle abgeleiteten Dateien aus data/core/ und data/extensions/.

Alles liegt im Ordner docs/. Er ist zugleich der Web-Ordner für das Hosting:
  docs/index.html                                    durchsuchbare Website mit Sprachwahl
  docs/dictionary/DE.md                    Datenfeldverzeichnis pro Sprache (DE.md, FR.md, IT.md, EN.md)
  docs/schema.json    JSON Schema für einen Bauteil-Datensatz
  docs/excel/DE.xlsx                        Excel-Erfassungsvorlage pro Sprache (tools/build_excel.py)
  docs/norm/DE.md                                    Normtext pro Sprache: von Hand geschrieben, nur die Tabellen
                                                     zwischen den GENERIERT-Markierungen werden erzeugt

Ausserdem werden die Auswahlfelder im Issue-Formular nachgeführt (GENERIERT-Markierungen).

Ausser dem Fliesstext in docs/norm/ und den Schriften in docs/fonts/ nichts in docs/ von Hand bearbeiten.  Aufruf:  python3 tools/build.py
"""
import json
import os
import re

import build_excel
import i18n
import swissinv
from i18n import T
from swissinv import LANGS

ROOT = swissinv.ROOT
# Adresse des Repositorys für den Link «Zum Repository» auf der Website; leer = kein Link.
REPO_URL = "https://github.com/AyraaT/SwissInv"
GENERATED = "<!-- Automatisch erzeugt von tools/build.py - nicht von Hand bearbeiten. -->"


def doc_name(lang):
    return "%s.md" % lang.upper()


def fmt_key(f):
    """Key der Formatbezeichnung; bei Mehrfachauswahl die Variante label_multiple."""
    return "%s_multi" % f.get("format") if f.get("multiple") else f.get("format")


def format_text(f, lang):
    s = T[lang]["formats"].get(fmt_key(f), str(f.get("format")))
    return "%s [%s]" % (s, f["unit"]) if f.get("unit") else s




def write(path, text):
    path = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    print("geschrieben:", swissinv.rel(path))


def cell(s):
    return str(s or "").replace("|", "\\|").replace("\n", " ")


# --------------------------------------------------------------------------- Markdown
def build_markdown(data, obl, lang):
    t = T[lang]
    tr = lambda d: (d or {}).get(lang, "")
    profiles = data["profiles"]
    links = " · ".join("**%s**" % T[l]["name"] if l == lang else "[%s](%s)" % (T[l]["name"], doc_name(l)) for l in LANGS)
    out = [GENERATED, "", "# " + t["title"], "", links, "", "%s: `%s`" % (t["version"], data["version"]), "", t["intro"], ""]
    for name, ent in data["entities"].items():
        out += ["## %s %s" % (t["fields_of"], tr(ent["title"])), ""]
        comp = any(f["key"] in obl[p["profile"]] for p in profiles for f in ent["fields"])
        head = [t["field"], t["key"], t["format"], t["layer"]] + ([tr(p["short"]) for p in profiles] if comp else []) + [t["definition"]]
        group = object()
        for f in ent["fields"]:
            if f.get("group") != group:
                group = f.get("group")
                out += ([] if out[-1] == "" else [""]) + ["### %s" % (tr(data["groups"].get(group)) or t["general"]), "",
                                                          "| " + " | ".join(head) + " |", "|" + " --- |" * len(head)]
            fmt = format_text(f, lang)
            if f.get("list"):
                fmt += " → [%s](#list-%s)" % (f["list"], f["list"])
            row = [tr(f.get("label")), "`%s`" % f["key"], fmt, t["layers"][f["layer"]]]
            if comp:
                row += [t["obligations"].get(obl[p["profile"]].get(f["key"]), "") for p in profiles]
            row += [tr(f.get("definition"))]
            out.append("| " + " | ".join(cell(c) for c in row) + " |")
        out.append("")
    out += ["## " + t["lists"], ""]
    for name, cl in data["lists"].items():
        out += ['<a id="list-%s"></a>' % name, "", "### %s (`%s`)" % (tr(cl["title"]), name), "",
                t["layers"][cl["layer"]], ""]
        if tr(cl.get("note")):
            out += [tr(cl["note"]), ""]
        if cl["values"]:
            grp = any(v["group"] for v in cl["values"])
            head = [t["key"], t["label"]] + ([t["group"]] if grp else []) + [t["definition"]]
            out += ["| " + " | ".join(head) + " |", "|" + " --- |" * len(head)]
            for v in cl["values"]:
                row = ["`%s`" % v["key"], v[lang]] + ([tr((cl.get("groups") or {}).get(v["group"]))] if grp else [])
                row += [v["definition_" + lang]]
                out.append("| " + " | ".join(cell(c) for c in row) + " |")
            out.append("")
    # Formate, Verpflichtungen und Einheiten: die Wertevorräte aus data/core/vocabulary.yaml
    out += ["## " + t["h_formats"], "", "| %s | %s |" % (t["key"], t["label"]), "| --- | --- |"]
    for k, v in data["formats"].items():
        out.append("| `%s` | %s |" % (k, cell(" / ".join(x for x in [tr(v["label"]), tr(v.get("label_multiple"))] if x))))
    out += ["", "## " + t["h_obligations"], "", "| %s | %s |" % (t["key"], t["label"]), "| --- | --- |"]
    out += ["| `%s` | %s |" % (k, cell(tr(v["label"]))) for k, v in data["obligations"].items()]
    out += ["", "## " + t["h_units"], "", "| %s | %s |" % (t["symbol"], t["label"]), "| --- | --- |"]
    out += ["| %s | %s |" % (cell(k), cell(tr(v["name"]))) for k, v in data["units"].items()]
    return "\n".join(out).rstrip() + "\n"


# --------------------------------------------------------------------------- Normtext
MARK = re.compile(r"(<!-- GENERIERT:START profil=(\S+) bereich=(\S+) -->)\n.*?(<!-- GENERIERT:ENDE -->)", re.S)


def norm_path(lang):
    return "docs/norm/%s.md" % lang.upper()


def norm_table(data, profile, scope, lang):
    """Tabelle «Zu erfassende Informationen» einer Audit-Stufe: Bauteile oder Projekt und Quellobjekte."""
    t = T[lang]
    tr = lambda d: d[lang]
    p = next(x for x in data["profiles"] if x["profile"] == profile)
    fields = {f["key"]: f for e in data["entities"].values() for f in e["fields"]}
    component = scope == "bauteile"
    caption = (t["n_caption_component"] if component else t["n_caption_project"]).replace("{title}", tr(p["title"]))
    out = ["**%s**" % caption, "", "| %s |" % " | ".join([t["n_information"], t["h_obligations"], t["field"], t["key"], t["format"]]),
           "| --- | --- | --- | --- | --- |"]
    for r in p["requirements"]:
        if (r.get("entity", "component") == "component") != component:
            continue
        info, ob = tr(r["information"]), t["obligations"][r["obligation"]]
        rows = [[tr(fields[k]["label"]), "`%s`" % k, format_text(fields[k], lang)] for k in r.get("fields") or []]
        rows += [[tr(u), "", t["n_unresolved"]] for u in r.get("unresolved") or []]
        if r.get("attachment"):
            rows = [[t["n_attachment"], "", ""]]
        for i, row in enumerate(rows):  # Information und Verpflichtung nur in der ersten Zeile
            out.append("| " + " | ".join(cell(c) for c in ([info, ob] if i == 0 else ["", ""]) + row) + " |")
    return "\n".join(out)


def build_norm(data):
    for lang in LANGS:
        with open(os.path.join(ROOT, norm_path(lang)), encoding="utf-8") as fh:
            text = fh.read()
        text = MARK.sub(lambda m: "%s\n%s\n%s" % (m.group(1), norm_table(data, m.group(2), m.group(3), lang), m.group(4)), text)
        write(norm_path(lang), text)


# --------------------------------------------------------------------------- Listen im Issue-Formular
YML_REGION = re.compile(r"^([ \t]*)# GENERIERT:START (\w+)\n.*?^[ \t]*# GENERIERT:ENDE", re.S | re.M)
REGION_FILES = [".github/ISSUE_TEMPLATE/neues-datenfeld.yml"]


def region_yml(data, name):
    if name == "formate":
        return [x for v in data["formats"].values() for x in [v["label"]["de"], (v.get("label_multiple") or {}).get("de")] if x]
    if name == "bereiche":
        return [e["title"]["de"] for e in data["entities"].values()]
    raise SystemExit("Unbekannte Markierung GENERIERT:START %s" % name)


def build_regions(data):
    for path in REGION_FILES:
        with open(os.path.join(ROOT, path), encoding="utf-8") as fh:
            text = fh.read()
        text = YML_REGION.sub(lambda m: "\n".join(
            ["%s# GENERIERT:START %s" % (m.group(1), m.group(2))]
            + ["%s- %s" % (m.group(1), json.dumps(x, ensure_ascii=False)) for x in region_yml(data, m.group(2))]
            + ["%s# GENERIERT:ENDE" % m.group(1)]), text)
        write(path, text)


# --------------------------------------------------------------------------- JSON Schema
def build_schema(data):
    props = {}
    for f in data["entities"]["component"]["fields"]:
        spec = data["formats"][f["format"]]
        p = dict(spec["schema"])  # Typ und Muster stehen in data/core/vocabulary.yaml
        if spec.get("list"):
            cl = data["lists"][f["list"]]
            if cl["values"] and not cl.get("placeholder"):
                p["enum"] = [v["key"] for v in cl["values"]]
            if f.get("multiple"):
                p = {"type": "array", "items": p}
        p["title"] = f["label"]["en"]
        p["description"] = f["definition"]["en"]
        props[f["key"]] = p
    return {"$schema": "https://json-schema.org/draft/2020-12/schema",
            "title": "Swiss Inv reuse component", "version": data["version"],
            "type": "object", "properties": props, "additionalProperties": True}


# --------------------------------------------------------------------------- Website
def build_site(data, obl):
    payload = {"version": data["version"], "langs": LANGS, "t": T, "groups": data["groups"], "repo": REPO_URL,
               "example": data.get("example") or {},
               "profiles": [{"id": p["profile"], "order": p["order"], "label": p["label"], "short": p["short"]} for p in data["profiles"]],
               "obligations": {k: {"phrase": v["phrase"], "required": bool(v.get("required"))} for k, v in data["obligations"].items()},
               "entities": [], "lists": []}
    for name, ent in data["entities"].items():
        payload["entities"].append({"name": name, "title": ent["title"], "fields": [
            {"key": f["key"], "label": f["label"], "group": f.get("group") or "", "format": fmt_key(f), "unit": f.get("unit") or "",
             "list": f.get("list") or "", "layer": f["layer"],
             "definition": f["definition"],
             "req": {p["profile"]: obl[p["profile"]][f["key"]] for p in data["profiles"] if f["key"] in obl[p["profile"]]}}
            for f in ent["fields"]]})
    for name, cl in data["lists"].items():
        payload["lists"].append({"name": name, "title": cl["title"], "layer": cl["layer"],
            "note": cl.get("note") or {}, "groups": cl.get("groups") or {},
            "values": [{"key": v["key"], "label": {l: v[l] for l in LANGS}, "group": v["group"],
                        "definition": {l: v["definition_" + l] for l in LANGS}} for v in cl["values"]]})
    with open(os.path.join(ROOT, "tools", "site-template.html"), encoding="utf-8") as fh:
        tpl = fh.read()
    blob = json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")
    return tpl.replace("/*__DATA__*/null", blob)


def main():
    data = swissinv.load()
    i18n.apply(data)
    obl = swissinv.obligations(data)
    for lang in LANGS:
        write("docs/dictionary/" + doc_name(lang), build_markdown(data, obl, lang))
    build_norm(data)
    build_regions(data)
    write("docs/index.html", build_site(data, obl))
    write("docs/schema.json", json.dumps(build_schema(data), ensure_ascii=False, indent=2) + "\n")
    build_excel.main(data)


if __name__ == "__main__":
    main()
