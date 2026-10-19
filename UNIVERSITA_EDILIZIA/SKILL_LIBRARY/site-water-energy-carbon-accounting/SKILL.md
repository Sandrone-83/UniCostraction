---
name: site-water-energy-carbon-accounting
description: Misura e governa acqua, energia e carbonio operativo di cantiere con confini, fattori e dati auditabili, senza sostituire inventario GHG certificato, contabilità ambientale o autorizzazioni.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: gestione acqua, energia di cantiere e carbon accounting
---

# Gestione acqua, energia di cantiere e carbon accounting

## Attivazione e input

Attiva questa skill quando il cantiere deve monitorare consumi di acqua ed energia, emissioni operative, generatori, mezzi, lavaggi, abbattimento polveri o obiettivi di riduzione con baseline e responsabili. È distinta da building-energy-decarbonization, che tratta l'edificio in esercizio, e da circular-materials-lca-inventory, che tratta ciclo di vita e materiali.

Raccogli confini del sito e periodo, utenze e contatori, generatori e combustibili, mezzi e ore, acqua potabile/industriale/reflua, approvvigionamenti, perdite, scarichi, subappaltatori, fatture, letture, fattori emissivi con fonte/versione, attività normalizzante, baseline, target, autorizzazioni, meteo e regole di allocazione. Se confini, contatori o fattori non sono verificabili, lo stato è blocked.

## Workflow

1. **Gate dei confini:** fissa sito, fase, organizzazione e fonti incluse/escluse; separa consumo diretto, energia acquistata, trasporti e dati allocati ai subappaltatori.
2. **Gate dei dati:** inventaria contatori, serbatoi, carburanti, fatture, letture e stime; riconcilia unità, periodo, numeri di matricola e saldi.
3. **Gate dell'acqua:** mappa uso, riuso, perdite, lavaggi, polveri, scarichi e qualità; collega ogni volume a misura, stima o autorizzazione.
4. **Gate dell'energia:** separa rete, generatori, ricarica, mezzi e combustibili; controlla conversioni, potere calorifico, ore e doppio conteggio.
5. **Gate del carbonio:** assegna fattore emissivo, fonte, anno, geografia e uncertainty; calcola CO2e per fonte e non presenta compensazioni o carbon neutrality senza perimetro e prova.
6. **Gate della prestazione:** normalizza per area, volume, ore, produzione o altra attività dichiarata; confronta baseline e target senza confondere riduzione assoluta con intensità.
7. **Gate del miglioramento:** propone riduzione alla fonte, manutenzione, elettrificazione, riuso, rilevazione perdite e procurement; verifica il beneficio con dati successivi e owner.

## Output

Produci un site_resource_carbon_record con confini, periodo, fonti, letture, fattori, conversioni, acqua, energia, CO2e, normalizzatori, incertezza, azioni e stato measured, estimated, conditional o blocked. Ogni KPI dichiara denominatore, periodo, fonte e qualità del dato.

## Quality gates

- Confini, fase, fonti, inclusioni/esclusioni e responsabili sono approvati.
- Contatori, fatture, serbatoi e stime sono riconciliati e le perdite o gap sono visibili.
- Unit conversion, fattori, anno, geografia e GWP sono versionati e replicabili.
- Acqua prelevata, riutilizzata, scaricata e persa sono separate; non usare una sola cifra aggregata.
- Emissioni Scope 1/2/altre categorie sono dichiarate secondo il metodo adottato, senza doppio conteggio.
- Target e claim sono subordinati a misura, baseline, qualità e revisione competente.

## Evidenza e provenienza

Conserva letture e foto contatori, seriali, fatture, fuel tickets, telemetria, log mezzi, registri acqua, autorizzazioni scarichi, dati subappaltatori, fattori emissivi, formule, baseline e azioni. Marca misurato, stimato, allocato, calcolato e compensato. Proteggi dati commerciali e informazioni sulle utenze; non cancellare gap o cambi di metodo.

## Fonti ufficiali e diritti

- [ISO 50001 — energy management](https://www.iso.org/iso-50001-energy-management.html): quadro ufficiale per gestione dell'energia e miglioramento.
- [ISO carbon footprint](https://www.iso.org/renewable-energy/carbon-footprint): riferimenti ufficiali a ISO 14064, ISO 14040/14044 e accounting GHG.
- [ISO 46001 — management system for water efficiency](https://www.iso.org/standard/68256.html): riferimento ufficiale per efficienza idrica.
- [ISPRA](https://www.isprambiente.gov.it/it): dati e riferimenti ambientali istituzionali da verificare per contesto e autorizzazioni.

Record, calcoli, controlli di qualità e workflow sono originali. Diritti: official_reference_only_no_text_reproduced; standard, fattori proprietari, bollette, telemetria e dati di terzi non sono redistribuiti. Un valore CO2e non equivale a certificazione o claim pubblicitario.

## Confini professionali e legali

La skill non emette inventario GHG verificato, certificazione ambientale, autorizzazione allo scarico, dichiarazione di carbon neutrality, incentivo o conformità energetica. Non sostituisce energy manager, environmental specialist, laboratorio, consulente GHG, gestore del servizio, progettista o autorità. Le decisioni che cambiano impianti, carburanti, scarichi o sicurezza richiedono approvazione competente.

## Failure modes

- **Confini cambiati a consuntivo:** congela il metodo e ricalcola le serie, documentando il break.
- **Fattore senza anno/geografia:** blocca il claim e sostituisce con fonte versionata.
- **Litri, kWh e m3 sommati:** separa grandezze e applica conversioni tracciate.
- **Acqua stimata presentata come misurata:** marca stima e definisci misura o range.
- **Riduzione da calo attività:** normalizza e mostra produzione, ore e clima.
- **Compensazione scambiata per riduzione:** separa riduzione reale, avoided emissions e offset.

## Strumenti

Usa utility register, meter map, reading log, fuel/water ledger, factor register, conversion sheet, baseline/normalization model, GHG inventory table e action tracker. Automatizza validazione unità, gap, fattori e riconciliazioni; non pubblicare claim o attribuire risparmi definitivi senza revisione e approvazione.
