#!/usr/bin/env python3
"""serialize_edilizia.py — converte tutto il materiale grezzo di Edilizia_Pack in JSONL
pronti per l'addestramento, con licenza e attribuzione per ogni record.

Output:
  parsed/manuals_us_gov.jsonl   manuali federali USA (public domain)
  parsed/ecfr_osha_1926.jsonl   regolamento sicurezza cantieri OSHA (public domain)
  parsed/norme_italiane.jsonl   normativa edilizia italiana (atti pubblici)
  parsed/ifc_bim_index.jsonl    indice modelli IFC con metadati (MIT)
"""
import json, os, re, glob

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw")
OUT = os.path.join(HERE, "parsed")
os.makedirs(OUT, exist_ok=True)

CHUNK = 6000      # caratteri per chunk
OVERLAP = 250     # sovrapposizione fra chunk contigui

# ---------------------------------------------------------------- metadati fonti
MANUALS = {
    "DTIC_ADA442216": ("UFC 3-600-01 - Fire Protection Engineering for Facilities", "U.S. DoD Unified Facilities Criteria", "2006", "https://archive.org/details/DTIC_ADA442216"),
    "DTIC_ADA530875": ("UFC 4-171-05 - Army Reserve Facilities", "U.S. DoD Unified Facilities Criteria", "2005/2010", "https://archive.org/details/DTIC_ADA530875"),
    "DTIC_ADA531892": ("Cost Savings Using Stirrup Reinforcement Instead of Standard Reinforcement", "US Army Corps of Engineers ERDC", "2010", "https://archive.org/details/DTIC_ADA531892"),
    "wood_handbook_USDA": ("Wood Handbook - Wood as an Engineering Material (FPL-GTR-190)", "USDA Forest Service, Forest Products Laboratory", "2010", "https://archive.org/details/wood-handbook"),
    "utilitiesmani024854mbp": ("Utilitiesman 1 (NAVEDTRA 14265) - impianti idraulici, riscaldamento, sanitari", "U.S. Navy Naval Education and Training Command", "1989", "https://archive.org/details/utilitiesmani024854mbp"),
    "utilitiesmanii024855mbp": ("Utilitiesman 2 - impianti idraulici e sanitari", "U.S. Navy Naval Education and Training Command", "1989", "https://archive.org/details/utilitiesmanii024855mbp"),
    "utilitiesmaniii024856mbp": ("Utilitiesman 3 - impianti idraulici, gas, aria compressa", "U.S. Navy Naval Education and Training Command", "1989", "https://archive.org/details/utilitiesmaniii024856mbp"),
    "concretemanualma00unit": ("Concrete Manual - A Manual for the Control of Concrete Construction (8th ed.)", "U.S. Bureau of Reclamation", "1975", "https://archive.org/details/concretemanualma00unit"),
    "Steelworker1andC10564A": ("Steelworker 1 & C (NAVPERS 10564-A) - carpenteria metallica navale/edilizia", "U.S. Navy Bureau of Naval Personnel", "1954", "https://archive.org/details/Steelworker1andC10564A"),
    "steelworker1": ("Steelworker Volume 1 - strutture metalliche, carpenteria, saldatura", "U.S. Navy (NRTC)", "1996", "https://archive.org/details/steelworker1"),
    "steelworker2": ("Steelworker Volume 2 - carpenteria metallica avanzata", "U.S. Navy (NRTC)", "1996", "https://archive.org/details/steelworker2"),
    "designofsmalldam00unit": ("Design of Small Dams (1st ed.)", "U.S. Bureau of Reclamation", "1960", "https://archive.org/details/designofsmalldam00unit"),
    "micro_IA41155138_0887": ("Engineering Aid 3 & 2, Vol. 2 (NAVEDTRA 10628) - rilievo, disegno tecnico, materiali", "U.S. Navy Naval Education and Training Command", "1982", "https://archive.org/details/micro_IA41155138_0887"),
    "micro_IA41153740_0391_djvu": ("Builder 3 & 2 (NAVEDTRA 14040) - carpenteria, muratura, calcestruzzo, finiture, impalcature", "U.S. Navy Naval Education and Training Command", "1981", "https://archive.org/details/micro_IA41153740_0391"),
    "SCS_NEH_1968_sezione": ("SCS National Engineering Handbook (sezione 1968) - ingegneria del suolo e delle acque", "U.S. Soil Conservation Service, USDA", "1968", "https://archive.org/details/CAT71334647013"),
    "SCS_NEH_1971_sezione": ("SCS National Engineering Handbook (sezione 1971) - ingegneria del suolo e delle acque", "U.S. Soil Conservation Service, USDA", "1971", "https://archive.org/details/CAT71334647020"),
    "NEETS_1992_elettronica_elettricita": ("NEETS - Navy Electricity and Electronics Training Series (sintesi 1992): materia, elettronica, circuiti", "U.S. Navy Naval Education and Training Program", "1992", "https://archive.org/details/navaleducationandtrainingprogrammanagementsupportactivity_navyelectricityandelectronicstrainin_1992"),
    "NEETS_Modulo_01": ("NEETS Modulo 1 - Matter, Energy, and Direct Current (elettricita' DC)", "U.S. Navy", "1992", "https://archive.org/details/NEETSModule01"),
    "NEETS_Modulo_02": ("NEETS Modulo 2 - Batteries and Battery Charging", "U.S. Navy", "1992", "https://archive.org/details/NEETSModule02"),
    "NEETS_Modulo_03": ("NEETS Modulo 3 - Alternating Current (corrente alternata)", "U.S. Navy", "1992", "https://archive.org/details/NEETSModule03"),
    "NEETS_Modulo_04": ("NEETS Modulo 4 - Transformers and Voltage Regulation", "U.S. Navy", "1992", "https://archive.org/details/NEETSModule04"),
    "Waddell_Bridge_Engineering_1916": ("Bridge Engineering (trattato completo di ingegneria dei ponti)", "J.A.L. Waddell", "1916", "https://archive.org/details/bridgeengineeri01waddgoog"),
    "MetcalfEddy_American_Sewerage_Practice_1914": ("American Sewerage Practice, Vol. I (fognature e depurazione - il classico)", "Leonard Metcalf & Harrison P. Eddy", "1914", "https://archive.org/details/americansewerag00eddygoog"),
    "Unwin_Town_Planning_in_Practice_1909": ("Town Planning in Practice (urbanistica operativa - il classico)", "Raymond Unwin", "1909", "https://archive.org/details/town-planning-in-practice"),
    "Robinson_Improvement_Towns_Cities_1901": ("The Improvement of Towns and Cities (igiene urbana e pianificazione)", "Charles Mulford Robinson", "1901", "https://archive.org/details/improvementoftow00robi"),
    "Catalogo_Holophane_illuminazione_1915": ("Holophane Light and Vision Institute (illuminazione tecnica rifrazione vetro)", "Holophane Glass Company", "1915", "https://archive.org/details/TheHolophaneLightAndVisionInstitute"),
    "Catalogo_illuminazione_uffici_1923": ("Eye Comfort Lighting System - illuminazione scientifica di uffici e banche", "s.a. (catalogo commerciale)", "1923", "https://archive.org/details/TheEyeComfortLightingSystemTheScientificIlluminationOfOfficesBanks_439"),
    "Sabine_Acoustics_1922": ("Collected Papers on Acoustics (fondatore dell'acustica architettonica: tempo di riverbero, assorbimento, criteri progettuali)", "Wallace Clement Sabine", "1922", "https://archive.org/details/collectedpapers00sabigoog"),
    "Merriman_Strength_of_Materials_1912": ("Strength of Materials (resistenza dei materiali: tensione, deformazione, travi, colonne)", "Mansfield Merriman", "1912", "https://archive.org/details/strengthofmateri00merriala"),
    "Kidder_Architects_Builders_PocketBook_1916": ("The Architect's and Builder's Pocket-Book (il 'prezzario' americano d'epoca: costi, quantita', dettagli costruttivi, formule)", "Frank E. Kidder", "1916", "https://archive.org/details/buildearchitects00kiddrich"),
    "NAVFAC_DM7_SoilMechanics_1971": ("Soil Mechanics, Foundations and Earth Structures (NAVFAC DM-7.1) - meccanica del terreno, portanza, spinte, stabilizzazione (757k caratteri)", "U.S. Navy Naval Facilities Engineering Command", "1971", "https://archive.org/details/soilmechanicsfou00unit"),
    "NAVFAC_DM7-2_Foundations_1982": ("Foundations and Earth Structures - Design Manual DM 7.2 (progettazione di fondazioni, pali, paratie)", "U.S. Navy Naval Facilities Engineering Command", "1982", "https://archive.org/details/DTIC_ADA123637"),
    "TM5-530_MaterialsTesting": ("Materials Testing (TM 5-530/NAVFAC MO-330) - prove su cemento, acciaio, terreno, bitumi", "U.S. Army / Navy NAVFAC", "1971", "https://archive.org/details/armytm5530navyna003564mbp"),
}

NORME = {
    "DLgs_81_2008_INL_CC_BY_SA.txt": ("D.Lgs 9 aprile 2008 n. 81 - Testo Unico Salute e Sicurezza sul Lavoro, ed. INL gennaio 2026 (testo coordinato, 1466 pp.)", "INL - Ispettorato Nazionale del Lavoro, CC BY-SA 4.0", "https://www.ispettorato.gov.it/files/2026/01/TU-81-08-Ed.-Gennaio-2026.pdf"),
    "NTC2018_DM_completo.txt": ("D.M. 17 gennaio 2018 - Norme Tecniche per le Costruzioni, testo completo G.U. (372 pp.)", "Regione Toscana (atto pubblico)", "https://www.regione.toscana.it/documents/10180/24622703/DM+2018+NTC+GU.pdf"),
    "NTC2018_Circolare_7_2019.txt": ("Circolare 21 gennaio 2019 n. 7 C.S.LL.PP. - Istruzioni per l'applicazione delle NTC 2018 (348 pp.)", "Regione Toscana (atto pubblico)", "https://www.regione.toscana.it/documents/10180/24622703/Circ+2018+NTC+2019+GU.pdf"),
    "Ordinanza_3274_2003_sismica.txt": ("Ordinanza PCM 3274/2003 - Classificazione sismica e norme tecniche per le costruzioni in zona sismica (300 pp.)", "Regione Toscana (atto pubblico)", "https://www.regione.toscana.it/documents/10180/11700802/ord_3274_2003.pdf"),
    "DPR_380_bosetti.htm": ("DPR 6 giugno 2001 n. 380 - Testo Unico in materia edilizia (testo vigente)", "Bosetti e Gatti (atto pubblico)", "https://www.bosettiegatti.eu/info/norme/statali/2001_0380.htm"),
    "DLgs_36_2023_appalti_bosetti.htm": ("D.Lgs 31 marzo 2023 n. 36 - Codice dei contratti pubblici (testo vigente)", "Bosetti e Gatti (atto pubblico)", "https://www.bosettiegatti.eu/info/norme/statali/2023_0036.htm"),
    "DM_37_2008_impianti.htm": ("D.M. 22 gennaio 2008 n. 37 - Regolamento attuazione art. 11 D.Lgs 81/08: attivita' di installazione degli impianti", "Bosetti e Gatti (atto pubblico)", "https://www.bosettiegatti.eu/info/norme/statali/2008_0037.htm"),
    "DLgs_42_2004_beni_culturali.htm": ("D.Lgs 22 gennaio 2004 n. 42 - Codice dei beni culturali e del paesaggio", "Bosetti e Gatti (atto pubblico)", "https://www.bosettiegatti.eu/info/norme/statali/2004_0042.htm"),
    "Legge_10_1991.htm": ("Legge 9 gennaio 1991 n. 10 - Norme per l'attuazione del Piano energetico nazionale (ed. originale)", "Bosetti e Gatti (atto pubblico)", "https://www.bosettiegatti.eu/info/norme/statali/1991_0010.htm"),
    "DLgs_152_2006_ambiente.htm": ("D.Lgs 3 aprile 2006 n. 152 - Norme in materia ambientale (Testo Unico Ambiente)", "Bosetti e Gatti (atto pubblico)", "https://www.bosettiegatti.eu/info/norme/statali/2006_0152.htm"),
    "DM_1444_1968_igiene_abitazioni.htm": ("D.M. 20 febbraio 1968 n. 1444 - Limiti igienico-abitativi degli edifici", "Bosetti e Gatti (atto pubblico)", "https://www.bosettiegatti.eu/info/norme/statali/1968_1444.htm"),
    "DLgs_28_2011_FER.htm": ("D.Lgs 3 marzo 2011 n. 28 - Attuazione direttiva 2009/28/CE sulle FER (art. 28: base del Conto Termico)", "Bosetti e Gatti (atto pubblico)", "https://www.bosettiegatti.eu/info/norme/statali/2011_0028.htm"),
    "DLgs_102_2014_EE_TEE.htm": ("D.Lgs 4 luglio 2014 n. 102 - Efficienza energetica, diagnosi energetiche, TEE (Certificati Bianchi)", "Bosetti e Gatti (atto pubblico)", "https://www.bosettiegatti.eu/info/norme/statali/2014_0102.htm"),
    "DLgs_192_2005_APE.htm": ("D.Lgs 19 agosto 2005 n. 192 - Certificazione energetica degli edifici (APE), recepimento direttiva EPBD", "Bosetti e Gatti (atto pubblico)", "https://www.bosettiegatti.eu/info/norme/statali/2005_0192.htm"),
    "DLgs_199_2021_CER.txt": ("D.Lgs 8 novembre 2021 n. 199 - Attuazione direttiva RED II: FER, autoconsumo, Comunita' Energetiche Rinnovabili (88 pp.)", "Bosetti e Gatti / Gazzetta Ufficiale (atto pubblico)", "https://www.bosettiegatti.eu/info/norme/statali/2021_0199.pdf"),
    "DL_34_2020_rilancio.txt": ("D.L. 19 maggio 2020 n. 34 - Decreto Rilancio: Superbonus 110% (art. 119) e misure economiche, testo originale (326 pp.)", "Ministero del Lavoro / Gazzetta Ufficiale (atto pubblico)", "https://www.lavoro.gov.it/documenti-e-norme/normative/Documents/2020/D-L-19-maggio-2020.pdf"),
    "DM_7_8_2025_ContoTermico3.txt": ("D.M. 7 agosto 2025 - Conto Termico 3.0: incentivazione interventi di piccole dimensioni di efficienza energetica e produzione di calore da FER, testo articolato completo (GU n. 224 del 26-9-2025)", "Gazzetta Ufficiale (atto pubblico)", "https://www.gazzettaufficiale.it/eli/id/2025/09/26/25A05263/sg"),
    "DM_26_6_2015_requisiti_minimi.txt": ("D.M. 26 giugno 2015 - Metodologie di calcolo delle prestazioni energetiche, requisiti minimi degli edifici, RTP e linee guida certificazione energetica, con allegati (112 pp., testo coordinato)", "ENEA / Gazzetta Ufficiale (atto pubblico)", "https://www.apelazio.enea.it/doc/dm_26062015.pdf"),
}

def strip_html(h):
    h = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", h)
    h = re.sub(r"(?is)<br\s*/?>", "\n", h)
    h = re.sub(r"(?is)</(p|div|article|li|h[1-6]|tr)>", "\n", h)
    h = re.sub(r"<[^>]+>", " ", h)
    import html as _h
    h = _h.unescape(h)
    return re.sub(r"[ \t]+", " ", h)

def strip_xml(x):
    x = re.sub(r"(?is)<HEAD>(.*?)</HEAD>", r"\n## \1\n", x)
    x = re.sub(r"<[^>]+>", " ", x)
    import html as _h
    x = _h.unescape(x)
    return re.sub(r"[ \t]+", " ", x)

def clean_txt(t):
    t = re.sub(r"\n{3,}", "\n\n", t)
    t = re.sub(r"[ \t]+", " ", t)
    return t.strip()

def chunks(text, source, meta, url, license_, attribution, extra=None):
    """Spezza in chunk su confini di paragrafo; ritorna lista record."""
    paras = re.split(r"\n\s*\n", text)
    out, buf, idx = [], [], 1
    def flush():
        nonlocal buf, idx
        if not buf: return
        body = "\n\n".join(buf).strip()
        if len(body) < 80: buf = []; return
        rec = {"doc_id": f"{source}_{idx:04d}", "source": source,
               "license": license_, "commercial_ok": True,
               "attribution": attribution, "url": url, "text": body}
        if extra: rec.update(extra)
        out.append(rec); idx += 1; buf = []
    for p in paras:
        p = p.strip()
        if not p: continue
        if sum(len(b) for b in buf) + len(p) > CHUNK and buf:
            flush()
        if len(p) > CHUNK:  # paragrafo enorme: spezza duro
            for i in range(0, len(p), CHUNK - OVERLAP):
                buf = [p[i:i + CHUNK]]; flush()
            buf = []
        else:
            buf.append(p)
    flush()
    return out

manifest = []

# ------------------------------------------------------------- manuali US gov
recs = []
for path in sorted(glob.glob(os.path.join(RAW, "manuals_txt", "*.txt"))):
    base = os.path.splitext(os.path.basename(path))[0]
    title, agency, year, url = MANUALS.get(base, (base, "U.S. Government", "n.d.", ""))
    text = clean_txt(open(path, encoding="utf-8", errors="ignore").read())
    text = re.sub(r"\n{2,}", "\n\n", text)
    lic = ("Public domain (opera del Governo federale USA)"
           if "U.S." in agency or "Navy" in agency or "USDA" in agency
           else "Public domain (pubblicato prima del 1930)")
    c = chunks(text, "manuali_us_gov", None, url, lic,
               f"{title} - {agency} ({year}) - public domain",
               extra={"title": title, "agency": agency, "year": year})
    recs += c
    manifest.append({"file": "parsed/manuali_us_gov.jsonl", "doc": title, "records": len(c),
                     "license": "Public domain (US Gov)", "url": url})
with open(os.path.join(OUT, "manuali_us_gov.jsonl"), "w", encoding="utf-8") as f:
    for r in recs: f.write(json.dumps(r, ensure_ascii=False) + "\n")
print(f"manuali_us_gov.jsonl: {len(recs)} record")

# ------------------------------------------------------------- OSHA eCFR
path = os.path.join(RAW, "ecfr", "29CFR1926_construction.xml")
recs = []
if os.path.exists(path):
    xml = open(path, encoding="utf-8", errors="ignore").read()
    # una divisione per sezione/sottoparte: splitta sui DIV9 (sezioni)
    parts = re.split(r"(?=<DIV9 )", xml)
    for p in parts:
        m = re.search(r"<HEAD>(.*?)</HEAD>", p, re.S)
        head = re.sub(r"<[^>]+>", " ", m.group(1)).strip() if m else "sezione"
        text = clean_txt(strip_xml(p))
        if len(text) < 100: continue
        c = chunks(text, "ecfr_osha1926", None,
                   "https://www.ecfr.gov/current/title-29/subtitle-B/chapter-XVII/part-1926",
                   "Public domain (regolamento Governo federale USA)",
                   f"29 CFR Part 1926 - OSHA Safety and Health Regulations for Construction - {head}",
                   extra={"title": head})
        recs += c
    manifest.append({"file": "parsed/ecfr_osha_1926.jsonl", "doc": "29 CFR 1926 OSHA Construction",
                     "records": len(recs), "license": "Public domain (US Gov)",
                     "url": "https://www.ecfr.gov/current/title-29/part-1926"})
with open(os.path.join(OUT, "ecfr_osha_1926.jsonl"), "w", encoding="utf-8") as f:
    for r in recs: f.write(json.dumps(r, ensure_ascii=False) + "\n")
print(f"ecfr_osha_1926.jsonl: {len(recs)} record")

# ------------------------------------------------------------- norme italiane
recs = []
for fn, (title, fonte, url) in NORME.items():
    path = os.path.join(RAW, "norme_it", fn)
    if not os.path.exists(path): continue
    text = clean_txt(strip_html(open(path, encoding="utf-8", errors="ignore").read()))
    if "INL" in fn:
        licenza = "CC BY-SA 4.0 (INL - Ispettorato Nazionale del Lavoro); testo normativo pubblico"
    else:
        licenza = "Testo normativo ufficiale italiano (atto pubblico, libera riproduzione - art. 5 L.633/1941)"
    c = chunks(text, "norme_italiane", None, url, licenza,
               f"{title} - fonte: {fonte}", extra={"title": title})
    recs += c
    manifest.append({"file": "parsed/norme_italiane.jsonl", "doc": title, "records": len(c),
                     "license": "Atto pubblico italiano", "url": url})
with open(os.path.join(OUT, "norme_italiane.jsonl"), "w", encoding="utf-8") as f:
    for r in recs: f.write(json.dumps(r, ensure_ascii=False) + "\n")
print(f"norme_italiane.jsonl: {len(recs)} record")

# ------------------------------------------------------------- indice IFC
recs = []
for path in sorted(glob.glob(os.path.join(RAW, "bim_ifc", "**", "*.ifc"), recursive=True)):
    sz = os.path.getsize(path)
    head = open(path, encoding="utf-8", errors="ignore").read(60000)
    schema = re.search(r"FILE_SCHEMA\s*\(\s*\(([^)']*'([^']+)'[^)]*)\)", head)
    fname = re.search(r"FILE_NAME\s*\(\s*'([^']*)'", head)
    ent = {}
    sample = head
    if sz > 5_000_000:
        # campiona entity types dal primo blocco
        pass
    for m in re.finditer(r"#\d+\s*=\s*IFC([A-Z0-9]+)", sample):
        ent[m.group(1)] = ent.get(m.group(1), 0) + 1
    top = sorted(ent.items(), key=lambda kv: -kv[1])[:15]
    recs.append({"file": os.path.relpath(path, HERE), "size_bytes": sz,
                 "schema": schema.group(2) if schema else "sconosciuto",
                 "file_name": fname.group(1) if fname else "",
                 "entity_types_in_first_60kb": dict(top),
                 "license": "MIT", "commercial_ok": True,
                 "attribution": "bim-whale-ifc-samples (andrewisen) - MIT",
                 "url": "https://github.com/andrewisen/bim-whale-ifc-samples"})
manifest.append({"file": "parsed/ifc_bim_index.jsonl", "doc": "Indice modelli IFC (6 edifici)",
                 "records": len(recs), "license": "MIT",
                 "url": "https://github.com/andrewisen/bim-whale-ifc-samples"})
with open(os.path.join(OUT, "ifc_bim_index.jsonl"), "w", encoding="utf-8") as f:
    for r in recs: f.write(json.dumps(r, ensure_ascii=False) + "\n")
print(f"ifc_bim_index.jsonl: {len(recs)} record")

# ------------------------------------------------------------- UFGS specs (public domain)
recs = []
import glob as _glob
for path in sorted(_glob.glob(os.path.join(RAW, "ufgs_specs", "txt", "*.txt"))):
    base = os.path.splitext(os.path.basename(path))[0].replace("_", " ")
    text = clean_txt(open(path, encoding="utf-8", errors="ignore").read())
    sec = " ".join(base.split()[1:4]) if base.upper().startswith("UFGS") else base
    c = chunks(text, "ufgs_specs", None,
               "https://www.wbdg.org/ffc/dod/unified-facilities-guide-specifications",
               "Public domain (opera del Governo federale USA)",
               f"{base} - Unified Facilities Guide Specification (U.S. DoD), public domain",
               extra={"title": base, "section": sec})
    recs += c
    manifest.append({"file": "parsed/ufgs_specs.jsonl", "doc": base, "records": len(c),
                     "license": "Public domain (US Gov)",
                     "url": "https://www.wbdg.org/ffc/dod/unified-facilities-guide-specifications"})
with open(os.path.join(OUT, "ufgs_specs.jsonl"), "w", encoding="utf-8") as f:
    for r in recs: f.write(json.dumps(r, ensure_ascii=False) + "\n")
print(f"ufgs_specs.jsonl: {len(recs)} record")

# ------------------------------------------------------------- classici design/estetica (public domain)
DESIGN = {
    "decorationofhous00whar.txt": ("The Decoration of Houses", "Edith Wharton & Ogden Codman Jr.", 1898, "https://archive.org/details/decorationofhous00whar"),
    "houseingoodtaste00deworich.txt": ("The House in Good Taste", "Elsie de Wolfe", 1913, "https://archive.org/details/houseingoodtaste00deworich"),
    "hintsonhousehold00east_0.txt": ("Hints on Household Taste", "Charles Eastlake", 1878, "https://archive.org/details/hintsonhousehold00east_0"),
    "gri_33125008700086_djvu.txt": ("The Grammar of Ornament", "Owen Jones", 1856, "https://archive.org/details/gri_33125008700086"),
    "lampsofarchseven00ruskrich_djvu.txt": ("The Seven Lamps of Architecture", "John Ruskin", 1889, "https://archive.org/details/lampsofarchseven00ruskrich"),
    "principlesofdeco00dres_djvu.txt": ("Principles of Decorative Design", "Christopher Dresser", 1873, "https://archive.org/details/principlesofdeco00dres"),
    "vitruviustenbook00vitruoft_djvu.txt": ("Vitruvius: The Ten Books on Architecture", "Vitruvius (tr. Morgan)", 1914, "https://archive.org/details/vitruviustenbook00vitruoft"),
    "andreapalladiosa00pall_djvu.txt": ("Andrea Palladio's Architecture, in Four Books (ed. 1736, in inglese)", "Andrea Palladio (tr. Isaac Ware)", 1736, "https://archive.org/details/andreapalladiosa00pall"),
    "quattrolibridell00pall_djvu.txt": ("I quattro libri dell'architettura (ed. 1590, in italiano)", "Andrea Palladio", 1590, "https://archive.org/details/quattrolibridell00pall_202401"),
    "stonesofvenice22rusk_djvu.txt": ("The Stones of Venice, Vol. II", "John Ruskin", 1851, "https://archive.org/details/stonesofvenice22rusk"),
    "radfordscycloped01unse_djvu.txt": ("Radford's Cyclopedia of Construction, Vol. 1 - carpentry, building and architecture", "Radford Architectural Company", 1915, "https://archive.org/details/radfordscycloped01unse"),
}
recs = []
for fn, (title, author, year, url) in DESIGN.items():
    path = os.path.join(RAW, "design_classics", fn)
    if not os.path.exists(path): continue
    text = clean_txt(open(path, encoding="utf-8", errors="ignore").read())
    c = chunks(text, "design_classics", None, url, "Public domain (pubblicato prima del 1930)",
               f"{title}, {author} ({year}) - public domain, scan archive.org",
               extra={"title": title, "author": author, "year": year})
    recs += c
    manifest.append({"file": "parsed/design_estetica.jsonl", "doc": title, "records": len(c),
                     "license": "Public domain", "url": url})
with open(os.path.join(OUT, "design_estetica.jsonl"), "w", encoding="utf-8") as f:
    for r in recs: f.write(json.dumps(r, ensure_ascii=False) + "\n")
print(f"design_estetica.jsonl: {len(recs)} record")

# ------------------------------------------------------------- prezzi materiali FRED (public domain US Gov)
FRED = {
    "WPU081": "PPI: Lumber", "WPU08": "PPI: Lumber and Wood Products",
    "WPU1322": "PPI: Cement, Hydraulic", "PCU327320327320": "PPI: Ready-Mix Concrete Manufacturing",
    "WPU101": "PPI: Iron and Steel", "WPU102502": "PPI: Copper and Brass Mill Shapes",
    "WPU1026": "PPI: Nonferrous Wire and Cable", "WPU137": "PPI: Gypsum Products",
    "WPU0679": "PPI: Miscellaneous Chemical Products", "WPU13": "PPI: Nonmetallic Mineral Products",
    "WPU103": "PPI: Metal Containers",
}
import csv as _csv
recs = []
for sid, name in FRED.items():
    path = os.path.join(RAW, "prezzi_fred", sid + ".csv")
    if not os.path.exists(path): continue
    rows = []
    with open(path, encoding="utf-8") as f:
        rd = _csv.reader(f); next(rd)
        for date, val in rd:
            if val in (".", ""): continue
            rows.append((date, float(val)))
    if not rows: continue
    yoy = round((rows[-1][1] / rows[-13][1] - 1) * 100, 1) if len(rows) > 12 else None
    rec = {"source": "fred_ppi_materiali", "license": "Public domain (dati Governo federale USA: BLS via FRED)",
           "commercial_ok": True,
           "attribution": f"{name} ({sid}) - FRED / U.S. Bureau of Labor Statistics, public domain",
           "url": f"https://fred.stlouisfed.org/series/{sid}",
           "series_id": sid, "title": name, "frequency": "monthly",
           "period": f"{rows[0][0]} to {rows[-1][0]}",
           "last_value": rows[-1][1], "yoy_pct": yoy, "n_obs": len(rows),
           "text": "; ".join(f"{d}:{v}" for d, v in rows)}
    recs.append(rec)
    manifest.append({"file": "parsed/materiali_prezzi.jsonl", "doc": f"{name} ({sid})", "records": 1,
                     "license": "Public domain (US Gov)", "url": f"https://fred.stlouisfed.org/series/{sid}"})
with open(os.path.join(OUT, "materiali_prezzi.jsonl"), "w", encoding="utf-8") as f:
    for r in recs: f.write(json.dumps(r, ensure_ascii=False) + "\n")
print(f"materiali_prezzi.jsonl: {len(recs)} record")

# ------------------------------------------------------------- NPS Preservation Briefs + FEMA P-749 (public domain)
REPORTS = {
    "FEMA_P749": ("FEMA P-749 - Earthquake-Resistant Design Concepts (NEHRP Recommended Seismic Provisions)", "FEMA / Building Seismic Safety Council", "2021", "https://www.fema.gov/emergency-managers/risk-management/earthquake/seismic-building-codes"),
}
_brief_titles = {
    "01": "Cleaning and Water-Repellent Treatments for Historic Masonry Buildings",
    "02": "Repointing Mortar Joints in Historic Masonry Buildings",
    "03": "Improving Energy Efficiency in Historic Buildings",
    "04": "Roofing for Historic Buildings",
    "05": "The Preservation of Historic Adobe Buildings",
    "06": "The Dangers of Abrasive Cleaning to Historic Buildings",
    "07": "The Preservation of Historic Glazed Architectural Terra-Cotta",
    "09": "The Repair of Historic Wooden Windows",
    "10": "Exterior Paint Problems on Historic Woodwork",
    "11": "Improving the Energy Efficiency of Historic Storefronts",
    "12": "The Preservation of Historic Structural Glass",
    "13": "The Repair and Thermal Upgrading of Historic Steel Windows",
    "14": "New Exterior Additions to Historic Buildings: Preservation Concerns",
    "15": "Preservation of Historic Concrete",
    "16": "The Use of Substitute Materials on Historic Building Exteriors",
    "17": "Architectural Character: Identifying the Visual Aspects of Historic Buildings",
    "18": "Rehabilitating Interiors in Historic Buildings",
    "19": "The Repair and Replacement of Historic Wooden Shingle Roofs",
    "20": "The Preservation of Historic Barns",
    "21": "Repairing Historic Flat Plaster Walls and Ceilings",
    "22": "The Preservation and Repair of Historic Stucco",
    "23": "Preserving Historic Ornamental Plaster",
    "24": "Heating, Ventilating, and Cooling Historic Buildings: Problems and Recommended Approaches",
    "25": "The Preservation of Historic Signs",
    "26": "The Preservation of Historic Log Buildings",
    "27": "The Maintenance and Repair of Architectural Cast Iron",
    "28": "Painting Historic Interiors",
    "29": "The Repair, Replacement and Maintenance of Historic Slate Roofs",
    "30": "The Preservation and Repair of Historic Clay Tile Roofs",
    "31": "Mothballing Historic Buildings",
    "32": "Making Historic Properties Accessible",
    "33": "The Preservation and Repair of Historic Stained and Leaded Glass",
    "34": "The Repair and Replacement of Historic Composition Ornament",
    "35": "Understanding Old Buildings: The Process of Architectural Investigation",
    "36": "Protecting Cultural Landscapes",
    "38": "Removing Graffiti from Historic Masonry",
    "39": "Controlling Unwanted Moisture in Historic Buildings",
    "40": "Preserving Historic Ceramic Tile Floors",
    "41": "The Seismic Retrofit of Historic Buildings",
    "42": "The Maintenance, Repair and Replacement of Historic Cast Stone",
    "43": "The Preparation and Use of Historic Structure Reports",
    "44": "The Use of Awnings on Historic Buildings",
    "45": "Preserving Historic Wood Porches",
    "46": "The Preservation of Historic Gas Stations",
    "47": "Maintaining the Exterior of Small and Medium Size Historic Buildings",
    "48": "Preserving Grave Markers in Historic Cemeteries",
    "49": "Historic Metal Ceilings and Walls",
    "50": "Lightning Protection for Historic Structures",
    "51": "Historic Building Codes and Contemporary Building Codes",
}
recs = []
for path in sorted(glob.glob(os.path.join(RAW, "us_gov_pdf", "*.txt"))):
    base = os.path.splitext(os.path.basename(path))[0]
    if base in REPORTS:
        title, agency, year, url = REPORTS[base]
    elif base.startswith("nps_preservation-brief-"):
        num = base.split("-")[3]
        t = _brief_titles.get(num, base)
        title = f"NPS Preservation Brief {num} - {t}"
        agency, year, url = "U.S. National Park Service, Technical Preservation Services", "1975-2024", "https://www.nps.gov/orgs/1739/preservation-briefs.htm"
    else:
        title, agency, year, url = base, "U.S. Government", "n.d.", ""
    text = clean_txt(open(path, encoding="utf-8", errors="ignore").read())
    c = chunks(text, "reports_us_gov", None, url,
               "Public domain (opera del Governo federale USA)",
               f"{title} - {agency} ({year}) - public domain",
               extra={"title": title, "agency": agency, "year": year})
    recs += c
    manifest.append({"file": "parsed/reports_us_gov.jsonl", "doc": title, "records": len(c),
                     "license": "Public domain (US Gov)", "url": url})
with open(os.path.join(OUT, "reports_us_gov.jsonl"), "w", encoding="utf-8") as f:
    for r in recs: f.write(json.dumps(r, ensure_ascii=False) + "\n")
print(f"reports_us_gov.jsonl: {len(recs)} record")

# copia licenza MIT IFC
lic_src = os.path.join(RAW, "bim_ifc", "LICENSE")
if os.path.exists(lic_src):
    open(os.path.join(OUT, "IFC_SAMPLES_LICENSE_MIT.txt"), "w", encoding="utf-8").write(open(lic_src, encoding="utf-8", errors="ignore").read())

with open(os.path.join(HERE, "manifest.json"), "w", encoding="utf-8") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)
print("manifest.json scritto")
