#!/usr/bin/env python3
"""
download_abc_full.py — Completa il download del chunk STEP 0000 dell'ABC Dataset.

Perché esiste questo script:
    Il server archive.nyu.edu NON supporta richieste HTTP Range (nessun resume),
    quindi il download va fatto in un'unica sessione continua (~10-13 min a
    ~2-2,7 MB/s). Un agente con chiamate limitate a 300 secondi non ce la fa:
    per questo lo lasciamo a voi da eseguire, ad esempio con:

        python CAD_Library/download_abc_full.py

Cosa fa:
    1. Rimuove il file parziale esistente (incompleto, inutilizzabile).
    2. Scarica in streaming abc_0000_step_v00.7z (1.594.129.754 byte attesi)
       con retry e riavvio automatico da zero se il server tronca lo stream.
    3. Verifica dimensione e MD5 (695388be7a278c7798c8c8ae239772ac).
    4. Estrae i 10.000 file .step in CAD_Library/training_corpus/abc_chunk/step000/
       con py7zr (pip install py7zr).
    5. (Opzionale, --serialize) lancia la pipeline di serializzazione esistente
       CAD_Library/training_corpus/serialize_corpus.py sui file estratti.
"""

import argparse
import hashlib
import os
import sys
import time
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(HERE, "training_corpus", "abc_chunk")
ARCHIVE = os.path.join(OUT_DIR, "abc_0000_step_v00.7z")
URL = "https://archive.nyu.edu/rest/bitstreams/88598/retrieve"
EXPECTED_SIZE = 1594129754
EXPECTED_MD5 = "695388be7a278c7798c8c8ae239772ac"


def download(max_retries: int = 5) -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    if os.path.exists(ARCHIVE):
        print(f"[info] rimuovo file parziale esistente: {ARCHIVE}", flush=True)
        os.remove(ARCHIVE)

    for attempt in range(1, max_retries + 1):
        try:
            print(f"[download] tentativo {attempt}/{max_retries} da {URL}", flush=True)
            req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0"})
            t0 = time.time()
            got = 0
            with urllib.request.urlopen(req, timeout=60) as r, open(ARCHIVE + ".part", "wb") as f:
                while True:
                    block = r.read(1 << 20)  # 1 MB
                    if not block:
                        break
                    f.write(block)
                    got += len(block)
                    if got % (100 << 20) < (1 << 20):  # ogni ~100 MB
                        mbps = got / (time.time() - t0) / 1e6
                        print(f"  {got/1e6:,.0f} MB / {EXPECTED_SIZE/1e6:,.0f} MB "
                              f"({mbps:.1f} MB/s)", flush=True)
            if got != EXPECTED_SIZE:
                raise IOError(f"stream troncato: {got} byte, attesi {EXPECTED_SIZE}")
            os.replace(ARCHIVE + ".part", ARCHIVE)
            print(f"[ok] download completo: {got:,} byte in "
                  f"{time.time() - t0:.0f}s", flush=True)
            return
        except Exception as e:
            print(f"[errore] {e}", flush=True)
            if os.path.exists(ARCHIVE + ".part"):
                os.remove(ARCHIVE + ".part")
            if attempt < max_retries:
                wait = 30 * attempt
                print(f"[download] riprovo tra {wait}s...", flush=True)
                time.sleep(wait)
            else:
                sys.exit("Download fallito dopo tutti i tentativi. "
                         "Verifica la connessione e rilancia.")


def verify() -> None:
    print("[verify] calcolo MD5 (può richiedere un minuto)...", flush=True)
    h = hashlib.md5()
    with open(ARCHIVE, "rb") as f:
        for block in iter(lambda: f.read(1 << 22), b""):
            h.update(block)
    digest = h.hexdigest()
    size = os.path.getsize(ARCHIVE)
    print(f"[verify] size: {size:,} (atteso {EXPECTED_SIZE:,})", flush=True)
    print(f"[verify] md5 : {digest} (atteso {EXPECTED_MD5})", flush=True)
    if size != EXPECTED_SIZE or digest != EXPECTED_MD5:
        sys.exit("Verifica fallita: file corrotto. Rilancia lo script per riprovare.")
    print("[ok] verifica superata.", flush=True)


def extract() -> None:
    import py7zr  # pip install py7zr
    target = os.path.join(OUT_DIR, "step000")
    if os.path.isdir(target):
        print(f"[info] cartella già estratta: {target}", flush=True)
        return
    os.makedirs(target, exist_ok=True)
    print(f"[extract] estrazione in {target} ...", flush=True)
    t0 = time.time()
    with py7zr.SevenZipFile(ARCHIVE, "r") as z:
        z.extractall(target)
    n = sum(1 for _ in os.scandir(target))
    print(f"[ok] estratti {n} file .step in {time.time() - t0:.0f}s", flush=True)


def main() -> None:
    ap = argparse.ArgumentParser(description="Completa il chunk STEP 0000 dell'ABC Dataset")
    ap.add_argument("--no-download", action="store_true",
                    help="salta il download (usa il .7z già presente)")
    ap.add_argument("--no-extract", action="store_true", help="salta l'estrazione")
    ap.add_argument("--serialize", action="store_true",
                    help="dopo l'estrazione lancia serialize_corpus.py sui file STEP")
    args = ap.parse_args()

    if not args.no_download:
        download()
    verify()
    if not args.no_extract:
        extract()
    if args.serialize:
        print("[pipeline] lancio serialize_corpus.py ...", flush=True)
        os.system(f'python "{os.path.join(HERE, "training_corpus", "serialize_corpus.py")}"')
    print("\nFatto. I 10.000 modelli STEP sono in:", flush=True)
    print("  " + os.path.join(OUT_DIR, "step000"), flush=True)


if __name__ == "__main__":
    main()
