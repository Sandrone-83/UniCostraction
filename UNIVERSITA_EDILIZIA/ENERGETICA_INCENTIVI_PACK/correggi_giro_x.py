# -*- coding: utf-8 -*-
"""Giro X — verifica su fonte primaria delle schede incentivi non-Conto Termico.
Patch applicate (prima -> dopo, vedi CHANGELOG):
X1 detrazioni: rimossa roadmap 'dal 2034 = 36%' (non confermata da fonti)
X2 Reddito Energetico: 80% Mezzogiorno per legge; rimossi riferimenti non verificati
X3 diagnosi energetica: riscrittura su D.Lgs 102/2024 (soglie TJ, scadenze 2026/2027)
X4 iperammortamento: scaglioni 180/100/50, finestra 2026-2028, piattaforma GSE, 105%, moduli UE
X5 TEE: origine D.M. 20/7/2004, obbligati >50.000 clienti, D.M. MASE 21/7/2025
X6 APE: validità subordinata ai controlli impianti (DPR 74/2013), DM 28/10/2025
X7 CER: typo municipaità -> municipalità
"""
import json, io

P = 'schede/schede.jsonl'
rows = [json.loads(l) for l in io.open(P, encoding='utf-8')]

def find(name):
    for d in rows:
        if d['nome'].startswith(name):
            return d
    raise KeyError(name)

# ---------------- X1 Detrazioni ----------------
d = find('Le detrazioni fiscali')
old = "Dal 2027 le aliquote scendono a 36% e 30%; dal 2028 al 2033 si prevede il 30% con limite di 48.000 euro."
new = "Dal 2027 le aliquote scendono a 36% e 30% (limite sempre 96.000 euro); dal 2028 l'aliquota e' unica al 30% con limite di 48.000 euro (art. 16-bis co. 3-ter TUIR, introdotto dalla L. 199/2025)."
assert old in d['descrizione'], 'X1a non trovato'
d['descrizione'] = d['descrizione'].replace(old, new)
old = "roadmap: 2027 = 36%/30% (limite 96.000 euro), 2028-2033 = 30% con limite 48.000 euro, dal 2034 = 36% con 48.000 euro"
new = "roadmap: 2027 = 36%/30% (limite 96.000 euro), dal 2028 = 30% unico con limite 48.000 euro (art. 16-bis co. 3-ter TUIR); la dicitura 'dal 2034 aliquota 36%' riportata da alcune fonti secondarie NON e' confermata dal testo di legge e va ignorata"
assert old in d['tecnologia'], 'X1b non trovato'
d['tecnologia'] = d['tecnologia'].replace(old, new)

# ---------------- X2 Reddito Energetico ----------------
d = find('Il Reddito Energetico')
old = "domanda prima dell'entrata in esercizio, realizzazione entro 18 mesi dall'accoglimento, energia non autoconsumata"
new = "domanda prima dell'entrata in esercizio, energia non autoconsumata"
assert old in d['tecnologia'], 'X2a non trovato'
d['tecnologia'] = d['tecnologia'].replace(old, new)
old = "larga quota destinata al Mezzogiorno (circa 80% dei fondi secondo le fonti di settore); alcune regioni hanno requisiti piu' ampi (es. Puglia: ISEE fino a 20.000 euro) con bandi regionali dedicati"
new = "per legge (D.M. 8/8/2023) l'80% delle risorse e' destinato al Mezzogiorno; esistono bandi regionali analoghi con requisiti propri (verificare sui portali regionali)"
assert old in d['tecnologia'], 'X2b non trovato'
d['tecnologia'] = d['tecnologia'].replace(old, new)

# ---------------- X3 Diagnosi energetica ----------------
d = find('Diagnosi energetica e energy manager')
d['nome'] = "Diagnosi energetica e energy manager: gli obblighi D.Lgs 102/2024"
d['descrizione'] = ("Il D.Lgs 102/2024 (recepimento della direttiva EED 2023/1791/UE, in vigore dal 10 ottobre 2025) "
    "ha riformato gli obblighi nazionali di efficienza energetica, sostituendo il precedente D.Lgs 102/2014: "
    "diagnosi energetica obbligatoria ogni 4 anni per i soggetti con consumi pari o superiori a 10 TJ/anno "
    "(circa 2,78 GWh), sistema di gestione energetico ISO 50001 per consumi pari o superiori a 85 TJ/anno "
    "(circa 23,6 GWh). Il vecchio sistema (grandi imprese ed energivore) resta storico fino al 2025.")
d['tecnologia'] = ("Obblighi verificati sul testo del D.Lgs 102/2024 (ottobre 2026): 1) DIAGNOSI ENERGETICA: audit completo "
    "dei consumi secondo la norma UNI CEI EN 16247, con cadenza quadriennale per i soggetti con consumi >= 10 TJ/anno "
    "(circa 2,78 GWh); chi rientra per la prima volta nel perimetro deve effettuare la prima diagnosi entro l'11 ottobre 2026; "
    "chi era gia' obbligato in forza del precedente decreto mantiene la cadenza quadriennale, con prossima scadenza "
    "5 dicembre 2027 (non piu' 'dicembre degli anni dispari'); 2) SISTEMA DI GESTIONE DELL'ENERGIA: adozione di un SGEn "
    "conforme alla UNI EN ISO 50001 obbligatoria per i soggetti con consumi >= 85 TJ/anno (circa 23,6 GWh), con adeguamento "
    "entro l'11 ottobre 2027 secondo le regole di transizione del decreto; 3) ENERGY MANAGER: la disciplina del nominativo "
    "esperto in gestione dell'energia resta richiamata per i soggetti con consumi rilevanti — prima di dichiarare l'obbligo "
    "verificare le soglie nei decreti attuativi vigenti (il D.Lgs 102/2024 rinvia a essi, non fissa numeri autonomi); "
    "4) STORICO (fino al 2025): grandi imprese (occupati > 250 E fatturato > 50 mln di euro, entrambe le condizioni) ed "
    "imprese energivore CSEA (consumi >= 2,4 GWh/anno con incidenza del costo dell'energia sul valore della produzione >= 3%), "
    "con possibilita' di esenzione per chi aveva ISO 50001 / ISO 14001 / EMAS; sanzioni amministrative da 2.000 a 20.000 euro "
    "(mancata diagnosi) e da 4.000 a 40.000 euro (mancata comunicazione); 5) le comunicazioni ai registri/organismi competenti "
    "seguono i decreti attuativi vigenti: verificare sempre la versione aggiornata prima della pratica.")
d['normative'] = ("D.Lgs 102/2024 (recepimento direttiva EED 2023/1791/UE, in vigore dal 10/10/2025); UNI CEI EN 16247 "
    "(diagnosi energetiche); UNI EN ISO 50001 (sistemi di gestione dell'energia); storico: D.Lgs 102/2014 e decreti MIMIT "
    "con gli elenchi delle imprese energivore.")
d['note_cantiere'] = ("Dal 2026 la prima domanda professionale non e' piu' 'sei una grande impresa?' ma 'quanto consumi in "
    "TJ/anno?': raccogliere i consumi elettrici e termici dell'ultimo triennio (fatture) prima di dichiarare l'obbligo. "
    "Le scadenze chiave sono l'11 ottobre 2026 (prima diagnosi per i nuovi soggetti) e l'11 ottobre 2027 (ISO 50001 per i "
    "soggetti >= 85 TJ). Chi si muove con un anno di anticipo trova le ESCo disponibili; chi si muove a ridosso paga il "
    "sovrapprezzo e rischia la sanzione.")

# ---------------- X4 Iperammortamento ----------------
d = find('Transizione 5.0 e iperammortamento')
d['nome'] = "Iperammortamento 2026-2028 e fine del ciclo Transizione 5.0"
d['descrizione'] = ("Per le imprese il ciclo Transizione 5.0 (credito d'imposta 35-45% su investimenti effettuati entro il "
    "31/12/2025) e' chiuso ai nuovi investimenti; la L. 199/2025 (Legge di Bilancio 2026, artt. 427-436) ha reintrodotto "
    "l'IPERAMMORTAMENTO per gli investimenti effettuati dal 1 gennaio 2026 al 30 settembre 2028: maggiorazione del costo "
    "deducibile al 180% per la quota fino a 2,5 mln di euro, 100% per la quota tra 2,5 e 10 mln, 50% tra 10 e 20 mln, "
    "nulla oltre 20 mln. Comprende i beni 4.0 (allegati IV e V) e gli impianti a fonti rinnovabili per autoconsumo con "
    "sistemi di accumulo, anche in via autonoma rispetto ai beni 4.0.")
d['tecnologia'] = ("Quadro verificato sulla L. 199/2025 (ottobre 2026): 1) SCAGLIONI: 180% di maggiorazione per la parte di "
    "costo fino a 2,5 mln di euro; 100% per la parte tra 2,5 e 10 mln; 50% per la parte tra 10 e 20 mln; nessuna maggiorazione "
    "oltre 20 mln (il beneficio massimo si ha quindi sui primi 2,5 mln di investimento); 2) FINESTRA: investimenti dal "
    "1/1/2026 al 30/9/2028, con completamento dei lavori e comunicazione entro il 15 novembre 2028; 3) BENI AMMESSI: beni "
    "materiali e immateriali 4.0 (allegati IV e V della disciplina agevolazioni) e impianti a fonti rinnovabili per "
    "autoconsumo con sistemi di accumulo, questi ultimi anche senza beni 4.0 'trainanti'; 4) FOTOVOLTAICO: ammesso se la "
    "producibilita' annua stimata non supera il 105% del fabbisogno energetico annuo del sito, con moduli iscritti alle "
    "sezioni B o C del Registro delle tecnologie per il fotovoltaico (art. 12 D.L. 181/2023); 5) ITER: comunicazione "
    "preventiva sulla piattaforma GSE, riserva con acconto (20% del beneficio) entro 60 giorni dalla richiesta, completamento "
    "e comunicazione finale entro il 15/11/2028; 6) VALORE: con IRES al 24% la maggiorazione al 180% vale circa il 43% del "
    "costo in termini di risparmio fiscale nel primo scaglione; il beneficio si realizza in dichiarazione, non in cassa "
    "immediata; 7) STORICO: Transizione 5.0 era un credito d'imposta del 35% (45% con incremento di produzione) su beni "
    "4.0 e software, con asseverazione energetica, per investimenti effettuati entro il 31/12/2025: chiuso ai nuovi "
    "investimenti, restano in corso di godimento i crediti gia' acquisiti.")
d['normative'] = ("L. 199/2025 (Legge di Bilancio 2026), artt. 427-436 (iperammortamento 2026-2028); D.L. 181/2023 art. 12 "
    "(Registro delle tecnologie per il fotovoltaico); disciplina precedente: crediti Transizione 4.0/5.0 2021-2025, chiusi "
    "ai nuovi investimenti dal 31/12/2025; piattaforma GSE per le comunicazioni (versione vigente).")

# ---------------- X5 TEE ----------------
d = find('I certificati bianchi')
old = "nati con l'obbligo per i distributori di energia elettrica e gas di conseguire obiettivi annuali di risparmio"
new = "nati con i decreti interministeriali 20 luglio 2004 (elettrico e gas), che hanno posto obblighi annuali di risparmio energetico ai distributori"
assert old in d['descrizione'], 'X5a non trovato'
d['descrizione'] = d['descrizione'].replace(old, new)
old = "1) gli obbligati (distributori con clienti sopra soglia)"
new = "1) gli obbligati sono i distributori di energia elettrica e di gas con piu' di 50.000 clienti finali ciascuno"
assert old in d['tecnologia'], 'X5b non trovato'
d['tecnologia'] = d['tecnologia'].replace(old, new)
old = "3) i TEE hanno durata (tipicamente 5 anni, poi alcuni anni di conservazione secondo regole aggiornate) e prezzo di mercato fluttuante"
new = ("3) i TEE hanno durata e regole di conservazione definite periodicamente dal Ministero e scadono: verificare sempre le regole vigenti; "
    "con il D.M. MASE 21 luglio 2025 (in vigore dal 12 settembre 2025) sono stati fissati i nuovi obiettivi 2025-2030 "
    "(7,9 mln di TEE elettrico + 4,9 mln di TEE gas cumulati nel periodo) ed e' stato introdotto il TEE virtuale, acquistabile "
    "dal GSE al prezzo fisso di 10 euro, con vincolo di detenzione minima dei TEE tradizionali crescente dal 40% (2025) "
    "all'80% (2029) per poter acquistare i virtuali")
assert old in d['tecnologia'], 'X5c non trovato'
d['tecnologia'] = d['tecnologia'].replace(old, new)
d['normative'] = ("D.M. 20 luglio 2004 (istituzione dei TEE, decreti gemelli elettrico e gas); D.Lgs 28/2011 art. 7 (obblighi "
    "raccordati di efficienza); D.M. MASE 21 luglio 2025 (nuovi obiettivi 2025-2030 e TEE virtuali, in vigore dal 12/9/2025); "
    "regole GSE per la certificazione e il mercato (aggiornate periodicamente); direttiva EED di riferimento (2023/1791/UE).")

# ---------------- X6 APE ----------------
d = find("L'APE:")
old = "Validità: 10 anni dalla data di rilascio (salvo rilevanti modifiche). Sanzioni"
new = ("Validità: massimo 10 anni dal rilascio (art. 6 co. 5 D.Lgs 192/2005), SUBORDINATA al rispetto dei controlli di "
    "efficienza energetica degli impianti termici (DPR 74/2013): se un controllo viene saltato l'APE decade il 31 dicembre "
    "dell'anno successivo alla prima scadenza non rispettata (per questo i libretti di impianto si allegano all'APE); va "
    "aggiornato prima dei dieci anni a ogni intervento che modifica la classe energetica. Dal 3 giugno 2026 i nuovi APE si "
    "redigono con la metodologia del DM 28 ottobre 2025, che sostituisce integralmente il DM 26 giugno 2015. Sanzioni")
assert old in d['tecnologia'], 'X6 non trovato'
d['tecnologia'] = d['tecnologia'].replace(old, new)
d['normative'] = ("D.Lgs 192/2005 art. 6 (obblighi e validità decennale subordinata), D.Lgs 63/2013, DPR 75/2013 (requisiti dei "
    "certificatori), DPR 74/2013 (controlli impianti termici: condizione della validità), DM 26 giugno 2015 e DM 28 ottobre "
    "2025 (metodologia di calcolo, in vigore dal 3/6/2026); regole regionali sui registri e sulle sanzioni.")

# ---------------- X7 CER typo ----------------
d = find('CER e autoconsumo collettivo')
assert 'municipaità' in d['applicazioni']
d['applicazioni'] = d['applicazioni'].replace('municipaità', 'municipalità')

with io.open(P, 'w', encoding='utf-8') as f:
    for d in rows:
        f.write(json.dumps(d, ensure_ascii=False) + '\n')
print('OK: %d schede riscritte' % len(rows))
