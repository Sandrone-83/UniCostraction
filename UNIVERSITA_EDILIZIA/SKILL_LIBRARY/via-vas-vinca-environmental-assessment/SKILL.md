---
name: via-vas-vinca-environmental-assessment
description: "Orchestrazione documentale e decisionale degli iter VIA, VAS e VIncA, con screening, consultazione, prescrizioni e monitoraggio sotto controllo di autorita e proponenti."
metadata:
  library: "UNIVERSITA_EDILIZIA/SKILL_LIBRARY"
  version: "G31.1"
  domain: "valutazioni ambientali VIA VAS VIncA"
---

# Valutazioni ambientali VIA, VAS e VIncA

Questa skill organizza il fascicolo e le decisioni di un procedimento di valutazione ambientale. Distingue progetto, piano o programma e sito Natura 2000; costruisce il registro di scoping, partecipazione, prescrizioni e monitoraggio. Non e una valutazione ambientale firmata e non sostituisce l'autorita competente.

## Attivazione e input

Attivare per screening o VIA di un progetto, VAS di piano o programma, valutazione di incidenza su Natura 2000, coordinamento tra procedimenti o verifica dell'ottemperanza. Richiedere:

- descrizione del progetto/piano, localizzazione, alternative, fasi, opere connesse e cronoprogramma;
- cartografia, vincoli, aree protette, siti Natura 2000, habitat/specie e dati ambientali con scala e data;
- autorita competente, proponente, soggetti da consultare, regione e procedura prevista;
- studi specialistici disponibili, baseline, pressioni, impatti diretti/indiretti/cumulativi e misure;
- precedenti provvedimenti, prescrizioni, pareri, osservazioni pubbliche e piano di monitoraggio.

Senza classificazione iniziale e autorita competente lo stato e `screening_pending`.

## Workflow

1. Classificare l'oggetto: VIA per progetto, VAS per piano/programma, VIncA per effetti su siti Natura 2000. Registrare possibili integrazioni, competenza statale/regionale e normativa vigente alla data di avvio.
2. Mappare soglie, esclusioni, screening, scoping, termini, consultazioni e documenti richiesti. Non trattare l'esito dello screening come autorizzazione alla costruzione.
3. Costruire una baseline datata con fonti, scala, incertezza e lacune; includere alternative ragionevoli, scenario zero, effetti cumulativi, cantiere, esercizio, dismissione e cambi climatici quando pertinenti.
4. Coordinare studi specialistici e produrre registro impatto-misura-indicatore: ogni impatto deve avere recettore, fase, significativita motivata, mitigazione, responsabile, evidenza e indicatore di monitoraggio.
5. Preparare rapporto ambientale, studio preliminare, studio di impatto o screening VIncA senza copiare fonti protette. Gestire metadati, versioni, mappe e allegati come un fascicolo controllato.
6. Tracciare pubblicazione, consultazione, osservazioni, controdeduzioni, pareri e richieste di integrazione. Ogni risposta deve citare il documento e la versione a cui risponde.
7. Registrare provvedimento, condizioni ambientali, prescrizioni, misure compensative e obblighi di monitoraggio. Convertire le prescrizioni in azioni verificabili con owner, scadenza, evidenza e criterio di chiusura.
8. Durante attuazione, controllare variazioni e ottemperanza. Una modifica sostanziale riapre il gate procedurale invece di essere assorbita come semplice revisione del piano di monitoraggio.

## Output

Produrre un `environmental_assessment_record` con `screening_pending`, `procedure_mapped`, `consultation_open`, `decision_recorded`, `monitoring_active` o `blocked`; matrice procedura-autorita-termine; baseline e lacune; registro impatti/misure; log di partecipazione; provvedimento e prescrizioni; piano di monitoraggio; registro variazioni e ottemperanza.

## Quality gates

- **Classificazione**: VIA, VAS e VIncA sono motivate e non intercambiate.
- **Competenza**: autorita, regione, ente gestore Natura 2000 e termini sono confermati alla data.
- **Baseline**: fonti, scala, periodo, qualita e lacune sono espliciti.
- **Alternative e cumulativi**: sono trattati o motivatamente esclusi.
- **Partecipazione**: pubblicazione, osservazioni e risposte hanno prova e scadenza.
- **Decisione**: provvedimento, condizioni e prescrizioni sono separati da una bozza di studio.
- **Monitoraggio**: indicatori, frequenza, soglie, responsabili e azioni correttive sono assegnati.
- **Cambi**: localizzazione, fasi, emissioni o opere connesse modificati riattivano lo screening.

## Evidenza e provenienza

Per ogni dato indicare ente autore, titolo, URL o protocollo, data di pubblicazione/consultazione, scala, versione, periodo di validita e trasformazioni GIS o statistiche. Conservare layer originali, mappe derivate, verbali, avvisi, osservazioni, risposte, pareri e ricevute. Un modello o una mappa non prova da sola la significativita dell'impatto; il ragionamento, il ruolo del tecnico e l'atto dell'autorita devono restare distinti.

## Fonti ufficiali e diritti

I contenuti della skill sono originali e sintetici: rispettare copyright, licenze, termini d'uso dei portali e diritti sugli asset; non redistribuire testi o allegati protetti.

- [D.Lgs. 152/2006 su Normattiva](https://www.normattiva.it/eli/id/2006/04/14/006G0171/CONSOLIDATED/20220511): Parte seconda, VIA e VAS; `official_public_legal_text_verify_current_consolidation`.
- [D.P.R. 357/1997 su Normattiva](https://www.normattiva.it/atto/caricaDettaglioAtto?atto.codiceRedazionale=097G0390&atto.dataPubblicazioneGazzetta=1997-10-23&bloccoAggiornamentoBreadCrumb=true&classica=true&dataVigenza=&generaTabId=true&qId=&tabID=&tipoDettaglio=originario&title=lbl.dettaglioAtto): VIncA e Natura 2000; `official_public_legal_text_verify_current_consolidation`.
- [Linee guida nazionali VIncA del MASE](https://www.mase.gov.it/sites/default/files/archivio/allegati/rete_natura_2000/linee_guida_nazionali_valutazione_di_incidenza_2019.pdf): integrazione procedurale e istruzioni; `official_reference_only_no_text_reproduced`.
- [Direttiva 2011/92/UE su EUR-Lex](https://eur-lex.europa.eu/legal-content/IT/TXT/?uri=CELEX:32011L0092) e [Direttiva 2001/42/CE](https://eur-lex.europa.eu/legal-content/IT/TXT/?uri=CELEX:32001L0042): quadro europeo VIA/VAS; `official_public_legal_text_verify_current_consolidation`.

I testi e le linee guida sono solo riferimenti ufficiali: non riprodurre contenuti protetti. Verificare sempre norme regionali, sito dell'autorita e aggiornamenti successivi alla data del caso.

## Confini professionali e legali

La skill non decide l'assoggettabilita, non redige o firma studi specialistici, non emette pareri, non autorizza opere e non sostituisce proponente, consulenti, ente gestore o autorita competente. Non garantisce l'assenza di impatti e non rende efficace un provvedimento. L'output e un supporto organizzativo e deve essere validato da professionisti e amministrazioni titolari del procedimento.

## Failure modes

- VIA, VAS e VIncA confusi per il solo nome del progetto: rifare la classificazione sull'oggetto e sugli effetti.
- Screening trattato come autorizzazione: bloccare gate di avvio lavori finche mancano gli atti necessari.
- Sito Natura 2000 non considerato per mancanza di layer aggiornato: verificare perimetri, habitat e autorita gestore.
- Baseline non datata o studio specialistico obsoleto: declassare l'evidenza e aprire integrazione.
- Prescrizione trascritta senza owner o indicatore: non chiudere l'ottemperanza.
- Variazione progettuale minimizzata: riaprire screening e valutare cumulativi/effetti indiretti.

## Strumenti

Usare portali VIA-VAS regionali/statali, cataloghi geospaziali ufficiali, GIS con versioning, repository documentale, registro scadenze, matrice impatti-misure e strumenti di consultazione pubblica. L'automazione puo confrontare versioni e verificare completezza, ma non classificare da sola la significativita ne inviare osservazioni o istanze senza approvazione.
