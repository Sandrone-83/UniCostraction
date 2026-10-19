---
name: special-waste-fir-rentri-management
description: "Tracciabilita operativa e documentale dei rifiuti speciali, dalla classificazione assistita del produttore alla gestione FIR, registro e RENTRI con riconciliazione delle movimentazioni."
metadata:
  library: "UNIVERSITA_EDILIZIA/SKILL_LIBRARY"
  version: "G31.1"
  domain: "rifiuti speciali, FIR e RENTRI"
---

# Rifiuti speciali, FIR e RENTRI

Questa skill presidia la catena documentale del rifiuto speciale: chi lo produce, come e stato caratterizzato, chi lo trasporta, dove va, quali documenti accompagnano il viaggio e come i dati vengono riconciliati con registro e RENTRI. E' distinta dalla skill sui materiali di scavo e gestione fisica dei rifiuti di cantiere: qui il centro e la tracciabilita amministrativa e digitale.

## Attivazione e input

Attivare per apertura o controllo di una posizione rifiuti, emissione/verifica FIR, registri di carico e scarico, iscrizione o adempimenti RENTRI, audit di trasportatore/destinatario e riconciliazione mensile. Richiedere:

- produttore/detentore, unita locale, attivita e quantitativi, codice EER proposto e caratteristiche di pericolo supportate;
- area di deposito temporaneo, date di produzione e movimentazione, contenitori, pesatura e documenti di analisi;
- trasportatore, iscrizione Albo e autorizzazioni, destinatario, impianto, operazione R/D e validita dei titoli;
- ruolo RENTRI, obbligo o esclusione, formato FIR, registro utilizzato, soggetti delegati e interoperabilita;
- contratti, deleghe, ricevute, esiti di accettazione, ritorno della quarta copia o equivalente digitale e non conformita aperte.

Se il codice EER, la pericolosita o il soggetto destinatario sono solo ipotesi, lo stato e `classification_pending`.

## Workflow

1. Disegnare la catena di responsabilita: produttore/detentore, intermediario, trasportatore, destinatario e delegato. Per ogni ruolo registrare titolo, scadenza, area geografica e verifica eseguita.
2. Raccogliere processo di origine, codice EER, analisi e caratteristiche di pericolo. Applicare la gerarchia delle evidenze e chiedere al responsabile ambientale la decisione finale, senza dedurre il codice dal solo nome commerciale.
3. Verificare deposito temporaneo, separazione dei flussi, contenitori, etichette, quantita e date. Questa skill non autorizza un deposito: segnala i dati mancanti e rinvia al titolare.
4. Controllare trasportatore, targa, autorizzazioni, destinatario e operazione prevista prima di emettere il FIR. Bloccare se il percorso o il titolo non sono coerenti con il rifiuto.
5. Compilare il FIR nel formato e con il canale vigente alla data: cartaceo, vidimato o digitale/xFIR secondo soggetto, rifiuto e fase RENTRI. Conservare copia immutabile dei dati inviati e delle firme.
6. Registrare carico, scarico, quantita, date, estremi FIR, esito dell'impianto e difformita. Riconciliare peso prodotto, peso trasportato, peso accettato e residui, con tolleranza motivata.
7. Trasmettere o rendere disponibili i dati RENTRI secondo calendario e ruolo, verificando ricevute, errori e rettifiche. Non duplicare un dato per risolvere un errore di sincronizzazione: aprire un evento di correzione.
8. Chiudere il fascicolo solo con evidenza di accettazione, scadenze di conservazione, audit trail e approvazione del responsabile. Segnalare a consulente/ente eventuali violazioni o dubbi di classificazione.

## Output

Produrre un `waste_traceability_record` con `classification_pending`, `ready_for_shipment`, `fir_issued`, `rentri_reconciled`, `closed` o `blocked`; anagrafica ruoli; matrice EER-evidenza; registro autorizzazioni e scadenze; FIR e formato; movimenti e pesi; ricevute RENTRI; eccezioni, rettifiche, responsabili e date di conservazione.

## Quality gates

- **Classificazione**: origine, EER, pericolosita e analisi sono motivati e datati.
- **Ruoli**: produttore, trasportatore, destinatario e intermediario sono identificati e autorizzati.
- **Movimento**: quantita, targa, percorso, contenitore, data e impianto coincidono tra documenti.
- **FIR**: modello, vidimazione, firma, formato e tempi sono quelli applicabili alla data.
- **RENTRI**: obbligo, iscrizione, registro, trasmissione e ricevuta sono verificati separatamente.
- **Riconciliazione**: differenze peso e rifiuto accettato hanno spiegazione e approvazione.
- **Conservazione**: documento originale, rettifica e audit trail sono recuperabili.
- **Escalation**: ogni dubbio legale o ambientale blocca l'automatismo e va a responsabile competente.

## Evidenza e provenienza

Conservare origine del rifiuto, schede di processo, analisi, fotografie dei contenitori, pesate, autorizzazioni con estremi e scadenze, FIR, registri, ricevute, log API e correzioni. Registrare autore, data, sistema, versione del modello e hash dei file. Un numero FIR dimostra un documento emesso o verificabile, non la correttezza sostanziale del codice EER o dell'operazione di recupero/smaltimento.

## Fonti ufficiali e diritti

I contenuti della skill sono originali e sintetici: rispettare copyright, licenze, termini d'uso dei portali e diritti sugli asset; non redistribuire testi o allegati protetti.

- [D.Lgs. 152/2006 su Normattiva](https://www.normattiva.it/eli/id/2006/04/14/006G0171/CONSOLIDATED/20220511): Parte quarta e artt. 188-bis, 189, 190, 193; `official_public_legal_text_verify_current_consolidation`.
- [Regolamento RENTRI e D.M. 59/2023](https://www.rentri.gov.it/normative/regolamento-rentri): registri, FIR, iscrizione e trasmissione; `official_reference_only_no_text_reproduced` con verifica degli aggiornamenti.
- [Portale RENTRI](https://www.rentri.gov.it/): servizi, modelli, verifiche e calendario; `official_reference_only_no_text_reproduced`.
- [Supporto RENTRI e FAQ](https://supporto.rentri.gov.it/): istruzioni operative e transizioni di formato; `official_reference_only_no_text_reproduced`.
- [Albo Nazionale Gestori Ambientali](https://www.albonazionalegestoriambientali.it/): verifica iscrizioni e categorie; `official_reference_only_no_text_reproduced`.

I portali e i modelli sono riferimenti ufficiali, non contenuto da redistribuire. Alla data di ogni movimento verificare decreto direttoriale, categoria, calendario, regola regionale e aggiornamenti RENTRI: un manuale locale non prevale sulla fonte vigente.

## Confini professionali e legali

La skill non classifica definitivamente un rifiuto, non certifica analisi, non rilascia autorizzazioni, non abilita un trasportatore, non decide l'operazione R/D e non presenta dati a nome dell'impresa senza delega. Non dichiara conformita ambientale sulla sola completezza del FIR. Responsabile ambientale, produttore/detentore, consulente e autorita mantengono le responsabilita previste dalla legge.

## Failure modes

- Codice EER copiato da una commessa diversa o deciso dal solo nome: riportare a `classification_pending`.
- FIR completo usato come prova di corretto trattamento: verificare destinatario, autorizzazione ed esito.
- Autorizzazione scaduta o categoria Albo incompatibile: bloccare il viaggio.
- Peso FIR diverso da registro/destinatario: aprire riconciliazione e non correggere silenziosamente.
- Cartaceo e digitale duplicati senza regola: identificare il documento prevalente e l'evento di rettifica.
- Calendario RENTRI o xFIR cambiato: versionare la regola con data, soggetto e tipo di rifiuto.
- Deposito o etichettatura fuori perimetro: escalare a responsabile sicurezza/ambiente.

## Strumenti

Usare registro rifiuti o gestionale interoperabile, portale RENTRI, verifica Albo, bilance con audit trail, scanner/OCR solo come precompilazione, repository immutabile, matrice ruoli-scadenze e dashboard di riconciliazione. L'automazione puo rilevare incoerenze, ma non firmare FIR, selezionare EER o inviare rettifiche senza approvazione.
