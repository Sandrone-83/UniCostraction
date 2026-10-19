---
name: probabilistic-estimating-cost-engineering
description: Costruisce stime di costo probabilistiche, range, contingency e decisioni di cost engineering con assunzioni e sensibilità senza trasformare una previsione in preventivo garantito o atto contrattuale.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: stima probabilistica e cost engineering
---

# Stima probabilistica e cost engineering

## Attivazione e input

Attiva questa skill quando una decisione di investimento, design, gara o commessa richiede costo base, range, probabilità di completamento, contingency, escalation o forecast at completion. È una faccetta quantitativa di estimate assurance distinta da construction-schedule-cost-risk-control, construction-business-operations, sal-progress-quantity-reconciliation e public-procurement-company-contracts: non approva budget, non certifica prezzi, non firma offerte o consuntivi.

Prima raccogli scopo e maturity della stima, WBS, quantità, inclusioni/esclusioni, classi di costo, base date, località, valuta, mercato, produttività, durate, schedule, escalation, rischio, opportunità, allowances, contingency, tax/VAT, finanziamento, contratti, dati storici e decisore. Registra fonte, qualità, periodo, correlazioni, distribuzioni e criterio P-value. Se perimetro, data base o denominatore sono ignoti, lo stato è blocked.

## Workflow

1. **Gate della base estimate:** definisci WBS/Cost Breakdown Structure, quantità, unità, prezzo base, inclusioni, esclusioni, allowances e currency; riconcilia il totale con quantità e deliverable.
2. **Gate della normalizzazione:** allinea località, anno, mercato, produttività, dimensione, valuta, indice, procurement route e condizioni; separa prezzo osservato, quota, proxy e giudizio.
3. **Gate delle incertezze:** distingue variabilità naturale, immaturità, omissione, rischio evento e opportunità; assegna range/distribuzione, motivazione, owner e dipendenze.
4. **Gate del modello:** scegli metodo deterministico/probabilistico, correlazioni, simulazioni, reference class e scenario; conserva seed, input, numero iterazioni, convergenza e versione del codice.
5. **Gate della contingency:** separa base cost, estimate uncertainty, risk contingency, management reserve, escalation, tax e financing; non nascondere rischio in voci generiche.
6. **Gate della decisione:** restituisci P10/P50/P80 o percentili dichiarati, range, sensitività, tornado, driver, downside, costo atteso e livello di confidenza; non scegliere percentile dopo aver visto il risultato.
7. **Gate del controllo:** congela baseline, confronta actual/commitment/forecast, spiega varianze e aggiorna il modello con change control; back-testa stime precedenti senza riscrivere la storia.

## Output

Consegna un probabilistic_estimate_record con base estimate, WBS/CBS, fonti, data/località, assunzioni, distribuzioni, correlazioni, simulazione, percentili, contingency, escalation, sensitività, rischi, forecast e stato screened, conditional o blocked. Ogni cifra conserva definizione, confine, probabilità, valuta, base date e autorizzazione d'uso.

## Quality gates

- Scopo, maturità, perimetro, WBS/CBS, valuta, base date e inclusioni sono dichiarati.
- Quantità, prezzi, proxy, indici, produttività e contratti hanno fonte e qualità.
- Incertezza, rischio evento, opportunità, escalation, contingency e reserve sono separati.
- Distribuzioni e correlazioni sono motivate, versionate e sottoposte a sensibilità/back-test.
- P-value, range, driver e scenario di downside sono leggibili e non presentati come certezza.
- Nessuna stima viene presentata come budget approvato, prezzo contrattuale, offerta o garanzia senza autorizzazione.

## Evidenza e provenienza

Conserva estimate sheets, WBS/CBS, quantità, listini, offerte, contratti, indici, dati storici, reference class, assunzioni, giudizi esperti, script, seed, output simulazioni, revisioni, approvazioni e hash. Marca dato osservato, proxy, normalizzato, imputato, simulato e giudicato. Prezzi, offerte e margini sono riservati; dati di terzi restano soggetti a licenza.

## Fonti ufficiali e diritti

- [ISO 21502:2020](https://committee.iso.org/sites/tc258/home/projects/published/iso-21502.html): guida ufficiale al project management e al controllo del contesto di progetto.
- [ISO 21512](https://committee.iso.org/sites/tc258/home/projects/published/iso-21512.html): riferimento ISO per implementazione dell'earned value management, da verificare per edizione e applicabilità.
- [AACE International — Recommended Practices](https://web.aacei.org/resources/publications/recommended-practices): pratiche professionali ufficiali per cost engineering e stima, soggette a membership/licenza.
- [D.Lgs. 36/2023 su Normattiva](https://www.normattiva.it/uri-res/N2Ls?urn%3Anir%3Astato%3Adecreto.legislativo%3A2023-03-31%3B36%21vig=): quadro dei contratti pubblici, da verificare per fase, ruolo e procedura.

ISO, AACE, listini, offerte, database e documenti contrattuali hanno diritti e licenze proprie; si citano identificativi e scopo senza riprodurre testi o dati. Il modello di stima, le matrici, le formule e i gate sono originali. Stato diritti: official_reference_only_no_text_reproduced.

## Confini professionali e legali

La skill non approva investimenti, non certifica budget, non determina prezzo contrattuale, non firma offerte, non decide contingency, non assevera danni o responsabilità e non sostituisce cost engineer, estimator, controller, project manager, RUP, direttore lavori, commercialista o legale. Un percentile non è una probabilità di successo se popolazione, modello, correlazioni e qualità dati non sono dimostrati.

## Failure modes

- **Base estimate incompleta:** blocca il range e costruisce registro di scope gap e maturity.
- **P50 chiamato budget garantito:** esplicita percentile, rischio residuo, esclusioni e decisione autorizzata.
- **Contingency doppia o nascosta:** separa eventi, uncertainty, reserve, escalation e tax e riconcilia il totale.
- **Distribuzioni arbitrarie:** usa dati, analoghi, giudizi documentati e sensibilità, non curve estetiche.
- **Correlazioni ignorate:** analizza driver comuni come quantità, mercato, durata e produttività.
- **Cambiamento retroattivo:** congela snapshot, registra change log e confronta forecast senza alterare la baseline storica.

## Strumenti

Usa WBS/CBS, cost database, normalizzazione indici, estimate workbook, risk register, simulazione Monte Carlo riproducibile, scenario manager, tornado chart, EVM e audit repository. Automatizza unità, formule, distribuzioni, seed, percentili e riconciliazioni; non automatizzare approvazione, prezzo d'offerta o decisione finanziaria.
