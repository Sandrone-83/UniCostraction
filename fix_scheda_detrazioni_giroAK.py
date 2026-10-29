# -*- coding: utf-8 -*-
"""Giro AK (29/10/2026): append nota datata alla scheda detrazioni (riga 6 di
ENERGETICA_INCENTIVI_PACK) dopo l'approvazione del DDL Bilancio 2027 in CdM (28/10/2026).
Fonti: edilportale.com 28/10/2026, tg24.sky.it 28/10/2026, lentepubblica.it 28/10/2026,
fiscoetasse.com 28/10/2026 (annunci di conferenza stampa: articolato da verificare).
"""
import json

PATH = 'UNIVERSITA_EDILIZIA/ENERGETICA_INCENTIVI_PACK/schede/schede.jsonl'

NOTA = (" Aggiornamento 29/10/2026: il 28/10/2026 il Consiglio dei Ministri ha approvato il "
        "disegno di legge di Bilancio 2027. In conferenza stampa il viceministro MEF Leo ha "
        "annunciato la PROROGA per il 2027 delle aliquote del 50% (abitazione principale) e 36% "
        "(altri immobili) per Bonus ristrutturazioni, Ecobonus e Sismabonus — evitando il calo a "
        "36%/30% previsto dalla normativa vigente (L. 199/2025) — e la conferma del Bonus Mobili "
        "2027 con limite di spesa di 5.000 euro; la presidente del Consiglio ha inoltre annunciato "
        "climatizzatori e pompe di calore nelle scuole ed efficientamento energetico di ospedali e "
        "universita' con risorse della clausola nazionale di salvaguardia UE per l'energia (bandi "
        "nel 2027, erogazione dal 2028). ATTENZIONE: sono annunci di conferenza stampa, NON ancora "
        "legge — la portata esatta (durata della proroga, agevolazioni incluse, sorte del Sismabonus "
        "acquisti, condizioni e massimali) e' DA VERIFICARE sull'articolato del DDL appena "
        "pubblicato e dopo l'iter parlamentare (approvazione finale attesa entro il 31/12/2026), "
        "anche in coordinamento col nuovo TUIR (D.Lgs 117/2026) applicabile dal 1/1/2027; finche' "
        "la legge non e' definitiva, nei preventivi per spese 2027 indicare entrambi gli scenari "
        "(vigente 36%/30% vs proroga annunciata 50%/36%). Fonti: edilportale.com, tg24.sky.it, "
        "lentepubblica.it, fiscoetasse.com (tutte del 28/10/2026).")

rows = []
with open(PATH, encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if line:
            rows.append(json.loads(line))

target = None
for r in rows:
    if r['nome'].startswith("Le detrazioni fiscali per l'edilizia"):
        target = r
        break
assert target is not None, 'scheda detrazioni non trovata'
assert 'Aggiornamento 29/10/2026' not in target['normative'], 'nota gia presente'
assert 'Aggiornamento 27/10/2026' in target['normative'], 'ancora 27/10 mancante: stato inatteso'

target['normative'] += NOTA

with open(PATH, 'w', encoding='utf-8', newline='\n') as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + '\n')

print('OK: nota 29/10/2026 appesa alla scheda detrazioni; righe totali:', len(rows))
