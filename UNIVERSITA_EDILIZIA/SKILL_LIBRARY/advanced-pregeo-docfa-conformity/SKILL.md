---
name: advanced-pregeo-docfa-conformity
description: Controlla il ciclo avanzato Pregeo/Docfa e la riconciliazione tra rilievo, atti catastali, stato fisico, titoli edilizi e conformità dichiarabile, senza sostituire tecnico catastale o autorità.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: catasto avanzato Pregeo/Docfa e conformità
---

# Catasto avanzato Pregeo/Docfa e controllo di conformità

## Attivazione e input

Attiva questa skill quando un aggiornamento Catasto Terreni o Fabbricati richiede controllo di rilievo, particelle, sagoma, subalterni, destinazioni, rendita, planimetrie e coerenza con stato legittimo e titoli. È distinta da italian-urban-planning-cadastre-pa, che tratta il flusso generale urbanistico-catastale, e da advanced-real-estate-technical-due-diligence, che tratta la due diligence multi-dominio.

Raccogli incarico, immobile, particelle/subalterni, titoli, visure storiche, estratti di mappa, rilievo e sistema di riferimento, elaborati grafici, stato di fatto, urbanistica, agibilità, intestazioni, diritti, causale, variazione, unità, classamento, rendita, elaborati Pregeo/Docfa, tecnico abilitato, deleghe, firma, SISTER, ricevute e sospensioni. Se identità, rilievo, titolo, causale o finalità sono incerti, lo stato è blocked.

## Workflow

1. **Gate dell'identità:** riconcilia comune, foglio, particella, subalterno, intestatari, indirizzo, coordinate, confini e storia degli atti; separa visura attuale, storica e ipotecaria.
2. **Gate del rilievo:** verifica datum, strumenti, punti fiduciali/controllo, precisione, copertura, restituzione, sagoma, quote e rapporto con mappa e fabbricato; conserva raw e derivati.
3. **Gate Pregeo:** definisci tipo di aggiornamento, schema, libretto, misure, modello censuario, particelle, allegati, firma e ricevuta; segnala elementi che richiedono scelta del professionista.
4. **Gate Docfa:** riconcilia causale, planimetrie, elaborato planimetrico, subalterni, consistenza, categoria, classe, rendita e stato fisico; controlla che la rappresentazione non mascheri difformità.
5. **Gate urbanistico:** confronta catasto, titolo edilizio, stato autorizzato e rilievo; classifica divergenza catastale, edilizia, grafica, anagrafica o sostanziale, senza chiamarla automaticamente conformità.
6. **Gate di presentazione:** controlla abilitazione, delega, file, firma digitale, pagamento, invio, ricevuta, protocollo, esito, sospensione e termini; non confondere accettazione formale con esito definitivo.
7. **Gate di chiusura:** conserva esito, visura aggiornata, mappa, planimetria, ricevute, versioni, correzioni e rapporto delle questioni residue per cliente, notaio, comune o tecnico competente.

## Output

Produci un cadastral_pregeo_docfa_record con identità, rilievo, atti, differenze, causale, pratica, file/versioni, firma, presentazione, esito, conformità distinguendo catastale/urbanistica, issue, owner e stato screened, conditional, ready_for_professional_submission, filed o blocked. Non rilasciare una dichiarazione di conformità dal solo output catastale.

## Quality gates

- Identità, titolarità, particelle, subalterni e fonti storiche sono coerenti.
- Rilievo, mappa, planimetrie, sagoma, confini e sistema di riferimento sono tracciabili.
- Causale e rappresentazione Pregeo/Docfa corrispondono allo stato fisico e all'incarico.
- Catasto, stato autorizzato, titolo edilizio e stato rilevato sono confrontati senza fonderne gli effetti.
- File firmati, delega, tecnico, invio, ricevuta, esito e sospensione sono conservati.
- Nessun risultato catastale viene usato come sanatoria, prova di proprietà, agibilità o conformità edilizia automatica.

## Evidenza e provenienza

Conserva incarico/delega, visure correnti e storiche, estratti di mappa, atti, rilievi raw/processed, libretti, punti di controllo, fotografie, planimetrie, elaborati, modelli censuari, file Pregeo/Docfa, firme, ricevute SISTER, esiti e correzioni. Marca fonte Agenzia, dato del cliente, misurato, derivato, ipotesi e interpretazione. Proteggi dati catastali personali, titoli, coordinate e credenziali; non copiare manuali o modelli proprietari oltre l'uso autorizzato.

## Fonti ufficiali e diritti

- [Agenzia delle Entrate - assistenza servizi catastali e ipotecari](https://assistenzaipocat.agenziaentrate.gov.it/): servizi ufficiali per consultazione e presentazione di Pregeo/Docfa, inclusi stati pratica.
- [Agenzia delle Entrate - presentazione documenti catastali](https://assistenzaipocat.agenziaentrate.gov.it/Knowledgebases/New_Sister_TP/attach/4.2_Presentazione_doc_catastali.pdf): guida istituzionale al flusso SISTER e alla trasmissione dei documenti.
- [Agenzia delle Entrate - Risoluzione 20/E e Pregeo](https://www.agenziaentrate.gov.it/portale/documents/20143/6021699/Risoluzione_nuova_versione_Pregeo_accessibile.pdf): riferimento ufficiale da verificare nella versione applicabile.
- [Normattiva - D.P.R. 380/2001](https://www.normattiva.it/atto/caricaDettaglioAtto?atto.articolo.numero=0&atto.codiceRedazionale=001G0429&atto.dataPubblicazioneGazzetta=2001-10-20): raccordo con titoli edilizi e stato legittimo, senza confondere i registri.

La procedura, le matrici e i controlli sono originali. Diritti: `official_reference_only_no_text_reproduced` per servizi e guide dell'Agenzia, `official_public_legal_text_verify_current_consolidation` per norme; visure, mappe, fotografie, dati del cliente, software, manuali e file tecnici restano soggetti a licenza, privacy e accesso.

## Confini professionali e legali

La skill non determina proprietà, stato legittimo, sanatoria, agibilità, rendita definitiva o conformità edilizia, non firma, non presenta e non corregge pratiche per conto del tecnico. Non sostituisce geometra/ingegnere/architetto abilitato, topografo, notaio, comune, Agenzia delle Entrate o legale. Una visura o planimetria catastale non prova da sola la conformità urbanistica o la legittimità dell'opera.

## Failure modes

- **Catasto scambiato per urbanistica:** apri confronto tra titolo, stato autorizzato e rilievo.
- **Pregeo senza controllo rilievo:** blocca e richiedi datum, punti, precisione, raw e metodo.
- **Docfa usato per sanare una difformità:** separa rappresentazione, causale e procedimento edilizio.
- **Subalterno copiato da visura vecchia:** verifica storia, intestazione, stato e fonte.
- **Ricevuta SISTER chiamata conformità:** registra il solo stato di trasmissione o esito disponibile.
- **Firma o credenziali del professionista usate da altri:** arresta e instrada a delega e tecnico autorizzato.

## Strumenti

Usa identity/property register, historical document chain, survey control report, GIS/CAD overlay, Pregeo/Docfa checklist, subaltern matrix, urban-cadastral discrepancy log, SISTER submission log e evidence package. Automatizza confronti geometrici e completezza; non inviare file o usare credenziali in autonomia.
