---
name: digital-twin-sensor-monitoring
description: Costruisce un digital twin operativo con identità, osservazioni, sincronizzazione, qualità e monitoraggio dei sensori senza confondere modello virtuale, dato misurato e stato reale.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: digital twin, sensori e monitoraggio
---

# Digital twin e sensori per il monitoraggio del costruito

## Attivazione e input

Attiva questa skill quando sensori, BMS, IoT, rilievi o log devono alimentare una rappresentazione operativa di edificio, impianto, ponte o asset. È una faccetta di osservabilità e sincronizzazione distinta da bim-ifc-openbim, commissioning-facility-asset-handover e survey-geospatial-topography-control: non dichiara che il modello sia lo stato reale, non comanda attuatori e non sostituisce il tecnico che interpreta il fenomeno.

Prima raccogli asset e identità, scopo, fenomeno, variabile, sensore, posizione e sistema di riferimento, frequenza, unità, timestamp, accuratezza, calibrazione, rete, storage, modello virtuale, relazione fisica, soglie, privacy, sicurezza, operatore e decisione attesa. Registra versione del modello, latenza tollerata, finestre mancanti, retention e owner. Se cosa, dove, quando o perché del dato sono ignoti, lo stato è blocked.

## Workflow

1. **Gate dell'identità:** assegna ID a asset, componente, sensore, osservazione e modello; collega posizione, relazione fisica, unità, dominio e versione senza duplicare l'asset.
2. **Gate della misura:** definisci variabile, range, accuratezza, calibrazione, campionamento, timestamp, timezone, qualità, latenza e perdita; separa misura grezza, dato pulito, aggregato e inferito.
3. **Gate dell'allineamento:** sincronizza coordinate, orologi, unità, periodi e revisioni del modello; misura disallineamento, ritardo, drift e copertura prima di usare il twin.
4. **Gate della pipeline:** traccia acquisizione, gateway, broker, API, trasformazioni, storage, accessi e retention; verifica replay, duplicati, outlier, gap e integrità con campione indipendente.
5. **Gate della semantica:** mappa osservazione a spazio, sistema, asset e requisito; non usare un nome simile come equivalenza semantica e conserva le trasformazioni.
6. **Gate del monitoraggio:** definisci baseline, qualità, soglie, trend, change point, allarme, destinatario e risposta; prova allarmi, perdita sensore e falsi positivi prima dell'esercizio.
7. **Gate della decisione:** collega alert a ispezione, commissioning, manutenzione o sicurezza con owner e autorizzazione; ogni comando automatico resta disabilitato finché non è approvato e testato.

## Output

Consegna un operational_twin_record con asset, sensori, schema dati, modello, sincronizzazione, qualità, pipeline, baseline, alert, gap, retention e stato observed, conditional o blocked. Ogni valore decisionale riporta origine, timestamp, trasformazioni, latenza e confidenza.

## Quality gates

- Asset, sensore, posizione, variabile, unità, timestamp e versione sono identificati.
- Grezzo, derivato, aggregato, inferito e visualizzato sono distinguibili.
- Calibrazione, sincronizzazione, latenza, drift, gap, duplicati e outlier sono monitorati.
- API, pipeline, accessi, retention, backup e provenienza sono auditabili.
- Allarme, destinatario, risposta, falso positivo e perdita dati hanno test.
- Il twin non viene presentato come rilievo, as-built, diagnosi o comando sicuro senza validazione professionale.

## Evidenza e provenienza

Conserva datasheet, seriali, calibrazioni, installazione, coordinate, firmware, configurazione, raw stream, schema, API, trasformazioni, log, alert, ticket, snapshot del modello e hash. Marca dato osservato, interpolato, inferito e simulato. Telemetria, persone, occupazione e sicurezza sono minimizzati e accessibili per ruolo; non rendere pubblici endpoint o credenziali.

## Fonti ufficiali e diritti

- [ISO 23247-1:2021](https://committee.iso.org/standard/75066.html?browse=ics): principi e quadro ufficiale per digital twin framework; verificare l'ambito manufacturing prima di trasferire concetti al costruito.
- [OGC SensorThings API](https://www.ogc.org/standards/sensorthings/): standard aperto per interconnettere dispositivi, osservazioni e applicazioni IoT geospaziali.
- [OGC SensorThings API Part 1](https://docs.ogc.org/is/18-088/18-088.html): riferimento normativo per modello e interfaccia delle osservazioni.

Gli standard ISO/OGC hanno diritti, versioni e condizioni d'uso proprie; si citano identificativi e scopo senza copiare clausole o schemi completi. Il modello di qualità, le pipeline di gate e il record sono originali. Stato diritti: official_reference_only_no_text_reproduced.

## Confini professionali e legali

La skill non certifica sensori, non attesta stato reale, non esegue diagnosi strutturale o energetica, non controlla attuatori e non sostituisce progettista, manutentore, OT/IT security, data protection officer o responsabile sicurezza. Accuratezza e continuità del twin valgono solo per sensori, posizioni, finestre, trasformazioni e condizioni dimostrate.

## Failure modes

- **Twin visuale senza osservazioni:** marca modello statico e non chiamarlo digital twin operativo.
- **Timestamp o coordinate discordanti:** blocca correlazione e riallinea orologi, CRS, unità e versioni.
- **Sensore driftato usato per allarme:** congela il dato, verifica calibrazione e confronta con misura indipendente.
- **Interpolazione nascosta nei gap:** conserva flag, metodo, durata del gap e impatto decisionale.
- **Allarme senza risposta:** non attivare notifiche operative finché owner, soglia e procedura non sono provati.
- **API aperta con dati sensibili:** limita accesso, ruota credenziali e verifica retention e privacy.

## Strumenti

Usa registry asset/sensori, gateway, broker, API standard, time-series store, data-quality monitor, digital model, dashboard, alert manager e ticketing. Automatizza schema, unità, timestamp, gap, drift e audit trail; non automatizzare diagnosi, comandi o dichiarazioni di sicurezza.
