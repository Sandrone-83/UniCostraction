# -*- coding: utf-8 -*-
"""EDILIZIA_INDUSTRIALE_LOGISTICA_PACK: capannoni, pavimenti industriali, scaffalature, baie."""
import json, os

ROOT = os.path.dirname(os.path.abspath(__file__))

def s(cat, nome, desc, tec, app, van, lim, cos, casi, norm, note):
    return dict(categoria=cat, nome=nome, descrizione=desc, tecnologia=tec,
                applicazioni=app, vantaggi=van, limiti=lim, costi_e_economia=cos,
                casi_real_world=casi, normative=norm, note_cantiere=note)

DATA = [
s("Capannoni", "I capannoni industriali: la scatola che lavora",
 "Il capannone industriale è architettura minima massimizzata: una scatola con struttura (acciaio o precast), involucro (pannelli sandwich), grandi porte e luce naturale; il progetto giusto parte dalla logistica interna (i flussi decidono luci, altezze e baie) e non dal disegno esterno.",
 "Parametri: altezza di libera (minimo 6-8 m per scaffalature, fino a 12+ m per magazzini automatizzati), luci in struttura metallica (20-30 m tra portali tipici), pannelli sandwich coibentati (50-120 mm), lucernari per luce naturale (il 10-15% della copertura), portoni sezionali o rapidi, pavimento industriale come seconda struttura; la destinazione modifica tutto: artigianato leggero vs logistica pesante vs produzione con carroponti.",
 "Magazzini, officine, produzione, logistica, agricoltura industriale.",
 "Il capannone giusto è uno strumento di produzione: chi progetta 'una tettoia' per un magazzino che lavora a turni paga poi il triplo per adattarla.",
 "L'economia spinge al minimo: il capannone 'troppo basso' o 'troppo stretto' blocca la crescita dell'azienda che lo usa.",
 "Costi: capannone base 250-450 €/m² chiavi in mano; con uffici e finiture industriali di pregio: 500-900 €/m².",
 "Capannone logistico progettato sui flussi (ricevimento, stoccaggio, spedizione in linea): la produttività del magazzino è salita del 30% dopo il trasferimento; il capannone precedente 'a caso' richiedeva il doppio dei percorsi interni.",
 "Normativa capannoni (logistica, antincendio DM 2015, energetica); NTC per la struttura; normativa agro-industriale se applicabile.",
 "La prima domanda: 'cosa succede DENTRO questo capannone?' — la risposta decide altezze, luci, pavimenti e porte."),
s("Pavimenti industriali", "I pavimenti industriali: il pavimento che porta carrelli",
 "Il pavimento industriale è una struttura: sopporta carrelli elevatori, scaffalature alte, carichi concentrati e il traffico continuo; si getta in calcestruzzo fibrorinforzato o con rete elettrosaldata su massetto di sabbia, con giunti di taglio che gestiscono la ritirata.",
 "Tecnologia: calcestruzzo di classe minima C30/37 (meglio Rc maggiorata per i carrelli pesanti), spessore 12-18 cm tipico, fibre (acciaio o polipropilene) o rete doppia per la fessurazione controllata, il massetto di sabbia 5-10 cm sotto, la levigatura meccanica o il quarzo insufflato per la resistenza all'abrasione, le guaine per pavimenti radianti? No: i giunti di taglio (max 6×6 m reticolo tipico) riempiti con resine per i carrelli; la planarità: la tolleranza per le scaffalature alte (max 3 mm su 3 m) è il requisito che i non addetti dimenticano.",
 "Magazzini, officine, centri logistici, lavanderie industriali, celle frigorifere.",
 "Il pavimento giusto non si vede ma si sente: niente polveri, niente giunti spaccati, i carrelli che scorrono senza sbattere.",
 "Il difetto classico: il pavimento 'fissurato' per il ritiro non controllato e i bordi dei giunti che si sfaldano sotto le ruote: le macchine smontano e si rifanno metà pavimento a 5 anni.",
 "Costi: pavimento industriale levigato: 35-70 €/m²; il rifacimento di una zona guasta costa il triplo del preventivo corretto.",
 "Magazzino con pavimento a giunti 5×5 m con resine di riempimento: dopo 8 anni di carrelli a turni continui, i giunti integri e il pavimento planarità perfetta; il magazzino vicino con giunti 'aperti': la manutenzione ha sostituito 1.200 m² di bordi in 6 anni.",
 "Norme pavimenti industriali (specifiche e linee guida; UNI 11714 per i pavimenti in calcestruzzo levigato); prescrizioni dei carrellisti (planarità).",
 "La regola: il pavimento industriale si progetta con chi ci lavora sopra (carrelli, scaffalature, macchinari) — non è un massetto, è una strada interna."),
s("Scaffalature", "Le scaffalature industriali: l'architettura interna del magazzino",
 "Le scaffalature sono strutture metalliche portanti che trasformano il volume del capannone in stoccaggio verticale: scaffali portapallet, scaffalature a gravità, drive-in, miniload automatizzati; ogni sistema ha il suo ciclo di carico/scarico e la sua resa di volume.",
 "Tipi: selettivi (accesso diretto a ogni pallet, la flessibilità massima), drive-in/drive-through (il carrello entra nella struttura, densità massima, FIFO o LIFO), a gravità (rulli inclinati), cantilever (per i lunghi), scaffalature leggere per picking; la normativa: calcolate con Eurocodice, verificate contro gli urti (i carrelli li colpiscono: le protezioni di base sono obbligatorie), ancorate al pavimento con tasselli di progetto; l'altezza cresce: 10-12 m manuali, fino a 30 m+ i magazzini automatici.",
 "Logistica, produzione, e-commerce, agricoltura, ferramenta industriale.",
 "La scaffalatura giusta raddoppia la capacità di stoccaggio a parità di superficie: il volume verticale è il terreno gratis.",
 "L'urto del carrello è la prima causa di crollo di scaffalature: senza protezioni di base, il rischio è quotidiano.",
 "Costi: scaffalatura selettiva 40-90 €/posizione pallet (ordine di grandezza); il magazzino automatico: investimenti su progetto.",
 "Magazzino con scaffalature a gravità per il picking veloce: i tempi di preparazione ordini sono calati del 25%; la protezione anticrollo (bordi e basi rinforzate) ha eliminato i danni da urto che costavano 8.000 €/anno.",
 "Normativa scaffalature (EN 15512, EN 15620, verifiche periodiche); Eurocodice 3; normativa sicurezza sul lavoro (le scaffalature sono attrezzature di lavoro, verifica annuale).",
 "Regole: le scaffalature si progettano insieme al capannone (altezze, carichi, pavimenti) e si proteggono SEMPRE alla base."),
s("Baie di carico", "Le baie di carico: dove il magazzino tocca la strada",
 "La baia di carico è il collo di bottiglia logistico: la zona dove i camion caricano e scaricano; gli elementi: portoni sezionali o rapidi, pensiline di protezione, dock leveler (rampe regolabili che pareggiano i dislivelli camion-banchina), bordi di banchina con cuscini di tenuta.",
 "Componenti: i portoni sezionali (apertura verticale, isolati, con oblò), i portoni rapidi (PVC ad alta velocità, per ambienti interni), i dock leveler (manual? idraulici o meccanici, capacità 6-10 t tipiche), le seals (cuscini o tende che sigillano il giunto camion-banchina per il clima), le segnalazioni (semafori di baia, luci) e la sicurezza (le barriere anti-caduta camion: i camion non devono muoversi durante la movimentazione).",
 "Ogni magazzino e centro di distribuzione.",
 "La baia efficiente elimina le attese dei camion (il costo nascosto più grande della logistica): i camion scaricano in 30 minuti invece di 2 ore.",
 "La baia mal attrezzata (senza leveler, senza sigillo) perde energia (freddo/caldo), espone alla pioggia e ferma i cicli di lavoro.",
 "Costi: dock leveler 3.000-8.000 €, portone sezionale industriale 3.000-7.000 €, la baia completa: 10.000-25.000 €.",
 "Centro logistico con baie dotate di leveler e sigilli: i tempi di sosta camion sono calati del 40% e i consumi di climatizzazione del molo del 25% (meno infiltrazioni d'aria).",
 "Normativa macchine (dock leveler CE); specifiche di settore; normativa antincendio per i moli.",
 "La domanda da logistica: 'quanti camion al giorno e quanto tempo stanno fermi?' — la risposta dimensiona le baie e le attrezzature."),
s("Portoni", "I portoni industriali: sezionali, rapidi, scorrevoli",
 "I portoni industriali chiudono i grandi varchi: sezionali (lastre che scorrono verso l'alto lungo guide, isolati, i più usati), rapidi (PVC arrotolabili ad alta velocità, per flussi interni continui), scorrevoli laterali (per luci enormi), a libro (poco usati, solo dove serve); la scelta dipende da: frequenza di apertura, isolamento, velocità richiesta, luce disponibile.",
 "Caratteristiche: i sezionali con pannelli sandwich coibentati (40-60 mm), velocità 0,15-0,25 m/s; i rapidi fino a 1-2 m/s con riapertura automatica (fondamentali per celle frigo e catene del freddo); la sicurezza: fotocellule, barre sensibili, finecorsa, la regolazione antischiacciamento; la manutenzione: le molle e i cavi si rivisionano, le guarnizioni si sostituiscono.",
 "Capannoni, magazzini, moli, officine, autorimesse industriali.",
 "Il portone giusto accelera i flussi: un portone rapido in un flusso continuo vale mezzo operaio in più.",
 "Il portone 'bloccato aperto' (guasto) annulla l'isolamento dell'intero capannone.",
 "Costi: portone sezionale 3.000-7.000 €, rapido 4.000-10.000 €, manutenzione annua 200-500 €.",
 "Cella frigorifera con portoni rapidi: la variazione di temperatura in cella è stata contenuta (+2 °C max all'apertura contro i +7 del portone precedente), con risparmio energetico misurabile e qualità del prodotto preservata.",
 "Normativa macchine (marcatura CE); specifiche produttori; normativa antincendio (i portoni tagliafuoco industriali hanno classi RE).",
 "La regola: il portone si sceglie sul traffico (aperture/ora) e sul clima (isolamento), mai solo sul prezzo."),
s("Illuminazione industriale", "L'illuminazione industriale: la luce che produce",
 "La luce industriale è produttività e sicurezza: gli impianti moderni a LED ad alta baia ( High bay 8-12 m) con regolazione (sensori di presenza e luce diurna) consumano la metà dei vecchi apparecchi a sodio; i requisiti: i lux per mansione (magazzino 150-200 lux piano lavoro, officina 300-500, picking dettagliato 500+).",
 "Sistemi: apparecchi a sospensione alta con ottiche ad ampia distribuzione, luce 4000K (neutra, da lavoro), CRI >80 (i colori contano nei magazzini), il controllo: gruppi per corsie con sensori (la corsia si illumina al passaggio del carrello), l'illuminazione di emergenza (le vie di esodo industriali), la manutenzione programmata (il LED dura 50.000 ore ma le ottiche si puliscono).",
 "Capannoni, magazzini, officine, celle frigorifere (apparecchi per freddo).",
 "La luce giusta nel punto giusto riduce gli errori di picking e gli infortuni: è un investimento produttivo, non una voce di consumo.",
 "L'illuminazione 'a giorno solo' nei magazzini interni crea zone d'ombra tra le scaffalature: gli errori di prelievo crescono.",
 "Costi: impianto LED industriale 30-60 €/m²; il risparmio sui consumi: 50-70% rispetto ai corpi tradizionali.",
 "Magazzino con illuminazione a sensori di presenza per corsie: il consumo elettrico dell'illuminazione è calato del 55% e gli errori di picking del 20% (confronto anno su anno).",
 "UNI EN 12464-1 (lux); CEI 64-8; normativa emergenza.",
 "La verifica rapida: 'il prelevatore legge il codice prodotto senza strizzare gli occhi?' — se no, l'illuminazione è sbagliata."),
s("Antincendio industriale", "L'antincendio industriale: magazzini e rischi speciali",
 "L'antincendio industriale segue il D.M. 03/08/2015 con le specifiche per le attività di deposito e produzione: i rischi salgono con la merce stoccata (plastiche, imballaggi, aerosol), le altezze di stoccaggio, le attività a caldo; gli impianti: rivelazione, estinzione (idranti, sprinkler dove richiesti), la gestione con il VVF.",
 "Focus: i depositi con scaffalature alte (la merce alta brucia diversa: gli sprinkler vanno adattati), le celle frigorifere (rischio ammoniaca nei vecchi impianti: il freon moderno riduce il rischio), le aree a caldo (saldature, tagli: permesso di lavoro a caldo con sorveglianza), la gestione delle batterie (i depositi di litio: nuovo rischio con le batterie degli strumenti e dei muletti), le vie di esodo ampie per i flussi di personale.",
 "Magazzini, produzione, logistica, ricambi, depositi materie plastiche.",
 "L'antincendio industriale ben progettato protegge il patrimonio aziendale (la merce) e continuità produttiva: il magazzino bruciato chiude l'azienda per mesi.",
 "Le gomme e i grassi dei muletti nei percorsi possono infiammarsi? No: il rischio reale è l'elettrico e l'umano: la formazione resta la prima difesa.",
 "Costi: il presidio antincendio industriale: voci specifiche (progetto, impianti, formazione); le sanzioni e i danni: incalcolabili.",
 "Magazzino con formazione antincendio annuale del personale e permessi a caldo: un principio d'incendio durante lavori è stato spento dal personale in 2 minuti; il danno si è fermato a 300 € di materiale.",
 "D.M. 03/08/2015; normativa prevenzione incendi depositi; EN sprinkler (UNI 12845).",
 "La cultura antincendio industriale è formazione continua: il magazzino sicuro è quello dove TUTTI sanno cosa fare."),
s("Manutenzione industriale", "La manutenzione industriale degli immobili: il capannone che dura",
 "L'immobile industriale è una macchina da mantenere: la copertura (guaine, fissaggi, lucernari), i portoni (molle, guarnizioni), le facciate (pannelli, fissaggi al vento), i pavimenti (giunti, levigature), gli impianti; la manutenzione programmata annuale raddoppia la vita dell'immobile.",
 "Programma: la copertura (ispezione e pulizia prima dell'inverno, i fissaggi delle lamiere dopo i venti forti), i portoni (la revisione annuale con il tecnico: molle e cavi), i pavimenti (il riciclo dei giunti e le riparazioni immediate: il bordo sfaldato si ripara in settimane, non anni), le facciate (controllo dei fissaggi e delle guarnizioni: il vento trova il punto debole), gli scarichi e le gronde; il contratto con manutentori specializzati (coperture, portoni, pavimenti).",
 "Patrimoni industriali, logistica, produzione, immobili in affitto (il tenant e il landlord devono accordarsi).",
 "Il capannone mantenuto vale di più e ferma meglio il fitto: la manutenzione è reddito immobiliare.",
 "La logica 'si aggiusta quando si rompe' trasforma ogni guasto in fermo produzione.",
 "Costi: manutenzione programmata: 5-10 €/m²/anno; il guasto non programmato: 3-5 volte tanto più fermo macchina.",
 "Magazzino logistico con contratto annuale di manutenzione (copertura, portoni, pavimenti): dopo 15 anni l'immobile è 'come nuovo' e il fitto è al top di mercato; il capannone identico non mantenuto è in ristrutturazione a 12 anni.",
 "Nessuna norma cogente; prassi assicurative e contrattuali (i contratti di locazione industriale prevedono la manutenzione programmata).",
 "L'immobile industriale è un attrezzo di produzione: si mantiene come la macchina utensile."),
]

README = """# EDILIZIA_INDUSTRIALE_LOGISTICA_PACK — Capannoni, pavimenti industriali, scaffalature, baie

**Facoltà:** FACOLTA_INGEGNERIA · **Livello:** L2 · **Schede:** {n}

## Contenuto
L'edilizia produttiva e logistica: il capannone come strumento di lavoro
(flussi prima della forma), i pavimenti industriali (calcestruzzo fibrorinforzato,
planarità, giunti), le scaffalature (tipologie, normative, protezioni anticrollo),
le baie di carico (dock leveler, sigilli, sicurezza), i portoni industriali
(sezionali, rapidi), l'illuminazione industriale a LED regolata,
l'antincendio industriale (depositi, rischi speciali) e la manutenzione
programmata degli immobili produttivi.

## Formato
- `schede/schede.jsonl` — una scheda per riga, 11 campi standard.
- `COURSE.yaml` — metadati del corso.

## Uso per l'addestramento
Adatto a: consulenza per imprese produttive e logistiche, dialogo con
scaffalisti e installatori di baie, verifica di capannoni in acquisto/affitto,
gestione della manutenzione industriale. Il filo conduttore: in edilizia
industriale tutto si misura in produttività (tempi, errori, fermi macchina).
""".format(n=len(DATA))

COURSE = """corso: "Edilizia industriale e logistica"
facolta: "FACOLTA_INGEGNERIA"
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
