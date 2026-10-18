# UNI QA / Provenance - G5-C guard esteso dei materiali pubblici

Data: 2026-10-18

Worktree autorizzato: `C:\Users\Alessandro\Documents\Codex\2026-10-17\unicostruction-university\worktrees\uni-qa-provenance`

Branch: `codex/uni-qa-provenance`

## Perimetro

G5-C estende il guard strutturale di G4 senza modificare le domande pubbliche
e senza inserire risposte attese nei test. La scoperta usa solo file tracciati
da Git e comprende:

- i file sotto `UNIVERSITA_EDILIZIA/ESAMI/`;
- ogni file il cui nome contiene `manifest`;
- tutti i documenti sotto `docs/coordination/`;
- i documenti testuali in qualunque percorso che contiene `corpus`, inclusi
  metadati JSON/JSONL/YAML e documentazione Markdown. Gli asset binari CAD
  nello stesso percorso restano fuori da questo controllo testuale.

Il guard cerca esclusivamente strutture riconoscibili: campi o chiavi per
answer/answer key, risposte, lettere corrette, spiegazioni/razionali,
soluzioni e punteggi, oltre a mappe numeriche domanda-valore senza etichetta.
I test negativi usano soltanto nomi di campo e valori segnaposto, mai lettere
corrette, testo di opzioni, spiegazioni reali o punteggi attesi.

## Marker documentali consentiti

Resta consentita la prosa che dichiara esplicitamente l'assenza o la
separazione della chiave, per esempio `Risposte NON presenti: il file chiave è
riservato (fuori repository)` e `Le chiavi restano fuori repository`. Restano
lecite anche frasi naturali delle domande o della documentazione quando il
termine non è un campo strutturato. I nomi `correct_letter`, `explanation`,
`risposte` e `score`, quando usati come campi strutturati, sono invece
bloccati anche se il valore è nullo o dichiara “non pubblicato”, salvo il
marker documentale di assenza riconosciuto esplicitamente.

## Limiti

Questo è un guard negativo e strutturale del confine del repository. Non
dimostra l'assenza di risposte mascherate in testo libero, opzioni, immagini,
asset binari, codifiche non riconosciute o semantica equivalente; non ricostruisce
una chiave e non valuta la qualità delle domande. In particolare, non è una
validazione didattica, fattuale, normativa o professionale e non verifica la
completezza/accuratezza della chiave esterna `ESAMI_RISPOSTE/`. `compileall`, i
test unitari e `git diff --check` attestano soltanto le rispettive proprietà
tecniche.

## Verifiche previste

```text
python -m unittest tests\coordination\test_exam_separation_g1.py tests\coordination\test_exam_separation_g2.py tests\coordination\test_exam_provenance_g3.py tests\coordination\test_public_exam_key_guard_g4.py
python -m compileall -q tests
git diff --check
```
