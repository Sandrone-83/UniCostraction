# -*- coding: utf-8 -*-
"""SERRAMENTI_E_VETRATE_PACK: infissi, materiali, vetro, posa, manutenzione."""
import json, os

ROOT = os.path.dirname(os.path.abspath(__file__))

def s(cat, nome, desc, tec, app, van, lim, cos, casi, norm, note):
    return dict(categoria=cat, nome=nome, descrizione=desc, tecnologia=tec,
                applicazioni=app, vantaggi=van, limiti=lim, costi_e_economia=cos,
                casi_real_world=casi, normative=norm, note_cantiere=note)

DATA = [
s("Materiali", "I materiali degli infissi: legno, alluminio, PVC, acciaio, misti",
 "Il telaio del serramento si sceglie per durabilità, isolamento, manutenzione e prezzo: legno (nobile, isolante, va mantenuto ogni 4-6 anni), alluminio (sottile, resistente, ponti termici da gestire), PVC (economico, isolante, vincoli sulle dimensioni), acciaio (sottilissimo, per tagli architettonici), misti (alluminio-legno: esterno resistente, interno caldo).",
 "Criteri tecnici: il profilo deve avere il taglio termico (barretta in poliammide) per non condensare; il legno: essenze stabili (meranti, rovere) o multistrato; il PVC: rinforzi interni in acciaio per luci grandi; il coefficiente Uw (trasmittanza finestra) dipende da telaio + vetro + spaziatura: i telai moderni arrivano a Uw 1,0-1,2 W/m²K con vetri tripli.",
 "Finestre e portefinestre residenziali, facciate continue, portoni, serramenti per edilizia pubblica.",
 "Il serramento giusto dura 30-50 anni e taglia i consumi del 20-40% rispetto a infissi vecchi: è tra gli investimenti con il ritorno più rapido nell'edilizia esistente.",
 "Il PVC lasciato al sole estivo si scalda e può deformare in luce; l'alluminio senza taglio termico condensa invernale; il legno trascurato marcisce ai ferri.",
 "Costi indicativi serramento completo: PVC 180-350 €/m², alluminio taglio termico 300-600 €/m², legno 400-900 €/m², misto 500-1.000 €/m², posa inclusa circa.",
 "Sostituzione serramenti in appartamento anni '70 (da vetro singolo a doppio con taglio termico): consumo riscaldamento ridotto del 28% misurato sulle bollette, eliminata la condensa mattutina sui vetri.",
 "UNI EN 14351-1 (finestre: marcatura CE, prestazioni); UNI 11673 (installazione); leggi regionali sui requisiti energetici.",
 "Domanda guida: esposizione al sole, budget, manutenzione che il cliente farà DAVVERO — le tre risposte scelgono il materiale."),
s("Vetro", "Il vetro: camera, triplo, basso emissivo, sicurezza",
 "Il vetro è il cuore prestazionale del serramento: vetro camera (2 lastre + intercapedine 12-16 mm con gas argon), triplo (3 lastre, per climi freddi), basso emissivo (metallizzazione che riflette il calore interno invernale), selettivo (lascia luce, taglia calore estivo), di sicurezza (temperato, stratificato con PVB).",
 "Parametri: Ug (trasmittanza del vetro: singolo 5,8 / doppio 1,1 / triplo 0,6 W/m²K circa), g (fattore solare: quanto calore entra), TL (trasmissione luce), sicurezza: temperato per resistere agli urti, stratificato per restare in posa quando si rompe; l'intercapedine con argon riduce le dispersioni; l'attacco ai telai con distanziali caldi evita condensa perimetrale.",
 "Ogni finestra: la scelta vetro dipende da esposizione (sud freddo: selettivo alto g; sud caldo: selettivo basso g) e da vincoli di sicurezza (porte, finestre basse, balaustre).",
 "Il vetro giusto fa più dell'isolante del muro: un buon vetro camera vale quanto 20 cm di cappotto sulla superficie vetrata.",
 "Il triplo non sempre paga: in climi miti il beneficio rispetto al doppio è modesto e l'aumento di peso/costo è reale.",
 "Delta costo: da vetro singolo a doppio basso emissivo: +40-80 €/m² di vetro; il triplo: altri +30-60 €/m².",
 "Vetrata sud-est con vetro selettivo a basso g: la sovratemperatura estiva interna è scomparsa senza schermature esterne; la vetrata gemella a vetro standard aveva reso la stanza inutilizzabile dalle 14 alle 18 in estate.",
 "UNI EN 674/675/676 (metodi prova Ug); UNI EN 1279 (vetro camera durabilità); UNI EN 12150/14449 (temperato/stratificato).",
 "La domanda non è 'quanto costa il vetro?' ma 'quanto calore entra ed esce da questo vetro in questa esposizione?'"),
s("Posa", "La posa in opera: il serramento si gioca nell'installazione",
 "Il miglior serramento del mondo installato male è una perdita di denaro: la posa corretta gestisce il sopralluce, l'ancoraggio al muro, la coibentazione dello spazio tra telaio e muratura, la tenuta all'acqua con i sistemi di drenaggio.",
 "Regole: il sopralluce di posa 10-20 mm (tolleranza muratura), ancoraggi a tasselli a distanza regolare (ogni 60-70 cm, mai sul profilo del vitigno? mai sulle alette), la schiuma espansa bassa espansione per il coibentamento interno + fascia perimetrale esterna con membrane traspiranti o profili di tenuta, il fissaggio della soglia con calzo strutturale, la prova di tenuta all'acqua (cannuccia? doccia di prova) prima della consegna.",
 "Installazione di infissi nuovi, sostituzione in ristrutturazione, posa in edilizia nuova con cassero.",
 "La posa certificata vale quanto il serramento: l'installazione a regola d'arte elimina le condense, le spifferate e le infiltrazioni che umiliano i serramenti belli.",
 "La sostituzione 'frettolosa' (serramento misurato a occhio, schiuma ovunque, niente tenuta esterna) produce muffa ai lati in 2 inverni.",
 "Costo posa: 60-150 €/infisso (o 15-25% del valore serramento); la certificazione di posa UNI 11673: richiesta al posatore.",
 "Sostituzione serramenti con fascia perimetrale a tenuta e prova doccia: dopo 3 inverni, zero infiltrazioni e zero condensa; il condominio vicino con posa 'classica' ha rifatto i davanzali umidi di 6 appartamenti.",
 "UNI 11673 (installazione serramenti: livelli di esecuzione); UNI 11425 (posa a regola d'arte); libretto di posa.",
 "Fermo al cantiere: nessun serramento si consegna senza il libretto di posa compilato e la prova di tenuta."),
s("Oscuranti", "Persiane, tapparelle, frangisole: l'ombra come prestazione",
 "Gli oscuranti esterni sono la prima schermatura solare: persiane (tradizione italiana, ottime in estate), tapparelle (comode, isolano), frangisole orientabili (prestazionali, architettonici), tende da sole per esterni; l'ombra esterna taglia il calore solare del 70-90% prima che entri in casa.",
 "Meccanismi: persiane a lamelle orientabili (alluminio, PVC, acciaio), tapparelle coibentate con schiuma (isolano oltre a oscurare), frangisole a lamelle con orientamento manuale o motorizzato; la motorizzazione: motori tubolari con comando centralizzato o domotico; la posa: cassetti da incasso o sovrapposto, guide a tenuta.",
 "Residenze, uffici con vetrature esterne, edilizia climatica calda, ristrutturazioni energeticamente rilevanti.",
 "La schermatura esterna vale più del vetro selettivo sul caldo estivo: blocca il sole PRIMA del vetro, il metodo più efficace in assoluto.",
 "Le tapparelle chiuse d'estate isolano ma oscurano: il compromesso luce/calore va gestito (lamelle orientabili come via di mezzo).",
 "Costi: tapparella coibentata 80-200 €/m², persiane alluminio 100-250 €/m², frangisole orientabili 200-500 €/m², motorizzazione +150-400 € per punto.",
 "Ufficio vetrato con frangisole orientabili motorizzati a sensori solari: il calore estivo in vena? No: in facciata è sceso del 60%, la luce naturale resta gestita e i consumi di climatizzazione estiva sono calati di un terzo.",
 "Nessuna norma cogente specifica (salvo requisiti energetici che li premiano); marcatura CE degli oscuranti.",
 "Regole climatiche: al sud e nelle vetrature grandi la schermatura esterna è obbligatoria 'di fatto' per il comfort estivo; progettarla SEMPRE insieme ai serramenti, non dopo."),
s("Facciate continue", "Le facciate continue: la vetrata architettonica",
 "La facciata continua (curtain wall) è il sistema a montanti e traversi in alluminio e vetro delle architetture moderne: la struttura portante sta dietro al vetro, l'acqua scende per gravità e defluisce nei condotti nascosti (principio a cascata).",
 "Sistemi: stick (montanti e traversi montati in sequenza, economici), unitized (moduli prefabbricati interi innalzati a gru, qualità industriale), semi-unitized; la tenuta: EPDM e siliconi strutturali o meccanici, la camera di drenaggio dietro al vetro, i nodi di giunzione; le prestazioni: permeabilità all'aria, tenuta all'acqua, resistenza al vento, trasmittanza Uf, fattore solare.",
 "Uffici, direzioni, sedi istituzionali, alberghi moderni, centri commerciali.",
 "La facciata continua libera l'architettura: superfici vetrate continue senza spalle di interruzione, con prestazioni controllate.",
 "La manutenzione delle facciate continue è specializzata e costosa: i guasti ai siliconi dopo 15-20 anni richiedono rifacimenti parziali con piattaforme.",
 "Costi: facciata continua 700-1.500 €/m² installata (ordini di grandezza, molto variabile).",
 "Sede direzionale con facciata unitized: il montaggio ha richiesto metà del tempo della facciata stick comparabile, con qualità di tenuta superiore verificata in prova camino? No: verificata in prova di tenuta in cantiere.",
 "Normativa facciate (reazione al fuoco, sicurezza strutturale vetri); specifiche sistemi; UNI sui vetri strutturali.",
 "La facciata continua si progetta con il facciatista (sistema, nodi, vetri) dall'inizio: chi la 'disegna' dopo dal generale paga di ritardi e varianti."),
s("Porte", "Le porte: interne, blindate, tagliafuoco, automatiche",
 "Le porte sono funzione e sicurezza: interne (legno, vetro, laminato), blindate (sicurezza abitativa), tagliafuoco REI (compartimentazione), automatiche (flussi pubblici), scorrevoli (risparmio spazio); ogni tipologia ha la sua norma, i suoi telai e le sue soglie.",
 "Porte interne: telaio + anta con cerniere a scomparsa o esterne, serrature magnetiche (silenzio), altezze standard 200-210 cm (fuori misura su misura); blindate: classe 3-4 di resistenza alla effrazione (UNI EN 1627), serrature a cilindro europeo, cerniere antistrappo; tagliafuoco: certificazione REI 30/60/120, chiudiporta obbligatorio, spioncini? No: segni? i vetri devono essere certificati tagliafuoco; automatiche: sensori e sicurezze anti-schiacciamento (normativa EN 16005).",
 "Ogni edificio: abitazioni, uffici, locali pubblici, alberghi, ospedali.",
 "La porta giusta nel punto giusto: la blindata sul perimetro, la tagliafuoco nei compartimenti, la silenziosa in camera da letto: dettaglio che cambia la vita quotidiana.",
 "La porta tagliafuoco tenuta aperta con un cuneo (per comodità) annulla la compartimentazione: è la violazione più comune e più pericolosa.",
 "Costi: porta interna 150-600 € (su misura 800-2.500 €), blindata 800-3.000 €, tagliafuoco 400-1.200 €, automatica 2.000-10.000 €.",
 "Albergo con porte tagliafuoco con chiudiporta a scomparsa (a norma e silenziose): in emergenza tutte chiuse; il cliente abituato agli alberghi 'con i cunei' ha apprezzato l'attenzione alla sicurezza reale.",
 "UNI EN 1627 (resistenza effrazione); UNI EN 1634 (tagliafuoco porte); UNI EN 16005 (porte automatiche).",
 "La porta si sceglie per percorso: dove passa chiunque (pubblico) va robusta e automatica, dove dorme qualcuno va silenziosa, dove divide il fuoco va certificata."),
s("Manutenzione", "La manutenzione dei serramenti: lubrificazione, guarnizioni, vetri",
 "I serramenti durano decenni se mantenuti: le guarnizioni (gomme che invecchiano), le cerniere e le guide (che vanno lubrificate), i vetri (pulizia e controllo distanziali), i ferramenta (serrature e maniglie).",
 "Programma: lubrificazione cerniere e meccanismi 1-2 volte/anno (grasso o olio a silicone), controllo guarnizioni ogni 3-5 anni (sostituzione quando si induriscono o si rompono), pulizia binari e profili (acqua e neutro, mai solventi aggressivi), verifica viti di ancoraggio dopo i primi anni, la riverniciatura del legno ogni 4-6 anni (smalto o impregnante), controllo condensa persistente nelle camere (distanziale guasto: sostituzione vetro).",
 "Condomini, case private, gestioni patrimoniali, manutenzione programmata.",
 "La manutenzione costa il 5% del valore del serramento l'anno e ne raddoppia la vita: il conto più semplice dell'edilizia.",
 "I serramenti 'mai toccati in 20 anni' richiedono la sostituzione totale mentre quelli mantenuti bastava riverniciare.",
 "Costi: manutenzione annua: 5-15 €/finestra; guarnizioni: 5-10 €/m; riverniciatura legno: 30-80 €/anta.",
 "Portoncino in legno riverniciato ogni 5 anni: a 30 anni è ancora perfetto; il portoncino identico del condominio vicino 'mai toccato': sostituito a 14 anni per marciume ai ferri.",
 "Nessuna norma cogente; prassi produttori e manutentori.",
 "La frase da insegnare: il serramento è come la macchina: il tagliando costa poco, il motore fuso costa tutto."),
]

README = """# SERRAMENTI_E_VETRATE_PACK — Infissi, vetri, posa, facciate, porte

**Facoltà:** FACOLTA_TECNOLOGIA_E_COSTRUZIONE · **Livello:** L2 · **Schede:** {n}

## Contenuto
Il mondo degli infissi: materiali dei telai (legno, alluminio, PVC, acciaio, misti),
il vetro (camera, triplo, basso emissivo, selettivo, sicurezza), la posa a regola
d'arte (UNI 11673, libretto di posa), gli oscuranti esterni come schermatura
solare, le facciate continue (stick, unitized, principio a cascata), le porte
(interne, blindate, tagliafuoco, automatiche) e la manutenzione programmata.

## Formato
- `schede/schede.jsonl` — una scheda per riga, 11 campi standard.
- `COURSE.yaml` — metadati del corso.

## Uso per l'addestramento
Adatto a: consulenza su sostituzione infissi, dialogo con posatori certificati,
scelta vetro-esposizione, verifica posa in cantiere. I valori U e i prezzi sono
fasce 2025 da verificare sulle schede tecniche aggiornate.
""".format(n=len(DATA))

COURSE = """corso: "Serramenti, vetrate e porte"
facolta: "FACOLTA_TECNOLOGIA_E_COSTRUZIONE"
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
