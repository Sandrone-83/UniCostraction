---
name: procurement-subcontractor-supply-chain-qualification
description: Struttura qualifica, due diligence, onboarding, subappalto e monitoraggio della filiera edilizia, senza aggiudicare, autorizzare subappalti o sostituire RUP, committente e legale.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: procurement, subappalto e qualificazione filiera
---

# Procurement, subappalto e qualificazione della filiera

## Attivazione e input

Attiva questa skill quando un fornitore, subappaltatore, lavoratore autonomo o filiera critica deve essere prequalificato, contrattualizzato, autorizzato all'accesso o monitorato per competenza, capacità, sicurezza, qualità, sostenibilità e continuità. È distinta da public-procurement-company-contracts, che governa il ciclo contrattuale generale, e da sustainable-procurement-cam-esg, che tratta CAM ed ESG.

Raccogli oggetto e categoria, requisiti tecnici, economici, legali e HSE, contratto e clausole, subappalto dichiarato, scope, organigramma, referenze, licenze, assicurazioni, capacità, DURC, qualificazioni, certificazioni, audit, supply chain tier, materiali critici, sanzioni/controversie dove legalmente consentito, privacy, conflitti e poteri di approvazione. Se scope, giurisdizione, requisito o titolare della decisione non sono definiti, lo stato è blocked.

## Workflow

1. **Gate del perimetro:** definisci prestazione, categoria, mercato pubblico/privato, giurisdizione, criticità, soglia e criteri minimi/premianti.
2. **Gate delle evidenze:** richiedi documenti con titolare, scadenza, scope, sito, prodotto e organismo; separa autodichiarazione, certificato, referenza e verifica indipendente.
3. **Gate della capacità:** valuta persone, mezzi, esperienza, metodo, qualità, sicurezza, finanza, continuità e capacità reale rispetto alla prestazione.
4. **Gate della filiera:** mappa subfornitori e subappaltatori, materiali e nodi critici; definisci approvazione, flow-down, audit, tracciabilità e sostituzione.
5. **Gate dell'integrità:** controlla conflitti, sanzioni e requisiti legalmente accessibili con fonti appropriate, minimizzando dati e senza inferenze reputazionali.
6. **Gate dell'onboarding:** collega contratto, scope, HSE, ITP, privacy, accessi, induzione, assicurazioni, deliverable e escalation; impedisci lavoro prima dei gate autorizzati.
7. **Gate del monitoraggio:** aggiorna scadenze, KPI, NCR, performance, pagamenti, incidenti, variazioni e audit; sospendi o riqualifica con decisione motivata.

## Output

Produci un supply_chain_qualification_record con scope, requisiti, evidence register, score/decision rule, filiera, approvazioni, scadenze, onboarding, monitoraggio, issue e stato screened, qualified, conditional, suspended o rejected. Il record deve distinguere idoneità documentale, tecnica, contrattuale e autorizzazione operativa.

## Quality gates

- Oggetto, requisiti, soglie, giurisdizione, decision owner e conflitti sono espliciti.
- Certificati, DURC, qualificazioni, assicurazioni e referenze hanno titolare, scope e validità verificati.
- Capacità dichiarata è coerente con risorse, persone, mezzi, siti e volume richiesto.
- Ogni subappalto/subfornitura è mappato, approvato secondo contratto e sottoposto a flow-down.
- HSE, qualità, privacy, diritti di audit, continuità e gestione NCR sono contrattualizzati.
- Nessun punteggio o rigetto si basa su dati irrilevanti, discriminatori, non verificati o fuori scopo.

## Evidenza e provenienza

Conserva RFQ, criteri, offerte, questionari, certificati, DURC e verifiche, referenze, audit, organigrammi, mezzi, assicurazioni, contratti, subcontratti, approvazioni, registri scadenze, performance, NCR e decision log. Marca dichiarato, verificato, scaduto, non applicabile e condizionato. Limita documenti societari e dati personali ai ruoli autorizzati.

## Fonti ufficiali e diritti

- [Normattiva — D.Lgs. 36/2023](https://www.normattiva.it/uri-res/N2Ls?urn%3Anir%3Astato%3Adecreto.legislativo%3A2023-03-31%3B36%21vig=): contratti pubblici, requisiti e subappalto, da verificare nella versione vigente.
- [ANAC — Codice dei contratti pubblici](https://www.anticorruzione.it/documents/91439/56f8f8cd-6004-5fcc-a05c-0aad83f7bbf7): atti e orientamenti ufficiali, da verificare per data e ambito.
- [INPS — DURC Online](https://www.inps.it/it/it/dettaglio-scheda.it.schede-servizio-strumento.schede-servizi.50130.durc-online.html): verifica telematica della regolarità contributiva.
- [Normattiva — D.Lgs. 81/2008](https://www.normattiva.it/eli/id/2008/04/30/008G0104/CONSOLIDATED): requisiti di sicurezza e ruoli di cantiere.

Matrice, questionari, scoring, workflow e record sono originali. Diritti: official_reference_only_no_text_reproduced; bandi, contratti, certificati, registri, banche dati e documenti societari restano soggetti a licenza, riservatezza e autorizzazione.

## Confini professionali e legali

La skill non aggiudica, non qualifica giuridicamente, non autorizza subappalto, non verifica in modo conclusivo antimafia/sanzioni, non rilascia DURC, non firma contratti e non sostituisce stazione appaltante, RUP, legale, HSE, procurement manager, SOA, INPS/INAIL o autorità. Un certificato non prova capacità attuale o prestazione futura.

## Failure modes

- **Certificato fuori scope:** sospendi il punteggio e richiedi prodotto, sito, periodo e titolare corretti.
- **DURC o assicurazione scaduti:** blocca onboarding/accesso e riapri verifica.
- **Subappaltatore non dichiarato:** congela attività e instrada a contract owner/RUP.
- **Tier 2 invisibile:** estendi la mappa ai materiali e processi critici.
- **Score reputazionale non provato:** rimuovi inferenza e usa criteri documentati.
- **Audit trasformato in approvazione:** separa finding, decisione e autorizzazione contrattuale.

## Strumenti

Usa supplier register, requirement matrix, evidence/scadenze register, DURC/insurance tracker, qualification questionnaire, supply-chain map, audit/NCR log, onboarding checklist e scorecard versionata. Automatizza reminder e completezza; non aggiudicare, autorizzare o sospendere rapporti in autonomia.
