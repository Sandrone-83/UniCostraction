---
name: landscape-environmental-authorizations
description: Governa screening, fascicolo e stato delle autorizzazioni paesaggistiche e ambientali per interventi edilizi e territoriali, senza sostituire autorità, progettista o valutazione specialistica.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: gestione paesaggistica e autorizzazioni ambientali
---

# Gestione paesaggistica e autorizzazioni ambientali

## Attivazione e input

Attiva questa skill quando un intervento può incidere su vincoli paesaggistici, beni culturali, suolo, acque, aria, habitat o altri procedimenti ambientali e occorre costruire una matrice di assoggettabilità e documenti. È distinta da italian-urban-planning-cadastre-pa, che tratta il titolo edilizio e il catasto, da heritage-conservation-diagnostics, che tratta diagnosi e conservazione del bene, e da current-law-pa-source-gating, che tratta il gate delle fonti.

Raccogli localizzazione, coordinate e particelle, proponente, opere e alternative, stato dei vincoli, piano paesaggistico, destinazione d'uso, fotografie, stato legittimo, suolo/acque/vegetazione, emissioni, cantierizzazione, vincoli culturali, pareri, VAS/VIA/VIncA/AIA/AUA o altri regimi possibili, autorità, modulistica, termini e versioni. Se intervento, vincolo, autorità o regime non sono verificabili, lo stato è blocked.

## Workflow

1. **Gate territoriale:** verifica coordinate, particelle, cartografia ufficiale, vincolo, strumento di piano, area protetta, bene culturale e autorità procedente; separa dato GIS da interpretazione.
2. **Gate dell'opera:** descrivi stato attuale, opere permanenti/temporanee, materiali, scavi, colori, volumi, alberature, scarichi, rumore, polveri e fasi; lega ogni impatto a una fonte.
3. **Gate del regime:** costruisci una matrice escluso, semplificato, ordinario, autorizzazione ambientale, valutazione o procedimento combinato; non dedurre esenzione da una sola categoria generica.
4. **Gate del fascicolo:** prepara elaborati, relazione paesaggistica/ambientale, fotoinserimenti, mappe, alternative, mitigazioni, monitoraggio, dichiarazioni e ricevute richieste dalla modulistica aggiornata.
5. **Gate dell'interfaccia:** assegna proponente, progettista, tecnico ambientale, ente delegato, Soprintendenza, comune, regione, ARPA o altra autorità; registra pareri, integrazioni, sospensioni e termini.
6. **Gate della decisione:** separa proposta, parere, autorizzazione, prescrizione, silenzio, diniego e titolo edilizio; verifica condizioni e durata prima dell'avvio lavori.
7. **Gate di cantiere:** trasferisci prescrizioni a elaborati esecutivi, piano controlli, registro materiali, protezioni, ripristini e as-built; chiudi con evidenza e responsabile.

## Output

Produci un landscape_environmental_authorization_record con sito, vincoli, opera, regime, autorità, document register, fonte/versione, prescrizioni, termini, mitigazioni, monitoraggio, gap, issue e stato screened, conditional, ready_for_authority_review, authorized_with_conditions o blocked. Non presentare la scheda come autorizzazione.

## Quality gates

- Localizzazione, vincoli e piano applicabile derivano da fonte ufficiale datata e sono riconciliati con il rilievo.
- Ogni procedimento ha base, autorità, modulistica, allegati, firme, termine e stato distinti.
- Paesaggio, ambiente, edilizia, sicurezza e patrimonio culturale non sono fusi in un unico via libera.
- Mitigazioni, prescrizioni e monitoraggi sono traducibili in responsabile, frequenza, criterio e prova.
- Le alternative e gli impatti cumulativi sono dichiarati quando pertinenti.
- Nessun lavoro, invio o dichiarazione di esenzione avviene senza revisione e autorizzazione del soggetto competente.

## Evidenza e provenienza

Conserva estratti di piano, mappe, vincoli, visure, rilievi, fotografie datate, modelli, relazione, elaborati, pareri, protocolli, ricevute, integrazioni, prescrizioni, monitoraggi e as-built. Marca fonte ufficiale, dato del proponente, osservazione, calcolo, assunzione e stato da confermare. Non pubblicare coordinate sensibili, immagini di persone o dati ambientali proprietari oltre lo scopo autorizzato.

## Fonti ufficiali e diritti

- [Normattiva - D.Lgs. 22 gennaio 2004, n. 42](https://www.normattiva.it/uri-res/N2Ls?urn%3Anir%3Astato%3A2004%3B42~art146%21vig=): Codice dei beni culturali e del paesaggio, inclusa l'autorizzazione paesaggistica.
- [Normattiva - D.P.R. 13 febbraio 2017, n. 31](https://www.normattiva.it/eli/stato/DECRETO_DEL_PRESIDENTE_DELLA_REPUBBLICA/2017/02/13/31/CONSOLIDATED): interventi esclusi e procedure paesaggistiche semplificate; verificare testo vigente e allegati.
- [Normattiva - D.Lgs. 3 aprile 2006, n. 152](https://www.normattiva.it/eli/id/2006/04/14/006G0171/CONSOLIDATED/20220511): matrici ambientali, autorizzazioni e valutazioni nei casi pertinenti.

La matrice, i record, le checklist e le sintesi sono originali e non riproducono testi protetti. Diritti: `official_public_legal_text_verify_current_consolidation` per norme e `official_reference_only_no_text_reproduced` per portali e atti; cartografie, fotografie, relazioni, modelli e dati di terzi restano soggetti a licenza e condizioni di accesso.

## Confini professionali e legali

La skill non dichiara assoggettabilità definitiva, non rilascia autorizzazioni, pareri o nulla osta, non firma relazioni, non approva mitigazioni e non ordina l'avvio dei lavori. Non sostituisce progettista, paesaggista, agronomo, geologo, biologo, tecnico competente, autorità procedente, Soprintendenza, ARPA o legale. Un vincolo cartografico o una pratica predisposta non prova l'autorizzazione.

## Failure modes

- **Esenzione dichiarata dalla particella:** verifica vincolo, intervento concreto, allegato e autorità.
- **Paesaggistica confusa con edilizia:** mantieni fascicoli, condizioni e titoli separati.
- **Parere scambiato per autorizzazione:** registra natura, efficacia, prescrizioni e atto finale.
- **Fotoinserimento usato come impatto completo:** aggiungi opere temporanee, alternative, suolo, acque e cantiere.
- **Prescrizione non trasferita al cantiere:** crea requisito verificabile, owner, frequenza e prova.
- **Norma o piano superato:** riapri data, consolidamento, regione e modulistica.

## Strumenti

Usa vincoli-GIS register, source/version ledger, regime matrix, document register, photo log, impact/mitigation matrix, authority map, deadline tracker, consultation log, permit conditions register e as-built compliance log. Automatizza confronti e scadenze; non inviare pratiche o dichiarare esenzioni in autonomia.
