# UNI QA / Provenance - G6-C guard cross-corpus

Data: 2026-10-18

Worktree autorizzato: `C:\Users\Alessandro\Documents\Codex\2026-10-17\unicostruction-university\worktrees\uni-qa-provenance`

Branch: `codex/uni-qa-provenance`

## Perimetro

G6-C aggiunge `tests/coordination/test_cross_corpus_key_guard_g6.py` come
controllo disgiunto dal guard G4/G5. La scoperta usa soltanto file tracciati
da Git e comprende:

- tutti i documenti testuali sotto `docs/coordination/`, inclusi i nuovi
  manifest/schema G5 di corpus e i report di revisione quando vengono
  integrati nel checkout;
- i documenti testuali in percorsi il cui nome contiene `corpus`;
- gli artefatti testuali il cui nome contiene `audit`, `dashboard` o `review`,
  così da coprire i report/audit previsti senza aprire asset binari.

Il guard riusa solo il riconoscimento strutturale del confine pubblico: nomi
di campi e mappe numeriche domanda-valore senza etichetta. I fixture negativi
usano esclusivamente `None` o `placeholder`; i fixture positivi usano
metadati, stati di revisione e avvisi documentali. Nei test non sono presenti
risposte attese, lettere di opzione, testo di spiegazioni, soluzioni o
punteggi.

## Significato e limiti

Il controllo verifica che le forme strutturate riconoscibili non espongano una
chiave, una lettera corretta, una soluzione, una spiegazione o un punteggio.
È un guard negativo e strutturale del repository, non una verifica
didattica, fattuale, normativa o professionale. Non dimostra l'assenza di
risposte mascherate in testo libero, opzioni, immagini, asset binari,
codifiche non riconosciute o semantica equivalente. Non valuta la qualità,
correttezza o completezza di domande, fonti, audit o manifest.

`compileall`, test unitari e `git diff --check` attestano soltanto le loro
rispettive proprietà tecniche; non costituiscono una validazione educativa,
fattuale, normativa o di provenienza.

## Verifiche previste

```text
python -m unittest tests\coordination\test_exam_separation_g1.py tests\coordination\test_exam_separation_g2.py tests\coordination\test_exam_provenance_g3.py tests\coordination\test_public_exam_key_guard_g4.py tests\coordination\test_public_exam_key_guard_g5.py tests\coordination\test_cross_corpus_key_guard_g6.py
python -m compileall -q tests
git diff --check
```
