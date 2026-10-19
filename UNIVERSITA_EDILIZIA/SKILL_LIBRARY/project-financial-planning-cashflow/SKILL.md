---
name: project-financial-planning-cashflow
description: Costruisce il piano economico-finanziario e il cash flow di una commessa collegando WBS, impegni, costi maturati, fatture, incassi e pagamenti senza trasformare il forecast in budget garantito o consiglio finanziario.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: pianificazione economico-finanziaria e cash flow di commessa
---

# Pianificazione economico-finanziaria e cash flow di commessa

## Attivazione e input

Attiva questa skill quando una commessa deve tradurre programma e contratto in budget, fabbisogno di cassa, piano incassi/pagamenti, forecast a finire o scenari di liquidità. È distinta da probabilistic-estimating-cost-engineering, che tratta range e probabilità, da operational-lifecycle-cost-evaluation, che tratta costi dell'asset lungo la vita, e da construction-business-operations, che tratta gestione aziendale generale.

Raccogli contratto e varianti approvate, WBS/OBS/CBS, calendario, budget, prezzi e base date, acquisti, subappalti, ore e quantità, impegni, costi maturati, fatture, SAL, ritenute, anticipi, milestone, incassi, pagamenti, garanzie, IVA, valuta, finanziamento, contingency e autorizzazioni. Se perimetro, cut-off, regole di competenza o calendario di cassa non sono definiti, lo stato è blocked.

## Workflow

1. **Gate del perimetro:** separa valore contrattuale, costi diretti/indiretti, overhead, esclusioni, pass-through, IVA e flussi del proprietario da quelli dell'appaltatore.
2. **Gate della struttura:** collega WBS, CBS, centri di costo, pacchetti di acquisto, subcontratti, milestone e conti bancari; definisci codice e responsabile di ogni movimento.
3. **Gate della baseline:** congela budget, curva costi, curva ricavi, programma, regole di accrual e base date con versione e approvazione; registra change log.
4. **Gate del rilevato:** riconcilia actual cost, commitments, goods received, invoice, payment, SAL, incasso e forecast con cut-off comune; separa maturato, fatturato e pagato.
5. **Gate della cassa:** costruisci cash-in/cash-out per periodo considerando termini, anticipo, ritenute, garanzie, retention, IVA, ritardi e valuta; esplicita il lag tra produzione, fattura e incasso.
6. **Gate del forecast:** aggiorna ETC/EAC, cash requirement e date di picco con scenario base, prudente e stress; collega variazioni a cause, owner e azione.
7. **Gate decisionale:** presenta varianze, covenant/limiti interni, fabbisogno e richieste di approvazione; il forecast diventa piano autorizzato solo con firma del decisore competente.

## Output

Produci un project_cashflow_record con perimetro, WBS/CBS, baseline, cut-off, budget, commitments, actual, accruals, fatturato, incassi, pagamenti, curva cumulata, ETC/EAC, working-capital lag, scenari, rischi, assunzioni, fonti e stato screened, conditional, approved_by_controller o blocked. Mostra sempre valuta, IVA, base date e distinzione forecast/actual.

## Quality gates

- Budget, ricavi, costi, cash-in e cash-out non sono sommati in un unico numero.
- Actual, accrual, commitment, invoice, payment e SAL hanno definizioni e periodi compatibili.
- Ogni variazione ha riferimento a contratto, change, ordine, timesheet, quantità o decisione.
- Curva di cassa, piano lavori e termini di pagamento sono coerenti e riconciliati.
- IVA, ritenute, anticipi, garanzie, valuta, interessi e ritardi sono trattati secondo contesto e non inventati.
- Il forecast riporta intervallo e rischio: non è margine certo, disponibilità bancaria garantita o autorizzazione a spendere.

## Evidenza e provenienza

Conserva contratto, budget approvato, WBS/CBS, calendario, ordini, subcontratti, timesheet, quantità, ricezioni, fatture, SAL, estratti contabili, incassi, pagamenti, tassi, assunzioni, formule, cut-off, riconciliazioni e approval log. Marca dato contabile, misurato, impegnato, stimato, proxy e scenario. Proteggi prezzi, conti, coordinate bancarie e informazioni finanziarie secondo ruoli e retention.

## Fonti ufficiali e diritti

- [ISO 21508 — Earned value management](https://committee.iso.org/sites/tc258/home/projects/published/iso-21508-ed2.html): riferimento metodologico ufficiale per collegare scope, tempi, costi e performance; usare l'edizione acquistata/licenziata applicabile.
- [RGS/OpenBDAP — perimetro degli investimenti pubblici](https://openbdap.rgs.mef.gov.it/it/Home/PerimetroInvestimentiPubblici): contesto istituzionale per monitoraggio finanziario, fisico e procedurale delle opere pubbliche.
- [RGS/Open Data — opere pubbliche](https://bdap-opendata.rgs.mef.gov.it/tema/opere-pubbliche): dati pubblici su piano costi, pagamenti, finanziamenti e iter, con licenza dichiarata dal catalogo.
- [Normattiva — D.Lgs. 36/2023](https://www.normattiva.it/atto/caricaDettaglioAtto?atto.codiceRedazionale=23G00044&atto.dataPubblicazioneGazzetta=2023-03-31): verificare disposizioni vigenti su contratto, programmazione, esecuzione e contabilità pubblica quando applicabili.

La procedura, il modello di cash flow e le tassonomie sono originali. Diritti: `official_reference_only_no_text_reproduced` per standard, portali e linee guida; contratti, listini, contabilità, dati bancari, software e dataset di terzi restano soggetti a licenza, riservatezza e accesso autorizzato.

## Confini professionali e legali

La skill non approva budget, finanziamenti, linee di credito, pagamenti, rendicontazioni fiscali o bilanci, non certifica SAL, non dichiara margini e non sostituisce direttore lavori, controller, commercialista, CFO, revisore, banca, stazione appaltante o organo deliberante. Un forecast è una previsione condizionata: non è garanzia di cassa, utile o solvibilità.

## Failure modes

- **Pagato confuso con maturato:** separa i quattro stati economici e riconciliali al cut-off.
- **Cash flow basato sul budget soltanto:** aggiungi termini contrattuali, lag, retention, IVA e impegni reali.
- **Forecast che incorpora varianti non approvate:** mostra scenario separato e richiedi autorizzazione.
- **Costo negativo o duplicato:** controlla segni, storni, pass-through, competenza e mapping CBS.
- **Curva ottimistica senza stress:** esegui scenario di ritardo, inflazione, claims, ritardi incasso e acquisti anticipati.
- **Dashboard usata come ordine di pagamento:** blocca l'azione e instrada al processo autorizzativo.

## Strumenti

Usa WBS/CBS dictionary, cost ledger, commitment register, accrual schedule, invoice/payment matching, S-curve, cash waterfall, EAC/ETC, scenario sheet, variance log, covenant/limit register e approval workflow. Automatizza riconciliazioni e controlli di unità; non esportare o inviare dati finanziari fuori dal perimetro autorizzato.
