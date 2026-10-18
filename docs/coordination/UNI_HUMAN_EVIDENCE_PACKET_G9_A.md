# UniCostraction — packet evidenze revisione umana tracciabile G9-A

Il packet è un indice metadata-only per la revisione umana dei sei item G5 pending.
I due esami legacy unmatched sono già inclusi in quei sei item e quindi compaiono
una sola volta, con copertura esplicita nel campo `coverage`.

Si rigenera dal checkout selezionato con:

```powershell
python tools/uni_human_evidence_packet_g9_a.py
```

## Collegamenti machine-readable

- G5 review: [`docs/coordination/UNI_PACK_EXAM_REVIEW_G5.json`](docs/coordination/UNI_PACK_EXAM_REVIEW_G5.json)
- G8 ledger: [`docs/coordination/UNI_COMPLETENESS_LEDGER_G8.json`](docs/coordination/UNI_COMPLETENESS_LEDGER_G8.json) e [`docs/coordination/UNI_COMPLETENESS_LEDGER_G8.md`](docs/coordination/UNI_COMPLETENESS_LEDGER_G8.md)
- G7 readiness: [`docs/coordination/UNI_RELEASE_READINESS_G7.json`](docs/coordination/UNI_RELEASE_READINESS_G7.json) e [`docs/coordination/UNI_RELEASE_READINESS_G7.md`](docs/coordination/UNI_RELEASE_READINESS_G7.md); stato **BLOCKED**

## Copertura

- G5 pending: **6**
- esami legacy unmatched: **2**
- record unici nel packet: **6**
- auto-risoluzione: **vietata**

La cardinalità non è 6+2 record: i due legacy sono il sottoinsieme `exam:IMPIANTI_FV_EOLICO` e `exam:MATERIALEDILE` della coda G5, non una seconda copia.

## Item

### `exam:IMPIANTI_FV_EOLICO`

- Identificativo record G8: `exam:IMPIANTI_FV_EOLICO`
- Classificazione: `unmatched_exam`; incertezza: `unmatched_legacy_domain`
- File osservati: `UNIVERSITA_EDILIZIA/ESAMI/IMPIANTI_FV_EOLICO/domande.md`, `UNIVERSITA_EDILIZIA/ESAMI/README.md`
- Motivo del blocco: The exam is explicitly legacy and has no observed pack candidate; the current metadata cannot establish an association.
- Evidenze da raccogliere:
  - `explicit_association_or_disposition`: A source or project-maintained record that either names one existing pack for this exam or explicitly records why it remains unmatched.
  - `legacy_scope_provenance`: Metadata establishing the legacy record's origin, scope, and applicable version or time context.
  - `review_audit`: Reviewer identity, date, cited evidence paths, and a note explaining the selected allowed outcome.
- Decisioni ammesse: `associate_with_explicit_evidence`, `keep_unmatched`, `defer`
- Divieto di auto-risoluzione: **sì**; nessuna decisione su nome, radice, prossimità, flag legacy o contenuto didattico.

### `exam:INFRASTRUTTURE`

- Identificativo record G8: `exam:INFRASTRUTTURE`
- Classificazione: `ambiguous`; incertezza: `ambiguous_observed_candidates`
- File osservati: `UNIVERSITA_EDILIZIA/ESAMI/INFRASTRUTTURE/domande.md`, `UNIVERSITA_EDILIZIA/ESAMI/README.md`
- Motivo del blocco: Observed naming or documentation signals leave multiple candidates; no canonical association has been established.
- Evidenze da raccogliere:
  - `explicit_candidate_association`: A source or project-maintained record that names exactly one candidate association for this pack or exam.
  - `candidate_scope_disambiguation`: Evidence identifying the candidate's scope, version, or ownership and addressing the competing observed candidates.
  - `review_audit`: Reviewer identity, date, cited evidence paths, and a note explaining the selected allowed outcome.
- Decisioni ammesse: `associate_with_explicit_evidence`, `keep_unresolved`, `defer`
- Divieto di auto-risoluzione: **sì**; nessuna decisione su nome, radice, prossimità, flag legacy o contenuto didattico.

### `exam:MATERIALEDILE`

- Identificativo record G8: `exam:MATERIALEDILE`
- Classificazione: `unmatched_exam`; incertezza: `unmatched_legacy_domain`
- File osservati: `UNIVERSITA_EDILIZIA/ESAMI/MATERIALEDILE/domande.md`, `UNIVERSITA_EDILIZIA/ESAMI/README.md`
- Motivo del blocco: The exam is explicitly legacy and has no observed pack candidate; the current metadata cannot establish an association.
- Evidenze da raccogliere:
  - `explicit_association_or_disposition`: A source or project-maintained record that either names one existing pack for this exam or explicitly records why it remains unmatched.
  - `legacy_scope_provenance`: Metadata establishing the legacy record's origin, scope, and applicable version or time context.
  - `review_audit`: Reviewer identity, date, cited evidence paths, and a note explaining the selected allowed outcome.
- Decisioni ammesse: `associate_with_explicit_evidence`, `keep_unmatched`, `defer`
- Divieto di auto-risoluzione: **sì**; nessuna decisione su nome, radice, prossimità, flag legacy o contenuto didattico.

### `exam:STRUTTURE`

- Identificativo record G8: `exam:STRUTTURE`
- Classificazione: `ambiguous`; incertezza: `ambiguous_observed_candidates`
- File osservati: `UNIVERSITA_EDILIZIA/ESAMI/README.md`, `UNIVERSITA_EDILIZIA/ESAMI/STRUTTURE/domande.md`
- Motivo del blocco: Observed naming or documentation signals leave multiple candidates; no canonical association has been established.
- Evidenze da raccogliere:
  - `explicit_candidate_association`: A source or project-maintained record that names exactly one candidate association for this pack or exam.
  - `candidate_scope_disambiguation`: Evidence identifying the candidate's scope, version, or ownership and addressing the competing observed candidates.
  - `review_audit`: Reviewer identity, date, cited evidence paths, and a note explaining the selected allowed outcome.
- Decisioni ammesse: `associate_with_explicit_evidence`, `keep_unresolved`, `defer`
- Divieto di auto-risoluzione: **sì**; nessuna decisione su nome, radice, prossimità, flag legacy o contenuto didattico.

### `pack:AEROPORTI_E_INFRASTRUTTURE_DI_VOLO_PACK`

- Identificativo record G8: `pack:AEROPORTI_E_INFRASTRUTTURE_DI_VOLO_PACK`
- Classificazione: `ambiguous`; incertezza: `ambiguous_observed_candidates`
- File osservati: `UNIVERSITA_EDILIZIA/AEROPORTI_E_INFRASTRUTTURE_DI_VOLO_PACK/COURSE.yaml`, `UNIVERSITA_EDILIZIA/AEROPORTI_E_INFRASTRUTTURE_DI_VOLO_PACK/README.md`, `UNIVERSITA_EDILIZIA/AEROPORTI_E_INFRASTRUTTURE_DI_VOLO_PACK/schede/schede.jsonl`
- Motivo del blocco: Observed naming or documentation signals leave multiple candidates; no canonical association has been established.
- Evidenze da raccogliere:
  - `explicit_candidate_association`: A source or project-maintained record that names exactly one candidate association for this pack or exam.
  - `candidate_scope_disambiguation`: Evidence identifying the candidate's scope, version, or ownership and addressing the competing observed candidates.
  - `review_audit`: Reviewer identity, date, cited evidence paths, and a note explaining the selected allowed outcome.
- Decisioni ammesse: `associate_with_explicit_evidence`, `keep_unresolved`, `defer`
- Divieto di auto-risoluzione: **sì**; nessuna decisione su nome, radice, prossimità, flag legacy o contenuto didattico.

### `pack:FORMULARIO_STRUTTURE_PACK`

- Identificativo record G8: `pack:FORMULARIO_STRUTTURE_PACK`
- Classificazione: `ambiguous`; incertezza: `ambiguous_observed_candidates`
- File osservati: `UNIVERSITA_EDILIZIA/FORMULARIO_STRUTTURE_PACK/COURSE.yaml`, `UNIVERSITA_EDILIZIA/FORMULARIO_STRUTTURE_PACK/README.md`, `UNIVERSITA_EDILIZIA/FORMULARIO_STRUTTURE_PACK/schede/schede.jsonl`
- Motivo del blocco: Observed naming or documentation signals leave multiple candidates; no canonical association has been established.
- Evidenze da raccogliere:
  - `explicit_candidate_association`: A source or project-maintained record that names exactly one candidate association for this pack or exam.
  - `candidate_scope_disambiguation`: Evidence identifying the candidate's scope, version, or ownership and addressing the competing observed candidates.
  - `review_audit`: Reviewer identity, date, cited evidence paths, and a note explaining the selected allowed outcome.
- Decisioni ammesse: `associate_with_explicit_evidence`, `keep_unresolved`, `defer`
- Divieto di auto-risoluzione: **sì**; nessuna decisione su nome, radice, prossimità, flag legacy o contenuto didattico.

## Confini

- il packet non copia contenuti didattici e non modifica corpus, domande, risposte, schede o decisioni G5;
- una decisione `associate_with_explicit_evidence` richiede evidenza esplicita citata e nota del revisore;
- `keep_unresolved`, `keep_unmatched` e `defer` mantengono aperta la revisione;
- il packet non trasforma una revisione umana in approvazione didattica, normativa, legale o semantica.
