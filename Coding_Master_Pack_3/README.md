# Coding_Master_Pack_3 — Terzo livello (aree mai coperte)

Il terzo pack coding: sei aree che i primi due pack non toccavano, scelte anche
per il dominio edile (geometria CAD, IoT da cantiere). 30 schede, sei corpus.

## Struttura

| Corpus | File | Schede | Contenuto |
|---|---|---|---|
| Interview e algoritmi | `parsed/interview_algoritmi.jsonl` | 5 | Sliding window e two pointers, intervalli e matrici, backtracking, come affrontare il colloquio tecnico, il system design interview |
| Geometria computazionale | `parsed/geometria_computazionale.jsonl` | 5 | Geometria 2D/3D, mesh e B-Rep, operazioni booleane e kernel CAD, GIS e dati spaziali, graphics e rendering |
| Embedded e IoT | `parsed/embedded_iot.jsonl` | 5 | Elettronica e microcontrollori, MQTT e architettura edge, sensoristica edile, automazione e controllo, progetto monitoraggio cantiere |
| Compilatori e linguaggi | `parsed/compilatori_linguaggi.jsonl` | 5 | Pipeline del compilatore, grammatiche e parsing, bytecode e VM, type systems, costruire un mini-linguaggio |
| Concorrenza avanzata | `parsed/concorrenza_avanzata.jsonl` | 5 | Modelli di concorrenza, lock e deadlock, lock-free e atomics, strutture concorrenti, async/await moderno |
| Testing avanzato | `parsed/testing_avanzato.jsonl` | 5 | Property-based testing, mutation e fuzzing, load testing, testcontainers, qualità come processo |

Formato: JSONL, una scheda JSON per riga (chiavi: id, categoria, tema, title,
text, source, license, commercial_ok, attribution, url).

## Licenza

Sintesi didattica originale redatta per questo progetto: uso commerciale libero,
nessun testo copiato da fonti protette. Vedi `licenze_audit.json`.

## Relazione con i pack 1 e 2

Coding_Master_Pack: nucleo (practices, algoritmi, linguaggi, system design,
sicurezza, AI coding). Coding_Master_Pack_2: superficie operativa (DevOps,
frontend, data/AI, rete, craft, progetti). Coding_Master_Pack_3: le discipline
specialistiche (colloqui, geometria/CAD, embedded, compilatori, concorrenza,
testing avanzato).
