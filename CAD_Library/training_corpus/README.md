# Training Corpus CAD — materiale di apprendimento per LLM

**Compilato il:** 26 settembre 2026 · 141 documenti · ~10,3 milioni di token stimati
**Doppia rappresentazione:** testo grezzo dei formati nativi (DXF ASCII, STEP ISO 10303) + serializzazione strutturata JSONL con geometria parsata entità per entità.

## Struttura

```
training_corpus/
├── raw/                  130 file originali scaricati dalle fonti (DXF, STEP, 3DS)
├── parsed/               141 file .jsonl (1 per documento): doc-header + entità/mesh/istogrammi
├── packed/               corpus impaccato pronto per il trainer:
│   ├── train_permissive.txt   (68 documenti, ~2,29M token — MIT/BSD, uso libero)
│   ├── train_research.txt     (65 documenti, ~7,56M token — GPL test-data, solo ricerca)
│   ├── eval_permissive.txt    (2 documenti, ~55k token)
│   ├── eval_research.txt      (6 documenti, ~428k token)
│   └── pack_summary.json
├── manifest.jsonl        metadati per documento: fonte, licenza, classe licenza,
│                         formato, byte, token stimati, split train/eval
└── README.md             questo file
```

## Fonti incluse (con classificazione licenze)

| Fonte | Licenza | Classe | Documenti | Note |
|---|---|---|---|---|
| mozman/ezdxf `examples_dxf` | MIT | permissive | 46 | copertura completa entità DXF (hatch, mtext, dimensioni, viewport) |
| assimp/assimp `test/models` | BSD | permissive | 14 | DXF mesh + 3DS con vertici/facce serializzati |
| ladybug-tools/3d-models | MIT | permissive | 7 | STEP bancali EPAL (AP214 AUTOMOTIVE_DESIGN) + header 3DM |
| LibreDWG `test/test-data` | GPL-3.0 (progetto) | research | 71 | 67 DXF versioni R14→R2018 + DWG (metadati header) |
| campioni libreria (MIT/BSD/GPL) | — | misto | 3 | TS1.dxf, wuson, fels |

**Esclusi per igiene di licenza:** jscad/sample-files (nessuna licenza dichiarata), assimp `models-nonbsd`, virtualagc (NOASSERTION), 3ds_assimp_jeep1.3ds.

## Formato della serializzazione JSONL

Ogni documento in `parsed/` inizia con una riga `doc` (metadati + istogramma entità + bounding box), seguita da:

- **DXF** — una riga `entity` per entità con geometria decodificata:
  `LINE` → x1,y1,x2,y2 · `CIRCLE/ARC` → cx,cy,r,(angoli) · `LWPOLYLINE/SPLINE` → bbox, n punti, closed · `TEXT/MTEXT` → testo, posizione, altezza · `INSERT` → blocco, posizione, scala, rotazione · `HATCH` → pattern, n percorsi · `DIMENSION` → tipo, punto
- **STEP** — riga `histogram` con conteggi entità ISO 10303 (ADVANCED_FACE, EDGE_CURVE, B_SPLINE_SURFACE...) + bbox dai punti campionati
- **3DS** — una riga `mesh` per oggetto: nome, vertici [[x,y,z]...], facce [[a,b,c]...], materiali
- **DWG/3DM** — riga `doc` con versione formato (es. AC1015=R2000, 3DM v50=Rhino 5) e nota di conversione

## Come usare il corpus

1. **Pre-training puro:** `packed/train_*.txt` — ogni documento ha intestazione commentata (`# file/format/license`) seguita dal testo nativo e dalla geometria JSONL.
2. **Training supervisionato strutturato:** leggere `parsed/*.jsonl` via `manifest.jsonl` — ogni entità è un record JSON con campi tipizzati; adatto a target di tipo "predici la prossima entità" o "genera la sequenza DXF".
3. **Filtraggio per licenza:** `manifest.jsonl` campo `license_class` — `permissive` per uso commerciale, `research` solo per ricerca.
4. **Split:** train/eval assegnato deterministicamente (hash del percorso, 5% eval).

## Rigenerazione

```
python download_corpus.py    # riscarica i raw (idempotente)
python serialize_corpus.py   # rigenera parsed/ + manifest.jsonl
python pack_corpus.py        # rigenera packed/
```

Parser disponibili anche in `../analyze_samples.py` (DXF/STEP/DWG/3DS/3DM).
Fonti aggiuntive pronte da aggiungere (vedi `../catalog.json`): DeepCAD, SketchGraphs, Fusion 360 Gallery, NIST — richiedono download esterno dei dataset (link nel catalogo).

### ABC Dataset — chunk STEP 0000 (in completamento)

La libreria include già l'indice dei **10.000 modelli STEP del chunk 0000** dell'ABC Dataset
(`abc_chunk/abc_ids_0000.json`: id → autore e metadati), estratto dal chunk meta ufficiale.

Il chunk STEP vero e proprio (`abc_0000_step_v00.7z`, 1,59 GB, 10.000 file `.step`) non è
stato scaricabile in sessione perché il server archive.nyu.edu non supporta il resume HTTP
(lo stream a ~2-2,7 MB/s supera il limite di 300 s per chiamata). Per completarlo:

```bash
python ../download_abc_full.py            # download + md5 + estrazione
python ../download_abc_full.py --serialize  # e poi serializzazione in parsed/
```

Lo script verifica dimensione e MD5 (`695388be7a278c7798c8c8ae239772ac`), estrae con py7zr
in `abc_chunk/step000/` e può lanciare la pipeline di serializzazione esistente.
