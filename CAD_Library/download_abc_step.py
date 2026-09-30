# -*- coding: utf-8 -*-
"""Scarica i 10.000 file STEP del chunk ABC 0000 da GitHub Pages (CDN).
Ripristinabile: salta i file gia' presenti. Uso: python download_abc_step.py"""
import json, os, time, urllib.request, concurrent.futures, threading

ROOT = os.path.dirname(os.path.abspath(__file__))
IDS = json.load(open(os.path.join(ROOT, "training_corpus", "abc_chunk", "abc_ids_0000.json"), encoding="utf-8"))
DEST_DIR = os.path.join(ROOT, "training_corpus", "raw", "abc")
os.makedirs(DEST_DIR, exist_ok=True)
BASE = "https://deep-geometry.github.io/abc-dataset/data/%s_step_000.step"

lock = threading.Lock()
done = fail = 0

def fetch(model_id):
    global done, fail
    dest = os.path.join(DEST_DIR, model_id + ".step")
    if os.path.exists(dest) and os.path.getsize(dest) > 200:
        with lock: done += 1
        return True
    url = BASE % model_id
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "abc-training-corpus"})
            data = urllib.request.urlopen(req, timeout=30).read()
            if len(data) < 200:
                raise IOError("file troppo piccolo")
            with open(dest, "wb") as f:
                f.write(data)
            with lock: done += 1
            return True
        except Exception:
            time.sleep(1 + attempt)
    with lock: fail += 1
    return False

ids = sorted(IDS.keys())
t0 = time.time()
with concurrent.futures.ThreadPoolExecutor(max_workers=16) as ex:
    for i, ok in enumerate(ex.map(fetch, ids)):
        if (i + 1) % 500 == 0:
            el = time.time() - t0
            print("%d/%d | ok=%d falliti=%d | %.0fs (%.1f file/s)" %
                  (i + 1, len(ids), done, fail, el, (i + 1) / el), flush=True)
print("FINE | scaricati+presenti:", done, "| falliti:", fail, "| tempo: %.0fs" % (time.time() - t0))
