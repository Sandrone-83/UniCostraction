# -*- coding: utf-8 -*-
"""PISCINE_E_WELLNESS_PACK: vasche, strutture, impianti filtrazione, saune, hammam, normative."""
import json, os

ROOT = os.path.dirname(os.path.abspath(__file__))

def s(cat, nome, desc, tec, app, van, lim, cos, casi, norm, note):
    return dict(categoria=cat, nome=nome, descrizione=desc, tecnologia=tec,
                applicazioni=app, vantaggi=van, limiti=lim, costi_e_economia=cos,
                casi_real_world=casi, normative=norm, note_cantiere=note)

DATA = [
s("Vasche", "La vasca da costruzione: struttura, tenuta, forma",
 "La piscina da costruzione è un serbatoio in calcestruzzo armato impermeabilizzato: la struttura (getto in opera o casseri a perdere), l'impermeabilizzazione (guaina PVC o ceramica? le guaine liquide o i rivestimenti), il rivestimento (mosaico, pastina, PVC armato), i sistemi di tenuta ai movimenti del terreno.",
 "Costruzione: il getto in opera con casseri a perdere (i casseri in polistirofo che restano come isolante) o il prefabbricato (pannelli d'acciaio o casseri modulari), l'armatura ben coperta (i ferri vicini alla superficie marciscono e 'spuntano'), il sistema di impermeabilizzazione continua (la guaina PVC saldata a caldo sotto il rivestimento, i sistemi liquidi poliuretanici), la pendenza del fondo verso i bocchettoni (1,5-2% per piscine private), le scale e le sedute in getto.",
 "Piscine private, alberghiere, pubbliche, centro benessere.",
 "La vasca ben costruita dura 50 anni: le vasche 'economiche' fanno le prime crepe al terzo anno.",
 "La tenuta è critica: una fessura non riparata consuma acqua, sale e riscalda? costa denaro e mina la struttura.",
 "Costi: piscina interrata in calcestruzzo 25-50 m²: 1.500-3.000 €/m² di vasca (finiture base); il rivestimento in mosaico: extra.",
 "Piscina con guaina PVC sotto il mosaico e getto curato (curing prolungato): dopo 12 anni, zero perdite e zero infiltrazioni strutturali; la vasca gemella senza guaina ha rifatto l'impermeabilizzazione a 6 anni per alzature e infiltrazioni.",
 "Normativa piscine (D.Lgs 116/1999 per le piscine? no: il riferimento è la normativa tecnica per piscine e le prescrizioni igieniche locali); UNI 13451? Riferimento: buona pratica e specifiche.",
 "La prima legge della piscina: l'acqua è pesante (1.000 kg/m³) e sempre in movimento — la struttura e la tenuta devono rispettarla sempre."),
s("Impianto filtrazione", "Filtrazione e disinfezione: l'acqua sempre pulita",
 "L'impianto di trattamento dell'acqua è il cuore tecnico: la filtrazione (sabbia o cartuccia o diatomee) rimuove le particelle, la disinfezione (cloro, sale elettrolisi, ozono, UV) uccide i microbi, il bilancio idraulico (pompe, skimmer, bocchettoni) garantisce il ricircolo.",
 "Sistema: il ricircolo completo ogni 4-6 ore (la norma per le piscine), gli skimmer (raccolgono l'acqua di superficie: il 70% dello sporco galleggia), i bocchettoni di fondo, i fari? le bocchette di mandata, i filtri a sabbia quarzosa (backwash ogni settimana, la sostituzione ogni 3-5 anni), le pompe con prevalenza adeguata (il filtro sporco aumenta la resistenza), la disinfezione: il cloro tradizionale, l'elettrolisi del sale (produce cloro in loco: meno manutenzione chimica), l'ozono + cloro residuo (le piscine di pregio).",
 "Piscine private, pubbliche, hotel, centri sportivi.",
 "L'impianto giusto fa l'acqua cristallina con 30 minuti di cura a settimana; quello sbagliato è un secondo lavoro.",
 "La chimica mal gestita (pH fuori controllo) rovina il cloro, il rivestimento e gli occhi dei bagnanti.",
 "Costi: impianto completo di filtrazione per piscina privata 30-60 m²: 3.000-8.000 €; il locale tecnico va progettato accessibile e drenato.",
 "Piscina con elettrolisi del sale e filtro oversize (dimensionato per 1,5 volte il volume): l'acqua resta cristallina con la metà dei controlli rispetto alla piscina 'standard' dello stesso costruttore.",
 "Normativa piscine (igiene, ricircolo); specifiche dei produttori; la manutenzione programmata.",
 "La regola: il filtro è il polmone, la pompa è il cuore, la chimica è il medico: se uno dei tre è sbagliato, l'acqua lo racconta subito."),
s("Riscaldamento", "Il riscaldamento della piscina: estendere la stagione",
 "L'acqua della piscina si scalda con scambiatori (caldaia, pompa di calore, solare), la copertura mantiene il calore (l'evaporazione è la prima perdita: la coperta riduce il 70% delle dispersioni), la stagione si estende da 3 a 6-9 mesi secondo il clima e il sistema.",
 "Sistemi: la pompa di calore per piscine (il COP alto: produce 4-5 kW termici per 1 elettrico, funziona con aria dai 5-10 °C in su), gli scambiatori a piastre con la caldaia (istantanei ma costosi da usare), i pannelli solari termici (gratis dopo l'investimento, estendono la stagione), la copertura (a doghe, a bolle, automatica: è il miglior 'impianto' di riscaldamento), i deumidificatori per le piscine interne (l'umidità dell'aria interna condensa ovunque).",
 "Piscine private, hotel, centri benessere, piscine coperte.",
 "La copertura + la pompa di calore: la combinazione che estende la stagione di mesi a costi contenuti.",
 "Il riscaldamento senza copertura è buttare soldi: l'acqua calda evapora e porta via il calore.",
 "Costi: pompa di calore piscina 1.500-4.000 €; copertura automatica 3.000-8.000 €; i consumi con la copertura: ridotti del 50-70%.",
 "Piscina con pompa di calore e copertura a doghe: la stagione è passata da 4 a 7 mesi con consumi elettrici contenuti; la piscina identica del vicino senza copertura ha speso il doppio per scaldare 3 mesi.",
 "Normativa sui refrigeranti (pompe di calore); specifiche produttori.",
 "La gerarchia: prima la copertura, poi il riscaldamento: mai riscaldare senza coprire."),
s("BeniEssere sauna", "Saune e bagni di vapore: il calore terapeutico",
 "La sauna finlandese (aria secca 80-100 °C, umidità bassa) e il bagno turco (hammam: vapore 40-50 °C, umidità quasi 100%) sono gli ambienti wellness classici: si costruiscono con materiali che resistono a calore e umidità (legno resinoso per la sauna, ceramica/mosaico per l'hammam) con le barriere al vapore rigorose.",
 "La sauna: il rivestimento in legno (abet, cedro: non resinose? le conifere non resinose), la stufa con le pietre (il löyly: l'acqua gettata sulle pietre), la ventilazione (l'aria rinnovata senza perdere calore), la porta in vetro temprato; l'hammam: la struttura in muratura o compositi, il generatore di vapore, la tenuta al vapore assoluta (la barriera vapore sotto il rivestimento, le porte con i sigilli), il pavimento con la pendenza verso il scarico e le pedane antiscivolo.",
 "Hotel, SPA, centri benessere, ville di pregio.",
 "La sauna e l'hammam trasformano una casa o un hotel: il valore percepito (e commerciale) sale immediatamente.",
 "La tenuta al vapore dell'hammam è critica: i vapori che scappano dietro il rivestimento marcisco la struttura in pochi anni.",
 "Costi: sauna 5.000-15.000 €; hammam 8.000-25.000 € (finiture comprese).",
 "Hammam in hotel con la barriera vapore continua e la camera di espansione del vapore: dopo 8 anni, la struttura intatta; l'hammam gemello con la barriera 'parziale' ha rifatto il controsoffitto adiacente per muffa a 4 anni.",
 "Normativa antincendio (le saune sono locali a rischio); specifiche costruttive; igiene (le saune pubbliche hanno regole).",
 "La regola dell'hammam: il vapore è più insidioso dell'acqua: dove arriva il vapore, serve la barriera assoluta."),
s("Piscine pubbliche", "Le piscine pubbliche: normative e gestione",
 "Le piscine aperte al pubblico (hotel incluse) seguono normative igieniche regionali: la qualità dell'acqua controllata (cloro residuo 1-1,5 mg/l tipico, pH 7,2-7,6), il ricircolo obbligatorio, i bagnini, gli accessi (i pediluvi, le docce obbligatorie), la sicurezza (i fondali segnalati, i salvagenti).",
 "Requisiti: il bilancio chimico quotidiano (registrato), i controlli batteriologici periodici, i bagnini (un salvataggio? i bagnini certificati), gli accessi controllati (i percorsi obbligatori: doccia → pediluvio → vasca), i limiti di affollamento, le norme di sicurezza (i bordi vasca, i segnali di profondità); la gestione: il personale qualificato, la manutenzione programmata, la gestione dei picchi estivi.",
 "Alberghi, centri sportivi, stabilimenti balneari, piscine comunali.",
 "La piscina pubblica conforme evita sanzioni, chiusure e (soprattutto) i rischi per i bagnanti.",
 "La burocrazia sanitaria è intensa: chi sottovaluta i controlli documentali rischia la sospensione.",
 "Costi: la gestione conforme aggiunge personale e controlli (il costo della sicurezza).",
 "Stabilimento balneare con il controllo chimico digitale e i registri automatici: un'ispezione sanitaria è durata 20 minuti con esito perfetto; la struttura vicina con i registri cartacei 'a memoria' ha avuto una diffida.",
 "Normativa regionale piscine (igiene); normativa antincendio; specifiche gestionali.",
 "La cultura della piscina pubblica: l'acqua bella è il risultato di processi (controlli, personale, manutenzione) invisibili ai bagnanti."),
s("Coperture", "Le coperture della piscina: proteggere e risparmiare",
 "La copertura della piscina non è un optional: mantiene il calore (il 70% delle perdite è evaporazione), mantiene pulita l'acqua (le foglie e la polvere), aumenta la sicurezza (i bambini e gli animali), prolunga la vita dell'impianto.",
 "Tipi: la copertura estiva (a bolle, la più economica: mantiene il calore), quella invernale (telone fissato ai bordi: protegge dalla foglie), la copertura di sicurezza (a doghe che reggono il peso di un bambino: i requisiti di norma NF P90-308 come riferimento), la copertura automatica (a tapparella? a doghe scorrevoli: comodità e risparmio insieme), i pergolati e le serre intorno alla piscina (l'estensione dell'uso).",
 "Piscine private, alberghiere, pubbliche in inverno.",
 "La copertura è l'investimento con il ritorno più rapido della piscina: risparmia calore, pulizia e prodotti chimici.",
 "La copertura manuale 'pesante' non si usa: la comodità decide l'uso reale.",
 "Costi: a bolle 200-600 €, telone invernale 300-800 €, copertura di sicurezza 2.000-5.000 €, automatica 5.000-12.000 €.",
 "Piscina con copertura automatica usata quotidianamente: i consumi di riscaldamento ridotti del 60%, la pulizia dimezzata e la sicurezza garantita; la piscina identica con copertura 'manuale riposta in garage' ha consumato il doppio e richiede pulizie triple.",
 "Normative di sicurezza piscine (i requisiti anti-annegamento per le coperture); specifiche produttori.",
 "La regola: la copertura si compra con la piscina, non dopo: è parte dell'impianto."),
s("Bordo vasca", "Bordi, impianti di massaggio e accessori: la finitura conta",
 "Il bordo vasca e gli accessori completano l'opera: i bordi in pietra o gres antiscivolo, gli skimmer invisibili (a sfioro: il livello dell'acqua al bordo), gli impianti idromassaggio (le bocchette d'aria), i giochi d'acqua (cascate, getti), l'illuminazione subacquea.",
 "Elementi: il bordo a sfioro (l'acqua arriva al livello del bordo: estetica massima ma richiede il vaschetta di compenso), gli skimmer classici (più pratici, meno eleganti), i rivestimenti dei bordi (gres antiscivolo classe 3, la pietra naturale trattata), l'idromassaggio (l'aria soffiata dalle bocchette: richiede il compressore e le canaline), l'illuminazione LED subacquea (il trasformatore a norma piscina, i cavi speciali), le docce solari e i giochi d'acqua.",
 "Piscine di pregio, hotel, centri benessere.",
 "Il bordo ben fatto trasforma la piscina da 'vasca' a 'opera': l'acqua che tocca il bordo è un effetto scenico permanente.",
 "L'estetica senza funzione genera manutenzione: il bordo a sfioro richiede il controllo del livello e la pulizia della vaschetta.",
 "Costi: bordo a sfioro +30-50% sul bordo classico; l'idromassaggio: +1.000-3.000 €; l'illuminazione subacquea: 500-2.000 €.",
 "Piscina con bordo a sfioro e illuminazione LED: l'effetto scenico notturno è il punto forte dell'hotel (le recensioni lo citano); la manutenzione extra (la vaschetta) è stata organizzata in 10 minuti settimanali.",
 "Normative elettriche (CEI 64-8 per le piscine: le zone 0-1-2); specifiche produttori.",
 "La domanda di progetto: 'l'estetica richiesta quanta manutenzione in più comporta?' — la risposta va scritta nel contratto."),
]

README = """# PISCINE_E_WELLNESS_PACK — Piscine da costruzione, impianti, wellness, normative

**Facoltà:** FACOLTA_IMPIANTI_ENERGIA · **Livello:** L2 · **Schede:** {n}

## Contenuto
Il mondo dell'acqua costruita: la vasca in calcestruzzo (struttura, guaine,
rivestimenti), l'impianto di filtrazione e disinfezione (sabbia, elettrolisi,
ozono), il riscaldamento (pompe di calore, coperture, estensione di stagione),
saune e hammam (materiali, barriere al vapore), le piscine pubbliche (normative
igieniche, bagnini, controlli), le coperture (sicurezza, risparmio, tipologie) e
i bordi vasca (sfioro, idromassaggio, illuminazione, accessori).

## Formato
- `schede/schede.jsonl` — una scheda per riga, 11 campi standard.
- `COURSE.yaml` — metadati del corso.

## Uso per l'addestramento
Adatto a: consulenza su piscine private e alberghiere, dialogo con costruttori
di vasche e manutentori, wellness center, sicurezza dell'acqua. La legge fisica
che governa tutto: 1 m³ d'acqua pesa una tonnellata e l'evaporazione porta via
il calore — rispettarle e le piscine durano decenni.
""".format(n=len(DATA))

COURSE = """corso: "Piscine e centri wellness"
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
