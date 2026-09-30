# -*- coding: utf-8 -*-
"""Analizza i campioni CAD scaricati e produce specifiche geometriche + metadati.
Parser leggeri: DXF ASCII (coppie codice/valore), STEP (testo ISO 10303),
DWG (versione dall'header binario), 3DS (walk ricorsivo dei chunk), 3DM (header OpenNURBS)."""
import json, os, re, struct
from collections import Counter, OrderedDict

SAMPLES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "samples")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "samples_index.json")

DXF_KNOWN = {"LINE","LWPOLYLINE","POLYLINE","CIRCLE","ARC","ELLIPSE","SPLINE","TEXT","MTEXT",
             "INSERT","HATCH","DIMENSION","POINT","3DFACE","SOLID","TRACE","MLINE","LEADER",
             "MLEADER","RAY","XLINE","VERTEX","SEQEND","VIEWPORT","IMAGE","WIPEOUT","HELIX",
             "REGION","BODY","TOLERANCE","ATTDEF","ATTRIB","SHAPE","MESH","SECTION"}
PT_ENTITIES = {"LINE","LWPOLYLINE","POLYLINE","CIRCLE","ARC","ELLIPSE","SPLINE","TEXT","MTEXT",
               "INSERT","POINT","3DFACE","SOLID","HATCH","DIMENSION","LEADER","MLEADER",
               "VERTEX","RAY","XLINE","ATTDEF","ATTRIB","SHAPE","MESH","HELIX","BODY","REGION"}

def dxf_pairs(txt):
    lines = [l.strip() for l in txt.splitlines()]
    if len(lines) % 2:
        lines = lines[:-1]
    return [(lines[i], lines[i+1]) for i in range(0, len(lines), 2)]

def parse_dxf(path):
    info = {"formato": "DXF", "encoding": "ASCII"}
    txt = open(path, encoding="ascii", errors="replace").read()
    pairs = dxf_pairs(txt)
    m = re.search(r"\$ACADVER\s*\n\s*1\s*\n\s*(AC\d{4})", txt)
    if m:
        info["versione_dxf"] = m.group(1)
    section = None; ent = Counter(); blk_ent = Counter(); blocks = set()
    layers = set(); pending_layer = False
    xmin = ymin = float("inf"); xmax = ymax = float("-inf")
    cur = None; pend_x = None; cen = None
    def upd(x, y):
        nonlocal xmin, ymin, xmax, ymax
        xmin = min(xmin, x); xmax = max(xmax, x)
        ymin = min(ymin, y); ymax = max(ymax, y)
    for code, val in pairs:
        if code == "2" and val in ("HEADER", "ENTITIES", "TABLES", "BLOCKS", "OBJECTS"):
            section = val; continue
        if code == "0" and val == "ENDSEC":
            section = None; continue
        if section == "TABLES":
            if code == "0" and val == "LAYER":
                pending_layer = True
            elif pending_layer and code == "2":
                layers.add(val); pending_layer = False
            continue
        if section == "BLOCKS":
            if code == "0" and val == "BLOCK":
                cur = "__block__"; continue
            if code == "0":
                if val in DXF_KNOWN:
                    blk_ent[val] += 1
                cur = val if val in PT_ENTITIES else None
                pend_x = None; cen = None
                continue
            if code == "2" and cur == "__block__":
                blocks.add(val); cur = None; continue
            if cur in PT_ENTITIES:
                if code in ("10", "11"):
                    try: pend_x = float(val)
                    except ValueError: pend_x = None
                elif code in ("20", "21") and pend_x is not None:
                    try: upd(pend_x, float(val)); pend_x = None
                    except ValueError: pass
            continue
        if section == "ENTITIES":
            if code == "0":
                cur = val if val in DXF_KNOWN else None
                pend_x = None; cen = None
                if cur:
                    ent[cur] += 1
                continue
            if cur in PT_ENTITIES:
                if code in ("10", "11"):
                    try: pend_x = float(val)
                    except ValueError: pend_x = None
                elif code in ("20", "21") and pend_x is not None:
                    try:
                        y = float(val); upd(pend_x, y)
                        if cur in ("CIRCLE", "ARC", "ELLIPSE"):
                            cen = (pend_x, y)
                        pend_x = None
                    except ValueError: pass
                elif cur in ("CIRCLE", "ARC") and code == "40" and cen is not None:
                    try:
                        r = float(val)
                        upd(cen[0]-r, cen[1]-r); upd(cen[0]+r, cen[1]+r)
                    except ValueError: pass
    info["entita_totali"] = sum(ent.values())
    info["entita_per_tipo"] = dict(ent.most_common(15))
    if blk_ent:
        info["entita_nel_blocco_mesh"] = sum(blk_ent.values())
        info["entita_blocco_per_tipo"] = dict(blk_ent.most_common(10))
        info["num_blocchi_definiti"] = len(blocks)
    info["num_layer"] = len(layers)
    info["layer_top"] = sorted(layers)[:8]
    if xmin != float("inf"):
        info["bbox"] = {"x": [round(xmin, 3), round(xmax, 3)],
                        "y": [round(ymin, 3), round(ymax, 3)]}
        info["area_bbox"] = round((xmax - xmin) * (ymax - ymin), 1)
    return info

STEP_KEYS = ["MANIFOLD_SOLID_BREP", "BREP_WITH_VOIDS", "ADVANCED_FACE", "EDGE_CURVE",
             "CARTESIAN_POINT", "DIRECTION", "CYLINDRICAL_SURFACE", "PLANE",
             "SPHERICAL_SURFACE", "TOROIDAL_SURFACE", "B_SPLINE_SURFACE", "B_SPLINE_CURVE",
             "LINE", "CIRCLE", "ELLIPSE", "SURFACE_CURVE", "SEAM_CURVE", "CLOSED_SHELL",
             "OPEN_SHELL", "FACETED_BREP", "NEXT_ASSEMBLY_USAGE_OCCURRENCE"]

def parse_step(path):
    info = {"formato": "STEP"}
    txt = open(path, encoding="ascii", errors="replace").read()
    m = re.search(r"FILE_NAME\(\s*'([^']*)'", txt)
    info["file_name_step"] = m.group(1) if m else None
    m = re.search(r"FILE_SCHEMA\(\s*\(\s*'([^']*)'", txt)
    info["schema"] = m.group(1) if m else None
    counts = Counter()
    for k in STEP_KEYS:
        c = len(re.findall(r"#\d+\s*=\s*" + k + r"\b", txt))
        if c:
            counts[k] = c
    info["entita_step_totali"] = len(re.findall(r"^#\d+\s*=", txt, re.M))
    info["entita_per_tipo"] = dict(counts.most_common())
    pts = re.findall(r"CARTESIAN_POINT\s*\(\s*'[^']*',\s*\(([^)]*)\)", txt)
    xs = []; ys = []; zs = []
    for p in pts:
        try:
            c = [float(v) for v in p.split(",")]
            if len(c) == 3:
                xs.append(c[0]); ys.append(c[1]); zs.append(c[2])
        except ValueError:
            pass
    if xs:
        info["bbox_xyz"] = [[round(min(xs), 3), round(max(xs), 3)],
                            [round(min(ys), 3), round(max(ys), 3)],
                            [round(min(zs), 3), round(max(zs), 3)]]
        info["n_punti_campione"] = len(xs)
    return info

def parse_dwg(path):
    info = {"formato": "DWG"}
    with open(path, "rb") as f:
        head = f.read(64)
    ver = head[:6].decode("ascii", errors="replace")
    info["versione_dwg"] = ver
    info["versione_autocad"] = {"AC1015": "AutoCAD 2000", "AC1018": "AutoCAD 2004",
        "AC1021": "AutoCAD 2007", "AC1024": "AutoCAD 2010", "AC1027": "AutoCAD 2013",
        "AC1028": "AutoCAD 2014", "AC1032": "AutoCAD 2018", "AC1033": "AutoCAD 2019",
        "AC1034": "AutoCAD 2022", "AC1035": "AutoCAD 2023"}.get(ver, "sconosciuta")
    return info

def parse_3ds(path):
    info = {"formato": "3DS"}
    data = open(path, "rb").read()
    if len(data) >= 8:
        magic, _, ver = struct.unpack("<HIH", data[:8])
        info["magic_ok"] = (magic == 0x4D4D)
        info["versione_3ds"] = ver
    objs = 0; faces = 0; verts = 0; mats = 0
    CONTAINERS = {0x4D4D, 0x3D3D, 0x4100, 0xAFFF, 0xB000}
    # i file v2 hanno un preambolo di 8 byte dopo la versione: si parte dal
    # primo chunk editore (0x3D3D) trovato nell'intestazione
    start = data.find(b"==", 8)
    if start < 0:
        start = 8
    def walk(pos, end):
        nonlocal objs, faces, verts, mats
        while pos + 6 <= end:
            cid, ln = struct.unpack("<HI", data[pos:pos+6])
            if ln < 6 or pos + ln > len(data):
                break
            body = pos + 6; sub_end = pos + ln
            if cid == 0x4000:
                objs += 1
                try:
                    name_end = data.index(0, body, sub_end)
                except ValueError:
                    name_end = body
                walk(name_end + 1, sub_end)
            elif cid == 0x4110:
                try:
                    verts += struct.unpack("<H", data[body:body+2])[0]
                except struct.error:
                    pass
            elif cid == 0x4120:
                try:
                    faces += struct.unpack("<H", data[body:body+2])[0]
                except struct.error:
                    pass
            elif cid == 0xAFFF:
                mats += 1
                walk(body, sub_end)
            elif cid in CONTAINERS:
                walk(body, sub_end)
            pos = sub_end
    walk(start, len(data))
    info["oggetti_mesh"] = objs
    info["vertici_totali"] = verts
    info["facce_totali"] = faces
    info["materiali"] = mats
    return info

def parse_3dm(path):
    info = {"formato": "3DM (OpenNURBS/Rhino)"}
    data = open(path, "rb").read(64)
    if data[:3] == b"3DM" or data.startswith(b"3D Geometry File Format"):
        info["magic_ok"] = True
        m = re.match(rb"3D Geometry File Format\s*(\d+)", data)
        if m:
            v = m.group(1).decode()
            info["versione_3dm"] = int(v)
            info["rhino"] = {"4": "Rhinoceros 4.x", "50": "Rhinoceros 5.x",
                             "60": "Rhinoceros 6.x", "70": "Rhinoceros 7.x",
                             "80": "Rhinoceros 8.x"}.get(v, "versione storica")
    else:
        info["magic_ok"] = False
    return info

PARSERS = {".dxf": parse_dxf, ".stp": parse_step, ".step": parse_step,
           ".dwg": parse_dwg, ".3ds": parse_3ds, ".3dm": parse_3dm}

index = []
for fn in sorted(os.listdir(SAMPLES)):
    ext = os.path.splitext(fn)[1].lower()
    path = os.path.join(SAMPLES, fn)
    rec = OrderedDict()
    rec["file"] = fn
    rec["dimensione_bytes"] = os.path.getsize(path)
    rec["fonte_repo"] = fn.split("_")[0]
    if ext in PARSERS:
        try:
            rec.update(PARSERS[ext](path))
        except Exception as e:
            rec["errore_analisi"] = str(e)
    index.append(rec)

json.dump({"campioni": index}, open(OUT, "w", encoding="utf-8"),
          ensure_ascii=False, indent=2)
for r in index:
    extra = " | ".join(f"{k}={v}" for k, v in r.items()
                       if k not in ("file", "formato", "dimensione_bytes", "fonte_repo",
                                    "entita_per_tipo", "entita_blocco_per_tipo",
                                    "layer_top", "bbox", "bbox_xyz", "encoding") and v is not None)
    print(f"{r['file']:44s} {r.get('formato','?'):22s} {r['dimensione_bytes']:>9d} B  {extra}")
print("\nSalvato:", OUT)
