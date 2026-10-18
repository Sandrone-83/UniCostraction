---
name: heritage-conservation-diagnostics
description: Organizza conoscenza, rilievo diagnostico, stratigrafia e compatibilità degli interventi sul patrimonio culturale senza sostituire il conservatore, il progettista o l'autorizzazione del Ministero.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: conservazione del patrimonio e diagnostica
---

# Conservazione del patrimonio e diagnostica edilizia

## Attivazione e input

Attiva questa skill quando un bene storico, architettonico o paesaggistico deve essere conosciuto, diagnosticato e preparato a un intervento reversibile e compatibile. È una faccetta di lettura stratigrafica, campionamento e decisione conservativa distinta da world-construction-history-1800-present, environmental-resilience-lca-diagnostics e structural-civil-engineering: non autentica un bene, non approva lavori e non sostituisce l'autorità di tutela.

Prima raccogli identificazione e regime di tutela, proprietà e autorizzazioni, storia documentata, rilievo geometrico, materiali e tecniche, alterazioni, umidità, sali, dissesti, uso, ambiente, interventi precedenti, urgenze, valore e significato, piano di campionamento e obiettivi. Se bene, localizzazione, stato di tutela, fonte o scopo non sono chiari, lo stato è blocked.

## Workflow

1. **Gate della significanza:** separa fatto documentato, attribuzione, ipotesi e interpretazione; registra quali valori storici, d'uso, materiali e paesaggistici possono essere alterati.
2. **Gate della conoscenza:** costruisci timeline di fonti e interventi, rilievo fotografico e geometrico, mappa dei materiali e stratigrafia costruttiva; conserva lo stato attuale prima di pulire o rimuovere.
3. **Gate del sintomo:** mappa fessure, deformazioni, umidità, biodeterioramento, distacchi, sali, corrosione e alterazioni cromatiche con posizione, scala, direzione e data; non convertire sintomo in causa senza verifica.
4. **Gate del campionamento:** definisci domanda, zona, invasività, quantità, contaminazione, catena di custodia, laboratorio, restituzione e autorizzazione; privilegia metodi non distruttivi ma non attribuire loro certezza automatica.
5. **Gate della diagnosi:** triangola osservazione, misura, documento, confronto tra materiali e causa plausibile; classifica confidenza, urgenza, rischio e reversibilità dell'azione.
6. **Gate della compatibilità:** confronta intervento proposto con supporto, umidità, sali, permeabilità, deformabilità, aspetto, manutenzione e possibilità di rimozione; valuta mock-up e monitoraggio prima dell'estensione.
7. **Gate della tutela:** prepara dossier con alternative, impatti, evidenze, autorizzazioni, responsabili, manutenzione e piano di monitoraggio. Nessuna rimozione, campionatura o pubblicazione di dati sensibili è automatica.

## Output

Consegna un heritage_diagnostics_record con bene e tutela, fonti, rilievi, mappa dei fenomeni, campioni, prove, stratigrafia, ipotesi causali, confidenza, alternative, compatibilità, monitoraggio e stato documented, conditional o blocked. Ogni proposta conserva reversibilità, invasività, manutenzione e autorizzazione necessaria.

## Quality gates

- Bene, significanza, tutela, proprietà e autorizzazioni sono verificate o marcate mancanti.
- Stato attuale, fonti storiche e interventi precedenti sono distinti e versionati.
- Fenomeno osservato, misura, causa ipotizzata e decisione sono collegati senza salti.
- Campioni e prove hanno domanda, posizione, metodo, laboratorio, catena di custodia e limiti.
- Alternative e mock-up considerano compatibilità, reversibilità, manutenzione e monitoraggio.
- Il dossier non si presenta come autorizzazione, progetto firmato o certificazione di autenticità.

## Evidenza e provenienza

Conserva rilievi, fotografie con data e posizione, ortofoto, nuvole, stratigrafie, fonti d'archivio, schede materiali, campioni, rapporti di laboratorio, strumenti, calibrazioni, monitoraggi, hash e registro delle manipolazioni. Marca originale, copia di lavoro, interpretazione e proposta. Disegni di sicurezza, indirizzi e dati di proprietà sono accessibili per ruolo; immagini e archivi hanno diritti propri.

## Fonti ufficiali e diritti

- [D.Lgs. 42/2004 su Normattiva](https://www.normattiva.it/atto/caricaDettaglioAtto?atto.codiceRedazionale=004G0066&atto.dataPubblicazioneGazzetta=2004-02-24&bloccoAggiornamentoBreadCrumb=true&classica=true&dataVigenza=&generaTabId=true&qId=d0c88cc2-b987-416f-a2e6-e878348303ab&tabID=&tipoDettaglio=multivigenza&title=lbl.dettaglioAtto): Codice dei beni culturali e del paesaggio, da verificare nella versione e nel regime di tutela applicabili.
- [Ministero della Cultura](https://cultura.gov.it/): riferimenti istituzionali, tutela, autorizzazioni e patrimonio culturale italiano.
- [ICCROM](https://www.iccrom.org/) e [ICOMOS](https://www.icomos.org/en): riferimenti internazionali per conservazione e gestione del patrimonio, da usare senza riprodurre testi o linee guida protette.

Le fonti legislative e istituzionali sono provenance, non licenza per ripubblicare archivi, immagini, standard o linee guida. Il workflow diagnostico, la mappa dei sintomi e i criteri di compatibilità sono originali. Stato diritti: official_reference_only_no_text_reproduced; campioni, immagini e dati del bene seguono autorizzazioni e diritti del proprietario.

## Confini professionali e legali

La skill non attribuisce autenticità o valore, non esegue restauri, non firma relazioni, non autorizza saggi o lavori e non sostituisce restauratore, conservatore, architetto, ingegnere, archeologo, laboratorio, soprintendenza o proprietario. Un'ipotesi diagnostica non è una causa accertata; nessuna pulitura, sostituzione o consolidamento va ordinato sulla sola scheda.

## Failure modes

- **Sintomo scambiato per causa:** mantieni ipotesi concorrenti e pianifica prova mirata.
- **Fonte archivistica trattata come stato attuale:** separa data, trasformazioni e rilievo contemporaneo.
- **Saggio non autorizzato:** blocca, documenta l'urgenza e richiedi autorizzazione e responsabile.
- **Metodo non distruttivo sovrainterpretato:** riporta sensibilità, profondità, calibrazione e conferme necessarie.
- **Materiale moderno dichiarato incompatibile o storico senza analisi:** marca confidenza e richiedi confronto.
- **Intervento irreversibile senza mock-up:** sospendi e proponi campione, monitoraggio e piano di rimozione.

## Strumenti

Usa GIS/CAD/BIM del bene, fotogrammetria e rilievo controllato, mappa dei fenomeni, database dei campioni, laboratorio qualificato, monitoraggio e repository versionato. Automatizza nomenclatura, coordinate, cronologia, completezza e confronto; non automatizzare attribuzione, autorizzazione o scelta conservativa.
