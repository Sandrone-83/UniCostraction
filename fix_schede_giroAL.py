# -*- coding: utf-8 -*-
"""Giro AL (30/10/2026): due append datate in ENERGETICA_INCENTIVI_PACK.
AL1 - scheda detrazioni (riga con 'Le detrazioni fiscali'): mappa nuovo TUIR confermata
da fonti concordanti (artt. 17/371/372/373/376) + conferme pmi.it che le misure sono nel DDL.
AL2 - scheda Reddito Energetico: stato sportello (chiuso) + ipotesi rifinanziamento
300 mln / 30.000 nuclei (BibLus 30/10/2026), con cautela.
Fonti: idealista.it 20/7/2026, lavoripubblici.it 22/7/2026, edilportale.com 16/7/2026,
agefis.it 21/7/2026 e 15/9/2026, fiscoetasse.com 13/7/2026, pmi.it 28/10/2026,
biblus.acca.it 30/10/2026.
"""
import json

PATH = 'UNIVERSITA_EDILIZIA/ENERGETICA_INCENTIVI_PACK/schede/schede.jsonl'

NOTA_DETRAZIONI = (" Aggiornamento 30/10/2026: (1) MAPPA NUOVO TUIR confermata da fonti tecniche "
    "concordanti (idealista.it, lavoripubblici.it, edilportale.com, agefis.it, fiscoetasse.com, "
    "luglio-settembre 2026): dal 1/1/2027 i riferimenti diventano art. 17 D.Lgs 117/2026 "
    "(disciplina ordinaria del recupero edilizio, in sostituzione dell'art. 16-bis DPR 917/1986; a "
    "regime 36% su 48.000 euro), art. 371 (sismabonus, ex art. 16 D.L. 63/2013), art. 372 "
    "(ecobonus, ex art. 14 D.L. 63/2013 e L. 296/2006), art. 373 (aliquote e limiti temporanei "
    "2025-2027: tetto 96.000 euro; 2025-2026: 36% ordinaria / 50% abitazione principale; 2027 "
    "secondo il testo vigente del TUIR: 30% ordinaria / 36% abitazione principale), art. 376 (i "
    "richiami a norme abrogate si intendono riferiti alle corrispondenti del nuovo testo). Dal 2027 "
    "vanno aggiornate causali di bonifico, asseverazioni e modulistica. Le aliquote 2027 scritte "
    "nell'art. 373 (30%/36%) sono proprio quelle che il DDL Bilancio 2027 annuncia di voler "
    "modificare riportandole a 50%/36%: il coordinamento avverra' nel testo finale della legge. "
    "(2) Conferme di stampa (pmi.it, 28/10/2026) riportano proroga 50%/36% e Bonus Mobili 5.000 "
    "euro come misure GIA' inserite nel DDL approvato dal CdM il 28/10/2026: resta comunque la "
    "verifica sull'articolato ufficiale presentato in Parlamento e sull'esito dell'iter "
    "(approvazione finale entro il 31/12/2026).")

NOTA_REDDITO = (" Aggiornamento 30/10/2026 (verifica web): lo sportello risulta CHIUSO per "
    "esaurimento delle risorse stanziate e il decreto di rifinanziamento non risulta pubblicato in "
    "GU; tra le ipotesi di stampa per la Legge di Bilancio 2027 figura un rifinanziamento di circa "
    "300 milioni di euro per raggiungere altri 30.000 nuclei (BibLus, 30/10/2026): previsione "
    "giornalistica NON stanziata; i requisiti di un'eventuale nuova edizione (ISEE, taglie, "
    "contributo) vanno verificati nei relativi atti ufficiali (portale GSE / MASE), senza presumere "
    "che restino invariati.")

rows = []
with open(PATH, encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if line:
            rows.append(json.loads(line))

det = red = None
for r in rows:
    if r['nome'].startswith("Le detrazioni fiscali per l'edilizia"):
        det = r
    if r['nome'].startswith('Il Reddito Energetico'):
        red = r
assert det is not None and red is not None, 'schede non trovate'
assert 'Aggiornamento 29/10/2026' in det['normative'], 'ancora 29/10 mancante'
assert 'Aggiornamento 30/10/2026' not in det['normative'], 'nota detrazioni gia presente'
assert 'Aggiornamento 30/10/2026' not in red['normative'], 'nota reddito gia presente'

det['normative'] += NOTA_DETRAZIONI
red['normative'] += NOTA_REDDITO

with open(PATH, 'w', encoding='utf-8', newline='\n') as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + '\n')

print('OK: note 30/10/2026 appese a scheda detrazioni e scheda Reddito Energetico; righe:', len(rows))
