#!/usr/bin/env python3
"""Prüft das Datenfeldverzeichnis. Fehler -> Exit-Code 1, Hinweise blockieren nicht.

Aufruf:  python3 tools/validate.py
"""
import re
import sys

import swissinv
from swissinv import CSV_COLUMNS, LANGS

FORMATS = {}  # wird in main() aus data/core/vocabulary.yaml gefüllt
SHEET_NAME = re.compile(r"^[^':\\/?*\[\]]{1,31}$")
KEY = re.compile(r"^[a-z][A-Za-z0-9]*$")
VALUE_KEY = re.compile(r"^[A-Za-z0-9][A-Za-z0-9.]*$")

errors, warnings = [], []


def check_langs(where, what, texts):
    """Alle vier Sprachen müssen ausgefüllt sein."""
    missing = [l for l in LANGS if not str((texts or {}).get(l) or "").strip()]
    if missing:
        errors.append("%s: %s fehlt in %s" % (where, what, ", ".join(missing)))


def main():
    data = swissinv.load()
    FORMATS.update(data["formats"])

    for key, f in data["formats"].items():
        where = "data/core/vocabulary.yaml formats [%s]" % key
        check_langs(where, "label", f.get("label"))
        if f.get("label_multiple"):
            check_langs(where, "label_multiple", f.get("label_multiple"))
        if not (f.get("schema") or {}).get("type"):
            errors.append("%s: schema.type fehlt" % where)
    for key, v in data["obligations"].items():
        check_langs("data/core/vocabulary.yaml obligations [%s]" % key, "label", v.get("label"))
        check_langs("data/core/vocabulary.yaml obligations [%s]" % key, "phrase", v.get("phrase"))
    for key, v in data["units"].items():
        check_langs("data/core/vocabulary.yaml units [%s]" % key, "name", v.get("name"))

    for key, labels in data["groups"].items():
        check_langs("data/core/vocabulary.yaml groups [%s]" % key, "Bezeichnung", labels)

    for name, cl in data["lists"].items():
        where = "%s [%s]" % (cl["source"], name)
        if cl.get("duplicate"):
            errors.append("%s: Auswahlliste ist doppelt definiert" % where)
        if cl.get("missing_file"):
            errors.append("%s: Datei %s fehlt" % (where, cl["file"]))
        check_langs(where, "title", cl.get("title"))
        if cl.get("note"):
            check_langs(where, "note", cl.get("note"))
        for g, labels in (cl.get("groups") or {}).items():
            check_langs("%s Gruppe %s" % (where, g), "Bezeichnung", labels)
        if not cl.get("file") and not cl.get("placeholder"):
            errors.append("%s: braucht file oder placeholder" % where)
        if cl["columns"] != CSV_COLUMNS:
            errors.append("%s: Spalten müssen %s sein" % (cl["source"], ",".join(CSV_COLUMNS)))
            continue
        for l in LANGS:
            labels = [v[l] for v in cl["values"] if v[l]]
            dup = sorted({x for x in labels if labels.count(x) > 1})
            if dup and cl.get("placeholder"):
                if l == LANGS[0]:
                    warnings.append("%s: Platzhalterliste mit gleichen Bezeichnungen (%s)" % (cl["source"], ", ".join(dup)))
            elif dup:
                errors.append("%s: Bezeichnung (%s) kommt mehrfach vor: %s" % (cl["source"], l, ", ".join(dup)))
        seen = set()
        for i, v in enumerate(cl["values"], start=2):
            w = "%s Zeile %d" % (cl["source"], i)
            if not VALUE_KEY.match(v["key"] or ""):
                errors.append("%s: key fehlt oder enthält unzulässige Zeichen" % w)
            if v["key"] in seen:
                errors.append("%s: key '%s' ist doppelt" % (w, v["key"]))
            seen.add(v["key"])
            check_langs(w, "Bezeichnung", v)
            defs = {l: v["definition_" + l] for l in LANGS}
            if any(defs.values()):
                check_langs(w, "Definition", defs)
            if v["group"] and v["group"] not in (cl.get("groups") or {}):
                errors.append("%s: Gruppe '%s' ist in index.yaml nicht definiert" % (w, v["group"]))

    for ent, e in data["entities"].items():
        check_langs("Entität %s" % ent, "title", e.get("title"))
        seen = {}
        for f in e["fields"]:
            key = f.get("key")
            where = "%s [%s]" % (f["source"], key)
            if not key or not KEY.match(str(key)):
                errors.append("%s: key muss camelCase sein (a-z, A-Z, 0-9)" % where)
            if key in seen:
                errors.append("%s: key ist in '%s' bereits vergeben (%s)" % (where, ent, seen[key]))
            seen[key] = f["source"]
            check_langs(where, "label", f.get("label"))
            check_langs(where, "definition", f.get("definition"))
            if f.get("group") not in data["groups"]:
                errors.append("%s: Gruppe '%s' ist in data/core/vocabulary.yaml nicht definiert" % (where, f.get("group")))
            fmt = data["formats"].get(f.get("format"))
            if not fmt:
                errors.append("%s: format muss eines von %s sein (data/core/vocabulary.yaml)" % (where, sorted(FORMATS)))
                fmt = {}
            if fmt.get("list"):
                if f.get("list") not in data["lists"]:
                    errors.append("%s: Auswahlliste '%s' existiert nicht" % (where, f.get("list")))
            elif f.get("list"):
                errors.append("%s: list ist bei format: %s nicht erlaubt" % (where, f.get("format")))
            if f.get("unit"):
                if not fmt.get("unit"):
                    errors.append("%s: unit ist bei format: %s nicht erlaubt" % (where, f.get("format")))
                elif f["unit"] not in data["units"]:
                    errors.append("%s: Einheit '%s' steht nicht in data/core/vocabulary.yaml" % (where, f["unit"]))

    every = [f["key"] for e in data["entities"].values() for f in e["fields"]]
    for k in sorted({k for k in every if every.count(k) > 1}):
        errors.append("Key '%s' kommt in mehreren Bereichen vor; Keys müssen über alle Bereiche eindeutig sein" % k)

    orders = [p.get("order") for p in data["profiles"]]
    for p in data["profiles"]:
        check_langs(p["source"], "title", p.get("title"))
        check_langs(p["source"], "label", p.get("label"))
        check_langs(p["source"], "short", p.get("short"))
        for l in LANGS:
            if not SHEET_NAME.match(str((p.get("label") or {}).get(l) or "")):
                errors.append("%s: label (%s) muss als Excel-Blattname taugen (1-31 Zeichen, ohne ' : \\ / ? * [ ])" % (p["source"], l))
        if not isinstance(p.get("order"), int) or orders.count(p.get("order")) > 1:
            errors.append("%s: order muss eine eindeutige ganze Zahl sein" % p["source"])
        for r in p.get("requirements") or []:
            fields = data["entities"].get(r.get("entity") or p.get("entity"), {}).get("fields", [])
            keys = {f["key"] for f in fields}
            core = {f["key"] for f in fields if f["layer"] == "core"}
            check_langs(p["source"], "information", r.get("information"))
            if r.get("obligation") not in data["obligations"]:
                errors.append("%s: obligation muss eines von %s sein (data/core/vocabulary.yaml)" % (p["source"], sorted(data["obligations"])))
            for k in r.get("fields") or []:
                if k not in keys:
                    errors.append("%s: Datenfeld '%s' existiert nicht" % (p["source"], k))
                elif k not in core:
                    errors.append("%s: Datenfeld '%s' ist Muss/Sollte, liegt aber nicht im Kern" % (p["source"], k))
            for u in r.get("unresolved") or []:
                check_langs(p["source"], "unresolved", u)
                warnings.append("%s: '%s' hat kein Datenfeld im Verzeichnis" % (p["source"], (u or {}).get("de")))

    # Normtext: jede Audit-Stufe braucht ihre zwei erzeugten Tabellen
    import os
    for lang in LANGS:
        name = "docs/norm/%s.md" % lang.upper()
        norm_path = os.path.join(swissinv.ROOT, "docs", "norm", "%s.md" % lang.upper())
        if not os.path.exists(norm_path):
            errors.append("%s fehlt" % name)
            continue
        norm = open(norm_path, encoding="utf-8").read()
        for p in data["profiles"]:
            for scope in ("projekt", "bauteile"):
                if "<!-- GENERIERT:START profil=%s bereich=%s -->" % (p["profile"], scope) not in norm:
                    errors.append("%s: Markierung für %s / %s fehlt" % (name, p["profile"], scope))
        if norm.count("GENERIERT:START") != norm.count("GENERIERT:ENDE"):
            errors.append("%s: GENERIERT:START und GENERIERT:ENDE sind nicht paarweise" % name)

    ex = data.get("example") or {}
    if ex:
        where = "data/example.yaml"
        fields = {f["key"]: f for f in data["entities"].get(ex.get("entity"), {}).get("fields", [])}
        record = ex.get("record") or {}
        for k, v in record.items():
            f = fields.get(k)
            if not f:
                errors.append("%s: Datenfeld '%s' existiert nicht" % (where, k))
                continue
            if isinstance(v, dict):
                check_langs("%s [%s]" % (where, k), "Wert", v)
            elif data["formats"][f["format"]].get("list"):
                cl = data["lists"][f["list"]]
                if isinstance(v, list) and not f.get("multiple"):
                    errors.append("%s [%s]: nur ein Wert erlaubt (kein multiple: true)" % (where, k))
                for one in (v if isinstance(v, list) else [v]):
                    if cl["values"] and str(one) not in {x["key"] for x in cl["values"]}:
                        errors.append("%s [%s]: Wert '%s' steht nicht in der Auswahlliste %s" % (where, k, one, f["list"]))
            elif data["formats"][f["format"]]["schema"]["type"] == "number" and not isinstance(v, (int, float)):
                errors.append("%s [%s]: Wert muss eine Zahl sein" % (where, k))
        for k in ex.get("card") or []:
            if k not in record:
                errors.append("%s: card nennt '%s', das in record fehlt" % (where, k))

    for w in warnings:
        print("HINWEIS  " + w)
    for e in errors:
        print("FEHLER   " + e)
    n = sum(len(e["fields"]) for e in data["entities"].values())
    v = sum(len(c["values"]) for c in data["lists"].values())
    print("\n%d Datenfelder, %d Auswahllisten mit %d Werten, %d Profile - %d Fehler, %d Hinweise"
          % (n, len(data["lists"]), v, len(data["profiles"]), len(errors), len(warnings)))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
