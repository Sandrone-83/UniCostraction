# -*- coding: utf-8 -*-
"""Aggiunge folder allo zip master, in chunk separati per non superare i timeout."""
import os, sys, zipfile

ROOT = os.path.abspath(os.path.dirname(__file__))
ZIP = os.path.join(ROOT, "UNIVERSITA_EDILIZIA_MASTER.zip")
mode = sys.argv[1]  # 'new' oppure 'add'
folders = sys.argv[2:]
EXCLUDE_EXT = {".7z"}

if mode == "new" and os.path.exists(ZIP):
    os.remove(ZIP)
zf = zipfile.ZipFile(ZIP, "a" if mode == "add" else "w", zipfile.ZIP_DEFLATED)
added = 0
for folder in folders:
    base = os.path.join(ROOT, folder)
    if not os.path.isdir(base):
        continue
    for b, _, files in os.walk(base):
        for fn in files:
            if os.path.splitext(fn)[1].lower() in EXCLUDE_EXT:
                continue
            full = os.path.join(b, fn)
            zf.write(full, os.path.relpath(full, ROOT))
            added += 1
zf.close()
print(f"mode={mode} folders={len(folders)} file aggiunti={added} zip={os.path.getsize(ZIP)/1048576:.1f} MB")
