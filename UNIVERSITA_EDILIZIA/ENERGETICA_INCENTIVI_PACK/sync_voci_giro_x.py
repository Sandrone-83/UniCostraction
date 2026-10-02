# -*- coding: utf-8 -*-
"""Giro X — sincronizzazione voci enciclopedia per le schede correttate."""
import io

P = '../ENCICLOPEDIA/VOCI_FACOLTA_IMPIANTI_ENERGIA.md'
t = io.open(P, encoding='utf-8').read()

def rep(old, new):
    global t
    assert old in t, 'NON TROVATO: ' + old[:70]
    assert t.count(old) == 1, 'DUPLICATO: ' + old[:70]
    t = t.replace(old, new)

# ---- APE ----
rep("Validità: 10 anni dalla data di rilascio (salvo rilevanti modifiche). Sanzioni",
    "Validità: massimo 10 anni dal rilascio (art. 6 co. 5 D.Lgs 192/2005), SUBORDINATA al rispetto dei controlli di efficienza energetica degli impianti termici (DPR 74/2013): se un controllo viene saltato l'APE decade il 31 dicembre dell'anno successivo alla prima scadenza non rispettata (per questo i libretti di impianto si allegano all'APE); va aggiornato prima dei dieci anni a ogni intervento che modifica la classe energetica. Dal 3 giugno 2026 i nuovi APE si redigono con la metodologia del DM 28 ottobre 2025, che sostituisce integralmente il DM 26 giugno 2015. Sanzioni")
rep("- **Normativa:** D.Lgs 192/2005 (origine, recepimento EPBD), D.Lgs 63/2013, DPR 75/2013 (metodo di calcolo unico nazionale); regole regionali sui registri e sulle sanzioni.",
    "- **Normativa:** D.Lgs 192/2005 art. 6 (obblighi e validità decennale subordinata), D.Lgs 63/2013, DPR 75/2013 (requisiti dei certificatori), DPR 74/2013 (controlli impianti termici: condizione della validità), DM 26 giugno 2015 e DM 28 ottobre 2025 (metodologia di calcolo, in vigore dal 3/6/2026); regole regionali sui registri e sulle sanzioni.")

# ---- CER typo ----
rep("Condomini, borghi e municipaità, filiere agricole",
    "Condomini, borghi e municipalità, filiere agricole")

# ---- Detrazioni ----
rep("Dal 2027 le aliquote scendono a 36% e 30%; dal 2028 al 2033 si prevede il 30% con limite di 48.000 euro.",
    "Dal 2027 scendono a 36% e 30% (limite sempre 96.000 euro); dal 2028 l'aliquota e' unica al 30% con limite di 48.000 euro (art. 16-bis co. 3-ter TUIR).")
rep("2) roadmap: 2027 = 36%/30% (limite 96.000 euro), 2028-2033 = 30% con limite 48.000 euro, dal 2034 = 36% con 48.000 euro",
    "2) roadmap: 2027 = 36%/30% (limite 96.000 euro), dal 2028 = 30% unico con limite 48.000 euro (art. 16-bis co. 3-ter TUIR; il ritorno al 36% 'dal 2034' citato da alcune fonti secondarie NON e' confermato dal testo di legge)")

# ---- Iperammortamento ----
rep("### Transizione 5.0 e iperammortamento: il lato imprese",
    "### Iperammortamento 2026-2028 e fine del ciclo Transizione 5.0")
rep("Per le imprese l'efficienza energetica si incentiva anche con il credito d'imposta: il Transizione 5.0 (2024-2025) è chiuso ai nuovi investimenti dal 31/12/2025; l'iperammortamento 2026 resta per beni immateriali e per l'autoproduzione rinnovabile con accumulo (fino al 30/9/2028), secondo la disciplina vigente.",
    "Il ciclo Transizione 5.0 (credito d'imposta 35-45% su investimenti effettuati entro il 31/12/2025) e' chiuso ai nuovi investimenti; la L. 199/2025 (Legge di Bilancio 2026, artt. 427-436) ha reintrodotto l'IPERAMMORTAMENTO per gli investimenti dal 1 gennaio 2026 al 30 settembre 2028: maggiorazione del costo deducibile al 180% per la quota fino a 2,5 mln di euro, 100% tra 2,5 e 10 mln, 50% tra 10 e 20 mln, nulla oltre 20 mln. Comprende i beni 4.0 (allegati IV e V) e gli impianti a fonti rinnovabili per autoconsumo con sistemi di accumulo, anche in via autonoma rispetto ai beni 4.0.")
old_tec = "- **Tecnologia e criteri:** Quadro verificato a ottobre 2026: 1) Transizione 5.0: credito d'imposta del 35% su investimenti in nuovi beni strumentali e software per efficienza energetica e transizione digitale/ecologica, erogato tramite piattaforma MIMIT con vincolo di consumo/risparmio misurabile; investimenti ammissibili fino al 31/12/2025 (transizione verso il nuovo ciclo); 2) Iperammortamento 2026: maggiorazione del costo deducibile per investimenti in beni materiali immateriali; per il fotovoltaico in autoconsumo con sistemi di accumulo la disciplina è rimasta tra gli strumenti principali (termine investimenti 30 settembre 2028 secondo le fonti di settore verificate); 3) logica diversa dal Conto Termico: credito d'imposta e ammortamento migliorano il bilancio d'impresa, il Conto Termico mette cassa; 4) per il fotovoltaico aziendale 'puro' (senza intervento sul riscaldamento) l'iperammortamento è oggi il riferimento principale; 5) verifiche: asseverazioni energetiche (audit o diagnosi per i crediti di efficienza), vincoli su beni nuovi, esclusi i beni ordinari."
new_tec = "- **Tecnologia e criteri:** Quadro verificato sulla L. 199/2025 (ottobre 2026): 1) SCAGLIONI: 180% di maggiorazione per la parte di costo fino a 2,5 mln di euro; 100% per la parte tra 2,5 e 10 mln; 50% per la parte tra 10 e 20 mln; nulla oltre 20 mln (il beneficio massimo si ha sui primi 2,5 mln); 2) FINESTRA: investimenti dal 1/1/2026 al 30/9/2028, completamento e comunicazione entro il 15 novembre 2028; 3) BENI AMMESSI: beni materiali e immateriali 4.0 (allegati IV e V) e impianti a fonti rinnovabili per autoconsumo con sistemi di accumulo, anche senza beni 4.0 'trainanti'; 4) FOTOVOLTAICO: producibilita' annua stimata non superiore al 105% del fabbisogno energetico annuo del sito, con moduli iscritti alle sezioni B o C del Registro delle tecnologie per il fotovoltaico (art. 12 D.L. 181/2023); 5) ITER: comunicazione preventiva sulla piattaforma GSE, riserva con acconto (20% del beneficio) entro 60 giorni dalla richiesta, completamento e comunicazione finale entro il 15/11/2028; 6) VALORE: con IRES al 24% la maggiorazione al 180% vale circa il 43% del costo in termini di risparmio fiscale nel primo scaglione; il beneficio si realizza in dichiarazione, non in cassa immediata; 7) STORICO: Transizione 5.0 era un credito d'imposta del 35% (45% con incremento di produzione) su beni 4.0 e software, con asseverazione energetica, per investimenti entro il 31/12/2025: chiuso ai nuovi investimenti, restano in godimento i crediti gia' acquisiti; 8) logica diversa dal Conto Termico: ammortamento e crediti migliorano il bilancio d'impresa, il Conto Termico mette cassa; per il fotovoltaico aziendale 'puro' l'iperammortamento e' oggi il riferimento principale."
rep(old_tec, new_tec)
rep("- **Normativa:** D.L. approvati per Transizione 5.0 (crediti 2024-2025) e legge di bilancio 2026; discipline iperammortamento aggiornate (verificare versione vigente); piattaforma MIMIT per i crediti energia.",
    "- **Normativa:** L. 199/2025 (Legge di Bilancio 2026), artt. 427-436 (iperammortamento 2026-2028); D.L. 181/2023 art. 12 (Registro delle tecnologie per il fotovoltaico); disciplina precedente: crediti Transizione 4.0/5.0 2021-2025, chiusi ai nuovi investimenti dal 31/12/2025; piattaforma GSE per le comunicazioni (versione vigente).")

# ---- Reddito Energetico ----
rep("polizza assicurativa multirischio e servizio di manutenzione e monitoraggio per almeno 10 anni, domanda prima dell'entrata in esercizio, realizzazione entro 18 mesi dall'accoglimento, energia non autoconsumata",
    "polizza assicurativa multirischio e servizio di manutenzione e monitoraggio per almeno 10 anni, domanda prima dell'entrata in esercizio, energia non autoconsumata")
rep("7) risorse: larga quota destinata al Mezzogiorno (circa 80% dei fondi secondo le fonti di settore); alcune regioni hanno requisiti piu' ampi (es. Puglia: ISEE fino a 20.000 euro) con bandi regionali dedicati.",
    "7) risorse: per legge (D.M. 8/8/2023) l'80% delle risorse e' destinato al Mezzogiorno; esistono bandi regionali analoghi con requisiti propri (verificare sui portali regionali).")

# ---- TEE ----
rep("nati con l'obbligo per i distributori di energia elettrica e gas di conseguire obiettivi annuali di risparmio",
    "nati con i decreti interministeriali 20 luglio 2004 (elettrico e gas), che hanno posto obblighi annuali di risparmio energetico ai distributori")
rep("1) gli obbligati (distributori con clienti sopra soglia)",
    "1) gli obbligati sono i distributori di energia elettrica e di gas con piu' di 50.000 clienti finali ciascuno")
rep("3) i TEE hanno durata (tipicamente 5 anni, poi alcuni anni di conservazione secondo regole aggiornate) e prezzo di mercato fluttuante",
    "3) i TEE hanno durata e regole di conservazione definite periodicamente dal Ministero (verificare sempre le regole vigenti); con il D.M. MASE 21 luglio 2025 (in vigore dal 12/9/2025) sono fissati i nuovi obiettivi 2025-2030 (7,9 mln di TEE elettrico + 4,9 mln di TEE gas cumulati) ed e' introdotto il TEE virtuale, acquistabile dal GSE al prezzo fisso di 10 euro con vincolo di detenzione minima crescente dal 40% (2025) all'80% (2029); il prezzo di mercato dei TEE tradizionali e' fluttuante")
rep("- **Normativa:** D.Lgs 28/2011 (art. 7: meccanismo dei TEE e obblighi); regole GSE per la certificazione e il mercato (aggiornate periodicamente); direttiva EED di riferimento (2012/27/UE).",
    "- **Normativa:** D.M. 20 luglio 2004 (istituzione dei TEE, decreti gemelli elettrico e gas); D.Lgs 28/2011 art. 7 (obblighi raccordati di efficienza); D.M. MASE 21 luglio 2025 (nuovi obiettivi 2025-2030 e TEE virtuali, in vigore dal 12/9/2025); regole GSE per la certificazione e il mercato; direttiva EED di riferimento (2023/1791/UE).")

# ---- Diagnosi energetica ----
rep("### Diagnosi energetica e energy manager: gli obblighi D.Lgs 102/2014",
    "### Diagnosi energetica e energy manager: gli obblighi D.Lgs 102/2024")
rep("Il D.Lgs 102/2014 (attuazione della direttiva EED) impone: diagnosi energetica periodica alle grandi imprese e alle imprese energivore (scadenza dicembre degli anni dispari), con obbligo alternativo per piccole e medie (sistema di gestione energetico ISO 50001), e l'energy manager per grandi imprese e energivore.",
    "Il D.Lgs 102/2024 (recepimento della direttiva EED 2023/1791/UE, in vigore dal 10 ottobre 2025) ha riformato gli obblighi nazionali, sostituendo il D.Lgs 102/2014: diagnosi energetica obbligatoria ogni 4 anni per i soggetti con consumi pari o superiori a 10 TJ/anno (circa 2,78 GWh), sistema di gestione energetico ISO 50001 per consumi pari o superiori a 85 TJ/anno (circa 23,6 GWh). Il vecchio sistema (grandi imprese ed energivore, scadenza dicembre degli anni dispari) resta storico fino al 2025.")
old_tec = "- **Tecnologia e criteri:** Obblighi principali: 1) diagnosi energetica: audit completo del consumo energetico di impianti e edifici, ripetuto ogni 4 anni (scadenza dicembre anni dispari: 5 dicembre), redatto secondo la norma UNI CEI 16247 da ESCo certificata o professionista; 2) grandi imprese: soglia occupati >250 o fatturato >50 mln (con possibili aggiornamenti del decreto: verificare); 3) imprese energivore: quelle con consumi rilevanti (elenco MIMIT, es. settori energivori con consumi oltre soglia definita per codice ATECO); 4) alternative per le PMI: adozione di un sistema di gestione dell'energia certificato ISO 50001 o audit energetici di qualità secondo le regole; 5) energy manager: obbligatorio per grandi imprese ed energivore, anche per le PA con consumi rilevanti; funzioni: identificare risparmi, proporre investimenti, rendicontare; 6) sanzioni: amministrative (migliaia di euro) in caso di mancata diagnosi o data mancata comunicazione al MIMIT."
new_tec = "- **Tecnologia e criteri:** Obblighi verificati sul D.Lgs 102/2024: 1) DIAGNOSI ENERGETICA: audit completo dei consumi secondo la norma UNI CEI EN 16247, cadenza quadriennale per i soggetti con consumi >= 10 TJ/anno (circa 2,78 GWh); chi rientra per la prima volta deve effettuare la prima diagnosi entro l'11 ottobre 2026; chi era gia' obbligato mantiene la cadenza quadriennale con prossima scadenza 5 dicembre 2027; 2) SISTEMA DI GESTIONE DELL'ENERGIA: SGEn conforme alla UNI EN ISO 50001 obbligatorio per consumi >= 85 TJ/anno (circa 23,6 GWh), con adeguamento entro l'11 ottobre 2027 secondo le regole di transizione; 3) ENERGY MANAGER: la disciplina del nominativo esperto in gestione dell'energia resta richiamata per i soggetti con consumi rilevanti — verificare le soglie nei decreti attuativi vigenti prima di dichiarare l'obbligo; 4) STORICO (fino al 2025): grandi imprese (occupati > 250 E fatturato > 50 mln, entrambe le condizioni) ed energivore CSEA (consumi >= 2,4 GWh con incidenza costo energia/valore produzione >= 3%), con esenzione per chi aveva ISO 50001/14001/EMAS; sanzioni da 2.000 a 20.000 euro (mancata diagnosi) e da 4.000 a 40.000 euro (mancata comunicazione); 5) le comunicazioni ai registri/organismi competenti seguono i decreti attuativi vigenti."
rep(old_tec, new_tec)
rep("- **Normativa:** D.Lgs 102/2014 (efficienza energetica, recepimento direttiva EED); UNI CEI 16247 (diagnosi energetiche); decreti MIMIT con elenchi energivore e aggiornamenti soglie.",
    "- **Normativa:** D.Lgs 102/2024 (recepimento direttiva EED 2023/1791/UE, in vigore dal 10/10/2025); UNI CEI EN 16247 (diagnosi energetiche); UNI EN ISO 50001 (sistemi di gestione dell'energia); storico: D.Lgs 102/2014 e decreti MIMIT con gli elenchi energivore.")
rep("- **Nota di cantiere:** La scadenza della diagnosi è dicembre degli anni dispari: chi si muove a ottobre dell'anno scorso trova le ESCo disponibili; chi si muove a novembre dell'anno scadenza paga il sovrapprezzo e rischia la sanzione.",
    "- **Nota di cantiere:** Dal 2026 la prima domanda non e' piu' 'sei una grande impresa?' ma 'quanto consumi in TJ/anno?': raccogliere i consumi elettrici e termici dell'ultimo triennio (fatture) prima di dichiarare l'obbligo. Le scadenze chiave sono l'11 ottobre 2026 (prima diagnosi per i nuovi soggetti) e l'11 ottobre 2027 (ISO 50001 per i soggetti >= 85 TJ). Chi si muove con un anno di anticipo trova le ESCo disponibili; chi si muove a ridosso paga il sovrapprezzo e rischia la sanzione.")

io.open(P, 'w', encoding='utf-8').write(t)
print('OK: enciclopedia sincronizzata (7 voci)')
