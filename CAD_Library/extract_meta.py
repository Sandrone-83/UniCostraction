# -*- coding: utf-8 -*-
"""Completa l'estrazione dei file yml mancanti dal chunk meta ABC."""
import py7zr, os

ROOT = os.path.dirname(os.path.abspath(__file__))
DEST = os.path.join(ROOT, "training_corpus", "abc_chunk", "meta000")
ARCH = os.path.join(ROOT, "training_corpus", "abc_chunk", "abc_0000_meta_v00.7z")

with py7zr.SevenZipFile(ARCH) as z:
    names = [n for n in z.getnames() if n.endswith(".yml")]
    have = set()
    for dp, _, fns in os.walk(DEST):
        for fn in fns:
            have.add(os.path.relpath(os.path.join(dp, fn), DEST).replace(os.sep, "/"))
    missing = [n for n in names if n not in have]
    print("nomi nel chunk:", len(names), "| gia' presenti:", len(have), "| mancanti:", len(missing))
    for i in range(0, len(missing), 2000):
        z.extract(DEST, targets=missing[i:i+2000])
        print("estratti", min(i + 2000, len(missing)), "/", len(missing), flush=True)
print("fine")
