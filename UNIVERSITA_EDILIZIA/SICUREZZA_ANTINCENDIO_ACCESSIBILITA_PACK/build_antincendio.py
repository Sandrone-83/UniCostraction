# -*- coding: utf-8 -*-
"""SICUREZZA_ANTINCENDIO_ACCESSIBILITA_PACK: prevenzione incendi, vie di esodo, accessibilità."""
import json, os

ROOT = os.path.dirname(os.path.abspath(__file__))

def s(cat, nome, desc, tec, app, van, lim, cos, casi, norm, note):
    return dict(categoria=cat, nome=nome, descrizione=desc, tecnologia=tec,
                applicazioni=app, vantaggi=van, limiti=lim, costi_e_economia=cos,
                casi_real_world=casi, normative=norm, note_cantiere=note)

DATA = [
s("Quadro", "La prevenzione incendi: quadro normativo e logica",
 "La prevenzione incendi italiana si basa sul D.M. 03/08/2015 (norme tecniche di prevenzione incendi): le attività sono classificate per livello di rischio (basso, medio, alto) e conseguente regime (SCIA antincendio, autorizzazione, nulla osta) con progetto a cura di un professionista abilitato (ingegnere/architetto iscritto agli elenchi del Ministero).",
 "Iter: classificazione attività → redazione progetto di prevenzione incendi → presentazione al comando VVF → integrazioni → provvedimento; il progetto valuta: vie di esodo, compartimentazione, mezzi di estinzione, rivelazione, impianti speciali, gestione dell'emergenza; le sanzioni per omessa SCIA o difformità sono pesantissime e possono portare alla chiusura dell'attività.",
 "Ogni edificio con pubblico (scuole, uffici, negozi, ristoranti, alberghi), industrie, depositi.",
 "La logica è preventiva: costruire sicuro costa una frazione di quanto costa ristrutturare dopo un incendio o adeguare un locale sequestrato.",
 "La normativa è vasta e i regolamenti locali si sovrappongono: serve il professionista abilitato, non il fai-da-te.",
 "Costo progetto prevenzione incendi: 2.000-10.000 € secondo complessità; oneri per presidi: voci specifiche.",
 "Ristorante aperto senza SCIA antincendio: sequestro preventivo dopo un controllo, 30 giorni di chiusura, rientro con progetto e adeguamenti: costo totale ~45.000 €; il progetto preventivo sarebbe costato 4.000 €.",
 "D.M. 03/08/2015; regolamento di esecuzione del TULPS (D.P.R. 635/1982, parte); D.Lgs 139/2006 (Codice sicura).",
 "Prima domanda su un locale commerciale: 'che livello di rischio incendio ha questa attività e che titolo mi serve?' — decide costi e tempi dell'apertura."),
s("Vie esodo", "Le vie di esodo: requisiti geometrici e funzionali",
 "Le vie di esodo permettono l'evacuazione: larghezza minime in funzione dell'attività e del numero di occupanti (spesso 1,20 m per corridoi e rampe nei luoghi di pubblico, verifiche sempre sul DM), porte in senso di uscita, percorso massimo per raggiungere un'uscita di sicurezza o uno spazio di sicurezza, illuminazione di emergenza che garantisca i lux minimi di legge.",
 "Elementi: unità di piano (max occupanti per compartimento), percorso massimo di esodo, porte con larghezza utile ≥ misura minima dell'attività, uscite su scalinata con pendenza e alzata regolari, spazi di sicurezza (vestiboli presso scale), aree di sicurezza o uscite all'aperto; verifica in progetto con il calcolo degli occupanti (da metratura e destinazione d'uso).",
 "Progettazione di edifici con pubblico, ristrutturazioni di locali commerciali, verifica di agibilità.",
 "L'esodo ben progettato salva vite: negli incendi reali la maggior parte delle vittime cade per fumi e calca, non per le fiamme.",
 "I requisiti minimi spesso sono in conflitto con il desiderio di 'guadagnare metri': la via di esodo non è negoziabile in fase estetica.",
 "Costo aggiuntivo in progettazione: modesto; la conformità in ristrutturazione può richiedere spazi che 'pesano' sulla superficie utile.",
 "Locale commerciale con unico uscita sul retro attraverso magazzino: la verifica di esodo ha richiesto un secondo percorso indipendente; il costo di 8.000 € ha evitato un sequestro e, in caso di incendio, una tragedia.",
 "D.M. 03/08/2015 (capo esodo); UNI 11280 (via di esodo e illuminazione); normativa VVF.",
 "Regola per il LLM: nessun progetto di locale con pubblico si chiude senza il diagramma di esodo con occupanti, larghezze e percorrenze massime."),
s("Estinzione", "I mezzi di estinzione: estintori, idranti, naspi",
 "I mezzi di estinzione manuali sono la prima risposta: estintori a polvere (universali, sporcano), a CO2 (locali elettrici, non lasciano residui), idranti a parete con naspo (portata e getto minimo per attività), impianti a sprinkler dove richiesti o scelti; dimensionamento e posizionamento per attività da tabelle del DM.",
 "Regole: estintore ogni 200 m² e ogni 25 m di percorso tipici per attività, in posizione visibile e accessibile (max 1,5 m da terra), revisione annuale (etichetta), idranti con pressione minima verificata (prova di erogazione), i materiali edili incombustibili riducono il carico d'incendio e possono alleggerire i requisiti; formazione del personale all'uso (obbligo datore di lavoro).",
 "Ogni edificio produttivo e commerciale, cantieri grandi, magazzini.",
 "L'estintore usato nei primi minuti spegne il 90% degli incendi che altrimenti diventano grandi (statistiche VVF): posizionato giusto e il personale formato, è il presidio più efficace in assoluto.",
 "L'estintore 'solo a norma sulla carta' (revisione scaduta, sepolto dietro scaffali) è carta straccia nel momento del bisogno.",
 "Costo estintore: 40-120 € (revisione 15-30 €/anno); idrante completo: 300-800 €; formazione personale: 30-80 €/persona.",
 "Incendio in officina: un dipendente formato ha spento un principio d'incendio al banco con l'estintore a 4 m di distanza in 40 secondi; danno limitato a 2.000 € invece che all'intera attività.",
 "D.M. 03/08/2015 (tabelle presidi); UNI 45 e UNI EN 3 (estintori); D.Lgs 81/2008 (formazione).",
 "Checklist cantiere/azienda: estintori presenti, accessibili, revisionati; idranti provati; personale formato — tre spunte ogni 6 mesi."),
s("Compartimentazione", "La compartimentazione: limitare la propagazione",
 "La compartimentazione divide l'edificio in setti con resistenza al fuoco certificata (pareti, solai, porte tagliafuoco REI 60/90/120): obiettivo è contenere l'incendio nel compartimento d'origine, proteggere le vie di esodo e dare tempo ai soccorsi.",
 "Elementi: setti con elementi costruttivi certificati (curve di decadimento, non solo 'cartongesso ignifugo' generico), porte tagliafuoco con certificazione UNI e chiusura automatica o semiautomatica dove richiesta, giunzioni e attraversamenti sigillati (mastici intumescenti), intonaci e rivestimenti protettivi su strutture portanti (acciaio: intumescenti o vernici al silicato); il progetto elenca le resistenze REI per ogni elemento e il cartello di certificazione va conservato.",
 "Nuove costruzioni, ristrutturazioni di edifici esistenti, adeguamenti di locali con pubblico.",
 "La compartimentazione funziona: negli incendi edilizi i compartimenti corretti hanno salvato intere ali di edificio mentre il compartimento d'origine bruciava.",
 "Un solo attraversamento non sigillato (cavo elettrico, tubo) annulla un settore intero: la qualità sta nei dettagli di posa.",
 "Costo porte tagliafuoco: 400-1.500 €; mastici e sigillature intumescenti: poche decine di euro a punto; il costo in fase di costruzione è una frazione del rifacimento.",
 "Verifica post-incendio in ufficio: il settore REI 90 ha contenuto il fuoco in due stanze; la porta tagliafuoco del corridoio (chiusa automaticamente) ha salvato l'ala opposta: danno da 180.000 € invece che all'edificio intero.",
 "D.M. 03/08/2015; UNI EN 13501-2 (classi REI); normativa prodotti da costruzione CPR (UE 305/2011).",
 "La domanda da fare al LLM: 'quali sono i setti REI di questo edificio e dove passano i servizi attraverso di essi?' — ogni passaggio è un punto critico."),
s("Gestione emergenza", "Gestione dell'emergenza: PEI, addestramento, evacuazione",
 "La gestione dell'emergenza è la parte 'umana' della prevenzione: Piano di Emergenza Interno (PEI) con procedure, ruoli (addetti alle emergenze e prime evacuazione), planimetrie con percorsi e presidi, addestramento annuale degli occupanti, prove di evacuazione (tempo massimo tipico 5 minuti per edifici con pubblico secondo norma).",
 "Contenuti PEI: scenari di rischio, numeri di emergenza, procedure per incendio/emergenza, planimetrie esodo, nominativi addetti, manutenzione presidi; l'addestramento: corsi base e aggiornamento (legge 81/08), prove di evacuazione con cronometraggio e verbale; la gestione delle merci pericolose (scheda di sicurezza, stoccaggi).",
 "Uffici, scuole, industrie, centri commerciali, edifici con pubblico.",
 "L'edificio progettato bene con persone non preparate resta pericoloso: la prova di evacuazione annuale è il momento di verità.",
 "Il PEI 'nel cassetto' senza aggiornamento o formazione è inutile in emergenza: chi non sa cosa fare, non lo legge.",
 "Costo formazione addetti: 50-150 €/persona; prova di evacuazione: tempo interno; redazione PEI: 500-2.000 €.",
 "Prova di evacuazione in una scuola: evidenziato che un corridoio si intasava per una porta contraria; invertita l'apertura e ricalibrato il percorso: la prova successiva ha rispettato il tempo con margine del 40%.",
 "D.M. 03/08/2015 (capo gestione); D.Lgs 81/2008 (emergenze); UNI ISO 45001 (sistemi gestione sicurezza).",
 "Il PEI va trattato come il libretto dell'auto: revisionato ogni anno, consultato prima di ogni modifica dell'edificio."),
s("Accessibilità", "L'accessibilità: superamento delle barriere architettoniche",
 "L'accessibilità è diritto (D.Lgs 80/1992): gli edifici pubblici e privati aperti al pubblico devono essere fruibili da disabili; il riferimento tecnico è il DM 236/1989 (requisiti minimi) aggiornato dalle norme UNI e dalle leggi regionali: percorsi senza barriere, servizi igienici accessibili, ascensori o piattaforme, segnaletica e percorsi tattili.",
 "Requisiti chiave: pendenze dei percorsi esterni (max 5% ideali, rampe con riposi oltre certe lunghezze), larghezze minime di passaggio (90 cm), servizi igienici accessibili (spazio di manovra 150×150), contrassegni tattili e visivi, posti auto riservati; in ristrutturazione l'obbligo di abbattimento barriere vale per interventi rilevanti; i lavori di messa in sicurezza/accessibilità godono di detrazioni fiscali dedicate (es. 75% secondo normativa vigente, da verificare).",
 "Edifici pubblici, commerciali, uffici, abitazioni di disabili, ristrutturazioni con detrazioni.",
 "L'accessibilità bene fatta serve a tutti: genitori con passeggini, anziani, corrieri: il 'disegno per tutti' migliora l'edilizia per tutti.",
 "Gli adempimenti fatti 'al limite' per spuntare la casella creano percorsi umilianti e inefficaci: il superamento barriere è progetto, non pezza.",
 "Costo servizio igienico accessibile in più: 2.000-5.000 €; piattaforma elevatrice esterna: 8.000-20.000 €; detrazione 75% su interventi dedicati (verificare normativa corrente).",
 "Farmacia ristrutturata con ingresso a gradini: l'abbattimento barriere con rampa e portello automatico ha aperto il mercato a carrozzine e passeggini; il titolare dichiara clientela aumentata in modo percettibile già dopo pochi mesi.",
 "D.Lgs 80/1992; DM 236/1989; legge 13/1989; norme UNI (pendenze, segnaletica).",
 "Prima verifica di progetto: 'una persona in carrozzina può entrare, girare nei locali, usare i servizi e uscire in autonomia?' — il percorso completo, non il singolo dettaglio."),
s("Ascensori", "Ascensori e piattaforme elevatrici: obblighi e scelte",
 "L'abbattimento barriere verticali si fa con ascensori (obbligatori sopra certi piani/attività), piattaforme elevatrici (per dislivelli ridotti e carichi limitati) e montacarichi; gli impianti sono sottoposti a regole precise di installazione, collaudo, manutenzione (DPR 162/1999) e verifiche periodiche.",
 "Scelta: ascensore (persone, portata 320-1.000 kg, vano con misure minime accessibili), piattaforma elevatrice (dislivello fino a 2-3 piani tipici, portata 200-400 kg, soluzione per esistenti), montascale a poltroncina (abitazioni); adempimenti: progetto, installazione da ditta autorizzata, collaudo, verbale d'installazione, contratto manutenzione, libretto impianto, verifiche periodiche (annuali di manutenzione regolare); in condominio l'installazione per accessibilità è favorita dalla legge (maggioranze ridotte secondo riforma 2012).",
 "Edifici pubblici e privati con più piani, ristrutturazioni, condomini.",
 "L'impianto verticale trasforma la fruibilità dell'edificio: per anziani e disabili è la differenza tra casa e prigione.",
 "In edifici storici lo spesso vano ascensore è impossibile: le piattaforme esterne sono spesso la soluzione, con il vincolo paesaggistico da gestire.",
 "Costo ascensore nuovo: 18.000-45.000 €; piattaforma: 8.000-20.000 €; manutenzione: 1.000-2.500 €/anno; montascale: 3.000-8.000 €.",
 "Condominio con anziani al terzo piano: installata piattaforma esterna con detrazione e maggioranza condominiale ridotta: costo netto rientrato in parte dalle detrazioni e i residenti hanno recuperato autonomia.",
 "DPR 162/1999; L. 220/2012 (installazioni agevolate in condominio); DM 236/1989.",
 "Regole: mai sottodimensionare la cabina (sedia a rotelle + accompagnatore), mai saltare il contratto di manutenzione (è obbligo), mai installare senza i verbali di collaudo (responsabilità penale in caso di incidente)."),
s("Segnaletica", "La segnaletica di sicurezza e i controlli documentali",
 "La segnaletica di sicurezza (UNI EN ISO 7010) guida l'evacuazione e l'azione in emergenza: cartelli fotoluminescenti o illuminati (uscite, estintori, idranti, punto di ritrovo), planimetrie di evacuazione affisse, percorsi contrassegnati; la manutenzione documentale è la metà della conformità.",
 "Requisiti: cartelli normalizzati (pittogrammi, colori: verde = esodo/primo soccorso, rosso = presidi antincendio, giallo = avvertimento), posizione su percorso esodo ad altezza e intervalli regolari, fotoluminescenza o alimentazione di emergenza (UNI EN 1838), planimetrie di evacuazione aggiornate; documenti da conservare: progetti prevenzione incendi, SCIA/nulla osta, verbali collaudi presidi, revisioni estintori, verbali prove evacuazione, certificazioni porte tagliafuoco e materiali.",
 "Ogni edificio con pubblico e le relative scadenze di controllo.",
 "La segnaletica corretta orienta anche chi non conosce l'edificio (clienti, visitatori): in emergenza non si ragiona, si segue.",
 "La segnaletica 'creativa' non normalizzata confonde: le persone cercano i pittogrammi standard che conoscono.",
 "Costo cartelli: 10-50 € l'uno; planimetrie stampate e incorniciate: 30-80 €; il costo della mancata documentazione in un controllo: sanzioni e chiusure.",
 "Controllo VVF in un centro commerciale: segnaletica ottima ma revisione estintori scaduta di 4 mesi: diffida con termine di 15 giorni; il registro digitale delle scadenze (semplice foglio con alert) avrebbe evitato la diffida e l'ansia.",
 "UNI EN ISO 7010 (segnaletica); UNI 11292 (planimetrie evacuazione); D.M. 03/08/2015 (documentazione).",
 "Il registro delle scadenze (estintori, porte, prove, formazione) è la spina dorsale della conformità: chi non ha il registro, non ha la conformità."),
s("Casi incendio", "Gli incendi edilizi: lezioni dai casi reali",
 "L'analisi degli incendi reali insegna più di ogni norma: i pattern ricorrenti in edilizia: incendi durante i lavori (saldature, flessibili, stufe da cantiere), sottodimensionamento o mancata manutenzione degli impianti elettrici, fumi letali attraverso gli impianti di climatizzazione non settati, materiali di finitura non conformi, vie di esodo bloccate da materiali.",
 "Pattern e contromisure: lavori a caldo (permesso di lavoro, vigilanza post-lavoro 60 minuti), manutenzione impianti elettrici (termografie periodiche), canalizzazioni con serrafiamma, materiali con reazione al fuoco certificata, esodi sempre liberi (ispezione quotidiana); l'assicurazione all-risk cantiere copre i danni diretti ma non la responsabilità penale.",
 "Cantieri, edifici esistenti, manutenzione programmata, gestione immobili.",
 "Le lezioni dei casi reali sono concrete: 'è successo davvero, così' è più efficace di ogni astratto nella formazione dei cantieri.",
 "Ogni incendio ha cause note e prevenibili: l'incidente 'imprevedibile' è quasi sempre una catena di scelte trascurabili.",
 "Costo delle contromisure: marginale (procedura, controllo, formazione); il costo medio di un incendio edilizio: da decine di migliaia a milioni di euro più eventuali responsabilità penali.",
 "Incendio in un cantiere di ristrutturazione causato da flessibile lasciato acceso su pannelli isolanti: danno totale 700.000 € e 2 persone intossicate; la vigilanza post-lavoro di 30 minuti (costo: nulla) avrebbe spento il principio.",
 "Relazioni VVF e studi settoriali; normativa vigente.",
 "Da insegnare al LLM: la sicurezza antincendio è una CULTURA quotidiana, non una pratica da esibire in fase di collaudo."),
]

README = """# SICUREZZA_ANTINCENDIO_ACCESSIBILITA_PACK — Prevenzione incendi e accessibilità

**Facoltà:** FACOLTA_IMPIANTI_ENERGIA · **Livello:** L2 · **Schede:** {n}

## Contenuto
La prevenzione incendi per edilizia: quadro normativo (D.M. 03/08/2015), vie di esodo,
mezzi di estinzione, compartimentazione REI, gestione dell'emergenza (PEI, prove di
evacuazione), accessibilità e abbattimento barriere (DM 236/89), ascensori e
piattaforme, segnaletica di sicurezza e documentazione, lezioni dai casi reali.

## Formato
- `schede/schede.jsonl` — una scheda per riga, 11 campi standard.
- `COURSE.yaml` — metadati del corso.

## Uso per l'addestramento
Adatto a: consulenza su attività con pubblico, verifica di conformità, dialogo con
professionisti abilitati e VVF. NON sostituisce il progetto del professionista
abilitato alla prevenzione incendi: insegna la logica e le domande giuste.
""".format(n=len(DATA))

COURSE = """corso: "Prevenzione incendi e accessibilità"
facolta: "FACOLTA_IMPIANTI_ENERGIA"
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
