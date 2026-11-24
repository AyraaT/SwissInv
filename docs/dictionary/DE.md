<!-- Automatisch erzeugt von tools/build.py - nicht von Hand bearbeiten. -->

# Datenfeldverzeichnis Swiss Inv

**Deutsch** · [Français](FR.md) · [Italiano](IT.md) · [English](EN.md)

Version: `2.0.0-draft`

**Kern** = stabil, ändert nur mit einer neuen Normausgabe. **Erweiterung** = optionale Datenfelder, die über Vorschläge wachsen.

## Datenfelder Projekt

### Identifikation

| Datenfeld | Key | Format | Ebene | Stufe I | Stufe II | Definition |
| --- | --- | --- | --- | --- | --- | --- |
| Projektname | `projectName` | Freitext (einzeilig) | Kern | Muss | Muss | Bezeichnung des Projekts, unter dem ein oder mehrere Quellobjekte zusammengefasst werden |
| Projekt-ID | `projectId` | Freitext (einzeilig) | Kern |  |  | Kennung des Projekts; Format und Vergabe der ID sind durch den Swiss Inv nicht vorgegeben |

### Projektbeteiligte

| Datenfeld | Key | Format | Ebene | Stufe I | Stufe II | Definition |
| --- | --- | --- | --- | --- | --- | --- |
| Eigentümerin | `projectOwner` | Kontakt | Kern | Muss | Muss | Eigentümerin der betroffenen Quellobjekte |
| Planerin | `projectPlanner` | Kontakt | Kern |  |  | Planerin des Um- oder Rückbaus |
| Auftraggeberin | `projectAuditClient` | Kontakt | Kern | Muss | Muss | Auftraggeberin des Wiederverwendungs-Audits |
| Auftragnehmerin | `projectAuditor` | Kontakt | Kern | Muss | Muss | Auftragnehmerin, die das Wiederverwendungs-Audit durchführt |

## Datenfelder Kontakte

### Ansprechperson

| Datenfeld | Key | Format | Ebene | Definition |
| --- | --- | --- | --- | --- |
| Name | `contactName` | Freitext (einzeilig) | Kern | Vor- und Nachname der Ansprechperson |
| Projektrolle | `contactRole` | Freitext (einzeilig) | Kern | Rolle oder Funktion der Ansprechperson im Projekt |

### Adresse

| Datenfeld | Key | Format | Ebene | Definition |
| --- | --- | --- | --- | --- |
| Unternehmen | `contactCompany` | Freitext (mehrzeilig) | Kern | Name des Unternehmens oder der Organisation |
| Strasse | `contactStreet` | Freitext (einzeilig) | Kern | Strassenname der Adresse der Ansprechperson |
| Hausnummer | `contactHouseNumber` | Freitext (einzeilig) | Kern | Hausnummer der Adresse der Ansprechperson |
| Postleitzahl | `contactPostalCode` | Postleitzahl | Kern | Postleitzahl der Adresse der Ansprechperson |
| Ort | `contactCity` | Freitext (einzeilig) | Kern | Ortschaft der Adresse der Ansprechperson |
| Land | `contactCountry` | Ländercode nach ISO 3166 | Kern | Land der Adresse der Ansprechperson als zweistelliger Ländercode nach ISO 3166-1 (z. B. CH) |

### Kontaktinformation

| Datenfeld | Key | Format | Ebene | Definition |
| --- | --- | --- | --- | --- |
| Telefon | `contactPhone` | Telefonnummer | Kern | Telefonnummer der Ansprechperson, möglichst im internationalen Format mit Ländervorwahl |
| E-Mail | `contactEmail` | E-Mail-Adresse | Kern | E-Mail-Adresse der Ansprechperson |

## Datenfelder Quellobjekte

### Adresse

| Datenfeld | Key | Format | Ebene | Stufe I | Stufe II | Definition |
| --- | --- | --- | --- | --- | --- | --- |
| EGID | `donorBuildingEgid` | Freitext (einzeilig) | Kern |  | Muss | Eidgenössischer Gebäudeidentifikator: Gebäudeidentifikationsnummer im eidg. GWR. Quelle: GWR-Merkmalskatalog 5.0, Merkmal EGID. |
| EGRID | `donorBuildingEgrid` | Freitext (einzeilig) | Kern |  | Muss | Eidgenössischer Grundstücksidentifikator (E-GRID) des Grundstücks, auf dem das Gebäude steht. Quelle: GWR-Merkmalskatalog 5.0, Merkmal GEGRID. |
| Strasse | `donorBuildingStreet` | Freitext (einzeilig) | Kern | Muss | Muss | Strassenname der Adresse des Quellobjekts |
| Hausnummer | `donorBuildingHouseNumber` | Freitext (einzeilig) | Kern | Muss | Muss | Hausnummer der Adresse des Quellobjekts |
| Postleitzahl | `donorBuildingPostalCode` | Postleitzahl | Kern | Muss | Muss | Postleitzahl der Adresse des Quellobjekts |
| Ort | `donorBuildingCity` | Freitext (einzeilig) | Kern | Muss | Muss | Ortschaft der Adresse des Quellobjekts |
| Land | `donorBuildingCountry` | Ländercode nach ISO 3166 | Kern | Sollte | Sollte | Land der Adresse des Quellobjekts als zweistelliger Ländercode nach ISO 3166-1 (z. B. CH) |

### Gebäudedaten

| Datenfeld | Key | Format | Ebene | Stufe I | Stufe II | Definition |
| --- | --- | --- | --- | --- | --- | --- |
| Gebäudeklasse | `donorBuildingGklas` | Auswahlliste → [gwr-gklas](#list-gwr-gklas) | Kern | Sollte | Sollte | Einteilung der Gebäude nach Eurostat-Klassifikation. Quelle: GWR-Merkmalskatalog 5.0, Merkmal GKLAS. |
| Gebäudekategorie | `donorBuildingGkat` | Auswahlliste → [gwr-gkat](#list-gwr-gkat) | Kern | Sollte | Sollte | Einteilung der Gebäude entsprechend ihrer Zweckbestimmung. Quelle: GWR-Merkmalskatalog 5.0, Merkmal GKAT. |
| Bauperiode | `donorBuildingGbaup` | Auswahlliste → [gwr-gbaup](#list-gwr-gbaup) | Kern | Sollte | Sollte | Angabe zu Periode der Fertigstellung des Gebäudes. Quelle: GWR-Merkmalskatalog 5.0, Merkmal GBAUP. |
| Bauweise | `donorBuildingConstructionType` | Auswahlliste → [construction-type](#list-construction-type) | Kern | Sollte | Sollte | Vorherrschende Bauweise bzw. Tragkonstruktion des Gebäudes, zum Beispiel Massivbau, Skelettbau oder Holzbau |
| Baujahr des Gebäudes | `donorBuildingGbauj` | JJJJ | Kern | Sollte | Sollte | Angabe zu Jahr der Fertigstellung des Gebäudes. Quelle: GWR-Merkmalskatalog 5.0, Merkmal GBAUJ. |
| Gebäudevolumen | `donorBuildingGvol` | Zahlenwert [m³] | Kern | Sollte | Sollte | Angabe zum Volumen des Gebäudes. Quelle: GWR-Merkmalskatalog 5.0, Merkmal GVOL. |
| Gebäudefläche | `donorBuildingGarea` | Zahlenwert [m²] | Kern | Sollte | Sollte | Gebäudefläche in Quadratmetern. Quelle: GWR-Merkmalskatalog 5.0, Merkmal GAREA. |
| Anzahl Geschosse | `donorBuildingGastw` | Zahlenwert | Kern | Sollte | Sollte | Anzahl Geschosse und Untergeschosse, einschliesslich Erdgeschoss. Quelle: GWR-Merkmalskatalog 5.0, Merkmal GASTW. |
| Baudatum | `donorBuildingConstructionDate` | JJJJ-MM-TT | Erweiterung |  |  | Datum der Fertigstellung des Gebäudes, sofern genauer bekannt als das Baujahr |

### Details

| Datenfeld | Key | Format | Ebene | Stufe I | Stufe II | Definition |
| --- | --- | --- | --- | --- | --- | --- |
| Vergangene Umbaumassnahmen | `donorBuildingPreviousRenovations` | Freitext (mehrzeilig) | Kern |  |  | Bekannte frühere Umbauten, Sanierungen oder Erweiterungen des Gebäudes, möglichst mit Jahr |
| Erschliessung | `donorBuildingAccess` | Freitext (mehrzeilig) | Kern |  | Muss | Zugänglichkeit des Gebäudes für Demontage und Abtransport, zum Beispiel Zufahrt, Lift, Kranstellplatz |
| Weitere Informationen | `donorBuildingDetails` | Freitext (mehrzeilig) | Kern |  |  | Weitere relevante Angaben zum Quellobjekt, welche nicht durch die übrigen Datenfelder abgedeckt sind |
| Aussergewöhnliche Einzelereignisse | `donorBuildingSpecialEvents` | Freitext (mehrzeilig) | Erweiterung |  |  | Aussergewöhnliche Ereignisse, die den Zustand der Bauteile beeinflusst haben können, zum Beispiel Brand, Wasserschaden oder längerer Leerstand |
| Jahr der letzten Umbaumassnahme | `donorBuildingLastRenovationYear` | JJJJ | Erweiterung |  |  | Jahr, in dem das Gebäude zuletzt umgebaut oder saniert wurde |
| Ausbau von | `donorBuildingDismantlingStartDate` | JJJJ-MM-TT | Erweiterung |  |  | Datum, ab dem Bauteile im Quellobjekt ausgebaut werden können |
| Ausbau bis | `donorBuildingDismantlingEndDate` | JJJJ-MM-TT | Erweiterung |  |  | Datum, bis zu dem der Ausbau der Bauteile abgeschlossen sein muss |
| Anhänge | `donorBuildingAttachments` | Freitext (mehrzeilig) | Erweiterung |  |  | Bezeichnung und Ablageort von Unterlagen zum Quellobjekt, zum Beispiel Pläne oder Schadstoffgutachten |

## Datenfelder Re-Use-Bauteile

### Identifikation

| Datenfeld | Key | Format | Ebene | Stufe I | Stufe II | Definition |
| --- | --- | --- | --- | --- | --- | --- |
| Bezeichnung | `name` | Freitext (einzeilig) | Kern | Muss | Muss | Kurze Bezeichnung |
| Bauteil-ID | `componentId` | Freitext (einzeilig) | Kern |  | Muss | Nummer zur Identifikation des DPPs; Format und Vergabe der ID sind durch den Swiss Inv nicht vorgegeben |
| eBKP-H Code | `ebkphCode` | Auswahlliste → [ebkph](#list-ebkph) | Kern | Muss | Muss | Nach eBKP-H SN 506 511; Code und Bezeichnung sind in getrennten Datenfeldern abzubilden; eine Auswahl möglicher eBKP-H ist in der Referenztabelle eBKP-H gelistet |
| eBKP-H Bezeichnung | `ebkphLabel` | Freitext (einzeilig) | Kern | Muss | Muss | Bezeichnung zum eBKP-H Code; Code und Bezeichnung sind in getrennten Datenfeldern abzubilden |
| Verortung im Quellobjekt | `positionInDonorBuilding` | Freitext (mehrzeilig) | Kern |  | Sollte | Beschreibung der Verortung im Quellobjekt, zum Beispiel Angabe von Geschoss, Raum usw. |
| UUID | `uuid` | UUID | Erweiterung |  |  | nach ISO/IEC 9834-8:2014; gewährleistet die weltweit eindeutige Identifikation |
| UUID der Masterposition | `parentUuid` | UUID | Erweiterung |  |  | Zeigt die Zugehörigkeit zu einer übergeordneten Gesamtposition |
| eBKP-Gate Code | `ebkpGateCode` | Auswahlliste → [ebkp-gate](#list-ebkp-gate) | Erweiterung |  |  | Nach eBKP-Gate; Code und Bezeichnung sind in getrennten Datenfeldern abzubilden |
| eBKP-Gate Bezeichnung | `ebkpGateLabel` | Freitext (einzeilig) | Erweiterung |  |  | Bezeichnung zum eBKP-Gate Code; Code und Bezeichnung sind in getrennten Datenfeldern abzubilden |

### Menge

| Datenfeld | Key | Format | Ebene | Stufe I | Stufe II | Definition |
| --- | --- | --- | --- | --- | --- | --- |
| Menge (min) | `quantityMin` | Zahlenwert | Kern | Muss | Muss | Die Menge kann bewusst unscharf als Bereich mit Ober- und Untergrenze angegeben werden; für eine präzise Angabe den gleichen Wert in beide Felder eintragen |
| Menge (max) | `quantityMax` | Zahlenwert | Kern | Muss | Muss | Die Menge kann bewusst unscharf als Bereich mit Ober- und Untergrenze angegeben werden; für eine präzise Angabe den gleichen Wert in beide Felder eintragen |
| Einheit | `unit` | Auswahlliste → [unit](#list-unit) | Kern | Muss | Muss | Empfohlen wird eine Einheit, die für eine Vermittlung der Bauteile geeignet ist |
| Zusatzinformation Menge | `quantityNotes` | Freitext (mehrzeilig) | Erweiterung |  |  | Zusatzinformationen zur Menge, zum Beispiel weitere Bezugsgrössen |

### Dimensionen

| Datenfeld | Key | Format | Ebene | Stufe I | Stufe II | Definition |
| --- | --- | --- | --- | --- | --- | --- |
| Aussenmass Höhe | `zDim` | Zahlenwert [cm] | Kern |  | Muss | Die drei Aussenmasse sollen die einheitliche Angabe von Abmessungen für möglichst allfällige Bauteilformen standardisieren; sie orientieren sich am Begrenzungsquader des IFC-Standards von buildingSMART |
| Aussenmass Breite | `yDim` | Zahlenwert [cm] | Kern |  | Muss | Die drei Aussenmasse sollen die einheitliche Angabe von Abmessungen für möglichst allfällige Bauteilformen standardisieren; sie orientieren sich am Begrenzungsquader des IFC-Standards von buildingSMART |
| Aussenmass Tiefe / Länge | `xDim` | Zahlenwert [cm] | Kern |  | Muss | Die drei Aussenmasse sollen die einheitliche Angabe von Abmessungen für möglichst allfällige Bauteilformen standardisieren; sie orientieren sich am Begrenzungsquader des IFC-Standards von buildingSMART |
| Freie Dimensionsangaben | `dimensionNotes` | Freitext (mehrzeilig) | Kern |  | Muss | Angabe relevanter Dimensionen, welche nicht durch die Aussenmasse oder sonstige Attribute abgedeckt sind |

### Details

| Datenfeld | Key | Format | Ebene | Stufe I | Stufe II | Definition |
| --- | --- | --- | --- | --- | --- | --- |
| Weitere Informationen | `description` | Freitext (mehrzeilig) | Kern | Sollte | Sollte | Beschreibung relevanter Eigenschaften, welche nicht durch die Aussenmasse oder sonstige Attribute abgedeckt sind |
| Materialkategorie | `material` | Auswahlliste (Mehrfachauswahl) → [material](#list-material) | Kern | Muss | Muss | Materialkategorien, aus denen das Bauteil hauptsächlich besteht; es können mehrere gewählt werden, bei einem Holzfenster bspw. Vollholz für den Rahmen und Glas für die Verglasung |
| Zusatzinformation Material | `materialNotes` | Freitext (mehrzeilig) | Kern |  | Muss | Ausführungen zum Material, welche nicht durch die Materialkategorie abgedeckt sind |

### Bewertung

| Datenfeld | Key | Format | Ebene | Stufe I | Stufe II | Definition |
| --- | --- | --- | --- | --- | --- | --- |
| Schadstoffgutachten | `pollutantReport` | Auswahlliste → [pollutant-report](#list-pollutant-report) | Kern |  | Muss | Angabe, ob für das Bauteil eine Beurteilung der Schadstoffbelastung durch ein Schadstoffgutachten vorliegt |
| Visueller Zustand | `visualCondition` | Auswahlliste → [visual-condition](#list-visual-condition) | Kern |  | Muss | Allfällige Ausführungen zum visuellen Zustand können im Datenfeld «Erläuterung der Empfehlung» ergänzt werden |
| Funktionaler Zustand | `functionalCondition` | Auswahlliste → [functional-condition](#list-functional-condition) | Kern |  | Muss | Allfällige Ausführungen zum funktionalen Zustand können im Datenfeld «Erläuterung der Empfehlung» ergänzt werden |
| Demontageaufwand | `demountability` | Auswahlliste → [demountability](#list-demountability) | Kern |  | Muss | Allfällige Ausführungen zum Demontageaufwand können im Datenfeld «Erläuterung der Empfehlung» ergänzt werden |
| Empfehlung Detailaufnahme | `recDetailedAssessment` | Auswahlliste → [rec-detailed-assessment](#list-rec-detailed-assessment) | Kern | Muss |  | Die Auditorin des Wiederverwendungs-Audit Stufe I empfiehlt, ob eine vertiefte Aufnahme des Bauteils im Wiederverwendungs-Audit Stufe II durchgeführt werden sollte |
| Empfehlung Vermittlung | `recDistribution` | Auswahlliste → [rec-distribution](#list-rec-distribution) | Kern |  | Muss | Die Auditorin des Wiederverwendungs-Audit Stufe II empfiehlt, ob eine Vermittlung des Bauteils angestrebt werden sollte |
| Erläuterung der Empfehlung | `recNotes` | Freitext (mehrzeilig) | Kern |  | Sollte | Allfällige Ausführungen zur Bewertung sowie zur Empfehlung für eine Vermittlung des Bauteils |
| Zusatzinformation Schadstoffe | `pollutantNotes` | Freitext (mehrzeilig) | Erweiterung |  |  | Weiterführende Angaben zum Schadstoffgutachten, zum Beispiel Verfasserin, Datum sowie Art und Grad der Schadstoffbelastung |
| Verbindungsart | `connection` | Auswahlliste (Mehrfachauswahl) → [connection](#list-connection) | Erweiterung |  |  | Gemeint sind alle Verbindungen, die für eine Demontage oder Montage des Bauteils relevant sind; zusätzliche Informationen, welche nicht durch die Auswahlliste abgedeckt sind, können im Datenfeld «Zusatzinformation Verbindungsart» als Freitext ergänzt werden |
| Zusatzinformation Verbindungsart | `connectionNotes` | Freitext (mehrzeilig) | Erweiterung |  |  | Zusätzliche Informationen zur Verbindung, welche nicht durch die Auswahlliste abgedeckt sind |

### Logistik

| Datenfeld | Key | Format | Ebene | Stufe I | Stufe II | Definition |
| --- | --- | --- | --- | --- | --- | --- |
| Re-Use-Status | `reUseStatus` | Auswahlliste → [reuse-status](#list-reuse-status) | Erweiterung |  |  | Aktueller Stand des Bauteils im Wiederverwendungsprozess |
| Postleitzahl des Standorts | `locationPostalCode` | Postleitzahl | Erweiterung |  |  | Postleitzahl des aktuellen Standorts des Bauteils |
| Land des Standorts | `locationCountry` | Ländercode nach ISO 3166 | Erweiterung |  |  | Land des aktuellen Standorts des Bauteils als zweistelliger Ländercode nach ISO 3166-1 (z. B. CH) |
| Datum Einlagerung | `storageStartDate` | JJJJ-MM-TT | Erweiterung |  |  | Datum, an dem das Bauteil eingelagert wurde |
| Datum Auslagerung | `storageEndDate` | JJJJ-MM-TT | Erweiterung |  |  | Datum, an dem das Bauteil ausgelagert wurde oder spätestens ausgelagert werden muss |
| Zusatzinformation Logistik | `logisticsNotes` | Freitext (mehrzeilig) | Erweiterung |  |  | Zusatzinformationen zu Lagerung, Verpackung und Transport des Bauteils |

### Konditionen

| Datenfeld | Key | Format | Ebene | Stufe I | Stufe II | Definition |
| --- | --- | --- | --- | --- | --- | --- |
| Startdatum Verfügbarkeit | `availabilityStartDate` | JJJJ-MM-TT | Erweiterung |  |  | Datum, ab dem das Bauteil für Abnehmerinnen verfügbar ist |
| Enddatum Verfügbarkeit | `availabilityEndDate` | JJJJ-MM-TT | Erweiterung |  |  | Datum, bis zu dem das Bauteil für Abnehmerinnen verfügbar ist |
| Verkaufspreis | `price` | Zahlenwert [CHF] | Erweiterung |  |  | Verkaufspreis in Schweizer Franken pro Einheit, welche für die Mengenangabe gewählt wurde |
| Übergabekonditionen | `handoverConditions` | Freitext (mehrzeilig) | Erweiterung |  |  | Bedingungen der Übergabe, zum Beispiel Abholung ab Quellobjekt oder Lager, Demontage durch die Abnehmerin, Fristen |

### Auswertung

| Datenfeld | Key | Format | Ebene | Stufe I | Stufe II | Definition |
| --- | --- | --- | --- | --- | --- | --- |
| THG-Einsparung pro Einheit | `emissionSavingsPerUnit` | Zahlenwert [kg CO₂-eq] | Erweiterung |  |  | Nach KBOB; gemeint ist die überschlägige THG-Einsparung durch die Wiederverwendung des Bauteils im Vergleich zur Neuherstellung; im Datenfeld «Zusatzinformation Ökobilanz» sollte die Methode beschrieben werden |
| THG-Einsparung | `emissionSavings` | Zahlenwert [kg CO₂-eq] | Erweiterung |  |  | Gesamte THG-Einsparung für die angegebene Menge; Methode wie bei «THG-Einsparung pro Einheit» |
| Zusatzinformation Ökobilanz | `emissionNotes` | Freitext (mehrzeilig) | Erweiterung |  |  | Ausführungen zur THG-Bilanz oder Angaben zu weiteren Klima- und Umweltindikatoren |

### Weitere Attribute

| Datenfeld | Key | Format | Ebene | Stufe I | Stufe II | Definition |
| --- | --- | --- | --- | --- | --- | --- |
| Herstellerin | `manufacturer` | Freitext (einzeilig) | Erweiterung |  |  | Name des Unternehmens, welches das Bauteil hergestellt hat |
| Produktbezeichnung | `productName` | Freitext (einzeilig) | Erweiterung |  |  | Vollständige Produktbezeichnung bzw. Markenname des Bauteils |
| Einbaujahr | `yearOfInstallation` | JJJJ | Erweiterung |  |  | Jahr, in welchem das Bauteil im Quellobjekt eingebaut wurde |
| Produktionsjahr | `yearOfManufacture` | JJJJ | Erweiterung |  |  | Jahr, in welchem das Bauteil hergestellt wurde |
| Farbe | `color` | Freitext (einzeilig) | Erweiterung |  |  | Relevante Farben des Bauteils |
| Gewicht | `weight` | Zahlenwert [kg] | Erweiterung |  |  | Gewichtsangabe pro Einheit, welche für die Mengenangabe gewählt wurde |
| Bewitterung | `weatheringExposure` | Freitext (einzeilig) | Erweiterung |  |  | Angabe, ob und wie stark das Bauteil der Witterung ausgesetzt war, zum Beispiel innen, aussen geschützt, aussen frei bewittert |
| Zone im Gebäude | `zoneInDonorBuilding` | Freitext (einzeilig) | Erweiterung |  |  | Zone oder Bereich des Quellobjekts, dem das Bauteil zugeordnet ist |
| Material nach KBOB | `materialKbob` | Freitext (mehrzeilig) | Erweiterung |  |  | Materialien des Bauteils nach der KBOB-Liste mit ihrem jeweiligen Anteil |
| Farbe als HEX | `colorInHex` | Freitext (einzeilig) | Erweiterung |  |  | Farbe des Bauteils als Hexadezimalwert, zum Beispiel #A0522D |
| Gewährleistung | `warranty` | Freitext (mehrzeilig) | Erweiterung |  |  | Angaben zu einer Gewährleistung oder Garantie auf das wiederverwendete Bauteil |
| Originalpreis | `priceOriginal` | Zahlenwert [CHF] | Erweiterung |  |  | Neupreis des Bauteils in Schweizer Franken, soweit bekannt |
| Mängel | `defects` | Freitext (mehrzeilig) | Erweiterung |  |  | Bekannte Mängel oder Schäden des Bauteils |

### Technische Angaben

| Datenfeld | Key | Format | Ebene | Stufe I | Stufe II | Definition |
| --- | --- | --- | --- | --- | --- | --- |
| U-Wert | `uValue` | Zahlenwert [W/m²K] | Erweiterung |  |  | Wärmedurchgangskoeffizient des Bauteils gemäss Herstellerangabe oder Messung |
| Nutzvolumen in Litern | `volumeInLiters` | Zahlenwert [l] | Erweiterung |  |  | Nutzbares Volumen des Bauteils in Litern, zum Beispiel bei Speichern oder Becken |
| Nutzvolumen in Kubikmetern | `volumeInM3` | Zahlenwert [m³] | Erweiterung |  |  | Nutzbares Volumen des Bauteils in Kubikmetern, zum Beispiel bei Containern oder Silos |
| Stromanschluss | `electricConnector` | Freitext (einzeilig) | Erweiterung |  |  | Art des Stromanschlusses, zum Beispiel Steckertyp oder Festanschluss |
| Elektrische Spannung | `electricVoltage` | Zahlenwert [V] | Erweiterung |  |  | Nennspannung des Bauteils |
| Elektrische Leistung | `electricWatt` | Zahlenwert [W] | Erweiterung |  |  | Nennleistung des Bauteils |
| Stromstärke | `electricAmp` | Zahlenwert [A] | Erweiterung |  |  | Nennstrom des Bauteils |
| Küchennorm | `kitchenNorm` | Freitext (einzeilig) | Erweiterung |  |  | Massnorm, nach der Küchenelemente gebaut sind, zum Beispiel SMS (55 cm) oder EURO (60 cm) |
| Lochabstand | `holeSpacing` | Zahlenwert [mm] | Erweiterung |  |  | Abstand zwischen den Befestigungs- oder Anschlusslöchern, von Mitte zu Mitte gemessen |

### Plattform

| Datenfeld | Key | Format | Ebene | Stufe I | Stufe II | Definition |
| --- | --- | --- | --- | --- | --- | --- |
| Aktiviert auf Plattform | `activeOnPlatform` | Ja/Nein | Erweiterung |  |  | Angabe, ob das Bauteil auf der Vermittlungsplattform sichtbar ist |
| Top-Angebot auf Plattform | `topOfferOnPlatform` | Ja/Nein | Erweiterung |  |  | Angabe, ob das Bauteil auf der Plattform hervorgehoben wird |
| Zahlungsart | `paymentMethod` | Freitext (einzeilig) | Erweiterung |  |  | Zulässige Zahlungsarten, zum Beispiel Rechnung oder Vorauskasse |
| Versandart | `shippingMethod` | Freitext (einzeilig) | Erweiterung |  |  | Mögliche Arten der Übergabe oder Lieferung, zum Beispiel Abholung oder Spedition |
| Reservierte Bestände | `reservedStock` | Zahlenwert | Erweiterung |  |  | Menge, die bereits für Abnehmerinnen reserviert ist, in der gewählten Einheit |

## Datenfelder Änderungsprotokoll

### Änderungsprotokoll

| Datenfeld | Key | Format | Ebene | Definition |
| --- | --- | --- | --- | --- |
| Verfasserin | `logAuthor` | Freitext (einzeilig) | Erweiterung | Person, die den Eintrag erstellt hat |
| Datum | `logDate` | JJJJ-MM-TT | Erweiterung | Datum des Ereignisses |
| Ereignis | `logEvent` | Freitext (einzeilig) | Erweiterung | Was erstellt oder geändert wurde, zum Beispiel «Audit Stufe I erstellt» |
| Telefon | `logPhone` | Telefonnummer | Erweiterung | Telefonnummer der Verfasserin |
| E-Mail | `logEmail` | E-Mail-Adresse | Erweiterung | E-Mail-Adresse der Verfasserin |

## Auswahllisten

<a id="list-ebkph"></a>

### eBKP-H (Referenzauswahl) (`ebkph`)

Kern

Platzhalter. Die Codes und Bezeichnungen nach eBKP-H SN 506 511 sind hier nicht hinterlegt. Die eBKP-H sollte nur in der Ebene Elementgruppe oder Element angegeben werden.

| Key | Bezeichnung | Definition |
| --- | --- | --- |
| `XY00` | Empty |  |
| `YZ00` | Empty |  |

<a id="list-unit"></a>

### Einheit (`unit`)

Kern

| Key | Bezeichnung | Definition |
| --- | --- | --- |
| `pc` | Stk. | Stück |
| `m` | lfm | Laufmeter |
| `m2` | m² | Quadratmeter |
| `m3` | m³ | Kubikmeter |
| `kg` | kg | Kilogramm |
| `t` | t | Tonne |
| `na` | Keine Angaben | Einheit nicht bekannt |

<a id="list-material"></a>

### Materialkategorie (`material`)

Kern

| Key | Bezeichnung | Gruppe | Definition |
| --- | --- | --- | --- |
| `me00` | Metall | Metallisch |  |
| `me01` | Stahl und Gusseisen | Metallisch |  |
| `me02` | Aluminium | Metallisch |  |
| `me03` | Kupfer | Metallisch |  |
| `on00` | Pflanzliche und tierische Stoffe | Organisch: natürlich |  |
| `on01` | Vollholz | Organisch: natürlich |  |
| `on02` | Holzwerkstoff | Organisch: natürlich |  |
| `os01` | Kunststoff | Organisch: synthetisch |  |
| `os02` | Bitumen | Organisch: synthetisch |  |
| `mi00` | Mineralische Baustoffe | Mineralisch |  |
| `mi01` | Naturstein | Mineralisch |  |
| `mi02` | Beton und zementgebundene Stoffe | Mineralisch |  |
| `mi03` | Keramik | Mineralisch |  |
| `mi04` | Gips | Mineralisch |  |
| `mi05` | Glas | Mineralisch |  |
| `mi06` | Mineralwolle | Mineralisch |  |
| `co01` | Verbund | Verbund |  |
| `un01` | Unbekannt | Unbekannt |  |

<a id="list-pollutant-report"></a>

### Schadstoffgutachten (`pollutant-report`)

Kern

| Key | Bezeichnung | Definition |
| --- | --- | --- |
| `available` | Vorliegend | Für das betroffene Bauteil liegt eine Beurteilung der Schadstoffbelastung durch ein Schadstoffgutachten vor |
| `notAvailable` | Nicht vorliegend | Für das betroffene Bauteil liegt keine Beurteilung der Schadstoffbelastung durch ein Schadstoffgutachten vor |

<a id="list-visual-condition"></a>

### Visueller Zustand (`visual-condition`)

Kern

| Key | Bezeichnung | Definition |
| --- | --- | --- |
| `0` | Keine Einschätzung |  |
| `1` | Neuwertig |  |
| `2` | Leichte Gebrauchsspuren |  |
| `3` | Starke Gebrauchsspuren |  |
| `4` | Beschädigt |  |

<a id="list-functional-condition"></a>

### Funktionaler Zustand (`functional-condition`)

Kern

| Key | Bezeichnung | Definition |
| --- | --- | --- |
| `0` | Keine Einschätzung |  |
| `1` | Voll funktionsfähig |  |
| `2` | Eingeschränkt funktionsfähig |  |
| `3` | Defekt (reparierbar) |  |
| `4` | Defekt (irreparabel) |  |

<a id="list-demountability"></a>

### Demontageaufwand (`demountability`)

Kern

| Key | Bezeichnung | Definition |
| --- | --- | --- |
| `0` | Keine Einschätzung |  |
| `1` | Sehr einfach |  |
| `2` | Einfach |  |
| `3` | Aufwändig |  |
| `4` | Sehr aufwändig |  |

<a id="list-rec-detailed-assessment"></a>

### Empfehlung Detailaufnahme (`rec-detailed-assessment`)

Kern

| Key | Bezeichnung | Definition |
| --- | --- | --- |
| `unknown` | Keine Angabe | Die Auditorin gibt keine Empfehlung ab |
| `yes` | Ja | Die Auditorin des Wiederverwendungs-Audit Stufe I empfiehlt eine vertiefte Aufnahme des Bauteils im Wiederverwendungs-Audit Stufe II |
| `no` | Nein | Die Auditorin des Wiederverwendungs-Audit Stufe I empfiehlt keine vertiefte Aufnahme des Bauteils im Wiederverwendungs-Audit Stufe II |

<a id="list-rec-distribution"></a>

### Empfehlung Vermittlung (`rec-distribution`)

Kern

| Key | Bezeichnung | Definition |
| --- | --- | --- |
| `unknown` | Keine Angabe | Die Auditorin gibt keine Empfehlung ab |
| `yes` | Ja | Die Auditorin des Wiederverwendungs-Audit Stufe II empfiehlt eine Vermittlung des Bauteils anzustreben |
| `no` | Nein | Die Auditorin des Wiederverwendungs-Audit Stufe II empfiehlt keine Vermittlung des Bauteils anzustreben |

<a id="list-gwr-gkat"></a>

### Gebäudekategorie (GWR GKAT) (`gwr-gkat`)

Kern

Codes und Bezeichnungen wörtlich aus dem Merkmalskatalog des eidg. Gebäude- und Wohnungsregisters (BFS): Deutsch und Französisch aus Version 5.0.0, Italienisch und Englisch aus Version 4.3.2.

| Key | Bezeichnung | Definition |
| --- | --- | --- |
| `1010` | Provisorische Unterkunft |  |
| `1020` | Gebäude mit ausschliesslicher Wohnnutzung |  |
| `1030` | Andere Wohngebäude (Wohngebäude mit Nebennutzung) |  |
| `1040` | Gebäude mit teilweiser Wohnnutzung |  |
| `1060` | Gebäude ohne Wohnnutzung |  |
| `1080` | Sonderbau |  |

<a id="list-gwr-gklas"></a>

### Gebäudeklasse (GWR GKLAS) (`gwr-gklas`)

Kern

Codes und Bezeichnungen wörtlich aus dem Merkmalskatalog des eidg. Gebäude- und Wohnungsregisters (BFS): Deutsch und Französisch aus Version 5.0.0, Italienisch und Englisch aus Version 4.3.2.

| Key | Bezeichnung | Definition |
| --- | --- | --- |
| `1110` | Gebäude mit einer Wohnung |  |
| `1121` | Gebäude mit zwei Wohnungen |  |
| `1122` | Gebäude mit drei oder mehr Wohnungen |  |
| `1130` | Wohngebäude für Gemeinschaften |  |
| `1211` | Hotelgebäude |  |
| `1212` | Andere Gebäude für kurzfristige Beherbergungen |  |
| `1220` | Bürogebäude |  |
| `1230` | Gross- und Einzelhandelsgebäude |  |
| `1231` | Restaurants und Bars in Gebäuden ohne Wohnnutzung |  |
| `1241` | Bahnhöfe, Abfertigungsgebäude, Fernsprechvermittlungszentralen |  |
| `1242` | Garagengebäude |  |
| `1251` | Industriegebäude |  |
| `1252` | Behälter, Silos und Lagergebäude |  |
| `1261` | Gebäude für Kultur- und Freizeitzwecke |  |
| `1262` | Museen / Bibliotheken |  |
| `1263` | Schul- und Hochschulgebäude, Forschungseinrichtungen |  |
| `1264` | Krankenhäuser und Facheinrichtungen des Gesundheitswesens |  |
| `1265` | Sporthallen |  |
| `1272` | Kirchen und sonstige Kultgebäude |  |
| `1273` | Denkmäler oder unter Denkmalschutz stehende Bauwerke |  |
| `1274` | Sonstige Hochbauten, anderweitig nicht genannt |  |
| `1275` | Andere Gebäude für die kollektive Unterkunft |  |
| `1276` | Gebäude für die Tierhaltung |  |
| `1277` | Gebäude für den Pflanzenbau |  |
| `1278` | Andere landwirtschaftliche Gebäude |  |

<a id="list-gwr-gbaup"></a>

### Bauperiode (GWR GBAUP) (`gwr-gbaup`)

Kern

Codes und Bezeichnungen wörtlich aus dem Merkmalskatalog des eidg. Gebäude- und Wohnungsregisters (BFS): Deutsch und Französisch aus Version 5.0.0, Italienisch und Englisch aus Version 4.3.2.

| Key | Bezeichnung | Definition |
| --- | --- | --- |
| `8011` | Periode vor 1919 |  |
| `8012` | Periode von 1919 bis 1945 |  |
| `8013` | Periode von 1946 bis 1960 |  |
| `8014` | Periode von 1961 bis 1970 |  |
| `8015` | Periode von 1971 bis 1980 |  |
| `8016` | Periode von 1981 bis 1985 |  |
| `8017` | Periode von 1986 bis 1990 |  |
| `8018` | Periode von 1991 bis 1995 |  |
| `8019` | Periode von 1996 bis 2000 |  |
| `8020` | Periode von 2001 bis 2005 |  |
| `8021` | Periode von 2006 bis 2010 |  |
| `8022` | Periode von 2011 bis 2015 |  |
| `8023` | Periode ab 2016 |  |

<a id="list-construction-type"></a>

### Bauweise (`construction-type`)

Erweiterung

| Key | Bezeichnung | Definition |
| --- | --- | --- |
| `solidHeavy` | Massivbau schwer |  |
| `solidLight` | Massivbau leicht |  |
| `logTimber` | Blockbau Holz |  |
| `lightTimber` | Leichtbau Holz |  |
| `lightSteel` | Leichtbau Stahl |  |
| `mixed` | Mischbau |  |
| `modular` | Modulbau |  |

<a id="list-connection"></a>

### Verbindungsart (`connection`)

Erweiterung

| Key | Bezeichnung | Definition |
| --- | --- | --- |
| `0` | Keine Angabe |  |
| `1` | Lose |  |
| `2` | Geschraubt / Gesteckt |  |
| `3` | Genagelt / Genietet |  |
| `4` | Festverbaut |  |
| `unknown` | Verbindung unbekannt |  |
| `screwed` | Geschraubt |  |
| `nailed` | Genagelt |  |
| `glued` | Geklebt |  |
| `welded` | Geschweisst |  |
| `riveted` | Genietet |  |
| `interlocked` | Verzahnt | z. B. bei Holzverbindungen |
| `plugged` | Gesteckt | z. B. bei Blechverbindungen |
| `clamped` | Geklemmt |  |
| `clipped` | Geclipst | z. B. bei Kunststoffelementen |
| `flanged` | Gebördelt | z. B. bei Rohrverbindungen |
| `dowelled` | Verzapft | z. B. traditionelle Holzverbindungen |
| `soldered` | Verlötet | z. B. bei Metallrohren |
| `other` | Andere |  |

<a id="list-reuse-status"></a>

### Re-Use-Status (`reuse-status`)

Erweiterung

| Key | Bezeichnung | Definition |
| --- | --- | --- |
| `unknown` | Keine Angabe |  |
| `installedInDonorBuilding` | Im Quellobjekt verbaut | Das Bauteil ist im Quellobjekt verbaut |
| `demounted` | Demontiert | Das Bauteil ist demontiert |
| `stored` | Im Lager | Das Bauteil ist in einem Lager zwischengelagert |
| `reused` | Wiederverwendet | Das Bauteil ist erfolgreich in einem Zielobjekt wiederverwendet |
| `retainedInPlace` | Bestandserhalt | Das Bauteil wird nicht wiederverwendet, da es im Bestandsgebäude erhalten bleibt |
| `noReuse` | Keine Wiederverwendung | Das Bauteil wird nicht wiederverwendet oder erhalten, sondern z. B. dem Recycling zugeführt oder entsorgt |

<a id="list-ebkp-gate"></a>

### eBKP-Gate (`ebkp-gate`)

Erweiterung

Externe Klassifikation; im Swiss Inv ist keine eigene Auswahlliste hinterlegt.

## Formate

| Key | Bezeichnung |
| --- | --- |
| `text` | Freitext (einzeilig) |
| `multiline` | Freitext (mehrzeilig) |
| `number` | Zahlenwert |
| `boolean` | Ja/Nein |
| `code` | Auswahlliste / Auswahlliste (Mehrfachauswahl) |
| `contact` | Kontakt |
| `country` | Ländercode nach ISO 3166 |
| `phone` | Telefonnummer |
| `email` | E-Mail-Adresse |
| `uuid` | UUID |
| `year` | JJJJ |
| `date` | JJJJ-MM-TT |
| `postalCode` | Postleitzahl |

## Verpflichtung

| Key | Bezeichnung |
| --- | --- |
| `muss` | Muss |
| `sollte` | Sollte |

## Einheiten

| Zeichen | Bezeichnung |
| --- | --- |
| mm | Millimeter |
| cm | Zentimeter |
| m² | Quadratmeter |
| m³ | Kubikmeter |
| l | Liter |
| kg | Kilogramm |
| kg CO₂-eq | Kilogramm CO₂-Äquivalente |
| CHF | Schweizer Franken |
| W/m²K | Watt pro Quadratmeter und Kelvin |
| V | Volt |
| W | Watt |
| A | Ampere |
