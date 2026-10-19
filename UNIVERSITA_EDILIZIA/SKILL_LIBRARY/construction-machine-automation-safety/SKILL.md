---
name: construction-machine-automation-safety
description: Valuta interfacce, modalità operative e barriere di sicurezza per macchine e automazione di cantiere, senza sostituire fabbricante, valutazione dei rischi, CE o autorizzazione alla manovra.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: sicurezza macchine e automazione di cantiere
---

# Sicurezza macchine e automazione di cantiere

## Attivazione e input

Attiva questa skill quando escavatori, gru, piattaforme, robot, guida assistita, sistemi machine-control, teleoperazione, geofencing o automazioni vengono introdotti, modificati o integrati nel cantiere. È una faccetta di hazard e interfaccia operativa distinta da construction-site-safety e da construction-robotics-industrialization, che tratta industrializzazione e robotica produttiva.

Raccogli macchina e configurazione, fabbricante, seriale, dichiarazioni e manuali, uso previsto e prevedibile, sito, terreno, persone e mezzi presenti, energia, zone cieche, sensori, software/firmware, modalità manuale/assistita/autonoma, geofence, comunicazioni, emergenza, manutenzione, competenze, prove e incidenti. Se macchina, configurazione, ambiente o responsabile non sono definiti, lo stato è blocked.

## Workflow

1. **Gate dell'identità:** inventaria macchina, attrezzatura, accessori, versione software e modifiche; distingui prodotto, installazione, integrazione e uso in sito.
2. **Gate dello scenario:** mappa compiti, persone, mezzi, carichi, interfacce, perdita GNSS/comunicazioni, ostacoli, meteo, visibilità, manutenzione e uso prevedibile non conforme.
3. **Gate delle barriere:** ordina eliminazione, protezioni fisiche, interlock, limitazione energia, separazione, segnalazione e procedure; tratta supervisione e DPI come livelli residuali.
4. **Gate della configurazione:** verifica parametri, zone, limiti, sensori, fail-safe, arresto di emergenza, recovery manuale, account e change control prima dell'uso.
5. **Gate della prova:** esegui test in area controllata e senza persone nella zona pericolosa; prova perdita sensore, geofence, comunicazione, alimentazione, restart e passaggio manuale.
6. **Gate dell'esercizio:** definisci pre-use check, permit, spotter o supervisore, zone interdette, comunicazioni, log anomalie e stop-work; non accettare “autonomia” come prova di sicurezza.
7. **Gate della modifica:** sospendi l'uso dopo modifica sostanziale, incidente, quasi incidente, aggiornamento software o variazione del sito fino a nuova revisione.

## Output

Produci un machine_automation_safety_record con asset, configurazione, scenari, hazard, barriere, test, competenze, limiti operativi, anomalie e stato cleared, conditional o blocked. Riporta sempre modalità di controllo, zona, precondizioni e recovery autorizzato.

## Quality gates

- Identità, configurazione, manuale, dichiarazione e limiti del fabbricante sono verificati.
- Uso previsto, persone esposte, zone, energia e interfacce sono osservati e rappresentati.
- Funzioni di sicurezza, arresto, interlock, fallback e comunicazione sono testate e registrate.
- Nessun bypass, account condiviso, geofence non validato o firmware non tracciato.
- Operatori e supervisori hanno competenza, autorizzazione e briefing specifici per macchina e fase.
- Ogni anomalia, modifica o near miss genera contenimento, riesame e autorizzazione prima della ripresa.

## Evidenza e provenienza

Conserva inventario e seriali, manuali e dichiarazioni, configurazioni, firmware, risk assessment, mappe zone, checklist, test log, calibrazioni sensori, permit, training records, video/foto autorizzati, incidenti e change requests. Marca fonte fabbricante, osservazione in campo, simulazione e giudizio. Proteggi telemetria, immagini e posizione delle persone.

## Fonti ufficiali e diritti

- [EUR-Lex — Regolamento (UE) 2023/1230 sulle macchine](https://eur-lex.europa.eu/eli/reg/2023/1230/oj): requisiti e operatori economici, verificare applicazione temporale e ambito.
- [EU-OSHA — Machinery Regulation](https://osha.europa.eu/en/legislation/directive/regulation-20231230eu-machinery): sintesi istituzionale e aggiornamenti.
- [Normattiva — D.Lgs. 81/2008](https://www.normattiva.it/eli/id/2008/04/30/008G0104/CONSOLIDATED): uso sicuro di attrezzature e lavoro, da verificare alla data.
- [ISO 12100 — pagina ISO](https://www.iso.org/standard/51528.html): principi di valutazione e riduzione del rischio macchina, riferimento soggetto a licenza.

La procedura, la matrice degli scenari e il record sono originali. Diritti: official_reference_only_no_text_reproduced; regolamenti pubblici, manuali del fabbricante, software, telemetria e standard tecnici mantengono titolarità e licenze proprie.

## Confini professionali e legali

La skill non modifica PLC, firmware o parametri di sicurezza, non comanda macchine, non redige dichiarazioni CE, non certifica conformità e non sostituisce fabbricante, datore di lavoro, RSPP, progettista della macchina, integratore, manutentore, operatore o autorità. Nessuna prova in area operativa autorizza da sola l'esercizio continuativo.

## Failure modes

- **Macchina identificata solo dal modello:** blocca e verifica seriale, allestimento e accessori.
- **Sensore o geofence presunto affidabile:** prova indipendente e fallback manuale prima dell'uso.
- **Aggiornamento software non registrato:** quarantena configurazione e ricostruzione della versione.
- **Spotter usato come barriera unica:** rivaluta separazione, interlock e zone fisiche.
- **Perdita comunicazione ignorata:** esegui test controllato e definisci stato sicuro.
- **Incidente trattato come errore dell'operatore:** preserva evidenze e riesamina sistema, compito e formazione.

## Strumenti

Usa asset register, manuale e configuration baseline, hazard log, zone map, permit-to-operate, checklist pre-use, safety-function test sheet, telemetry log e change register. Automatizza promemoria, versioni e completezza; non inviare comandi, disabilitare protezioni o dichiarare CE/conformità in autonomia.
