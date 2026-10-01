# -*- coding: utf-8 -*-
"""VERDE_ARREDO_URBANO_PACK: verde urbano, coperture verdi, arredo urbano, irrigazione, essenze."""
import json, os

ROOT = os.path.dirname(os.path.abspath(__file__))

def s(cat, nome, desc, tec, app, van, lim, cos, casi, norm, note):
    return dict(categoria=cat, nome=nome, descrizione=desc, tecnologia=tec,
                applicazioni=app, vantaggi=van, limiti=lim, costi_e_economia=cos,
                casi_real_world=casi, normative=norm, note_cantiere=note)

DATA = [
s("Verde urbano", "Il verde urbano: funzioni, benefici, progetto",
 "Il verde in città non è decorazione: è infrastruttura ecologica: mitiga isola di calore (le superfici verdi sono più fresche fino a 10-15 °C rispetto all'asfalto in estate), assorbe acqua piovana, filtra inquinanti, produce benessere psicofisico documentato, incrementa il valore immobiliare circostante (stima ricorrente: fino al 10-15% per prossimità a parchi di qualità).",
 "Progetto: gerarchia del verde (alberi ad alto fusto lungo le strade, arbusti nelle aiuole, tappeti erbosi dove usati), la scelta delle essenze adatte al contesto urbano (resistenza a siccità, inquinamento, compattazione del terreno), i sistemi di irrigazione automatica, la manutenzione programmata come parte del progetto; gli standard urbanistici obbligano dotazioni di verde pubblico negli interventi nuovi.",
 "Parchi urbani, giardini di edifici, strade alberate, aiuole, cortili, aree industriali.",
 "Il verde è l'unica infrastruttura che cresce di valore con gli anni: un albero piantato oggi rende servizi per decenni.",
 "Il verde mal progettato (essenze sbagliate, manutenzione assente) diventa un passivo: alberi che cadono, aiuole infestate.",
 "Costi: impianto giardino urbano 80-250 €/m²; manutenzione 5-20 €/m²/anno; un albero ad alto fusto piantumato: 200-800 €.",
 "Strada alberata con platani maturi: la temperatura estiva misurata a 2 m dal suolo è 6-8 °C inferiore alla strada parallela senza alberi; i negozi della strada alberata segnalano maggiore permanenza dei clienti nei mesi caldi.",
 "Standard DM 1444/68 e leggi regionali; linee guida verde urbano comunali; norme paesaggistiche.",
 "Prima regola del verde urbano: si pianta pensando a come sarà tra 20 anni, non a come appare oggi."),
s("Progettazione giardino", "La progettazione del giardino: i principi del progetto verde",
 "Il giardino si progetta come l'architettura: funzione (gioco, relax, produzione), gerarchia spaziale (aree definite da siepi e percorrenze), successione cromatica e di fioriture, rapporto tra pieni e vuoti; il 'verde architettonico' usa le piante come materiali costruttivi (seto, soffitto, pavimento).",
 "Metodo: analisi sito (esposizione, terreno, clima), definizione delle zone e dei percorsi (camminamenti 80-120 cm), la tavola delle essenze con schema di impianto (distanze di piantagione: es. siepi ogni 40-80 cm secondo specie), i sistemi tecnici (irrigazione, illuminazione), la progettazione della manutenzione (chi cura e come); le piante vanno scelte per ADATTAMENTO, non per moda.",
 "Giardini privati, condomini, aziende, giardini terapeutici, cortili scolastici.",
 "Il giardino ben progettato vive con poca acqua e poca manutenzione: la sostenibilità inizia dalle scelte correttive.",
 "Il giardino 'da rivista' con essenze non adattate al clima muore entro 2-3 anni o diventa un pozzo di soldi.",
 "Costo progettazione giardino: 5-15% del valore dell'impianto; impianto completo residenziale: 100-300 €/m².",
 "Giardino mediterraneo sostituito a prato inglese in una villa: consumo idrico da 8.000 a 1.200 €/anno, manutenzione quasi dimezzata, valore estetico salito per coerenza con il contesto.",
 "Nessuna norma cogente salvo standard urbanistici; prassi di settore (architettura del paesaggio).",
 "Domande guida: chi usa questo giardino? quanta acqua e manutenzione possiamo permetterci? cosa resterà tra 10 anni senza interventi eroici?"),
s("Coperture verdi", "Le coperture verdi: tetti giardino",
 "I tetti giardino trasformano la copertura in spazio verde: stratigrafia a rovescio su piano orizzontale: protezione radici, drenaggio, filtro, substrato colturale, vegetazione; i benefici: isolamento termico aggiuntivo, ritenzione delle acque piovane, protezione della guaina (raddoppia la vita), nuovo spazio utilizzabile.",
 "Tipi: estensivo (substrato 8-15 cm, piante rustiche sedum/graminacee, manutenzione minima, non calpestabile), intensivo (substrato 20-40+ cm, vero giardino con arbusti, accessibile, manutenzione completa); il progetto verifica: il porto strutturale del solaio (i tetti intensivi pesano 150-300+ kg/m² saturi), l'impermeabilizzazione verificata, l'irrigazione di soccorso, i dettagli di bordo e gli ancoraggi contro il vento.",
 "Edifici residenziali, uffici, coperture di box, serre, strutture commerciali.",
 "Il tetto verde protegge la guaina dal sole e dagli sbalzi: la vita dell'impermeabilizzazione passa da 15-20 a 40+ anni (stima di settore).",
 "Il peso è il limite decisivo: su solai vecchi non rinforzati il tetto verde intensivo è impossibile; la valutazione strutturale precede ogni entusiasmo.",
 "Costi: estensivo 60-120 €/m²; intensivo 150-350 €/m²; il risparmio energetico estivo: sensibile sulle coperture esposte.",
 "Ufficio con tetto estensivo: la temperatura interna sotto copertura in estate è scesa di 4-5 °C con minore uso di climatizzazione; la guaina, verificata a 12 anni, era come nuova sotto il substrato.",
 "UNI EN 12056? No: riferimento normativo: norme sui tetti verdi (linee guida nazionali e specifiche FLL tedesche di riferimento internazionale); verifica strutturale NTC.",
 "La sequenza corretta: struttura → impermeabilizzazione (verificata in condizioni reali) → sistemi → piante: mai invertire l'ordine."),
s("Pareti verdi", "Le pareti verdi e i giardini verticali",
 "I giardini verticali portano il verde in su: pannelli modulari o feltri stratificati ancorati a parete con impianto di irrigazione integrato; il verde verticale raffredda la parete d'estate (l'evapotraspirazione toglie calore), isola acusticamente, depura l'aria percettibilmente.",
 "Sistemi: moduli a cassette (piante singole sostituibili, manutenzione facile), feltri tecnici (stratificati con irrigazione a goccia e nutrimento liquido), il supporto strutturale e il distacco dalla parete (ventilazione, accesso), l'impianto di irrigazione con recupero dell'acqua; le essenze: rustiche e di piccola taglia (felci, erbacee perenni, piante da ombra secondo esposizione).",
 "Facciate di edifici, pareti interne di atri, barriere acustiche verdi, spazi commerciali.",
 "Il giardino verticale trasforma una parete anonima in habitat: valore estetico e ambientale insieme.",
 "L'impianto di irrigazione è il cuore: se si guasta, il muro muore in settimane; la manutenzione richiede specialisti.",
 "Costi: 400-900 €/m² installato (moduli, ordini di grandezza variabili); manutenzione: 10-30 €/m²/anno.",
 "Parete verde in un atrio d'ufficio: la qualità dell'aria percepita migliorata e le temperature estive della parete orientata a ovest ridotte di 8 °C in superficie; l'irrigazione con centralina e recupero condensa consuma pochissimo.",
 "Nessuna norma specifica nazionale; specifiche dei sistemi e verifica strutturale degli ancoraggi.",
 "Regole: irrigazione ridondante (doppia linea o backup), accesso per la sostituzione delle cassette, essenze per l'esposizione reale."),
s("Arredo urbano", "L'arredo urbano: panchine, giochi, ciclabili, illuminazione",
 "L'arredo urbano qualifica lo spazio pubblico: panchine e sedute, giochi per bambini (con norme di sicurezza UNI EN 1176), arredi per anziani, fontane, ciclobox, tavoli, segnaletica, superfici drenanti; la qualità dell'arredo decide l'uso dello spazio: arredi brutti o rotti = spazio abbandonato.",
 "Criteri: materiali durevoli e poco manutentivi (legno di latifoglie, acciaio zincato e verniciato, ghisa), la disposizione (le sedute devono guardare qualcosa: la 'teoria dello sguardo' di Whyte), la sicurezza (giochi certificati, superfici di riassorbimento: gomma o sabbia con spessori UNI), l'illuminazione integrata, la manutenzione programmata (il legno va oliato, l'acciaio ritoccato).",
 "Piazze, parchi, lungomari, aree di sosta, cortili condominiali.",
 "L'arredo giusto anima lo spazio: una piazza con sedute comode e ombra viene usata; una piazza senza arredi no, anche se 'nuova'.",
 "L'arredo mal scelto diventa pericoloso o vandalico: i giochi non certificati espongono a responsabilità penali.",
 "Costi: panchina 200-800 €, gioco certificato 800-5.000 €, fontana da 3.000 € in su; la manutenzione annua: 5-10% del valore.",
 "Piazza riqualificata con sedute orientate verso il centro, ombra e giochi certificati: il tasso di utilizzo (conteggi) è triplicato e le lamentele per degrado sono azzerate.",
 "UNI EN 1176/1177 (giochi e superfici); norme locali di arredo urbano; specifiche dei produttori.",
 "La prima regola dell'arredo: disegnare per l'uso, non per la foto — sedute sotto il sole battente senza ombra non le userà nessuno."),
s("Pavimentazioni permeabili", "Le pavimentazioni esterne permeabili: l'acqua che torna nel terreno",
 "Le superfici permeabili (autobloccanti drenanti, ghiaia stabilizzata, erba rinforzata, conglomerati drenanti) lasciano infiltrare l'acqua: riducono la portata in rete fognaria, alimentano la falda, evitano ristagni e ghiaccio; dove il suolo non drena, servono sistemi di accumulo sotto la pavimentazione (vasche di laminazione).",
 "Sistemi: autobloccanti con giunto ghiaia (classici, economici, drenanti), masselli drenanti con fondo a ghiaia grossa, ghiaia stabilizzata con leganti (economica, rustica), grigliati in plastica o calcestruzzo con erba (per parchi e piste); il progetto prevede: il substrato drenante (30-50 cm di pietrisco), i bordi di contenimento, la pendenza verso le aree di laminazione.",
 "Parcheggi, vialetti, piste ciclabili, giardini, aree di sosta camper, piazze parzialmente.",
 "Il parcheggio permeabile elimina il tombamento? No: elimina l'acqua che ristagna: il ghiaccio invernale e le pozze scompaiono.",
 "La permeabilità richiede manutenzione: il giunto si intasa di terra e foglie perdendo efficienza (spazzolatura annuale).",
 "Costi: pari o inferiore ai masselli tradizionali (i sistemi drenanti hanno lo stesso costo base, si risparmia sulla fogna); la manutenzione: irrisoria.",
 "Parcheggio condominiale rifatto con autobloccanti drenanti e vasca di laminazione sotto: l'acqua piovana non va più in rete (zero allagamenti garage a valle) e la quota di smaltimento fognario è stata ridotta.",
 "Normativa sul deflusso (leggi regionali e regolamenti comunali); specifiche produttori.",
 "La domanda progettuale: 'dove va l'acqua che cade qui?' — se la risposta è 'nella fogna', valutare il permeabile."),
s("Irrigazione", "L'irrigazione: sistemi e progettazione",
 "L'irrigazione moderna è a goccia e programmata: consuma il 30-60% in meno dell'aspersione tradizionale, distribuisce l'acqua alle radici dove serve; il cuore è la centralina con elettrovalvole a zone, il progetto divide il giardino in zone omogenee (sole/ombra, prato/aiuole).",
 "Componenti: centralina (programmabile, con sensore pioggia che sospende dopo pioggia sufficiente), elettrovalvole a zone, tubazioni in polietilene, gocciolatori o microspruzzatori per le aiuole, irrigatori statici o dinamici per i prati; il dimensionamento: portata disponibile (da contatore) vs portata delle zone (ogni zona entro i limiti), i filtri e la fertirrigazione integrabile.",
 "Giardini privati, parchi, coperture verdi, campi sportivi, agricoltura urbana.",
 "L'irrigazione programmata col sensore pioggia: risparmio idrico garantito e piante più sane (meno funghi per foglie bagnate).",
 "Il sistema mal dimensionato (zone troppo grandi) dà pressioni basse e coperture a macchia di leopardo.",
 "Costi: impianto a goccia 4-10 €/m²; irrigazione interrata completa 8-20 €/m²; il risparmio idrico: documentato 30-50%.",
 "Parco pubblico con irrigazione zonata e sensore pioggia: il consumo idrico annuo è sceso del 45% rispetto all'aspersione notturna precedente, con migliore stato del tappeto erboso.",
 "Nessuna norma cogente; prassi e specifiche dei produttori; normativa sul risparmio idrico locale.",
 "La regola: irrigare poco e spesso? No: irrigare profondo e raramente (radici profonde = piante resistenti), con sensore pioggia obbligatorio."),
s("Essenze", "La scelta delle essenze: alberi, arbusti, prati per il clima italiano",
 "La scelta delle piante è la decisione che vale decenni: gli alberi da fusto alto per le strade (platano, tiglio, frassino, cipresso? No: cipresso non da fusto alto urbano), gli arbusti per le aiuole (lauroceraso, viburno, lavanda per il mediterraneo), i prati (suddivisi in ombreggiati, soleggiati, rustici); i criteri: resistenza a siccità e caldo crescenti, resistenza a parassiti e malattie, manutenzione richiesta, allergenicità, messa a dimora in periodi correttivi.",
 "Tabella rapida: mediterranee (ulivo, alloro, corbezzolo, mirto, rosmarino: minima acqua, massima resa), caducifoglie da ombra (platano, tiglio, acero: grandi ombreggianti ma allergie e rifiuti), sempreverdi (cipresso, leccio, pino: barriera ma attenzione a incendi vicino alle case), prato rustico con sementi miscuglio (resiste a siccità e calpestio); il criterio guida: l'acqua che servirà tra 20 anni, non quella di oggi.",
 "Parchi, giardini, aiuole stradali, siepi, aree private.",
 "Le essenze giuste riducono manutenzione e acqua del 50-70% rispetto alle scelte 'da rivista' non adattate.",
 "La moda delle piante esotiche crea passivi: palme e banani in climi non loro sopravvivono con cure costose o muoiono.",
 "Costi: pianta da siepe 5-20 €; arbusto 10-40 €; albero da fusto 150-800 €; prato a semina 3-8 €/m².",
 "Comune che ha sostituito il lungo viale di platani malati con frassini e tigli più resistenti: le spese di manutenzione e sostituzione si sono dimezzate in 6 anni e l'ombreggiamento è tornato pieno.",
 "Nessuna norma cogente; conoscenze botaniche e prassi locali (vivai).",
 "La domanda futura: 'questa pianta reggerà i 40 °C di luglio tra 10 anni con l'acqua che avremo?' — se la risposta è incerta, scegliere altro."),
s("Verde vincolato", "Il verde in regime di vincolo: paesaggio e sostituzioni",
 "Il verde in aree vincolate (paesaggistico, parco, monumentale) ha regole speciali: le piante 'monumentali' sono tutelate (schedatura comunale), gli interventi su alberature vincolate richiedono autorizzazioni, le sostituzioni devono essere 'a parità di chioma' (sostituire la chioma persa con nuova piantagione equivalente).",
 "Regole pratiche: verificare la presenza di alberi monumentali/schedati prima di ogni progetto, le potature devono seguire le regole arboricolturali (tagli di ritorno, mai a pollone? le potature severe sono vietate in molti regolamenti), le radici degli alberi stradali sono tutelate (i lavori vicino al fusto richiedono protezioni e interventi manuali), la sostituzione per morte: una o più piante equivalenti concordate col Comune.",
 "Cantieri in zone vincolate, lavori stradali con alberature, riqualificazioni di parchi storici.",
 "Il rispetto delle regole del verde evita sanzioni e blocchi: in vincolo, una potatura abusiva può costare decine di migliaia di euro.",
 "Le regole variano per Comune: la verifica preventiva con il settore verde evita il 90% dei problemi.",
 "Costo autorizzazioni: tempi amministrativi (il costo vero); la sostituzione a parità: da poche centinaia a migliaia di euro.",
 "Lavori stradali con protezione delle radici degli alberi (stesura manuale, niente escavatore entro il raggio di chioma): tutti gli alberi sono sopravvissuti; nel cantiere parallelo senza protezioni, 6 alberi su 10 sono morti in 2 anni con richiesta di risarcimento.",
 "D.Lgs 42/2004 (vincolo paesaggistico); regolamenti comunali del verde; leggi regionali su alberature.",
 "Domanda preliminare: 'ci sono alberi tutelati in questo cantiere?' — la risposta cambia metodi, prezzi e tempi."),
s("Manutenzione verde", "La manutenzione del verde: il contratto che fa vivere il giardino",
 "Il verde senza manutenzione muore o diventa pericolo: potature, concimazioni, irrigazione, trattamenti fitosanitari (con regole sui prodotti), sfalci, sostituzioni; la manutenzione si programma annualmente (calendario) e si affida con capitolato chiaro (frequenze, standard, penali).",
 "Programma tipo: sfalci prato (ogni 2-4 settimane in stagione), potature arbusti (2 volte/anno), potature alberi (cicli pluriennali secondo specie), concimazione primavera/autunno, controllo irrigazione stagionale, monitoraggio fitosanitario (con principi attivi consentiti e D.Lgs 150/2012 per i professionisti); il contratto: a corpo (mensilità fissa) o a misura (interventi conteggiati), con verbali di sopralluogo condivisi.",
 "Condòmini, aziende, parchi pubblici, proprietari privati.",
 "La manutenzione programmata costa meno degli interventi d'emergenza: il ramo caduto costa 10 volte la potatura programmata.",
 "Il contratto vago ('manutenzione ordinaria del verde') genera liti infinite su cosa sia 'ordinaria'.",
 "Costi: manutenzione giardino privato: 3-10 €/m²/anno; parchi pubblici: budget comunali dedicati; la potatura di un albero da fusto: 150-600 €.",
 "Condominio passato da manutenzione 'a chiamata' a contratto annuale con capitolato e calendario: il giardino è rinato in una stagione e le spese impreviste (alberi caduti, infestanti) sono azzerate.",
 "Capitolati tipo e regolamenti locali; normativa fitosanitaria (D.Lgs 150/2012); prassi di settore.",
 "Il giardino è un contratto continuo, non un evento: chi lo tratta come tale ha giardini belli; chi no, ha spese e lamentele."),
]

README = """# VERDE_ARREDO_URBANO_PACK — Verde urbano, coperture verdi, arredo urbano, irrigazione

**Facoltà:** FACOLTA_ARCHITETTURA_DESIGN · **Livello:** L2 · **Schede:** {n}

## Contenuto
Il mondo del verde costruito: verde urbano come infrastruttura ecologica,
progettazione del giardino, coperture verdi (tetti giardino estensivi e
intensivi), pareti verdi e giardini verticali, arredo urbano (panchine, giochi
certificati, fontane), pavimentazioni permeabili, irrigazione programmata,
scelta delle essenze per il clima italiano che cambia, verde in regime di
vincolo e manutenzione programmata.

## Formato
- `schede/schede.jsonl` — una scheda per riga, 11 campi standard.
- `COURSE.yaml` — metadati del corso.

## Uso per l'addestramento
Adatto a: progettazione di esterni, consulenza su verde e irrigazione, dialogo
con vivai e manutentori, sostenibilità idrica. Le essenze consigliate seguono
la logica mediterranea e il risparmio idrico: verificare sempre il contesto
locale e le allergenicità per le scelte stradali.
""".format(n=len(DATA))

COURSE = """corso: "Verde urbano e arredo urbano"
facolta: "FACOLTA_ARCHITETTURA_DESIGN"
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
