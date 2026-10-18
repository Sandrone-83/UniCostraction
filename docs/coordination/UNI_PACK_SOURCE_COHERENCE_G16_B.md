# G16-B — Coerenza pack/source

Questo report riconcilia, in modalità metadata-only, la coverage provenance G13-B, la coda evidence G14-B e la riconciliazione manifest G15-B.

## Risultato

- 71 pack presenti una sola volta, ordinati per `pack_path`.
- 70 pack hanno la richiesta evidence G14-B in stato `blocked`.
- `ENERGETICA_INCENTIVI_PACK` non è nella coda G14-B perché ha un match esplicito di manifest in G13-B; conserva comunque una richiesta evidence aperta riferita ai remediation code G13-B.
- Tutti i pack restano `blocked` come stato complessivo, perché nessun pack ha contemporaneamente evidence e licence status osservati localmente.
- Ogni riga conserva riferimenti di remediation G13-B e G15-B; le righe in coda aggiungono il riferimento ai blocker G14-B.

## Contratto

Il tool `tools/audit_pack_source_coherence_g16_b.py` usa solo l’identità esplicita `pack_path` per unire i tre report. Verifica che G13 e G15 abbiano gli stessi 71 pack e che G14 sia l’esatto sottoinsieme di 70 pack non matched della coverage G13.

Ogni riga espone:

- matrice di stato G13 (`source_record`, `locator`, `license`, `evidence`), limitata a `blocked`/`observed_local`;
- stato e identificativo della richiesta G14, oppure `not_queued` per il pack matched;
- scope manifest e remediation aperta G15;
- `evidence_request` con riferimenti verificabili alle richieste, senza copiare payload di fonte;
- `remediation.references` con riferimenti G13/G14/G15.

Non vengono creati source mapping semantici. Nomi corso, `COURSE.yaml` `fonti`, titoli, argomenti e similarità testuale non sono basi di matching. Il report non modifica fonti, pack, schede, esami o contenuti protetti e non equivale a clearance legale, accuratezza tecnica, vigenza normativa o claim-ready.

## Input e output

- G13: `docs/coordination/UNI_PACK_PROVENANCE_COVERAGE_G13_B.json`
- G14: `docs/coordination/UNI_PACK_EVIDENCE_QUEUE_G14_B.json`
- G15: `docs/coordination/UNI_MANIFEST_RECONCILIATION_G15_B.json`
- Output: `docs/coordination/UNI_PACK_SOURCE_COHERENCE_G16_B.json`
- Schema: `docs/coordination/UNI_PACK_SOURCE_COHERENCE_G16_B_SCHEMA.json`

Il report è ancorato a `6d0f5920d253a09491e739aadcd705cde0539212` e osservato il 2026-10-18.

## Verifica

La verifica prevista per G16-B è:

```text
python -m unittest tests/test_g16_b_pack_source_coherence.py
python -m compileall -q tools tests
```

La validazione JSON comprende parsing dei quattro JSON G16 e controllo del contratto tramite `validate_report`; la validazione formale del documento usa lo schema G16-B come artefatto versionato.
