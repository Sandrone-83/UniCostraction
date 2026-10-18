---
name: construction-schedule-cost-risk-control
description: Integra baseline di tempi, costi, avanzamento e rischi di cantiere con forecast e change control, senza sostituire direzione lavori, project manager, contabilità o autorità contrattuale.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: pianificazione tempi, costi e rischio di cantiere
---

# Pianificazione integrata di tempi, costi e rischio di cantiere

## Attivazione e input

Attiva questa skill quando un cantiere deve costruire o aggiornare una baseline integrata, leggere ritardi e costi, stimare il completamento o governare rischi e cambiamenti. È una faccetta di project controls distinta da construction-business-operations, sal-progress-quantity-reconciliation, public-procurement-company-contracts e construction-site-safety: non certifica SAL, non decide varianti, non firma contestazioni e non sostituisce il responsabile del contratto.

Prima raccogli WBS/OBS, contratto e revisioni autorizzate, programma, calendario, quantità, prezzi, budget, risorse, procurement, vincoli di accesso, meteo, progress rules, calendario di cut-off, contabilità, rischi, assunzioni, ruoli e soglie di escalation. Se data status, baseline, fonte dei costi o regola di avanzamento sono ignoti, lo stato è blocked.

## Workflow

1. **Gate del perimetro:** definisci deliverable, WBS, pacchetti, responsabilità e interfacce; separa programma contrattuale, piano operativo, forecast e registro storico.
2. **Gate della baseline:** congela calendario, logica, durate, quantità, costi, risorse, prezzi, date e vincoli; registra versione, approvatore e regola per ogni cambiamento.
3. **Gate della misurazione:** stabilisci cut-off, avanzamento fisico, earned value o regola equivalente, costi impegnati/contabilizzati/previsionali, produttività e fonti; non convertire fattura o percentuale dichiarata in lavoro eseguito.
4. **Gate del percorso:** calcola ritardi, float, vincoli, look-ahead e interfacce con procurement e approvazioni; isola effetto di dati mancanti, ritardo reale e modifica autorizzata.
5. **Gate del rischio:** registra evento, causa, probabilità, impatto su tempo/costo/sicurezza/qualità, trigger, owner, risposta, residuo e data di revisione. Usa scenari e range, non una riserva nascosta.
6. **Gate del forecast:** aggiorna estimate at completion, date probabili, cash profile, fabbisogni e downside; confronta baseline, corrente e scenario e spiega ogni varianza con evidenza.
7. **Gate del cambiamento:** valuta richiesta, effetto su WBS, costo, tempo, rischio, documenti e autorizzazioni; solo il ruolo competente approva baseline, ordine, variante o comunicazione contrattuale.

## Output

Consegna un project_controls_record con perimetro, baseline versionata, calendario, cost breakdown, cut-off, misure, varianze, forecast, registro rischi, scenari, change log, azioni, owner e stato controlled, conditional o blocked. Mantieni separati fatto misurato, previsione, riserva, richiesta e decisione approvata.

## Quality gates

- WBS, baseline, calendario, data di cut-off, regole di avanzamento e approvatori sono espliciti.
- Quantità, costi, impegni, fatture, forecast e pagamenti hanno stati e fonti distinti.
- Le varianze di tempo e costo sono riconciliate con attività, quantità, risorse e decisioni.
- Rischi e opportunità hanno owner, trigger, risposta, impatto e data di revisione.
- Il forecast mostra range, sensibilità e dati mancanti senza mascherare la riserva.
- Nessun output viene presentato come SAL approvato, variante autorizzata, contestazione o previsione certa.

## Evidenza e provenienza

Registra contratto e revisioni, programma nativo e PDF, baseline hashata, calendario, quantità, registri giornalieri, misure, ordini, impegni, fatture, costi, meteo, verbali, foto geolocalizzate, log di aggiornamento e approvazioni. Marca fonte, data, autore, trasformazione e confidenza. Dati commerciali, prezzi, persone e sicurezza sono limitati per ruolo; non incorporare credenziali o dati personali nei dashboard.

## Fonti ufficiali e diritti

- [ISO 21502:2020](https://committee.iso.org/sites/tc258/home/projects/published/iso-21502.html): guida ufficiale al project management applicabile a progetti di diversa scala e complessità.
- [D.Lgs. 36/2023 su Normattiva](https://www.normattiva.it/uri-res/N2Ls?urn%3Anir%3Astato%3Adecreto.legislativo%3A2023-03-31%3B36%21vig=): Codice dei contratti pubblici da verificare per regime, versione e ruolo.
- [ANAC — Banca dati nazionale contratti pubblici](https://www.anticorruzione.it/-/banca-dati-nazionale-contratti-pubblici): riferimento istituzionale per dati e tracciabilità nei contratti pubblici, con ambito da verificare.

ISO e altri standard sono restricted: si citano identificativo e scopo senza copiare contenuti. Gli atti normativi si consultano presso la fonte ufficiale e non conferiscono licenza generale per ripubblicare commenti o dati. Il metodo, il record, le formule di varianza e i gate sono originali. Stato diritti: official_reference_only_no_text_reproduced.

## Confini professionali e legali

La skill non approva SAL, non certifica quantità o pagamenti, non determina responsabilità contrattuale, non autorizza varianti, non firma riserve e non sostituisce project manager, direttore lavori, direttore dell'esecuzione, RUP, contabile, controller, legale o datore di lavoro. Un forecast non è una promessa di data o margine; un indicatore è valido solo per definizioni, dati e cut-off dichiarati.

## Failure modes

- **Baseline mobile:** congela versione e approvatore e separa il cambiamento dalla correzione retroattiva.
- **Avanzamento dichiarato senza misura:** mantieni stato non dimostrato e richiedi regola, quantità e fonte.
- **Costo fatturato scambiato per costo maturato:** separa committed, incurred, invoiced, paid e forecast.
- **Ritardo assorbito dal float:** mostra percorso, vincoli, interfacce e impatto sulla data obiettivo.
- **Rischio senza owner o trigger:** non conteggiare mitigazione e assegna responsabilità e data.
- **Dashboard usato come atto contrattuale:** blocca invio e richiedi revisione e autorizzazione competente.

## Strumenti

Usa planner con calendario e dipendenze, cost breakdown, registro quantità/costi, risk register, dashboard con snapshot, analisi scenari e repository versionato. Automatizza riconciliazioni, date, formule, soglie e audit trail; non automatizzare approvazioni, attestazioni o comunicazioni contrattuali.
