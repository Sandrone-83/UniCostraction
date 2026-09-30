# Fondamenti_Pack — Basi matematiche, scientifiche e filosofiche per LLM

Pacchetto complementare a Edilizia_Pack: dà al LLM le **fondamenta del ragionamento** —
matematica, geometria, trigonometria, calcolo, fisica, chimica, metodo scientifico e
filosofia — perché ragioni correttamente sui calcoli strutturali, parli con cultura e
interagisca in modo naturale. **Tutto a licenza commerciale libera, verificata**
(vedi `licenze_audit.json`).

## Cosa contiene

| File | Contenuto | Licenza |
| --- | --- | --- |
| `parsed/classici_fondamenti.jsonl` | 14 capostipiti public domain: Euclide, Newton, Einstein, Lavoisier, Darwin, Thompson, Flatland, Platone, Aristotele, Marco Aurelio, Russell, Descartes, Kant, Wittgenstein | Public domain |
| `parsed/wiki_fondamenti/wikibooks_en.jsonl` | Wikibooks: Trigonometry, Calculus, Physics (didattica completa) | CC BY-SA 4.0 |
| `parsed/wiki_fondamenti/wiki_fondamenti_en.jsonl` | Voci EN: matematica, fisica (anche resistenza dei materiali base: tensione, deformazione, modulo elastico, trave), chimica, metodo scientifico, filosofia | CC BY-SA 4.0 |
| `parsed/wiki_fondamenti/wiki_fondamenti_it.jsonl` | Voci IT: le stesse basi in italiano (terminologia per l'utente italiano) | CC BY-SA 4.0 |
| `raw/gutenberg/` | Testi grezzi sorgente | come sopra |

## Perché questo pack

- **Calcoli**: trigonometria, calcolo, vettori e unità di misura sono la base di ogni
  verifica strutturale (NTC, Eurocodici) e di ogni computo
- **Fisica**: meccanica, termodinamica (impianti HVAC), ottica (illuminotecnica),
  acustica, resistenza dei materiali
- **Filosofia e metodo scientifico**: logica, epistemologia, filosofia della scienza —
  per un LLM che ragiona con spirito critico e parla con cultura generale

## Estendere

```bash
python fetch_wiki_fondamenti.py   # riprende e completa Wikipedia/Wikibooks (throttling: pazienza)
python serialize_fondamenti.py    # rigenera parsed/classici_fondamenti.jsonl + manifest.json
```

## Escluso di proposito

**OpenStax** è CC BY ma ogni pagina dichiara che il contenuto *non può essere usato per
l'addestramento di LLM senza permesso di OpenStax* — escluso. Dettagli in `licenze_audit.json`.

---

## Aggiornamento 29/09/2026 — Cultura del pensiero

**`parsed/cultura_pensiero.jsonl`** — 9 schede: pensiero antico e medievale (Presocratici, Socrate, Platone, Aristotele, Agostino, Tommaso, Rinascimento), filosofia moderna (Cartesio, Hume, Kant, Hegel, Marx, Nietzsche), filosofia contemporanea (esistenzialismo, pragmatismo, filosofia analitica, Frankfurt, filosofia della scienza), logica e retorica (fallacie, Toulmin, ethos/pathos/logos), metodo scientifico ed epistemologia (Popper, Kuhn, Bayes, statistica pratica), bias cognitivi e negoziazione (Kahneman, Fisher-Ury), micro/macro economia essenziale, scrittura professionale, grammatica e lessico dell'italiano tecnico.

Licenza: sintesi didattica originale (pubblico dominio) — fonte CULTURA-PENSIERO nell'audit.
