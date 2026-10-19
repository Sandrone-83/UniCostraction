---
name: building-energy-audit-diagnosis
description: Esegue la diagnosi energetica operativa di un edificio con campagna dati, rilievo degli usi, bilancio, baseline calibrata e misure di risparmio senza sostituire auditor, certificatore o progettista abilitato.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: audit energetico e diagnosi dell'edificio
---

# Audit energetico e diagnosi dell'edificio

## Attivazione e input

Attiva questa skill quando occorre capire come e dove un edificio consuma energia, verificare la qualità dei dati e confrontare misure di efficienza con calcoli trasparenti. È distinta da building-energy-decarbonization, che tratta roadmap e gestione della decarbonizzazione, e da mep-energy-systems, che tratta scelta e progettazione dei sistemi.

Raccogli edificio/gruppo e confini, destinazioni d'uso, orari, occupazione, clima, involucro, impianti, vettori, contatori, bollette, profili di carico, regolazione, manutenzione, BMS, produzione locale, qualità dell'aria, comfort, vincoli, tariffe e obiettivi. Se periodo, confini, misure, dati di esercizio o uso del fabbricato non sono affidabili, lo stato è blocked o screening_only.

## Workflow

1. **Gate del perimetro:** definisci edificio, servizi energetici, vettori, usi inclusi/esclusi, periodo, anno base, unità, temperatura e confini tra asset, tenant e parti comuni.
2. **Gate della campagna:** pianifica sopralluoghi, inventario apparecchiature, letture, sub-meter, log BMS, profili e interviste; documenta strumento, calibrazione, frequenza, occupazione e condizioni.
3. **Gate della qualità dati:** riconcilia bollette, contatori e fatture con periodi, unità, fattori, perdite e anomalie; marca misurato, fatturato, stimato, proxy o assunto.
4. **Gate del bilancio:** costruisci inventario end-use e bilancio energetico, verifica chiusura, picchi, carichi base, stagionalità e scostamenti; separa energia finale, primaria, costo ed emissioni.
5. **Gate della diagnosi:** formula cause e opportunità per involucro, generazione, distribuzione, emissione, controllo, acqua calda, illuminazione, processo e comportamento; distingue guasto, inefficienza e vincolo d'uso.
6. **Gate del calcolo:** stima risparmio, costo, vita, manutenzione, comfort, interazioni e rischio con metodo dichiarato; calibra o limita il modello e mostra sensibilità.
7. **Gate del piano:** ordina misure per prestazione, costo, fattibilità, lock-in e rischio; definisci baseline, misura e verifica post-intervento, owner, decisione e dati mancanti.

## Output

Produci un energy_audit_record con perimetro, inventario, campagna, dati, bilancio, baseline, indicatori, end-use, anomalie, misure, calcoli, costi, priorità, incertezze, M&V plan, fonti e stato screened, conditional, audit_ready_for_professional_review o blocked. Non chiamare "risparmio conseguito" una previsione.

## Quality gates

- Dati energetici aggiornati, tracciabili, coerenti per periodo, unità e contatore.
- Bilancio e indicatori spiegano differenze, normalizzazione, clima, occupazione e uso.
- Impianti e involucro sono osservati o dichiarati non osservati; non si deduce una prestazione da sole bollette.
- Misure indipendenti o interagenti sono calcolate senza doppio conteggio.
- Costi, manutenzione, tempi, comfort, sicurezza e vincoli autorizzativi sono espliciti.
- Baseline, metodo di misura, incertezza e responsabilità di verifica sono approvati prima di promettere risultati.

## Evidenza e provenienza

Conserva bollette, letture, serie orarie, foto, schemi, libretti, inventari, manuali, dati BMS, meteo, fattori di conversione/emissione, fogli di calcolo, modelli, assunzioni, sopralluoghi e approvazioni. Marca dati originali, misurati, stimati e forniti dal gestore; conserva versione, timestamp, strumento, operatore e catena di trasformazione. Non inserire dati di occupanti o contatori individuali senza scopo e accesso autorizzati.

## Fonti ufficiali e diritti

- [ENEA PNPE2 — diagnosi energetiche](https://pnpe2.enea.it/diagnosi_energetiche): portale istituzionale e riferimenti operativi alle diagnosi degli edifici e alle linee guida nazionali.
- [Normattiva — D.Lgs. 4 luglio 2014, n. 102](https://www.normattiva.it/uri-res/N2Ls?urn%3Anir%3Astato%3Adecreto.legislativo%3A2014%3B102~art8%21vig=): quadro italiano sull'efficienza energetica e diagnosi, da verificare nella versione vigente e per il soggetto interessato.
- [EUR-Lex — Direttiva (UE) 2023/1791](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32023L1791): criteri europei per dati misurati, profilo dei consumi, misure, calcoli e tracciabilità degli audit.
- [ISO 50001](https://www.iso.org/iso-50001-energy-management.html): riferimento ufficiale per sistemi di gestione dell'energia e miglioramento continuo, senza riprodurre lo standard.

La procedura, i record, le formule illustrative e il piano di gate sono originali. Diritti: `official_public_legal_text_verify_current_consolidation` per norme e `official_reference_only_no_text_reproduced` per ENEA, direttive e standard; dati di edificio, software, bollette, modelli, fattori e documenti di produttori restano soggetti a licenza e autorizzazione.

## Confini professionali e legali

La skill non rilascia APE, diagnosi asseverata, certificazione energetica, dichiarazione di conformità, incentivo o garanzia di risparmio, non firma pratiche e non prescrive lavori pericolosi. Non sostituisce auditor competente, certificatore, progettista, energy manager, manutentore, installatore o autorità. Un bilancio energetico è valido solo per edificio, periodo, uso, dati e metodo dichiarati.

## Failure modes

- **Bollette come diagnosi completa:** riapri sopralluogo, inventario, end-use e misure.
- **Baseline non calibrata:** separa dato osservato, normalizzazione e ipotesi; non calcolare payback certo.
- **Doppio conteggio tra misure:** costruisci interazioni e scenario integrato.
- **Modello preciso con dati poveri:** riduci la precisione dichiarata e richiedi campagna.
- **Risparmio confuso con decarbonizzazione:** separa kWh, costo, fattore emissivo, energia esportata e compensazioni.
- **Audit scambiato per APE o incentivo:** instrada al professionista e al regime vigente.

## Strumenti

Usa meter/data register, utility reconciliation, end-use inventory, load profile, degree-day normalization, Sankey/balance sheet, calibrated model, measure register, LCC handoff, sensitivity sheet e M&V plan. Automatizza unità, controlli di chiusura e anomalie; non alterare contatori, BMS o setpoint senza autorizzazione.
