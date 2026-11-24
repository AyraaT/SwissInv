# Introduzione
In elaborazione…

# Audit di riuso

<!-- Le tabelle tra GENERIERT:START e GENERIERT:ENDE sono generate da tools/build.py a partire da data/core/audits/. Modificarle lì, non qui. Il resto del testo è redatto a mano. -->
## Scopo ed estensione
L'audit di riuso serve a rilevare i componenti edilizi esistenti interessati da una trasformazione o da una decostruzione, per i quali va esaminata la possibilità di riuso.

A tal fine, in un rapporto vengono rilevati i dati del progetto, degli edifici e dei componenti. Questi dati devono costituire la base per scegliere quali componenti collocare presso acquirenti interni o esterni.

Se necessario, il rilevamento può avvenire in due livelli. Il livello I è una stima sommaria volta a stabilire se la sostanza edilizia considerata si presta al riuso e quindi a un rilievo approfondito nel livello II. Vengono inoltre delimitati i gruppi di componenti per i quali si raccomanda un rilievo approfondito nel livello II.

Il livello II è un rilievo approfondito dei componenti. Può essere scelto sulla base della raccomandazione del livello I oppure senza esame preliminare. Il livello II ha lo scopo di selezionare i componenti idonei al collocamento presso acquirenti.
## Livello di osservazione e strutturazione
Per strutturare l'audit di riuso occorre stabilire come l'intervento viene suddiviso in progetti, edifici e cataloghi di componenti.

Anzitutto va indicato nel modo più preciso possibile il perimetro della sostanza edilizia interessata, compresi gli spazi esterni circostanti ed eventualmente le tappe di costruzione.

Riunire più edifici in un unico progetto è opportuno, ad esempio, quando gli edifici vengono decostruiti o trasformati nello stesso periodo e un catalogo di componenti comune può essere considerato per tutti gli oggetti.

Per ogni progetto, i dati del progetto e i partecipanti vanno rilevati una sola volta secondo la tabella X: «Campi di dati Progetto».

Per tutti gli edifici di un progetto vanno rilevati i dati degli edifici secondo la tabella X: «Campi di dati Edifici di origine». Per edifici identici o collegati, tali dati possono essere riuniti e indicati una sola volta.

L'estensione del rilevamento dei dati dei componenti differisce tra i livelli I e II dell'audit di riuso e risulta dalle sezioni seguenti. La strutturazione e i livelli di osservazione dei componenti non sono prescritti dallo Swiss Inv.
## Audit di riuso livello I: scopo e procedimento
L'audit di riuso livello I serve a stimare sommariamente il potenziale di riuso dei componenti di un edificio di origine. Consente una prima valutazione dell'opportunità e dell'estensione di un esame approfondito. Per un rilevamento adeguato alle esigenze, prima del sopralluogo andrebbero comunicati al mandatario gli obiettivi del committente e il perimetro della sostanza edilizia interessata.

La stima del potenziale costituisce la base per un approfondimento mirato e adeguato alle esigenze. In particolare vanno delimitati i gruppi di componenti rilevanti per un esame approfondito.

Al termine dell'audit il committente riceve un rapporto che funge da base decisionale per le seguenti domande:

- Occorre eseguire un audit di riuso livello II per l'edificio di origine esaminato?

- Quali gruppi di componenti vanno rilevati e valutati in modo approfondito nell'ambito dell'audit di riuso livello II?

Una volta concluso il rapporto, i risultati andrebbero confrontati con gli obiettivi e le risorse del committente per decidere come procedere.
## Audit di riuso livello I: formato ed estensione
L'audit di riuso livello I comprende le seguenti sezioni:

- Progetto: indicazioni sul progetto e sui partecipanti

- Introduzione: descrizione del progetto, obiettivi, scadenze, perimetro, basi (ad es. piani / rapporto sulle sostanze nocive) e procedimento del mandatario

- Edifici: indicazioni sugli edifici di origine considerati

- Componenti: rilevamento sommario di tutti i componenti, ciascuno con la raccomandazione a favore o contro un rilievo approfondito

- Conclusione: raccomandazione motivata a favore o contro un audit di riuso livello II degli edifici di origine considerati

Il formato di consegna va concordato tra committente e mandatario. Si raccomanda di consegnare l'intero rapporto in formato PDF.

I dati del progetto e degli edifici vanno rilevati secondo la sezione «Livello di osservazione e strutturazione».

Per il progetto e gli edifici di origine vanno rilevate almeno le informazioni della tabella seguente.

<!-- GENERIERT:START profil=stage-1 bereich=projekt -->
**Tabella: informazioni da rilevare su progetto ed edifici di origine nell'Audit di riuso livello I**

| Informazione | Obbligo | Campo | Chiave | Formato |
| --- | --- | --- | --- | --- |
| Nome del progetto | Obbligatorio | Nome del progetto | `projectName` | Testo libero (una riga) |
| Proprietario, committente e mandatario | Obbligatorio | Proprietario | `projectOwner` | Contatto |
|  |  | Committente | `projectAuditClient` | Contatto |
|  |  | Mandatario | `projectAuditor` | Contatto |
| Indirizzo dell'edificio di origine | Obbligatorio | Via | `donorBuildingStreet` | Testo libero (una riga) |
|  |  | Numero civico | `donorBuildingHouseNumber` | Testo libero (una riga) |
|  |  | Codice postale | `donorBuildingPostalCode` | Codice postale |
|  |  | Località | `donorBuildingCity` | Testo libero (una riga) |
| Paese dell'edificio di origine | Raccomandato | Paese | `donorBuildingCountry` | Codice paese secondo ISO 3166 |
| Dati dell'edificio secondo il REA e tipo di costruzione | Raccomandato | Classe di edificio | `donorBuildingGklas` | Elenco di selezione |
|  |  | Categoria di edificio | `donorBuildingGkat` | Elenco di selezione |
|  |  | Epoca di costruzione | `donorBuildingGbaup` | Elenco di selezione |
|  |  | Tipo di costruzione | `donorBuildingConstructionType` | Elenco di selezione |
|  |  | Anno di costruzione dell'edificio | `donorBuildingGbauj` | AAAA |
|  |  | Volume dell'edificio | `donorBuildingGvol` | Valore numerico [m³] |
|  |  | Superficie dell'edificio | `donorBuildingGarea` | Valore numerico [m²] |
|  |  | Numero di piani | `donorBuildingGastw` | Valore numerico |
<!-- GENERIERT:ENDE -->

Per ogni componente vanno rilevate almeno le informazioni indicate come «Obbligatorio» nella colonna «Obbligo» della tabella X: «Informazioni da rilevare per componente nell'audit di riuso livello I». Nella colonna «Campo» sono raccomandati campi adeguati della tabella Y: «Campi di dati Componenti di riuso», da utilizzare per tali informazioni.

L'**indicazione della quantità** dei componenti può essere data in modo approssimativo come intervallo. Affinché i limiti inferiore e superiore dell'intervallo siano leggibili da macchina, i campi Quantità (min) e Quantità (max) vanno indicati come valori numerici. Una quantità verificata può essere segnalata inserendo la stessa quantità in entrambi i campi.

Una **valutazione della contaminazione da sostanze nocive** ai fini del riuso non fa parte dei requisiti minimi degli audit di riuso livello I.

Le **ulteriori proprietà** dei componenti vanno rilevate come testo nel campo «Ulteriori informazioni» o in altri campi adeguati. Per uno scambio di dati ottimale vanno preferiti a tal fine i campi standardizzati della tabella Y: «Campi di dati Componenti di riuso».

<!-- GENERIERT:START profil=stage-1 bereich=bauteile -->
**Tabella: informazioni da rilevare per componente nell'Audit di riuso livello I**

| Informazione | Obbligo | Campo | Chiave | Formato |
| --- | --- | --- | --- | --- |
| Denominazione breve | Obbligatorio | Denominazione | `name` | Testo libero (una riga) |
| eCCC-E | Obbligatorio | Codice eCCC-E | `ebkphCode` | Elenco di selezione |
|  |  | Denominazione eCCC-E | `ebkphLabel` | Testo libero (una riga) |
| Quantità, eventualmente approssimativa, con indicazione dell'imprecisione | Obbligatorio | Quantità (min) | `quantityMin` | Valore numerico |
|  |  | Quantità (max) | `quantityMax` | Valore numerico |
|  |  | Unità | `unit` | Elenco di selezione |
| Almeno una categoria di materiale | Obbligatorio | Categoria di materiale | `material` | Elenco di selezione (scelta multipla) |
| Ulteriori informazioni | Raccomandato | Ulteriori informazioni | `description` | Testo libero (più righe) |
| Raccomandazione a favore o contro un rilievo approfondito | Obbligatorio | Raccomandazione rilievo dettagliato | `recDetailedAssessment` | Elenco di selezione |
<!-- GENERIERT:ENDE -->

Le definizioni e i formati dei campi si trovano nel [repertorio dei campi di dati](../dictionary/IT.md).

## Audit di riuso livello II: scopo e procedimento
L'audit di riuso livello II serve a preparare il collocamento dei componenti presso acquirenti interni o esterni. Per un rilevamento adeguato alle esigenze, prima del sopralluogo andrebbero comunicati al mandatario gli obiettivi del committente e il perimetro della sostanza edilizia interessata.

Al termine dell'audit il committente riceve un rapporto in base al quale è possibile scegliere quali componenti rendere visibili per un collocamento.

Le informazioni rilevate devono poter essere riutilizzate almeno per un chiarimento informale del fabbisogno presso potenziali acquirenti. A seconda delle strategie e dei canali di collocamento possono rendersi necessari chiarimenti di dettaglio supplementari sui componenti.

L'elaborazione delle strategie di collocamento, la gestione dei canali di collocamento e i chiarimenti supplementari per il collocamento non fanno parte dell'audit di riuso livello II. Queste prestazioni, che si basano sull'audit, non sono standardizzate dallo Swiss Inv.

Una volta concluso il rapporto, i risultati andrebbero confrontati con gli obiettivi e le risorse del committente per decidere come procedere.
## Audit di riuso livello II: formato ed estensione
L'audit di riuso livello II comprende le seguenti sezioni:

- Progetto: indicazioni sul progetto e sui partecipanti

- Introduzione: descrizione del progetto, obiettivi, scadenze, perimetro, basi (ad es. piani / rapporto sulle sostanze nocive) e procedimento del mandatario

- Edifici: indicazioni sugli edifici di origine considerati

- Componenti: rilievo approfondito di tutti i componenti, ciascuno con la raccomandazione a favore o contro il collocamento

- Conclusione: sintesi dei risultati

Il formato di consegna va concordato tra committente e mandatario. Si raccomanda di consegnare l'intero rapporto in formato PDF, i componenti rilevati in un formato di dati tabellare e i file immagine degli edifici e dei componenti.

I dati del progetto e degli edifici vanno rilevati secondo la sezione «Livello di osservazione e strutturazione».

Per il progetto e gli edifici di origine vanno rilevate almeno le informazioni della tabella seguente.

<!-- GENERIERT:START profil=stage-2 bereich=projekt -->
**Tabella: informazioni da rilevare su progetto ed edifici di origine nell'Audit di riuso livello II**

| Informazione | Obbligo | Campo | Chiave | Formato |
| --- | --- | --- | --- | --- |
| Nome del progetto | Obbligatorio | Nome del progetto | `projectName` | Testo libero (una riga) |
| Proprietario, committente e mandatario | Obbligatorio | Proprietario | `projectOwner` | Contatto |
|  |  | Committente | `projectAuditClient` | Contatto |
|  |  | Mandatario | `projectAuditor` | Contatto |
| Indirizzo dell'edificio di origine | Obbligatorio | Via | `donorBuildingStreet` | Testo libero (una riga) |
|  |  | Numero civico | `donorBuildingHouseNumber` | Testo libero (una riga) |
|  |  | Codice postale | `donorBuildingPostalCode` | Codice postale |
|  |  | Località | `donorBuildingCity` | Testo libero (una riga) |
| Paese dell'edificio di origine | Raccomandato | Paese | `donorBuildingCountry` | Codice paese secondo ISO 3166 |
| Dati dell'edificio secondo il REA e tipo di costruzione | Raccomandato | Classe di edificio | `donorBuildingGklas` | Elenco di selezione |
|  |  | Categoria di edificio | `donorBuildingGkat` | Elenco di selezione |
|  |  | Epoca di costruzione | `donorBuildingGbaup` | Elenco di selezione |
|  |  | Tipo di costruzione | `donorBuildingConstructionType` | Elenco di selezione |
|  |  | Anno di costruzione dell'edificio | `donorBuildingGbauj` | AAAA |
|  |  | Volume dell'edificio | `donorBuildingGvol` | Valore numerico [m³] |
|  |  | Superficie dell'edificio | `donorBuildingGarea` | Valore numerico [m²] |
|  |  | Numero di piani | `donorBuildingGastw` | Valore numerico |
| EGID e EGRID | Obbligatorio | EGID | `donorBuildingEgid` | Testo libero (una riga) |
|  |  | EGRID | `donorBuildingEgrid` | Testo libero (una riga) |
| Accesso | Obbligatorio | Accesso | `donorBuildingAccess` | Testo libero (più righe) |
<!-- GENERIERT:ENDE -->

Per ogni componente vanno rilevate almeno le informazioni indicate come «Obbligatorio» nella colonna «Obbligo» della tabella X: «Informazioni da rilevare per componente nell'audit di riuso livello II». Nella colonna «Campo» sono raccomandati campi adeguati della tabella Y: «Campi di dati Componenti di riuso», da utilizzare per tali informazioni.

L'**indicazione della quantità** dei componenti deve essere precisa. Una quantità verificata può essere segnalata indicando lo stesso valore in Quantità (min) e Quantità (max).

Una **valutazione della contaminazione da sostanze nocive** ai fini del riuso non fa parte dei requisiti minimi degli audit di riuso livello II. Il mandatario deve indicare nel campo «Perizia sulle sostanze nocive» se per il componente interessato è disponibile una valutazione della contaminazione mediante perizia sulle sostanze nocive. Le indicazioni supplementari sull'autore e sulla data della perizia nonché sul tipo e sul grado di contaminazione sono facoltative. Le conseguenze di una valutazione delle sostanze nocive per il riuso del componente possono essere interpretate solo da specialisti in sostanze nocive.

Per ogni componente va fornita almeno una **foto principale**. Inoltre andrebbero scattate almeno altre due foto che aggiungano informazioni utili su dettagli o viste d'insieme. L'attribuzione delle foto o degli altri allegati ai componenti interessati andrebbe garantita mediante una denominazione adeguata dei file.

Oltre ai campi obbligatori, **ulteriori proprietà** possono essere rilevate in campi supplementari adeguati. Per uno scambio di dati ottimale vanno preferiti a tal fine i campi standardizzati della tabella Y: «Campi di dati Componenti di riuso».

<!-- GENERIERT:START profil=stage-2 bereich=bauteile -->
**Tabella: informazioni da rilevare per componente nell'Audit di riuso livello II**

| Informazione | Obbligo | Campo | Chiave | Formato |
| --- | --- | --- | --- | --- |
| Denominazione breve | Obbligatorio | Denominazione | `name` | Testo libero (una riga) |
| ID del componente | Obbligatorio | ID del componente | `componentId` | Testo libero (una riga) |
| eCCC-E | Obbligatorio | Codice eCCC-E | `ebkphCode` | Elenco di selezione |
|  |  | Denominazione eCCC-E | `ebkphLabel` | Testo libero (una riga) |
| Ubicazione nell'edificio di origine | Raccomandato | Ubicazione nell'edificio di origine | `positionInDonorBuilding` | Testo libero (più righe) |
| Indicazione precisa della quantità | Obbligatorio | Quantità (min) | `quantityMin` | Valore numerico |
|  |  | Quantità (max) | `quantityMax` | Valore numerico |
|  |  | Unità | `unit` | Elenco di selezione |
| Dimensioni esterne del componente o dimensioni rilevanti specifiche della categoria | Obbligatorio | Dimensione esterna altezza | `zDim` | Valore numerico [cm] |
|  |  | Dimensione esterna larghezza | `yDim` | Valore numerico [cm] |
|  |  | Dimensione esterna profondità / lunghezza | `xDim` | Valore numerico [cm] |
|  |  | Indicazioni libere sulle dimensioni | `dimensionNotes` | Testo libero (più righe) |
| Almeno una categoria di materiale | Obbligatorio | Categoria di materiale | `material` | Elenco di selezione (scelta multipla) |
| Ulteriori indicazioni sul materiale | Obbligatorio | Informazioni supplementari sul materiale | `materialNotes` | Testo libero (più righe) |
| Ulteriori informazioni | Raccomandato | Ulteriori informazioni | `description` | Testo libero (più righe) |
| Rimando alla perizia sulle sostanze nocive | Obbligatorio | Perizia sulle sostanze nocive | `pollutantReport` | Elenco di selezione |
| Valutazione dello stato | Obbligatorio | Stato visivo | `visualCondition` | Elenco di selezione |
|  |  | Stato funzionale | `functionalCondition` | Elenco di selezione |
| Stima dell'onere di smontaggio | Obbligatorio | Onere di smontaggio | `demountability` | Elenco di selezione |
| Raccomandazione a favore o contro il collocamento | Obbligatorio | Raccomandazione collocamento | `recDistribution` | Elenco di selezione |
| Motivazione della raccomandazione | Raccomandato | Spiegazione della raccomandazione | `recNotes` | Testo libero (più righe) |
| Foto principale del componente | Obbligatorio | I file immagine e gli altri allegati non sono contenuti nel formato di dati tabellare; vanno consegnati separatamente |  |  |
| Almeno altre due foto d'insieme o di dettaglio | Raccomandato | I file immagine e gli altri allegati non sono contenuti nel formato di dati tabellare; vanno consegnati separatamente |  |  |
<!-- GENERIERT:ENDE -->

Le definizioni e i formati dei campi si trovano nel [repertorio dei campi di dati](../dictionary/IT.md).


# Requisiti per le interfacce digitali
In elaborazione…
