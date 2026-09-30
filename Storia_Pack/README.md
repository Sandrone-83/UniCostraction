# Storia_Pack — Storia di architettura, costruzioni e ingegneria

Dalla fondazione del pack di addestramento: dà al LLM la **memoria storica del costruito** —
dalle piramidi al post-moderno, dall'acquedotto romano al calcestruzzo precompresso,
dai cataloghi dei materiali d'epoca alle biografie di ingegneri e architetti.
**Tutto licenza commerciale libera, verificata** (`licenze_audit.json`).

## Cosa contiene

| File | Contenuto | Licenza |
| --- | --- | --- |
| `parsed/storia_classici.jsonl` | 7 testi fondativi: Fletcher (History of Architecture 1905), Choisy 1899, Viollet-le-Duc 1858, Laugier 1753, Durand 1802, FHWA America's Highways 1776-1976, USACE History Corps of Engineers 1998 | Public domain |
| `parsed/cataloghi_edilizia.jsonl` | 4 cataloghi storici materiali/componenti: vetri 1919, acciaio strutturale 1910, infissi 1895, legname/finiture 1917 (tipologie, dimensioni, prezzi d'epoca) | Public domain |
| `parsed/wiki_storia/wiki_storia_en.jsonl` | Voci EN: storia architettura antica→oggi, storia costruzioni/ingegneria, grattacieli, ponti, dighe, tunnel, biografie (Brunel, Eiffel, Nervi, Freyssinet, maestri 1950-oggi) | CC BY-SA 4.0 |
| `parsed/wiki_storia/wiki_storia_it.jsonl` | Voci IT: la stessa storia in italiano (Brunelleschi, Palladio, razionalismo, INA-Casa, Nervi, Morandi, grattacielo Pirelli…) | CC BY-SA 4.0 |

## Perché questo pack

- **Cultura del progetto**: sapere da dove vengono le tecniche (romana, gotica, rinascimentale,
  industriale) per usarle consapevolmente e citarle con cognizione
- **Spirito critico**: la storia dei successi E dei fallimenti (Pruitt-Igoe, collassi, renewal)
- **Lessico d'epoca**: i cataloghi originali insegnano come si chiamavano e si commercializzavano
  i materiali prima del 1930 — utile per restauro e per riconoscere componenti storici

## Estendere

```bash
python fetch_wiki_storia.py    # riprende e completa le voci Wikipedia (throttling: pazienza)
python serialize_storia.py     # rigenera parsed/ + manifest.json
```

## Escluso di proposito

Le storie dell'architettura moderne in commercio (Frampton, Giedion, Pevsner) sono protette da
copyright — le edizioni pre-1930 e le opere del Governo USA sono la fonte libera equivalente.
Dettagli in `licenze_audit.json`.
