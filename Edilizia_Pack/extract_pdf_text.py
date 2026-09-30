#!/usr/bin/env python3
"""extract_pdf_text.py — estrae testo da un PDF in raw/norme_it -> .txt (RIPRENDIBILE).
Uso: python extract_pdf_text.py <nomefile.pdf>
Riprende dalla pagina successiva all'ultima completata (file .prog)."""
import os, sys, time
from pypdf import PdfReader

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw", "norme_it")
fn = sys.argv[1]
src = os.path.join(RAW, fn)
dst = os.path.join(RAW, os.path.splitext(fn)[0] + ".txt")
prog = dst + ".prog"
t0 = time.time()
r = PdfReader(src)
n = len(r.pages)
start = 0
if os.path.exists(prog):
    start = int(open(prog).read().strip() or 0)
if start >= n:
    print(f"[ok] gia' completo: {n} pagine"); sys.exit(0)
out = open(dst, "a", encoding="utf-8") if start else open(dst, "w", encoding="utf-8")
for i in range(start, n):
    try: t = r.pages[i].extract_text() or ""
    except Exception: t = ""
    out.write(f"\n\n=== [pagina {i+1}/{n}] ===\n\n{t}")
    if (i + 1) % 25 == 0:
        out.flush()
        open(prog, "w").write(str(i + 1))
        print(f"  {i+1}/{n} pagine, {time.time()-t0:.0f}s", flush=True)
out.flush(); open(prog, "w").write(str(n))
out.close()
os.remove(prog)
print(f"[ok] {n} pagine -> {dst} ({os.path.getsize(dst):,} byte) in {time.time()-t0:.0f}s")
