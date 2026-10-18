# G14-B — coda di evidenza per i pack senza source record

La coda machine-readable è [UNI_PACK_EVIDENCE_QUEUE_G14_B.json](./UNI_PACK_EVIDENCE_QUEUE_G14_B.json), con schema [UNI_PACK_EVIDENCE_QUEUE_G14_B_SCHEMA.json](./UNI_PACK_EVIDENCE_QUEUE_G14_B_SCHEMA.json). È generata dal report G13-B presente nel commit `7bdaa0a33260fb5380f02f0a8b41ec6e625a1b44` e include esattamente i 70 pack per i quali `matched_source_records` è vuoto.

## Stato della coda

Tutti i 70 item sono `blocked`. Per ogni pack la coda registra separatamente:

- `source`: source record esplicito, evidenza, locator e prova di licenza source-specific;
- `interpretation`: interpretazione, claim e mapping claim→source da sottoporre a revisione umana;
- `context`: territorio, versione, vigenza e contesto ufficiale;
- `legal_clearance`: revisione indipendente per l’esatto ambito di conservazione/riuso.

Questi livelli non si sostituiscono a vicenda. Un contesto ufficiale non è una licenza; un locator non è prova di accuratezza; un source record non è clearance legale; un titolo o una somiglianza non sono una relazione di provenienza.

## Blocco e divieto di mapping

Il motivo comune di blocco è l’assenza, nel perimetro G13-B, di un source record esplicitamente collegato al pack tramite metadata di manifest o percorso locale. Restano quindi non provati l’evidence, il locator, la licenza source-specific e la clearance legale.

È vietato il mapping semantico automatico basato su `COURSE.yaml fonti`, nome del corso, titoli, argomenti, lessico, similarità testuale o corrispondenza presunta della materia. La coda non copia payload e non modifica fonti, schede, esami o contenuti.

## Criteri di chiusura

Un item può uscire dalla coda solo quando sono presenti e verificabili: source record esplicito; evidenza identificabile e riproducibile; locator esatto con versione/territorio; prova di licenza specifica; interpretazione separata e revisionata da una persona; contesto separato; clearance legale indipendente oppure classificazione esplicita reference-only. Dopo la registrazione, G13-B/G14-B deve essere rigenerato e il pack non deve più risultare privo di source record esplicito.

La chiusura non autorizza da sola accuratezza educativa, vigenza normativa, riuso commerciale o pubblicazione. Il report è metadata-only e non esegue richieste live né fornisce un parere legale.

## Riproducibilità

```text
python tools/build_pack_evidence_queue_g14_b.py
python -m unittest tests/test_g14_b_pack_evidence_queue.py
```
