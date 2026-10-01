# -*- coding: utf-8 -*-
"""OSPEDALI_E_HEALTHCARE_PACK: edilizia sanitaria, flussi, gas medicali, finiture igieniche."""
import json, os

ROOT = os.path.dirname(os.path.abspath(__file__))

def s(cat, nome, desc, tec, app, van, lim, cos, casi, norm, note):
    return dict(categoria=cat, nome=nome, descrizione=desc, tecnologia=tec,
                applicazioni=app, vantaggi=van, limiti=lim, costi_e_economia=cos,
                casi_real_world=casi, normative=norm, note_cantiere=note)

DATA = [
s("Fondamenti", "L'edilizia sanitaria: progettare per la cura",
 "L'ospedale è la tipologia edilizia più complessa: ospita attività che vanno dalla grande chirurgia (l'area operatoria è una 'fabbrica' di precisione) all'accoglienza dell'utente fragile (il paziente anziano, il bambino, il disabile); il progetto integra flussi (puliti, sporchi, pubblici, sanitari), tecnologie (medical gas, imaging), normative (sanitarie, antincendio, igieniche) e architettura.",
 "Principi: la separazione dei flussi (il percorso del paziente pulito non incrocia quello dei rifiuti o dei defunti, il pubblico non entra nelle zone sanitarie), la degenza come cuore (le camere con servizi, la day surgery), la flessibilità (la sanità cambia: i locali devono adattarsi), la luce naturale e il verde (il benessere cura: la terrazza di degenza, il cortile); le norme: le prescrizioni igienico-sanitarie regionali, l'antincendio DM 2015 con specifiche per le attività sanitarie, l'accessibilità.",
 "Nuovi ospedali, ristrutturazioni di reparti, cliniche, residenze sanitarie assistite (RSA).",
 "L'ospedale ben progettato riduce lo stress dei pazienti (degenza più corta: studi documentati su vista verde e luce) e degli operatori (i flussi efficienti risparmiano migliaia di passi al giorno).",
 "La complessità normativa e funzionale è massima: i progetti ospedalieri richiedono team multidisciplinari e anni.",
 "Costi: un nuovo ospedale: 3.000-8.000 €/m² (molto variabile per le attrezzature); la ristrutturazione di un reparto: 1.500-4.000 €/m².",
 "Ospedale con degenze con vista su un cortile verde e percorsi interni 'a anello' (nessun corridoio cieco): la soddisfazione dei pazienti e dei familiari è salita (rilevazioni) e i tempi di degenza per alcuni reparti si sono ridotti percettibilmente.",
 "Normativa sanitaria nazionale e regionale (requisiti igienici, DPR 14/1/1997 per le strutture accreditate); DM 03/08/2015; D.Lgs 80/1992 (accessibilità).",
 "La prima domanda: 'chi entra qui e chi esce, con cosa e dove?' — la mappa dei flussi si disegna prima delle piante."),
s("Flussi", "I flussi ospedalieri: puliti, sporchi, pubblici e sanitari",
 "L'ospedale vive di flussi separati: il paziente (pubblico → sanitario), il personale (cambio → reparto), le merci (consegna → magazzino → reparto), i rifiuti (reparto → smaltimento), i defunti (reparto → obitorio → uscita dedicata), i mezzi (ambulanze → pronto soccorso). La separazione è gerarchica: i flussi 'sporchi' non incrociano mai i 'puliti'.",
 "Strumenti: lo schema dei flussi (diagramma che sovrappone tutti i percorsi sulle piante: gli incroci da eliminare), le corsie (i corridoi ospedalieri hanno larghezze doppie per far passare due barelle in controv), le corsie? i 'corridoi di distribuzione' separati per servizi e per sanitari, i montacarichi dedicati (uno per cibo e farmaci, uno per rifiuti e biancheria sporca), gli ascensori 'ibridi' per pazienti, le uscite dedicate (l'uscita ambulanze separata dal pronto soccorso pubblico).",
 "Progettazione e riorganizzazione di ospedali, cliniche, laboratori.",
 "I flussi giusti risparmiano tempo e riducono gli errori (la barella che non aspetta l'ascensore, il farmaco che non attraversa la cucina).",
 "La separazione totale dei flussi richiede spazio: i budget stretti spingono a compromessi che poi pagano in efficienza quotidiana.",
 "Costo: lo schema dei flussi è progetto (il costo è nel tempo dei progettisti); il risparmio operativo: il vero beneficio.",
 "Pronto soccorso riorganizzato con percorso ambulanze separato dal pubblico e triage all'ingresso: i tempi di presa in carico sono migliorati del 30% e gli accessi 'inappropriati' ridotti (il percorso pubblico non si confonde più con quello sanitario).",
 "Normativa sanitaria regionale; linee guida ministeriali (il 'modello ospedale'); buona pratica internazionale ( Evidence-based design).",
 "La prova del nove: disegnare il percorso di una barella dal pronto soccorso alla sala operatoria e contare le porte, gli incroci e gli ascensori."),
s("Sale operatorie", "Le sale operatorie: la fabbrica della precisione",
 "La sala operatoria è l'ambiente tecnologicamente più denso dell'edilizia: il blocco operatorio (il gruppo di sale) richiede: aria a flusso laminare con filtrazione assoluta (le sale 'pulite' hanno una qualità d'aria controllatissima), i gas medicali a colonna? (a colonna di distribuzione), i pavimenti e i rivestimenti lavabili e continui, la possibilità di manutenere le attrezzature senza entrare in sala (i locali tecnici attorno).",
 "Elementi: il sistema di ventilazione a flusso laminare verticale (l'aria 'cade' sulla zona operatoria sterile, i ricambi 20-600? i ricambi d'aria alti, i filtri HEPA assoluti), le colonne di distribuzione dei gas (ossigeno, protossido? no: protossido esclude; anidride carbonica, aria medicale, vuoto per le aspirazioni) con le prese a parete standardizzate (i colori e le forme distinguono i gas per non scambiare mai), i controsoffitti tecnici con l'accesso dall'alto, la separazione dei percorsi (il paziente entra da una parte, il personale da un'altra, i materiali da un'altra).",
 "Blocchi operatori di ospedali e cliniche, ambulatori chirurgici, laboratori di alta sicurezza.",
 "La sala operatoria è il gioiello: l'efficienza del blocco (i tempi di cambio sala) decide la produttività chirurgica dell'ospedale.",
 "La rigidità progettuale: le sale mal pensate non si adattano ai robot chirurgici (il Da Vinci richiede spazi e strutture specifici).",
 "Costi: il blocco operatorio: 10.000-30.000 €/m² (con attrezzature); la sola edilizia: voci specifiche.",
 "Blocco operatorio riprogettato con sale modulari e locali tecnici esterni: i tempi di cambio tra un intervento e l'altro sono calati del 25% (più sale operabili al giorno); la sala gemella 'tradizionale' dello stesso ospedale resta il collo di bottiglia.",
 "Normativa UNI EN ISO 14644? No: i riferimenti: linee guida ministeriali sulle sale operatorie; norme sui gas medicali (UNI EN ISO 9170); antincendio specifico.",
 "La domanda di progetto: 'quanto tempo perde il chirurgo tra un paziente e l'altro?' — la risposta si progetta."),
s("Gas medicali", "I gas medicali: ossigeno, vuoto, aria medicale",
 "I gas medicali sono l'impianto vitale dell'ospedale: l'ossigeno (i pazienti in terapia intensiva), l'aria medicale (la respirazione assistita), il vuoto (le aspirazioni chirurgiche), l'anidride carbonica (la chirurgia laser e laparoscopica), i generatori speciali; distribuiti da centrali (le bombolette? i serbatoi criogenici esterni o i compressori) a colonne di reparto e prese terminali.",
 "Sistemi: le centrali (l'ossigeno liquido in serbatoi criogenici, l'aria compressa da centrali con filtrazione, il vuoto da centrali di aspirazione), le reti di distribuzione (il rame o l'acciaio inox, la sezione 'a doppia' per la continuità), le colonne di reparto (i quadri di zona con valvole di sicurezza), le prese terminali (i punti di connessione standardizzati: ogni gas ha la sua forma e il suo colore per non scambiare mai); la verifica: l'allarme di pressione, il controllo continuo, le manutenzioni certificate.",
 "Ospedali, cliniche, RSA, ambulatori con chirurgia.",
 "I gas medicali sono come l'elettricità del paziente critico: quando mancano, i reparti di terapia intensiva si fermano in minuti.",
 "Il rischio di scambio gas (la presa sbagliata) è il disastro tecnico massimo: la standardizzazione delle prese è sacra.",
 "Costi: la centrale gas di un ospedale medio: 200.000-1.000.000 €; la rete: 100-300 €/punto presa.",
 "Centralina di ossigeno con doppia linea di backup e allarmi: durante un guasto alla linea principale, il passaggio automatico sul serbatoio di riserva è avvenuto in secondi senza che i reparti se ne accorgessero.",
 "UNI EN ISO 7396-1 (sistemi gas medicali); normativa ministeriale; certificazioni specifiche.",
 "La regola ferrea: mai scambiare le prese, mai manomettere? mai manomettere; le prese hanno forme diverse proprio per questo — la tolleranza zero."),
s("Degenza", "La degenza: la camera come ambiente di cura",
 "La camera di degenza è la 'casa' del paziente per giorni o mesi: il progetto moderno privilegia le camere con servizi private o doppie (l'isolamento dell'infezione, la dignità), la vista verde (il contatto con la natura accelera la guarigione: studi di evidence-based design), i sistemi di nurse call (il pulsante di chiamata con risposta garantita).",
 "Elementi: il letto come centro (gli spazi laterali 80-90 cm per i carrelli e l'accesso dei medici), il bagno accessibile (braccioli, spazi manovra, sedili doccia), la parete testata del letto con i punti tecnici (ossigeno, vuoto, correnti, nurse call), l'illuminazione d'atmosfera (per la notte senza svegliare il compagno di stanza), la TV e il Wi-Fi come servizio, la climatizzazione con aria singola? (le camere con ventilazione autonoma per il controllo infezioni); le camere 'High Dependency' (quelle vicine alla guardia).",
 "Ospedali, cliniche, RSA, hospice.",
 "La camera dignitosa migliora il percepito della qualità sanitaria più di molte tecnologie: il paziente 'si cura anche con gli occhi'.",
 "Il privato singolo costa: il budget pubblico spinge a camere multiple che in epoca pandemica si sono rivelate critiche.",
 "Costi: la camera di degenza arredata e attrezzata: 15.000-40.000 € (escluso il letto tecnico).",
 "Reparto con camere doppie convertite in singole durante un'emergenza epidemica: la flessibilità progettuale (le pareti divisorie smontabili) ha permesso il cambio in giorni invece che mesi.",
 "Normativa sanitaria regionale; linee guida ministeriali; standard di accreditamento.",
 "La camera si progetta dal letto: si parte dal paziente sdraiato e si disegna tutto intorno."),
s("Imaging", "L'imaging diagnostico: Tac, Risonanza, i locali blindati",
 "L'imaging diagnostico (TAC, Risonanza Magnetica, PET, mammografia) richiede locali specialissimi: la Risonanza ha il magnete superconduttivo (il campo magnetico resta SEMPRE attivo: le stanze hanno regole ferree di accesso, i materiali ferrosi sono banditi vicino), la TAC ha il bunker di radiazione (pareti in piombo o barite contro le radiazioni).",
 "Requisiti: la RM ha il siting magnetico (le onde 'radiofrequency' interferiscono: le apparecchiature vicine vanno schermate, il magnete ha i quench pipe per lo scarico dell'elio in emergenza), il pavimento rinforzato (il magnete pesa 4-8 tonnellate), la zona di sicurezza con controllo accessi ferrosi (i sedili? i metalli volano verso il magnete); la TAC ha il bunker (le pareti con barite o piombo calcolati in base alla potenza), la porta scorrevole piombata, i sistemi di interlock (la porta aperta ferma la macchina); entrambe hanno l'aria condizionata dedicata e l'alimentazione elettrica stabilizzata.",
 "Ospedali, centri diagnostici, policlinici.",
 "Le apparecchiature costano milioni: l'edilizia che le ospita va progettata CON il produttore (i manuali di siting vanno rispettati al centimetro).",
 "La RM 'incompatibile' con l'edificio (i ferri strutturali vicini, i cavi dell'impianto) richiede interventi di schermatura costosissimi o il ripensamento dell'ubicazione.",
 "Costi: il locale RM (schermature comprese): 300.000-800.000 €; il bunker TAC: 150.000-400.000 €; l'apparecchiatura: a parte (milioni).",
 "Centro diagnostico con la RM posizionata al piano terra lontana dai ferri strutturali (il siting studiato dal produttore): la schermatura è stata minima e l'installazione senza sorprese; il centro gemello con la RM 'dove c'era spazio' ha speso il doppio in schermature correttive.",
 "Manuali di siting dei produttori; normativa radioprotezione (D.Lgs 101/2020); norme elettromagnetiche.",
 "La prima verifica: il siting magnetico viene fatto PRIMA di scegliere il locale — il magnete decide dove vive, non il contrario."),
s("Ospedale diffuso", "L'ospedale diffuso: digitale, territorio, riabilitazione",
 "Il futuro sanitario è diffuso: l'ospedale si alleggerisce (la day surgery, la diagnostica veloce) e il territorio si rafforza (le case della salute, i distretti, la telemedicina); l'edilizia segue: meno grandi monoblocchi, più reti di strutture piccole vicine alle persone.",
 "Modelli: le Case della Salute (i poli territoriali che uniscono medicina di base e specialistica), i centri di riabilitazione (il post-ospedale che sgrava i grandi ospedali), gli Hospice (le cure palliative dignitose in contesti domestici), l'ospedale digitale (i posti letto 'virtuali' con il monitoraggio domiciliare); il progetto: le piccole strutture sanitarie devono comunque rispettare le norme (gas medicali, antincendio, accessibilità) in scala ridotta e flessibile.",
 "Reti sanitarie territoriali, riabilitazione, lungodegenza, assistenza domiciliare.",
 "L'ospedale diffuso porta la cura vicino: meno trasporti, più prevenzione, degenze più corte.",
 "La dispersione aumenta i costi di gestione (tante piccole strutture da mantenere).",
 "Costi: la casa della salute: 2.000-5.000 €/m²; il centro di riabilitazione: simile all'edilizia sanitaria standard.",
 "Rete di Case della Salute in una regione: i ricoveri ordinari per patologie croniche sono calati del 15% in 3 anni (meno accessi al grande ospedale, più gestione sul territorio).",
 "Normativa sanitaria regionale; direttive ministeriali sulla riorganizzazione territoriale.",
 "La direzione: il grande ospedale fa il complesso, il territorio fa il resto — l'edilizia sanitaria del futuro è una rete."),
]

README = """# OSPEDALI_E_HEALTHCARE_PACK — Edilizia sanitaria: flussi, sale operatorie, gas medicali

**Facoltà:** FACOLTA_INGEGNERIA · **Livello:** L3 · **Schede:** {n}

## Contenuto
L'edilizia della cura: principi dell'ospedale moderno (flussi separati, degenza
dignitosa, evidence-based design), la mappa dei flussi (puliti/sporchi/pubblici/
sanitari), le sale operatorie (flusso laminare, gas medicali a colonna, percorsi
separati), i gas medicali (centrali, reti, prese standardizzate anti-scambio),
la camera di degenza come ambiente di cura, l'imaging diagnostico (RM e siting
magnetico, bunker TAC in barite/piombo) e l'ospedale diffuso (Case della Salute,
riabilitazione, telemedicina).

## Formato
- `schede/schede.jsonl` — una scheda per riga, 11 campi standard.
- `COURSE.yaml` — metadati del corso.

## Uso per l'addestramento
Adatto a: cultura delle strutture sanitarie, dialogo con planner sanitari e
fornitori di apparecchiature, verifica di locali tecnici, comprensione delle
reti sanitarie territoriali. Il criterio guida: l'ospedale si progetta dal
paziente (sdraiato sul letto) e dal flusso (la barella che non aspetta).
""".format(n=len(DATA))

COURSE = """corso: "Edilizia sanitaria e ospedaliera"
facolta: "FACOLTA_INGEGNERIA"
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
