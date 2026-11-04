# -*- coding: utf-8 -*-
"""Giro AP: append nota DDL Bilancio 2027 (articolato bollinato) alla scheda detrazioni."""
import json

P = 'UNIVERSITA_EDILIZIA/ENERGETICA_INCENTIVI_PACK/schede/schede.jsonl'
NOTA = (" Aggiornamento 04/11/2026 (articolato DDL Bilancio 2027, testo bollinato trasmesso al Parlamento "
        "il 30/10/2026; fonti: edilizia.com con PDF del testo bollinato, Il Sole 24 Ore del 1/11/2026, "
        "comunicato CdM n. 195 del 28/10/2026): l'art. 4 del DDL propone di abrogare tre disposizioni "
        "transitorie del nuovo TUIR e di introdurre gli artt. 360-bis (misure antisismiche), 360-ter "
        "(riqualificazione energetica) e 360-quater (recupero del patrimonio edilizio e arredo degli "
        "immobili ristrutturati). Ecobonus 2027 proposto: 36% ordinario, elevato al 50% per le spese "
        "sostenute dal proprietario o dal titolare di diritto reale di godimento per lavori sull'abitazione "
        "principale; limite 96.000 euro per unita' immobiliare, per gli interventi sulle parti comuni "
        "condominiali 40.000 euro moltiplicati per il numero delle unita' dell'edificio; ripartizione in "
        "10 quote annuali; espressamente escluse le sostituzioni degli impianti di climatizzazione invernale "
        "con caldaie uniche alimentate a combustibili fossili. Sismabonus 2027 proposto: 36%/50% alle "
        "stesse condizioni, limite 96.000 euro per unita' immobiliare e 96.000 euro x numero unita' per le "
        "parti comuni. Bonus ristrutturazioni 2027: 36%/50%, limite 96.000 euro per unita' immobiliare. "
        "Arredo dell'immobile ristrutturato: detrazione 50% su massimo 5.000 euro di spesa, collegata alla "
        "detrazione per il recupero edilizio (lavori iniziati dal 1/1 dell'anno precedente all'acquisto); "
        "misura distinta dal ripristino elettrodomestici del comma 2 (50 milioni per il 2027, criteri "
        "rinviati a decreto attuativo). Il ritorno dell'Ecobonus al 65% NON compare in questa formulazione: "
        "ipotesi accantonata. STATO: proposta legislativa in esame parlamentare (approvazione prevista "
        "entro il 31/12/2026): aliquote, limiti e condizioni possono cambiare durante l'iter; NON inserire "
        "nei preventivi 2027 come benefici certi finche' la legge non e' definitivamente approvata e "
        "pubblicata in Gazzetta Ufficiale.")

lines = open(P, encoding='utf-8').read().splitlines()
assert len(lines) >= 6
o = json.loads(lines[5])
assert 'detrazioni fiscali' in o['nome'].lower(), o['nome']
assert '04/11/2026' not in o['normative']
o['normative'] = o['normative'].rstrip() + NOTA
lines[5] = json.dumps(o, ensure_ascii=False)
open(P, 'w', encoding='utf-8', newline='\n').write('\n'.join(lines) + '\n')
# ricalcola conteggio COURSE.yaml
import re
cy = 'UNIVERSITA_EDILIZIA/ENERGETICA_INCENTIVI_PACK/COURSE.yaml'
t = open(cy, encoding='utf-8').read()
print('righe pack:', len(lines))
print('OK append, nuova lunghezza normative:', len(o['normative']))
