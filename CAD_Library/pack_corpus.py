# -*- coding: utf-8 -*-
"""Impacca il corpus in file di testo pronti per il training.
Per ogni documento: blocco di intestazione (fonte, licenza, formato) + testo grezzo
(se leggibile: DXF/STEP) + serializzazione strutturata JSONL.
Split per classe di licenza: permissive (MIT/BSD) separato da research."""
import json, os

ROOT = os.path.dirname(os.path.abspath(__file__))
CORPUS = os.path.join(ROOT, "training_corpus")
PACKED = os.path.join(CORPUS, "packed")
os.makedirs(PACKED, exist_ok=True)

manifest = [json.loads(l) for l in open(os.path.join(CORPUS, "manifest.jsonl"), encoding="utf-8")]
TEXT_EXT = (".dxf", ".stp", ".step")

def doc_block(m):
    if m["file"].startswith("samples/"):
        raw_path = os.path.join(ROOT, m["file"])
    else:
        raw_path = os.path.join(CORPUS, "raw", m["file"])
    parts = ["# " + "-" * 60,
             "# file: %s" % m["file"],
             "# format: %s | source: %s | license: %s" % (m["format"], m["source"], m["license"]),
             "# entities: %s | tokens_est: %s" % (m["n_entities"], m["tokens_est"]),
             "# " + "-" * 60]
    if os.path.exists(raw_path) and raw_path.lower().endswith(TEXT_EXT):
        try:
            parts.append(open(raw_path, encoding="ascii", errors="replace").read())
        except Exception:
            pass
    parsed_path = os.path.join(ROOT, m["parsed"])
    if os.path.exists(parsed_path):
        parts.append(open(parsed_path, encoding="utf-8").read())
    return "\n".join(parts) + "\n\n"

groups = {}
for m in manifest:
    key = (m["split"], m["license_class"])
    groups.setdefault(key, []).append(m)

summary = {}
for (split, lic_class), items in sorted(groups.items()):
    name = "%s_%s.txt" % (split, lic_class)
    out = os.path.join(PACKED, name)
    chars = 0
    with open(out, "w", encoding="utf-8") as f:
        for m in sorted(items, key=lambda x: x["file"]):
            block = doc_block(m)
            f.write(block); chars += len(block)
    summary[name] = {"documenti": len(items), "caratteri": chars, "token_stimati": chars // 4}
    print(name, summary[name])

with open(os.path.join(PACKED, "pack_summary.json"), "w", encoding="utf-8") as f:
    json.dump(summary, f, ensure_ascii=False, indent=2)
print("\nTotale token stimati:", sum(v["token_stimati"] for v in summary.values()))
