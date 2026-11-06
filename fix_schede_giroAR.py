# -*- coding: utf-8 -*-
"""Giro AR: append nota 06/11/2026 (conferma art. 4 + art. 37 + fondi FV/PA) alla scheda detrazioni."""
import json

P = 'UNIVERSITA_EDILIZIA/ENERGETICA_INCENTIVI_PACK/schede/schede.jsonl'
NOTA = (" Aggiornamento 06/11/2026 (DDL Bilancio 2027 in esame alla Camera; conferme da stampa tecnica "
        "concordante: BibLus, Finanza&Fisco, Ingenio): confermati i contenuti dell'art. 4 gia' riportati "
        "nella nota del 04/11/2026 (aliquote 36%/50%, Ecobonus max 96.000 euro/u.i. e parti comuni 40.000 "
        "euro x unita', Sismabonus max 96.000 euro e parti comuni 96.000 euro x unita', esclusione caldaie "
        "uniche a fossili). Precisazioni emerse: (1) l'art. 360-ter supera la precedente struttura dei "
        "massimali Ecobonus differenziati per tipologia di intervento e NON ripropone la disciplina speciale "
        "degli interventi condominiali congiunti energia+sisma con limite maggiorato; (2) l'art. 360-quater "
        "(bonus arredo, 50% su 5.000 euro) richiama espressamente solo i MOBILI destinati all'arredo "
        "dell'immobile ristrutturato: i grandi elettrodomestici non sono richiamati nel testo e restano alla "
        "misura separata del comma 2 (50 milioni per il 2027, decreto attuativo); il perimetro potra' "
        "cambiare nell'iter parlamentare. Altre misure della manovra rilevanti per il settore, tutte "
        "PROPOSTE in esame parlamentare: (3) art. 37: le quote annuali di crediti d'imposta Superbonus 2023 "
        "(art. 119 D.L. 34/2020) utilizzabili in compensazione nel 2027 sono ulteriormente ripartite in 10 "
        "rate annuali di pari importo (salva l'opzione ex art. 9 comma 4 D.L. 176/2022); (4) efficienza "
        "energetica degli edifici pubblici: 600 milioni per il 2028 e 500 milioni/anno per 2029 e 2030 al "
        "GSE, con copertura fino al 100% per ospedali e strutture sanitarie pubbliche, scuole, universita', "
        "istituzioni AFAM, enti pubblici di ricerca, piscine e impianti per sport del ghiaccio, a condizione "
        "di riduzione di almeno il 30% del fabbisogno di energia primaria; decreti attuativi entro 90 giorni "
        "dall'entrata in vigore; (5) fotovoltaico di nuova costruzione fino a 1 MW: contributo in conto "
        "capitale fino al 40% dei costi ammissibili per i soggetti che accedono al meccanismo FER-X "
        "(D.M. 18/6/2026), plafond 800 milioni per il 2028 e 200 milioni/anno per 2029-2030, contingente 3 "
        "GW; (6) ricostruzione post-sisma: contributo fino al 100% del danno puntuale per centri storici e "
        "borghi del cratere 2016, 20 milioni per il restauro dei piccoli borghi del cratere 2009, proroga "
        "strutture al 2029 e piattaforma digitale GEDISI. STATO: tutto in esame parlamentare, non operativo "
        "fino ad approvazione definitiva e pubblicazione in GU.")

lines = open(P, encoding='utf-8').read().splitlines()
o = json.loads(lines[5])
assert 'detrazioni fiscali' in o['nome'].lower(), o['nome']
assert '06/11/2026' not in o['normative']
o['normative'] = o['normative'].rstrip() + NOTA
lines[5] = json.dumps(o, ensure_ascii=False)
open(P, 'w', encoding='utf-8', newline='\n').write('\n'.join(lines) + '\n')
print('OK append AR1, nuova lunghezza normative:', len(o['normative']))
json.loads(lines[5])
print('json valido')
