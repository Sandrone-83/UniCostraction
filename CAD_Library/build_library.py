# -*- coding: utf-8 -*-
"""Compila la libreria CAD: catalog.json, catalog.xlsx, README.md."""
import json, os
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

ROOT = os.path.dirname(os.path.abspath(__file__))

CATALOG = [
 # ---------------- STEP / B-Rep / parametrici ----------------
 dict(id="STEP-01", nome="ABC Dataset (Autodesk Research)",
  tipo="Dataset accademico/industriale", url="https://deep-geometry.github.io/abc-dataset/",
  formati=["STEP", "mesh OBJ/STL"], scala="~1.000.000 di modelli CAD reali (chunk da 10k)",
  licenza="MIT (dati); pipeline GPL", dominio="Meccanico / oggetti di design reali (Onshape)",
  geometria="B-Rep solida (solidi manifold) + mesh campionate",
  annotazioni="Filtri geometrici/topologici di qualita'; meta-informazioni sui creatori",
  task_ml="Ricostruzione B-Rep, geometric deep learning, surface segmentation",
  area="Mondiale (utenza Onshape)", verificato=True,
  note="Benchmark standard per CAD ML (CVPR 2019). Geometria industry-grade."),
 dict(id="STEP-02", nome="Fusion 360 Gallery Dataset",
  tipo="Dataset accademico/industriale",
  url="https://github.com/AutodeskAILab/Fusion360GalleryDataset",
  formati=["STEP", "SMT", "OBJ", "JSON sequenze"],
  scala="8.625 design ricostruzione + 8.335 assembly (~58k design totali citati)",
  licenza="Uso ricerca non commerciale", dominio="Meccanico, modelli parametrici reali",
  geometria="B-Rep + albero feature (sketch, estrusioni, booleane) + assembly",
  annotazioni="Sequenze di costruzione complete, sketch con profili, label facce B-Rep",
  task_ml="Text-to-CAD, apprendimento sequenze di modellazione, assembly reasoning",
  area="Mondiale (utenza Fusion 360)", verificato=True, note="741 stelle GitHub."),
 dict(id="STEP-03", nome="DeepCAD",
  tipo="Dataset accademico", url="https://github.com/ChrisWu1997/DeepCAD",
  formati=["JSON sequenze", "STEP (derivati da ABC)"],
  scala="~178.000 modelli con sequenze di costruzione",
  licenza="MIT", dominio="Meccanico",
  geometria="Sequenze sketch+estruso parametriche",
  annotazioni="Storia costruttiva esplicita (operazioni + parametri)",
  task_ml="Modelli sequenza (Transformer) per sintesi CAD, completion",
  area="Hong Kong (HKU) + utenza Onshape", verificato=True, note="830 stelle GitHub."),
 dict(id="STEP-04", nome="SketchGraphs (Princeton LIPS)",
  tipo="Dataset accademico", url="https://github.com/PrincetonLIPS/SketchGraphs",
  formati=["JSON", "grafo vincoli", "binario sequenze"],
  scala="15.000.000 di sketch 2D (~43 GB raw)",
  licenza="MIT (codice); copyright creatori originali (Onshape ToU 1.g.ii)",
  dominio="Meccanico (sketch di modelli reali)",
  geometria="Sketch 2D con vincoli geometrici (grafo entita'-vincoli)",
  annotazioni="Vincoli espliciti (coincident, parallel, distance...), ordine costruttivo",
  task_ml="Autoconstrain, generazione sketch vincolati, program induction",
  area="USA (Princeton/Columbia), dati Onshape mondiali", verificato=True, note="491 stelle."),
 dict(id="STEP-05", nome="NIST MBE PMI Test Cases",
  tipo="Archivio governativo",
  url="https://www.nist.gov/ctl/smart-connected-systems-division/smart-connected-manufacturing-systems-group/mbe-pmi-0",
  formati=["STEP AP203", "STEP AP242"], scala="Decine di test case (FTC, STC, CTC, HTC)",
  licenza="Pubblico dominio (governo USA)", dominio="Meccanico / manifatturiero",
  geometria="Solidi B-Rep con Product & Manufacturing Information",
  annotazioni="PMI semantico e grafico (quote, tolleranze, datumi, fori)",
  task_ml="Comprensione disegni tecnici 3D, GD&T, MBD",
  area="USA (NIST)", verificato=True,
  note="Standard di riferimento CAx-IF; include modelli CATIA/Creo/NX oltre a STEP."),
 dict(id="STEP-06", nome="Better-STEP (University of Victoria)",
  tipo="Dataset accademico",
  url="https://www.frdr-dfdr.ca/repo/dataset/d54b95e0-bc14-4236-b50b-922e5bf4ba7d",
  formati=["HDF5 (derivato da STEP)"], scala="Fusion 360 Gallery + ABC convertiti",
  licenza="Da verificare (FRDR)", dominio="Meccanico",
  geometria="B-Rep in formato HDF5 aperto (senza kernel CAD)",
  annotazioni="Topologia e geometria B-Rep serializzate",
  task_ml="Training su cluster senza licenze CAD kernel",
  area="Canada (University of Victoria)", verificato=True,
  note="Alternativa open a STEP per pipeline di learning su larga scala."),
 dict(id="STEP-07", nome="HistCAD",
  tipo="Dataset accademico", url="https://arxiv.org/abs/2602.19171",
  formati=["STEP", "sequenze parametriche", "render", "testi"],
  scala="162.143 sequenze accademiche + 8.093 modelli industriali",
  licenza="Da verificare", dominio="Meccanico industriale (complessita' reale)",
  geometria="History-based CAD con vincoli (fillet, chamfer, revolve, sweep elicoidali)",
  annotazioni="Sequenze con vincoli, annotazioni testuali generate (Gemma-4-31B)",
  task_ml="CAD agent, modellazione history-based, captioning geometrico",
  area="Internazionale", verificato=True, note="Settembre 2026."),
 dict(id="STEP-08", nome="Text2CAD",
  tipo="Dataset accademico",
  url="https://www.3dcodebench.com/3dcodeverse",
  formati=["sequenze CAD", "caption testuali"],
  scala="~170.000 modelli, ~660.000 caption",
  licenza="CC BY-NC-SA 4.0", dominio="Meccanico",
  geometria="Sequenze sketch+estruso con descrizioni linguistiche",
  annotazioni="Coppie testo-geometria per allineamento visione-linguaggio",
  task_ml="Text-to-CAD supervisionato, allineamento LLM-geometria",
  area="Internazionale", verificato=True,
  note="Tra i pochi dataset con coppie testo<->CAD su larga scala."),
 dict(id="STEP-09", nome="Omni-CAD / CAD-MLLM",
  tipo="Dataset accademico",
  url="https://www.3dcodebench.com/3dcodeverse",
  formati=["multimodale (testo+immagine+punti+comandi)"],
  scala="~450.000 esempi multimodali",
  licenza="MIT", dominio="Meccanico",
  geometria="Coppie cross-modali su sequenze CAD",
  annotazioni="Testo, immagini render, point cloud, sequenze di comandi",
  task_ml="CAD-MLLM multimodale, tool-use per modellazione",
  area="Internazionale", verificato=True),
 dict(id="STEP-10", nome="Zero-to-CAD",
  tipo="Dataset/generatore", url="https://www.3dcodebench.com/3dcodeverse",
  formati=["Codice CadQuery (Python)", "STEP", "STL"],
  scala="~1.000.000 di programmi (100k curati)",
  licenza="Apache-2.0", dominio="Meccanico",
  geometria="Modelli parametrici generati proceduralmente",
  annotazioni="Programma sorgente associato alla geometria",
  task_ml="Code-generation CAD, esecuzione tool LLM",
  area="Internazionale", verificato=True),
 dict(id="STEP-11", nome="GenCAD-Code",
  tipo="Dataset accademico", url="https://www.3dcodebench.com/3dcodeverse",
  formati=["Codice CadQuery", "immagini render"],
  scala="~163.000 coppie immagine-codice",
  licenza="Codice Apache-2.0 (dataset da verificare)", dominio="Meccanico",
  geometria="Coppie render<->programma parametrico",
  annotazioni="Ground truth eseguibile (Codice Python)",
  task_ml="Image-to-CAD, reverse engineering visiva",
  area="Internazionale", verificato=True),
 dict(id="STEP-12", nome="Dataset B-Rep accademici aggiuntivi",
  tipo="Lista curata",
  url="https://github.com/Bigger-and-Stronger/awesome-brep-reconstruction",
  formati=["STEP", "B-Rep"], scala="MFCAD/MFCAD++, WHUCAD, TMCAD, Brep2Seq, Param20K, CC3D(-ops)",
  licenza="Varie (una per dataset)", dominio="Meccanico",
  geometria="B-Rep + feature annotation (MFCAD: feature recognition)",
  annotazioni="Dipende dal dataset (etichette feature, parametri)",
  task_ml="Feature recognition, ricostruzione B-Rep, benchmark comparativi",
  area="Internazionale (UK, Lussemburgo, Cina...)", verificato=True,
  note="MFCAD++: https://pure.qub.ac.uk/en/datasets/mfcad-dataset ; CC3D-ops: https://cvi2.uni.lu/cc3d-ops/"),
 # ---------------- Open hardware (STEP/DXF/DWG reali) ----------------
 dict(id="HW-01", nome="Openwater openmotion-mechanical",
  tipo="Repository GitHub",
  url="https://github.com/OpenwaterHealth/openmotion-mechanical",
  formati=["STEP", "DXF", "DWG", "STL", "PDF"],
  scala="Archivi zip di disegni (custodie, enclosure, profili laser-cut)",
  licenza="AGPL-3.0", dominio="Dispositivo medico (imaging ematico)",
  geometria="Parti meccaniche 3D + disegni 2D di produzione",
  annotazioni="Disegni di produzione, assiemi, documentazione",
  task_ml="Comprensione disegni tecnici 2D/3D, estrazione quote",
  area="USA (Openwater Health)", verificato=True),
 dict(id="HW-02", nome="SparkFun RTK mosaic-X5",
  tipo="Repository GitHub",
  url="https://github.com/sparkfun/SparkFun_RTK_mosaic-X5",
  formati=["STEP", "DXF", "PDF", "Eagle"],
  scala="Disegni case estruso, pannelli frontali/retro, sticker",
  licenza="SparkFun (open hardware, da verificare)", dominio="Elettronica / geodesia",
  geometria="Custodie 3D + disegni 2D per taglio/laser",
  annotazioni="Quote dimensionali, disegni tecnici PDF",
  task_ml="OCR su disegni, estrazione entita' tecniche",
  area="USA (SparkFun)", verificato=True),
 dict(id="HW-03", nome="Virtual AGC - mechanical branch",
  tipo="Repository GitHub",
  url="https://github.com/virtualagc/virtualagc/tree/mechanical",
  formati=["STEP", "DXF"], scala="25 modelli STEP verificati (hardware Apollo AGC/DSKY)",
  licenza="NOASSERTION (progetto misto; modelli di Ron Burkey)",
  dominio="Aerospaziale (storia, replica Apollo)",
  geometria="Parti meccaniche B-Rep da disegni originali MIT/NA",
  annotazioni="Codici disegno originali (es. 1006315A)",
  task_ml="Ricostruzione 3D da disegni tecnici storici",
  area="USA", verificato=True, note="3.237 stelle progetto; campioni scaricati e indicizzati."),
 # ---------------- DXF architettura ----------------
 dict(id="DXF-01", nome="FloorPlanCAD",
  tipo="Dataset accademico", url="https://floorplancad.github.io/",
  formati=["CAD (SVG+PNG derivati)", "annotazioni COCO"],
  scala="15.663 planimetrie reali (release 2021-11-26)",
  licenza="Annotazioni CC BY-NC 4.0; disegni (c) autori originali",
  dominio="Edilizio residenziale + commerciale (mondiale)",
  geometria="Disegni 2D vettoriali con simboli architettonici",
  annotazioni="Panoptic symbol spotting (muri, finestre, ringhiere, 3D shape)",
  task_ml="Riconoscimento simboli, parsing planimetrie, retrieval",
  area="Mondiale (team USTHK/SFU)", verificato=True,
  note="Progetto chiuso inizio 2022; download ancora disponibile."),
 dict(id="DXF-02", nome="CubiCasa5K",
  tipo="Dataset accademico/industriale",
  url="https://github.com/CubiCasa/CubiCasa5k",
  formati=["immagini raster", "SVG vettoriale annotato"],
  scala="5.000 planimetrie, 80+ categorie oggetto",
  licenza="CC BY-NC 4.0 (dati); MIT (codice modello)",
  dominio="Edilizio residenziale (annunci immobiliari, mondiale)",
  geometria="Planimetrie 2D con annotazioni poligonali dense",
  annotazioni="Stanze, muri, porte, finestre, categorie arredo",
  task_ml="Raster-to-vector, floorplan parsing, room classification",
  area="Finlandia (CubiCasa) + dati mondiali", verificato=True, note="592 stelle."),
 dict(id="DXF-03", nome="CubiGraph5K",
  tipo="Dataset accademico", url="https://github.com/luyueheng/CubiGraph5K",
  formati=["JSON grafi", "SVG (derivati)"],
  scala="5.000 grafi di relazione tra stanze",
  licenza="Da verificare (nessuna dichiarata)", dominio="Edilizio",
  geometria="Grafi adiacenza/adiazione stanze da CubiCasa5K",
  annotazioni="Grafo stanze (adiacente/collegata), diametro, conteggi tipologia",
  task_ml="Generazione planimetrie come grafi, graph ML",
  area="Internazionale", verificato=True),
 dict(id="DXF-04", nome="ArchCAD-400K",
  tipo="Dataset accademico",
  url="https://huggingface.co/datasets/jackluoluo/ArchCAD",
  formati=["disegni CAD", "sezioni annotate"],
  scala="5.538 disegni, 413.062 sezioni annotate",
  licenza="Da verificare (Hugging Face)", dominio="Architettura / edilizio",
  geometria="Disegni tecnici architettonici con segmentazione",
  annotazioni="Annotazione fine-grained a livello di sezione",
  task_ml="CAD drawing understanding, VLM su disegni tecnici",
  area="Internazionale", verificato=True),
 dict(id="DXF-05", nome="RUB Floorplan Dataset (MapGeneralization)",
  tipo="Dataset accademico", url="https://github.com/Chrps/MapGeneralization",
  formati=["DXF", "gpickle (grafi)"],
  scala="Dataset pubblico di planimetrie con porte etichettate (AAU)",
  licenza="Accademico (da verificare)", dominio="Edilizio",
  geometria="Primitive DXF + grafi di elementi planimetria",
  annotazioni="Label porte per node classification (ICIP 2021)",
  task_ml="GNN su disegni tecnici, generalizzazione mappe",
  area="Danimarca (Aalborg University)", verificato=True,
  note="Include datasets.pdf con panoramica altri dataset planimetrie."),
 dict(id="DXF-06", nome="RescueForge testdata",
  tipo="Repository GitHub",
  url="https://github.com/NWichter-NeoTube/RescueForge",
  formati=["DXF", "DWG"], scala="15 file test (10 reali + 5 sintetici)",
  licenza="NOASSERTION; fonti documentate in testdata/SOURCES.md",
  dominio="Edilizio (piani antincendio)",
  geometria="Planimetrie DWG/DXF con layer multilingua (EN/DE/FR/ES/VI)",
  annotazioni="Fonti e licenze tracciate per file",
  task_ml="Estrazione entita' (muri/porte/sprinkler), conversione standard",
  area="Germania (hackathon Siemens) + fonti mondiali", verificato=True,
  note="Punta a DWGShare, FloorPlanCAD, ArchCAD, CubiCasa come fonti esterne."),
 dict(id="DXF-07", nome="jscad/sample-files",
  tipo="Repository GitHub", url="https://github.com/jscad/sample-files",
  formati=["DXF"], scala="Set di esempi (floorplan.dxf 1,07 MB / 126.100 righe verificato)",
  licenza="Nessuna licenza dichiarata (da verificare prima dell'uso)",
  dominio="Architettonico + meccanico (esempi di parser)",
  geometria="2D wireframe + blocchi (147 blocchi in floorplan.dxf)",
  annotazioni="Layer nominati (24 layer in floorplan.dxf)",
  task_ml="Test parser DXF, dataset seed per disegni 2D",
  area="Internazionale (OpenJSCAD)", verificato=True,
  note="Campioni scaricati e indicizzati nella libreria."),
 dict(id="DXF-08", nome="ezdxf examples_dxf",
  tipo="Repository GitHub",
  url="https://github.com/mozman/ezdxf/tree/master/examples_dxf",
  formati=["DXF"], scala="40+ file di esempio (R12-2018, verificati 61 voci)",
  licenza="MIT", dominio="Meccanico/tecnico (stress-test di formato)",
  geometria="Entita' avanzate: hatch, mtext, dimensioni, viewport, wipeout",
  annotazioni="Copertura estesa delle specifiche DXF",
  task_ml="Robustezza parser, edge case per training su sintassi DXF",
  area="Austria (Manfred Moitzi)", verificato=True, note="1.447 stelle."),
 dict(id="DXF-09", nome="assimp test models (DXF + 3DS)",
  tipo="Repository GitHub",
  url="https://github.com/assimp/assimp/tree/master/test/models",
  formati=["DXF", "3DS"], scala="test/models: licenza BSD; models-nonbsd: esclusa licenza BSD",
  licenza="BSD (test/models); NONBSD (test/models-nonbsd)",
  dominio="Vari (oggetti, veicoli, personaggi)",
  geometria="Mesh poligonali, wireframe DXF",
  annotazioni="Copertura casi di test del importer",
  task_ml="Conversione formati, benchmark mesh",
  area="Internazionale", verificato=True,
  note="wuson.dxf: mesh 6.939 entita' in blocco; fels.3ds e jeep1.3ds indicizzati."),
 # ---------------- DWG ----------------
 dict(id="DWG-01", nome="LibreDWG test-data",
  tipo="Repository GitHub",
  url="https://github.com/LibreDWG/libredwg/tree/master/test/test-data",
  formati=["DWG", "DXF"], scala="209 file DWG/DXF verificati (R2000, R2004, R2007, R2010+)",
  licenza="GPL-3.0 (toolkit); file di test di varia provenienza",
  dominio="Tecnico generico (entita' 2D/3D, superfici, vincoli)",
  geometria="Entita' AutoCAD per versione (linee, polilinee 3D, spline, hatch, solidi)",
  annotazioni="Coppie DWG/DXF equivalenti per round-trip testing",
  task_ml="Parsing DWG binario, conversione DWG<->DXF, robustezza",
  area="Internazionale (GNU)", verificato=True,
  note="1.609 stelle; campioni R2000/R2004 scaricati e indicizzati."),
 dict(id="DWG-02", nome="DWGShare",
  tipo="Archivio web", url="https://www.dwgshare.com/",
  formati=["DWG"], scala="Catalogo di piani DWG gratuiti (appartamenti, uffici, hotel, scuole, fabbriche)",
  licenza="Download gratuito, licenza non aperta (verificare termini)",
  dominio="Edilizio (mondiale)", geometria="Planimetrie/piante 2D DWG",
  annotazioni="Categorie per tipo di edificio",
  task_ml="Dataset piani edilizi per VLM (con verifica licenze)",
  area="Mondiale", verificato=True,
  note="Segnalato come fonte esterna in RescueForge testdata/SOURCES.md."),
 # ---------------- 3DS ----------------
 dict(id="3DS-01", nome="Autodesk 3ds Max Sample Files",
  tipo="Archivio vendor",
  url="https://www.autodesk.com/support/technical/article/caas/tsarticles/ts/3CM2c0t6Fvo2lSawUNRICT.html",
  formati=["3DS (MAX)"], scala="Pacchetto esempi ufficiale (exe ~1,4 GB)",
  licenza="Proprietaria Autodesk (uso dimostrativo)",
  dominio="Architettonico, design, animazione",
  geometria="Scene 3DS con materiali e animazioni",
  annotazioni="Scene di esempio complete",
  task_ml="Conversione/dataset supervisionato (con verifica licenza)",
  area="USA (Autodesk)", verificato=True),
 dict(id="3DS-02", nome="archive3d.net",
  tipo="Archivio web", url="https://archive3d.net/",
  formati=["3DS"], scala="Raccolta di modelli 3DS gratuiti (edilizio, arredo, oggetti)",
  licenza="Gratuita per uso, termini da verificare per modello",
  dominio="Architettonico / arredo / generico", geometria="Mesh 3DS",
  annotazioni="Categorie e anteprime",
  task_ml="Pre-training mesh 3D (con verifica licenze)",
  area="Mondiale", verificato=True,
  note="Elencato nell'archivio common-3d-test-models."),
 # ---------------- 3DM ----------------
 dict(id="3DM-01", nome="Food4Rhino (McNeel)",
  tipo="Archivio design", url="https://www.food4rhino.com/",
  formati=["3DM"], scala="Raccolta modelli nativi Rhino (componenti architettonici, arredo, definizioni parametriche)",
  licenza="Varia per modello (gratuita/pagata)",
  dominio="Architettonico / design parametrico",
  geometria="NURBS Rhino con layer e naming puliti",
  annotazioni="Layer organizzati, definizioni Grasshopper",
  task_ml="Training NURBS/parametrico Rhino",
  area="Mondiale (comunita' Rhino)", verificato=True),
 dict(id="3DM-02", nome="OpenNURBS / file di esempio McNeel",
  tipo="Repository/toolkit", url="https://github.com/mcneel/opennurbs",
  formati=["3DM"], scala="Toolkit open source per lettura/scrittura 3DM + file di esempio",
  licenza="Licenza openNURBS permissiva (da verificare)",
  dominio="Generico (NURBS)",
  geometria="NURBS, mesh, annotazioni 3DM",
  annotazioni="Specifica del formato documentata",
  task_ml="Parser nativo 3DM per pipeline di training",
  area="USA (McNeel)", verificato=True,
  note="Confermato dalle e-news Rhino (openNURBS open-source)."),
 dict(id="3DM-03", nome="BlockTool (demo urbana)",
  tipo="Repository/dataset", url="https://blocktool.github.io/BlockTool/",
  formati=["3DM", "GH (Grasshopper)"],
  scala="Demo site 3DM + script generazione edifici",
  licenza="Da verificare (GitHub)", dominio="Urbanistica / massing edilizio",
  geometria="Volumi edilizi 2.5D generati da curve Rhino",
  annotazioni="Layer IN/PARKING, parametri di generazione",
  task_ml="Generazione volumetrica assistita",
  area="Internazionale", verificato=True),
 # ---------------- Correlati ----------------
 dict(id="GEN-01", nome="common-3d-test-models",
  tipo="Repository GitHub",
  url="https://github.com/alecjacobson/common-3d-test-models",
  formati=["vari (OBJ + originali)"], scala="~25 modelli storici (Stanford Bunny, Teapot, Fandisk CAD...)",
  licenza="Nessuna dichiarata (fonti documentate)", dominio="Grafica 3D / benchmark",
  geometria="Mesh di riferimento (alcuni da CAD: Fandisk)",
  annotazioni="Provenienza e prima apparizione documentate",
  task_ml="Benchmark comparativi, test di conversione",
  area="Internazionale", verificato=True, note="1.622 stelle."),
 dict(id="GEN-02", nome="Liste curate awesome-cad / awesome-brep-reconstruction",
  tipo="Lista curata",
  url="https://github.com/mlightcad/awesome-cad",
  formati=["riferimento"], scala="Panoramica aggiornata di dataset, tool e kernel CAD open source",
  licenza="MIT", dominio="Riferimento trasversale",
  geometria="-", annotazioni="Categorie: dataset B-Rep, parser DXF/DWG, kernel geometrici",
  task_ml="Scouting fonti", area="Internazionale", verificato=True),
]

# ---------------- scrittura catalog.json ----------------
catalog = {
  "libreria": "CAD-Open-Library per training LLM su modellazione 3D e disegno tecnico",
  "data_compilazione": "2026-09-26",
  "formati_coperti": ["DWG", "DXF", "3DS", "3DM", "STEP"],
  "fonti_totali": len(CATALOG),
  "fonti": CATALOG,
}
with open(os.path.join(ROOT, "catalog.json"), "w", encoding="utf-8") as f:
    json.dump(catalog, f, ensure_ascii=False, indent=2)

# ---------------- samples ----------------
samples = json.load(open(os.path.join(ROOT, "samples_index.json"), encoding="utf-8"))["campioni"]
for s in samples:
    s["dimensione_kb"] = round(s["dimensione_bytes"] / 1024, 1)
with open(os.path.join(ROOT, "samples_index.json"), "w", encoding="utf-8") as f:
    json.dump({"campioni": samples}, f, ensure_ascii=False, indent=2)

# ---------------- xlsx ----------------
wb = Workbook()
ws = wb.active
ws.title = "Catalogo fonti"
HEAD = ["ID", "Nome", "Tipo", "Formati", "Scala", "Licenza", "Dominio",
        "Geometria", "Annotazioni/Metadati", "Task ML", "Area geografica",
        "Verificato", "URL", "Note"]
ws.append(HEAD)
for c in CATALOG:
    ws.append([c["id"], c["nome"], c["tipo"], ", ".join(c["formati"]), c["scala"],
               c["licenza"], c["dominio"], c["geometria"], c["annotazioni"],
               c["task_ml"], c["area"], "si'" if c["verificato"] else "no",
               c["url"], c.get("note", "")])

ws2 = wb.create_sheet("Campioni analizzati")
HEAD2 = ["File", "Formato", "Dim. (KB)", "Fonte repo", "Versione", "Entita'/chunk",
         "Dettagli geometrici", "Layer/Blocchi", "BBox/Vertici"]
ws2.append(HEAD2)
for s in samples:
    ver = s.get("versione_dxf") or s.get("versione_dwg") or s.get("versione_3ds") \
        or (("3DM v%s (%s)" % (s.get("versione_3dm"), s.get("rhino"))) if s.get("versione_3dm") else "") \
        or s.get("schema") or ""
    if s.get("versione_autocad"): ver += " = " + s["versione_autocad"]
    if s.get("rhino") and "3DM v" not in ver: ver = "3DM v%s %s" % (s.get("versione_3dm"), s.get("rhino"))
    ent = s.get("entita_totali") or s.get("entita_step_totali") or s.get("oggetti_mesh") or ""
    det = []
    if s.get("entita_per_tipo"):
        det.append("top: " + ", ".join(f"{k}x{v}" for k, v in list(s["entita_per_tipo"].items())[:6]))
    if s.get("entita_step_totali"):
        top = list(s.get("entita_per_tipo", {}).items())[:6]
        det.append("STEP top: " + ", ".join(f"{k}x{v}" for k, v in top))
    if s.get("vertici_totali") is not None:
        det.append(f"v={s['vertici_totali']}, f={s['facce_totali']}, mat={s['materiali']}")
    if s.get("n_punti_campione"):
        det.append(f"punti campionati={s['n_punti_campione']}")
    lay = []
    if s.get("num_layer") is not None: lay.append(f"layer={s['num_layer']}")
    if s.get("num_blocchi_definiti"): lay.append(f"blocchi={s['num_blocchi_definiti']}")
    if s.get("entita_nel_blocco_mesh"): lay.append(f"entita' blocco={s['entita_nel_blocco_mesh']}")
    bb = ""
    if s.get("bbox"): bb = f"X{s['bbox']['x']} Y{s['bbox']['y']}"
    if s.get("bbox_xyz"): bb = " / ".join(str(a) for a in s["bbox_xyz"])
    ws2.append([s["file"], s.get("formato", ""), s["dimensione_kb"], s["fonte_repo"],
                ver, ent, "; ".join(det), "; ".join(lay), bb])

header_fill = PatternFill("solid", fgColor="1F4E79")
header_font = Font(bold=True, color="FFFFFF", size=10)
thin = Border(*[Side(style="thin", color="B0B0B0")] * 4)
for sheet, widths in ((ws, [9, 34, 20, 16, 34, 26, 26, 30, 34, 30, 22, 10, 46, 40]),
                      (ws2, [36, 20, 10, 14, 22, 12, 52, 26, 40])):
    for j, w in enumerate(widths, 1):
        sheet.column_dimensions[get_column_letter(j)].width = w
    for cell in sheet[1]:
        cell.fill = header_fill; cell.font = header_font
        cell.alignment = Alignment(vertical="center", wrap_text=True)
    for row in sheet.iter_rows(min_row=2):
        for cell in row:
            cell.border = thin
            cell.alignment = Alignment(vertical="top", wrap_text=True)
            cell.font = Font(size=9)
    sheet.freeze_panes = "A2"
    sheet.auto_filter.ref = sheet.dimensions
wb.save(os.path.join(ROOT, "catalog.xlsx"))
print("catalog.json:", len(CATALOG), "fonti |", "catalog.xlsx con 2 fogli |", len(samples), "campioni")
