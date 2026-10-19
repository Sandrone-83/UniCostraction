---
name: seismic-structural-deposits
description: Organizza classificazione, fascicolo e tracciamento di preavviso, deposito e autorizzazione sismica delle opere strutturali, senza sostituire progettazione, asseverazione o controllo dell'ufficio competente.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: pratiche sismiche e deposito opere strutturali
---

# Pratiche sismiche e deposito delle opere strutturali

## Attivazione e input

Attiva questa skill quando un intervento strutturale in zona sismica deve essere classificato e accompagnato da progetto, preavviso, deposito, autorizzazione, denuncia o integrazione presso lo sportello/ufficio regionale. È distinta da structural-civil-engineering, che tratta analisi e progettazione, da geotechnical-foundation-data-gating, che tratta dati geotecnici, e da construction-quality-itp-nonconformity, che tratta controlli esecutivi.

Raccogli località e classificazione sismica, intervento, uso, struttura esistente, livello di conoscenza, categoria rilevanza/minore/priva, titolo edilizio, progettista, direttore lavori, collaudatore, impresa, relazione, elaborati, calcoli, materiali, geologia/geotecnica, modello, firma, portale regionale, ricevute, termini e varianti. Se categoria, ufficio, versione normativa o set documentale non sono verificabili, lo stato è blocked.

## Workflow

1. **Gate di giurisdizione:** identifica regione, ufficio tecnico, portale, modulistica, classificazione, deleghe e regola locale; la procedura nazionale non sostituisce requisiti regionali.
2. **Gate dell'intervento:** classifica nuova costruzione, riparazione, sopraelevazione, intervento locale, miglioramento, adeguamento, variante sostanziale o non sostanziale secondo atto e responsabilità professionale.
3. **Gate di coerenza:** riconcilia progetto architettonico, strutturale, geotecnico, sismico, materiali, titolo edilizio, relazione e modello; registra ogni differenza come issue.
4. **Gate del fascicolo:** controlla tavole, relazione, calcoli, asseverazioni, nomine, elaborati geologici/geotecnici, piano controlli, firme, file, naming, formato e allegati richiesti dal portale.
5. **Gate della presentazione:** verifica soggetto legittimato, delega, firma, pagamento, invio, ricevuta, numero pratica e stato istruttoria; separa deposito, autorizzazione, ricevuta e silenzio.
6. **Gate delle integrazioni:** registra richiesta dell'ufficio, risposta, revisione, data, responsabile e impatto sul titolo; non sostituire un elaborato approvato con uno non tracciato.
7. **Gate di esecuzione e chiusura:** trasferisci pratica e prescrizioni a direzione lavori, controlli materiali, varianti, collaudo e agibilità; conserva as-built e prova dell'atto finale.

## Output

Produci un seismic_structural_filing_record con sito, categoria, intervento, fonti, ruolo, autorità, document register, revisioni, firme, ricevute, termini, integrazioni, prescrizioni, issue e stato screened, conditional, filed, authority_review o blocked. Non presentare il record come deposito efficace o autorizzazione.

## Quality gates

- Zona sismica, categoria dell'intervento, ufficio e procedura locale sono documentati e aggiornati.
- Progetto strutturale, architettonico, geotecnico, sismico e titolo edilizio sono coerenti per revisione.
- Professionisti, competenze, firme, asseverazioni e deleghe sono identificati senza fabbricare attestazioni.
- File, calcoli, tavole, materiali, modelli e ricevute sono versionati e recuperabili.
- La pratica distingue preavviso, deposito, autorizzazione, integrazione, collaudo e chiusura.
- Nessuna costruzione, variante o dichiarazione di conformità è autorizzata dal solo controllo documentale.

## Evidenza e provenienza

Conserva classificazione e fonte territoriale, titolo, progetto, relazione, calcoli, modello, relazioni geologica/geotecnica, nomine, firme, deleghe, ricevute, protocollo, richieste, integrazioni, verbali, prove materiali, collaudo e as-built. Marca documento firmato, copia, estrazione, calcolo, assunzione e dato da confermare. Proteggi elaborati strutturali, dati dei proprietari e credenziali del portale; non usare account o firme di altri.

## Fonti ufficiali e diritti

- [Normattiva - D.P.R. 6 giugno 2001, n. 380, art. 93](https://www.normattiva.it/uri-res/N2Ls?urn%3Anir%3Astato%3Adecreto.presidente.repubblica%3A2001%3B380~art93%21vig=): preavviso, deposito del progetto e asseverazione in zona sismica, da verificare in testo vigente e attuazione regionale.
- [Normattiva - D.P.R. 380/2001, art. 94-bis](https://www.normattiva.it/uri-res/N2Ls?urn%3Anir%3Astato%3Adecreto.del.presidente.della.repubblica%3A2001-06-06%3B380~art94bis=): categorie degli interventi strutturali e relativo regime.
- [Gazzetta Ufficiale - D.M. 17 gennaio 2018, NTC](https://www.gazzettaufficiale.it/eli/id/2018/02/20/18A00716/sg): Norme tecniche per le costruzioni; usare testo e circolari nella versione applicabile.
- [MIT - circolare esplicativa NTC](https://mit.gov.it/node/9701): riferimento istituzionale per l'applicazione delle NTC, senza riprodurne il testo.

La procedura, la matrice documentale e i gate sono originali. Diritti: `official_public_legal_text_verify_current_consolidation` per norme pubbliche e `official_reference_only_no_text_reproduced` per pagine/guide; standard, calcoli, modelli, software, tavole e documenti di progetto restano soggetti a licenza e riservatezza.

## Confini professionali e legali

La skill non calcola la sicurezza, non classifica in via definitiva l'intervento, non assevera, non firma, non deposita e non autorizza lavori o varianti. Non sostituisce ingegnere/architetto/geologo abilitato, progettista, direttore lavori, collaudatore, ufficio tecnico regionale, Genio Civile, impresa o autorità. Una ricevuta telematica non prova approvazione tecnica né sicurezza strutturale.

## Failure modes

- **Deposito confuso con autorizzazione:** conserva stato, atto, ufficio e condizione distinti.
- **Categoria sismica copiata da pratica vecchia:** verifica comune, data, intervento e regola regionale.
- **Tavole e modello disallineati:** blocca invio e apre issue di coordinamento.
- **Firma del professionista trattata come garanzia automatica:** verifica ruolo e non sostituire l'asseverazione.
- **Integrazione non versionata:** registra richiesta, risposta, file e impatto sulla pratica.
- **As-built non riconciliato:** non chiudere collaudo o documentazione finale dal solo fascicolo iniziale.

## Strumenti

Usa jurisdiction matrix, intervention classifier, document register, revision/hash ledger, model-drawing cross-check, signature/delegation register, portal submission log, integration tracker, conditions register e as-built closure checklist. Automatizza completezza e coerenza; non accedere a portali o inviare pratiche senza autorizzazione.
