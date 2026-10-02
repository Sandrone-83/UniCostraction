# -*- coding: utf-8 -*-
"""Correttore esami UniCostraction.

Uso:
  python valuta_esami.py template <SETTORE>|--tutti   # genera scheda risposta vuota
  python valuta_esami.py valuta <SETTORE>|--tutti      # corregge e scrive il verbale

Le chiavi riservate vivono in ESAMI_RISPOSTE/ (fuori repository).
Le risposte del candidato vanno in ESAMI/RISPOSTE_CANDIDATO/<SETTORE>.txt
"""
import glob
import json
import os
import re
import sys
from datetime import date

ROOT = os.path.dirname(os.path.abspath(__file__))          # UNIVERSITA_EDILIZIA
WS = os.path.dirname(ROOT)
CHIAVI = os.path.join(WS, 'ESAMI_RISPOSTE')
CAND = os.path.join(ROOT, 'ESAMI', 'RISPOSTE_CANDIDATO')
VERBALE = os.path.join(CAND, 'VERBALE_VALUTAZIONE.md')

GIUDIZI = [(90, 'Eccellente'), (80, 'Buono'), (70, 'Sufficiente'),
           (50, 'Insufficiente — ripassare le schede indicate')]


def settori():
    out = []
    for d in sorted(glob.glob(os.path.join(ROOT, 'ESAMI', '*'))):
        if os.path.isdir(d) and os.path.basename(d) != 'RISPOSTE_CANDIDATO':
            if os.path.exists(os.path.join(d, 'domande.md')):
                out.append(os.path.basename(d))
    return out


def n_domande(settore):
    txt = open(os.path.join(ROOT, 'ESAMI', settore, 'domande.md'), encoding='utf-8').read()
    n = len(re.findall(r'^## Domanda', txt, re.M))
    if n == 0:
        n = len(re.findall(r'^\*\*D\d+\.\*\*', txt, re.M))
    return n


def _lettere_da_domande(settore):
    """Per le chiavi legacy senza lettera: ricava A-D confrontando il testo
    della risposta corretta con le opzioni del file domande.md."""
    txt = open(os.path.join(ROOT, 'ESAMI', settore, 'domande.md'), encoding='utf-8').read()
    blocchi = re.split(r'\*\*D(\d+)\.\*\*', txt)[1:]
    out = {}
    norm = lambda s: re.sub(r'\s+', ' ', s).strip().lower()
    for i in range(0, len(blocchi) - 1, 2):
        n, corpo = int(blocchi[i]), blocchi[i + 1]
        out[n] = {m.group(1): m.group(2).strip()
                  for m in re.finditer(r'^\s+([ABCD])\) (.+)$', corpo, re.M)}
    return out, norm


def carica_chiave(settore):
    path = os.path.join(CHIAVI, settore + '_risposte.jsonl')
    if not os.path.exists(path):
        return None
    chiave = {}
    righe = [json.loads(l) for l in open(path, encoding='utf-8') if l.strip()]
    if righe and 'lettera' in righe[0]:
        for d in righe:
            chiave[int(d['n'])] = {'lettera': d['lettera'], 'fonte': d.get('fonte', '')}
    else:
        for d in righe:
            n = int(d['domanda'])
            rc = str(d.get('risposta_corretta', '')).strip().upper()
            if rc in ('A', 'B', 'C', 'D'):
                chiave[n] = {'lettera': rc, 'fonte': d.get('scheda_fonte', '')}
                continue
            opzioni, norm = _lettere_da_domande(settore)
            lettera = ''
            for l, testo in opzioni.get(n, {}).items():
                if norm(testo) == norm(rc):
                    lettera = l
                    break
            chiave[n] = {'lettera': lettera, 'fonte': d.get('scheda_fonte', '')}
    return chiave


def cmd_template(arg):
    os.makedirs(CAND, exist_ok=True)
    lista = settori() if arg == '--tutti' else [arg]
    for s in lista:
        n = n_domande(s)
        path = os.path.join(CAND, s + '.txt')
        if os.path.exists(path):
            print('esiste gia:', path)
            continue
        with open(path, 'w', encoding='utf-8') as f:
            for i in range(1, n + 1):
                f.write('%d;\n' % i)
        print('scheda creata:', path, '(%d domande)' % n)


def cmd_valuta(arg):
    os.makedirs(CAND, exist_ok=True)
    lista = settori() if arg == '--tutti' else [arg]
    righe = ['# Verbale di valutazione — %s\n' % date.today().isoformat(),
             '| Settore | Domande | Corrette | % | Giudizio |',
             '|---|---|---|---|---|']
    dettagli = []
    riepilogo = []
    for s in lista:
        chiave = carica_chiave(s)
        if chiave is None:
            righe.append('| %s | — | — | — | chiave riservata assente |' % s)
            continue
        risp_path = os.path.join(CAND, s + '.txt')
        if not os.path.exists(risp_path):
            tot_ns = n_domande(s)
            righe.append('| %s | %d | — | — | non sostenuto |' % (s, tot_ns))
            continue
        risp = {}
        for ln in open(risp_path, encoding='utf-8'):
            m = re.match(r'\s*(\d+)\s*;\s*([ABCDabcd])', ln)
            if m:
                risp[int(m.group(1))] = m.group(2).upper()
        corrette = 0
        errate = []
        for n, k in sorted(chiave.items()):
            r = risp.get(n)
            if r is not None and r == k['lettera']:
                corrette += 1
            else:
                errate.append((n, k['lettera'], k.get('fonte', ''), r))
        tot = len(chiave)
        pct = round(100.0 * corrette / tot) if tot else 0
        giudizio = next((g for soglia, g in GIUDIZI if pct >= soglia),
                        'Da rifare — gap sistemico sul settore')
        righe.append('| %s | %d | %d | %d | %s |' % (s, tot, corrette, pct, giudizio))
        riepilogo.append((s, tot, corrette, pct, giudizio))
        if errate:
            dettagli.append('\n## %s — errori da ripassare (%d)\n' % (s, len(errate)))
            dettagli.append('| Domanda | Corretta | Risposta data | Fonte da ripassare |')
            dettagli.append('|---|---|---|---|')
            for n, lett, fonte, data_ in errate:
                dettagli.append('| %d | %s | %s | %s |' % (
                    n, lett, data_ or 'mancante', fonte.replace('|', '/')))
    media = round(sum(x[3] for x in riepilogo) / len(riepilogo), 1) if riepilogo else 0
    righe.append('\n**Media complessiva: %s%%**' % media)
    da_ripassare = sorted([x for x in riepilogo if x[3] < 70], key=lambda x: x[3])
    if da_ripassare:
        righe.append('\nSettori sotto il 70%% da riprendere: %s' %
                     ', '.join('%s (%d%%)' % (x[0], x[3]) for x in da_ripassare))
    righe.append('\nLe risposte corrette riportate sopra riguardano solo le domande '
                 'errate o mancanti; le chiavi complete restano in ESAMI_RISPOSTE/ '
                 '(fuori repository).')
    out = '\n'.join(righe) + '\n' + '\n'.join(dettagli) + '\n'
    with open(VERBALE, 'w', encoding='utf-8') as f:
        f.write(out)
    print(out[:2000])
    print('...verbale completo in', VERBALE)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    if sys.argv[1] == 'template':
        cmd_template(sys.argv[2])
    elif sys.argv[1] == 'valuta':
        cmd_valuta(sys.argv[2])
    else:
        print(__doc__)
        sys.exit(1)
