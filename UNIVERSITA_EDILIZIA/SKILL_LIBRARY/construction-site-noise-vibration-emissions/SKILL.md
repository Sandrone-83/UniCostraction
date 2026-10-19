---
name: construction-site-noise-vibration-emissions
description: Governa valutazione, mitigazione e monitoraggio di rumore, vibrazioni e emissioni atmosferiche di cantiere verso lavoratori, ricettori e ambiente, separando obblighi ambientali da igiene occupazionale e acustica edilizia.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: rumore, vibrazioni ed emissioni di cantiere
---

# Gestione di rumore, vibrazioni ed emissioni di cantiere

## Attivazione e input

Attiva questa skill quando lavorazioni, mezzi, impianti, demolizioni, scavi, frantumazioni o trasporti possono disturbare ricettori, danneggiare beni, generare polveri o produrre emissioni e serve un piano di controllo con evidenze. È distinta da building-acoustics-performance-control, che tratta prestazioni acustiche dell'edificio, da occupational-health-exposure-hygiene, che tratta esposizione dei lavoratori, e da site-water-energy-carbon-accounting, che tratta consumi e carbon accounting.

Raccogli sito, fasi, orari, macchine, sorgenti, ricettori, distanze, topografia, fondo, meteo, lavorazioni impulsive, vibrazioni trasmesse, polveri, scarichi, autorizzazioni, classificazione acustica, limiti, esposti sensibili, monitoraggi, manutenzione e canali reclamo. Se ricettori, regime autorizzativo, sorgente o metodo non sono identificati, lo stato è blocked.

## Workflow

1. **Gate ambientale:** identifica matrice, sorgente, ricettore, giurisdizione, norma, autorizzazione, limite, periodo di riferimento e soggetto competente; separa rumore, vibrazione, polvere, gas e odore.
2. **Gate della baseline:** misura o documenta fondo, meteo, attività vicine, condizioni di sito e stato dei ricettori prima dei lavori; registra strumento, calibrazione, posizione e orario.
3. **Gate dello scenario:** collega WBS, macchine, percorsi, turni e contemporaneità a sorgente e ricettore; valuta propagazione, schermature, distanza, terreno e incertezza.
4. **Gate dei controlli:** ordina misure alla fonte, percorso e ricettore: scelta attrezzatura, manutenzione, enclosure, barriere, umidificazione, velocità, orari, silenziatori, lavaggio ruote e gestione terre/polveri.
5. **Gate autorizzativo:** verifica permessi, deroghe, comunicazioni, prescrizioni, piano di monitoraggio, tecnico competente/laboratorio e condizioni di sospensione; non dedurre autorizzazione dal solo piano interno.
6. **Gate del monitoraggio:** confronta valori con criterio e periodo, qualifica dati anomali, fondo, eventi estranei e incertezza; collega superamenti a causa, azione, owner e termine.
7. **Gate del reclamo:** registra segnalazione, ricettore, timestamp, attività, evidenza, risposta, verifica e escalation; chiudi solo con prova e approvazione del responsabile.

## Output

Produci un site_environmental_impact_record con sorgenti, ricettori, baseline, attività, limiti, autorizzazioni, monitoraggio, risultati, incertezza, controlli, reclami, incidenti, escalation e stato screened, conditional, monitoring_ready, authority_review o blocked. Separa sempre valore misurato, stima, previsione e limite applicabile.

## Quality gates

- Norma, ente, classificazione/limite, autorizzazione e periodo sono dichiarati e verificati localmente.
- Punti di misura, strumenti, taratura, meteo, fondo, condizioni operative e catena dati sono tracciati.
- Il piano include contemporaneità, eventi impulsivi, vibrazione strutturale, polveri e scarichi pertinenti.
- Ogni controllo ha responsabile, frequenza, criterio di efficacia e piano di reazione.
- Superamento e reclamo attivano contenimento, indagine e autorità competente quando richiesto.
- Non si confondono limite ambientale, dose del lavoratore, requisito acustico dell'edificio e carbon emission.

## Evidenza e provenienza

Conserva permessi, classificazione acustica, piani di lavoro, inventario macchine, specifiche, baseline, file grezzi, certificati di taratura, meteo, posizione, log attività, risultati laboratorio, fotografie, manutenzione, reclami, comunicazioni e azioni correttive. Marca misurato, calcolato, modellato, dichiarato dal fornitore e assunto. Proteggi coordinate di abitazioni, immagini e contatti dei reclamanti; non pubblicare dati identificativi senza base e autorizzazione.

## Fonti ufficiali e diritti

- [Normattiva — Legge 26 ottobre 1995, n. 447](https://www.normattiva.it/atto/caricaDettaglioAtto?atto.codiceRedazionale=095G0477&atto.dataPubblicazioneGazzetta=1995-10-30&bloccoAggiornamentoBreadCrumb=true&dataVigenza=&generaTabId=true&tabID=&tipoDettaglio=vigente&title=lbl.dettaglioAtto): quadro nazionale sull'inquinamento acustico e competenze, da integrare con regione/comune e testo vigente.
- [Normattiva — D.Lgs. 3 aprile 2006, n. 152](https://www.normattiva.it/eli/id/2006/04/14/006G0171/CONSOLIDATED/20220511): tutela ambientale, aria, emissioni e autorizzazioni nei casi pertinenti; verificare aggiornamenti e applicabilità dell'attività.
- [INAIL — vibrazioni](https://www.inail.it/portale/prevenzione-e-sicurezza/it/come-fare-per/conoscere-il-rischio/agenti-fisici/vibrazioni.html): riferimento istituzionale per distinguere vibrazioni e rischio occupazionale; non sostituisce la valutazione ambientale.
- [Normattiva — D.Lgs. 9 aprile 2008, n. 81](https://www.normattiva.it/eli/id/2008/04/30/008G0104/CONSOLIDATED): da usare per il raccordo con la sicurezza dei lavoratori, senza duplicare la skill di igiene occupazionale.

La procedura, il piano di monitoraggio, le matrici e i registri sono originali. Diritti: `official_public_legal_text_verify_current_consolidation` per testi normativi e `official_reference_only_no_text_reproduced` per guide istituzionali; dati di monitoraggio, rapporti di laboratorio, mappe, software e documenti del fornitore mantengono diritti, riservatezza e licenze proprie.

## Confini professionali e legali

La skill non rilascia autorizzazioni o deroghe, non certifica conformità, non dichiara assenza di danno, non ordina sospensioni d'emergenza per persone in pericolo e non sostituisce tecnico competente in acustica, laboratorio, ambientalista, RSPP, datore di lavoro, comune, ARPA, VVF o altra autorità. Una misura puntuale non prova l'impatto di tutta la fase né esclude danni strutturali o sanitari.

## Failure modes

- **Rumore di cantiere confuso con isolamento dell'edificio:** instrada a requisito edilizio o tecnico competente.
- **Vibrazione misurata solo sul macchinario:** verifica ricettore, struttura, fondo e durata.
- **Polvere gestita con una promessa generica:** lega controllo a vento, traffico, umidità, materiale e ispezione.
- **Deroga locale assunta nazionale:** blocca e richiede atto, durata, condizioni e autorità.
- **Monitoraggio senza condizione operativa:** riapri log di macchine, turni e contemporaneità.
- **Reclamo archiviato senza prova:** conserva indagine, risposta, verifica e decisione di escalation.

## Strumenti

Usa source-receptor map, activity-schedule matrix, baseline register, noise/vibration/emission monitoring plan, calibrated instrument log, weather log, dust control checklist, permit matrix, complaint/incident register e corrective-action tracker. Automatizza alert e completezza; non disabilitare allarmi, alterare dati o comunicare conformità senza revisione competente.
