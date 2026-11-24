<!-- Automatisch erzeugt von tools/build.py - nicht von Hand bearbeiten. -->

# Repertorio dei campi di dati Swiss Inv

[Deutsch](DE.md) · [Français](FR.md) · **Italiano** · [English](EN.md)

Versione: `2.0.0-draft`

**Nucleo** = stabile, cambia solo con una nuova edizione della norma. **Estensione** = campi facoltativi che crescono tramite proposte.

## Campi di dati Progetto

### Identificazione

| Campo | Chiave | Formato | Livello | Livello I | Livello II | Definizione |
| --- | --- | --- | --- | --- | --- | --- |
| Nome del progetto | `projectName` | Testo libero (una riga) | Nucleo | Obbligatorio | Obbligatorio | Denominazione del progetto che raggruppa uno o più edifici di origine |
| ID del progetto | `projectId` | Testo libero (una riga) | Nucleo |  |  | Identificativo del progetto; il formato e l'assegnazione dell'ID non sono prescritti dallo Swiss Inv |

### Partecipanti al progetto

| Campo | Chiave | Formato | Livello | Livello I | Livello II | Definizione |
| --- | --- | --- | --- | --- | --- | --- |
| Proprietario | `projectOwner` | Contatto | Nucleo | Obbligatorio | Obbligatorio | Proprietario degli edifici di origine interessati |
| Progettista | `projectPlanner` | Contatto | Nucleo |  |  | Progettista della trasformazione o della decostruzione |
| Committente | `projectAuditClient` | Contatto | Nucleo | Obbligatorio | Obbligatorio | Committente dell'audit di riuso |
| Mandatario | `projectAuditor` | Contatto | Nucleo | Obbligatorio | Obbligatorio | Mandatario che esegue l'audit di riuso |

## Campi di dati Contatti

### Persona di contatto

| Campo | Chiave | Formato | Livello | Definizione |
| --- | --- | --- | --- | --- |
| Nome | `contactName` | Testo libero (una riga) | Nucleo | Nome e cognome della persona di contatto |
| Ruolo nel progetto | `contactRole` | Testo libero (una riga) | Nucleo | Ruolo o funzione della persona di contatto nel progetto |

### Indirizzo

| Campo | Chiave | Formato | Livello | Definizione |
| --- | --- | --- | --- | --- |
| Impresa | `contactCompany` | Testo libero (più righe) | Nucleo | Nome dell'impresa o dell'organizzazione |
| Via | `contactStreet` | Testo libero (una riga) | Nucleo | Nome della via dell'indirizzo della persona di contatto |
| Numero civico | `contactHouseNumber` | Testo libero (una riga) | Nucleo | Numero civico dell'indirizzo della persona di contatto |
| Codice postale | `contactPostalCode` | Codice postale | Nucleo | Codice postale dell'indirizzo della persona di contatto |
| Località | `contactCity` | Testo libero (una riga) | Nucleo | Località dell'indirizzo della persona di contatto |
| Paese | `contactCountry` | Codice paese secondo ISO 3166 | Nucleo | Paese dell'indirizzo della persona di contatto come codice paese a due lettere secondo ISO 3166-1 (ad es. CH) |

### Recapiti

| Campo | Chiave | Formato | Livello | Definizione |
| --- | --- | --- | --- | --- |
| Telefono | `contactPhone` | Numero di telefono | Nucleo | Numero di telefono della persona di contatto, possibilmente in formato internazionale con prefisso del paese |
| E-mail | `contactEmail` | Indirizzo e-mail | Nucleo | Indirizzo e-mail della persona di contatto |

## Campi di dati Edifici di origine

### Indirizzo

| Campo | Chiave | Formato | Livello | Livello I | Livello II | Definizione |
| --- | --- | --- | --- | --- | --- | --- |
| EGID | `donorBuildingEgid` | Testo libero (una riga) | Nucleo |  | Obbligatorio | Identificatore federale dell'edificio: numero di identificazione dell'edificio nel REA federale. Fonte: catalogo dei caratteri REA 5.0, carattere EGID. |
| EGRID | `donorBuildingEgrid` | Testo libero (una riga) | Nucleo |  | Obbligatorio | Identificatore federale (E-GRID) del fondo, oggetto della proprietà fondiaria, sul quale si trova l'edificio. Fonte: catalogo dei caratteri REA 5.0, carattere GEGRID. |
| Via | `donorBuildingStreet` | Testo libero (una riga) | Nucleo | Obbligatorio | Obbligatorio | Nome della via dell'indirizzo dell'edificio di origine |
| Numero civico | `donorBuildingHouseNumber` | Testo libero (una riga) | Nucleo | Obbligatorio | Obbligatorio | Numero civico dell'indirizzo dell'edificio di origine |
| Codice postale | `donorBuildingPostalCode` | Codice postale | Nucleo | Obbligatorio | Obbligatorio | Codice postale dell'indirizzo dell'edificio di origine |
| Località | `donorBuildingCity` | Testo libero (una riga) | Nucleo | Obbligatorio | Obbligatorio | Località dell'indirizzo dell'edificio di origine |
| Paese | `donorBuildingCountry` | Codice paese secondo ISO 3166 | Nucleo | Raccomandato | Raccomandato | Paese dell'indirizzo dell'edificio di origine come codice paese a due lettere secondo ISO 3166-1 (ad es. CH) |

### Dati dell'edificio

| Campo | Chiave | Formato | Livello | Livello I | Livello II | Definizione |
| --- | --- | --- | --- | --- | --- | --- |
| Classe di edificio | `donorBuildingGklas` | Elenco di selezione → [gwr-gklas](#list-gwr-gklas) | Nucleo | Raccomandato | Raccomandato | Suddivisione degli edifici secondo la classificazione di Eurostat. Fonte: catalogo dei caratteri REA 5.0, carattere GKLAS. |
| Categoria di edificio | `donorBuildingGkat` | Elenco di selezione → [gwr-gkat](#list-gwr-gkat) | Nucleo | Raccomandato | Raccomandato | Suddivisione degli edifici secondo la destinazione. Fonte: catalogo dei caratteri REA 5.0, carattere GKAT. |
| Epoca di costruzione | `donorBuildingGbaup` | Elenco di selezione → [gwr-gbaup](#list-gwr-gbaup) | Nucleo | Raccomandato | Raccomandato | Indicazione dell'epoca di completamento dell'edificio. Fonte: catalogo dei caratteri REA 5.0, carattere GBAUP. |
| Tipo di costruzione | `donorBuildingConstructionType` | Elenco di selezione → [construction-type](#list-construction-type) | Nucleo | Raccomandato | Raccomandato | Tipo di costruzione o struttura portante predominante dell'edificio, ad esempio costruzione massiccia, a scheletro o in legno |
| Anno di costruzione dell'edificio | `donorBuildingGbauj` | AAAA | Nucleo | Raccomandato | Raccomandato | Indicazione dell'anno di completamento dell'edificio. Fonte: catalogo dei caratteri REA 5.0, carattere GBAUJ. |
| Volume dell'edificio | `donorBuildingGvol` | Valore numerico [m³] | Nucleo | Raccomandato | Raccomandato | Indicazione del volume dell'edificio. Fonte: catalogo dei caratteri REA 5.0, carattere GVOL. |
| Superficie dell'edificio | `donorBuildingGarea` | Valore numerico [m²] | Nucleo | Raccomandato | Raccomandato | Superficie dell'edificio in metri quadrati. Fonte: catalogo dei caratteri REA 5.0, carattere GAREA. |
| Numero di piani | `donorBuildingGastw` | Valore numerico | Nucleo | Raccomandato | Raccomandato | Numero di piani compreso il pianterreno. Fonte: catalogo dei caratteri REA 5.0, carattere GASTW. |
| Data di costruzione | `donorBuildingConstructionDate` | AAAA-MM-GG | Estensione |  |  | Data di completamento dell'edificio, se nota con maggiore precisione rispetto all'anno di costruzione |

### Dettagli

| Campo | Chiave | Formato | Livello | Livello I | Livello II | Definizione |
| --- | --- | --- | --- | --- | --- | --- |
| Trasformazioni precedenti | `donorBuildingPreviousRenovations` | Testo libero (più righe) | Nucleo |  |  | Trasformazioni, risanamenti o ampliamenti precedenti noti dell'edificio, se possibile con l'anno |
| Accesso | `donorBuildingAccess` | Testo libero (più righe) | Nucleo |  | Obbligatorio | Accessibilità dell'edificio per lo smontaggio e il trasporto, ad esempio accesso stradale, ascensore, area per gru |
| Ulteriori informazioni | `donorBuildingDetails` | Testo libero (più righe) | Nucleo |  |  | Ulteriori indicazioni rilevanti sull'edificio di origine non coperte dagli altri campi |
| Eventi straordinari | `donorBuildingSpecialEvents` | Testo libero (più righe) | Estensione |  |  | Eventi straordinari che possono aver influito sullo stato dei componenti, ad esempio incendio, danni da acqua o lunga inoccupazione |
| Anno dell'ultima trasformazione | `donorBuildingLastRenovationYear` | AAAA | Estensione |  |  | Anno dell'ultima trasformazione o dell'ultimo risanamento dell'edificio |
| Smontaggio dal | `donorBuildingDismantlingStartDate` | AAAA-MM-GG | Estensione |  |  | Data a partire dalla quale i componenti possono essere smontati nell'edificio di origine |
| Smontaggio fino al | `donorBuildingDismantlingEndDate` | AAAA-MM-GG | Estensione |  |  | Data entro la quale lo smontaggio dei componenti deve essere concluso |
| Allegati | `donorBuildingAttachments` | Testo libero (più righe) | Estensione |  |  | Denominazione e ubicazione dei documenti relativi all'edificio di origine, ad esempio piani o perizia sulle sostanze nocive |

## Campi di dati Componenti di riuso

### Identificazione

| Campo | Chiave | Formato | Livello | Livello I | Livello II | Definizione |
| --- | --- | --- | --- | --- | --- | --- |
| Denominazione | `name` | Testo libero (una riga) | Nucleo | Obbligatorio | Obbligatorio | Denominazione breve |
| ID del componente | `componentId` | Testo libero (una riga) | Nucleo |  | Obbligatorio | Numero di identificazione del DPP; il formato e l'assegnazione dell'ID non sono prescritti dallo Swiss Inv |
| Codice eCCC-E | `ebkphCode` | Elenco di selezione → [ebkph](#list-ebkph) | Nucleo | Obbligatorio | Obbligatorio | Secondo eCCC-E SN 506 511; codice e denominazione vanno indicati in campi separati; una selezione di codici possibili è riportata nella tabella di riferimento eCCC-E |
| Denominazione eCCC-E | `ebkphLabel` | Testo libero (una riga) | Nucleo | Obbligatorio | Obbligatorio | Denominazione corrispondente al codice eCCC-E; codice e denominazione vanno indicati in campi separati |
| Ubicazione nell'edificio di origine | `positionInDonorBuilding` | Testo libero (più righe) | Nucleo |  | Raccomandato | Descrizione dell'ubicazione nell'edificio di origine, ad esempio piano, locale ecc. |
| UUID | `uuid` | UUID | Estensione |  |  | secondo ISO/IEC 9834-8:2014; garantisce l'identificazione univoca a livello mondiale |
| UUID della posizione principale | `parentUuid` | UUID | Estensione |  |  | Indica l'appartenenza a una posizione complessiva sovraordinata |
| Codice eBKP-Gate | `ebkpGateCode` | Elenco di selezione → [ebkp-gate](#list-ebkp-gate) | Estensione |  |  | Secondo eBKP-Gate; codice e denominazione vanno indicati in campi separati |
| Denominazione eBKP-Gate | `ebkpGateLabel` | Testo libero (una riga) | Estensione |  |  | Denominazione corrispondente al codice eBKP-Gate; codice e denominazione vanno indicati in campi separati |

### Quantità

| Campo | Chiave | Formato | Livello | Livello I | Livello II | Definizione |
| --- | --- | --- | --- | --- | --- | --- |
| Quantità (min) | `quantityMin` | Valore numerico | Nucleo | Obbligatorio | Obbligatorio | La quantità può essere indicata volutamente in modo approssimativo come intervallo con limite inferiore e superiore; per un'indicazione precisa inserire lo stesso valore in entrambi i campi |
| Quantità (max) | `quantityMax` | Valore numerico | Nucleo | Obbligatorio | Obbligatorio | La quantità può essere indicata volutamente in modo approssimativo come intervallo con limite inferiore e superiore; per un'indicazione precisa inserire lo stesso valore in entrambi i campi |
| Unità | `unit` | Elenco di selezione → [unit](#list-unit) | Nucleo | Obbligatorio | Obbligatorio | Si raccomanda un'unità adatta al collocamento dei componenti |
| Informazioni supplementari sulla quantità | `quantityNotes` | Testo libero (più righe) | Estensione |  |  | Informazioni supplementari sulla quantità, ad esempio altre grandezze di riferimento |

### Dimensioni

| Campo | Chiave | Formato | Livello | Livello I | Livello II | Definizione |
| --- | --- | --- | --- | --- | --- | --- |
| Dimensione esterna altezza | `zDim` | Valore numerico [cm] | Nucleo |  | Obbligatorio | Le tre dimensioni esterne mirano a uniformare l'indicazione delle misure per il maggior numero possibile di forme di componenti; si basano sul parallelepipedo di delimitazione dello standard IFC di buildingSMART |
| Dimensione esterna larghezza | `yDim` | Valore numerico [cm] | Nucleo |  | Obbligatorio | Le tre dimensioni esterne mirano a uniformare l'indicazione delle misure per il maggior numero possibile di forme di componenti; si basano sul parallelepipedo di delimitazione dello standard IFC di buildingSMART |
| Dimensione esterna profondità / lunghezza | `xDim` | Valore numerico [cm] | Nucleo |  | Obbligatorio | Le tre dimensioni esterne mirano a uniformare l'indicazione delle misure per il maggior numero possibile di forme di componenti; si basano sul parallelepipedo di delimitazione dello standard IFC di buildingSMART |
| Indicazioni libere sulle dimensioni | `dimensionNotes` | Testo libero (più righe) | Nucleo |  | Obbligatorio | Indicazione delle dimensioni rilevanti non coperte dalle dimensioni esterne o da altri attributi |

### Dettagli

| Campo | Chiave | Formato | Livello | Livello I | Livello II | Definizione |
| --- | --- | --- | --- | --- | --- | --- |
| Ulteriori informazioni | `description` | Testo libero (più righe) | Nucleo | Raccomandato | Raccomandato | Descrizione delle proprietà rilevanti non coperte dalle dimensioni esterne o da altri attributi |
| Categoria di materiale | `material` | Elenco di selezione (scelta multipla) → [material](#list-material) | Nucleo | Obbligatorio | Obbligatorio | Categorie di materiale di cui il componente è principalmente costituito; se ne possono scegliere più d'una, ad esempio, per una finestra in legno, legno massiccio per il telaio e vetro per la vetratura |
| Informazioni supplementari sul materiale | `materialNotes` | Testo libero (più righe) | Nucleo |  | Obbligatorio | Precisazioni sul materiale non coperte dalla categoria di materiale |

### Valutazione

| Campo | Chiave | Formato | Livello | Livello I | Livello II | Definizione |
| --- | --- | --- | --- | --- | --- | --- |
| Perizia sulle sostanze nocive | `pollutantReport` | Elenco di selezione → [pollutant-report](#list-pollutant-report) | Nucleo |  | Obbligatorio | Indica se per il componente è disponibile una valutazione della contaminazione mediante perizia sulle sostanze nocive |
| Stato visivo | `visualCondition` | Elenco di selezione → [visual-condition](#list-visual-condition) | Nucleo |  | Obbligatorio | Eventuali precisazioni sullo stato visivo possono essere aggiunte nel campo «Spiegazione della raccomandazione» |
| Stato funzionale | `functionalCondition` | Elenco di selezione → [functional-condition](#list-functional-condition) | Nucleo |  | Obbligatorio | Eventuali precisazioni sullo stato funzionale possono essere aggiunte nel campo «Spiegazione della raccomandazione» |
| Onere di smontaggio | `demountability` | Elenco di selezione → [demountability](#list-demountability) | Nucleo |  | Obbligatorio | Eventuali precisazioni sull'onere di smontaggio possono essere aggiunte nel campo «Spiegazione della raccomandazione» |
| Raccomandazione rilievo dettagliato | `recDetailedAssessment` | Elenco di selezione → [rec-detailed-assessment](#list-rec-detailed-assessment) | Nucleo | Obbligatorio |  | L'auditor dell'audit di riuso di livello I raccomanda se effettuare un rilievo approfondito del componente nell'audit di riuso di livello II |
| Raccomandazione collocamento | `recDistribution` | Elenco di selezione → [rec-distribution](#list-rec-distribution) | Nucleo |  | Obbligatorio | L'auditor dell'audit di riuso di livello II raccomanda se puntare al collocamento del componente |
| Spiegazione della raccomandazione | `recNotes` | Testo libero (più righe) | Nucleo |  | Raccomandato | Eventuali precisazioni sulla valutazione e sulla raccomandazione di collocamento del componente |
| Informazioni supplementari sulle sostanze nocive | `pollutantNotes` | Testo libero (più righe) | Estensione |  |  | Indicazioni supplementari sulla perizia, ad esempio autore, data nonché tipo e grado di contaminazione |
| Tipo di collegamento | `connection` | Elenco di selezione (scelta multipla) → [connection](#list-connection) | Estensione |  |  | Si intendono tutti i collegamenti rilevanti per lo smontaggio o il montaggio del componente; le informazioni supplementari non coperte dall'elenco di selezione possono essere aggiunte come testo libero nel campo «Informazioni supplementari sul tipo di collegamento» |
| Informazioni supplementari sul tipo di collegamento | `connectionNotes` | Testo libero (più righe) | Estensione |  |  | Informazioni supplementari sul collegamento non coperte dall'elenco di selezione |

### Logistica

| Campo | Chiave | Formato | Livello | Livello I | Livello II | Definizione |
| --- | --- | --- | --- | --- | --- | --- |
| Stato di riuso | `reUseStatus` | Elenco di selezione → [reuse-status](#list-reuse-status) | Estensione |  |  | Stato attuale del componente nel processo di riuso |
| Codice postale dell'ubicazione | `locationPostalCode` | Codice postale | Estensione |  |  | Codice postale dell'ubicazione attuale del componente |
| Paese dell'ubicazione | `locationCountry` | Codice paese secondo ISO 3166 | Estensione |  |  | Paese dell'ubicazione attuale del componente come codice paese a due lettere secondo ISO 3166-1 (ad es. CH) |
| Data di entrata a magazzino | `storageStartDate` | AAAA-MM-GG | Estensione |  |  | Data in cui il componente è stato immagazzinato |
| Data di uscita dal magazzino | `storageEndDate` | AAAA-MM-GG | Estensione |  |  | Data in cui il componente è uscito dal magazzino o deve uscirne al più tardi |
| Informazioni supplementari sulla logistica | `logisticsNotes` | Testo libero (più righe) | Estensione |  |  | Informazioni supplementari su stoccaggio, imballaggio e trasporto del componente |

### Condizioni

| Campo | Chiave | Formato | Livello | Livello I | Livello II | Definizione |
| --- | --- | --- | --- | --- | --- | --- |
| Data di inizio disponibilità | `availabilityStartDate` | AAAA-MM-GG | Estensione |  |  | Data a partire dalla quale il componente è disponibile per gli acquirenti |
| Data di fine disponibilità | `availabilityEndDate` | AAAA-MM-GG | Estensione |  |  | Data fino alla quale il componente è disponibile per gli acquirenti |
| Prezzo di vendita | `price` | Valore numerico [CHF] | Estensione |  |  | Prezzo di vendita in franchi svizzeri per unità scelta per l'indicazione della quantità |
| Condizioni di consegna | `handoverConditions` | Testo libero (più righe) | Estensione |  |  | Condizioni di consegna, ad esempio ritiro presso l'edificio di origine o il magazzino, smontaggio a cura dell'acquirente, termini |

### Analisi

| Campo | Chiave | Formato | Livello | Livello I | Livello II | Definizione |
| --- | --- | --- | --- | --- | --- | --- |
| Risparmio di gas serra per unità | `emissionSavingsPerUnit` | Valore numerico [kg CO₂-eq] | Estensione |  |  | Secondo KBOB; si intende il risparmio approssimativo di gas serra ottenuto con il riuso del componente rispetto a una nuova produzione; il metodo andrebbe descritto nel campo «Informazioni supplementari sull'ecobilancio» |
| Risparmio di gas serra | `emissionSavings` | Valore numerico [kg CO₂-eq] | Estensione |  |  | Risparmio totale di gas serra per la quantità indicata; metodo come per «Risparmio di gas serra per unità» |
| Informazioni supplementari sull'ecobilancio | `emissionNotes` | Testo libero (più righe) | Estensione |  |  | Precisazioni sul bilancio dei gas serra o indicazioni su altri indicatori climatici e ambientali |

### Altri attributi

| Campo | Chiave | Formato | Livello | Livello I | Livello II | Definizione |
| --- | --- | --- | --- | --- | --- | --- |
| Fabbricante | `manufacturer` | Testo libero (una riga) | Estensione |  |  | Nome dell'impresa che ha fabbricato il componente |
| Denominazione del prodotto | `productName` | Testo libero (una riga) | Estensione |  |  | Denominazione completa del prodotto o nome commerciale del componente |
| Anno di posa | `yearOfInstallation` | AAAA | Estensione |  |  | Anno in cui il componente è stato posato nell'edificio di origine |
| Anno di fabbricazione | `yearOfManufacture` | AAAA | Estensione |  |  | Anno in cui il componente è stato fabbricato |
| Colore | `color` | Testo libero (una riga) | Estensione |  |  | Colori rilevanti del componente |
| Peso | `weight` | Valore numerico [kg] | Estensione |  |  | Peso per unità scelta per l'indicazione della quantità |
| Esposizione alle intemperie | `weatheringExposure` | Testo libero (una riga) | Estensione |  |  | Indica se e in che misura il componente è stato esposto alle intemperie, ad esempio interno, esterno protetto, esterno esposto |
| Zona nell'edificio | `zoneInDonorBuilding` | Testo libero (una riga) | Estensione |  |  | Zona o settore dell'edificio di origine a cui è attribuito il componente |
| Materiale secondo KBOB | `materialKbob` | Testo libero (più righe) | Estensione |  |  | Materiali del componente secondo l'elenco KBOB, con la rispettiva quota |
| Colore in HEX | `colorInHex` | Testo libero (una riga) | Estensione |  |  | Colore del componente come valore esadecimale, ad esempio #A0522D |
| Garanzia | `warranty` | Testo libero (più righe) | Estensione |  |  | Indicazioni su una garanzia concessa per il componente riutilizzato |
| Prezzo originale | `priceOriginal` | Valore numerico [CHF] | Estensione |  |  | Prezzo a nuovo del componente in franchi svizzeri, se noto |
| Difetti | `defects` | Testo libero (più righe) | Estensione |  |  | Difetti o danni noti del componente |

### Dati tecnici

| Campo | Chiave | Formato | Livello | Livello I | Livello II | Definizione |
| --- | --- | --- | --- | --- | --- | --- |
| Valore U | `uValue` | Valore numerico [W/m²K] | Estensione |  |  | Coefficiente di trasmissione termica del componente secondo le indicazioni del fabbricante o una misurazione |
| Volume utile in litri | `volumeInLiters` | Valore numerico [l] | Estensione |  |  | Volume utile del componente in litri, ad esempio per serbatoi o vasche |
| Volume utile in metri cubi | `volumeInM3` | Valore numerico [m³] | Estensione |  |  | Volume utile del componente in metri cubi, ad esempio per container o silos |
| Allacciamento elettrico | `electricConnector` | Testo libero (una riga) | Estensione |  |  | Tipo di allacciamento elettrico, ad esempio tipo di spina o allacciamento fisso |
| Tensione elettrica | `electricVoltage` | Valore numerico [V] | Estensione |  |  | Tensione nominale del componente |
| Potenza elettrica | `electricWatt` | Valore numerico [W] | Estensione |  |  | Potenza nominale del componente |
| Intensità di corrente | `electricAmp` | Valore numerico [A] | Estensione |  |  | Corrente nominale del componente |
| Norma per cucine | `kitchenNorm` | Testo libero (una riga) | Estensione |  |  | Norma dimensionale degli elementi di cucina, ad esempio SMS (55 cm) o EURO (60 cm) |
| Interasse dei fori | `holeSpacing` | Valore numerico [mm] | Estensione |  |  | Distanza tra i fori di fissaggio o di raccordo, misurata da centro a centro |

### Piattaforma

| Campo | Chiave | Formato | Livello | Livello I | Livello II | Definizione |
| --- | --- | --- | --- | --- | --- | --- |
| Attivato sulla piattaforma | `activeOnPlatform` | Sì/No | Estensione |  |  | Indica se il componente è visibile sulla piattaforma di collocamento |
| Offerta in evidenza sulla piattaforma | `topOfferOnPlatform` | Sì/No | Estensione |  |  | Indica se il componente è messo in evidenza sulla piattaforma |
| Modalità di pagamento | `paymentMethod` | Testo libero (una riga) | Estensione |  |  | Modalità di pagamento ammesse, ad esempio fattura o pagamento anticipato |
| Modalità di spedizione | `shippingMethod` | Testo libero (una riga) | Estensione |  |  | Modalità di consegna possibili, ad esempio ritiro o spedizioniere |
| Scorte riservate | `reservedStock` | Valore numerico | Estensione |  |  | Quantità già riservata per gli acquirenti, nell'unità scelta |

## Campi di dati Registro delle modifiche

### Registro delle modifiche

| Campo | Chiave | Formato | Livello | Definizione |
| --- | --- | --- | --- | --- |
| Autore | `logAuthor` | Testo libero (una riga) | Estensione | Persona che ha creato la voce |
| Data | `logDate` | AAAA-MM-GG | Estensione | Data dell'evento |
| Evento | `logEvent` | Testo libero (una riga) | Estensione | Che cosa è stato creato o modificato, ad esempio «Audit livello I redatto» |
| Telefono | `logPhone` | Numero di telefono | Estensione | Numero di telefono dell'autore |
| E-mail | `logEmail` | Indirizzo e-mail | Estensione | Indirizzo e-mail dell'autore |

## Elenchi di selezione

<a id="list-ebkph"></a>

### eCCC-E (selezione di riferimento) (`ebkph`)

Nucleo

Segnaposto. I codici e le denominazioni secondo eCCC-E SN 506 511 non sono riportati qui. L'eCCC-E andrebbe indicato solo a livello di gruppo di elementi o di elemento.

| Chiave | Denominazione | Definizione |
| --- | --- | --- |
| `XY00` | Empty |  |
| `YZ00` | Empty |  |

<a id="list-unit"></a>

### Unità (`unit`)

Nucleo

| Chiave | Denominazione | Definizione |
| --- | --- | --- |
| `pc` | pz. | Pezzo |
| `m` | ml | Metro lineare |
| `m2` | m² | Metro quadrato |
| `m3` | m³ | Metro cubo |
| `kg` | kg | Chilogrammo |
| `t` | t | Tonnellata |
| `na` | Nessuna indicazione | Unità sconosciuta |

<a id="list-material"></a>

### Categoria di materiale (`material`)

Nucleo

| Chiave | Denominazione | Gruppo | Definizione |
| --- | --- | --- | --- |
| `me00` | Metallo | Metallico |  |
| `me01` | Acciaio e ghisa | Metallico |  |
| `me02` | Alluminio | Metallico |  |
| `me03` | Rame | Metallico |  |
| `on00` | Materiali vegetali e animali | Organico: naturale |  |
| `on01` | Legno massiccio | Organico: naturale |  |
| `on02` | Materiale a base di legno | Organico: naturale |  |
| `os01` | Materia plastica | Organico: sintetico |  |
| `os02` | Bitume | Organico: sintetico |  |
| `mi00` | Materiali da costruzione minerali | Minerale |  |
| `mi01` | Pietra naturale | Minerale |  |
| `mi02` | Calcestruzzo e materiali a base di cemento | Minerale |  |
| `mi03` | Ceramica | Minerale |  |
| `mi04` | Gesso | Minerale |  |
| `mi05` | Vetro | Minerale |  |
| `mi06` | Lana minerale | Minerale |  |
| `co01` | Composito | Composito |  |
| `un01` | Sconosciuto | Sconosciuto |  |

<a id="list-pollutant-report"></a>

### Perizia sulle sostanze nocive (`pollutant-report`)

Nucleo

| Chiave | Denominazione | Definizione |
| --- | --- | --- |
| `available` | Disponibile | Per il componente interessato è disponibile una valutazione della contaminazione mediante perizia sulle sostanze nocive |
| `notAvailable` | Non disponibile | Per il componente interessato non è disponibile una valutazione della contaminazione mediante perizia sulle sostanze nocive |

<a id="list-visual-condition"></a>

### Stato visivo (`visual-condition`)

Nucleo

| Chiave | Denominazione | Definizione |
| --- | --- | --- |
| `0` | Nessuna valutazione |  |
| `1` | Come nuovo |  |
| `2` | Lievi tracce d'uso |  |
| `3` | Forti tracce d'uso |  |
| `4` | Danneggiato |  |

<a id="list-functional-condition"></a>

### Stato funzionale (`functional-condition`)

Nucleo

| Chiave | Denominazione | Definizione |
| --- | --- | --- |
| `0` | Nessuna valutazione |  |
| `1` | Pienamente funzionante |  |
| `2` | Funzionamento limitato |  |
| `3` | Difettoso (riparabile) |  |
| `4` | Difettoso (irreparabile) |  |

<a id="list-demountability"></a>

### Onere di smontaggio (`demountability`)

Nucleo

| Chiave | Denominazione | Definizione |
| --- | --- | --- |
| `0` | Nessuna valutazione |  |
| `1` | Molto semplice |  |
| `2` | Semplice |  |
| `3` | Oneroso |  |
| `4` | Molto oneroso |  |

<a id="list-rec-detailed-assessment"></a>

### Raccomandazione rilievo dettagliato (`rec-detailed-assessment`)

Nucleo

| Chiave | Denominazione | Definizione |
| --- | --- | --- |
| `unknown` | Nessuna indicazione | L'auditor non formula alcuna raccomandazione |
| `yes` | Sì | L'auditor dell'audit di riuso di livello I raccomanda un rilievo approfondito del componente nell'audit di riuso di livello II |
| `no` | No | L'auditor dell'audit di riuso di livello I non raccomanda un rilievo approfondito del componente nell'audit di riuso di livello II |

<a id="list-rec-distribution"></a>

### Raccomandazione collocamento (`rec-distribution`)

Nucleo

| Chiave | Denominazione | Definizione |
| --- | --- | --- |
| `unknown` | Nessuna indicazione | L'auditor non formula alcuna raccomandazione |
| `yes` | Sì | L'auditor dell'audit di riuso di livello II raccomanda di puntare al collocamento del componente |
| `no` | No | L'auditor dell'audit di riuso di livello II non raccomanda di puntare al collocamento del componente |

<a id="list-gwr-gkat"></a>

### Categoria di edificio (REA GKAT) (`gwr-gkat`)

Nucleo

Codici e denominazioni ripresi alla lettera dal catalogo delle caratteristiche del Registro federale degli edifici e delle abitazioni (UST): tedesco e francese dalla versione 5.0.0, italiano e inglese dalla versione 4.3.2.

| Chiave | Denominazione | Definizione |
| --- | --- | --- |
| `1010` | Abitazione provvisoria |  |
| `1020` | Edificio ad uso esclusivamente abitativo |  |
| `1030` | Altro edificio abitativo (con utilizzazione accessoria) |  |
| `1040` | Edificio ad uso parzialmente abitativo |  |
| `1060` | Edificio ad uso non abitativo |  |
| `1080` | Costruzione speciale |  |

<a id="list-gwr-gklas"></a>

### Classe di edificio (REA GKLAS) (`gwr-gklas`)

Nucleo

Codici e denominazioni ripresi alla lettera dal catalogo delle caratteristiche del Registro federale degli edifici e delle abitazioni (UST): tedesco e francese dalla versione 5.0.0, italiano e inglese dalla versione 4.3.2.

| Chiave | Denominazione | Definizione |
| --- | --- | --- |
| `1110` | Edifici ad una abitazione |  |
| `1121` | Edifici a due abitazioni |  |
| `1122` | Edifici a tre e più abitazioni |  |
| `1130` | Residenze per collettività |  |
| `1211` | Alberghi |  |
| `1212` | Altri edifici per abitazione di breve durata |  |
| `1220` | Fabbricati per uffici |  |
| `1230` | Fabbricati per il commercio all'ingrosso e al dettaglio |  |
| `1231` | Ristoranti e bar in edifici non residenziali |  |
| `1241` | Stazioni, terminal, centrali telefoniche |  |
| `1242` | Fabbricati per garage |  |
| `1251` | Fabbricati industriali |  |
| `1252` | Serbatoi, silos e depositi |  |
| `1261` | Edifici destinati ad attività ricreative o culturali |  |
| `1262` | Musei e biblioteche |  |
| `1263` | Edifici scolastici, universitari ed edifici di ricerca |  |
| `1264` | Edifici per fini ospedalieri e di assistenza sociale |  |
| `1265` | Sale sportive |  |
| `1272` | Edifici utilizzati come luoghi di culto e per attività religiose |  |
| `1273` | Monumenti storici o protetti |  |
| `1274` | Altri edifici, n.c.a. |  |
| `1275` | Altri edifici che ospitano collettività |  |
| `1276` | Edifici per la tenuta di animali |  |
| `1277` | Edifici per le colture vegetali |  |
| `1278` | Altri fabbricati rurali non residenziali |  |

<a id="list-gwr-gbaup"></a>

### Epoca di costruzione (REA GBAUP) (`gwr-gbaup`)

Nucleo

Codici e denominazioni ripresi alla lettera dal catalogo delle caratteristiche del Registro federale degli edifici e delle abitazioni (UST): tedesco e francese dalla versione 5.0.0, italiano e inglese dalla versione 4.3.2.

| Chiave | Denominazione | Definizione |
| --- | --- | --- |
| `8011` | Periodo prima del 1919 |  |
| `8012` | Periodo dal 1919 al 1945 |  |
| `8013` | Periodo dal 1946 al 1960 |  |
| `8014` | Periodo dal 1961 al 1970 |  |
| `8015` | Periodo dal 1971 al 1980 |  |
| `8016` | Periodo dal 1981 al 1985 |  |
| `8017` | Periodo dal 1986 al 1990 |  |
| `8018` | Periodo dal 1991 al 1995 |  |
| `8019` | Periodo dal 1996 al 2000 |  |
| `8020` | Periodo dal 2001 al 2005 |  |
| `8021` | Periodo dal 2006 al 2010 |  |
| `8022` | Periodo dal 2011 al 2015 |  |
| `8023` | Periodo a partire dal 2016 |  |

<a id="list-construction-type"></a>

### Tipo di costruzione (`construction-type`)

Estensione

| Chiave | Denominazione | Definizione |
| --- | --- | --- |
| `solidHeavy` | Costruzione massiccia pesante |  |
| `solidLight` | Costruzione massiccia leggera |  |
| `logTimber` | Costruzione a blockbau in legno |  |
| `lightTimber` | Costruzione leggera in legno |  |
| `lightSteel` | Costruzione leggera in acciaio |  |
| `mixed` | Costruzione mista |  |
| `modular` | Costruzione modulare |  |

<a id="list-connection"></a>

### Tipo di collegamento (`connection`)

Estensione

| Chiave | Denominazione | Definizione |
| --- | --- | --- |
| `0` | Nessuna indicazione |  |
| `1` | Posato libero |  |
| `2` | Avvitato / A innesto |  |
| `3` | Inchiodato / Rivettato |  |
| `4` | Fissato in modo permanente |  |
| `unknown` | Collegamento sconosciuto |  |
| `screwed` | Avvitato |  |
| `nailed` | Inchiodato |  |
| `glued` | Incollato |  |
| `welded` | Saldato |  |
| `riveted` | Rivettato |  |
| `interlocked` | A incastro | ad es. nei collegamenti in legno |
| `plugged` | A innesto | ad es. nei collegamenti in lamiera |
| `clamped` | Serrato |  |
| `clipped` | A clip | ad es. negli elementi in plastica |
| `flanged` | Bordato | ad es. nei raccordi di tubi |
| `dowelled` | A tenone e mortasa | ad es. collegamenti tradizionali in legno |
| `soldered` | Brasato | ad es. nei tubi metallici |
| `other` | Altro |  |

<a id="list-reuse-status"></a>

### Stato di riuso (`reuse-status`)

Estensione

| Chiave | Denominazione | Definizione |
| --- | --- | --- |
| `unknown` | Nessuna indicazione |  |
| `installedInDonorBuilding` | Installato nell'edificio di origine | Il componente è installato nell'edificio di origine |
| `demounted` | Smontato | Il componente è smontato |
| `stored` | A magazzino | Il componente è depositato temporaneamente in un magazzino |
| `reused` | Riutilizzato | Il componente è stato riutilizzato con successo in un edificio di destinazione |
| `retainedInPlace` | Mantenimento in opera | Il componente non viene riutilizzato perché resta nell'edificio esistente |
| `noReuse` | Nessun riuso | Il componente non viene riutilizzato né conservato, ma ad es. riciclato o smaltito |

<a id="list-ebkp-gate"></a>

### eBKP-Gate (`ebkp-gate`)

Estensione

Classificazione esterna; lo Swiss Inv non contiene un proprio elenco di selezione.

## Formati

| Chiave | Denominazione |
| --- | --- |
| `text` | Testo libero (una riga) |
| `multiline` | Testo libero (più righe) |
| `number` | Valore numerico |
| `boolean` | Sì/No |
| `code` | Elenco di selezione / Elenco di selezione (scelta multipla) |
| `contact` | Contatto |
| `country` | Codice paese secondo ISO 3166 |
| `phone` | Numero di telefono |
| `email` | Indirizzo e-mail |
| `uuid` | UUID |
| `year` | AAAA |
| `date` | AAAA-MM-GG |
| `postalCode` | Codice postale |

## Obbligo

| Chiave | Denominazione |
| --- | --- |
| `muss` | Obbligatorio |
| `sollte` | Raccomandato |

## Unità

| Simbolo | Denominazione |
| --- | --- |
| mm | Millimetro |
| cm | Centimetro |
| m² | Metro quadrato |
| m³ | Metro cubo |
| l | Litro |
| kg | Chilogrammo |
| kg CO₂-eq | Chilogrammo di CO₂ equivalente |
| CHF | Franco svizzero |
| W/m²K | Watt per metro quadrato kelvin |
| V | Volt |
| W | Watt |
| A | Ampere |
