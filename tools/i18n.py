"""Texte der Oberfläche (Überschriften, Hinweise) in den vier Sprachen.

Bezeichnungen von Formaten, Verpflichtungen und Audit-Stufen stehen nicht hier,
sondern in data/core/vocabulary.yaml und data/core/audits/. apply() übernimmt sie.
"""

T = {
    "de": {
        "name": "Deutsch",
        "n_caption_component": "Tabelle: Zu erfassende Informationen pro Bauteil im {title}", "n_caption_project": "Tabelle: Zu erfassende Informationen zu Projekt und Quellobjekten im {title}", "n_information": "Information", "n_unresolved": "Datenfeld noch nicht festgelegt", "n_attachment": "Bilddateien und andere Anhänge sind nicht im tabellarischen Datenformat enthalten, sondern separat abzugeben", "h_formats": "Formate", "h_units": "Einheiten", "h_obligations": "Verpflichtung", "symbol": "Zeichen", "title": "Datenfeldverzeichnis Swiss Inv", "version": "Version",
        "intro": "**Kern** = stabil, ändert nur mit einer neuen Normausgabe. **Erweiterung** = optionale Datenfelder, die über Vorschläge wachsen.",
        "intro_site": "Diese Seite zeigt alle Datenfelder des Swiss Inv: was zu einem wiederverwendbaren Bauteil, seinem Quellobjekt und dem Projekt erfasst wird, in welchem Format und in welcher Audit-Stufe.",
        "fields_of": "Datenfelder", "field": "Datenfeld", "key": "Key", "format": "Format", "layer": "Ebene",
        "definition": "Definition", "group": "Gruppe",
        "label": "Bezeichnung", "lists": "Auswahllisten", "values": "Werte", "general": "Allgemein",
        "layers": {"core": "Kern", "extension": "Erweiterung"},
        "search": "Datenfeld, Key oder Definition suchen …", "all_layers": "Alle Ebenen", "all_fields": "Alle Datenfelder",
        "count": "{n} von {total} Datenfeldern",
        "none": "Keine Datenfelder gefunden.", "language": "Sprache",
    },
    "fr": {
        "name": "Français",
        "n_caption_component": "Tableau: informations à saisir par élément dans l'{title}", "n_caption_project": "Tableau: informations à saisir sur le projet et les bâtiments sources dans l'{title}", "n_information": "Information", "n_unresolved": "Champ pas encore défini", "n_attachment": "Les fichiers d'images et autres annexes ne figurent pas dans le format de données tabulaire; ils sont à remettre séparément", "h_formats": "Formats", "h_units": "Unités", "h_obligations": "Obligation", "symbol": "Symbole", "title": "Répertoire des champs de données Swiss Inv", "version": "Version",
        "intro": "**Noyau** = stable, ne change qu'avec une nouvelle édition de la norme. **Extension** = champs facultatifs qui s'étoffent au fil des propositions.",
        "intro_site": "Cette page présente tous les champs de données du Swiss Inv: ce qui est saisi pour un élément réemployable, son bâtiment source et le projet, dans quel format et à quel niveau d'audit.",
        "fields_of": "Champs de données", "field": "Champ", "key": "Clé", "format": "Format", "layer": "Niveau",
        "definition": "Définition", "group": "Groupe",
        "label": "Désignation", "lists": "Listes de sélection", "values": "valeurs", "general": "Général",
        "layers": {"core": "Noyau", "extension": "Extension"},
        "search": "Rechercher un champ, une clé ou une définition …", "all_layers": "Tous les niveaux", "all_fields": "Tous les champs",
        "count": "{n} champs sur {total}",
        "none": "Aucun champ trouvé.", "language": "Langue",
    },
    "it": {
        "name": "Italiano",
        "n_caption_component": "Tabella: informazioni da rilevare per componente nell'{title}", "n_caption_project": "Tabella: informazioni da rilevare su progetto ed edifici di origine nell'{title}", "n_information": "Informazione", "n_unresolved": "Campo non ancora definito", "n_attachment": "I file immagine e gli altri allegati non sono contenuti nel formato di dati tabellare; vanno consegnati separatamente", "h_formats": "Formati", "h_units": "Unità", "h_obligations": "Obbligo", "symbol": "Simbolo", "title": "Repertorio dei campi di dati Swiss Inv", "version": "Versione",
        "intro": "**Nucleo** = stabile, cambia solo con una nuova edizione della norma. **Estensione** = campi facoltativi che crescono tramite proposte.",
        "intro_site": "Questa pagina mostra tutti i campi di dati dello Swiss Inv: che cosa viene rilevato per un componente riutilizzabile, il suo edificio di origine e il progetto, in quale formato e a quale livello di audit.",
        "fields_of": "Campi di dati", "field": "Campo", "key": "Chiave", "format": "Formato", "layer": "Livello",
        "definition": "Definizione", "group": "Gruppo",
        "label": "Denominazione", "lists": "Elenchi di selezione", "values": "valori", "general": "Generale",
        "layers": {"core": "Nucleo", "extension": "Estensione"},
        "search": "Cercare campo, chiave o definizione …", "all_layers": "Tutti i livelli", "all_fields": "Tutti i campi",
        "count": "{n} campi su {total}",
        "none": "Nessun campo trovato.", "language": "Lingua",
    },
    "en": {
        "name": "English",
        "n_caption_component": "Table: information to be recorded per component in the {title}", "n_caption_project": "Table: information to be recorded on project and donor buildings in the {title}", "n_information": "Information", "n_unresolved": "Data field not yet defined", "n_attachment": "Image files and other attachments are not part of the tabular data format; they are delivered separately", "h_formats": "Formats", "h_units": "Units", "h_obligations": "Obligation", "symbol": "Symbol", "title": "Swiss Inv data dictionary", "version": "Version",
        "intro": "**Core** = stable, changes only with a new edition of the standard. **Extension** = optional data fields that grow through proposals.",
        "intro_site": "This page shows all Swiss Inv data fields: what is recorded for a reusable building component, its donor building and the project, in which format and at which audit stage.",
        "fields_of": "Data fields", "field": "Data field", "key": "Key", "format": "Format", "layer": "Layer",
        "definition": "Definition", "group": "Group",
        "label": "Label", "lists": "Code lists", "values": "values", "general": "General",
        "layers": {"core": "Core", "extension": "Extension"},
        "search": "Search data field, key or definition …", "all_layers": "All layers", "all_fields": "All data fields",
        "count": "{n} of {total} data fields",
        "none": "No data fields found.", "language": "Language",
    },
}

# Texte der Website (docs/index.html)
SITE = {
    "de": {
        "dl_excel": "Excel-Vorlage (XLSX)", "ex_title": "Beispiel-Bauteil", "ex_hint": "Datenfeld anklicken, um die Definition zu sehen.", "ex_img": "Strichzeichnung eines zweiflügligen Fensters",
        "eyebrow": "Datenstandard für die Wiederverwendung von Bauteilen", "draft": "Entwurf", "nav_downloads": "Downloads",
                "sec_fields": "Alle Datenfelder, filterbar",         "f_all": "Alle", "f_audit": "Audit", "f_search": "Suche", "search_ph": "z. B. Material, Zustand, Datum",
        "none_long": "Kein Datenfeld passt zu dieser Auswahl. Filter zurücksetzen oder die Suche anpassen.",
        "d_not_required": "In keiner Audit-Stufe verlangt", "d_list": "Auswahlliste",         "d_details": "Details zum Datenfeld",                 "no_values": "Für diese Liste sind im Swiss Inv keine eigenen Werte hinterlegt.",
        "sec_dl": "Daten herunterladen", "dl_tables": "Excel-Vorlage", "dl_tables_text": "Die Excel-Erfassungsvorlage. Sie enthält auch alle Datenfelder und Auswahllisten.",
        "dl_software": "Für Software", "dl_software_text": "Ein JSON Schema für Bauteil-Datensätze.",
        "dl_contrib": "Mitwirken", "dl_contrib_text": "Swiss Inv wird auf GitHub gepflegt. Dort lassen sich neue Datenfelder und Listenwerte vorschlagen und Fehler melden.",
        "dl_schema": "JSON Schema",
        "dl_repo": "GitHub", "footer": "Erzeugt aus dem Datenfeldverzeichnis Swiss Inv",
    },
    "fr": {
        "dl_excel": "Modèle Excel (XLSX)", "ex_title": "Exemple d'élément", "ex_hint": "Cliquer sur un champ pour voir sa définition.", "ex_img": "Dessin au trait d'une fenêtre à deux vantaux",
        "eyebrow": "Standard de données pour le réemploi d'éléments de construction", "draft": "Projet", "nav_downloads": "Téléchargements",
                "sec_fields": "Tous les champs, avec filtres",         "f_all": "Tous", "f_audit": "Audit", "f_search": "Recherche", "search_ph": "p. ex. matériau, état, date",
        "none_long": "Aucun champ ne correspond à cette sélection. Réinitialiser les filtres ou adapter la recherche.",
        "d_not_required": "Exigé dans aucun niveau d'audit", "d_list": "Liste de sélection",         "d_details": "Détails du champ",                 "no_values": "Le Swiss Inv ne contient pas de valeurs propres pour cette liste.",
        "sec_dl": "Télécharger les données", "dl_tables": "Modèle Excel", "dl_tables_text": "Le modèle de saisie Excel. Il contient aussi tous les champs et toutes les listes de sélection.",
        "dl_software": "Pour les logiciels", "dl_software_text": "Un schéma JSON pour les jeux de données d'éléments.",
        "dl_contrib": "Contribuer", "dl_contrib_text": "Swiss Inv est maintenu sur GitHub. On peut y proposer de nouveaux champs et de nouvelles valeurs de liste et y signaler des erreurs.",
        "dl_schema": "Schéma JSON",
        "dl_repo": "GitHub", "footer": "Généré à partir du répertoire des champs de données Swiss Inv",
    },
    "it": {
        "dl_excel": "Modello Excel (XLSX)", "ex_title": "Componente di esempio", "ex_hint": "Fare clic su un campo per vederne la definizione.", "ex_img": "Disegno al tratto di una finestra a due ante",
        "eyebrow": "Standard di dati per il riuso di componenti edilizi", "draft": "Bozza", "nav_downloads": "Download",
                "sec_fields": "Tutti i campi, con filtri",         "f_all": "Tutti", "f_audit": "Audit", "f_search": "Ricerca", "search_ph": "ad es. materiale, stato, data",
        "none_long": "Nessun campo corrisponde a questa selezione. Reimpostare i filtri o modificare la ricerca.",
        "d_not_required": "Non richiesto in alcun livello di audit", "d_list": "Elenco di selezione",         "d_details": "Dettagli del campo",                 "no_values": "Lo Swiss Inv non contiene valori propri per questo elenco.",
        "sec_dl": "Scaricare i dati", "dl_tables": "Modello Excel", "dl_tables_text": "Il modello di rilevamento Excel. Contiene anche tutti i campi e gli elenchi di selezione.",
        "dl_software": "Per il software", "dl_software_text": "Uno schema JSON per i record dei componenti.",
        "dl_contrib": "Contribuire", "dl_contrib_text": "Swiss Inv è gestito su GitHub. Lì si possono proporre nuovi campi e nuovi valori di elenco e segnalare errori.",
        "dl_schema": "Schema JSON",
        "dl_repo": "GitHub", "footer": "Generato dal repertorio dei campi di dati Swiss Inv",
    },
    "en": {
        "dl_excel": "Excel template (XLSX)", "ex_title": "Example component", "ex_hint": "Click a data field to see its definition.", "ex_img": "Line drawing of a two-sash window",
        "eyebrow": "Data standard for the reuse of building components", "draft": "Draft", "nav_downloads": "Downloads",
                "sec_fields": "All data fields, filterable",         "f_all": "All", "f_audit": "Audit", "f_search": "Search", "search_ph": "e.g. material, condition, date",
        "none_long": "No data field matches this selection. Reset the filters or change the search.",
        "d_not_required": "Not required in any audit stage", "d_list": "Code list",         "d_details": "Data field details",                 "no_values": "Swiss Inv holds no values of its own for this list.",
        "sec_dl": "Download the data", "dl_tables": "Excel template", "dl_tables_text": "The Excel capture template. It also contains all data fields and code lists.",
        "dl_software": "For software", "dl_software_text": "A JSON Schema for component records.",
        "dl_contrib": "Contribute", "dl_contrib_text": "Swiss Inv is maintained on GitHub. There you can propose new data fields and list values and report errors.",
        "dl_schema": "JSON Schema",
        "dl_repo": "GitHub", "footer": "Generated from the Swiss Inv data dictionary",
    },
}
for _lang in T:
    T[_lang].update(SITE[_lang])

# Texte der Excel-Vorlage (docs/excel/<SPRACHE>.xlsx). Blattnamen: höchstens 31 Zeichen, ohne ' : \ / ? * [ ]
XL = {
    "de": {
        "sheets": {"guide": "Anleitung", "project": "Projekt", "all": "Bauteile alle Felder", "fields": "Datenfelder", "lists": "Auswahllisten"},
        "guide_title": "Swiss Inv – Erfassungsvorlage",
        "guide": [
            "Diese Vorlage wurde automatisch aus dem Datenfeldverzeichnis Swiss Inv erzeugt (Version {v}).",
            "Blatt «Projekt»: Angaben zum Projekt, zu den Beteiligten und zu den Quellobjekten.",
            "Blätter {p}: pro Bauteil eine Zeile. Die Spalten entsprechen dem Mindestumfang der jeweiligen Audit-Stufe. Angaben aus einem früheren Blatt erscheinen in den folgenden Blättern automatisch in derselben Zeile (erste 300 Zeilen); dort nur ergänzen.",
            "Blatt «Bauteile alle Felder»: alle Datenfelder inklusive der optionalen Erweiterungen, zum Beispiel für die Vermittlung.",
            "Fehlt in einer begonnenen Zeile eine Muss-Angabe, wird die Zelle farbig markiert.",
            "Datenfelder mit Auswahlliste bieten die Werte aus dem Blatt «Auswahllisten» an. Die Definition eines Datenfelds erscheint als Notiz am Spaltenkopf.",
            "Die technischen Namen (Keys) der Datenfelder stehen im Blatt «Datenfelder».",
            "Fotos und andere Anhänge sind separat abzugeben; in der Tabelle wird nur der Dateiname eingetragen.",
        ],
        "legend": "Legende", "must": "Muss", "should": "Sollte", "optional": "Optional", "missing": "Muss-Angabe fehlt",
        "role": "Rolle", "multi": "Mehrere Werte mit ; trennen", "file": "Dateiname", "entity": "Bereich", "list": "Auswahlliste", "unit": "Einheit",
    },
    "fr": {
        "sheets": {"guide": "Guide", "project": "Projet", "all": "Elements tous les champs", "fields": "Champs", "lists": "Listes"},
        "guide_title": "Swiss Inv – Modèle de saisie",
        "guide": [
            "Ce modèle a été généré automatiquement à partir du répertoire des champs de données Swiss Inv (version {v}).",
            "Feuille «Projet»: indications sur le projet, les intervenants et les bâtiments sources.",
            "Feuilles {p}: une ligne par élément. Les colonnes correspondent au contenu minimal du niveau d'audit concerné. Les indications d'une feuille précédente apparaissent automatiquement à la même ligne dans les feuilles suivantes (300 premières lignes); il suffit de les y compléter.",
            "Feuille «Elements tous les champs»: tous les champs, y compris les extensions facultatives, par exemple pour le placement.",
            "Si une indication obligatoire manque dans une ligne commencée, la cellule est mise en couleur.",
            "Les champs avec liste de sélection proposent les valeurs de la feuille «Listes». La définition d'un champ apparaît en note sur l'en-tête de colonne.",
            "Les noms techniques (clés) des champs figurent dans la feuille «Champs».",
            "Les photos et autres annexes sont à remettre séparément; seul le nom du fichier est saisi dans le tableau.",
        ],
        "legend": "Légende", "must": "Obligatoire", "should": "Recommandé", "optional": "Facultatif", "missing": "Indication obligatoire manquante",
        "role": "Rôle", "multi": "Séparer plusieurs valeurs par ;", "file": "Nom du fichier", "entity": "Domaine", "list": "Liste de sélection", "unit": "Unité",
    },
    "it": {
        "sheets": {"guide": "Guida", "project": "Progetto", "all": "Componenti tutti i campi", "fields": "Campi", "lists": "Elenchi"},
        "guide_title": "Swiss Inv – Modello di rilevamento",
        "guide": [
            "Questo modello è stato generato automaticamente dal repertorio dei campi di dati Swiss Inv (versione {v}).",
            "Foglio «Progetto»: indicazioni sul progetto, sui partecipanti e sugli edifici di origine.",
            "Fogli {p}: una riga per componente. Le colonne corrispondono al contenuto minimo del rispettivo livello di audit. Le indicazioni di un foglio precedente compaiono automaticamente nella stessa riga dei fogli successivi (prime 300 righe); lì basta completarle.",
            "Foglio «Componenti tutti i campi»: tutti i campi, comprese le estensioni facoltative, ad esempio per il collocamento.",
            "Se in una riga iniziata manca un'indicazione obbligatoria, la cella viene evidenziata a colori.",
            "I campi con elenco di selezione propongono i valori del foglio «Elenchi». La definizione di un campo appare come nota nell'intestazione di colonna.",
            "I nomi tecnici (chiavi) dei campi si trovano nel foglio «Campi».",
            "Foto e altri allegati vanno consegnati separatamente; nella tabella si inserisce solo il nome del file.",
        ],
        "legend": "Legenda", "must": "Obbligatorio", "should": "Raccomandato", "optional": "Facoltativo", "missing": "Indicazione obbligatoria mancante",
        "role": "Ruolo", "multi": "Separare più valori con ;", "file": "Nome del file", "entity": "Ambito", "list": "Elenco di selezione", "unit": "Unità",
    },
    "en": {
        "sheets": {"guide": "Guide", "project": "Project", "all": "Components all fields", "fields": "Data fields", "lists": "Code lists"},
        "guide_title": "Swiss Inv – capture template",
        "guide": [
            "This template was generated automatically from the Swiss Inv data dictionary (version {v}).",
            "Sheet «Project»: details of the project, the participants and the donor buildings.",
            "Sheets {p}: one row per component. The columns match the minimum content of the respective audit stage. Values from an earlier sheet appear automatically in the same row of the following sheets (first 300 rows); only add to them there.",
            "Sheet «Components all fields»: all data fields including the optional extensions, for example for placement.",
            "If a required value is missing in a row that has been started, the cell is highlighted.",
            "Data fields with a code list offer the values from the sheet «Code lists». The definition of a data field appears as a note on the column header.",
            "The technical names (keys) of the data fields are listed in the sheet «Data fields».",
            "Photos and other attachments are delivered separately; only the file name is entered in the table.",
        ],
        "legend": "Legend", "must": "Must", "should": "Should", "optional": "Optional", "missing": "Required value missing",
        "role": "Role", "multi": "Separate several values with ;", "file": "File name", "entity": "Area", "list": "Code list", "unit": "Unit",
    },
}


def apply(data):
    """Übernimmt die Bezeichnungen aus dem Datenfeldverzeichnis in T (einmal pro Build)."""
    for lang in T:
        fm = {k: v["label"][lang] for k, v in data["formats"].items()}
        fm.update({k + "_multi": v["label_multiple"][lang] for k, v in data["formats"].items() if v.get("label_multiple")})
        T[lang]["formats"] = fm
        T[lang]["obligations"] = {k: v["label"][lang] for k, v in data["obligations"].items()}
    return T
