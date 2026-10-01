# -*- coding: utf-8 -*-
"""DATA_CENTER_E_CRITICAL_FACILITIES_PACK: sale server, continuità, climatizzazione di precisione."""
import json, os

ROOT = os.path.dirname(os.path.abspath(__file__))

def s(cat, nome, desc, tec, app, van, lim, cos, casi, norm, note):
    return dict(categoria=cat, nome=nome, descrizione=desc, tecnologia=tec,
                applicazioni=app, vantaggi=van, limiti=lim, costi_e_economia=cos,
                casi_real_world=casi, normative=norm, note_cantiere=note)

DATA = [
s("Fondamenti", "Che cos'è un data center: l'edificio che non può fermarsi",
 "Il data center è l'edificio della continuità: ospita i server che tengono in funzione aziende, servizi, cloud; ogni interruzione costa migliaia di euro al minuto (stime settoriali per i servizi finanziari e cloud), quindi tutto è ridondante: alimentazione, clima, rete, struttura.",
 "I livelli: lo standard Uptime Tier (I-IV) classifica la resilienza (Tier IV = tollera ogni guasto senza interruzione, con duplicazione totale); il TIA-942 definisce gli aspetti di progetto (camere, corridoi, potenza); le metriche: PUE (Power Usage Effectiveness: energia totale / energia IT, il santo graal dell'efficienza: i migliori < 1,2, la media storica ~1,5+), il livello di servizio (SLA 99,982% per Tier IV).",
 "Cloud provider, banche, PA, grandi aziende, edge computing urbano.",
 "La domanda digitale cresce del 10-20%/anno: i data center sono l'edilizia che più cresce nel mondo (stima settore).",
 "Consumano tantissima energia: la localizzazione (freddo, energia rinnovabile) è la nuova leva competitiva.",
 "Costi: un rack IT (0,5 m²) vale 15.000-50.000 €; l'edilizia: 6.000-15.000 €/m² (iper-specializzata).",
 "Edge data center in una città del nord: il freddo esterno free-cooling (l'aria esterna raffredda direttamente) ha ridotto il PUE da 1,5 a 1,15, con risparmio energetico di milioni di euro in 10 anni.",
 "TIA-942 (standard progettazione); standard Uptime Tier; EN 50600 (serie europea); normativa antincendio specifica.",
 "La prima legge del data center: il costo di NON funzionare supera qualsiasi costo di costruzione — si progetta per non fermarsi mai."),
s("Continuità", "La continuità elettrica: UPS, gruppi elettrogeni, doppie alimentazioni",
 "L'alimentazione del data center è a catena ridondata: due linee elettriche indipendenti (da sottostazioni diverse), gli UPS (batterie che coprono i micro-interruzioni), i gruppi elettrogeni (motoriduttori? No: generatori diesel/gas per le interruzioni lunghe), le STS (commutazioni statiche che scambiano tra le due linee in millisecondi).",
 "Architettura: le due linee A e B alimentano ogni rack (doppia alimentazione dei server), gli UPS a modularità o monoblocco (10-15 minuti di autonomia: il tempo di avviare i generatori), i generatori con autonomia di carburante 24-48 ore (o gas metano), i bypass di manutenzione (si può manutenere tutto senza spegnere); la verifica: i collaudi con il 'black building test' (si stacca tutto e si guarda se regge).",
 "Ogni data center: dal piccolo locale aziendale all'hyperscale di 100.000 m².",
 "La ridondanza elettrica è assoluta: il data center più piccolo ha più continuità di un ospedale medio.",
 "La ridondanza non usata è costo morto: il Tier giusto si sceglie sul business (non tutti i server valgono Tier IV).",
 "Costi: UPS 200-400 €/kVA; generatori 150-300 €/kVA; la ridondanza N+1 aggiunge il 30-50% sui sistemi.",
 "Test annuale 'black building' in un data center Tier III: il passaggio sui generatori è avvenuto in 8 secondi senza interruzione dei servizi; il test ha scoperto un bypass mal configurato che avrebbe lasciato un intero corridoio scoperto.",
 "CEI 0-16 (connessione rete); specifiche TIA-942; normativa antincendio e ambientale per i generatori.",
 "Domanda cardine: 'quanto vale un minuto di fermo per questo servizio?' — la risposta definisce il Tier."),
s("Climatizzazione", "La climatizzazione di precisione: freddo per i server",
 "I server scaldano in continuazione: la climatizzazione di precisione mantiene 22-27 °C e umidità 40-60% (con tolleranze strette, i server sono delicati); i sistemi: CRAC/CRAH (unità di precisione a liquido o ad aria), i corridoi caldi e freddi (l'aria fredda davanti ai rack, quella calda dietro), il free-cooling (usare l'aria esterna quando è fredda), la refrigerazione adiabatica (l'acqua che evapora raffredda).",
 "Architetture: il contenimento (corridoi chiusi con porte, l'aria non si mescola: il free-cooling diventa possibile anche d'estate), la rear-door cooling (le porte dei rack sono radiatori ad acqua fredda), l'immersion cooling (i server immersi in liquido dielettrico: la frontiera, per i carichi estremi); il PUE guida le scelte: ogni 0,1 di PUE risparmiato vale milioni sui grandi impianti.",
 "Data center di ogni dimensione, sale server aziendali, edge node.",
 "La climatizzazione è il 40-50% del consumo elettrico: migliorarla è il primo business case (il PUE da 1,5 a 1,2 vale un terzo della bolletta).",
 "I margini di temperatura sono stretti: gli errori di taratura (umidità troppo bassa: elettrostatica; troppo alta: corrosione) guastano i server silenziosamente.",
 "Costi: CRAC 3.000-10.000 €/unità; il contenimento dei corridoi: 100-300 €/m; l'impatto sul PUE: il vero parametro economico.",
 "Data center con contenimento corridoi caldi e free-cooling: il PUE è sceso da 1,55 a 1,22; la bolletta elettrica annua si è ridotta di oltre il 20% e la potenza liberata ha permesso l'installazione di altri 200 rack senza nuovo allaccio.",
 "ASHRAE TC 9.9 (i margini termici dei server); EN 50600; specifiche dei produttori IT.",
 "La regola: il freddo è per i server, non per la stanza: contenere i corridoi, non raffrescare l'aria inutilmente."),
s("Reti", "Le reti e il cablaggio strutturato: le autostrade dei dati",
 "Il data center è fatto di connessioni: il cablaggio strutturato (fibre ottiche e rame categorizzato) collega i rack, le sale, l'esterno; la gerarchia: spine-area (fuori), inter-building (tra edifici), intra-building (le dorsali), horizontal? le horizontal (ai rack).",
 "Standard: le fibre OM4/OM5 multimodali e le OS2 monomodali (per le lunghe distanze), il cavo in rame Cat6A/Cat8 per i brevi, le prese e i pannelli di permutazione (le patch) che permettono di cambiare configurazione senza toccare i cavi strutturali; il 'cable management': le canaline e le finger (le 'dita' che guidano i cavi), la documentazione (ogni cavo etichettato: senza mappa, il data center è indecifrabile in 6 mesi).",
 "Cablaggio di data center e grandi uffici, SAN (storage), reti industriali.",
 "Il cablaggio ben documentato dimezza i tempi di intervento: l'errore 'ho staccato il cavo sbagliato' costa ore di downtime.",
 "Il cablaggio 'arruffato' (spaghetti cabling) blocca la ventilazione dei rack e rende ogni cambio un rischio.",
 "Costi: il cablaggio strutturato completo: 50-150 €/punto (ordine di grandezza); le fibre: da 5-15 €/m il cavo.",
 "Data center riorganizzato con cable management rigoroso e mappa aggiornata: i tempi di risoluzione guasti sono calati del 60% e gli errori di manutenzione azzerati.",
 "Standard TIA-568 e ISO/IEC 11801 (cablaggio); specifiche produttori.",
 "La regola: il cavo si tira una volta nella vita, la documentazione si aggiorna ogni volta che si tocca."),
s("Sicurezza DC", "La sicurezza del data center: fisica, logica, antincendio",
 "La sicurezza del data center è a cipolle: fisica (cancelli, guardie, varchi con badge, telecamere, antitaccheggio? No: anti-intrusione), logica (firewall, segmentazione), ambientale (antincendio, allagamenti, polveri); ogni accesso è tracciato (chi entra, dove, quando).",
 "Livelli: il perimetro (il sito), l'edificio (i varchi), la sala (le impronte? i badge biometrici), il rack (le chiavi elettroniche individuali); l'antincendio specifico: i gas estinguenti (FM-200, NOVEC 1230, oggi in transizione verso sostanze meno inquinanti: i clean agent) che spengono senza danneggiare i server, la rivelazione precoce (VESDA: rileva il fumo nella fase di incipiente), l'allagamento: i rilevatori d'acqua sulle pavimentazioni sospese e sotto i pavimenti rialzati; la sicurezza logica interagisce con quella fisica (l'accesso al rack richiede l'autorizzazione logica).",
 "Data center aziendali e commerciali, locali server critici.",
 "La sicurezza a strati è efficace: un solo strato violato non basta a chi non è autorizzato.",
 "La sicurezza eccessiva rallenta le operazioni quotidiane: i livelli vanno calibrati (non tutto serve Tier IV).",
 "Costi: i sistemi di controllo accessi: 5.000-50.000 €; il rilevamento incendio VESDA: 2.000-10.000 €.",
 "Tentativo di accesso non autorizzato a un rack in un data center: il badge non autorizzato ha allertato, la telecamera ha registrato, l'accesso è stato negato e tracciato: il cliente ha rinnovato il contratto per la sicurezza documentata.",
 "Normativa antincendio (D.M. 2015 con prescrizioni specifiche); GDPR per i dati di accesso; specifiche settore.",
 "La domanda: 'chi può toccare questo rack e chi lo sa?' — la tracciabilità è la metà della sicurezza."),
s("Struttura", "L'edilizia del data center: struttura, pavimenti rialzati, altezze",
 "L'edificio del data center ha esigenze particolari: i pavimenti rialzati (il sottopavimento è la plenum per l'aria fredda e i cavi, oppure tutto in over-head), le altezze generose (3-5 m sotto i controsoffitti per canalizzare aria e cavi), i carichi (i rack pieni pesano 800-1.500 kg/m²: le strutture vanno verificate), la possibilità di espansione.",
 "Elementi: il pavimento rialzato (lastre removibili su piedini: ogni punto accessibile, il freddo passa sotto), il controsoffitto tecnico (i cavi e i sensori sopra), la struttura portante con luci ridotte e controventi? la struttura con portate ridotte per i carichi concentrati, le scalinature per i passaggi (porte di ventilazione? i varchi tra le sale con sigillature per non perdere l'aria), l'isolamento acustico (i server sono rumorosi: il muro tra sale server e uffici è fonoisolante).",
 "Progettazione di nuovi data center e retrofit di edifici esistenti (la modalità più comune: ex-industriali riconvertiti).",
 "L'edilizia del data center è ingegneria 'ospedaliera': pulizia, precisione, previsione dell'imprevisto.",
 "Il retrofit dell'edificio esistente spesso non regge i carichi: le verifiche strutturali preliminari evitano cantieri bloccati.",
 "Costi: pavimento rialzato 80-200 €/m²; la struttura rinforzata: quota strutturale; l'edilizia base: 6.000-15.000 €/m².",
 "Ex capannone industriale riconvertito a data center: il rinforzo dei solai con le verifiche preliminari ha permesso l'uso senza sostituzione della struttura; il progetto senza verifica (di un altro team, poi abbandonato) richiedeva la demolizione del solaio.",
 "NTC (carichi); specifiche TIA-942; normativa antincendio e della sala.",
 "La verifica preliminare dei carichi (rack pieni, pavimenti rialzati, i gruppi elettrogeni sul tetto o in cortile) è il primo passo di ogni progetto DC."),
s("Edge e micro", "L'edge computing: il data center piccolo e ovunque",
 "L'edge computing porta il calcolo vicino all'utente (il 5G, l'IoT, la guida autonoma non possono aspettare il cloud lontano): i micro-data center (un armadio rack in un edificio), i container data center (il DC in un box pronto all'uso), le sale server pre-fabbricate; il mercato cresce più veloce dei grandi DC.",
 "Forme: l'armadio edge (2-12 rack con UPS e clima integrati, silenziosi per gli uffici), il container (20-40 piedi con tutto dentro, da collocare in un parcheggio), la micro-sala (una stanza dell'edificio con i sistemi ridondati miniaturizzati); i vantaggi: tempi di deploy settimanali, scalabilità modulare, vicinanza (latenza millisecondi invece di decine).",
 "Telco, reti 5G, industria 4.0, reti IoT, filiali bancarie.",
 "L'edge porta la potenza dove serve: la latenza è la nuova valuta (la guida autonoma non può aspettare 50 ms).",
 "I micro-DC sono vulnerabili (fisicamente accessibili): la sicurezza va rivista per il contesto urbano.",
 "Costi: armadio edge 20.000-80.000 €; container data center 100.000-500.000 € (ordini di grandezza).",
 "Container data center per una fiera tecnologica: installato in 3 giorni, operativo per l'evento, poi spostato in un'altra sede: la modularità ha evitato la costruzione di un locale permanente per un'esigenza temporanea.",
 "Standard EN 50600 (modulare); specifiche produttori; normativa antincendio ridotta per gli armadi.",
 "La direzione è chiara: il calcolo va verso le persone (edge), il consolidamento va verso l'energia pulita (grandi DC al nord) — entrambi sono edilizia."),
]

README = """# DATA_CENTER_E_CRITICAL_FACILITIES_PACK — Data center, continuità, climatizzazione di precisione

**Facoltà:** FACOLTA_IMPIANTI_ENERGIA · **Livello:** L3 · **Schede:** {n}

## Contenuto
L'edilizia della continuità digitale: i tier Uptime e lo standard TIA-942,
la continuità elettrica (UPS, generatori, doppie linee, black building test),
la climatizzazione di precisione (corridoi caldi/freddi, contenimento,
free-cooling, PUE), il cablaggio strutturato e la documentazione, la sicurezza
a cipolle (fisica, logica, antincendio con clean agent e VESDA), l'edilizia
specifica (pavimenti rialzati, carichi, acustica) e l'edge computing modulare.

## Formato
- `schede/schede.jsonl` — una scheda per riga, 11 campi standard.
- `COURSE.yaml` — metadati del corso.

## Uso per l'addestramento
Adatto a: consulenza su continuità operativa, conversazioni su Tier/PUE/SLA,
verifica di locali tecnici, cultura della ridondanza. Il criterio economico
fondamentale: il costo del fermo supera ogni costo di costruzione — si progetta
per non fermarsi mai.
""".format(n=len(DATA))

COURSE = """corso: "Data center e critical facilities"
facolta: "FACOLTA_IMPIANTI_ENERGIA"
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
