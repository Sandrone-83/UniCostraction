---
name: tender-document-bid-no-bid
description: Valuta completezza dei documenti di gara e prepara un gate bid/no-bid con matrice di conformità, capacità, rischio e approvazioni senza presentare offerte o decidere l'aggiudicazione.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: documenti di gara e bid/no-bid
---

# Gestione documenti di gara e bid/no-bid

## Attivazione e input

Attiva questa skill quando un'impresa o un gruppo deve decidere se partecipare a una gara, richiesta d'offerta, invito o procedura negoziata e deve trasformare un pacchetto documentale in un dossier controllato. È distinta da public-procurement-company-contracts, che tratta il ciclo contrattuale generale, e da sustainable-procurement-cam-esg, che tratta criteri CAM/ESG.

Raccogli bando/invito, disciplinare, capitolato, schema di contratto, allegati, chiarimenti, quesiti e addenda, piattaforma e scadenze, requisiti, criteri, importi, categorie, sopralluogo, garanzie, subappalto, CAM, sicurezza, dati di gara, capacità interna, partner, costi di offerta, vincoli di rischio e deleghe. Se il pacchetto non è completo o l'ultima versione non è certa, lo stato è blocked e non si avvia la presentazione.

## Workflow

1. **Gate della ricezione:** acquisisci pacchetto da fonte autorizzata, assegna hash/versione/data/ora e congela l'elenco documenti; registra addenda e chiarimenti successivi.
2. **Gate della leggibilità:** mappa obblighi, formati, firme, lingue, scadenze, criteri, cause di esclusione, requisiti e portale in una compliance matrix con riferimento puntuale.
3. **Gate dell'ammissibilità:** separa requisiti generali, economico-finanziari, tecnico-professionali, SOA/qualificazioni, capacità, conflitti, assicurazioni e dichiarazioni; evidenzia prove mancanti.
4. **Gate dell'esecuzione:** valuta scope, interfacce, programma, sito, risorse, procurement, subappalto, contraddizioni, rischi, liquidità, responsabilità, penali e assunzioni tecniche.
5. **Gate economico:** stima costi di tender, prezzo, contingency, garanzie, oneri, cash flow, capacità disponibile e opportunità strategica; non ottimizzare il punteggio ignorando obblighi.
6. **Gate bid/no-bid:** applica una matrice pesata con soglie rosse, dati mancanti, rischio reputazionale/legale e owner; produci bid, no-bid o bid_conditional con scadenze di chiusura.
7. **Gate di submission readiness:** controlla versioni, moduli, firme, certificati, separazione tecnica/economica, naming, allegati, caricamento di prova e autorizzazione; il submit resta un'azione umana esplicita.

## Output

Produci un tender_readiness_record con identificativo gara, fonte, document register, versioni, deadline, compliance matrix, requisiti, gap, assumptions, risk register, costi di offerta, scoring bid/no-bid, decisione proposta, approvatori e stato screened, conditional, ready_for_authorized_submission o blocked. Conserva anche la motivazione del no-bid e l'elenco dei dati da recuperare.

## Quality gates

- La versione del bando e degli addenda è provata dalla fonte e dal timestamp di ricezione.
- Ogni requisito ha owner, evidenza, scadenza, formato e stato; "non applicabile" è motivato.
- Requisiti di ammissione, criteri di valutazione, esecuzione e condizioni contrattuali sono separati.
- Costo, capacità, programma, rischio e cash flow sono coerenti con la possibilità reale di eseguire.
- Moduli, firme, dichiarazioni, certificati, referenze e autorizzazioni sono verificati senza inventare prove.
- Nessuna offerta, PEC, caricamento o dichiarazione è inviata dal workflow senza autorizzazione esplicita.

## Evidenza e provenienza

Conserva URL/portale, bando, disciplinare, capitolato, contratto, allegati, chiarimenti, addenda, log download, hash, matrice requisiti, calcoli, CV/referenze, certificati, preventivi, approvazioni e screenshot/receipt della piattaforma se autorizzati. Marca fonte ufficiale, documento del cliente, evidenza interna, dichiarazione del partner, assunzione e punto da chiarire. Non copiare testi protetti: estrai obblighi minimi con riferimenti e sintesi originali.

## Fonti ufficiali e diritti

- [Normattiva — D.Lgs. 31 marzo 2023, n. 36](https://www.normattiva.it/atto/caricaDettaglioAtto?atto.codiceRedazionale=23G00044&atto.dataPubblicazioneGazzetta=2023-03-31): quadro vigente da verificare per procedura, bandi, documenti, requisiti, offerte e accesso.
- [ANAC — obblighi di pubblicazione dei contratti pubblici](https://www.anticorruzione.it/-/pubblicazione-dei-dati-relativi-ai-contratti-pubblici-di-lavori-servizi-e-forniture-art.-37-): riferimenti istituzionali a BDNCP, pubblicità e trasparenza.
- [ANAC — Piano Nazionale Anticorruzione](https://www.anticorruzione.it/documents/91439/276705410/Piano%2BNazionale%2BAnticorruzione%2B-%2B2025.pdf/38fd1e25-a3b1-36c2-9e23-0930912df5e8?t=1770197527657): riferimento istituzionale per contesto di prevenzione e documentazione, da usare per l'edizione vigente.
- [AgID — documento informatico](https://www.agid.gov.it/it/piattaforme/sistema-gestione-procedimenti-amministrativi/documento-informatico): principi operativi per documenti e gestione digitale quando pertinenti.

La matrice, i punteggi e il workflow sono originali. Diritti: `official_public_legal_text_verify_current_consolidation` per legge e `official_reference_only_no_text_reproduced` per linee guida/portali; bando, capitolato, modelli, certificati, marchi, prezzi e dati del cliente restano soggetti a licenza, segreto e condizioni di accesso.

## Confini professionali e legali

La skill non decide l'aggiudicazione, non certifica ammissibilità, non firma dichiarazioni, non interpreta in via definitiva il bando, non offre garanzie di vittoria e non invia l'offerta. Non sostituisce legale, RUP, buyer, responsabile gare, commercialista, progettista, organismo di attestazione o soggetto con procura. Un punteggio bid/no-bid supporta una decisione interna, non crea un diritto alla partecipazione.

## Failure modes

- **Addendum non acquisito:** blocca il gate e ricostruisci la versione completa dal portale ufficiale.
- **Requisito trattato come preferenza:** distingue obbligo, criterio, premialità, chiarimento e assunzione.
- **Partner promesso senza prova:** marca gap e richiedi impegno, ruoli, capacità e autorizzazione.
- **Prezzo basso usato per vincere il gate:** riapri costi, cash flow, rischi, penali e capacità.
- **Firma o upload automatico:** arresta prima della submission e richiedi approvatore e conferma finale.
- **Testo del cliente copiato nel corpus:** rimuovi la riproduzione e conserva solo sintesi, metadati e riferimenti autorizzati.

## Strumenti

Usa document register con hash, requirements/compliance matrix, tender Q&A log, gate checklist, bid/no-bid scorecard, risk and assumption register, capacity plan, pricing handoff, submission pack index e approval log. Automatizza confronti di versione e completezza; non manipolare piattaforme di gara o credenziali senza autorizzazione.
