# UNI QA globale — G2 separazione esami

Data: 2026-10-17
Worktree autorizzato: `C:\Users\Alessandro\Documents\Codex\2026-10-17\unicostruction-university\worktrees\uni-qa-provenance`
Branch: `codex/uni-qa-provenance`
Base: `0a2ceaf8eda15e1281ed3ac67092e65a33ed6767`

## Perimetro

`tests/coordination/test_exam_separation_g2.py` estende il controllo G1 a tutti
i file pubblici compatibili con il contratto del repository:

```text
UNIVERSITA_EDILIZIA/ESAMI/*/domande.md
```

Alla base G2 l’inventario comprende 73 file. Il controllo mantiene separati i
due formati pubblici riconosciuti:

| Formato | Intestazione riconosciuta | File alla base G2 |
|---|---|---:|
| standard | `## Domanda N` | 71 |
| legacy | `**D<n>.**` | 2 |

I parser sono distinti e non trasformano il formato legacy nello standard.
Questo conserva il confine tra i generatori storici e quello corrente. Il
controllo non usa il contenuto delle opzioni per stabilire alcun esito.

## Invarianti verificati

Per ogni file pubblico il test verifica soltanto:

1. presenza, contenuto non vuoto e appartenenza all’inventario previsto;
2. riconoscimento da parte di uno e uno solo dei due parser;
3. numerazione consecutiva a partire da 1, senza buchi o duplicati;
4. assenza, nei blocchi delimitati dalle intestazioni, di righe con forma di
   campo esplicito di risposta.

Sono trattati come campi strutturati solo nomi in testa a una riga con `:` o
`=` (incluse varianti comuni di marcatura Markdown e dei nomi del campo). Le
frasi della premessa che dichiarano l’assenza delle risposte restano fuori dai
blocchi e non vengono interpretate come dati d’esame.

## Confini e residui

Il controllo non verifica:

- quale opzione sia corretta, né conserva lettere, chiavi o spiegazioni;
- correttezza didattica, fattuale o normativa delle domande;
- qualità, completezza o accuratezza dell’archivio esterno
  `ESAMI_RISPOSTE/`;
- corrispondenza con le schede fonte, aggiornamento delle fonti o validità di
  affermazioni tecniche;
- file diversi da `*/domande.md`, inclusi eventuali payload pubblici futuri
  con un’estensione o una struttura non prevista dal contratto;
- campi di risposta mascherati dentro testo libero, opzioni o codifiche non
  riconoscibili come righe strutturate.

Un esito positivo è quindi soltanto un esito di separazione/formato per
l’inventario coperto. Non è un esame superato e non costituisce un giudizio
sulla validità dei contenuti.

La chiave esterna resta fuori repository; non va aggiunta per far passare il
test. L’eventuale aggiunta, rimozione o conversione di un esame richiede un
nuovo controllo dell’inventario e del parser interessato.

## Verifiche previste

```text
python -m unittest discover -s tests
python -m compileall -q tests
git diff --check
```
