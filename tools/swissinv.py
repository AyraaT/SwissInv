"""Lädt das Swiss-Inv-Datenfeldverzeichnis aus data/ (core/ und extensions/)."""
import csv
import glob
import os

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")  # hier liegen core/ und extensions/
LAYERS = ["core", "extensions"]
LANGS = ["de", "fr", "it", "en"]
ENTITY_ORDER = ["project", "contact", "donorBuilding", "component", "changeLog"]
CSV_COLUMNS = ["key", "group", "de", "fr", "it", "en", "definition_de", "definition_fr",
               "definition_it", "definition_en"]


def rel(path):
    return os.path.relpath(path, ROOT).replace(os.sep, "/")


def read_yaml(path):
    with open(path, encoding="utf-8") as fh:
        return yaml.safe_load(fh) or {}


def load():
    """Gibt das zusammengeführte Verzeichnis als dict zurück."""
    with open(os.path.join(DATA, "VERSION"), encoding="utf-8") as fh:
        version = fh.read().strip()
    voc = read_yaml(os.path.join(DATA, "core", "vocabulary.yaml"))
    groups, formats, units, obl = [voc.get(n) or {} for n in ("groups", "formats", "units", "obligations")]
    entities, lists, profiles = {}, {}, []

    for layer in LAYERS:
        for path in sorted(glob.glob(os.path.join(DATA, layer, "fields", "*.yaml"))):
            doc = read_yaml(path)
            ent = entities.setdefault(doc.get("entity"), {"title": doc.get("title", {}), "fields": [], "groups": []})
            ent["groups"] += [g for g in doc.get("groups") or [] if g not in ent["groups"]]
            for f in doc.get("fields") or []:
                f = dict(f)
                f["layer"] = "core" if layer == "core" else "extension"
                f["source"] = rel(path)
                ent["fields"].append(f)

        idx_path = os.path.join(DATA, layer, "lists", "index.yaml")
        if not os.path.exists(idx_path):
            continue
        for entry in read_yaml(idx_path).get("lists") or []:
            cl = dict(entry)
            cl["layer"] = "core" if layer == "core" else "extension"
            cl["source"] = rel(idx_path)
            cl["values"] = []
            cl["columns"] = CSV_COLUMNS
            if cl.get("file"):
                p = os.path.join(DATA, layer, "lists", cl["file"])
                cl["source"] = rel(p)
                if os.path.exists(p):
                    with open(p, encoding="utf-8", newline="") as fh:
                        reader = csv.DictReader(fh)
                        cl["values"] = list(reader)
                        cl["columns"] = reader.fieldnames
                else:
                    cl["missing_file"] = True
            cl["duplicate"] = cl["name"] in lists
            lists.setdefault(cl["name"], cl)

    for path in sorted(glob.glob(os.path.join(DATA, "core", "audits", "*.yaml"))):
        p = read_yaml(path)
        p["source"] = rel(path)
        profiles.append(p)

    profiles.sort(key=lambda p: (p.get("order", 0), p.get("profile", "")))
    for ent in entities.values():
        # Felder nach Gruppen ordnen: festgelegte Reihenfolge, sonst erstes Auftreten; Kern vor Erweiterung
        order = list(dict.fromkeys(ent["groups"] + [f.get("group") for f in ent["fields"]]))
        ent["fields"].sort(key=lambda f: order.index(f.get("group")))
    ordered = {k: entities[k] for k in ENTITY_ORDER if k in entities}
    ordered.update({k: v for k, v in entities.items() if k not in ordered})
    ex_path = os.path.join(DATA, "example.yaml")
    example = read_yaml(ex_path) if os.path.exists(ex_path) else {}
    return {"version": version, "groups": groups, "formats": formats, "units": units,
            "obligations": obl, "entities": ordered, "lists": lists, "profiles": profiles, "example": example}


def obligations(data):
    """{profilname: {feldschlüssel: verpflichtung}}; bei mehreren Nennungen gilt die strengste."""
    rank = list(data["obligations"])  # strengste zuerst
    pos = lambda o: rank.index(o) if o in rank else len(rank)
    out = {}
    for p in data["profiles"]:
        m = out.setdefault(p["profile"], {})
        for r in p.get("requirements") or []:
            for k in r.get("fields") or []:
                if k not in m or pos(r.get("obligation")) < pos(m[k]):
                    m[k] = r.get("obligation")
    return out


def strictest(data, obl, key):
    """Strengste Verpflichtung eines Datenfelds über alle Profile, sonst ''."""
    found = [o[key] for o in obl.values() if key in o]
    return min(found, key=list(data["obligations"]).index) if found else ""
