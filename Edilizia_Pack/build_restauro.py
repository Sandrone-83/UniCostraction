# -*- coding: utf-8 -*-
"""Genera il corpus Restauro e Patologie: teoria, normativa e tecniche di consolidamento."""
import json, os

S = []

S.append(("teoria_restauro",
"TEORIA DEL RESTAURO - DALLA SINTESI ALLA CRITICA",
"""Il restauro architettonico nasce in Europa tra Settecento e Ottocento come riflessione sul trattamento dell'antico. Le posizioni fondamentali:

1. SINTESI STORICA (Viollet-le-Duc, 1814-1879): il restauro e' 'ristabilire in un completo stato che puo' non essere mai esistito'. Sostegno del razionalismo strutturale: la forma segue la funzione, anche a costo di ricostruzioni ipotetiche.

2. SCIENZA E STOICISMO (Boito, 1836-1914): camillo Boito propone il restauro come 'scienza', documentando stratigraficamente le aggiunte e distinguendo il ripristino dall'integrazione. Le aggiunte devono essere riconoscibili e documentate.

3. CRITICA STORICA (Beltrami, Luca Beltrami con la definizione 1893): il restauro come 'critica storica materializzata', rivolto alla ricostruzione della storia dell'opera piu' che alla sua forma.

4. TEOREMA DEL RESTAURO (Brandi, 1963): Cesare Brandi definisce il restauro come 'il momento metodologico del riconoscimento dell'opera d'arte, nella sua fisicita', nel contesto storico e estetico, in vista della sua trasmissione al futuro'. Principi: rispetto dell'opera come documento (le aggiunte rispettano la storia), il ripristino si limita all'integrazione di lacune senza cancellare il tempo.

5. RESTAURO CRITICO CONTEMPORANEO: la Carta di Venezia (1964), la Carta di Atene (1931), la Carta di Krakow (2000) e la Convenzione di Faro (2005) integrano la tutela con la valorizzazione e la partecipazione. Il restauro e' oggi reversibile, documentato, rispettoso della stratificazione.

Il dibattito continua tra conservazione, valorizzazione e innovazione."""))

S.append(("normativa_tutela",
"D.LGS 42/2004 - CODICE DEI BENI CULTURALI E DEL PAESAGGIO",
"""Il D.Lgs 22 gennaio 2004 n. 42 (e s.m.i.) e' la norma italiana di riferimento per la tutela dei beni culturali e del paesaggio. Punti chiave per l'edilizia:

1. AMBITO: beni culturali (artt. 10 ss.) sono gli edifici, le opere e le cose di interesse artistico, storico, archeologico, etnoantropologico; il paesaggio (artt. 131 ss.) sono i luoghi di rilevante interesse pubblico.

2. VINCOLI: dichiarazione di interesse culturale (vincolo diretto) o vincolo paesaggistico (VINCA per opere di pregio). In presenza di vincolo, qualsiasi modifica, anche interna, richiede l'autorizzazione del Ministero.

3. AUTORIZZAZIONI: per beni vincolati serve il nullaosta della Soprintendenza (art. 21), con tempi di 60-120 giorni e possibili prescrizioni su materiali, colori e tecniche.

4. SANZIONI: le opere eseguite in assenza di autorizzazione sono soggette a demolizione obbligatoria e sanzioni penali.

5. PROFESSIONISTI: i lavori su beni vincolati devono essere eseguiti da imprese abilitate al restauro, secondo la classificazione ministeriale.

Per il tecnico che opera su patrimonio storico la conoscenza di questo codice e' indispensabile prima di qualsiasi progetto."""))

S.append(("patologie_umidita",
"PATOLOGIE DA UMIDITA' - CAUSE E INTERVENTI",
"""L'umidita' e' la causa piu' diffusa di degrado nelle murature storiche. Le patologie principali:

1. RISALITA CAPILLARE: l'acqua sale dal terreno per capillarita' attraverso i pori dei materiali. Evidenze: alzata umida a basamento, muffa nei locali a piano terra, sfaldamento degli intonaci bassi. Interventi: barriera chimica orizzontale, intonaci deumidificanti, ventilazione del sottosuolo.

2. CONDENSA SUPERFICIALE: vapore acqueo interno che condensa su superfici fredde. Evidenze: muffa in angoli e dietro mobili, goccioline su finestre. Interventi: miglioramento isolamento, ventilazione (VMC), riduzione umidita' interna.

3. INFILTRAZIONE: acqua meteorica che entra attraverso coperture, cordoli, fessure. Evidenze: macchie umide dopo pioggia, lungo davanzali e cordoli. Interventi: ripristino tenuta copertura, sigillature, rinvigorimento cordoli.

4. SALI: cristallizzazione di sali solubili che porta a sfaldamento (alveolizzazione), distacco di intonaco, corrosione di malte. Evidenze: polveri bianche (efflorescenze) o croste scure. Interventi: rimozione croste, applicazione di sostanze consolidanti, barriera chimica.

5. DIAGNOSI: misura di umidita' (carburo di calcio, misure elettriche), termografia, rilievo percorso acqua. La diagnosi corretta e' la base per l'intervento mirato."""))

S.append(("patologie_strutturali",
"PATOLOGIE STRUTTURALI NELL'EDILIZIO STORICO",
"""Le patologie strutturali degli edifici storici derivano da azioni ambientali, sismiche, umane o da difetti di costruzione:

1. FESSURAZIONI STRUTTURALI: lesioni diagonali ai lati dei vani (cedimento dei carichi), lesioni verticali (cedimenti differenziali delle fondazioni), lesioni orizzontali (spinta del tetto). La mappatura delle fessure con data e larghezza e' essenziale per il monitoraggio.

2. DEFORMAZIONI: frecce eccessive nei solai di legno, inflessioni delle travi metalliche, deformazioni fuori piano dei muri (pericolose per l'instabilita' sismica).

3. DEGRADO MATERIALI: corrosione degli elementi metallici (travi di colmo, catene), carie e tarlatura del legno (in particolare sottotetti e solai), degrado delle malte storiche (malte aerea sostituite da cementizie che intrappolano umidita').

4. CAUSE UMANE: tagli strutturali non autorizzati, sovraccarichi, interventi con materiali incompatibili.

5. INTERVENTI DI CONSOLIDAMENTO: cerchiatura, intubamento, rinforzo fibre (FRP), iniezioni di malte speciali, sostituzione selettiva di elementi degradati, ammodernamento dei collegamenti.

La valutazione della sicurezza di un edificio storico richiede sempre un'indagine conoscitiva completa prima di qualsiasi intervento."""))

S.append(("materiali_storici",
"MATERIALI STORICI - LATERIZIO, CALCE E PIETRA",
"""I materiali storici definiscono il carattere dell'edilizio antico e richiedono specifiche competenze:

1. LATERIZIO: cotto pieno e semipieno, con varieta' regionali (mattone fiorentino, cotto lombardo, laterizio veneto). Caratteristiche: buona resistenza, permeabilita' al vapore, durabilita'. Problemi: degrado da sali, gelo-disgelo, sostituzioni con blocchi moderni incompatibili.

2. CALCE: la malta di calce aerea (grassello) e' il legante tradizionale: permeabile, flessibile, autorigenerante. Il cemento portland, introdotto alla fine dell'Ottocento, e' piu' rigido e impermeabile: l'applicazione su muratura storica intrappola umidita' e accelera il degrado. La ricetta della malta di calce (dosaggi 1:2 - 1:3) e' fondamentale per il restauro.

3. PIETRA: marmo, travertino, arenaria, tufo, granito. Problemi: degrado da smog (nitrati), cristallizzazione sali, corrosione di elementi metallici di ancoraggio. Interventi: pulitura (acqua, nebulizzazione, microsabbiatura con cautela), consolidamento, protezione.

4. LEGNO: essenze tradizionali (castagno, quercia, larice, abete). Degrado: carie, tarli, umidita'. Interventi: consolidamento con resine, sostituzione selettiva, trattamenti biocidi.

5. METALLI: ferro, acciaio, piombo, rame, ottone. Degrado: ruggine, corrosione galvanica. Interventi: sabbiatura, protezione con smalti specifici, sostituzione di parti corrode.

La conoscenza dei materiali e' il prerequisito per l'intervento conservativo."""))

S.append(("tecniche_consolidamento",
"TECNICHE DI CONSOLIDAMENTO DELLE MURATURE",
"""Le tecniche di consolidamento delle murature storiche mirano a migliorare la sicurezza senza alterare il carattere dell'edificio:

1. CERCHIATURA: inserimento di barre o catene di acciaio (o FRP) che legano i muri trasversalmente. Tipica per le pareti fuori piano: contrasta l'espulsione nel sisma.

2. INTUBAMENTO: inserimento di profili metallici o in FRP in fori orizzontali o verticali che collegano le pareti e migliorano la resistenza a taglio.

3. RINFORZO CON FRP (Fibre Reinforced Polymer): tessuti in fibra di carbonio o vetro incollati sulla superficie o inseriti in fessure (NSM - Near Surface Mounted). Vantaggi: leggerezza, reversibilita' relativa, minimo impatto visivo.

4. INIEZIONI DI MALTA: iniezione di malte cementizie o di calce per ripristinare l'aderenza tra il paramento e il nucleo del muro, colmare cavita' e fessure.

5. RIPRISTINO DEI GIUNTI: scalpellatura e rifacimento dei giunti con malte compatibili, per ripristinare la coesione della muratura.

6. RINFORZO DEGLI ANGOLI: inserimento di staffe o barre angolari per migliorare il comportamento sismico degli spigoli.

7. MONITORAGGIO: deformazione, fessurazione, vibrazioni, umidita' e temperatura. Il consolidamento e' sempre preceduto dalla diagnosi e seguito dal monitoraggio."""))

S.append(("restauro_legno",
"RESTAURO DELLE STRUTTURE IN LEGNO",
"""Il legno e' uno dei materiali piu' diffusi nel patrimonio storico (solai, tetti, travi). Il restauro richiede:

1. DIAGNOSI: ispezione visiva con rilievo del tipo di degrado (carie bianca, carie bruna, tarli, umidita'), misura dell'umidita' del legno (igrometro), valutazione strutturale con prove non distruttive (sclero, penetrometro, carotaggi).

2. CONSOLIDAMENTO: iniezioni di resine epossidiche per ricostruire le sezioni perse, applicazione di tessuti in fibra di carbonio (CFRP) per rinforzare le parti tese, sostituzione selettiva dei pezzi gravemente degradati con legno di specie compatibile.

3. PROTEZIONE: trattamenti biocidi contro funghi e insetti, vernici o impregnanti protettivi, controllo dell'umidita' con barriera vapore e ventilazione.

4. PRINCIPI: il restauro del legno deve essere reversibile (le aggiunte devono essere riconoscibili), documentato e rispettoso della storia dell'elemento. Le tecniche moderne (FRP, resine) sono accettabili se applicate con criterio e documentazione.

5. ESEMPI TIPICI: consolidamento di solai in legno di case rurali, ripristino di tetti in capriate di chiese e palazzi, rinforzo di travi in legno di solai urbani."""))

S.append(("restauro_coperture",
"RESTAURO DELLE COPERTURE STORICHE",
"""Le coperture sono l'elemento piu' esposto del patrimonio edilizio. Il restauro richiede:

1. DIAGNOSI: ispezione della struttura portante (legno, metallo, laterocemento), del manto (tegole, lastre, manti bituminosi), della tenuta all'acqua e della ventilazione.

2. RESTAURO DEL MANTO: recupero e riposizionamento delle tegole storiche (coppi, marsigliesi), sostituzione delle parti mancanti con pezzi di recupero o nuovi compatibili, ripristino della pendenza e dei colmi.

3. STRUTTURA: consolidamento del legno di copertura (vedi scheda dedicata), sostituzione dei cordoli ammalorati, ripristino degli ancoraggi e dei collegamenti al corpo murario.

4. TENUTA: posa di membrane traspiranti o di fasce di tenuta, ripristino della gronda e dei pluviali, controllo delle infiltrazioni.

5. INNOVAZIONE COMPATIBILE: inserimento di isolamento termico nella falda senza alterare l'aspetto esterno, con attenzione alla ventilazione e alla traspirabilita'.

6. DOCUMENTAZIONE: rilievo fotografico prima/dopo, schedatura dei materiali recuperati, carta di manutenzione per il proprietario.

Il restauro della copertura e' spesso l'intervento piu' urgente e dal maggiore impatto sulla sopravvivenza dell'edificio."""))

S.append(("architettura_rurale",
"L'ARCHITETTURA RURALE TRADIZIONALE ITALIANA",
"""L'architettura rurale italiana e' caratterizzata da sistemi costruttivi legati al clima, ai materiali locali e alle attivita' agricole:

1. MATERIALI: pietra locale, laterizio, legno, terra cruda, intonaci di calce. Ogni regione ha sviluppato tecniche specifiche (muri a secco in Liguria, cascine lombarde in mattoni, trulli pugliesi a secco).

2. TIPI EDILIZI: cascine (Lombardia, Piemonte), masserie (Puglia), palmenti (Sicilia), baiti (Alpi), fienili, stalle, tabaccare.

3. STRUTTURE: muri portanti in pietra o laterizio, solai in legno a travi e travicelli, coperture a falde in legno e tegole o lastre di pietra.

4. RESTAURO: la conservazione dell'architettura rurale richiede il recupero dei materiali originali, il ripristino delle tecniche tradizionali e l'inserimento discreto di impianti moderni. La destinazione a nuovi usi (agriturismo, residenza) deve rispettare la tipologia.

5. PROBLEMATICHE: abbandono e degrado, sismicità delle zone rurali, umidità di risalita, incompatibilità di interventi moderni.

Il restauro dell'architettura rurale e' un settore specialistico che richiede la conoscenza delle tecniche tradizionali e dei materiali locali."""))

os.makedirs('parsed', exist_ok=True)
meta = {
    "source": "restauro_patologie_kimi",
    "license": "Sintesi didattica originale Kimi (pubblico dominio)",
    "commercial_ok": True,
    "attribution": "Corpus restauro e patologie a cura di Kimi",
    "url": "",
}
out = []
for i, (tema, titolo, testo) in enumerate(S, 1):
    rec = dict(meta)
    rec.update({"id": f"REST-{i:02d}", "tema": tema, "title": titolo, "text": testo.strip()})
    out.append(rec)

path = 'parsed/restauro_patologie.jsonl'
with open(path, 'w', encoding='utf-8') as f:
    for r in out:
        f.write(json.dumps(r, ensure_ascii=False) + '\n')
print(f"scritte {len(out)} schede restauro -> {os.path.abspath(path)}")
