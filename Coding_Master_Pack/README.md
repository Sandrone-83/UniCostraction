# Coding_Master_Pack — Sapere da ingegnere del software di livello senior

Materiale didattico per portare un LLM a scrivere codice veloce, corretto,
sicuro e ben architettato: le pratiche che separano chi programma da chi
progetta software. Sei corpus, 36 schede.

## Struttura

| Corpus | File | Schede | Contenuto |
|---|---|---|---|
| Best practices | `parsed/coding_best_practices.jsonl` | 6 | Clean code avanzato, refactoring (catalogo dei movimenti sicuri), code review, gestione errori e logging, documentazione che viene letta, technical debt |
| Algoritmi avanzati | `parsed/algoritmi_avanzati.jsonl` | 6 | Il metodo del pensiero algoritmico, strutture dati avanzate, grafi (BFS/DFS/cammini minimi/MST), programmazione dinamica, divide et impera e greedy, ricerca/ordinamento e complessità in pratica |
| Linguaggi in profondità | `parsed/linguaggi_deep.jsonl` | 6 | Python avanzato, JavaScript/TypeScript moderni, SQL avanzato, C++/Rust, Go, come scegliere il linguaggio giusto |
| System design | `parsed/system_design.jsonl` | 6 | Il metodo in 6 fasi, scalabilità (CAP/sharding/caching), architetture (event-driven/CQRS/microservizi/DDD), scelta e modellazione database, API design evoluto, affidabilità (idempotenza/retry/circuit breaker/saga) |
| Sicurezza del codice | `parsed/sicurezza_coding.jsonl` | 6 | OWASP Top 10, autenticazione moderna, crittografia pratica, supply chain, sicurezza nel coding con AI, GDPR per sviluppatori |
| AI coding | `parsed/ai_coding.jsonl` | 6 | Prompt engineering per codice, dirigere gli agenti, contesto e RAG sul codebase, ciclo genera-verifica, pratica deliberata e benchmark, costruire tool con AI |

Formato: JSONL, una scheda JSON per riga (chiavi: id, categoria, tema, title,
text, source, license, commercial_ok, attribution, url).

## Licenza

Sintesi didattica originale redatta per questo progetto: uso commerciale libero,
nessun testo copiato da fonti protette. Vedi `licenze_audit.json`.

## Avvertenze

- Versioni di linguaggi/framework riferite al 2026: verificare documentazione ufficiale.
- Soglie e percentuali citate sono prassi consolidate indicative.
