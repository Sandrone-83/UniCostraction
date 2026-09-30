# HANDOFF — Istruzioni per Claude Code (Fondamenti_Pack)

Pacchetto delle BASI per il LLM: matematica, geometria, trigonometria, calcolo, fisica,
chimica, metodo scientifico, filosofia. Da usare INSIEME a Edilizia_Pack (le basi
potenziano la parte tecnica: calcoli strutturali, impiantistica fisica, ragionamento).

## Ingestione

1. `parsed/classici_fondamenti.jsonl` — 14 capostipiti public domain (1.418 chunk):
   Euclide, Newton, Einstein, Lavoisier, Darwin, Thompson, Abbott, Platone, Aristotele,
   Marco Aurelio, Russell, Descartes, Kant, Wittgenstein. Campi: title/author/year.
2. `parsed/wiki_fondamenti/wikibooks_en.jsonl` — Trigonometry / Calculus / Physics
   (Wikibooks, campo `book` per bilanciare).
3. `parsed/wiki_fondamenti/wiki_fondamenti_en.jsonl` + `_it.jsonl` — voci Wikipedia
   matematica/fisica/chimica/filosofia (parziali: throttling Wikimedia, completabili
   rilanciando `fetch_wiki_fondamenti.py` che riprende da solo).

Tutti i record hanno `license`, `attribution`, `commercial_ok: true`.

## Pesi consigliati

- Classici: peso pieno per filosofia/logica; Euclide + Thompson + Newton = fondamenta
  dei calcoli — mai sotto-campionare
- Wikibooks/Wikipedia: peso 0,7 (didattica essenziale ma ridondante)

## NON aggiungere (licenze)

OpenStax (clausola anti-LLM su CC BY), MIT OCW/NPTEL/LibreTexts (NC), testi editi.
Dettagli: `licenze_audit.json`.
