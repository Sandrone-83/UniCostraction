# -*- coding: utf-8 -*-
"""Crea Edilizia_Pack.zip e Training_Completo.zip (4 pack) e li copia sul Desktop."""
import os, shutil, zipfile

WS = r"C:\Users\alessandro\Documents\kimi\tasks\2026-09-26\15-14-07-e3d653af"
DESK = r"C:\Users\alessandro\Desktop"
SKIP_EXT = (".pdf", ".zip", ".prog", ".req", ".pyc")

def make_zip(src_dir, zip_path):
    if os.path.exists(zip_path):
        os.remove(zip_path)
    zf = zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED, compresslevel=6)
    n = 0
    for root, dirs, files in os.walk(src_dir):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for fn in files:
            if fn.lower().endswith(SKIP_EXT):
                continue
            full = os.path.join(root, fn)
            arc = os.path.join(os.path.basename(src_dir), os.path.relpath(full, src_dir))
            zf.write(full, arc); n += 1
    zf.close()
    bad = zipfile.ZipFile(zip_path).testzip()
    print(f"{os.path.basename(zip_path)}: {n} file, {os.path.getsize(zip_path)//1024} KB, testzip={'OK' if bad is None else 'ERR '+str(bad)}")
    return zip_path

# 1) Edilizia_Pack
p1 = make_zip(os.path.join(WS, "Edilizia_Pack"), os.path.join(WS, "Edilizia_Pack.zip"))
shutil.copy(p1, os.path.join(DESK, "Edilizia_Pack.zip"))

# 2) Italia_Sistema_Pack
p2 = make_zip(os.path.join(WS, "Italia_Sistema_Pack"), os.path.join(WS, "Italia_Sistema_Pack.zip"))
shutil.copy(p2, os.path.join(DESK, "Italia_Sistema_Pack.zip"))

# 2b) Digitale_Marketing_Pack
p2b = make_zip(os.path.join(WS, "Digitale_Marketing_Pack"), os.path.join(WS, "Digitale_Marketing_Pack.zip"))
shutil.copy(p2b, os.path.join(DESK, "Digitale_Marketing_Pack.zip"))

# 2c) Coding_Master_Pack
p2c = make_zip(os.path.join(WS, "Coding_Master_Pack"), os.path.join(WS, "Coding_Master_Pack.zip"))
shutil.copy(p2c, os.path.join(DESK, "Coding_Master_Pack.zip"))

# 2d) Coding_Master_Pack_2
p2d = make_zip(os.path.join(WS, "Coding_Master_Pack_2"), os.path.join(WS, "Coding_Master_Pack_2.zip"))
shutil.copy(p2d, os.path.join(DESK, "Coding_Master_Pack_2.zip"))

# 2e) Coding_Master_Pack_3
p2e = make_zip(os.path.join(WS, "Coding_Master_Pack_3"), os.path.join(WS, "Coding_Master_Pack_3.zip"))
shutil.copy(p2e, os.path.join(DESK, "Coding_Master_Pack_3.zip"))

# 2f) Coding_Master_Pack_4
p2f = make_zip(os.path.join(WS, "Coding_Master_Pack_4"), os.path.join(WS, "Coding_Master_Pack_4.zip"))
shutil.copy(p2f, os.path.join(DESK, "Coding_Master_Pack_4.zip"))

# 2g) Coding_Master_Pack_5
p2g = make_zip(os.path.join(WS, "Coding_Master_Pack_5"), os.path.join(WS, "Coding_Master_Pack_5.zip"))
shutil.copy(p2g, os.path.join(DESK, "Coding_Master_Pack_5.zip"))

# 2h) Coding_Master_Pack_TOTALE = i 5 pack coding in uno
ct = os.path.join(WS, "Coding_Master_Pack_TOTALE.zip")
if os.path.exists(ct):
    os.remove(ct)
zc = zipfile.ZipFile(ct, "w", zipfile.ZIP_STORED)
for pack in ("Coding_Master_Pack.zip", "Coding_Master_Pack_2.zip", "Coding_Master_Pack_3.zip", "Coding_Master_Pack_4.zip", "Coding_Master_Pack_5.zip"):
    zc.write(os.path.join(WS, pack), pack)
zc.close()
bad = zipfile.ZipFile(ct).testzip()
print(f"Coding_Master_Pack_TOTALE.zip: {os.path.getsize(ct)//1024} KB, testzip={'OK' if bad is None else 'ERR '+str(bad)}")
shutil.copy(ct, os.path.join(DESK, "Coding_Master_Pack_TOTALE.zip"))

# 3) Training_Completo = 11 pack
tc = os.path.join(WS, "Training_Completo.zip")
if os.path.exists(tc):
    os.remove(tc)
zf = zipfile.ZipFile(tc, "w", zipfile.ZIP_STORED)
for pack in ("Edilizia_Pack.zip", "CAD_Library.zip", "Fondamenti_Pack.zip", "Storia_Pack.zip", "Italia_Sistema_Pack.zip", "Digitale_Marketing_Pack.zip", "Coding_Master_Pack.zip", "Coding_Master_Pack_2.zip", "Coding_Master_Pack_3.zip", "Coding_Master_Pack_4.zip", "Coding_Master_Pack_5.zip"):
    src = os.path.join(WS, pack)
    if not os.path.exists(src):
        src = os.path.join(DESK, pack)
    zf.write(src, pack)
zf.close()
bad = zipfile.ZipFile(tc).testzip()
print(f"Training_Completo.zip: {os.path.getsize(tc)//1024} KB, testzip={'OK' if bad is None else 'ERR '+str(bad)}")
shutil.copy(tc, os.path.join(DESK, "Training_Completo.zip"))
print("copiati sul Desktop")
