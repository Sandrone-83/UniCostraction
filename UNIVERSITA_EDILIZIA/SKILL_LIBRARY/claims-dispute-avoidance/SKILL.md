---
name: claims-dispute-avoidance
description: Struttura early warning, cronologia, notices, entitlement, quantum e percorsi collaborativi per prevenire escalation contrattuali, senza redigere atti legali o assumere decisioni per le parti.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: gestione reclami, claims e dispute avoidance
---

# Gestione reclami, claims e dispute avoidance

## Attivazione e input

Attiva questa skill quando una parte segnala ritardo, variazione, interferenza, accesso negato, costo aggiuntivo, qualità contestata, pagamento, evento compensabile o rischio di controversia e serve preservare fatti e opzioni senza irrigidire prematuramente la posizione. È distinta da public-procurement-company-contracts, che tratta il ciclo contrattuale generale, e da construction-schedule-cost-risk-control, che tratta il controllo corrente di tempi, costi e rischio.

Raccogli contratto e gerarchia documentale, legge e foro applicabili, notice clauses e termini, scope/WBS, baseline di tempi e costi, cronologia, corrispondenza, submittal, accessi, ordini, istruzioni, misure, records contemporanei, eventi, impatto, mitigazioni, assicurazioni, escalation e deleghe. Se contratto, parti, evento, data o termine non sono verificabili, lo stato è blocked e il record resta preliminare.

## Workflow

1. **Gate della preservazione:** crea issue ID, calendario dei fatti, custodia dei record e separazione tra dato, opinione, privilegio legale e comunicazione negoziale.
2. **Gate del contratto:** estrai solo clausole necessarie, notice, condizioni, cause di compensazione, obblighi di mitigazione, dispute ladder, documentazione e poteri di firma; non assumere che prassi o email prevalgano.
3. **Gate della causalità:** ricostruisci evento, responsabilità potenziale, diritto contrattuale, interferenze e percorso critico con baseline e aggiornamenti, separando correlazione da causa.
4. **Gate dell'impatto:** quantifica o stima tempo, costo, risorse e disruption con metodo dichiarato, inclusioni/esclusioni, actuals, forecast e doppio conteggio controllato.
5. **Gate dell'early warning:** segnala rischio e opzioni tempestivamente al titolare autorizzato, proponendo mitigazione, istruzione, accesso, prova o accordo transitorio senza ammettere responsabilità.
6. **Gate del notice:** prepara una bozza interna di dati e scadenze per il legale/contract manager; il testo inviato deve essere approvato, firmato e trasmesso secondo contratto.
7. **Gate della soluzione:** prova escalation collaborativa, riunione tecnica, decisione documentata, negoziazione o mediazione prevista; se fallisce, preserva fascicolo e instrada al legale/arbitro/autorità competente.

## Output

Produci un claim_issue_record con issue, eventi, clausole da verificare, timeline, causa, impatto, evidenze, mitigazioni, termini, owner, opzioni e stato early_warning, under_review, negotiated, escalated o blocked. Produci anche un decision log che distingue proposta, posizione, ammissione, accordo e atto formalmente trasmesso.

## Quality gates

- Contratto, versione, foro, parti, termine e canale di notice sono verificati.
- Fatti e documenti contemporanei sono ordinati e collegati; opinioni e stime sono marcate.
- Entitlement, causation, delay, quantum e contributory factors sono analizzati separatamente.
- Ogni cifra ha base, unità, periodo, fonte, assunzioni e controllo duplicazioni.
- Early warning e mitigazione non cancellano diritti né costituiscono ammissioni non autorizzate.
- Nessun notice, rinuncia, transazione, accordo o posizione legale viene inviato senza delega e revisione competente.

## Evidenza e provenienza

Conserva contratto e allegati con versione, registro revisioni, contemporaneous records, giornali di cantiere, RFI, transmittal, email, istruzioni, foto, access log, programma baseline e aggiornato, cost ledger, timesheet, procurement, verbali, misure e calcoli. Usa hash o sistema di conservazione controllato dove autorizzato; non cancellare, retrodatare, alterare o ricostruire email come originali. Limita dati personali e comunicazioni riservate agli autorizzati.

## Fonti ufficiali e diritti

- [ISO 10002:2018](https://www.iso.org/standard/71580.html): linee guida ufficiali per gestione dei reclami interni; lo standard distingue reclami e dispute esterne.
- [ISO 10003:2018 — catalogo ISO/TC 176](https://www.iso.org/committee/53934/x/catalogue/): riferimento ufficiale per risoluzione esterna delle dispute, da verificare nello stato corrente.
- [Normattiva — D.Lgs. 36/2023](https://www.normattiva.it/uri-res/N2Ls?urn%3Anir%3Astato%3Adecreto.legislativo%3A2023-03-31%3B36%21vig=): rimedi e procedure dei contratti pubblici quando applicabili.
- [ANAC](https://www.anticorruzione.it/): atti e indicazioni istituzionali per la contrattualistica pubblica; verificare ambito e data.

La matrice, la cronologia, i registri e il workflow sono originali. Diritti: official_reference_only_no_text_reproduced; contratto, corrispondenza, dati di costo e standard sono soggetti a titolarità, riservatezza e licenze proprie. Non si copiano clausole, moduli o testi di terzi oltre il riferimento necessario.

## Confini professionali e legali

La skill non formula pareri legali, non interpreta definitivamente il contratto, non quantifica un danno vincolante, non redige o invia notice, riserve, transazioni, atti giudiziari o arbitrali e non rappresenta una parte. Non sostituisce avvocato, contract manager, RUP, direttore lavori, project manager, perito, mediatore o arbitro. Il record interno non è una ammissione, rinuncia o prova autosufficiente.

## Failure modes

- **Termine scaduto non verificato:** segnala urgenza al titolare, congela conclusioni e ricostruisci contratto/versione/canale.
- **Cronologia ricostruita a memoria:** marca l'incertezza e cerca record contemporanei; non retrodatare.
- **Ritardo attribuito dal solo aggiornamento:** esegui analisi causale e confronto baseline, progressi e mitigazioni.
- **Costo senza base:** separa actual, forecast, allowance e stima; blocca cifra presentata come danno certo.
- **Email inviata come notice:** controlla poteri, forma e clausola prima di ogni trasmissione.
- **Negoziazione confusa con accettazione:** registra opzioni e senza-prejudice secondo indicazione legale; non chiudere diritti implicitamente.

## Strumenti

Usa issue register, chronology builder, notice calendar, contract obligation matrix, baseline comparison, delay/quantum workbook, document hold, decision log e action tracker. Automatizza estrazione metadati, scadenze e collegamenti documentali; non inviare comunicazioni, calcolare diritti vincolanti o decidere la strategia legale in autonomia.
