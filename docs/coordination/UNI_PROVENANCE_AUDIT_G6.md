# G6-B — audit deterministico di provenienza

Audit metadata-only dei record/manifests di provenienza già presenti al commit G5.
Non è stata letta o modificata la sostanza di PDF, XML, schede, valori o contenuti d'esame.

## Perimetro e regola di prova

- Manifest inclusi: 33 record normalizzati da 4 manifest.
- `verified` non viene assegnato per inferenza: compare solo se dichiarato esplicitamente in ingresso.
- `observed_local` indica controlli locali già dichiarati dai manifest, non disponibilità URL, licenza corrente o validazione legale indipendente.
- `context_only` non viene trattato come fonte primaria; `blocked` resta bloccato.

## Quadro sintetico

| Dimensione | Esito |
| --- | ---: |
| Record totali | 33 |
| Stato `verified` | 0 |
| Stato `observed_local` | 29 |
| Stato `context_only` | 2 |
| Stato `blocked` | 2 |
| URL dichiarato | 31 |
| URL non dichiarato | 2 |
| Licenza/riuso dichiarato | 29 |
| Licenza/riuso non dichiarato | 4 |

## Copertura dei manifest

| Manifest | ID | Collezioni |
| --- | --- | --- |
| `docs/coordination/UNI_CORPUS_LOTTO_G1.json` | `G1-FONDAMENTI-GUTENBERG-RAW` | `records`=14 |
| `Fondamenti_Pack/PROVENANCE_MANIFEST_G2.json` | `G2-FONDAMENTI-PACK-G1-PROVENANCE` | `records`=14 |
| `UNIVERSITA_EDILIZIA/ENERGETICA_INCENTIVI_PACK/fonti/PROVENANCE_MANIFEST_G3_GSE_CT3.json` | `G3-2-ENERGETICA-GSE-CT3` | `records`=2 |
| `docs/coordination/UNI_CORPUS_LOTTO_G5_ECFR.json` | `G5-ECFR-OSHA-1926` | `source_records`=1, `official_context_records`=1, `related_blockers`=1 |

## Record auditati

| Record | Manifest | Stato | URL | Licenza/riuso | Residui |
| --- | --- | --- | --- | --- | ---: |
| `G1-001` | `G2-FONDAMENTI-PACK-G1-PROVENANCE` | `observed_local` | declared | declared | 8 |
| `G1-002` | `G2-FONDAMENTI-PACK-G1-PROVENANCE` | `observed_local` | declared | declared | 8 |
| `G1-003` | `G2-FONDAMENTI-PACK-G1-PROVENANCE` | `observed_local` | declared | declared | 8 |
| `G1-004` | `G2-FONDAMENTI-PACK-G1-PROVENANCE` | `observed_local` | declared | declared | 8 |
| `G1-005` | `G2-FONDAMENTI-PACK-G1-PROVENANCE` | `observed_local` | declared | declared | 8 |
| `G1-006` | `G2-FONDAMENTI-PACK-G1-PROVENANCE` | `observed_local` | declared | declared | 8 |
| `G1-007` | `G2-FONDAMENTI-PACK-G1-PROVENANCE` | `observed_local` | declared | declared | 8 |
| `G1-008` | `G2-FONDAMENTI-PACK-G1-PROVENANCE` | `observed_local` | declared | declared | 8 |
| `G1-009` | `G2-FONDAMENTI-PACK-G1-PROVENANCE` | `observed_local` | declared | declared | 8 |
| `G1-010` | `G2-FONDAMENTI-PACK-G1-PROVENANCE` | `observed_local` | declared | declared | 8 |
| `G1-011` | `G2-FONDAMENTI-PACK-G1-PROVENANCE` | `observed_local` | declared | declared | 8 |
| `G1-012` | `G2-FONDAMENTI-PACK-G1-PROVENANCE` | `observed_local` | declared | declared | 8 |
| `G1-013` | `G2-FONDAMENTI-PACK-G1-PROVENANCE` | `observed_local` | declared | declared | 8 |
| `G1-014` | `G2-FONDAMENTI-PACK-G1-PROVENANCE` | `observed_local` | declared | declared | 8 |
| `G3-2-001` | `G3-2-ENERGETICA-GSE-CT3` | `blocked` | not_declared | not_declared | 13 |
| `G3-2-002` | `G3-2-ENERGETICA-GSE-CT3` | `context_only` | declared | not_declared | 12 |
| `G1-001` | `G1-FONDAMENTI-GUTENBERG-RAW` | `observed_local` | declared | declared | 10 |
| `G1-002` | `G1-FONDAMENTI-GUTENBERG-RAW` | `observed_local` | declared | declared | 10 |
| `G1-003` | `G1-FONDAMENTI-GUTENBERG-RAW` | `observed_local` | declared | declared | 10 |
| `G1-004` | `G1-FONDAMENTI-GUTENBERG-RAW` | `observed_local` | declared | declared | 10 |
| `G1-005` | `G1-FONDAMENTI-GUTENBERG-RAW` | `observed_local` | declared | declared | 10 |
| `G1-006` | `G1-FONDAMENTI-GUTENBERG-RAW` | `observed_local` | declared | declared | 10 |
| `G1-007` | `G1-FONDAMENTI-GUTENBERG-RAW` | `observed_local` | declared | declared | 10 |
| `G1-008` | `G1-FONDAMENTI-GUTENBERG-RAW` | `observed_local` | declared | declared | 10 |
| `G1-009` | `G1-FONDAMENTI-GUTENBERG-RAW` | `observed_local` | declared | declared | 10 |
| `G1-010` | `G1-FONDAMENTI-GUTENBERG-RAW` | `observed_local` | declared | declared | 10 |
| `G1-011` | `G1-FONDAMENTI-GUTENBERG-RAW` | `observed_local` | declared | declared | 10 |
| `G1-012` | `G1-FONDAMENTI-GUTENBERG-RAW` | `observed_local` | declared | declared | 10 |
| `G1-013` | `G1-FONDAMENTI-GUTENBERG-RAW` | `observed_local` | declared | declared | 10 |
| `G1-014` | `G1-FONDAMENTI-GUTENBERG-RAW` | `observed_local` | declared | declared | 10 |
| `BLOCKER-001` | `G5-ECFR-OSHA-1926` | `blocked` | not_declared | not_declared | 7 |
| `G5-001` | `G5-ECFR-OSHA-1926` | `observed_local` | declared | declared | 12 |
| `G5-CONTEXT-001` | `G5-ECFR-OSHA-1926` | `context_only` | declared | not_declared | 2 |

## Residui visibili

### `Fondamenti_Pack/PROVENANCE_MANIFEST_G2.json#G1-001`
- Codici: `external_url_availability_not_checked`, `independent_license_clearance_not_checked`
- not_checked:external_url_availability
- not_checked:current_license_terms
- not_checked:independent_legal_public_domain_status
- limitation:La licenza è riportata come dichiarazione osservata nei file locali e non come parere giuridico indipendente.
- limitation:Il record non contiene il testo della fonte né una validazione di accuratezza o completezza.
- limitation:L'anno è il metadato locale della pubblicazione/opera, non una revisione del file raw.

### `Fondamenti_Pack/PROVENANCE_MANIFEST_G2.json#G1-002`
- Codici: `external_url_availability_not_checked`, `independent_license_clearance_not_checked`
- not_checked:external_url_availability
- not_checked:current_license_terms
- not_checked:independent_legal_public_domain_status
- limitation:La licenza è riportata come dichiarazione osservata nei file locali e non come parere giuridico indipendente.
- limitation:Il record non contiene il testo della fonte né una validazione di accuratezza o completezza.
- limitation:L'anno è il metadato locale della pubblicazione/opera, non una revisione del file raw.

### `Fondamenti_Pack/PROVENANCE_MANIFEST_G2.json#G1-003`
- Codici: `external_url_availability_not_checked`, `independent_license_clearance_not_checked`
- not_checked:external_url_availability
- not_checked:current_license_terms
- not_checked:independent_legal_public_domain_status
- limitation:La licenza è riportata come dichiarazione osservata nei file locali e non come parere giuridico indipendente.
- limitation:Il record non contiene il testo della fonte né una validazione di accuratezza o completezza.
- limitation:L'anno è il metadato locale della pubblicazione/opera, non una revisione del file raw.

### `Fondamenti_Pack/PROVENANCE_MANIFEST_G2.json#G1-004`
- Codici: `external_url_availability_not_checked`, `independent_license_clearance_not_checked`
- not_checked:external_url_availability
- not_checked:current_license_terms
- not_checked:independent_legal_public_domain_status
- limitation:La licenza è riportata come dichiarazione osservata nei file locali e non come parere giuridico indipendente.
- limitation:Il record non contiene il testo della fonte né una validazione di accuratezza o completezza.
- limitation:L'anno è il metadato locale della pubblicazione/opera, non una revisione del file raw.

### `Fondamenti_Pack/PROVENANCE_MANIFEST_G2.json#G1-005`
- Codici: `external_url_availability_not_checked`, `independent_license_clearance_not_checked`
- not_checked:external_url_availability
- not_checked:current_license_terms
- not_checked:independent_legal_public_domain_status
- limitation:La licenza è riportata come dichiarazione osservata nei file locali e non come parere giuridico indipendente.
- limitation:Il record non contiene il testo della fonte né una validazione di accuratezza o completezza.
- limitation:L'anno è il metadato locale della pubblicazione/opera, non una revisione del file raw.

### `Fondamenti_Pack/PROVENANCE_MANIFEST_G2.json#G1-006`
- Codici: `external_url_availability_not_checked`, `independent_license_clearance_not_checked`
- not_checked:external_url_availability
- not_checked:current_license_terms
- not_checked:independent_legal_public_domain_status
- limitation:La licenza è riportata come dichiarazione osservata nei file locali e non come parere giuridico indipendente.
- limitation:Il record non contiene il testo della fonte né una validazione di accuratezza o completezza.
- limitation:L'anno è il metadato locale della pubblicazione/opera, non una revisione del file raw.

### `Fondamenti_Pack/PROVENANCE_MANIFEST_G2.json#G1-007`
- Codici: `external_url_availability_not_checked`, `independent_license_clearance_not_checked`
- not_checked:external_url_availability
- not_checked:current_license_terms
- not_checked:independent_legal_public_domain_status
- limitation:La licenza è riportata come dichiarazione osservata nei file locali e non come parere giuridico indipendente.
- limitation:Il record non contiene il testo della fonte né una validazione di accuratezza o completezza.
- limitation:L'anno è il metadato locale della pubblicazione/opera, non una revisione del file raw.

### `Fondamenti_Pack/PROVENANCE_MANIFEST_G2.json#G1-008`
- Codici: `external_url_availability_not_checked`, `independent_license_clearance_not_checked`
- not_checked:external_url_availability
- not_checked:current_license_terms
- not_checked:independent_legal_public_domain_status
- limitation:La licenza è riportata come dichiarazione osservata nei file locali e non come parere giuridico indipendente.
- limitation:Il record non contiene il testo della fonte né una validazione di accuratezza o completezza.
- limitation:L'anno è il metadato locale della pubblicazione/opera, non una revisione del file raw.

### `Fondamenti_Pack/PROVENANCE_MANIFEST_G2.json#G1-009`
- Codici: `external_url_availability_not_checked`, `independent_license_clearance_not_checked`
- not_checked:external_url_availability
- not_checked:current_license_terms
- not_checked:independent_legal_public_domain_status
- limitation:La licenza è riportata come dichiarazione osservata nei file locali e non come parere giuridico indipendente.
- limitation:Il record non contiene il testo della fonte né una validazione di accuratezza o completezza.
- limitation:L'anno è il metadato locale della pubblicazione/opera, non una revisione del file raw.

### `Fondamenti_Pack/PROVENANCE_MANIFEST_G2.json#G1-010`
- Codici: `external_url_availability_not_checked`, `independent_license_clearance_not_checked`
- not_checked:external_url_availability
- not_checked:current_license_terms
- not_checked:independent_legal_public_domain_status
- limitation:La licenza è riportata come dichiarazione osservata nei file locali e non come parere giuridico indipendente.
- limitation:Il record non contiene il testo della fonte né una validazione di accuratezza o completezza.
- limitation:L'anno è il metadato locale della pubblicazione/opera, non una revisione del file raw.

### `Fondamenti_Pack/PROVENANCE_MANIFEST_G2.json#G1-011`
- Codici: `external_url_availability_not_checked`, `independent_license_clearance_not_checked`
- not_checked:external_url_availability
- not_checked:current_license_terms
- not_checked:independent_legal_public_domain_status
- limitation:La licenza è riportata come dichiarazione osservata nei file locali e non come parere giuridico indipendente.
- limitation:Il record non contiene il testo della fonte né una validazione di accuratezza o completezza.
- limitation:L'anno è il metadato locale della pubblicazione/opera, non una revisione del file raw.

### `Fondamenti_Pack/PROVENANCE_MANIFEST_G2.json#G1-012`
- Codici: `external_url_availability_not_checked`, `independent_license_clearance_not_checked`
- not_checked:external_url_availability
- not_checked:current_license_terms
- not_checked:independent_legal_public_domain_status
- limitation:La licenza è riportata come dichiarazione osservata nei file locali e non come parere giuridico indipendente.
- limitation:Il record non contiene il testo della fonte né una validazione di accuratezza o completezza.
- limitation:L'anno è il metadato locale della pubblicazione/opera, non una revisione del file raw.

### `Fondamenti_Pack/PROVENANCE_MANIFEST_G2.json#G1-013`
- Codici: `external_url_availability_not_checked`, `independent_license_clearance_not_checked`
- not_checked:external_url_availability
- not_checked:current_license_terms
- not_checked:independent_legal_public_domain_status
- limitation:La licenza è riportata come dichiarazione osservata nei file locali e non come parere giuridico indipendente.
- limitation:Il record non contiene il testo della fonte né una validazione di accuratezza o completezza.
- limitation:L'anno è il metadato locale della pubblicazione/opera, non una revisione del file raw.

### `Fondamenti_Pack/PROVENANCE_MANIFEST_G2.json#G1-014`
- Codici: `external_url_availability_not_checked`, `independent_license_clearance_not_checked`
- not_checked:external_url_availability
- not_checked:current_license_terms
- not_checked:independent_legal_public_domain_status
- limitation:La licenza è riportata come dichiarazione osservata nei file locali e non come parere giuridico indipendente.
- limitation:Il record non contiene il testo della fonte né una validazione di accuratezza o completezza.
- limitation:L'anno è il metadato locale della pubblicazione/opera, non una revisione del file raw.

### `UNIVERSITA_EDILIZIA/ENERGETICA_INCENTIVI_PACK/fonti/PROVENANCE_MANIFEST_G3_GSE_CT3.json#G3-2-001`
- Codici: `exact_url_not_declared`, `license_or_reuse_terms_not_declared`, `blocked_until_missing_metadata_or_evidence_is_supplied`
- not_checked:registered_gse_url_for_this_pdf
- not_checked:external_url_availability
- not_checked:current_validity_or_applicability
- not_checked:independent_license_or_reuse_clearance
- not_checked:legal_validity
- not_checked:accuracy_or_completeness_of_incentive_values
- limitation:Il manifest è bloccato perché nel PDF, nel README locale e nella storia del branch non è stato trovato un URL GSE già registrato per questo specifico PDF; gse.it è citato solo come dominio, non come locator completo.
- limitation:Il PDF è identificato come fonte ufficiale GSE sulla base di copertina, autore PDF e README locale; ciò non dimostra vigenza corrente, validità legale o completezza normativa.
- limitation:Nessuna licenza o autorizzazione di riuso è dichiarata nei metadati locali; la presenza del file nella repository non equivale a permesso di riproduzione o distribuzione.
- limitation:Il record non incorpora testo, tabelle, valori incentivanti o interpretazioni e non valida le schede che lo citano.

### `UNIVERSITA_EDILIZIA/ENERGETICA_INCENTIVI_PACK/fonti/PROVENANCE_MANIFEST_G3_GSE_CT3.json#G3-2-002`
- Codici: `license_or_reuse_terms_not_declared`, `context_does_not_prove_source_vigency_or_reuse`
- not_checked:identity_of_the_local_pdf
- not_checked:registered_gse_url_for_the_local_pdf
- not_checked:current_validity_or_applicability_of_the_pdf
- not_checked:independent_license_or_reuse_clearance
- not_checked:legal_validity
- not_checked:accuracy_or_completeness_of_incentive_values
- limitation:La pagina correlata non è prova dell'URL esatto del PDF locale, della sua vigenza corrente, validità legale o completezza.
- limitation:La pagina correlata non è prova di una licenza o autorizzazione al riuso, riproduzione o distribuzione del PDF.
- limitation:Il record non incorpora testo, tabelle, valori incentivanti o interpretazioni e non cambia lo stato blocked del record G3-2-001.
- context_relation:{"description": "Pagina istituzionale GSE correlata al Conto Termico 3.0 e alla modulistica; non è registrata come locator del PDF locale e non prova la sua vigenza o il suo riuso.", "related_source_record_id": "G3-2-001", "relationship": "institutional_context_only"}

### `docs/coordination/UNI_CORPUS_LOTTO_G1.json#G1-001`
- Codici: `external_url_availability_not_checked`, `independent_license_clearance_not_checked`, `manifest_metadata_only_flag_not_declared`, `manifest_id_not_declared_lot_id_used_as_reference`
- not_checked:external_url_availability
- not_checked:current_license_terms
- not_checked:independent_legal_public_domain_status
- limitation:La licenza è riportata come dichiarazione osservata nei file locali e non come parere giuridico indipendente.
- limitation:Il record non contiene il testo della fonte né una validazione di accuratezza o completezza.
- limitation:L'anno è il metadato locale della pubblicazione/opera, non una revisione del file raw.

### `docs/coordination/UNI_CORPUS_LOTTO_G1.json#G1-002`
- Codici: `external_url_availability_not_checked`, `independent_license_clearance_not_checked`, `manifest_metadata_only_flag_not_declared`, `manifest_id_not_declared_lot_id_used_as_reference`
- not_checked:external_url_availability
- not_checked:current_license_terms
- not_checked:independent_legal_public_domain_status
- limitation:La licenza è riportata come dichiarazione osservata nei file locali e non come parere giuridico indipendente.
- limitation:Il record non contiene il testo della fonte né una validazione di accuratezza o completezza.
- limitation:L'anno è il metadato locale della pubblicazione/opera, non una revisione del file raw.

### `docs/coordination/UNI_CORPUS_LOTTO_G1.json#G1-003`
- Codici: `external_url_availability_not_checked`, `independent_license_clearance_not_checked`, `manifest_metadata_only_flag_not_declared`, `manifest_id_not_declared_lot_id_used_as_reference`
- not_checked:external_url_availability
- not_checked:current_license_terms
- not_checked:independent_legal_public_domain_status
- limitation:La licenza è riportata come dichiarazione osservata nei file locali e non come parere giuridico indipendente.
- limitation:Il record non contiene il testo della fonte né una validazione di accuratezza o completezza.
- limitation:L'anno è il metadato locale della pubblicazione/opera, non una revisione del file raw.

### `docs/coordination/UNI_CORPUS_LOTTO_G1.json#G1-004`
- Codici: `external_url_availability_not_checked`, `independent_license_clearance_not_checked`, `manifest_metadata_only_flag_not_declared`, `manifest_id_not_declared_lot_id_used_as_reference`
- not_checked:external_url_availability
- not_checked:current_license_terms
- not_checked:independent_legal_public_domain_status
- limitation:La licenza è riportata come dichiarazione osservata nei file locali e non come parere giuridico indipendente.
- limitation:Il record non contiene il testo della fonte né una validazione di accuratezza o completezza.
- limitation:L'anno è il metadato locale della pubblicazione/opera, non una revisione del file raw.

### `docs/coordination/UNI_CORPUS_LOTTO_G1.json#G1-005`
- Codici: `external_url_availability_not_checked`, `independent_license_clearance_not_checked`, `manifest_metadata_only_flag_not_declared`, `manifest_id_not_declared_lot_id_used_as_reference`
- not_checked:external_url_availability
- not_checked:current_license_terms
- not_checked:independent_legal_public_domain_status
- limitation:La licenza è riportata come dichiarazione osservata nei file locali e non come parere giuridico indipendente.
- limitation:Il record non contiene il testo della fonte né una validazione di accuratezza o completezza.
- limitation:L'anno è il metadato locale della pubblicazione/opera, non una revisione del file raw.

### `docs/coordination/UNI_CORPUS_LOTTO_G1.json#G1-006`
- Codici: `external_url_availability_not_checked`, `independent_license_clearance_not_checked`, `manifest_metadata_only_flag_not_declared`, `manifest_id_not_declared_lot_id_used_as_reference`
- not_checked:external_url_availability
- not_checked:current_license_terms
- not_checked:independent_legal_public_domain_status
- limitation:La licenza è riportata come dichiarazione osservata nei file locali e non come parere giuridico indipendente.
- limitation:Il record non contiene il testo della fonte né una validazione di accuratezza o completezza.
- limitation:L'anno è il metadato locale della pubblicazione/opera, non una revisione del file raw.

### `docs/coordination/UNI_CORPUS_LOTTO_G1.json#G1-007`
- Codici: `external_url_availability_not_checked`, `independent_license_clearance_not_checked`, `manifest_metadata_only_flag_not_declared`, `manifest_id_not_declared_lot_id_used_as_reference`
- not_checked:external_url_availability
- not_checked:current_license_terms
- not_checked:independent_legal_public_domain_status
- limitation:La licenza è riportata come dichiarazione osservata nei file locali e non come parere giuridico indipendente.
- limitation:Il record non contiene il testo della fonte né una validazione di accuratezza o completezza.
- limitation:L'anno è il metadato locale della pubblicazione/opera, non una revisione del file raw.

### `docs/coordination/UNI_CORPUS_LOTTO_G1.json#G1-008`
- Codici: `external_url_availability_not_checked`, `independent_license_clearance_not_checked`, `manifest_metadata_only_flag_not_declared`, `manifest_id_not_declared_lot_id_used_as_reference`
- not_checked:external_url_availability
- not_checked:current_license_terms
- not_checked:independent_legal_public_domain_status
- limitation:La licenza è riportata come dichiarazione osservata nei file locali e non come parere giuridico indipendente.
- limitation:Il record non contiene il testo della fonte né una validazione di accuratezza o completezza.
- limitation:L'anno è il metadato locale della pubblicazione/opera, non una revisione del file raw.

### `docs/coordination/UNI_CORPUS_LOTTO_G1.json#G1-009`
- Codici: `external_url_availability_not_checked`, `independent_license_clearance_not_checked`, `manifest_metadata_only_flag_not_declared`, `manifest_id_not_declared_lot_id_used_as_reference`
- not_checked:external_url_availability
- not_checked:current_license_terms
- not_checked:independent_legal_public_domain_status
- limitation:La licenza è riportata come dichiarazione osservata nei file locali e non come parere giuridico indipendente.
- limitation:Il record non contiene il testo della fonte né una validazione di accuratezza o completezza.
- limitation:L'anno è il metadato locale della pubblicazione/opera, non una revisione del file raw.

### `docs/coordination/UNI_CORPUS_LOTTO_G1.json#G1-010`
- Codici: `external_url_availability_not_checked`, `independent_license_clearance_not_checked`, `manifest_metadata_only_flag_not_declared`, `manifest_id_not_declared_lot_id_used_as_reference`
- not_checked:external_url_availability
- not_checked:current_license_terms
- not_checked:independent_legal_public_domain_status
- limitation:La licenza è riportata come dichiarazione osservata nei file locali e non come parere giuridico indipendente.
- limitation:Il record non contiene il testo della fonte né una validazione di accuratezza o completezza.
- limitation:L'anno è il metadato locale della pubblicazione/opera, non una revisione del file raw.

### `docs/coordination/UNI_CORPUS_LOTTO_G1.json#G1-011`
- Codici: `external_url_availability_not_checked`, `independent_license_clearance_not_checked`, `manifest_metadata_only_flag_not_declared`, `manifest_id_not_declared_lot_id_used_as_reference`
- not_checked:external_url_availability
- not_checked:current_license_terms
- not_checked:independent_legal_public_domain_status
- limitation:La licenza è riportata come dichiarazione osservata nei file locali e non come parere giuridico indipendente.
- limitation:Il record non contiene il testo della fonte né una validazione di accuratezza o completezza.
- limitation:L'anno è il metadato locale della pubblicazione/opera, non una revisione del file raw.

### `docs/coordination/UNI_CORPUS_LOTTO_G1.json#G1-012`
- Codici: `external_url_availability_not_checked`, `independent_license_clearance_not_checked`, `manifest_metadata_only_flag_not_declared`, `manifest_id_not_declared_lot_id_used_as_reference`
- not_checked:external_url_availability
- not_checked:current_license_terms
- not_checked:independent_legal_public_domain_status
- limitation:La licenza è riportata come dichiarazione osservata nei file locali e non come parere giuridico indipendente.
- limitation:Il record non contiene il testo della fonte né una validazione di accuratezza o completezza.
- limitation:L'anno è il metadato locale della pubblicazione/opera, non una revisione del file raw.

### `docs/coordination/UNI_CORPUS_LOTTO_G1.json#G1-013`
- Codici: `external_url_availability_not_checked`, `independent_license_clearance_not_checked`, `manifest_metadata_only_flag_not_declared`, `manifest_id_not_declared_lot_id_used_as_reference`
- not_checked:external_url_availability
- not_checked:current_license_terms
- not_checked:independent_legal_public_domain_status
- limitation:La licenza è riportata come dichiarazione osservata nei file locali e non come parere giuridico indipendente.
- limitation:Il record non contiene il testo della fonte né una validazione di accuratezza o completezza.
- limitation:L'anno è il metadato locale della pubblicazione/opera, non una revisione del file raw.

### `docs/coordination/UNI_CORPUS_LOTTO_G1.json#G1-014`
- Codici: `external_url_availability_not_checked`, `independent_license_clearance_not_checked`, `manifest_metadata_only_flag_not_declared`, `manifest_id_not_declared_lot_id_used_as_reference`
- not_checked:external_url_availability
- not_checked:current_license_terms
- not_checked:independent_legal_public_domain_status
- limitation:La licenza è riportata come dichiarazione osservata nei file locali e non come parere giuridico indipendente.
- limitation:Il record non contiene il testo della fonte né una validazione di accuratezza o completezza.
- limitation:L'anno è il metadato locale della pubblicazione/opera, non una revisione del file raw.

### `docs/coordination/UNI_CORPUS_LOTTO_G5_ECFR.json#BLOCKER-001`
- Codici: `exact_url_not_declared`, `license_or_reuse_terms_not_declared`, `blocked_until_missing_metadata_or_evidence_is_supplied`
- blocker_reason:Il PDF GSE già registrato non ha un URL esatto locale per quel file e non ha termini di riuso dichiarati nei metadati osservati; non viene promosso in G5.
- blocker_evidence:UNIVERSITA_EDILIZIA/ENERGETICA_INCENTIVI_PACK/fonti/PROVENANCE_MANIFEST_G3_GSE_CT3.json
- blocker_evidence:record=G3-2-001
- blocker_evidence:verification_status.state=blocked

### `docs/coordination/UNI_CORPUS_LOTTO_G5_ECFR.json#G5-001`
- Codici: `external_url_availability_not_checked`, `independent_license_clearance_not_checked`, `current_version_or_vigency_not_checked`, `content_or_legal_accuracy_not_checked`
- not_checked:external_url_availability
- not_checked:current_content_as_of_observed_at
- not_checked:independent_legal_clearance
- not_checked:current_regulatory_applicability
- not_checked:technical_accuracy_or_completeness
- limitation:Il locator è verificato localmente nei registri, ma la disponibilità esterna e il contenuto corrente della pagina non sono stati validati in questo manifest.
- limitation:La licenza è una dichiarazione osservata nel registro locale; non equivale a parere legale o a verifica indipendente dei diritti su eventuali trasformazioni.
- limitation:Il record non contiene testo XML, sezioni regolamentari, interpretazioni, valori tecnici o risposte d'esame.

### `docs/coordination/UNI_CORPUS_LOTTO_G5_ECFR.json#G5-CONTEXT-001`
- Codici: `license_or_reuse_terms_not_declared`, `context_does_not_prove_source_vigency_or_reuse`

## Alias tra manifest

Le righe seguenti sono rappresentazioni dello stesso path+SHA-256 in manifest diversi; non sono deduplicate automaticamente.

- `Fondamenti_Pack/raw/gutenberg/Aristotle_Ethics_pg8438.txt` — `A68264A6537BB58B899ED68E25D1C7D8EA1BCB3E9544B4D1B464F74D99C3D059`: `Fondamenti_Pack/PROVENANCE_MANIFEST_G2.json#G1-001`, `docs/coordination/UNI_CORPUS_LOTTO_G1.json#G1-001`
- `Fondamenti_Pack/raw/gutenberg/Calculus_Made_Easy_Thompson.txt` — `C24B6E367D112398B488AAF61BE728EC125E3B251212BA98CEFFB73FD9ADBF0F`: `Fondamenti_Pack/PROVENANCE_MANIFEST_G2.json#G1-002`, `docs/coordination/UNI_CORPUS_LOTTO_G1.json#G1-002`
- `Fondamenti_Pack/raw/gutenberg/Descartes_Discourse_pg59.txt` — `7768BA8D3895BE3D6F1492733FFAB983D69875CC743EDD23A1840E1530D02924`: `Fondamenti_Pack/PROVENANCE_MANIFEST_G2.json#G1-003`, `docs/coordination/UNI_CORPUS_LOTTO_G1.json#G1-003`
- `Fondamenti_Pack/raw/gutenberg/Einstein_Relativity_pg30155.txt` — `86ED8156239455CBB6ED33E06097707D3AB7C40D46E9AA5FF32D3C3F94EF68FD`: `Fondamenti_Pack/PROVENANCE_MANIFEST_G2.json#G1-004`, `docs/coordination/UNI_CORPUS_LOTTO_G1.json#G1-004`
- `Fondamenti_Pack/raw/gutenberg/Euclid_Elements.txt` — `A274721324564572153A54D31E94FB9A15E18481B71085293484750941799EDD`: `Fondamenti_Pack/PROVENANCE_MANIFEST_G2.json#G1-005`, `docs/coordination/UNI_CORPUS_LOTTO_G1.json#G1-005`
- `Fondamenti_Pack/raw/gutenberg/Flatland_pg201.txt` — `03DD4508636E44AB9B37EFDA856745545F22EA5ACE95E2EB16C3EF50307CD9F7`: `Fondamenti_Pack/PROVENANCE_MANIFEST_G2.json#G1-006`, `docs/coordination/UNI_CORPUS_LOTTO_G1.json#G1-006`
- `Fondamenti_Pack/raw/gutenberg/Kant_Critique_pg4280.txt` — `9E44B1BC6042DA4AEB669D4F3F585037A5488A2908E7EC225F9431C43F6720FC`: `Fondamenti_Pack/PROVENANCE_MANIFEST_G2.json#G1-007`, `docs/coordination/UNI_CORPUS_LOTTO_G1.json#G1-007`
- `Fondamenti_Pack/raw/gutenberg/Lavoisier_Chemistry_pg30775.txt` — `E23A6F8685CA0A2B7E60C57AF9357C56803AD08E0D1B91F6B55800D28524D1E9`: `Fondamenti_Pack/PROVENANCE_MANIFEST_G2.json#G1-008`, `docs/coordination/UNI_CORPUS_LOTTO_G1.json#G1-008`
- `Fondamenti_Pack/raw/gutenberg/Marcus_Meditations_pg2680.txt` — `6977474F82A39DD88A4AF31A59504821658174D33C177732C54357E4D680B96C`: `Fondamenti_Pack/PROVENANCE_MANIFEST_G2.json#G1-009`, `docs/coordination/UNI_CORPUS_LOTTO_G1.json#G1-009`
- `Fondamenti_Pack/raw/gutenberg/Newton_Principia_pg28233.txt` — `A734045637DEEF5F22CE71D469DEB44B19F73583D9576A9646DB8DD3431B30AB`: `Fondamenti_Pack/PROVENANCE_MANIFEST_G2.json#G1-010`, `docs/coordination/UNI_CORPUS_LOTTO_G1.json#G1-010`
- `Fondamenti_Pack/raw/gutenberg/Origin_Species_pg1228.txt` — `EDEDA9C0BF8761EFED092C303B46C1C92DE956838CBA6249A33BEDFD6D7363B4`: `Fondamenti_Pack/PROVENANCE_MANIFEST_G2.json#G1-011`, `docs/coordination/UNI_CORPUS_LOTTO_G1.json#G1-011`
- `Fondamenti_Pack/raw/gutenberg/Plato_Republic_pg1497.txt` — `917C1CB469E1A8EBA6083808764D7131DA8D79140B575B4214C9D02A73EC4528`: `Fondamenti_Pack/PROVENANCE_MANIFEST_G2.json#G1-012`, `docs/coordination/UNI_CORPUS_LOTTO_G1.json#G1-012`
- `Fondamenti_Pack/raw/gutenberg/Russell_Problems_pg5827.txt` — `2505EA57849C64ABE7962FFE56972174C9160606348E08CB7876D46B2C5B2D96`: `Fondamenti_Pack/PROVENANCE_MANIFEST_G2.json#G1-013`, `docs/coordination/UNI_CORPUS_LOTTO_G1.json#G1-013`
- `Fondamenti_Pack/raw/gutenberg/Wittgenstein_Tractatus_tractatuslogicop1971witt.txt` — `88F528760B8EE4DFEE44E3AD9B83ED06DAE4E57BDE3308F03115F6CCB4705BB6`: `Fondamenti_Pack/PROVENANCE_MANIFEST_G2.json#G1-014`, `docs/coordination/UNI_CORPUS_LOTTO_G1.json#G1-014`

## Limiti

Questo audit rende leggibili gli stati e i residui dichiarati; non prova accuratezza tecnica, vigenza normativa, disponibilità esterna degli URL, titolarità/licenza indipendente o correttezza didattica.
