# -*- coding: utf-8 -*-
"""Giro di sicurezza pre-tag v1.4 — audit incrociato della repository.
Controlli:
A. schede: JSON valido, chiavi complete, valori non vuoti, typo noti, stringhe stale
B. esami: ogni risposta chiave ricostruibile dalla scheda fonte (substring check)
C. cloze corrotte in tutti i fogli domande
D. riferimenti stale in enciclopedia
Scrive AUDIT_SICUREZZA_V1_4.md ed esce con riepilogo.
"""
import json, io, os, re, glob, sys

ROOT = os.path.dirname(os.path.abspath(__file__))          # UNIVERSITA_EDILIZIA
WK = os.path.dirname(ROOT)                                  # workspace (radice git)
RISPOSTE = os.path.join(WK, 'ESAMI_RISPOSTE')

REQ = ['nome', 'categoria', 'descrizione', 'tecnologia', 'applicazioni',
       'vantaggi', 'limiti', 'costi_e_economia', 'casi_real_world',
       'normative', 'note_cantiere']
STALE = ['PRIERA', 'municipaità', 'dal 2034 = 36%', 'dal 2034 = 36 %',
         'D.Lgs 102/2014', 'Transizione 5.0 e iperammortamento: il lato imprese',
         'gli obblighi D.Lgs 102/2014']

report = []
def out(s=''):
    report.append(s)
    print(s)

# ---------------- A. schede ----------------
out('# AUDIT DI SICUREZZA PRE-TAG v1.4 — UniCostraction')
out('')
out('Data: 2026-10-02. Metodo: controlli automatizzati incrociati (schede ↔ esami ↔ enciclopedia).')
out('')
out('## A. Controllo schede (70 pack)')
A_issues = 0
packs = sorted(glob.glob(os.path.join(ROOT, '*_PACK')))
tot_schede = 0
for pdir in packs:
    pname = os.path.basename(pdir)
    sf = os.path.join(pdir, 'schede', 'schede.jsonl')
    if not os.path.exists(sf):
        out('- **MANCANTE** %s: nessuno schede/schede.jsonl' % pname); A_issues += 1; continue
    nomi = set()
    for i, line in enumerate(io.open(sf, encoding='utf-8')):
        tot_schede += 1
        try:
            d = json.loads(line)
        except Exception as e:
            out('- **JSON ERRATO** %s riga %d: %s' % (pname, i + 1, e)); A_issues += 1; continue
        for k in REQ:
            v = d.get(k)
            if v is None or (isinstance(v, str) and len(v.strip()) < 10):
                out('- **CAMPO VUOTO/CORTO** %s riga %d, scheda «%s», campo %s' % (pname, i + 1, d.get('nome', '?'), k))
                A_issues += 1
        n = d.get('nome', '')
        if n in nomi:
            out('- **NOME DUPLICATO** %s: «%s»' % (pname, n)); A_issues += 1
        nomi.add(n)
        blob = json.dumps(d, ensure_ascii=False)
        for st in STALE:
            if st in blob:
                out('- **STRINGA STALE** %s, «%s»: contiene «%s»' % (pname, n, st)); A_issues += 1
out('')
out('Schede totali lette: **%d**. Problemi A: **%d**.' % (tot_schede, A_issues))

# ---------------- B. chiavi esami ----------------
out('')
out('## B. Verifica chiavi esami (risposta ricostruibile dalla scheda fonte)')
B_fail = 0; B_tot = 0; B_files = 0
schede_cache = {}
for kf in sorted(glob.glob(os.path.join(RISPOSTE, '*_risposte.jsonl'))):
    settore = os.path.basename(kf).replace('_risposte.jsonl', '')
    fails = []
    prev_n = 0
    for line in io.open(kf, encoding='utf-8'):
        k = json.loads(line); B_tot += 1; B_files += 0
        if k.get('n') != prev_n + 1:
            fails.append('numerazione: atteso %d trovato %s' % (prev_n + 1, k.get('n')))
        prev_n = k.get('n', prev_n)
        fonte = k.get('fonte', '')
        if ' / ' not in fonte:
            fails.append('n. %s: fonte malformato «%s»' % (k.get('n'), fonte)); continue
        pack, nome = fonte.split(' / ', 1)
        if pack not in schede_cache:
            pf = os.path.join(ROOT, pack, 'schede', 'schede.jsonl')
            if not os.path.exists(pf):
                fails.append('n. %s: pack %s non trovato' % (k.get('n'), pack)); schede_cache[pack] = {}; continue
            m = {}
            for l2 in io.open(pf, encoding='utf-8'):
                dd = json.loads(l2); m[dd['nome']] = json.dumps(dd, ensure_ascii=False).lower()
            schede_cache[pack] = m
        src = schede_cache[pack].get(nome)
        if src is None:
            fails.append('n. %s: scheda «%s» non trovata in %s' % (k.get('n'), nome, pack)); continue
        if str(k.get('risposta', '')).lower() not in src:
            fails.append('n. %s: risposta NON ricostruibile da «%s»' % (k.get('n'), nome))
    B_files += 1
    if fails:
        B_fail += len(fails)
        out('- **%s**: %d problemi' % (settore, len(fails)))
        for f in fails[:8]:
            out('  - %s' % f)
        if len(fails) > 8:
            out('  - ... e altri %d' % (len(fails) - 8))
    else:
        n_keys = sum(1 for _ in io.open(kf, encoding='utf-8'))
        out('- OK %s: %d chiavi' % (settore, n_keys))
out('')
out('Settori chiavi: **%d**. Chiavi totali: **%d**. Problemi B: **%d**.' % (B_files, B_tot, B_fail))

# ---------------- C. cloze corrotte ----------------
out('')
out('## C. Cloze corrotte nei fogli domande (pattern ___lettera)')
C_bad = 0
for df in sorted(glob.glob(os.path.join(ROOT, 'ESAMI', '*', 'domande.md'))):
    settore = os.path.basename(os.path.dirname(df))
    txt = io.open(df, encoding='utf-8').read()
    m = re.findall(r'___[a-zàèéìòù]', txt)
    if m:
        C_bad += len(m)
        out('- **%s**: %d cloze corrotte, esempi: %s' % (settore, len(m), ', '.join(sorted(set(m))[:6])))
if C_bad == 0:
    out('Nessuna cloze corrotta su %d fogli domande.' % len(glob.glob(os.path.join(ROOT, 'ESAMI', '*', 'domande.md'))))
out('Problemi C: **%d**.' % C_bad)

# ---------------- D. riferimenti stale enciclopedia ----------------
out('')
out('## D. Riferimenti stale in ENCICLOPEDIA/')
D_hits = 0
for md in sorted(glob.glob(os.path.join(ROOT, 'ENCICLOPEDIA', '*.md'))):
    txt = io.open(md, encoding='utf-8').read()
    for st in STALE:
        for mm in re.finditer(re.escape(st), txt):
            D_hits += 1
            line_no = txt[:mm.start()].count('\n') + 1
            out('- %s riga %d: «%s»' % (os.path.basename(md), line_no, st))
out('Problemi D: **%d**.' % D_hits)

# ---------------- Esito ----------------
out('')
out('## ESITO')
out('- Schede lette: %d | Problemi schede: %d' % (tot_schede, A_issues))
out('- Chiavi esami: %d su %d settori | Problemi: %d' % (B_tot, B_files, B_fail))
out('- Cloze corrotte: %d' % C_bad)
out('- Riferimenti stale enciclopedia: %d' % D_hits)
out('- **TOTALE PROBLEMI: %d**' % (A_issues + B_fail + C_bad + D_hits))

io.open(os.path.join(ROOT, 'AUDIT_SICUREZZA_V1_4.md'), 'w', encoding='utf-8').write('\n'.join(report) + '\n')
