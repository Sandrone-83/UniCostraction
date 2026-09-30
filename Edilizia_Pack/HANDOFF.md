# HANDOFF — Istruzioni per Claude Code

Questo archivio (`Edilizia_Pack.zip`) + `CAD_Library.zip` costituiscono il materiale di
addestramento per un LLM del mondo costruzioni (edilizia, progettazione, impiantistica,
sicurezza, appalti, cantiere). Tutto è a licenza commerciale libera, verificata in
`licenze_audit.json`.

## 1. Leggere per primi (in quest'ordine)

1. `README.md` — struttura del pacchetto e formato dei record
2. `licenze_audit.json` — licenza, attribuzione richiesta e URL di ogni fonte
3. `manifest.json` — indice documenti e conteggi
4. Un campione di `parsed/*.jsonl` per vedere il formato training-ready

## 2. Formato dei record (parsed/*.jsonl)

Un JSON per riga, chunk da ~6000 caratteri su confini di paragrafo:

```json
{"doc_id":"...","source":"...","license":"...","commercial_ok":true,
 "attribution":"...","url":"...","title":"...","text":"..."}
```

Campi chiave per l'ingestione:
- `commercial_ok: true` su TUTTI i record — filtro già applicato
- `license` + `attribution` — conservarli nei metadati di training (attribuzione CC BY-SA
  per Wikipedia e per l'edizione INL del D.Lgs 81/08; MIT per i modelli IFC)
- `source` — utile per bilanciare i pesi (es. sotto-campionare `wikipedia_*` se domina)

## 3. Blocchi del corpus

| File | Contenuto | Token stimati |
| --- | --- | --- |
| `parsed/manuali_us_gov.jsonl` | 14 manuali tecnici federali (impianti idraulici, carpenteria metallica, carpenteria edile Navy Builder 3&2, calcestruzzo, dighe, legno, antincendio, rilievo/disegno) | ~3,5 M |
| `parsed/norme_italiane.jsonl` | D.Lgs 81/08 (1466 pp.), NTC 2018 (372 pp.), Circolare 7/2019 (348 pp.), Ord. 3274/2003, DPR 380/01, D.Lgs 36/2023 | ~2,1 M |
| `parsed/ecfr_osha_1926.jsonl` | Regolamento sicurezza cantieri USA, per sezione | ~0,7 M |
| `parsed/ufgs_specs.jsonl` | 46 specifiche edilizie UFGS formato CSI/MasterFormat | ~0,4 M |
| `parsed/design_estetica.jsonl` | 11 trattati classici: Vitruvio, Palladio (IT+EN), Grammar of Ornament, Seven Lamps, Stones of Venice, Dresser, Wharton/Codman, de Wolfe, Eastlake, Radford Cyclopedia (home building) | ~1,2 M |
| `parsed/reports_us_gov.jsonl` | 48 NPS Preservation Briefs (restauro/riabilitazione/manutenzione edilizi storici) + FEMA P-749 sismica | ~0,7 M |
| `parsed/materiali_prezzi.jsonl` | 11 serie PPI mensili 1926-2026 (legname, cemento, calcestruzzo, acciaio, rame, gesso, chimica, minerali) con yoy_pct — prezzi e cicli dei materiali | ~0,25 M |
| `parsed/wiki_construction/wiki_en.jsonl` | 181 voci EN: tecniche + domotica (KNX/BACnet/Zigbee/Matter/MQTT/BMS), materiali e finiture, design/stili/designers, comfort, economia | ~1,8 M |
| `parsed/wiki_construction/wiki_it.jsonl` | 92 voci IT: terminologia edile, norme, figure professionali + domotica, materiali/finiture, design/maestri italiani, comfort, prezzi | ~1,0 M |
| `raw/bim_ifc/ifc_models/*.ifc` | 6 edifici BIM (IFC2X3) — addestramento parsing/serializzazione BIM, non testo libero | — |

## 4. Completamenti automatici (script inclusi, riprendibili)

Da eseguire nella root del pacchetto scompattato. Ogni script salta ciò che è già fatto.

```bash
# a. Wikipedia: alcune voci saltate per throttling 429 (Wikimedia limita gli IP):
#    rilanciare finché non dà "mancanti: 0" (gli script riprendono da soli)
python fetch_wiki_corpus.py        # EN + IT (primo giro: tecniche/cantiere)
python fetch_wiki_materiale_design.py  # EN + IT (secondo giro: domotica, materiali, design, comfort, prezzi)
python fetch_wiki_it_only.py       # solo IT, attese più lunghe

# a2. Prezzi materiali: le serie FRED si aggiornano mensilmente — riscaricare i CSV
#     con lo stesso pattern https://fred.stlouisfed.org/graph/fredgraph.csv?id=<ID>
#     (lista ID in serialize_edilizia.py → dict FRED), poi:
python serialize_edilizia.py

# b. Altre specifiche UFGS: il catalogo completo (1.582 sezioni) è in
#    discovery/wbdg_all.json — aggiungere numeri di sezione alla lista SEZIONI in
#    fetch_ufgs.py, poi:
python fetch_ufgs.py
python extract_ufgs_text.py

# c. Nuovi PDF normativi/tecnici (es. FEMA, USACE — link in licenze_audit.json):
python extract_pdf_text.py <file.pdf>   # riprendibile, scrive .txt in raw/norme_it/

# d. Rigenerare parsed/ + manifest.json dopo ogni aggiunta:
python serialize_edilizia.py
```

## 5. Regole d'oro licenze

- NON aggiungere: Eurocodici, norme UNI/EN, codici ICC, prezzari (RSMeans/DEI/BCIS),
  Engineering LibreTexts / MIT OCW / NPTEL (clausola NC), documentazioni Home Assistant
  e ESPHome (CC BY-NC-SA 4.0, verificato sui LICENSE.md dei repo) — elenco completo in
  `licenze_audit.json` → `fonti_escluse_per_licenza`
- Testi normativi italiani = atti pubblici (art. 5 L.633/1941): liberi anche commercialmente
- Opere Governo federale USA = public domain (17 U.S.C. § 105)
- CC BY-SA richiede attribuzione: è già nel campo `attribution` di ogni record

## 6. CAD_Library.zip (pacchetto gemello)

- `catalog.json` — 33 fonti dati CAD (ABC Dataset, DeepCAD, Fusion 360 Gallery…) con licenze
- `training_corpus/parsed/` — 141 JSONL già serializzati (DXF/STEP/DWG/3DS/3DM, 32.252 righe)
- `training_corpus/packed/` — pacchetti train/eval già impacchettati (~9,9 M token)
- `samples/` — 16 file CAD reali + `samples_index.json` con specifiche geometriche
- `download_abc_full.py` — completa i 10.000 modelli STEP dell'ABC Dataset
  (richiede ~13 min di download continuo; il server NYU non ammette resume)
- `analyze_samples.py` — parser DXF/STEP/DWG/3DS/3DM riutilizzabili nel tuo software

## 7. Suggerimento pipeline

1. Ingestire `parsed/*.jsonl` così come sono (già chunkati)
2. Per i file IFC: parser dedicato (IfcOpenShell, LGPL — uso consentito) → serializzare
   entità/facce in testo strutturato prima del training
3. Tenere `licenze_audit.json` come registro di provenienza per audit futuri
