# UNI QA / Provenance - G7-C publication readiness and remediation

Data: 2026-10-18
Worktree autorizzato: `C:\Users\Alessandro\Documents\Codex\2026-10-17\unicostruction-university\worktrees\uni-qa-provenance`
Branch: `codex/uni-qa-provenance`

## Gate di pubblicazione

Questo report è un controllo strutturale del percorso di pubblicazione. Lo
stato corrente è `blocked`: un esito `pending` o `blocked` non autorizza da
solo la pubblicazione e richiede la verifica/remediation prevista dal
percorso di rilascio.

I manifest pubblici devono dichiarare nel campo `publication_contract`:

- limiti non vuoti e leggibili;
- gli stati ammessi `pending` e `blocked`;
- `answer_key_separation.status = separate` e
  `answer_key_separation.public = false`.

La answer key resta separata e fuori dal materiale pubblico. Nessun report,
manifest o fixture di questo gate contiene una risposta reale, una lettera di
opzione, una spiegazione, una soluzione o un punteggio.

## Limiti espliciti

Il gate verifica nomi di campi, forme JSON e dichiarazioni di stato. Non
dimostra correttezza didattica, fattuale, normativa, legale o professionale;
non ispeziona semantica del testo libero, immagini, asset binari o risposte
mascherate. `compileall`, i test unitari e `git diff --check` attestano solo le
loro proprietà tecniche.

## Remediation e verifiche

Se il gate è `pending` o `blocked`, il report deve restare non pubblicabile
finché il proprietario non completa la remediation e una revisione umana
esplicita. La suite G1-G7, `compileall` e `git diff --check` sono prerequisiti
tecnici separati; commit, push e `git ls-remote` sono verifiche di stato Git e
non sostituiscono la revisione del contenuto.

```text
python -m unittest tests\coordination\test_exam_separation_g1.py tests\coordination\test_exam_separation_g2.py tests\coordination\test_exam_provenance_g3.py tests\coordination\test_public_exam_key_guard_g4.py tests\coordination\test_public_exam_key_guard_g5.py tests\coordination\test_cross_corpus_key_guard_g6.py tests\coordination\test_publication_readiness_guard_g7.py
python -m compileall -q tests
git diff --check
```
