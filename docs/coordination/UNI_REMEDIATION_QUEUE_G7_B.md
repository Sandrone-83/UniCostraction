# G7-B — coda di remediation della provenienza

## Scopo

`UNI_REMEDIATION_QUEUE_G7_B.json` è una coda machine-readable derivata esclusivamente da `UNI_PROVENANCE_AUDIT_G6.json`. È un registro di lavoro metadata-only: non promuove stati di prova, non decide licenze, non inventa URL o identificativi e non modifica fonti, PDF, XML, schede o contenuti didattici.

Il generatore è `tools/build_remediation_queue_g7.py`. Il report può essere rigenerato con:

```powershell
python tools/build_remediation_queue_g7.py --write
```

## Perimetro osservato

La coda contiene 48 item aperti, con sovrapposizioni intenzionali quando uno stesso record presenta più lacune indipendenti:

| Categoria | Item | Riferimento G6 |
| --- | ---: | --- |
| `missing_manifest_id` | 14 | `manifest_id_not_declared_lot_id_used_as_reference` sui record G1 del lotto |
| `missing_metadata_only` | 14 | `manifest_metadata_only_flag_not_declared` sui record G1 del lotto |
| `license_missing` | 4 | `license_or_reuse_terms_not_declared` |
| `g3_pdf_blocked` | 1 | PDF G3 con `proof_state=blocked` |
| `gse_context_only` | 1 | record GSE con `proof_state=context_only` |
| `alias_not_deduplicated` | 14 | `cross_manifest_alias_review_required` |

Il PDF G3 compare sia nella categoria del blocco sia in quella della licenza mancante: sono due prove di chiusura diverse e non vanno fuse. Il record GSE di contesto non viene usato per chiudere il blocco del PDF.

Sono fuori dal perimetro di questa coda, e quindi non sono implicitamente chiusi, i residui G6 relativi a disponibilità URL esterna, clearance indipendente per licenze dichiarate, vigenza/versione corrente e accuratezza contenutistica o legale.

## Contratto di stato e checklist

Ogni item ha uno `status` tra `open` e `resolved`, un `source_ref` riconducibile a un `record_key` G6 oppure a un hash di alias G6, i codici osservati, criteri di chiusura e vincoli. Un item `resolved` deve avere un `evidence_ref` non vuoto; la transizione `open -> resolved` è rifiutata dal validatore se il riferimento manca. Un item `open` mantiene `evidence_ref=null` e la relativa checklist in `pending`.

`closure_checklist` è un artefatto machine-readable generato per ogni item: contiene un controllo per ciascun criterio, il tipo di controllo, lo stato e l'eventuale `evidence_ref`. La checklist non chiude alcun item per inferenza: nella coda G7-B tutti i controlli restano `pending`.

`closure_evidence` resta vuoto finché una verifica successiva non produce evidenza esplicita. La coda non contiene payload protetti (`text`, `content`, domande, risposte o soluzioni).

Gli alias sono riportati ma non deduplicati automaticamente. `representation_count=2` descrive due rappresentazioni nei manifest, non autorizza a cancellare o riscrivere nessun file. Il validatore richiede che ogni item alias abbia controlli distinti per relazione alias e decisione di deduplicazione (`independence.must_be_distinct=true`); il fatto che due file abbiano lo stesso hash non viene trattato come deduplicazione eseguita.

## Criteri di chiusura

Un item può passare da `open` a `resolved` solo in un aggiornamento successivo, con evidenze verificabili e riesecuzione del controllo G6:

- `missing_manifest_id`: il manifest sorgente dichiara esplicitamente `manifest_id`; il valore è approvato dal proprietario del corpus e il nuovo G6 non segnala più il codice residuo.
- `missing_metadata_only`: il manifest sorgente dichiara esplicitamente il booleano `metadata_only`; valore e perimetro sono approvati, senza scegliere automaticamente `true` o `false`.
- `license_missing`: sono registrati termini esatti di licenza o riuso con base tracciabile; quando necessario è presente una revisione indipendente dei diritti; il nuovo G6 non segnala più la lacuna.
- `g3_pdf_blocked`: il locator esatto del PDF locale è registrato e associato al file corretto, i termini di riuso sono documentati, identità e applicabilità sono verificate senza modificare il PDF, e il nuovo G6 non lo mantiene bloccato.
- `gse_context_only`: il record resta marcato `context_only` finché non viene rivalutato; una fonte primaria per il PDF è identificata e valutata separatamente; la pagina GSE non viene trattata come prova di identità, vigenza, licenza o riuso. Il relativo item PDF si chiude con criteri propri.
- `alias_not_deduplicated`: il proprietario registra il record canonico e la relazione alias, riconcilia i riferimenti senza cancellare o riscrivere payload, ricontrolla hash/percorso e il nuovo G6 non segnala più la revisione alias.

La presenza di un’evidenza locale o di una pagina istituzionale non basta da sola a chiudere una lacuna. Per un item alias risolto, i due controlli indipendenti devono inoltre avere `evidence_ref` distinti. Le verifiche legali, di vigenza, accuratezza e correttezza dei contenuti restano distinte da questo artefatto metadata-only.

## Validazione

Il test `tests/test_g7_remediation_queue.py` controlla schema e identità, conteggi, tracciabilità completa a G6, transizioni di stato, obbligo di `evidence_ref`, checklist, indipendenza alias/deduplicazione, confini G1/G3/GSE/alias, assenza di payload e determinismo della generazione. Il file JSON Schema associato è `UNI_REMEDIATION_QUEUE_G7_B_SCHEMA.json`.
