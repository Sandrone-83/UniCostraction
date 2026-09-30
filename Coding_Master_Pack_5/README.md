# Coding_Master_Pack_5 — Quinto livello (le ultime aree non ridondanti)

Cinque aree che chiudono il cerchio della serie: il motore dietro la ricerca e
i sistemi RAG, il motore dietro le query SQL, l'hardware che esegue il codice,
la toolchain che costruisce e distribuisce il software, e i grafi di
conoscenza (il complemento strutturato dei documenti per un LLM).
20 schede, cinque corpus.

## Struttura

| Corpus | File | Schede | Contenuto |
|---|---|---|---|
| Information retrieval | `parsed/information_retrieval.jsonl` | 4 | Indice invertito e BM25, valutazione (precision/recall/NDCG), ricerca vettoriale e HNSW, IR in produzione |
| Query engines | `parsed/query_engines.jsonl` | 4 | Pipeline SQL, algoritmi di join, ottimizzazione cost-based, modelli di esecuzione (OLTP vs OLAP) |
| Architettura calcolatori | `parsed/architettura_calcolatori.jsonl` | 4 | CPU per programmatori, memoria e cache, GPU e SIMT, acceleratori |
| Build systems e tooling | `parsed/build_systems_tooling.jsonl` | 4 | Build incrementali, package manager, monorepo e DX, release engineering |
| Knowledge graphs | `parsed/knowledge_graphs.jsonl` | 4 | Grafi di conoscenza, RDF/OWL, query Cypher, Graph RAG |

Formato: JSONL, una scheda JSON per riga.

## Licenza

Sintesi didattica originale redatta per questo progetto: uso commerciale libero.
Vedi `licenze_audit.json`.

## Nota di chiusura serie

Con questo pack la serie coding tocca 136 schede su 22 corpus: oltre, i
contenuti inizierebbero a ripetersi con le parole cambiate.
