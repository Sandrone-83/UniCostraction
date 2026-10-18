# UniCostraction — audit anti-ridondanza G10-A

## Esito verificato

Il tool [`uni_redundancy_audit_g10_a.py`](../../tools/uni_redundancy_audit_g10_a.py)
costruisce un report JSON deterministico per le unità di contenuto delle
schede e degli esami pubblici. L'output machine-readable è
[`UNI_REDUNDANCY_AUDIT_G10_A.json`](UNI_REDUNDANCY_AUDIT_G10_A.json), con
contratto in [`UNI_REDUNDANCY_AUDIT_G10_A.schema.json`](UNI_REDUNDANCY_AUDIT_G10_A.schema.json).

Snapshot del checkout osservato:

| Perimetro | File | Unità |
| --- | ---: | ---: |
| schede JSONL | 71 | 963 card |
| esami pubblici | 73 | 18.689 domande |
| totale | 144 | 19.652 unità |

Non sono stati rilevati errori di parsing. Sono stati riconosciuti sia gli
heading standard `## Domanda N` sia il formato legacy inline `**D<n>.**`.
Il report non legge chiavi di risposta, non copia il testo didattico nel report
e non modifica, sposta, fonde o cancella file.

Risultato dello snapshot:

| Classificazione | Unità | Significato operativo |
| --- | ---: | --- |
| `duplicate_exact` | 0 | Nessun gruppo con `content_sha256` uguale nel perimetro indicizzato. |
| `candidate_review` | 241 | Unità coinvolte in 303 coppie sopra la soglia esplicita di similarità. |
| `distinct` | 19.411 | Nessun segnale secondo la metrica configurata; non è una prova di unicità semantica. |

## Metodo conservativo

Per ogni file vengono conservati `raw_sha256` e hash del file con soli line
ending normalizzati. Per ogni riga JSONL viene calcolato un
`content_sha256` sul JSON canonico con chiavi ordinate; per ogni domanda viene
calcolato sul corpo della domanda, con line ending normalizzati e senza il
numero dell'heading. Questa è la frontiera dell'hash: non vengono riordinati
campi didattici, riscritti sinonimi, rimossi numeri o dedotte equivalenze.

La similarità non è un'impressione nominale. Il tool usa esclusivamente
`token_set_jaccard = |token comuni| / |unione token|`, con:

- soglia `0.90`;
- almeno 12 token distinti per unità;
- confronto solo dentro lo stesso gruppo sorgente (`cards` oppure
  `public_exams`), per non promuovere automaticamente una domanda derivata da
  una scheda a duplicato;
- indice di token condivisi e limite di 50.000 coppie emesse.

Il valore e la soglia sono registrati in ogni elemento `candidate_review`.
L'ordine di file, unità, gruppi e coppie è stabile; il report non contiene
timestamp o dati dipendenti dall'ordine di enumerazione del filesystem.

## Differenza tra le tre classi

- `duplicate_exact`: collisione di `content_sha256` fra almeno due unità. È
  evidenza riproducibile da esaminare, non autorizzazione a cancellare o
  accorpare.
- `candidate_review`: coppia non esatta che supera la metrica dichiarata. È una
  coda di revisione umana: servono contenuto, provenienza, scopo didattico e
  decisione esplicita prima di qualunque intervento.
- `distinct`: nessuno dei segnali configurati è scattato. Non significa che le
  unità siano semanticamente, didatticamente, normativamente o legalmente
  uniche.

La classificazione delle unità applica la precedenza `duplicate_exact`, poi
`candidate_review`, poi `distinct`. Il report contiene anche le coppie
candidate, perché una singola unità può partecipare a più revisioni.

## Verifiche e residui

Sono stati verificati tool e fixture deterministici, parser JSONL, parser dei
due formati d'esame, assenza di contenuto didattico copiato nell'evidenza e
rispetto del limite di generazione delle coppie. Restano fuori dal perimetro
raw/discovery, README, manifesti, asset, chiavi di risposta e confronto
semantico supervisionato. Nessun risultato autorizza una deduplicazione
automatica o certifica correttezza didattica, fattuale, normativa o di licenza.

Rigenerazione:

```powershell
python tools/uni_redundancy_audit_g10_a.py
```
