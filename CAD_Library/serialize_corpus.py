# -*- coding: utf-8 -*-
"""Serializza il corpus CAD in rappresentazioni testuali per il training di un LLM.
Per ogni documento produce un file .jsonl in training_corpus/parsed/:
  riga 1: {"kind":"doc", ...}   metadati documento (fonte, licenza, formato, versione,
                                layer, entita', bbox)
  righe successive: {"kind":"entity"/"mesh"/"histogram", ...} geometria strutturata.
Inoltre compila manifest.jsonl (licenza, token stimati, split train/eval)."""
import json, os, re, struct, hashlib
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(ROOT, "training_corpus", "raw")
PARSED = os.path.join(ROOT, "training_corpus", "parsed")
MANIFEST = os.path.join(ROOT, "training_corpus", "manifest.jsonl")

# classi di licenza per lo split
PERMISSIVE = {"MIT", "BSD"}
RESEARCH = {"GPL-3.0 (progetto); file di test di varia provenienza"}

# ---------------- DXF ----------------
GEO_TYPES = {"LINE","LWPOLYLINE","POLYLINE","CIRCLE","ARC","ELLIPSE","SPLINE","TEXT","MTEXT",
             "INSERT","HATCH","DIMENSION","POINT","3DFACE","SOLID","LEADER","MLEADER","RAY",
             "XLINE","MLINE","VERTEX","ATTDEF","ATTRIB","SHAPE","MESH","HELIX","BODY","REGION",
             "WIPEOUT","IMAGE","VIEWPORT","TOLERANCE"}

def parse_dxf_records(path):
    txt = open(path, encoding="ascii", errors="replace").read()
    lines = [l.strip() for l in txt.splitlines()]
    if len(lines) % 2: lines = lines[:-1]
    pairs = [(lines[i], lines[i+1]) for i in range(0, len(lines), 2)]
    m = re.search(r"\$ACADVER\s*\n\s*1\s*\n\s*(AC\d{4})", txt)
    version = m.group(1) if m else None
    section = None; records = []; cur = None; cur_codes = None
    layers = set(); blocks = 0
    def flush():
        nonlocal cur, cur_codes
        if cur and cur_codes is not None:
            records.append((section_hint, cur, cur_codes))
        cur = None; cur_codes = None
    section_hint = None
    for code, val in pairs:
        if code == "2" and val in ("HEADER","ENTITIES","TABLES","BLOCKS","OBJECTS"):
            section = val; flush(); continue
        if code == "0" and val == "ENDSEC":
            section = None; flush(); continue
        if section == "TABLES":
            if code == "2" and val not in ("LAYER",): pass
            continue
        if code == "0":
            flush()
            if val in GEO_TYPES or val in ("BLOCK","SEQEND"):
                cur = val; cur_codes = defaultdict(list); section_hint = section
                if val == "BLOCK": blocks += 1
            continue
        if cur_codes is not None:
            cur_codes[code].append(val)
            if cur == "LAYER" and code == "2":
                layers.add(val)
    flush()
    return version, layers, blocks, records

def num(v, default=None):
    try: return float(v)
    except (TypeError, ValueError): return default

def entity_json(etype, c):
    e = {"kind": "entity", "type": etype}
    if etype == "LINE":
        e.update(layer=(c.get("8") or [None])[0], x1=num((c.get("10") or [0])[0]),
                 y1=num((c.get("20") or [0])[0]), x2=num((c.get("11") or [0])[0]),
                 y2=num((c.get("21") or [0])[0]))
    elif etype in ("CIRCLE", "ARC"):
        e.update(layer=(c.get("8") or [None])[0], cx=num((c.get("10") or [0])[0]),
                 cy=num((c.get("20") or [0])[0]), r=num((c.get("40") or [0])[0]))
        if etype == "ARC":
            e.update(a1=num((c.get("50") or [0])[0]), a2=num((c.get("51") or [0])[0]))
    elif etype == "ELLIPSE":
        e.update(layer=(c.get("8") or [None])[0], cx=num((c.get("10") or [0])[0]),
                 cy=num((c.get("20") or [0])[0]), ax=num((c.get("11") or [0])[0]),
                 ay=num((c.get("21") or [0])[0]), ratio=num((c.get("40") or [0])[0]))
    elif etype in ("LWPOLYLINE",):
        xs = [num(v) for v in c.get("10", [])]; ys = [num(v) for v in c.get("20", [])]
        e.update(layer=(c.get("8") or [None])[0],
                 n=min(len(xs), len(ys)), closed=bool(int(num((c.get("70") or [0])[0]) or 0) & 1))
        e["bbox"] = [[min(xs), max(xs)], [min(ys), max(ys)]] if xs and ys else None
    elif etype in ("TEXT", "MTEXT"):
        e.update(layer=(c.get("8") or [None])[0], text=(c.get("1") or [""])[0][:200],
                 x=num((c.get("10") or [0])[0]), y=num((c.get("20") or [0])[0]),
                 h=num((c.get("40") or [0])[0]))
    elif etype == "INSERT":
        e.update(layer=(c.get("8") or [None])[0], block=(c.get("2") or [None])[0],
                 x=num((c.get("10") or [0])[0]), y=num((c.get("20") or [0])[0]),
                 sx=num((c.get("41") or [1])[0]), sy=num((c.get("42") or [1])[0]),
                 rot=num((c.get("50") or [0])[0]))
    elif etype == "SPLINE":
        xs = [num(v) for v in c.get("10", [])]; ys = [num(v) for v in c.get("20", [])]
        e.update(layer=(c.get("8") or [None])[0], degree=num((c.get("71") or [0])[0]),
                 n_ctrl=min(len(xs), len(ys)), n_fit=len(c.get("11", [])))
        e["bbox"] = [[min(xs), max(xs)], [min(ys), max(ys)]] if xs and ys else None
    elif etype == "POINT":
        e.update(layer=(c.get("8") or [None])[0], x=num((c.get("10") or [0])[0]),
                 y=num((c.get("20") or [0])[0]))
    elif etype in ("HATCH",):
        e.update(layer=(c.get("8") or [None])[0], pattern=(c.get("2") or [None])[0],
                 n_paths=num((c.get("91") or [0])[0]))
    elif etype == "DIMENSION":
        e.update(layer=(c.get("8") or [None])[0], dimtype=(c.get("1") or [None])[0],
                 x=num((c.get("10") or [0])[0]), y=num((c.get("20") or [0])[0]))
    else:
        e.update(layer=(c.get("8") or [None])[0])
    return {k: v for k, v in e.items() if v is not None}

def serialize_dxf(src, rel, source, lic, out_f):
    version, layers, n_blocks, records = parse_dxf_records(src)
    ents = [r for r in records if r[1] in GEO_TYPES and r[1] != "VERTEX"]
    hist = Counter(r[1] for r in ents)
    xs = []; ys = []
    for _, et, c in ents:
        for cx_ in ("10", "11"):
            for v in c.get(cx_, []):
                f = num(v)
                if f is not None: xs.append(f)
        for cy_ in ("20", "21"):
            for v in c.get(cy_, []):
                f = num(v)
                if f is not None: ys.append(f)
    doc = {"kind": "doc", "format": "DXF", "version": version, "file": rel,
           "source": source, "license": lic, "n_entities": len(ents),
           "entity_histogram": dict(hist.most_common(20)), "n_layers": len(layers),
           "layers": sorted(layers)[:30], "n_block_defs": n_blocks,
           "bbox": [[round(min(xs),3), round(max(xs),3)], [round(min(ys),3), round(max(ys),3)]]
           if xs and ys else None}
    out_f.write(json.dumps(doc, ensure_ascii=False) + "\n")
    n = 0
    for _, et, c in ents:
        out_f.write(json.dumps(entity_json(et, c), ensure_ascii=False) + "\n")
        n += 1
        if n >= 20000:  # tetto di sicurezza per file enormi
            break
    return doc

# ---------------- STEP ----------------
def serialize_step(src, rel, source, lic, out_f):
    txt = open(src, encoding="ascii", errors="replace").read()
    m = re.search(r"FILE_NAME\((?:\s|/\*.*?\*/)*'([^']*)'", txt, re.S)
    fname = m.group(1) if m else None
    m = re.search(r"FILE_SCHEMA\s*\(\s*\(\s*'([^']*)'", txt, re.S)
    schema = m.group(1) if m else None
    hist = Counter(re.findall(r"^#\d+\s*=\s*([A-Z_0-9]+)", txt, re.M))
    pts = re.findall(r"CARTESIAN_POINT\s*\(\s*'[^']*',\s*\(([^)]*)\)", txt)
    xs=[]; ys=[]; zs=[]
    for p in pts:
        try:
            cc = [float(v) for v in p.split(",")]
            if len(cc)==3: xs.append(cc[0]); ys.append(cc[1]); zs.append(cc[2])
        except ValueError: pass
    doc = {"kind": "doc", "format": "STEP", "file": rel, "source": source,
           "license": lic, "step_file_name": fname, "schema": schema,
           "n_entities": sum(hist.values()),
           "entity_histogram": dict(hist.most_common(25)),
           "bbox_xyz": [[round(min(xs),3), round(max(xs),3)],
                        [round(min(ys),3), round(max(ys),3)],
                        [round(min(zs),3), round(max(zs),3)]] if xs else None,
           "n_points_sampled": len(xs)}
    out_f.write(json.dumps(doc, ensure_ascii=False) + "\n")
    # istogramma come righe di apprendimento (testo <-> conteggio)
    out_f.write(json.dumps({"kind": "histogram", "entities": dict(hist.most_common(60))},
                           ensure_ascii=False) + "\n")
    return doc

# ---------------- 3DS ----------------
def serialize_3ds(src, rel, source, lic, out_f):
    data = open(src, "rb").read()
    magic, _, ver = struct.unpack("<HIH", data[:8]) if len(data) >= 8 else (0, 0, 0)
    start = data.find(b"==", 8)
    if start < 0: start = 8
    objects = []
    def walk(pos, end):
        while pos + 6 <= end:
            cid, ln = struct.unpack("<HI", data[pos:pos+6])
            if ln < 6 or pos + ln > len(data): break
            body, sub_end = pos + 6, pos + ln
            if cid == 0x4000:
                try: name_end = data.index(0, body, sub_end)
                except ValueError: name_end = body
                name = data[body:name_end].decode("ascii", "replace")
                obj = {"name": name, "vertices": [], "faces": [], "materials": []}
                walk_obj(name_end + 1, sub_end, obj)
                objects.append(obj)
            elif cid in (0x3D3D, 0x4D4D, 0xB000):
                walk(body, sub_end)
            pos = sub_end
    def walk_obj(pos, end, obj):
        while pos + 6 <= end:
            cid, ln = struct.unpack("<HI", data[pos:pos+6])
            if ln < 6 or pos + ln > len(data): break
            body, sub_end = pos + 6, pos + ln
            if cid == 0x4110:
                nv = struct.unpack("<H", data[body:body+2])[0]
                fl = struct.unpack("<%df" % (nv*3), data[body+2:body+2+nv*12])
                obj["vertices"] = [[round(fl[i*3],4), round(fl[i*3+1],4), round(fl[i*3+2],4)]
                                   for i in range(nv)]
            elif cid == 0x4120:
                nf = struct.unpack("<H", data[body:body+2])[0]
                fc = struct.unpack("<%dH" % (nf*4), data[body+2:body+2+nf*8])
                obj["faces"] = [[fc[i*4], fc[i*4+1], fc[i*4+2]] for i in range(nf)]
            elif cid == 0x4130:
                ln2 = data.index(0, body, sub_end)
                obj["materials"].append(data[body:ln2].decode("ascii", "replace"))
            elif cid == 0x4100:
                walk_obj(body, sub_end, obj)
            pos = sub_end
    walk(start, len(data))
    doc = {"kind": "doc", "format": "3DS", "file": rel, "source": source,
           "license": lic, "version": ver, "n_objects": len(objects),
           "n_vertices": sum(len(o["vertices"]) for o in objects),
           "n_faces": sum(len(o["faces"]) for o in objects)}
    out_f.write(json.dumps(doc, ensure_ascii=False) + "\n")
    for o in objects:
        out_f.write(json.dumps({"kind": "mesh", "name": o["name"], "n_vertices": len(o["vertices"]),
                                "n_faces": len(o["faces"]), "materials": o["materials"],
                                "vertices": o["vertices"], "faces": o["faces"]},
                               ensure_ascii=False) + "\n")
    return doc

# ---------------- 3DM / DWG: metadati header ----------------
def serialize_3dm(src, rel, source, lic, out_f):
    data = open(src, "rb").read(64)
    m = re.match(rb"3D Geometry File Format\s*(\d+)", data)
    doc = {"kind": "doc", "format": "3DM", "file": rel, "source": source, "license": lic,
           "version_3dm": int(m.group(1)) if m else None,
           "note": "binario NURBS: usare openNURBS per la serializzazione completa"}
    out_f.write(json.dumps(doc, ensure_ascii=False) + "\n")
    return doc

def serialize_dwg(src, rel, source, lic, out_f):
    with open(src, "rb") as f: head = f.read(64)
    ver = head[:6].decode("ascii", "replace")
    doc = {"kind": "doc", "format": "DWG", "file": rel, "source": source, "license": lic,
           "version": ver,
           "note": "binario DWG: convertire in DXF con LibreDWG/ODA per il testo"}
    out_f.write(json.dumps(doc, ensure_ascii=False) + "\n")
    return doc

SERIALIZERS = {".dxf": serialize_dxf, ".stp": serialize_step, ".step": serialize_step,
               ".3ds": serialize_3ds, ".3dm": serialize_3dm, ".dwg": serialize_dwg}

# ---------------- raccolta documenti ----------------
SOURCES = {  # (cartella, source, licenza)
    "libredwg": ("LibreDWG/libredwg", "GPL-3.0 (progetto); file di test di varia provenienza"),
    "ezdxf": ("mozman/ezdxf", "MIT"),
    "assimp": ("assimp/assimp (test/models, BSD)", "BSD"),
    "ladybug": ("ladybug-tools/3d-models", "MIT"),
}
docs = []
for folder, (source, lic) in SOURCES.items():
    base = os.path.join(RAW, folder)
    for dp, _, fns in os.walk(base):
        for fn in sorted(fns):
            src = os.path.join(dp, fn)
            rel = os.path.relpath(src, RAW).replace("\\", "/")
            ext = os.path.splitext(fn)[1].lower()
            if ext in SERIALIZERS:
                docs.append((src, rel, source, lic))

# campioni licenza-pulita della libreria principale
EXTRA = [
    ("samples/dxf_ezdxf_text.dxf", "mozman/ezdxf", "MIT"),
    ("samples/dxf_ezdxf_hatches_1.dxf", "mozman/ezdxf", "MIT"),
    ("samples/dxf_assimp_wuson.dxf", "assimp/assimp (test/models, BSD)", "BSD"),
    ("samples/dxf_libredwg_TS1.dxf", "LibreDWG/libredwg", "GPL-3.0 (progetto); file di test di varia provenienza"),
    ("samples/step_ladybug_EPalOriginal01.stp", "ladybug-tools/3d-models", "MIT"),
    ("samples/dwg_libredwg_TS1_R2000.dwg", "LibreDWG/libredwg", "GPL-3.0 (progetto); file di test di varia provenienza"),
    ("samples/dwg_libredwg_entities2d_R2000.dwg", "LibreDWG/libredwg", "GPL-3.0 (progetto); file di test di varia provenienza"),
    ("samples/dwg_libredwg_Surface_R2004.dwg", "LibreDWG/libredwg", "GPL-3.0 (progetto); file di test di varia provenienza"),
    ("samples/3dm_ladybug_Book_Case.3dm", "ladybug-tools/3d-models", "MIT"),
    ("samples/3dm_ladybug_heart_signet.3dm", "ladybug-tools/3d-models", "MIT"),
    ("samples/3ds_assimp_fels.3ds", "assimp/assimp (test/models, BSD)", "BSD"),
]
for rel, source, lic in EXTRA:
    src = os.path.join(ROOT, rel)
    if os.path.exists(src):
        docs.append((src, rel.replace("samples/", "samples/"), source, lic))

manifest = []
for src, rel, source, lic in docs:
    ext = os.path.splitext(src)[1].lower()
    dest = os.path.join(PARSED, re.sub(r"[^A-Za-z0-9_.-]", "_", rel) + ".jsonl")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    try:
        with open(dest, "w", encoding="utf-8") as out_f:
            doc = SERIALIZERS[ext](src, rel, source, lic, out_f)
    except Exception as e:
        print("ERRORE serializzazione", rel, e)
        continue
    raw_size = os.path.getsize(src)
    parsed_size = os.path.getsize(dest)
    token_est = (raw_size + parsed_size) // 4
    lic_class = "permissive" if lic in PERMISSIVE else ("research" if lic in RESEARCH else "check")
    split = "eval" if int(hashlib.md5(rel.encode()).hexdigest(), 16) % 20 == 0 else "train"
    manifest.append({"file": rel, "parsed": os.path.relpath(dest, ROOT).replace("\\","/"),
                     "format": doc.get("format"), "source": source, "license": lic,
                     "license_class": lic_class, "bytes_raw": raw_size,
                     "bytes_parsed": parsed_size, "tokens_est": token_est,
                     "n_entities": doc.get("n_entities"), "split": split})

with open(MANIFEST, "w", encoding="utf-8") as f:
    for m in manifest:
        f.write(json.dumps(m, ensure_ascii=False) + "\n")

tot_tokens = sum(m["tokens_est"] for m in manifest)
by_fmt = Counter(m["format"] for m in manifest)
by_class = Counter(m["license_class"] for m in manifest)
print("documenti:", len(manifest))
print("per formato:", dict(by_fmt))
print("per classe licenza:", dict(by_class))
print("split:", dict(Counter(m["split"] for m in manifest)))
print("token stimati (raw+parsed)/4:", tot_tokens)
print("dim. raw totale MB:", round(sum(m['bytes_raw'] for m in manifest)/1048576, 1))
print("dim. parsed totale MB:", round(sum(m['bytes_parsed'] for m in manifest)/1048576, 1))
