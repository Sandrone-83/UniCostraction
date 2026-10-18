# UNI QA / Provenance - G3 fixture pubblico protetto

Data: 2026-10-18

Worktree autorizzato: `C:\Users\Alessandro\Documents\Codex\2026-10-17\unicostruction-university\worktrees\uni-qa-provenance`

Branch: `codex/uni-qa-provenance`

Base: `45335dee48a9710b232ed2c6e2ec366bb70ea6c6`

## Perimetro

G3 estende il controllo strutturale G2 con:

- `docs/coordination/PUBLIC_EXAM_FIXTURE_MANIFEST_G3.json`, manifest pubblico
  degli hash SHA-256 dei 73 file
  `UNIVERSITA_EDILIZIA/ESAMI/*/domande.md`;
- `tests/coordination/test_exam_provenance_g3.py`, che confronta il manifest
  con il checkout corrente e ricontrolla l'assenza di campi espliciti di
  risposta in ogni file pubblico elencato.

Il test richiede che il set dei percorsi sia esattamente quello scoperto nel
checkout, che il conteggio resti 73 e che ogni digest SHA-256 corrisponda ai
byte del file. Il manifest contiene esclusivamente metadati di integrità e
coppie `path`/`sha256`: non contiene answer key, lettere corrette,
spiegazioni o punteggi.

## Significato dell'hash

L'hash protegge l'integrità del fixture pubblico: consente di rilevare una
modifica, sostituzione o omissione dei file elencati rispetto al manifest.
Non protegge e non dimostra la correttezza delle risposte, delle opzioni,
delle domande o dei contenuti didattici. Un digest coincidente non equivale a
un esame superato e non è una valutazione educativa, fattuale, normativa o
professionale.

## Controllo dei campi espliciti

Il test cerca righe strutturate che nominano un campo di risposta, incluse le
varianti comuni `risposta`, `risposta corretta`, `lettera`, `answer` e
`solution` seguite da `:` o `=`. Non interpreta come chiavi le frasi libere
contenute nelle domande o nelle opzioni e non tenta di ricostruire risposte.

Questo è un controllo negativo sui campi espliciti. Non dimostra l'assenza di
risposte mascherate in testo libero, opzioni, codifiche non riconosciute o
semantica delle domande.

## Copertura e residui

Copertura dichiarata:

- 73/73 file pubblici nel perimetro `*/domande.md` presenti nel manifest;
- 73/73 digest SHA-256 confrontati con il checkout;
- 73/73 file sottoposti al controllo dei campi espliciti;
- la separazione dei formati e la numerazione restano coperte dai test G2
  (71 standard e 2 legacy).

Residui:

- il manifest non valida correttezza, qualità, completezza o aggiornamento
  delle domande e delle fonti;
- la chiave esterna `ESAMI_RISPOSTE/` resta fuori repository e non è oggetto
  di questo manifest;
- file pubblici futuri con estensione o struttura diversa da `*/domande.md`
  richiedono un aggiornamento esplicito dell'inventario e del test;
- i controlli statici e strutturali non costituiscono un esame superato.

## Verifiche previste

```text
python -m unittest tests\coordination\test_exam_separation_g1.py tests\coordination\test_exam_separation_g2.py tests\coordination\test_exam_provenance_g3.py
python -m compileall -q tests
git diff --check
```
