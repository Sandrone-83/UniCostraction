---
name: bim-4d-5d-planning-control
description: Collega modello, WBS, programma e cost baseline per pianificazione BIM 4D/5D verificabile, senza sostituire project control, computo approvato o decisioni contrattuali.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: pianificazione e controllo BIM 4D/5D
---

# Pianificazione e controllo BIM 4D/5D

## Attivazione e input

Attiva questa skill quando un progetto deve collegare elementi BIM, attività di programma, quantità, costi, avanzamento e scenari di costruzione in una vista 4D/5D auditabile. È distinta da bim-cde-information-security, che governa CDE e accessi, e da probabilistic-estimating-cost-engineering, che tratta incertezza e distribuzioni di costo.

Raccogli WBS/OBS/CBS, programma baseline e aggiornato, calendario e vincoli, modello coordinato con revisioni e GUID stabili, codici elemento-attività, quantità e regole di misura, rate/price source, cost code, unità, produttività, status date, percent complete, regole earned value, change log e responsabili. Se modello, programma, costo o data di stato non sono identificati, lo stato è blocked.

## Workflow

1. **Gate dell'allineamento:** definisci purpose, livello di dettaglio, baseline, codifica comune e regole di inclusione; non assumere che un modello geometrico sia già un modello di controllo.
2. **Gate della mappatura:** collega elementi, sistemi e zone a attività e cost codes tramite chiavi stabili; registra elementi non mappati, duplicati, aggregati e attività senza geometria.
3. **Gate delle quantità:** estrai quantità con regola dichiarata, unità coerenti, revisioni e confini; riconcilia estratto BIM, computo e misura contrattuale senza sostituire il computo approvato.
4. **Gate del tempo:** simula sequenze, accessi, aree, mezzi, subappalti, precedenze e vincoli; confronta baseline e forecast e marca assunzioni di produttività.
5. **Gate del costo:** collega quantità, rate, curve di produzione e costo autorizzato; separa committed, actual, forecast, allowance, variation e cost risk.
6. **Gate dell'avanzamento:** definisci status date, rule of credit, evidenza fisica e pesi; impedisci che percentuale dichiarata, colore del modello o ore caricate diventino avanzamento senza prova.
7. **Gate della decisione:** pubblica scenario, scostamenti, impatto e decisioni con revisione; congela baseline solo con approvazione e conserva la versione precedente.

## Output

Produci un bim_4d5d_control_record con modello/revisione, mapping, WBS/CBS, estratti quantità, programma, cost view, avanzamento, scostamenti, scenari, assunzioni e stato mapped, conditional o blocked. Ogni grafico o simulazione riporta data di stato, fonte, regola e limiti.

## Quality gates

- GUID, codici WBS/CBS, unità, calendario, status date e revisioni sono riconciliati.
- Tutti gli oggetti/attività rilevanti hanno esito mapped, intentionally_unmapped o issue aperta.
- Quantità, rate e pesi hanno provenienza e regola; nessun doppio conteggio tra aggregati e componenti.
- Baseline e forecast restano separati e gli aggiornamenti sono immutabili tramite log.
- Avanzamento e earned value hanno evidenza fisica/contrattuale e owner.
- Scenari 4D/5D sono presentati come supporto decisionale, non come autorizzazione a variare lavori, costi o tempi.

## Evidenza e provenienza

Conserva file IFC/native o estratti autorizzati, GUID, mapping table, WBS/CBS, revisioni, schedule exports, quantity take-off, rate book, cost ledger, progress photos, site records, change log e hash quando disponibile. Marca dato estratto, dato dichiarato, assunzione, forecast e decisione. Gestisci licenze di modelli, prezzi, immagini e dati di subappaltatori con minimo accesso.

## Fonti ufficiali e diritti

- [buildingSMART — Information Delivery Manual](https://www.buildingsmart.org/standards/bsi-standards/information-delivery-manual/): metodologia ufficiale per processi e flussi informativi, senza riprodurne il testo.
- [ISO 19650 — pagina ISO](https://www.iso.org/standard/68078.html): gestione dell'informazione nel ciclo di vita dell'asset, da verificare nell'edizione applicabile.
- [Normattiva — D.Lgs. 36/2023](https://www.normattiva.it/uri-res/N2Ls?urn%3Anir%3Astato%3Adecreto.legislativo%3A2023-03-31%3B36%21vig=): riferimenti al ciclo dei contratti pubblici quando pertinenti.
- [AACE International — recommended practices](https://web.aacei.org/resources/publications/recommended-practices): riferimenti professionali per cost e schedule, soggetti a licenza.

Il mapping, le regole di riconciliazione e il record sono originali. Diritti: official_reference_only_no_text_reproduced; standard, modelli, listini, schedule e contratti restano dei titolari. Non si copiano template proprietari o testi protetti.

## Confini professionali e legali

La skill non approva baseline, computi, SAL, varianti, claims, tempi contrattuali o budget; non sostituisce BIM manager, planner, cost controller, direttore lavori, RUP, progettista o contract manager. Un clash visivo o un modello 4D/5D non prova conformità, diritto al pagamento, produttività reale o autorizzazione di una modifica.

## Failure modes

- **GUID rigenerati:** blocca il confronto, ricostruisci identità e mappa le revisioni.
- **WBS diversa dal modello:** mantieni la voce non mappata e concorda codifica prima di produrre KPI.
- **Quantità doppie:** riconcilia aggregati, parti e unità e sospendi il totalizzato.
- **Forecast trattato come baseline:** ripristina versioni e marca la data di stato.
- **Avanzamento da colore:** richiedi evidenza di campo, regola di credito e approvazione.
- **Rate fuori periodo o scope:** verifica base date, inclusioni, escalation e licenza prima del forecast.

## Strumenti

Usa CDE autorizzato, IFC/model viewer, mapping table, WBS/CBS register, schedule tool, quantity take-off, cost workbook, progress evidence register, change log e dashboard. Automatizza controlli di chiavi, unità, duplicati e coverage; non aggiornare baseline, costi approvati o percentuali contrattuali senza autorizzazione.
