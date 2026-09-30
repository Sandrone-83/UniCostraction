# -*- coding: utf-8 -*-
"""Estrae in memoria i metadati dal chunk meta ABC e costruisce l'indice
id modello -> {autore, nome documento, data} per il chunk 0000."""
import json, os, re
import py7zr
from py7zr.io import BytesIOFactory

ROOT = os.path.dirname(os.path.abspath(__file__))
ARCH = os.path.join(ROOT, "training_corpus", "abc_chunk", "abc_0000_meta_v00.7z")
OUT = os.path.join(ROOT, "training_corpus", "abc_chunk", "abc_ids_0000.json")

fac = BytesIOFactory(limit=4 * 1024 * 1024)
with py7zr.SevenZipFile(ARCH) as z:
    z.extractall(factory=fac)
print("membri estratti in memoria:", len(fac.products))

def field(txt, key):
    m = re.search(r"^%s:\s*(.+)$" % key, txt, re.M)
    return m.group(1).strip() if m else None

index = {}
for name, bio in fac.products.items():
    try:
        bio.seek(0)
        data = bio.read().decode("utf-8", "replace")
    except Exception:
        continue
    m = re.search(r"([0-9a-f]{8}_[0-9a-f]{24})_metadata", name)
    if not m:
        continue
    model_id = m.group(1)
    author = field(data, "  name") or field(data, "name")
    docname = field(data, "name:")
    created = field(data, "createdAt")
    index[model_id] = {"author": author, "doc_name": docname, "created": created}

print("id indicizzati:", len(index))
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(index, f, ensure_ascii=False, indent=1)
sample = list(index.items())[:3]
for k, v in sample:
    print(k, v)
