# Mitwirken

## Ablauf

1. **Issue eröffnen** mit dem Formular «Neues Datenfeld» oder «Neuer Listenwert», mit Anwendungsfall und Beispiel.
2. **Diskussion** im Issue: Genügt ein bestehendes Datenfeld?
3. **Pull Request**, automatische Prüfung und Review.
4. **Aufnahme** als Erweiterung in `data/extensions/`.

Änderungen am Kern (`data/core/`) sind nur mit einer neuen Ausgabe der Norm möglich. Bewährte Erweiterungen können dann in den Kern übernommen werden.

## Regeln

- **Keys sind endgültig.** Nach der Veröffentlichung werden sie nie umbenannt, gelöscht oder neu belegt.
- **Keys von Datenfeldern:** englisch, camelCase, ausgeschrieben (`weatheringExposure`). Projekt-Datenfelder beginnen mit `project`, Kontakte mit `contact`, Quellobjekte mit `donorBuilding`; Bauteil-Datenfelder haben kein Präfix.
- **Feste Endungen:** `…Notes` für ergänzenden Freitext, `…Code` / `…Label` für Code und Bezeichnung einer Klassifikation, `…Min` / `…Max` für Bereiche, `…StartDate` / `…EndDate` für Zeiträume.
- **Keys von Listenwerten:** englisches Wort in camelCase (`screwed`); bei abgestuften Skalen Ziffern mit `0` für «keine Einschätzung»; bei externen Klassifikationen der Originalcode.
- **Vier Sprachen sind Pflicht:** Bezeichnung und Definition auf Deutsch, Französisch, Italienisch und Englisch. Wer eine Sprache nicht beherrscht, vermerkt das im Pull Request.
- **Keine Einzelfalllösungen.** Ein Datenfeld muss für mehrere Akteurinnen nützlich sein. Erst im [Datenfeldverzeichnis](docs/dictionary/DE.md) prüfen, ob es das schon gibt.

## Beispiel Datenfeld

In `data/extensions/fields/` in der Datei des Bereichs ergänzen:

```yaml
- key: fireResistanceClass
  label:
    de: Feuerwiderstandsklasse
    fr: Classe de résistance au feu
    it: Classe di resistenza al fuoco
    en: Fire resistance class
  group: furtherAttributes
  format: text
  definition:
    de: Feuerwiderstandsklasse gemäss Herstellerangabe oder Typenschild
    fr: Classe de résistance au feu selon les indications du fabricant ou la plaque signalétique
    it: Classe di resistenza al fuoco secondo le indicazioni del fabbricante o la targhetta
    en: Fire resistance class according to the manufacturer or the type plate
```

Die erlaubten Werte für `format`, `unit` und `group` stehen in `data/core/vocabulary.yaml` und sind am Ende des Datenfeldverzeichnisses aufgelistet.

## Beispiel Listenwert

Eine Zeile in der CSV-Datei der Auswahlliste ergänzen, direkt auf GitHub oder in Excel:

```
key,group,de,fr,it,en,definition_de,definition_fr,definition_it,definition_en
bolted,,Verbolzt,Boulonné,Bullonato,Bolted,z. B. bei Stahlträgern,p. ex. pour les poutres en acier,ad es. nelle travi in acciaio,e.g. for steel beams
```

Die Definition ist freiwillig; wenn sie angegeben wird, dann in allen vier Sprachen.

## Vor dem Pull Request

```
python3 tools/validate.py
python3 tools/build.py
```

Die erzeugten Dateien in `docs/` gehören in denselben Pull Request.
