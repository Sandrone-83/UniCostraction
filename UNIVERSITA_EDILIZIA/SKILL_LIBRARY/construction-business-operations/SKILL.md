---
name: construction-business-operations
description: Pianifica e controlla impresa di costruzioni e commesse con modelli di costi, capacità, approvvigionamento, produzione, cassa, rischio e KPI verificabili.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: gestione d'impresa, commesse e operations edilizie
---

# Impresa di costruzioni, imprenditorialità e operations

## Attivazione

Usa la skill per business plan, qualificazione di commesse, preventivazione, budget, pianificazione di produzione, acquisti, subappalti, capacità, controllo costi, cassa, KPI e miglioramento operativo. Non trasformare una simulazione economica in promessa di margine, solvibilità o risultato fiscale.

## Input

Acquisisci forma e territorio dell'impresa, periodo contabile, organico, mezzi, pipeline, contratti, listini, prezziari, costi diretti/indiretti, ore, produttività, acquisti, subappalti, impegni, incassi, finanziamenti, assicurazioni, rischi e vincoli di sicurezza. Chiedi fonte, data, IVA, valuta, unità e stato: preventivo, impegnato, maturato, fatturato, incassato o stimato.

## Workflow

1. Definisci decisione, periodo, perimetro societario e commessa; separa dati storici, forecast e scenario.
2. Costruisci struttura di commessa: WBS, centri di costo, risorse, quantità, prezzi, ore, produzione prevista e responsabili.
3. Calcola costo e ricavo con regole esplicite per diretti, indiretti, rischi, oneri, finanziari, imposte e margine; non mescolare IVA e redditività.
4. Verifica capacità di persone, attrezzature, subappaltatori, spazio, materiali, cassa e tempi rispetto alla pipeline.
5. Collega acquisti e impegni a fabbisogni, lead time, alternative, qualità, lotti, consegne e condizioni di pagamento.
6. Imposta ritmo operativo: programma, avanzamento fisico, ore, produttività, non conformità, varianti, cost-to-complete e forecast a finire.
7. Chiudi con dashboard, scostamenti, cause, azione, owner, scadenza e riesame; conserva anche le ipotesi scartate.

## Output

Produci scheda opportunità, budget e cash-flow, matrice costi/ricavi, capacità e pipeline, piano approvvigionamenti, WBS e calendario, registro rischi, forecast a finire, dashboard KPI e verbale decisionale. Indica per ogni numero fonte, data, stato e livello di confidenza.

## Quality gates

- Costi diretti, indiretti, costi di struttura, oneri, IVA, imposte e finanziamento sono separati.
- Impegnato, maturato, fatturato, pagato e previsto non sono trattati come lo stesso valore.
- Produttività e prezzi hanno unità, periodo, squadra, luogo e condizioni comparabili.
- Cash-flow espone scadenze, ritardi, ritenute, anticipi e scenari; il margine non prova la liquidità.
- Ogni KPI ha formula, fonte, owner, frequenza, soglia e azione; dati personali e salariali sono minimizzati.

## Provenienza ed evidenza

Conserva contabilità o estratti autorizzati, preventivi, contratti, ordini, DDT, timesheet, misure, SAL, fatture, incassi, listini, verbali e versioni dei fogli con hash e permessi. Registra chi ha inserito o approvato ogni rettifica. Un dashboard non auditato non è bilancio, contabilità ufficiale o attestazione di solvibilità.

## Controllo versione, territorio e data

Indica paese, regione, valuta, regime fiscale, anno d'imposta, versione di classificazioni, prezziario, contratto collettivo, aliquote, scadenze e data di cambio. Verifica periodicamente fonti ISTAT, Agenzia delle Entrate, INAIL, prezzi e regole del committente; non portare un KPI o costo storico in un nuovo territorio senza ricalibrazione.

## Confini professionali e legali

La skill non sostituisce commercialista, revisore, consulente del lavoro, consulente finanziario, RSPP, legale o amministratore. Non presenta dichiarazioni, paga imposte, assume personale, firma contratti, approva subappalti, concede credito o invia offerte senza autorizzazione. Le decisioni su sicurezza e lavoro seguono i ruoli obbligatori e la normativa vigente.

## Failure modes

- **Margine positivo e cassa negativa:** ricostruisci scadenze, anticipi, ritardi, ritenute e cost-to-complete.
- **Preventivo senza produttività:** separa quantità, ore, squadra, condizioni e rischio.
- **Ordine duplicato:** confronta impegno, consegna, fattura e centro di costo con identificativi univoci.
- **KPI scelto per convenienza:** conserva definizione, periodo e dati grezzi; non cambiare formula retroattivamente.
- **Prezziario scaduto:** verifica edizione, territorio, data di validità e clausola di aggiornamento.

## Strumenti

Usa ERP o fogli protetti, WBS, calendario, registro acquisti, analisi dati, contabilità gestionale, repository documentale e dashboard con ruoli. Automatizza riconciliazioni solo con log, controlli di quadratura e possibilità di ricostruire il dato originale; evita fogli senza owner o versione.

## Fonti ufficiali e diritti

- [ISTAT — Classificazioni](https://www.istat.it/classificazioni/): `rights_state: official_reference_only_no_text_reproduced`; classificazioni ufficiali da verificare per edizione e data.
- [Agenzia delle Entrate](https://www.agenziaentrate.gov.it/portale/): `rights_state: official_reference_only_no_text_reproduced`; riferimenti istituzionali fiscali; non sostituisce il parere sul caso concreto.
- [INAIL](https://www.inail.it/portale/it.html): `rights_state: official_reference_only_no_text_reproduced`; orientamenti istituzionali su prevenzione e lavoro; verificare la disciplina applicabile.

La procedura è una sintesi originale. Dati contabili, modelli aziendali, listini, software, contratti e banche dati mantengono diritti, segreti e autorizzazioni propri.
