---
name: operational-lifecycle-cost-evaluation
description: Valuta costi operativi, manutenzione, sostituzione, energia e fine vita lungo il ciclo dell'asset con scenari e attualizzazione tracciabili, senza sostituire budget approvato o decisione finanziaria.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: costi operativi e ciclo di vita
---

# Valutazione dei costi operativi e del ciclo di vita

## Attivazione e input

Attiva questa skill quando una scelta tecnica o di gestione deve essere confrontata per costi di acquisizione, energia, acqua, personale, manutenzione, ricambi, sostituzione, fermo, dismissione e rischi per un periodo dichiarato. È distinta da probabilistic-estimating-cost-engineering, che tratta incertezza della stima, e da predictive-maintenance-reliability, che tratta affidabilità e decisioni condizionate.

Raccogli asset e funzione, alternative, orizzonte, vita utile, service levels, CAPEX, OPEX, consumi, tariffe, manutenzione preventiva/correttiva, ricambi, manodopera, rinnovi, downtime, inflazione, tasso di sconto, fiscalità, finanziamento, valore residuo, rischi, externalities e dati storici. Se funzione, periodo, confini o base date non sono definiti, lo stato è blocked.

## Workflow

1. **Gate dello scopo:** definisci decisione, alternative, orizzonte, confini costi/ricavi/externalities e prospettiva del proprietario o gestore.
2. **Gate della funzione:** verifica che le alternative forniscano servizio, comfort, capacità, sicurezza e disponibilità comparabili; registra differenze e compensazioni.
3. **Gate della baseline:** costruisci cost taxonomy, asset hierarchy, cost drivers, base date, quantità, tariffe, frequenze e qualità dei dati.
4. **Gate dello scenario:** modella acquisizione, energia, acqua, manutenzione, rinnovi, ricambi, downtime, fine vita e valore residuo per ciascuna alternativa.
5. **Gate economico:** applica attualizzazione, escalation e unità coerenti; separa costo nominale, reale, presente, budget, rischio e costo esterno.
6. **Gate della sensibilità:** prova vita, tariffa, tasso, frequenza, guasto, performance, disponibilità e residual value; mostra driver e break-even.
7. **Gate della decisione:** produce raccomandazione condizionata con range, assunzioni, dati mancanti, monitoraggio e decisione autorizzata; aggiorna il forecast con actuals.

## Output

Produci un lifecycle_cost_record con funzione, alternative, confini, base date, cash flow, OPEX/CAPEX, attualizzazione, scenari, sensitività, rischi, dati e stato screened, conditional, approved_by_owner o blocked. Se il valore dipende da un'ipotesi, riportala vicino al risultato.

## Quality gates

- Funzione, asset, orizzonte, vita, service level e base date sono comuni o differenziati esplicitamente.
- CAPEX, OPEX, energia, manutenzione, sostituzione, downtime e fine vita hanno fonti e unità.
- Tasso, inflazione, escalation, fiscalità, tariffa e valore residuo sono dichiarati e non mischiati.
- Costi di alternative non duplicano manutenzione, rinnovi, incentivi o externalities.
- Sensitività e break-even mostrano quanto la decisione dipenda dalle assunzioni.
- Il risultato è presentato come supporto decisionale e non come costo certo, prezzo contrattuale o garanzia di risparmio.

## Evidenza e provenienza

Conserva asset register, OPR/service levels, preventivi, contratti manutenzione, fatture, tariffe, log consumi, work order, failure data, replacement plan, formule, tasso, scenario, software e approvazioni. Marca actual, forecast, proxy, vendor quote e assunzione. Proteggi prezzi, contratti e dati operativi di terzi.

## Fonti ufficiali e diritti

- [ISO 15686-5:2017](https://committee.iso.org/standard/61148.html?browse=tc): life-cycle costing per edifici e asset costruiti.
- [ISO 55001](https://www.iso.org/standard/83054.html): gestione del valore e del ciclo di vita degli asset.
- [ISO 50001](https://www.iso.org/iso-50001-energy-management.html): gestione dell'energia e miglioramento delle prestazioni.
- [Commissione europea — Level(s)](https://environment.ec.europa.eu/topics/circular-economy/levels_en): indicatori e framework europeo per performance del costruito quando pertinente.

Il modello, le tassonomie e i record sono originali. Diritti: official_reference_only_no_text_reproduced; standard, offerte, dati tariffari, software e modelli finanziari di terzi mantengono diritti e licenze.

## Confini professionali e legali

La skill non approva investimenti, budget, business plan, tariffa, valore immobiliare o finanziamento, non garantisce risparmi e non sostituisce cost engineer, facility manager, energy manager, finanziario, proprietario, revisore o organo deliberante. Un LCC non è una valutazione LCA, una diagnosi energetica o una certificazione.

## Failure modes

- **Alternative non equivalenti:** blocca confronto e riallinea servizio e prestazioni.
- **OPEX da brochure:** richiedi dati storici, condizioni e range.
- **Tasso/escalation incoerenti:** ricalcola con base date e convenzioni esplicite.
- **Risparmio senza downtime o rinnovi:** riapri il confine e mostra costi omessi.
- **P50 trattato come costo certo:** separa scenario, rischio e decisione.
- **Valore residuo inventato:** usa evidenza o sensibilità, non una cifra per far prevalere un'alternativa.

## Strumenti

Usa asset/cost taxonomy, cash-flow model, OPEX ledger, maintenance plan, tariff/factor register, discount/escalation sheet, sensitivity/tornado, break-even e approval log. Automatizza unità, formule, scadenze e versioni; non impegnare budget o comunicare garanzie in autonomia.
