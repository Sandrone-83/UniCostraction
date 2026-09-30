# CAD Open Library — Dataset di file CAD per training LLM su modellazione 3D e disegno tecnico

**Data di compilazione:** 26 settembre 2026
**Formati coperti:** DWG · DXF · 3DS · 3DM · STEP
**Fonti indicizzate:** 33 (dataset accademici, repository GitHub, archivi di design, archivi governativi) — ricerca a livello mondiale, qualsiasi tipologia di struttura edilizia e non.

---

## 1. Cos'è questa libreria

Una libreria indicizzata di **fonti open source / pubbliche di file CAD**, con:

- `catalog.json` — catalogo machine-readable delle 33 fonti con specifiche e metadati (formato, scala, licenza, dominio, tipo di geometria, annotazioni, task ML consigliati, area geografica);
- `catalog.xlsx` — lo stesso catalogo in Excel (foglio *Catalogo fonti*), più il foglio *Campioni analizzati* con le specifiche geometriche dei file scaricati;
- `samples/` — 16 file di esempio effettivamente scaricati dai repository (6 DXF, 3 STEP, 3 DWG, 2 3DM, 2 3DS), 5,4 MB totali;
- `samples_index.json` — specifiche geometriche estratte dai campioni (versioni formato, conteggi entità/chunk, layer, blocchi, bounding box);
- `analyze_samples.py` — parser leggeri usati per l'estrazione (DXF ASCII, STEP ISO 10303, header DWG, chunk 3DS, header OpenNURBS 3DM), riutilizzabili sulla raccolta completa;
- `discovery/` — risposte grezze delle API GitHub usate per il rilievo (strutture ad albero, metadati ufficiali licenze/stelle).

## 2. Panoramica per formato

### STEP (solidi B-Rep — il nucleo per il 3D tecnico)
| Fonte | Scala | Licenza |
|---|---|---|
| ABC Dataset | ~1.000.000 modelli | MIT |
| Fusion 360 Gallery | 8.6k ricostruzioni + 8.3k assembly | ricerca non commerciale |
| DeepCAD | ~178k sequenze | MIT |
| SketchGraphs | 15M sketch vincolati | MIT / ToU Onshape |
| NIST MBE PMI | decine di test case AP203/AP242 | pubblico dominio |
| Text2CAD | ~170k modelli + 660k caption | CC BY-NC-SA 4.0 |
| Omni-CAD / Zero-to-CAD / GenCAD-Code | 450k / 1M / 163k | MIT / Apache-2.0 |
| HistCAD (2026) | 162k sequenze + 8k industriali | da verificare |

### DXF (disegno tecnico 2D — edilizio e meccanico)
- **Architettura:** FloorPlanCAD (15.663 planimetrie), CubiCasa5K (5.000), CubiGraph5K (grafi stanze), ArchCAD-400K (5.538 disegni annotati), RUB Floorplan Dataset, DWGShare (piani edilizi).
- **Tecnico/meccanico e test:** ezdxf `examples_dxf` (MIT), jscad/sample-files, assimp test models, RescueForge `testdata` (fonti tracciate in SOURCES.md).

### DWG (formato nativo AutoCAD, binario)
- **LibreDWG test-data** — 209 file DWG/DXF verificati, versioni R2000→R2018, con coppie DWG↔DXF equivalenti.
- **DWGShare** — catalogo gratuito di piani edilizi (licenza non aperta, da verificare).
- I file DWG reali si ottengono in genere convertendo DXF con ODA File Converter o LibreDWG (`dwg2dxf`/`dxf2dwg`).

### 3DS (mesh storiche)
- assimp test models (BSD / non-BSD separati), Autodesk 3ds Max Sample Files, archive3d.net.

### 3DM (NURBS Rhinoceros)
- Food4Rhino (McNeel), OpenNURBS + file di esempio, BlockTool (demo urbana), ladybug-tools/3d-models (MIT, verificato).

## 3. Campioni scaricati e specifiche geometriche

| File | Formato | Versione | Specifiche |
|---|---|---|---|
| dxf_jscad_floorplan.dxf | DXF | AC1018 (AutoCAD 2004) | 970 entità, 24 layer, 147 blocchi, area bbox 4.581.753 |
| dxf_jscad_splines.dxf | DXF | AC1021 (AutoCAD 2007) | 2 entità spline |
| dxf_ezdxf_text.dxf | DXF | AC1032 (AutoCAD 2018) | 229 entità, 5 blocchi |
| dxf_ezdxf_hatches_1.dxf | DXF | AC1032 | 32 entità (hatch) |
| dxf_assimp_wuson.dxf | DXF | — | mesh da 6.939 entità in blocco |
| dxf_libredwg_TS1.dxf | DXF | AC1015 (AutoCAD 2000) | 45 entità, 11 blocchi |
| step_virtualagc_1006315A.stp | STEP | AP214 | 5.255 entità ISO 10303 |
| step_virtualagc_1006340C.stp | STEP | AP214 | 635 entità |
| step_ladybug_EPalOriginal01.stp | STEP | — | 3.314 entità (bancale EPAL) |
| dwg_libredwg_TS1_R2000.dwg | DWG | AC1015 (R2000) | 418 KB |
| dwg_libredwg_entities2d_R2000.dwg | DWG | AC1015 | 24 KB |
| dwg_libredwg_Surface_R2004.dwg | DWG | AC1018 (R2004) | 163 KB |
| 3dm_ladybug_Book_Case.3dm | 3DM | v4 (Rhino 4) | 687 KB |
| 3dm_ladybug_heart_signet.3dm | 3DM | v50 (Rhino 5) | 546 KB |
| 3ds_assimp_fels.3ds | 3DS | v2 | 1 oggetto, 386 vertici, 768 facce |
| 3ds_assimp_jeep1.3ds | 3DS | v2 | 7 oggetti, 1.948 vertici, 2.032 facce |

## 4. Note sulle licenze (fondamentali per il training)

- **Utilizzabili liberamente (permissive):** ABC, DeepCAD, SketchGraphs (con attribuzione), ezdxf, ladybug-tools, Omni-CAD, Zero-to-CAD, OpenNURBS, NIST (pubblico dominio USA).
- **Solo ricerca / non commerciale:** Fusion 360 Gallery, FloorPlanCAD, CubiCasa5K, Text2CAD, assimp `models-nonbsd`.
- **Da verificare prima dell'uso in training commerciale:** jscad/sample-files (nessuna licenza dichiarata), assimp (NOASSERTION a livello di repository), virtualagc, DWGShare, archive3d.net, Food4Rhino (per modello).
- Per un LLM destinato a uso commerciale: **privilegiare MIT/Apache/BSD/pubblico dominio** e tenere i dataset CC-NC in un split di ricerca separato.

## 5. Roadmap suggerita per il training

1. **Pre-training testuale/strutturale:** serializzare STEP/DXF in rappresentazioni testuali (es. Better-STEP HDF5, s-expression B-Rep, dump DXF per coppie codice/valore) — parser già pronti in `analyze_samples.py`.
2. **Supervisionato text→geometria:** Text2CAD, Omni-CAD, Zero-to-CAD (coppie testo-programma).
3. **Sequenze di modellazione:** DeepCAD, Fusion 360 Gallery, HistCAD (sketch→estruso→fillet con parametri).
4. **Disegno tecnico 2D edilizio:** FloorPlanCAD + CubiCasa5K + RUB (planimetrie, simboli, grafi stanze) — ottimo per VLM su disegni architettonici.
5. **DWG:** usare LibreDWG/ODA per normalizzare a DXF prima del parsing.
6. **3DS/3DM:** assimp per la conversione mesh; OpenNURBS per il parsing nativo NURBS.

## 6. Training corpus (pronto all'uso)

La sottocartella `training_corpus/` contiene il materiale di apprendimento compilato: 141 documenti (raw + JSONL strutturato + packed) con manifest per licenza e split train/eval — vedi `training_corpus/README.md`.

## 7. Estensione della libreria

Il rilievo è replicabile: gli script in `discovery/` e le chiamate alle API GitHub (`git/trees?recursive=1`) permettono di aggiornare il catalogo e scaricare in blocco nuovi repository. Liste curate di riferimento per lo scouting: `mlightcad/awesome-cad`, `Bigger-and-Stronger/awesome-brep-reconstruction`.
