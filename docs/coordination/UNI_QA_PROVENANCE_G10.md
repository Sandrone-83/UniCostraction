# UNI QA / Provenance — G10-C esami protetti e audit pubblici

Data: 2026-10-18

Worktree autorizzato: `C:\Users\Alessandro\Documents\Codex\2026-10-17\unicostruction-university\worktrees\uni-qa-provenance`

Branch: `codex/uni-qa-provenance`

Base: `6fbf5ae773affd03c74cf52d29d20908b91e32fc` (G10)

## Perimetro

`tools/validate_public_qa_g10.py` e
`tests/coordination/test_public_qa_gate_g10.py` sottopongono al controllo
strutturale tutti i 76 file pubblici tracciati sotto
`UNIVERSITA_EDILIZIA/ESAMI/`, non soltanto i 73 file `domande.md`. Il perimetro
comprende quindi anche `README.md`, `PROTOCOLLO_VALUTAZIONE.md` e
`AUDIT_CONTENT_LOCKED.md`, oltre ai due audit metadata-only G10 di
anti-ridondanza e provenienza.

Lo stesso guard riconosce anche gli artefatti integrati G11-C in
`docs/coordination/`: candidate-review clusters, priority queues e matrice
evidence/licenza. Per ciascuno richiede un contratto con limiti, stati ammessi
e separazione della chiave protetta.

Il guard cerca soltanto forme strutturate per answer key, correct option,
explanation, solution, score, response, grade e varianti italiane, oltre a
mappe numeriche domanda-valore. I risultati riportano soltanto percorso,
posizione e tipo di struttura: non stampano valori, opzioni o risposte.

## Audit G10

- `UNI_REDUNDANCY_AUDIT_G10.json` registra il perimetro e mantiene la revisione
  dei duplicati semantici nello stato `pending`.
- `UNI_PROVENANCE_AUDIT_G10.json` registra il perimetro, l'algoritmo e il
  riferimento al manifest precedente; la review di fonte/licenza resta
  `pending`.

Entrambi sono contratti di metadati. Non contengono chiavi, spiegazioni,
punteggi o risposte e non trasformano un controllo strutturale in una
valutazione del contenuto.

## Limiti semantici

Il gate non valuta la correttezza didattica, fattuale, normativa, legale o
professionale delle domande e non prova che una fonte sia autorevole o che una
licenza sia utilizzabile. Non rileva risposte mascherate nel testo libero,
nelle opzioni, nelle immagini, negli asset binari o in codifiche non
riconoscibili come campi strutturati; non esegue la revisione semantica dei
duplicati. Il fatto che lo stato resti `pending` è intenzionale.

Gli hash e i percorsi sono metadati di integrità/provenienza, non una chiave di
correzione e non un esame superato. `compileall`, i test unitari e
`git diff --check` attestano soltanto le rispettive proprietà tecniche.

## Gate richiesti

```text
python -m unittest tests\coordination\test_exam_separation_g1.py tests\coordination\test_exam_separation_g2.py tests\coordination\test_exam_provenance_g3.py tests\coordination\test_public_exam_key_guard_g4.py tests\coordination\test_public_exam_key_guard_g5.py tests\coordination\test_cross_corpus_key_guard_g6.py tests\coordination\test_publication_readiness_guard_g7.py tests\coordination\test_evidence_ledger_remediation_guard_g8.py tests\coordination\test_public_qa_gate_g9.py tests\coordination\test_public_qa_gate_g10.py
python -m compileall -q tests tools
git diff --check
```
