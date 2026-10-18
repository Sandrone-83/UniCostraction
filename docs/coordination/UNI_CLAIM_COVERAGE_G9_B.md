# G9-B — Indice di provenienza e claim coverage

Audit deterministico, metadata-only, costruito dai report G6 e G7-B. Non modifica PDF, XML, schede o contenuti.

## Esito

- Record indicizzati: **33**; record di fonte espliciti: **30**.
- URL presenti: **31**; licenze dichiarate: **29**.
- Record claim-ready: **0**; item remediation coperti: **48**, aperti: **48**.
- Item claim-ready: **0**; residui distinti: **17**.

`evidence_status` copia il `proof_state` G6 senza promozioni. `claim_ready` richiede un’evidenza esplicita `claim_ready=true`; tale evidenza non è presente in G8, quindi nessun record o item è promosso a ready.

## Copertura per stato di evidenza

| evidence_status | record |
| --- | ---: |
| `verified` | 0 |
| `observed_local` | 29 |
| `context_only` | 2 |
| `blocked` | 2 |

## Residui

| Codice | Record | Item remediation |
| --- | ---: | ---: |
| `claim_not_ready` | 33 | 48 |
| `evidence_not_verified` | 33 | 48 |
| `explicit_claim_ready_evidence_missing` | 33 | 48 |
| `g6:blocked_until_missing_metadata_or_evidence_is_supplied` | 2 | 3 |
| `g6:content_or_legal_accuracy_not_checked` | 1 | 0 |
| `g6:context_does_not_prove_source_vigency_or_reuse` | 2 | 3 |
| `g6:current_version_or_vigency_not_checked` | 1 | 0 |
| `g6:exact_url_not_declared` | 2 | 3 |
| `g6:external_url_availability_not_checked` | 29 | 42 |
| `g6:independent_license_clearance_not_checked` | 29 | 42 |
| `g6:license_or_reuse_terms_not_declared` | 4 | 6 |
| `g6:manifest_id_not_declared_lot_id_used_as_reference` | 14 | 42 |
| `g6:manifest_metadata_only_flag_not_declared` | 14 | 42 |
| `license_missing` | 4 | 6 |
| `remediation_open` | 0 | 48 |
| `source_record_missing` | 3 | 4 |
| `url_missing` | 2 | 3 |

## Limiti e confini

- La presenza di URL o licenza è una dichiarazione osservata nei metadati G6, non una verifica esterna o un parere sui diritti.
- `observed_local`, `context_only` e `blocked` restano tali; non vengono trasformati in `verified`.
- I 48 item G7-B sono collegati ai loro record G6, inclusi i gruppi alias, senza deduplicazione e senza chiusura automatica.
- Il report non dimostra accuratezza tecnica, vigenza normativa, completezza dei contenuti o idoneità professionale dei claim.
