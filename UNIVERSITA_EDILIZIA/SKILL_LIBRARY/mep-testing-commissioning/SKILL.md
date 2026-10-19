---
name: mep-testing-commissioning
description: Coordina pre-functional check, test funzionali, TAB, integrazione e retest di impianti MEP con script e dati tracciabili, senza sostituire progettista, installatore, collaudatore o autorità.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: collaudi, testing e messa in servizio MEP
---

# Collaudi, testing e messa in servizio MEP

## Attivazione e input

Attiva questa skill quando impianti meccanici, elettrici, idrico-sanitari, controllo o antincendio devono passare da installati a funzionanti e verificabili mediante pre-functional check, test, bilanciamento, trend e integrazione. È distinta da commissioning-facility-asset-handover, che governa la consegna dell'asset e dei dati operativi, e da fire-engineering-performance-verification, che tratta la prestazione antincendio.

Raccogli OPR e requisiti di progetto, schemi e revisioni, equipment schedule, cause-and-effect, submittal, certificati, manuali, sequenze di controllo, matrice interfacce, alimentazioni, prerequisiti, strumenti e calibrazioni, TAB plan, script, witness, stagionalità, sicurezza e criteri pass/fail. Se sistema, confine, prerequisiti o criterio non sono definiti, lo stato è blocked.

## Workflow

1. **Gate della base:** congela as-built, tag equipment, reti, setpoint, potenze, unità e collegamenti; risolvi ogni mismatch tra modello, elaborati e installato.
2. **Gate della readiness:** verifica installazione, accessibilità, tenuta, pulizia, filtri, serraggi, protezioni, alimentazione, sicurezza, sensori, valvole, allarmi e documentazione prima di alimentare o avviare.
3. **Gate dei test pre-funzionali:** esegui checklist per componente e sottosistema, annotando misura, strumento, condizioni, difetto e rilascio; una checklist spuntata senza prova non vale.
4. **Gate TAB e test funzionale:** definisci punti, condizioni di carico, tolleranze e stabilizzazione; esegui taratura e prova della risposta locale secondo script approvato.
5. **Gate delle sequenze:** prova modo normale, start/stop, setpoint, allarmi, perdita sensore, fallback, interlock e ripartenza controllata; separa simulazione da evento reale.
6. **Gate integrato:** coordina interfacce HVAC-BMS, elettrico-emergenza, idrico-antincendio e sistemi di sicurezza con matrice causa-effetto e test dei responsabili.
7. **Gate del retest e trend:** registra punch list, retest indipendente, trend e limiti; chiudi solo con evidenza, approvazione e aggiornamento di as-built, setpoint e manuali.

## Output

Produci un mep_cx_record con sistema, confini, prerequisiti, script, strumenti, raw data, risultati, difetti, retest, trend, condizioni e stato prefunctional, functionally_tested, conditionally_accepted o blocked. Evidenzia test non eseguiti per carico, stagione, accesso o safety.

## Quality gates

- OPR, criteri, sequenze, interfacce e versione degli elaborati sono identificati.
- Readiness e sicurezza sono firmate prima di energizzazione, pressione o rotazione.
- Strumenti sono identificati e calibrati; unità, punti, condizioni e incertezza sono registrati.
- Ogni test ha precondizioni, metodo, expected result, actual result, witness e pass/fail motivato.
- Integrati, allarmi e modalità di guasto sono provati senza creare pericolo o falsi allarmi non governati.
- Punch list, retest, as-built, setpoint e dati di manutenzione sono riconciliati prima dell'accettazione.

## Evidenza e provenienza

Conserva revisioni di schemi e sequenze, tag e seriali, checklist, foto, rapporti TAB, tracciati BMS, log eventi, strumenti e calibrazioni, condizioni meteo/carico, script, witness e punch list. Distingui misura grezza, valore filtrato, simulazione, osservazione e giudizio. Proteggi credenziali e dati operativi; consegna solo estratti autorizzati.

## Fonti ufficiali e diritti

- [ASHRAE — Titles, Purposes and Scopes](https://www.ashrae.org/technical-resources/standards-and-guidelines/titles-purposes-and-scopes): descrizioni ufficiali del processo di commissioning e delle linee guida, senza riprodurne il testo.
- [ISO 41001](https://www.iso.org/cms/%20render/live/en/sites/isoorg/contents/data/standard/06/80/68021.html): gestione delle facility e servizi, come riferimento di contesto.
- [ISO 50001](https://www.iso.org/standard/69426.html): gestione dell'energia e verifica delle prestazioni, quando pertinente.
- [Normattiva — D.Lgs. 81/2008](https://www.normattiva.it/eli/id/2008/04/30/008G0104/CONSOLIDATED): sicurezza di prove, avviamenti e lavori in campo, da verificare nella versione vigente.

Gli script, le checklist e la matrice delle prove sono originali. Diritti: official_reference_only_no_text_reproduced; ASHRAE e ISO sono pubblicazioni soggette a licenza, manuali e dati BMS restano del titolare. Non si riusano sequenze o moduli proprietari senza autorizzazione.

## Confini professionali e legali

La skill non esegue manovre elettriche, prove in pressione, test di sicurezza o modifiche di setpoint senza personale competente e autorizzato; non firma collaudi, dichiarazioni di conformità, agibilità o certificazioni energetiche. Non sostituisce progettista, installatore, responsabile sicurezza, manutentore, collaudatore, laboratorio o autorità. Un test passato vale solo per configurazione e condizioni registrate.

## Failure modes

- **Sistema non pronto:** blocca il test e apri precondition failure; non trasformare l'assenza di prova in pass.
- **Setpoint o sequenza errati:** congela la revisione, confronta OPR/as-built e ripeti il test coinvolto.
- **Strumento non calibrato:** invalida o condiziona il risultato e ripeti con strumento idoneo.
- **Trend manipolato:** conserva raw data, log e trasformazioni; separa dato reale da interpolazione.
- **Interfaccia non testata:** apri issue integrata e definisci scenario, owner e retest prima dell'accettazione.
- **Test pericoloso:** ferma la prova, applica permit-to-work e safety review; mai bypass non autorizzati.

## Strumenti

Usa equipment/tag register, readiness checklist, script library, TAB sheets, data logger, multimetro/manometro/datalogger autorizzati, BMS historian, cause-effect matrix, punch list e commissioning tracker. Automatizza raccolta, timestamp, versioni e report; non comandare attuatori né concludere l'accettazione senza controllo umano.
