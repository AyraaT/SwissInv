# Swiss Inv

Datenstandard für die Wiederverwendung von Bauteilen: Wiederverwendungs-Audit (Stufe I und II) und Datenfeldverzeichnis, in vier Sprachen. **Stand: Entwurf.**

## Inhalt

| | Deutsch | Français | Italiano | English |
| --- | --- | --- | --- | --- |
| Normtext zum Audit | [DE](docs/norm/DE.md) | [FR](docs/norm/FR.md) | [IT](docs/norm/IT.md) | [EN](docs/norm/EN.md) |
| Datenfeldverzeichnis | [DE](docs/dictionary/DE.md) | [FR](docs/dictionary/FR.md) | [IT](docs/dictionary/IT.md) | [EN](docs/dictionary/EN.md) |
| Excel-Erfassungsvorlage | [DE](docs/excel/DE.xlsx) | [FR](docs/excel/FR.xlsx) | [IT](docs/excel/IT.xlsx) | [EN](docs/excel/EN.xlsx) |

Dazu die durchsuchbare Website `docs/index.html` und das [JSON Schema](docs/schema.json) für Software.

## Aufbau

| Ordner | Inhalt |
| --- | --- |
| `data/` | Die Daten: Datenfelder, Auswahllisten und Audit-Stufen. `core/` ist der stabile Kern und ändert nur mit einer neuen Ausgabe der Norm. `extensions/` sind optionale Datenfelder und Auswahllisten, die über Vorschläge wachsen. |
| `docs/` | Das Ergebnis, erzeugt aus den Daten. Von Hand gepflegt sind nur der Fliesstext in `docs/norm/` und die Schriften in `docs/fonts/`. Der Ordner kann unverändert von einem Webserver ausgeliefert werden. |
| `tools/` | Die Skripte, die prüfen und erzeugen. |

## Erzeugen

```
pip install -r tools/requirements.txt
python3 tools/validate.py     # prüft die Daten
python3 tools/build.py        # erzeugt alles in docs/
```

Die Versionsnummer steht in `data/VERSION`.

## Mitwirken

Neue Datenfelder und Listenwerte werden über ein Issue vorgeschlagen. Ablauf und Regeln stehen in [CONTRIBUTING.md](CONTRIBUTING.md).
