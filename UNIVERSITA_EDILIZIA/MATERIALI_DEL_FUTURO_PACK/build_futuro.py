# -*- coding: utf-8 -*-
"""MATERIALI_DEL_FUTURO_PACK: calcestruzzi avanzati, bio-based, stampa 3D, materiali intelligenti."""
import json, os

ROOT = os.path.dirname(os.path.abspath(__file__))

def s(cat, nome, desc, tec, app, van, lim, cos, casi, norm, note):
    return dict(categoria=cat, nome=nome, descrizione=desc, tecnologia=tec,
                applicazioni=app, vantaggi=van, limiti=lim, costi_e_economia=cos,
                casi_real_world=casi, normative=norm, note_cantiere=note)

DATA = [
s("Calcestruzzi avanzati", "I calcestruzzi del futuro: UHPC, autoriparanti, translucidi",
 "I calcestruzzi evoluti superano i limiti del materiale classico: UHPC (Ultra High Performance Concrete: resistenze 120-200 MPa, spessori ridotti del 50%, durabilità eccezionale), autoriparanti (con batteri o capsule curanti che 'riparano' le microfessure), translucidi (con fibre ottiche che lasciano passare la luce), leggeri strutturali (densità ridotta con resistenze alte).",
 "UHPC: granulometria ottimizzata con fibre d'acciaio, autocompattante, getto controllato in laboratorio più che in cantiere; autoriparanti: la microcapsule? No: le capsule con agente curante si rompono con la fessura e la sigillano; translucidi: fibre ottiche disposte in matrice per trasmissione laterale; tutti richiedono dosaggi precisi e controllo qualità di livello industriale.",
 "Opere sottili (ponti pedonali, coperture leggere), restauri con spessori minimi, elementi di pregio, contesti aggressivi (industria, mare).",
 "Il UHPC permette strutture impossibili con il c.a. tradizionale: sezioni sottili, luci maggiori, vita utile enormemente allungata.",
 "Il costo è 5-15 volte il c.a. ordinario: si usa dove il peso e la durata valgono più del prezzo al metro cubo.",
 "Costi: UHPC 1.500-4.000 €/m³ in opera (ordini di grandezza); il c.a. ordinario posato: 100-200 €/m³.",
 "Passerella pedonale in UHPC: sezione di appena 12 cm per una luce di 20 m, posata in due giorni; dopo 8 anni, zero manutenzione e zero degrado visibile.",
 "Norme sui calcestruzzi (EN 206 e specifiche produttori); per UHPC: linee guida e documenti d'applicazione ( SETRA/AFGC di riferimento internazionale).",
 "La regola: il materiale avanzato si giustifica nel costo del ciclo di vita, non nel prezzo d'acquisto."),
s("Bio-based", "I materiali bio-based: canapa, bambù, fibre naturali",
 "I materiali da fonti biologiche crescono rapidi e sequestrano CO2: canapa edile (calce-canapa, blocchi, isolanti: ottimo isolante igrometrico), bambù strutturale (tuboli con resistenza specifica paragonabile all'acciaio), fibre naturali in compositi (lino, canapa, juta per pannelli), sughero (già re, isolante e sostenibile), terra cruda (risorsa locale, regolatore igrometrico).",
 "Caratteristiche: la canapa con la calce forma un composito 'vivo' che continua a carbonatare (assorbe CO2 nel tempo); il bambù richiede trattamenti anti-insetto e attenzione ai nodi come zone deboli; i pannelli in fibre naturali sostituiscono il vetroresina in molti usi non strutturali; la terra cruda: mattoni di terra compressa (adobe) o intonaci, meglio con leganti naturali (calce); tutti: attenzione alla normativa sul fuoco (trattamenti ignifughi necessari).",
 "Isolamenti naturali, interni salubri, architetture a bassissimo impatto, edilizia rurale e ricettiva.",
 "L'abitazione in bio-based ha interni di qualità aria superiore (meno emissioni) e comfort igrometrico naturale: il 'muro che respira' non è marketing, è fisica dei materiali.",
 "La variabilità del materiale naturale richiede manifattura esperta: il bambù mal selezionato fessura e infesta; la canapa mal dosata con la calce perde resistenza.",
 "Costi: isolante canapa 20-40 €/m² (comparabile al fibra di legno); bambù strutturale: su preventivo; intonaco terra-calce 20-45 €/m².",
 "Casa in paglia e legno con intonaci terra-calce: consumi riscaldamento ridotti del 70% rispetto al precedente edificio, comfort estivo eccellente senza climatizzazione, interni con qualità dell'aria percepita nettamente superiore dagli abitanti.",
 "Normativa sui materiali da costruzione (reazione al fuoco, emissioni); specifiche dei consorzi di settore (canapa, paglia).",
 "Il bio-based richiede artigiani formati: il materiale è semplice, la manifattura no."),
s("Stampa 3D", "La stampa 3D in edilizia: cosa può e cosa non può",
 "La stampa 3D edile deposita calcestruzzo a getto continuo secondo un percorso digitale: pareti portanti con geometrie libere, costruzione rapida, meno manodopera; oggi stampa pareti (il solaio e i nodi restano convenzionali), domani chissà.",
 "Tecnologie: stampa estrusione (ugello che deposita malta, bracci robotici o gru), stampa a letto di sabbia (leganti selettivi per elementi), i materiali: malte speciali a presa regolata, fibre per la coesione; i limiti attuali: l'altezza libera (il solaio si posa convenzionalmente), le finiture richiedono ulteriori passaggi, la normativa (i processi di collaudo sono in aggiornamento), i requisiti sismici da dimostrare caso per caso.",
 "Case unifamiliari, edilizia di emergenza, elementi decorativi complessi, murature di contenimento curve.",
 "Velocità di pareti impressionante (metri lineari al giorno) e libertà geometrica: curve e spessori variabili a costo zero aggiuntivo.",
 "La stampa non stampa 'case': stampa pareti; il 60% del lavoro (impianti, solai, finiture) resta tradizionale; il costo complessivo oggi è pari o superiore al metodo tradizionale.",
 "Costi: prototipi e case dimostrative: quotazioni altissime; il mercato reale è ancora in fase sperimentale (TRL medio-basso).",
 "Casa stampata dimostrativa: le pareti esterne curve con spessori variabili sono state completate in 10 giorni; il resto dei lavori (solaio, tetto, impianti, finiture) ha richiesto 4 mesi convenzionali.",
 "Normativa in evoluzione (processi di collaudo per stampa 3D in aggiornamento nei tavoli tecnici); NTC come riferimento prestazionale.",
 "Il criterio professionale: valutare la stampa 3D come PROCESSO (con i suoi costi nascosti), non come gadget: oggi vince sulle geometrie speciali, non sul prezzo."),
s("Materiali intelligenti", "I rivestimenti intelligenti: aerogel, PCM, termocromici",
 "I materiali 'intelligenti' rispondono all'ambiente: l'aerogel (gel siliceo disidratato: il miglior isolante esistente, λ 0,014-0,020 W/mK, sottilissimo, trasparente), i PCM (phase change materials: paraffine o sali che assorbono calore fondendosi e lo restituiscono solidificando, stabilizzando la temperatura), i rivestimenti termocromici (cambiano colore/tinta con la temperatura per gestire l'assorbimento solare).",
 "Aerogel: pannelli sottilissimi (10 mm = 50-70 mm di lana), ideali per retrofit dove lo spazio non c'è; PCM: microincapsulati in gesso o malte, il cambio di fase avviene a temperature di comfort (20-26 °C); termocromici: pellicole o vernici per vetrate e facciate; tutti: costi elevati e applicazioni specialistiche, il beneficio si valuta nel bilancio energetico dell'edificio.",
 "Retrofit di edilizi storici (l'aerogel rispetta gli spessori), climatizzazione passiva (PCM nelle pareti), facciate adattive.",
 "L'aerogel risolve l'irrisolvibile: isolare dove non c'è spazio (cornici, volte, sottili spessori) senza alterare le geometrie.",
 "Il costo premium è reale: l'aerogel costa 10-20 volte la lana; i PCM richiedono massicci volumi per un beneficio misurabile.",
 "Costi: aerogel 40-80 €/m²; PCM in malta/gesso: premium 30-60% sul materiale base; i risparmi energetici: da simulazione energetica, non da promesse.",
 "Restauro di un edificio storico con cappotto interno in aerogel di 15 mm: il dispersions? No: la dispersione è scesa come con 8 cm di lana, le cornici storiche sono intatte e l'U-value ha raggiunto il requisito di legge.",
 "Normativa energetica (D.Lgs 192/2005 s.m.i.); marcatura CE dei materiali da costruzione.",
 "La domanda: 'quanto vale qui un centimetro di spessore?' — dove vale molto, l'aerogel vince."),
s("Riciclati avanzati", "I materiali riciclati avanzati: plastica, CO2, rifiuti in costruzione",
 "Il riciclato avanzato trasforma rifiuti in risorsa strutturale: plastiche riciclate in elementi arredo e tubazioni, aggregati da demolizione selezionata (con percentuali crescenti nel calcestruzzo), CO2 mineralizzata nel calcestruzzo (Carbfix-like: la CO2 diventa carbonato stabile dentro il materiale), gomma da pneumatici in asfalti e sottofondi sportivi.",
 "Processi: la plastica riciclata diventa (con additivi) profili, pavimentazioni, arredi urbani, con durabilità eccellente all'esterno; l'aggregato riciclato richiede selezione accurata e classificazione EN; la CO2 in calcestruzzo: cura carbonatica accelerata (il calcestruzzo assorbe CO2 durante l'indurimento, fino a percentuali significative del legante); la gomma granulata in asfalti riduce rumore e migliora elasticità.",
 "Arredo urbano sostenibile, pavimentazioni esterne, asfalti modificati, elementi di alleggerimento, commesse green con requisiti di riciclato.",
 "Il riciclato avanzato chiude il cerchio: meno discarica, meno estrazione, e in molti casi prestazioni migliori (la gomma nell'asfalto silenzia).",
 "Il riciclato mal tracciato è un rischio: plastica senza provenienza certificata, aggregato con gesso o amianto contamina il cantiere e la reputazione.",
 "Costi: arredo in plastica riciclata pari a quello vergine (oggi); l'aggregato riciclato 10-30% in meno del vergine; i premi ESG possono valere più del risparmio.",
 "Pista ciclabile in asfalto con gomma riciclata: il rumore al passaggio delle bici è ridotto percettibilmente e l'elasticità ha migliorato il comfort; il Comune ha usato il dato per la comunicazione ambientale del bando Europa.",
 "Normative sui materiali riciclati (CTU e linee guida nazionali; marcatura CE dove applicabile); norme ambientali sui rifiuti (D.Lgs 152/2006).",
 "La regola: il riciclato serio ha certificazione di provenienza e di prestazione: 'è riciclato' non basta."),
s("Vetri futuro", "I vetri del futuro: elettrocromici, fotovoltaici, autopulenti",
 "Il vetro intelligente cambia le facciate: elettrocromico (la trasmissione luminosa cambia con una tensione: si scurisce elettronicamente come gli occhiali fotocromatici ma controllato), fotovoltaico trasparente o semitrasparente (genera energia diventando 'pelle' dell'edificio), autopulente (rivestimento fotocatalitico che scompone lo sporco con la luce), basso emissivo selettivo (gira calore e luce in modo differenziato).",
 "Elettrocromici: stratificati con ossidi metallici che cambiano stato ottico; controllo manuale o automatico (sensori luce); i fotovoltaici trasparenti: celle a film sottile o organico con trasparenze parziali (generano meno ma sono finestre); autopulenti: biossido di titanio fotocatalitico; il dimensionamento di facciata passa da 'quanto isolano' a 'quanta energia gestiscono'.",
 "Facciate di uffici e residenze di pregio, involucri in climi estremi, edilizia ad alta efficienza energetica (facciate dinamiche).",
 "La facciata elettrocromica elimina le schermature esterne e ottimizza luce e calore in automatico: comfort e risparmio insieme.",
 "Il costo premium è elevato (2-5 volte il vetro selettivo standard) e la manutenzione elettronica si aggiunge a quella del vetro.",
 "Costi: vetro elettrocromico 250-600 €/m²; fotovoltaico trasparente: su progetto; autopulente: premium 15-30%.",
 "Facciata uffici elettrocromica: il disagio abbagliamento scomparso e il fabbisogno di raffreddamento estivo ridotto del 25% rispetto alla simulazione con schermature interne.",
 "Normativa facciate (reazione al fuoco, sicurezza); specifiche produttori; marcatura CE.",
 "La facciata del futuro non isola: gestisce energia, luce e comfort in tempo reale."),
s("PCM", "I materiali a cambio di fase (PCM): il calore nel cassetto",
 "I PCM (Phase Change Materials) immagazzinano calore come la ghicciolo? No: come il ghiaccio nella borsa frigo: assorbono calore fondendosi e lo restituiscono solidificando; integrati in intonaci, mattoni o pannelli, 'raddrizzano' le escursioni termiche giornaliere: di notte rilasciano, di giorno assorbono.",
 "Materiali: paraffine, sali idrati, acidi grassi; il punto di fusione si sceglie per il comfort (21-26 °C per l'abitazione); le forme: microcapsule in gesso/malte, lastre macroincapsulate, pannelli; il dimensionamento: i PCM equivalgono a una massa termica aggiuntiva (5-10 cm di calcestruzzo in più) in un materiale sottilissimo.",
 "Edilizi con inerzia termica insufficiente (case in legno, case ligth-weight), climi con escursioni giornaliere marcate, rifugi e locali senza climatizzazione notturna.",
 "I PCM migliorano il comfort estivo senza climatizzazione: le temperature picco si abbassano di 2-4 °C negli edifici ben progettati (dati di simulazione e monitoraggio).",
 "Il beneficio è zero se l'edificio è già massiccio o se le escursioni sono piccole: serve il calcolo, non l'entusiasmo.",
 "Costi: intonaco/malta con PCM: +30-60%; pannelli PCM: 50-120 €/m².",
 "Casa in legno in clima continentale con intonaco al PCM: le temperature estive interne non superano mai i 27 °C senza aria condizionata (monitoraggio estivo), contro i 31 °C della casa gemella senza PCM.",
 "Normativa energetica (la massa termica entra nei calcoli); specifiche produttori.",
 "La verità: i PCM sono 'massa termica liquida' portatile: pagano dove la massa vera non si può avere."),
s("Innovazione criteri", "Come valutare un materiale innovativo: TRL, LCA, norme",
 "Il professionista di fronte all'innovazione usa strumenti: il TRL (Technology Readiness Level: scala 1-9 dalla ricerca al prodotto commerciale), la LCA (Life Cycle Assessment: il bilancio ambientale dall'estrazione alla fine vita), le EPD (Environmental Product Declarations), la marcatura CE e le norme applicabili, il monitoraggio delle prime applicazioni reali.",
 "Metodo: 1) TRL: sotto il 6 è sperimentale (usare solo in ricerca o con garanzie forti); 2) LCA/EPD: quantifica impatti (CO2, acqua, energia) contro le alternative; 3) norme: esiste la EN/UNI di riferimento? il CE è marcato correttamente? 4) track record: quante applicazioni reali > 5 anni? come sono andate? 5) costo del ciclo di vita, non del solo acquisto.",
 "Selezione materiali per commesse innovative, R&D di prodotto, verifica di promesse commerciali.",
 "Il metodo protegge dal marketing: i 'materialetti miracolosi' muoiono di fronte a TRL basso e track record assente.",
 "La cautela eccessiva uccide l'innovazione utile: i materiali nuovi sono necessari (decarbonizzazione): valutarli seriamente, non liquidarli né ingoiarli.",
 "Costi: LCA completa 3.000-15.000 € per prodotto (a carico del produttore); la verifica documentale da parte del progettista: tempo di studio.",
 "Materiale isolante 'rivoluzionario' proposto dal rappresentante: TRL 4, nessuna EPD, track record zero: la verifica ha evitato un cappotto sperimentale su 40 appartamenti; tre anni dopo il prodotto non esiste più.",
 "UNI EN ISO 14040/44 (LCA); regolamento UE 305/2011 (marcatura CE); linee guida TRL (NASA-origin, uso settoriale).",
 "La frase da insegnare: 'Mi mostri EPD, marcatura CE, casi studio di 5 anni e il costo del ciclo di vita' — quattro richieste che smascherano il 90% delle innovazioni premature."),
s("Biocementi", "I biocementi e i materiali da micelio: la costruzione naturale",
 "La frontiera bio: i biocementi (batteri che induriscono la sabbia precipitando carbonato di calcio: il 'cemento' lo fanno i microbi), i mattoni da micelio (il micelio dei funghi cresce su scarti agricoli e li lega in blocchi leggeri, isolanti, compostabili), i bioplastiche strutturali in evoluzione.",
 "Processi: biocementazione: batteri (Sporosarcina pasteurii) inducono la precipitazione del carbonato sulla sabbia: un conglomerato naturale senza cottura; micelio: coltivato in stampi con scarti (paglia, bucce), essiccato blocca la crescita: blocchi con buona resistenza a compressione e ottimo isolamento; entrambi: assorbimento CO2 nella crescita, fine vita compostabile o inerte; i limiti: scala industriale ancora piccola, standardizzazione assente, durabilità all'esterno da dimostrare.",
 "Architetture temporanee, design di interni, pannelli e isolanti naturali, ricerca e prototipi.",
 "La prospettiva è radicale: materiali che crescono, assorbono carbonio e tornano alla terra: l'edilizia come ciclo biologico.",
 "Oggi sono nicchia e laboratorio: niente di strutturale all'esterno senza anni di test.",
 "Costi: prototipi e piccoli lotti: elevati; su scala industriale futura: potenzialmente molto competitivi (la materia prima è scarto).",
 "Padiglione temporaneo in mattoni di micelio: costruito in 2 settimane di coltivazione, smontato e compostato dopo l'evento: zero rifiuto, zero cemento, zero trasporto di peso.",
 "Nessuna norma strutturale specifica (TRL basso); ricerca accademica in corso (MIT, università europee).",
 "Da insegnare: il bio è una DIREZIONE, non ancora un catalogo: chi promette bio-strutturale oggi vende ricerca, non prodotto."),
]

README = """# MATERIALI_DEL_FUTURO_PACK — Materiali innovativi e costruzione del futuro

**Facoltà:** FACOLTA_TECNOLOGIA_E_COSTRUZIONE · **Livello:** L3 · **Schede:** {n}

## Contenuto
La frontiera dei materiali: calcestruzzi UHPC, autoriparanti e translucidi,
materiali bio-based (canapa, bambù, terra cruda, paglia), stampa 3D in edilizia,
materiali intelligenti (aerogel, PCM, termocromici), riciclati avanzati (plastica,
CO2 mineralizzata, gomma), vetri del futuro (elettrocromici, fotovoltaici,
autopulenti), PCM per la massa termica e il metodo di valutazione dell'innovazione
(TRL, LCA, EPD, track record), biocementi e micelio.

## Formato
- `schede/schede.jsonl` — una scheda per riga, 11 campi standard.
- `COURSE.yaml` — metadati del corso.

## Uso per l'addestramento
Adatto a: consulenza su innovazione, valutazione di promesse commerciali,
progettazione con materiali avanzati, cultura R&D. Il criterio cardine: il
materiale del futuro si valuta sul ciclo di vita e sul track record, mai sul
lancio marketing.
""".format(n=len(DATA))

COURSE = """corso: "Materiali del futuro e costruzione innovativa"
facolta: "FACOLTA_TECNOLOGIA_E_COSTRUZIONE"
livello: "L3"
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
