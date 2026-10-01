# -*- coding: utf-8 -*-
"""URBANISTICA_TERRITORIO_PACK: strumenti urbanistici, vincoli, procedure, attuazione."""
import json, os

ROOT = os.path.dirname(os.path.abspath(__file__))

def s(cat, nome, desc, tec, app, van, lim, cos, casi, norm, note):
    return dict(categoria=cat, nome=nome, descrizione=desc, tecnologia=tec,
                applicazioni=app, vantaggi=van, limiti=lim, costi_e_economia=cos,
                casi_real_world=casi, normative=norm, note_cantiere=note)

DATA = [
s("Principi", "Il governo del territorio: principi costituzionali",
 "L'urbanistica italiana si fonda sugli artt. 42 e 44 della Costituzione: proprietà pubblica e privata riconosciuta ma con funzione sociale, che può essere vincolata in base ai piani; l'art. 117 attribuisce la pianificazione territoriale alle Regioni.",
 "Gerarchia: Costituzione → leggi statali quadro (L. 1150/1942, L. 765/1967) → leggi regionali di settore → strumenti comunali; il principio di leale collaborazione vincola i livelli; la giurisprudenza costituzionale e della Cassazione completa il quadro.",
 "Qualsiasi intervento sul territorio: prima di progettare si verifica COSA il piano consente.",
 "I principi fermi permettono di interpretare le infinite variabili locali: chi conosce i principi ragiona, chi conosce solo il regolamento del proprio comune resta prigioniero.",
 "La frammentazione normativa (8.000 comuni, 20 regioni) rende la verifica locale sempre indispensabile.",
 "Costo: cultura (zero) o parere urbanistico da tecnico locale: 200-800 €.",
 "Operatore che ha verificato solo il regolamento edilizio e non la legge regionale: progetto rifiutato per un vincolo di legge regionale sui corpi soggetti a distanza dalle strade, non presente nel regolamento comunale.",
 "Artt. 42, 44, 117 Cost.; L. 1150/1942; L. 765/1967; L. 241/1990.",
 "La prima domanda professionale su un terreno: 'cosa dice il piano vigente?' — prima ancora di pensare al progetto."),
s("Strumenti", "Gli strumenti urbanistici: PSC, Piano operativo, Piano regolatore",
 "Lo strumento fondamentale è il Piano Strutturale Comunale (PSC, dove adottato) o il vecchio PRG: il PSC detta destinazioni d'uso, vincoli e indirizzi; il piano operativo (o le NTA del PRG) traducono in regole numerate (indici, altezze, distanze, copertura).",
 "Elementi tipici delle NTA: destinazioni d'uso zonizzate, indice di fabbricabilità (m²/m²), indice di copertura (%), altezza massima, distanze dai confini (per legge: 3 m, salvo deroghe locali e rapporti di reciproco rispetto), frazionamenti minimi, standards e dotazioni, vincoli di salvaguardia.",
 "Verifica di fattibilità di interventi, compravendite, pratiche edilizie, opposizioni a varianti.",
 "Le regole scritte del piano sono oggettive: se un progetto rispetta i numeri, il rifiuto deve motivare eccezioni reali, non gusti.",
 "I piani sono spesso datati o inadeguati alla realtà: le varianti sono lente; l'operatore deve saper lavorare anche con strumenti imperfetti (conformità al piano VIGENTE, non a quello 'che dovrebbe arrivare').",
 "Costo verifica urbanistica pre-acquisto: 300-1.000 €; pratica edilizia completa: 1.500-6.000 € onorario tecnico.",
 "Acquisto terreno con 'vista lago' a prezzo pieno: il piano lo classificava zona agricola vincolata (non edificabile): un controllo di 500 € avrebbe risparmiato 300.000 €.",
 "L. 1150/1942 (fondamenti); leggi regionali urbanistiche (una per regione); NTA comunali.",
 "Regole d'oro: mai comprare su promesse verbali ('il comune fa variante'), mai costruire sul piano che non c'è."),
s("Standards", "Gli standards urbanistici e le dotazioni",
 "Le leggi (DM 1444/1968 e leggi regionali) fissano gli standard minimi di servizi urbani per abitante: scuole ( mq/abitante), verde, parcheggi, servizi sociali, deporti; sui nuovi insediamenti il privato deve dotarli o versare un contributo in sostituzione.",
 "Calcolo: il progettista dimensiona l'intervento → ricava gli standard dovuti (es. 25 m²/abitante di verde pubblico, da verificare nella legge regionale) → li realizza o versa il contributo commisurato (spesso valutato sul costo di realizzazione); alcune regioni usano standard 'privatizzabili' (servizi nell'edificio) vs pubblici (aree da consegnare al Comune).",
 "Lottizzazioni, nuovi quartieri, ampliamenti residenziali, trasformazioni edilizie complesse.",
 "Gli standard sono il vero costo nascosto delle lottizzazioni: chi li dimentica nel business plan scopre in corso d'opera che il margine è finito nelle aree pubbliche.",
 "I valori standard variano per regione e per tipo di intervento: la verifica è sempre locale.",
 "Impatto tipo: aree pubbliche + contributi = 10-20% della superficie o equivalente monetario (ordine di grandezza, da calcolare caso per caso).",
 "Lottizzazione con business plan senza standards: gli oneri (aree + contributi) hanno assorbito il 22% del valore invece del 12% ipotizzato: margine azzerato e rientro negli anni.",
 "DM 1444/1968 (standards minimi); leggi regionali (valori aggiornati); regolamenti comunali edilizi.",
 "Domanda da insegnare al LLM: 'in questa commessa, chi paga scuole, verde, strade e parcheggi — e quanto?'"),
s("Vincoli", "I vincoli: paesaggistico, idrogeologico, archeologico, naturalistico",
 "Il territorio è attraversato da vincoli sovrapposti: paesaggistico (Codice dei beni culturali, D.Lgs 42/2004: nulla osta Soprintendenza per quasi tutto il territorio italiano), idrogeologico (aree di pericolosità PAI/PGR, zone rosse/frane), archeologico (archeologia preventiva, art. 28 D.Lgs 42/2004), naturalistico (reti Natura 2000, parchi), vincoli idraulici (fasce fluviali).",
 "Verifica a strati: cartografie regionali (PAI), banca dati vincoli Soprintendenza (sigec web), carta Natura 2000, regolamenti di fascia fluviale; per opere soggette a vincolo paesaggistico: Autorizzazione paesaggistica semplificata o ordinaria PRIORA del titolo edilizio; scavi con possibilità archeologica: presenza archeologica all'apertura degli scavi (reperibilità).",
 "Qualsiasi intervento edilizio e viario; in Italia il vincolo paesaggistico copre la stragrande maggioranza del territorio (circa il 95% secondo le stime del settore).",
 "Conoscere i vincoli PRIMA di comprare o progettare evita due disastri: il progetto impossibile e il terreno invendibile.",
 "La stratificazione rende la verifica complessa: possono esserci più vincoli sovrapposti sullo stesso metro quadro, ognuno con la sua procedura.",
 "Costo verifica completa (geologo + archeologo dove serve + istruttoria): 1.000-8.000 € a seconda dell'intervento.",
 "Villa progettata senza verifica archeologica: durante gli scavi emerge strada romana; lavori fermi 8 mesi per scavo preventivo con sorveglianza: costo imprevisto 120.000 € e ritardo analogo.",
 "D.Lgs 42/2004 (Codice beni culturali); D.Lgs 152/2006 (acque, fasce fluviali); direttive reti Natura 2000; leggi regionali paesaggistiche.",
 "La mappa dei vincoli si verifica SEMPRE per iscritto (visure e carte ufficiali), mai 'a memoria' o 'il geometra di zona dice'."),
s("Procedure", "Le procedure edilizie: CILA, SCIA, Permesso di costruire",
 "Il titolo abilitativo dipende dall'intervento: Permesso di costruire (opere nuove, ristrutturazioni che aumentano il volume/superficie utilizzando l'edificabilità residua), SCIA (opere di ristrutturazione ordinaria senza aumento di superficie, opere interne), CILA/CIL (piccoli interventi, manutenzione straordinaria secondo leggi regionali), DIA (soppressa, ma ancora citata).",
 "Iter tipo: progetto a firma di professionista abilitato → presentazione al SUAP con modulistica unificata → integrazioni → (per il permesso) il Comune approva o tace-rifiuta → inizio lavori con comunicazione → fine lavori con asseverazione di regolare esecuzione → agibilità → variazione catastale; i termini variano da Regione a Regione (da 30 a 90 giorni tipici).",
 "Ogni cantiere: la scelta sbagliata del titolo è la causa più comune di abusi edilizi.",
 "La tracciabilità delle procedure protegge tutti: un lavoro regolare ha valore legale e vendibile; quello irregolare è un passivo.",
 "I termini e le categorie cambiano per legge regionale: la classificazione dell'intervento va verificata ogni volta, non ricordata.",
 "Costo pratica: onorario tecnico 1.500-6.000 €; diritti comunali: centinaia di euro in genere.",
 "Veranda chiusa 'senza permesso, tanto è CILA': in realtà aumentava superficie utile → permesso richiesto → demolizione coatto e sanzione pecuniaria: 40.000 € tra sanzione, demolizione e rifacimento.",
 "DPR 380/2001 (Testo Unico Edilizia); leggi regionali di attuazione; regolamenti edilizi comunali.",
 "La prima verifica di ogni intervento: classificazione (manutentiva/ordinaria/straordinaria) + destinazione d'uso + rispetto regolamento: questi tre numeri decidono TUTTO il percorso."),
s("Edilizia libera", "L'edilizia libera e le variazioni catastali",
 "Alcuni interventi sono LIBERI (nessun titolo, comunicazione al Comune): opere interne senza modifiche di destinazione e senza alterazione dei prospetti (zone umide escluse), finiture, impianti equivalenti; la fine lavori resta documentata e la variazione catastale è comunque obbligatoria quando cambiano le consistenze.",
 "Regola pratica: se non si toccano struttura, prospetti e destinazioni d'uso (e si sta fuori zone vincolate o tutelate), spesso si è in edilizia libera; la variazione catastale (tipo mappale o DOCFA) aggiorna le planimetrie e le consistenze: obbligatoria per legittimità dell'immobile.",
 "Rimodulazioni interne, aggiornamenti catastali, opere da documentare senza iter completo.",
 "Il libero NON significa irregolare: documentare sempre con foto prima/dopo, computo delle opere e dichiarazione del tecnico.",
 "Confondere 'libero' con 'invisibile' è il classico abuso: l'abuso edilizio si configura anche senza opere esterne (es. bagno in zona umida o nuova camera in mansarda).",
 "Costo: nulla per il titolo; variazione catastale: 300-800 € tecnico + diritti.",
 "Appartamento con cucina spostata in veranda chiusa anni prima: all'atto di vendita, il catastale non quadrava e l'accatastamento richiedeva sanatoria: trattativa con sconto di 25.000 € al compratore per la pratica da fare.",
 "DPR 380/2001 (art. 6); normativa catastale (DPR 223/1989); regolamento DOCFA.",
 "Domanda obbligatoria per il LLM: 'questo intervento altera struttura, prospetti o destinazioni d'uso?' — le tre risposte decidono la strada."),
s("Attuazione", "L'attuazione urbanistica: lottizzazioni, convenzioni, piani di recupero",
 "Gli strumenti di attuazione trasformano il piano in opere: lottizzazione convenzionata (l'imprenditore costruisce infrastrutture e standard in cambio delle aree edificabili), piani di recupero (edilizia consolidata), programmi integrati, PEEP; il Comune guida, il privato finanzia, convenzione regola diritti e obblighi.",
 "Fasi: proposta → convenzione urbanistica con oneri e tempi → esecuzione opere pubbliche/standard → lotti edificabili → cessione o costruzione; clausole critiche: tempi di attuazione, obblighi di realizzazione infrastrutture, penali, cessioni a titolo gratuito delle aree pubbliche.",
 "Sviluppo immobiliare, trasformazione di aree industriali dismesse, recupero di borghi e centri storici.",
 "La convenzione giusta allinea Comune e investitore: ognuno sa cosa deve fare, quando e a quale costo.",
 "I tempi della pubblica amministrazione possono congelare il capitale per anni: il piano economico deve prevedere anche lo scenario 'attuazione lenta'.",
 "Costi di attuazione (opere pubbliche, standard, oneri): 15-30% del valore di trasformazione (ordine di grandezza); tempi: 2-8 anni.",
 "Recupero di ex area industriale: convenzione con standard privatizzati (parcheggi interni, servizi nell'edificio) invece di aree pubbliche: l'attuazione è durata 3 anni invece dei 7 stimati con la cessione tradizionale.",
 "DPR 380/2001 (titoli attuativi); leggi regionali; prassi convenzionale locale.",
 "La regola d'oro dello sviluppatore: il valore si crea nell'attuazione, non nel terreno — e l'attuazione è al 90% relazioni con la pubblica amministrazione."),
s("Valutazione", "VAS, VIA e la valutazione ambientale degli interventi",
 "Gli interventi con impatto significativo subiscono la Valutazione di Impatto Ambientale (VIA) o, a livello di piano, la Valutazione Ambientale Strategica (VAS): un processo che valuta alternative, impatti e misure di mitigazione PRIORA dell'approvazione.",
 "Screening: il decreto VIA elenca i soggetti (opere sopra soglie dimensionali: strade, ponti, grandi insediamenti, discariche...); iter: presentazione studio di impatto → consultazioni (Soprintendenza, ARPA, enti) → conferenza di servizi → provvedimento autorizzatorio VIA che vincola il progetto definitivo; tempi: 90-180 giorni tipici.",
 "Infrastrutture, grandi edilizie, opere industriali, modifiche al territorio di rilievo.",
 "La VIA fatta bene riduce i ricorsi: le istanze di contrasto si esauriscono nel processo, non nei tribunali anni dopo.",
 "La valutazione è onerosa e incerta: progetti di dubbia qualità ambientale muoiono dopo aver speso centinaia di migliaia di euro di studi.",
 "Costo studi VIA: 20.000-200.000 € a seconda della complessità; tempi totali con iter: 1-3 anni.",
 "Centro commerciale: la VIA ha imposto compensazioni ambientali (riqualificazione di area retrostante e bonifica) pari al 4% dell'investimento: il progetto è partito con la piena copertura autorizzativa, zero ricorsi.",
 "D.Lgs 152/2006 parte seconda (VIA); D.Lgs 104/2017 (modifiche); linee guida europee (direttiva 2011/92/UE).",
 "Per il LLM: saper dire 'questo progetto probabilmente richiede VIA, e queste sono le alternative da studiare' è consulenza di alto livello — chi scopre la VIA dopo aver comprato il terreno ha già perso."),
s("Edilizia pubblica", "Edilizia residenziale pubblica e housing sociale",
 "L'edilizia pubblica abitativa è tornata centrale: ERP (edilizia residenziale pubblica) con assegnazione a canone calmierato, housing sociale (bandi regionali e nazionali con risorse PNRR), riqualificazione del patrimonio pubblico esistente (borgate, case popolari anni '50-'70).",
 "Strumenti: bandi per nuova costruzione ERP (spesso con terreni pubblici concessi a canone), programmi di riqualificazione energetica e antisismica del patrimonio ERP, housing sociale con operatori no-profit e cooperativi; i requisiti: fasce ISEE per assegnazione, standard di qualità più alti del passato (certificazioni energetiche elevate).",
 "Comuni, regioni, social housing operatori, imprese che partecipano ai bandi.",
 "Il patrimonio ERP è una miniera di commesse: riqualificare il costruito esistente pubblico è una pipeline di lavoro per il prossimo decennio (PNRR e fondi nazionali).",
 "La complessità amministrativa dei bandi pubblici filtra via le imprese piccole: serve consulenza o associazione temporanea.",
 "Referenza: i bandi ERP regionali coprono in genere quote importanti del costo di costruzione/riqualificazione; verificare i bandi vigenti.",
 "Torre di edilizia popolare anni '60 riqualificata (cappotto, serramenti, impianti, ricomposizione distributiva): assegnazioni passate da 40% a 100% di occupazione in 2 anni, con riduzione dei costi energetici per le famiglie del 55%.",
 "Normativa ERP nazionale e regionale; PNRR (fondi housing); regolamenti di assegnazione comunali.",
 "Il segmento pubblico residenziale premia chi sa lavorare con la PA: tempi lunghi ma commesse solide e ricorrenti."),
s("Riqualificazione", "Riqualificazione urbana: contratti di quartiere, periferie, rigenerazione",
 "La politica urbana nazionale degli ultimi decenni si è concentrata sulla riqualificazione: Contratti di Quartiere (anni 2000), Bando Periferie (2016-2022), Contratti di Fiume, rigenerazione urbana e sociale: interventi integrati su edilizia, spazi pubblici, servizi e coesione sociale nei quartieri degradati.",
 "Caratteristiche comuni: finanziamento statale/regionalo vincolato a programmi INTEGRATI (non solo opere: anche servizi, inclusione, gestione successiva); governance con tavoli di quartiere; opere tipiche: demolizioni selettive, rigenerazione di edilizi esistente, spazi pubblici, infrastrutture sociali; la gestione post-intervento (chi cura?) è il punto critico riconosciuto dai bandi stessi.",
 "Comuni in difficoltà, aree periferiche degradate, grandi proprietà pubbliche da rilanciare.",
 "I programmi integrati funzionano dove il 'fai edilizia e basta' ha fallito: la chiave è il mix fisico + sociale + gestionale.",
 "La fragilità di gestione post-opera lascia molti interventi abbandonati dopo pochi anni: il progetto serio include il piano di gestione.",
 "Investimenti tipici: da milioni a decine di milioni per quartiere, con copertura statale che ha variato dal 50% al 100% secondo i bandi.",
 "Quartiere con Bando Periferie: riqualificazione di 12 edilizi, parchi, una casa di quartiere con servizi: dopo 3 anni, la percezione di sicurezza dei residenti è migliorata sensibilmente (rilevazioni comunali) e il mercato immobili locale si è riattivato.",
 "Bando Periferie (DPCM 2016 e ss.); normativa contratti di quartiere; linee guida rigenerazione urbana PNRR.",
 "Lezione centrale per il LLM: gli edifici non bastano — la rigenerazione vera è fisica + sociale + economica, e dura più della pavimentazione nuova."),
]

README = """# URBANISTICA_TERRITORIO_PACK — Urbanistica, territorio e procedure

**Facoltà:** FACOLTA_GESTIONE_SISTEMA · **Livello:** L2 · **Schede:** {n}

## Contenuto
Il ramo territoriale dell'università: principi costituzionali e leggi quadro,
strumenti urbanistici (PSC/PRG/NTA), standards e dotazioni (DM 1444/68),
vincoli sovrapposti (paesaggistico, idrogeologico, archeologico, naturalistico),
procedure edilizie (CILA/SCIA/Permesso), edilizia libera e catasto,
attuazione (lottizzazioni, convenzioni), VIA/VAS, edilizia residenziale pubblica
e riqualificazione urbana (Periferie, Contratti di quartiere).

## Formato
- `schede/schede.jsonl` — una scheda per riga, 11 campi standard.
- `COURSE.yaml` — metadati del corso.

## Uso per l'addestramento
Adatto a: verifiche di fattibilità, conversazioni su terreni e procedure,
lettura di regolamenti edilizi, supporto a compravendite immobiliari.
Le regole edilizie variano per regione e comune: questo corso insegna la
STRUTTURA del ragionamento, da completare con la norma locale vigente.
""".format(n=len(DATA))

COURSE = """corso: "Urbanistica, territorio e procedure edilizie"
facolta: "FACOLTA_GESTIONE_SISTEMA"
livello: "L2"
schede: {n}
formato: "JSONL"
lingua: "it"
schema_campi: [categoria, nome, descrizione, tecnologia, applicazioni, vantaggi, limiti, costi_e_economia, casi_real_world, normative, note_cantiere]
""".format(n=len(DATA))

os.makedirs(os.path.join(ROOT, "schede"), exist_ok=True)
with open(os.path.join(ROOT, "schede", "schede.jsonl"), "w", encoding="utf-8") as f:
    for d in DATA:
        f.write(json.dumps(d, ensure_ascii=False) + "\n")
with open(os.path.join(ROOT, "README.md"), "w", encoding="utf-8") as f:
    f.write(README)
with open(os.path.join(ROOT, "COURSE.yaml"), "w", encoding="utf-8") as f:
    f.write(COURSE)
print("OK", len(DATA), "schede")
