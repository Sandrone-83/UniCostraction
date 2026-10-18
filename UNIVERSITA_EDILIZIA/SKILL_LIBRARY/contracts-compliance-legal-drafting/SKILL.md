---
name: contracts-compliance-legal-drafting
description: Prepara bozze controllate, matrici di clausole e registri di compliance per rapporti edilizi, mantenendo fatti, fonti, approvazioni e limiti legali espliciti.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: documenti contrattuali, conformità e controllo giuridico
---

# Contratti, compliance e drafting legale controllato

## Attivazione

Usa la skill per analizzare un contratto, preparare una bozza o revisione, creare una matrice di clausole, organizzare evidenze di compliance, predisporre quesiti, notice, riserve, richieste di chiarimento o emendamenti. L'output è sempre una bozza o uno strumento di controllo finché il professionista o il ruolo autorizzato non approva.

## Input

Richiedi territorio e legge applicabile, tipo di rapporto, ruolo dell'utente, parti e poteri, oggetto, documenti contrattuali, versione, date, scadenze, importi, fatti provati, risultato desiderato, destinatario e canale autorizzato. Acquisisci contratto, allegati, capitolato, ordine, verbali, corrispondenza e policy interne; separa fatto, dichiarazione della parte, interpretazione e ipotesi.

## Workflow

1. Identifica giurisdizione, fonte applicabile, gerarchia dei documenti, lingua prevalente, termini definiti e autorità che può approvare.
2. Congela fascicolo, versione e data; costruisci indice degli allegati con hash, provenienza, riservatezza e lacune.
3. Crea matrice obbligo/clausola: soggetto, azione, termine, condizione, evidenza, rischio, rimedio, approvatore e stato.
4. Mappa clausole su fatti ed evidenze; segnala conflitti tra corpo, allegati, ordine, capitolato, offerta e modifiche.
5. Prepara una bozza originale con placeholder visibili per dati mancanti, opzioni alternative e note per il legale; non inventare fatti, firme, numeri o riferimenti.
6. Esegui controllo incrociato di definizioni, date, importi, valuta, IVA, responsabilità, assicurazioni, garanzie, privacy, subappalto, proprietà intellettuale, recesso, controversie e allegati pertinenti.
7. Sottoponi a revisione di ruolo, registra commenti e decisioni, congela la versione approvata e prepara il pacchetto per firma o invio solo dopo autorizzazione separata.

## Output

Consegna matrice obblighi e scadenze, registro fonti/versioni, bozza con stato e placeholder, redline o changelog, lista rischi e conflitti, domande al professionista, pacchetto evidenze, registro approvazioni e checklist di firma/invio. Indica esplicitamente cosa è verificato, non verificato, contestato o da negoziare.

## Quality gates

- Legge applicabile, territorio, versione, parti, poteri, date e allegati sono confermati o marcati mancanti.
- Ogni obbligo ha soggetto, trigger, termine, prova, responsabile e conseguenza da verificare.
- Definizioni, numerazione, rinvii, importi, unità, valuta e versioni degli allegati sono coerenti.
- Fatti e citazioni normative non sono inventati; la bozza non maschera placeholder o assunzioni.
- Firma, PEC, portale, registrazione, privacy e conservazione sono trattati secondo ruolo e autorizzazione; nessun invio automatico.

## Provenienza ed evidenza

Conserva originali in sola lettura, hash, timestamp, fonte, canale di ricezione, permessi, versioni, commenti, approvazioni, log di confronto e copie dell'output. Non cancellare una versione firmata o alterare metadata probatori. Una bozza ben formattata non prova validità, autenticità, consenso o opponibilità.

## Controllo versione, territorio e data

Verifica alla data dell'atto la legge applicabile, il testo consolidato, la giurisprudenza o prassi che il legale richiede, i poteri di firma, la sede delle parti, il luogo di esecuzione, la lingua, le soglie e le regole di piattaforma. Per appalti pubblici controlla versione del bando e Codice vigente; per firma digitale controlla territorio, formato e validità del certificato. Una clausola valida in un ordinamento non è automaticamente valida in un altro.

## Confini professionali e legali

La skill non offre consulenza legale, rappresentanza, parere vincolante, interpretazione definitiva, asseverazione, autenticazione, firma, notifica o invio. Non decide ammissibilità, responsabilità, sanzioni, contenzioso, rinunce o transazioni. Invia il fascicolo a avvocato, notaio, RUP, organo societario o altro professionista competente secondo il ruolo e non condividere dati riservati senza base autorizzativa.

## Failure modes

- **Legge o versione sbagliata:** arresta la bozza e congela la fonte ufficiale corretta.
- **Allegato mancante:** non colmare il vuoto; registra impatto e richiesta formale.
- **Rinvio incoerente:** esegui controllo dei termini definiti e dei numeri di clausola.
- **Bozza scambiata per impegno:** apponi stato, revisione, destinatario e blocco di invio finché manca approvazione.
- **Dati personali o segreti esposti:** minimizza, limita accessi e richiedi canale autorizzato.

## Strumenti

Usa confronto documentale, redline, estrazione controllata, matrice in foglio protetto, repository con permessi, checksum, firma/verifica digitale e registro scadenze. Un modello linguistico può proporre struttura e domande, ma non può autenticare, firmare, notificare o assumere impegni.

## Fonti ufficiali e diritti

- [Normattiva — D.Lgs. 36/2023](https://www.normattiva.it/uri-res/N2Ls?urn%3Anir%3Astato%3Adecreto.legge%3A2023-03-31%3B36%21vig=): `rights_state: official_public_legal_text_verify_current_consolidation`; riferimento pubblico per contratti pubblici; verificare testo vigente e ambito.
- [Normattiva — Codice civile](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262!vig=): `rights_state: official_public_legal_text_verify_current_consolidation`; riferimento legislativo pubblico per obbligazioni e contratti; applicazione da valutare nel caso.
- [EUR-Lex — Regolamento (UE) n. 910/2014](https://eur-lex.europa.eu/eli/reg/2014/910/oj): `rights_state: official_public_legal_text_verify_current_consolidation`; fonte europea su identità e servizi fiduciari; verificare versione, territorio e condizioni tecniche.

La skill contiene sintesi originali e non riproduce clausole di terzi. Contratti, formulari, policy, banche dati normative, firme e documenti delle parti restano soggetti a diritti, segreti, licenze e autorizzazioni.
