# UNI QA / Provenance - G8-C evidence ledger e remediation

Data: 2026-10-18

Worktree autorizzato: `C:\Users\Alessandro\Documents\Codex\2026-10-17\unicostruction-university\worktrees\uni-qa-provenance`

Branch: `codex/uni-qa-provenance`

## Contratto strutturale

`UNI_EVIDENCE_LEDGER_G8.json` è un ledger di metadati e non contiene
contenuto d'esame. Il contratto dichiara limiti espliciti e gli stati ammessi
`blocked`, `pending`, `open` e `resolved`; il gruppo di stati non risolti
obbligatori è `blocked`, `pending`, `open`.

Una voce `resolved` deve avere un `evidence_ref` non vuoto. Per le voci non
risolte il riferimento può restare nullo. Il valore di riferimento identifica
solo una forma di tracciabilità: il gate non certifica l'esistenza, la qualità,
l'attualità o l'autorevolezza dell'evidenza.

## Limiti e separazione

Il validator verifica forma JSON, nomi di campo, stati e presenza del
riferimento richiesto. Non dimostra correttezza didattica, fattuale,
normativa, legale o professionale; non interpreta testo libero, immagini,
asset binari o risposte mascherate.

Il ledger e le fixture del gate non contengono strutture di answer key,
response, grade o solution. Le fixture sintetiche usate per i casi negativi
usano esclusivamente `None` o `placeholder`.

## Verifica

```text
python tools\validate_remediation_g8.py docs\coordination\UNI_EVIDENCE_LEDGER_G8.json
python -m unittest tests\coordination\test_evidence_ledger_remediation_guard_g8.py
```
