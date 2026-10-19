---
name: predictive-maintenance-reliability
description: Traduce dati di guasto, condizioni e work order in decisioni di manutenzione predittiva e affidabilità con soglie, incertezza e feedback senza sostituire manutentore o responsabile dell'asset.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: manutenzione predittiva e affidabilità
---

# Manutenzione predittiva e affidabilità degli asset

## Attivazione e input

Attiva questa skill quando un asset, impianto o componente deve passare da manutenzione a guasto a una strategia basata su condizioni, rischio, affidabilità e conseguenze. È una faccetta di failure data e decisione manutentiva distinta da commissioning-facility-asset-handover, digital-twin-sensor-monitoring e construction-site-safety: non comanda l'impianto, non certifica la sicurezza e non sostituisce il manutentore o il responsabile tecnico.

Prima raccogli asset hierarchy, funzione, funzione richiesta, modalità di guasto, effetti, criticità, conseguenze, sensori, storico guasti e interventi, ore di esercizio, ambiente, spare parts, competenze, costi, tempi, manutenzione preventiva e vincoli di sicurezza. Registra qualità e completezza dei dati, definizione di guasto, censura, soglie, owner e criterio di escalation. Se asset, funzione o conseguenza sono ignoti, lo stato è blocked.

## Workflow

1. **Gate della funzione:** definisci asset, funzione, performance minima, contesto e conseguenza del mancato servizio; separa failure, degradazione, allarme e indisponibilità.
2. **Gate del dato:** normalizza ID, failure mode, causa, effetto, data, ore, intervento, downtime, ricambio e costo; distingue eventi osservati, classificati, censurati e mancanti.
3. **Gate della criticità:** valuta sicurezza, ambiente, continuità, qualità, costo e compliance con scala e owner; non usare frequenza storica bassa come prova di rischio basso.
4. **Gate del segnale:** collega misura, sensore, unità, baseline, trend, rumore, latenza, temperatura e condizioni; verifica calibrazione, drift e correlazione con failure reale.
5. **Gate del modello:** sceglie soglia, trend, regola, survival/reliability model o classificatore con campione, split temporale, falsi positivi, falsi negativi e intervallo di confidenza; blocca il modello non spiegabile per una decisione safety-critical.
6. **Gate dell'azione:** mappa allarme a ispezione, derating, ricambio, fermata controllata o emergenza con precondizioni, tempo, competenza e autorizzazione; prova la catena senza esporre persone o impianti.
7. **Gate del feedback:** confronta previsione, intervento, guasto mancato, falso allarme e costo evitato; aggiorna soglie e modello solo con change control e preserva la versione usata nella decisione.

## Output

Consegna un reliability_maintenance_record con asset, funzioni, failure taxonomy, dati, criticità, segnali, modello, soglie, azioni, work order, esiti, KPI, incertezza, versione e stato monitored, conditional o blocked. Ogni allarme indica evidenza, confidenza, finestra d'azione e chi può autorizzarla.

## Quality gates

- Gerarchia, funzione, performance minima, failure mode e conseguenza sono definiti.
- Dati di guasto, manutenzione, sensore, ore e downtime hanno schema, qualità e periodo.
- Training/test temporale, censura, sbilanciamento, falsi positivi/negativi e confidenza sono valutati.
- Soglia e allarme sono collegati a un'azione autorizzata, sicura e verificabile.
- Il modello in produzione è versionato e monitorato per drift e prestazione.
- Predizione e priorità non vengono presentate come diagnosi certa, certificazione o ordine automatico.

## Evidenza e provenienza

Conserva asset register, manuali, failure report, work order, log sensori, calibrazioni, dati grezzi, trasformazioni, dataset di training/test, modello, versioni, soglie, dashboard, esiti e approvazioni. Marca fonte, censura, imputazione, esclusione, autore e timestamp. Dati di produzione, sicurezza e fornitori sono limitati per ruolo; non esportare telemetria sensibile senza autorizzazione.

## Fonti ufficiali e diritti

- [ISO 55001:2024](https://www.iso.org/standard/83054.html): requisiti ufficiali per sistemi di asset management, inclusa l'azione predittiva nel ciclo di vita.
- [ISO 14224:2016](https://www.iso.org/standard/64076.html?trk=public_post_comment-text): raccolta e scambio strutturato di dati di affidabilità e manutenzione; verificarne l'ambito industriale prima di adattarlo.
- [ISO TC 251 — ISO 55001](https://committee.iso.org/sites/tc251/home/projects/published/iso-55001.html): riferimento ufficiale e stato della serie di asset management.

Gli standard ISO sono restricted: si usano identificativi, scopo e concetti senza copiare clausole o tabelle. Taxonomy, record, gate e procedura di feedback sono originali. Stato diritti: official_reference_only_no_text_reproduced.

## Confini professionali e legali

La skill non certifica affidabilità, non dichiara sicurezza, non ordina fermate o riavvii, non valida un modello safety-critical e non sostituisce manutentore, ingegnere, asset owner, responsabile sicurezza, laboratorio o autorità. Una previsione è una stima condizionata e non prova che il guasto accadrà o non accadrà.

## Failure modes

- **ID asset o failure mode incoerenti:** blocca aggregazione e correggi taxonomy e gerarchia.
- **Dati censurati trattati come assenza di guasto:** separa fine osservazione, failure e censura.
- **Modello addestrato su futuro o leak:** rifai split temporale e registra la pipeline.
- **Soglia ottimizzata sul dataset storico:** valida out-of-sample e misura costi dei falsi.
- **Allarme senza ricambio o competenza:** non promettere beneficio e definisci capacità operativa.
- **Modello driftato:** sospendi automazione, confronta baseline e riaddestra con change control.

## Strumenti

Usa CMMS/EAM, asset register, failure taxonomy, historian/IoT, notebook riproducibile, time-series analytics, reliability model, issue/work-order tracker e dashboard. Automatizza classificazione, qualità, soglie e KPI; non automatizzare diagnosi definitiva, fermata, bypass o accettazione del rischio.
