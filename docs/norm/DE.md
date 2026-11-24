# Einleitung
In Erarbeitung…

# Wiederverwendungs-Audit

<!-- Die Tabellen zwischen GENERIERT:START und GENERIERT:ENDE erzeugt tools/build.py aus data/core/audits/. Dort ändern, nicht hier. Der übrige Text wird von Hand gepflegt. -->
## Zweck und Umfang
Das Wiederverwendungs-Audit dient der Aufnahme von bestehenden Bauteilen, welche von einem Umbau oder Rückbau betroffen sind und für eine Wiederverwendung geprüft werden sollen.

In einem Bericht werden dazu Projekt-, Gebäude und Bauteildaten erfasst. Diese Daten sollen die Grundlage für die Auswahl bilden, welche Bauteile an interne oder externe Abnehmerinnen vermittelt werden sollen.

Bei Bedarf kann eine zweistufige Erfassung gewählt werden. Die Stufe I ist eine Grobeinschätzung dazu, ob die betrachtete Bausubstanz sich für eine Wiederverwendung und damit einer vertieften Aufnahme in Stufe II eignet. Es wird ausserdem eingegrenzt, für welche Bauteilgruppen eine vertiefte Aufnahme in Stufe II empfohlen wird.

Die Stufe II ist eine vertiefte Aufnahme der Bauteile. Sie kann aufbauend auf die Empfehlung in Stufe I oder ohne Vorprüfung gewählt werden. Die Stufe II hat das Ziel, geeignete Bauteile für eine Vermittlung an Abnehmerinnen auszuwählen.
## Betrachtungsebene und Strukturierung
Für die Gliederung des Wiederverwendungs-Audits ist festzulegen, wie das Vorhaben in Projekte, Gebäude und Bauteilkataloge gegliedert wird.

Zunächst sollte der Perimeter der betroffenen Bausubstanz inklusive des umliegenden Aussenraums sowie ggf. Bauetappen möglichst präzise angegeben werden.

Eine Zusammenfassung mehrerer Gebäude zu einem Projekt ist zum Beispiel dann sinnvoll, wenn die Gebäude in einem gemeinsamen Zeitraum rück- oder umgebaut werden und ein gemeinsamer Bauteilkatalog objektübergreifend betrachtet werden kann.

Für jedes Projekt sind die Projektdaten und -beteiligten nach Tabelle X: «Datenfelder Projekt» einmalig zu erfassen.

Für alle Gebäude eines Projekts sind die Gebäudedaten nach Tabelle X: «Datenfelder Quellobjekte» zu erfassen. Bei baugleichen oder verbundenen Gebäuden können diese zusammengefasst und einmalig angegeben werden.

Der Umfang der Erfassung von Bauteildaten unterscheidet sich in Stufe I und II des Wiederverwendungs-Audits und kann den nachfolgenden Abschnitten entnommen werden. Die Gliederung und Betrachtungsebenen der Bauteile werden durch den Swiss Inv nicht vorgegeben.
## Wiederverwendungs-Audit Stufe I: Ziel und Vorgehen
Das Wiederverwendungs-Audit Stufe I dient der überschlägigen Einschätzung des Wiederverwendungspotenzials der Bauteile eines Quellobjekts. Es ermöglicht eine erste Beurteilung, ob und in welchem Umfang eine vertiefte Untersuchung sinnvoll ist. Für eine bedarfsgerechte Aufnahme sollten der Auftragnehmerin vor der Begehung die Ziele der Auftraggeberin sowie das Perimeter der betroffenen Bausubstanz mitgeteilt werden.

Die Potenzialeinschätzung bildet die Grundlage für eine gezielte und bedarfsgerechte Vertiefung der Untersuchung. Dabei sollen insbesondere die für eine vertiefte Untersuchung relevanten Bauteilgruppen eingegrenzt werden.

Nach Abschluss des Audits erhält die Auftraggeberin einen Bericht, der als Entscheidungsgrundlage für folgende Fragen dient:

- Soll für das untersuchte Quellobjekt ein Wiederverwendungs-Audit Stufe II durchgeführt werden?

- Welche Bauteilgruppen sollen im Rahmen des Wiederverwendungs-Audits Stufe II vertieft erfasst und beurteilt werden?

Nach Abschluss des Berichts sollten die Ergebnisse mit den Zielen und Ressourcen der Auftraggeberin abgestimmt werden, um Entscheide für das weitere Vorgehen zu treffen. 
## Wiederverwendungs-Audit Stufe I: Format und Umfang
Das Wiederverwendungs-Audit Stufe I umfasst folgende Abschnitte:

- Projekt: Angaben zum Projekt und zu Projektbeteiligten

- Einleitung: Projektbeschrieb, Ziele, Termine, Perimeter, Grundlagen (z. B. Pläne / Schadstoffbericht) sowie Vorgehen der Auftragnehmerin

- Gebäude: Angaben zu den betrachteten Quellobjekten

- Bauteile: Groberfassung aller Bauteile inklusive der jeweiligen Empfehlung für oder gegen eine vertiefte Aufnahme

- Fazit: Empfehlung für oder gegen ein Wiederverwendungs-Audit Stufe II der betrachteten Quellobjekte inklusive einer Begründung

Das Format der Abgabe ist zwischen Auftraggeberin und Auftragnehmerin abzustimmen. Empfohlen wird eine Abgabe des gesamten Berichts als PDF.

Die Projekt- und Gebäudedaten sind gem. Abschnitt „Betrachtungsebene und Strukturierung“ zu erfassen.

Für Projekt und Quellobjekte sind mindestens die Informationen der folgenden Tabelle zu erfassen.

<!-- GENERIERT:START profil=stage-1 bereich=projekt -->
**Tabelle: Zu erfassende Informationen zu Projekt und Quellobjekten im Wiederverwendungs-Audit Stufe I**

| Information | Verpflichtung | Datenfeld | Key | Format |
| --- | --- | --- | --- | --- |
| Projektname | Muss | Projektname | `projectName` | Freitext (einzeilig) |
| Eigentümerin, Auftraggeberin und Auftragnehmerin | Muss | Eigentümerin | `projectOwner` | Kontakt |
|  |  | Auftraggeberin | `projectAuditClient` | Kontakt |
|  |  | Auftragnehmerin | `projectAuditor` | Kontakt |
| Adresse des Quellobjekts | Muss | Strasse | `donorBuildingStreet` | Freitext (einzeilig) |
|  |  | Hausnummer | `donorBuildingHouseNumber` | Freitext (einzeilig) |
|  |  | Postleitzahl | `donorBuildingPostalCode` | Postleitzahl |
|  |  | Ort | `donorBuildingCity` | Freitext (einzeilig) |
| Land des Quellobjekts | Sollte | Land | `donorBuildingCountry` | Ländercode nach ISO 3166 |
| Gebäudedaten nach GWR und Bauweise | Sollte | Gebäudeklasse | `donorBuildingGklas` | Auswahlliste |
|  |  | Gebäudekategorie | `donorBuildingGkat` | Auswahlliste |
|  |  | Bauperiode | `donorBuildingGbaup` | Auswahlliste |
|  |  | Bauweise | `donorBuildingConstructionType` | Auswahlliste |
|  |  | Baujahr des Gebäudes | `donorBuildingGbauj` | JJJJ |
|  |  | Gebäudevolumen | `donorBuildingGvol` | Zahlenwert [m³] |
|  |  | Gebäudefläche | `donorBuildingGarea` | Zahlenwert [m²] |
|  |  | Anzahl Geschosse | `donorBuildingGastw` | Zahlenwert |
<!-- GENERIERT:ENDE -->

Für jedes Bauteil sind mindestens die Informationen zu erfassen, welche in Tabelle X: «Zu erfassende Informationen pro Bauteil im Wiederverwendungs-Audit Stufe I» in der Spalte «Verpflichtung» als «Muss» ausgewiesen sind. In der Spalte «Datenfelder» werden geeignete Datenfelder aus der Tabelle Y: «Datenfelder Re-Use-Bauteile» empfohlen, die für die Angaben der Informationen genutzt werden sollten.

Die **Mengenangabe** der Bauteile kann überschlägig als Bereich angegeben werden. Um die Maschinenlesbarkeit der unteren und oberen Bereichsgrenzen zu gewährleisten, müssen die Datenfelder Menge (min) und Menge (max) als Zahlenwerte angegeben werden. Eine geprüfte Mengenangabe kann ausgewiesen werden, indem dieselbe Menge in beide Datenfelder eingetragen wird.

Eine **Bewertung der Schadstoffbelastung** für die Wiederverwendung ist nicht Teil der Mindestanforderungen an Wiederverwendungs-Audits Stufe I.

**Weitere** **Eigenschaften** der Bauteile sollen als Text im Datenfeld «Weitere Informationen» oder in geeigneten sonstigen Datenfeldern erfasst werden. Für einen optimierten Datenaustausch sind hierfür standardisierte Datenfelder aus der Tabelle Y: «Datenfelder Re-Use-Bauteile» zu bevorzugen.

<!-- GENERIERT:START profil=stage-1 bereich=bauteile -->
**Tabelle: Zu erfassende Informationen pro Bauteil im Wiederverwendungs-Audit Stufe I**

| Information | Verpflichtung | Datenfeld | Key | Format |
| --- | --- | --- | --- | --- |
| Kurze Bezeichnung | Muss | Bezeichnung | `name` | Freitext (einzeilig) |
| eBKP-H | Muss | eBKP-H Code | `ebkphCode` | Auswahlliste |
|  |  | eBKP-H Bezeichnung | `ebkphLabel` | Freitext (einzeilig) |
| Menge, ggf. überschlägig inkl. Ausweisung der Ungenauigkeit | Muss | Menge (min) | `quantityMin` | Zahlenwert |
|  |  | Menge (max) | `quantityMax` | Zahlenwert |
|  |  | Einheit | `unit` | Auswahlliste |
| Mindestens eine Materialkategorie | Muss | Materialkategorie | `material` | Auswahlliste (Mehrfachauswahl) |
| Weitere Informationen | Sollte | Weitere Informationen | `description` | Freitext (mehrzeilig) |
| Empfehlung für oder gegen eine vertiefte Aufnahme | Muss | Empfehlung Detailaufnahme | `recDetailedAssessment` | Auswahlliste |
<!-- GENERIERT:ENDE -->

Ausführungen zu Definitionen und Formatierungen der Datenfelder sind dem [Datenfeldverzeichnis](../dictionary/DE.md) zu entnehmen.

## Wiederverwendungs-Audit Stufe II: Ziel und Vorgehen
Das Wiederverwendungs-Audit Stufe II dient der Vorbereitung für eine Vermittlung der Bauteile an interne oder externe Abnehmerinnen. Für eine bedarfsgerechte Aufnahme sollten der Auftragnehmerin vor der Begehung die Ziele der Auftraggeberin sowie das Perimeter der betroffenen Bausubstanz mitgeteilt werden.

Nach Abschluss des Audits erhält die Auftraggeberin einen Bericht, anhand welchem ausgewählt werden kann, welche Bauteile für eine Vermittlung sichtbar gemacht werden sollen. 

Die erfassten Informationen sollen dabei mindestens für eine informelle Bedarfsabklärung bei potenziellen Abnehmerinnen weiterverwendet werden können. Abhängig von den Vermittlungsstrategien und -kanälen können ergänzende Detailabklärungen zu Bauteilen anfallen.

Die Erarbeitung der Vermittlungsstrategien, die Verwaltung der Vermittlungskanäle sowie ergänzende Abklärungen für die Vermittlung sind nicht Teil des Wiederverwendungs-Audits Stufe II. Diese aufbauenden Dienstleistungen sind nicht durch den Swiss Inv standardisiert.

Nach Abschluss des Berichts sollten die Ergebnisse mit den Zielen und Ressourcen der Auftraggeberin abgestimmt werden, um Entscheide für das weitere Vorgehen zu treffen.
## Wiederverwendungs-Audit Stufe II: Format und Umfang
Das Wiederverwendungs-Audit Stufe II umfasst folgende Abschnitte:

- Projekt: Angaben zum Projekt und zu Projektbeteiligten

- Einleitung: Projektbeschrieb, Ziele, Termine, Perimeter, Grundlagen (z. B. Pläne / Schadstoffbericht) sowie Vorgehen der Auftragnehmerin

- Gebäude: Angaben zu den betrachteten Quellobjekten

- Bauteile: Vertiefte Aufnahme aller Bauteile inklusive der jeweiligen Empfehlung für oder gegen eine Vermittlung

- Fazit: Zusammenfassung der Ergebnisse

Das Format der Abgabe ist zwischen Auftraggeberin und Auftragnehmerin abzustimmen. Empfohlen wird eine Abgabe des gesamten Berichts als PDF, ein tabellarisches Datenformat der erfassten Bauteile und die Bilddateien zu Gebäuden und Bauteilen.

Die Projekt- und Gebäudedaten sind gem. Abschnitt «Betrachtungsebene und Strukturierung» zu erfassen.

Für Projekt und Quellobjekte sind mindestens die Informationen der folgenden Tabelle zu erfassen.

<!-- GENERIERT:START profil=stage-2 bereich=projekt -->
**Tabelle: Zu erfassende Informationen zu Projekt und Quellobjekten im Wiederverwendungs-Audit Stufe II**

| Information | Verpflichtung | Datenfeld | Key | Format |
| --- | --- | --- | --- | --- |
| Projektname | Muss | Projektname | `projectName` | Freitext (einzeilig) |
| Eigentümerin, Auftraggeberin und Auftragnehmerin | Muss | Eigentümerin | `projectOwner` | Kontakt |
|  |  | Auftraggeberin | `projectAuditClient` | Kontakt |
|  |  | Auftragnehmerin | `projectAuditor` | Kontakt |
| Adresse des Quellobjekts | Muss | Strasse | `donorBuildingStreet` | Freitext (einzeilig) |
|  |  | Hausnummer | `donorBuildingHouseNumber` | Freitext (einzeilig) |
|  |  | Postleitzahl | `donorBuildingPostalCode` | Postleitzahl |
|  |  | Ort | `donorBuildingCity` | Freitext (einzeilig) |
| Land des Quellobjekts | Sollte | Land | `donorBuildingCountry` | Ländercode nach ISO 3166 |
| Gebäudedaten nach GWR und Bauweise | Sollte | Gebäudeklasse | `donorBuildingGklas` | Auswahlliste |
|  |  | Gebäudekategorie | `donorBuildingGkat` | Auswahlliste |
|  |  | Bauperiode | `donorBuildingGbaup` | Auswahlliste |
|  |  | Bauweise | `donorBuildingConstructionType` | Auswahlliste |
|  |  | Baujahr des Gebäudes | `donorBuildingGbauj` | JJJJ |
|  |  | Gebäudevolumen | `donorBuildingGvol` | Zahlenwert [m³] |
|  |  | Gebäudefläche | `donorBuildingGarea` | Zahlenwert [m²] |
|  |  | Anzahl Geschosse | `donorBuildingGastw` | Zahlenwert |
| EGID und EGRID | Muss | EGID | `donorBuildingEgid` | Freitext (einzeilig) |
|  |  | EGRID | `donorBuildingEgrid` | Freitext (einzeilig) |
| Erschliessung | Muss | Erschliessung | `donorBuildingAccess` | Freitext (mehrzeilig) |
<!-- GENERIERT:ENDE -->

Für jedes Bauteil sind mindestens die Informationen zu erfassen, welche in Tabelle X: «Zu erfassende Informationen pro Bauteil im Wiederverwendungs-Audit Stufe II» in der Spalte «Verpflichtung» als «Muss» ausgewiesen sind. In der Spalte «Datenfelder» werden geeignete Datenfelder aus der Tabelle Y: «Datenfelder Re-Use-Bauteile» empfohlen, die für die Angaben der Informationen genutzt werden sollten.

Die **Mengenangabe** der Bauteile soll präzise angegeben werden. Eine geprüfte Mengenangabe kann ausgewiesen werden, indem in Menge (min) und Menge (max) derselbe Wert angegeben wird.

Eine **Bewertung der Schadstoffbelastung** für die Wiederverwendung ist nicht Teil der Mindestanforderungen an Wiederverwendungs-Audits Stufe II. Die Auftragnehmerin muss im Datenfeld «Schadstoffgutachten» angeben, ob für das betroffene Bauteil eine Beurteilung der Schadstoffbelastung durch ein Schadstoffgutachten vorliegt. Weiterführende Angaben zur Verfasserin und zum Datum des Schadstoffgutachtens sowie zur Art und zum Grad der Schadstoffbelastung sind optional. Die Auswirkungen einer Schadstoffbeurteilung für die Wiederverwendung des Bauteils dürfen nur durch Schadstofffachpersonen interpretiert werden.

Zu jedem Bauteil muss mindestens ein **Titelfoto** hinterlegt werden. Zusätzlich sollten mindestens zwei weitere Fotos erstellt werden, welche hilfreiche Informationen zu Details oder Übersichten ergänzen. Eine Zuordnung der Fotos oder weiteren Anhänge zu den betroffenen Bauteilen sollte durch eine geeignete Dateibeschriftung gewährleistet sein.

Neben den Pflichtfeldern können **weitere Eigenschaften** in geeigneten zusätzlichen Datenfeldern erfasst werden. Für einen optimierten Datenaustausch sind hierfür standardisierte Datenfelder aus der Tabelle Y: «Datenfelder Re-Use-Bauteile» zu bevorzugen.

<!-- GENERIERT:START profil=stage-2 bereich=bauteile -->
**Tabelle: Zu erfassende Informationen pro Bauteil im Wiederverwendungs-Audit Stufe II**

| Information | Verpflichtung | Datenfeld | Key | Format |
| --- | --- | --- | --- | --- |
| Kurze Bezeichnung | Muss | Bezeichnung | `name` | Freitext (einzeilig) |
| Bauteil-ID | Muss | Bauteil-ID | `componentId` | Freitext (einzeilig) |
| eBKP-H | Muss | eBKP-H Code | `ebkphCode` | Auswahlliste |
|  |  | eBKP-H Bezeichnung | `ebkphLabel` | Freitext (einzeilig) |
| Verortung im Quellobjekt | Sollte | Verortung im Quellobjekt | `positionInDonorBuilding` | Freitext (mehrzeilig) |
| Präzise Mengenangabe | Muss | Menge (min) | `quantityMin` | Zahlenwert |
|  |  | Menge (max) | `quantityMax` | Zahlenwert |
|  |  | Einheit | `unit` | Auswahlliste |
| Aussenmasse des Bauteils oder relevante kategoriespezifische Dimensionen | Muss | Aussenmass Höhe | `zDim` | Zahlenwert [cm] |
|  |  | Aussenmass Breite | `yDim` | Zahlenwert [cm] |
|  |  | Aussenmass Tiefe / Länge | `xDim` | Zahlenwert [cm] |
|  |  | Freie Dimensionsangaben | `dimensionNotes` | Freitext (mehrzeilig) |
| Mindestens eine Materialkategorie | Muss | Materialkategorie | `material` | Auswahlliste (Mehrfachauswahl) |
| Weitere Materialangaben | Muss | Zusatzinformation Material | `materialNotes` | Freitext (mehrzeilig) |
| Weitere Informationen | Sollte | Weitere Informationen | `description` | Freitext (mehrzeilig) |
| Verweis auf Schadstoffgutachten | Muss | Schadstoffgutachten | `pollutantReport` | Auswahlliste |
| Bewertung des Zustands | Muss | Visueller Zustand | `visualCondition` | Auswahlliste |
|  |  | Funktionaler Zustand | `functionalCondition` | Auswahlliste |
| Einschätzung des Demontageaufwands | Muss | Demontageaufwand | `demountability` | Auswahlliste |
| Empfehlung für oder gegen eine Vermittlung | Muss | Empfehlung Vermittlung | `recDistribution` | Auswahlliste |
| Begründung der Empfehlung | Sollte | Erläuterung der Empfehlung | `recNotes` | Freitext (mehrzeilig) |
| Titelfoto des Bauteils | Muss | Bilddateien und andere Anhänge sind nicht im tabellarischen Datenformat enthalten, sondern separat abzugeben |  |  |
| Mindestens zwei weitere Übersichts- oder Detailfotos | Sollte | Bilddateien und andere Anhänge sind nicht im tabellarischen Datenformat enthalten, sondern separat abzugeben |  |  |
<!-- GENERIERT:ENDE -->

Ausführungen zu Definitionen und Formatierungen der Datenfelder sind dem [Datenfeldverzeichnis](../dictionary/DE.md) zu entnehmen.


# Anforderungen an digitale Schnittstellen
In Erarbeitung…
