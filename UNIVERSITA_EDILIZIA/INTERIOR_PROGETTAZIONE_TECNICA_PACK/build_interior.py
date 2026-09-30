# -*- coding: utf-8 -*-
"""Costruisce INTERIOR_PROGETTAZIONE_TECNICA_PACK: arredi su misura, ergonomia, disegno di interni, capitolato interior."""
import json, os

ROOT = os.path.dirname(os.path.abspath(__file__))

def s(cat, nome, desc, tec, app, van, lim, cos, casi, norm, note):
    return dict(categoria=cat, nome=nome, descrizione=desc, tecnologia=tec,
                applicazioni=app, vantaggi=van, limiti=lim, costi_e_economia=cos,
                casi_real_world=casi, normative=norm, note_cantiere=note)

DATA = [
s("Fondamenti", "Il progetto di interni come disciplina tecnica",
 "Il progetto di interni è ingegnerizzazione dello spazio abitato: distribuzione, ergonomia, materiali, impianti integrati, luce, acustica, con documentazione esecutiva che i falegnami e gli installatori eseguono senza interpretazioni; non è 'arredamento' ma progetto completo di micro-architettura.",
 "Flusso: analisi esigenze → concept (moodboard) → planimetria arredi in scala → disegni esecutivi dei particolari su misura (mobili, boiserie, controsoffitti) → schedule materiali e arredi → direzione dei lavori di allestimento; il tutto coordinato con architettura e impianti.",
 "Residenze private, appartamenti per locazione, hospitality (camere, lobby), uffici, retail.",
 "Il cliente compra un risultato coordinato, non una somma di mobili: il valore professionale sta nell'eliminazione delle frizioni (porte che non aprono, prese coperte, luce sbagliata).",
 "L'interior 'solo bello' senza disegni esecutivi produce cantieri infiniti e mobili che non entrano: la componente tecnica non è optional.",
 "Onorario progetto interni completo: 8-15% del valore dei lavori di allestimento, o quotazione a metro quadro (50-150 €/m² per la sola progettazione).",
 "Appartamento di 110 m²: progetto completo con disegni esecutivi dei 14 mobili su misura e schedule integrato ha portato l'allestimento a 6 settimane con zero voci 'a completamento'.",
 "Nessuna norma specifica sul progetto di interni; valgono le norme dei materiali (fuoco, sicurezza) e degli impianti.",
 "Principio: ogni mobile su misura deve avere il proprio disegno quotato (piante, prospetti, sezioni) prima della produzione — il 'sì sì ce l'ho in testa' del falegname è il preludio del disastro."),
s("Ergonomia", "Ergonomia degli ambienti domestici: le misure che contano",
 "Le dimensioni ergonomiche sono il lessico minimo del progettista di interni: altezze di lavoro, spazi di manovra, profondità di uso; si basano su antropometria (popolazione europea: statura media uomo ~176 cm, donna ~164 cm, variazione anziani ridotta).",
 "Misure cardine: piano cucina 85-95 cm (x persona 160-190 cm); piano lavabo bagno 80-85 cm (85-90 cm per lavabo soprapiano); wc seduta 40-45 cm; doccia minima 80×80 (90×90 comfort); spazio frontale elettrodomestici 90-120 cm; spazio di lavoro davanti a un armadio a ante: 80 cm minimo, 100 cm comfort; corridoio abitativo ≥ 90 cm di luce libera; tavolo pranzo 4 persone 80×160 con 60 cm perimetro sgombro.",
 "Verifica planimetrie arredi, adattamento per anziani e disabili, progettazione cucine e bagni.",
 "Le misure giuste sono invisibili: nessuno le nota, ma tutti notano quando sono sbagliate (schiena, spalle, sportelli che non si aprono).",
 "L'ergonomia media non vale per tutti: un cliente di 150 o 200 cm richiede la personalizzazione; l'adattamento disabili segue norme precise (DM 236/89, UNI 9182).",
 "Costo aggiuntivo nullo: è progetto; il valore è nella qualità d'uso quotidiana.",
 "Cucina progettata a 92 cm di piano per un utente di 190 cm: l'utente ha dichiarato di non aver mai avuto una cucina 'così naturale' — la misura giusta vale più di ogni accessorio.",
 "UNI EN ISO 9241 (ergonomia interazione uomo-sistema); DM 236/1989 e UNI 9182 (barriere architettoniche).",
 "Da memorizzare per il LLM: la tabella delle 15 misure cardine dell'abitazione — è il 20% del sapere che risolve l'80% delle verifiche."),
s("Cucina", "La progettazione tecnica della cucina",
 "La cucina è il laboratorio domestico più tecnico: layout (lineare, ad L, a U, con isola/penisola), triangolo di lavoro (lavello-forno-frigo), superfici resistenti a calore e taglio, elettrodomestici integrati con le proprie esigenze (altezze, sfiati, prese), luce di lavoro vera.",
 "Regola del triangolo: i 3 vertici entro 6 m complessivi e senza passaggi di traffico attraverso; moduli base 60 cm di profondità standard; colonne frigo/forno 60×60 o 60×240; isola: minimo 90 cm di perimetro libero, 120 se due persone cucinano; prese: una ogni 50 cm di piano, niente sotto il lavello a meno di esigenze specifiche (lavastoviglie); cappa con portata adeguata (cucina aperta: 700+ m³/h) e sfiato verso l'esterno quando possibile.",
 "Cucine residenziali, open space, piccola ristorazione, show-cooking.",
 "La cucina giusta cambia la vita quotidiana: il 60% del tempo attivo in casa si passa qui (stime di settore), merita la massima cura progettuale.",
 "La moda dell'isola impone spazi che non tutti hanno: forzare un'isola in 12 m² uccide la funzionalità; la penisola spesso è la scelta corretta.",
 "Cucina completa media: 8.000-25.000 € chiavi in mano (mobili + elettrodomestici + top); su misura alta: 30.000-80.000 €+.",
 "Cucina aperta sul soggiorno con cappa sottodimensionata (estetica voluta): dopo un mese, odori permanenti sul divano; correzione con cappa a ricircolo potenziata e captazione perimetrale ha risolto senza demolire.",
 "CEI 64-8 (impianto elettrico); UNI 7129 (impianti gas domestici); linee guida produttori cucina (moduli standard).",
 "Domande tecniche prima di disegnare: quanti cucinano? quanto spazio perimetro? fuochi a gas o induzione? il forno a che altezza? la spesa dove si scompatta?"),
s("Bagno", "La progettazione tecnica del bagno",
 "Il bagno è l'ambiente con la maggior densità di vincoli: scarichi, altezze, umidità, sicurezza elettrica, comfort termico; progettarlo bene significa risolvere ingombri e manutenzioni PRIORA di chiudere le pareti.",
 "Stack scarichi: convogliare wc, lavabo, doccia sulla stessa colonna verticale; wc con scarico a parete (cassetta incasso) libera il pavimento e semplifica pulizia; portata estrazione: minimo 10-15 volumi/ora (aspiratore canalizzato o finestra); sicurezza: zone 0-1-2 con gradi IP e differenziali dedicati (30 mA); riscaldamento: scalda-salviette dimensionato 400-600 W; il piano doccia a filo pavimento richiede pavimento con pendenza o canaletta e impermeabilizzazione continua (sistema a tenuta certificata).",
 "Bagni residenziali, bagni pubblici (bar, uffici), hospitality, adattamento anziani (doccia walk-in, seduta, maniglioni).",
 "Il bagno ben fatto è l'ambiente che più influenza la percezione di qualità dell'intera abitazione (e il prezzo di vendita/locazione).",
 "Le superfici 'bellissime ma scivolose' e i mobili 'belli ma che non si aprono per lo scaldasalviette' sono errori da catalogo: la simulazione 3D di apertura sportelli e percorsi umidi è obbligatoria.",
 "Bagno completo rifatto: 6.000-18.000 €; bagno di pregio con sanitari design e sistema doccia evoluto: 20.000-50.000 €+.",
 "Bagno con doccia a filo pavimento e canaletta lineare: la pendenza eseguita male (1 cm invece di 1,5-2 cm/m) lasciava 2 cm d'acqua stagnante; risolto con micro-piastrellatura correttiva — costo 4 volte la posa giusta.",
 "CEI 64-8 (zone elettriche bagno); UNI EN 14428 (box doccia); UNI EN 997 (wc); linee guida CNPI impianti idrici.",
 "Checklist: scarichi impilati? aspirazione dimensionata? IP corretti per zona? sportelli apribili? pendenza doccia verificata in cantiere PRIORA del rivestimento?"),
s("Armadi e cabine", "Armadi a muro, cabine armadio e sistemi di contenimento",
 "Il contenimento su misura è il grande assente dalle planimetrie e la prima lamentela d'uso: armadi a muro (anta o patta), cabine armaggio (minimo 90×120 cm, meglio 120×160), guardaroba con configurazioni interne (doppie appendi, cassettiere, vani alto).",
 "Profondità minima armadio: 60 cm per appendere (55 cm stretto); altezza moduli: 240-260 cm standard, sfruttare fino a soffitto con vani alto (60 cm) per cambio stagione; cabina armadio: passaggio minimo 80 cm tra file frontali; illuminazione interna LED con sensore di apertura; ante scorrevoli risparmiano spazio ma bloccano metà luce frontale: preferire a battente quando lo spazio lo consente.",
 "Residenze, camere hotel, ingressi (armadio-scarpiera), spazi lavanderia.",
 "Un metro quadro di cabina ben fatta vale 3 m² di armadio a parete per capienza e fruibilità: ottimizza la superficie vendibile/locabile.",
 "Le cabine 'di moda' rubano metratura alla camera: il rapporto giusto è progettuale, non da catalogo.",
 "Armadio su misura: 400-900 €/m lineare (ante + interno base); cabina armadio completa: 1.500-4.000 € a seconda di finiture e sistema.",
 "Camera con cabina armadio troppo grande (richiesta del cliente 'da rivista'): la camera residua era 10 m² con il letto che stentava; ridisegnata la cabina (-40 cm) la camera è tornata abitabile e il cliente ha ringraziato.",
 "Nessuna norma specifica; ergonomia di riferimento UNI; sistemi dei produttori (rimadesio, Poliform, Lema come riferimenti di fascia).",
 "Domanda da porsi sempre: 'quanti metri lineari di appendiabiti servono DAVVERO a questa famiglia?' — la risposta si ottiene facendo l'inventario dei vestiti, non dalla foto."),
s("Illuminazione interni", "La luce negli interni: progetto per strati",
 "L'illuminazione di qualità si progetta a strati indipendenti: generale (soffitti), d'accento (oggetti, quadri), funzionale (cucina, lettura, specchi), atmosfera (indiretta, LED integrati); ogni strato ha il suo circuito e il suo comando (interruttori scenari o domotica).",
 "Parametri: temperatura colore (K), CRI (>90 dove si giudicano colori e volti: cucina, bagno, guardaroba), flusso (lumen) per ambiente (soggiorno ~300 lux piano lavoro, cucina 300-500 sul piano), angoli di fascio per l'accento (24°-36° per quadri), dimmerabilità dei circuiti d'atmosfera.",
 "Tutti gli ambienti interni, in particolare cucine, bagni, home office, zona notte.",
 "I 4 strati comandati separatamente trasformano lo stesso ambiente da lavoro a relax: flessibilità percettiva a costo quasi nullo se prevista in progetto.",
 "La luce a soffitto unica 'a plafone' è il difetto più comune: tutto illuminato e nulla valorizzato; le retrofite costano più del previsto (cavidotti, nuovi circuiti).",
 "Punto luce nuovo: 60-150 € installato (in muratura); sistema binario d'accento: 80-200 €/m; scenari domotici: vedi DOMOTICA_PACK.",
 "Soggiorno 'a plafone' riconvertito con binario a parete e LED indiretto dietro boiserie: tre scene (lettura, ricevimento, cinema) con lo stesso impianto potenziato in 2 giorni.",
 "UNI EN 12464-1 (lux di riferimento); CEI 64-8; marcatura CE e regolamento Ecodesign delle sorgenti.",
 "Regole per il LLM: mai una sola sorgente per ambiente; CRI alto dove il colore conta; dimmerare tutto ciò che è d'atmosfera."),
s("Materiali interni", "I materiali per interni: resilienza, manutenzione, pregio",
 "Ogni materiale interno ha un profilo d'uso: resistenza all'usura, alla macchia, all'umidità, alla luce (ingiallimento), alla fiamma, e un profilo manutentivo (riparabile? sostituibile?); scegliere significa abbinare il profilo all'uso reale, non alla foto.",
 "Matrice d'uso: pavimenti zona giorno (gres porcellanato grande formato: indistruttibile, freddo; legno: caldo, sensibile ad acqua e graffi; resina: seamless, riparabile ma giunta fragile; LVT: economico, resistente, meno nobil); pareti (pittura lavabile vs cartongesso vs boiserie); bagni (gres tutta altezza vs resina vs smalto); piani cucina (quarzo: durevole, non si lucida; laminato: economico, sensibile al caldo; acciaio: igienico, graffiabile; marmo: nobile, macchiabile da acidi).",
 "Scelta finiture per nuovi progetti, ripristini, consulenza 'dove investire'.",
 "La giusta abbinata materiale-uso elimina il 90% dei difetti di fine lavori e delle lamentele post-consegna.",
 "Ogni materiale ha il suo difetto: nasconderlo al cliente è disonesto professionale; dosarlo (marmo sul piano snack, quarzo sul piano lavoro) è design.",
 "Delta di costo tra materiali: laminato 30-60 €/ml; quarzo 250-600 €/ml; marmo 300-900 €/ml; gres 20-80 €/m²; LVT 15-40 €/m²; parquet 40-150 €/m².",
 "Piano cucina in marmo 'tutto uguale': dopo 3 mesi, macchie d'olio permanenti sul piano cottura; correzione con piano snack in quarzo e ripristino marmo sul resto — il cliente avrebbe scelto diversamente se avesse saputo.",
 "Riferimento UNI EN 685 (classi di usura pavimenti), reazioni al fuoco (DM/UNI 9177), dichiarazioni CE dei prodotti.",
 "Tabella da insegnare: materiale → pregio → difetto → uso ideale → fascia prezzo. È il cuore di questa scheda."),
s("Controsoffitti", "Controsoffitti e sistemi a secco per interni",
 "I controsoffitti in cartongesso o pannelli minerali risolvono: abbassamenti, integrazione impianti (clima, elettrico, acustica), creazione di geometrie luminose; i sistemi a secco (pareti, controsoffitti) sono la norma nella ristrutturazione per rapidità e pulizia.",
 "Struttura: montanti e profili in acciaio zincato, lastre in gesso rivestito (standard, idrofuga per umidi, antincendio, acustica), lana minerale per l'isolamento/acustica interposta; sospensioni ogni 40-60 cm; il cantiere corretto prevede botole di ispezione su ogni valvola/contatore nascosto; luce LED integrata in profili appositi con dissipazione corretta.",
 "Ristrutturazioni complete, uffici, retail, correzione acustica, integrazione VMC e clima.",
 "Il controsoffitto è il 'piano di lavoro' dei servizi: tutto passa lì e tutto resta ispezionabile se progettato con botole giuste.",
 "Un controsoffitto senza botole sui punti di manutenzione è una bomba a orologeria (intervento = demolizione); la rigidità del cartongesso maschera crepe strutturali se usato per 'coprire' invece che per 'risolvere'.",
 "Controsoffitto in cartongesso: 45-90 €/m² posato; con lana acustica e luce integrata: 90-160 €/m²; pannelli minerali ufficio: 25-50 €/m².",
 "Ufficio con controsoffitto continuo 'pulito' senza botole: il guasto ad una valvola di zona ha richiesto l'apertura di 4 m² di controsoffitto e 2 settimane di disagi; il progetto corretto (botole ogni 2 m sui servizi) costava 300 € in più.",
 "UNI EN 520 (lastre di gesso); ETAG/ETA sistemi; CEI per l'integrazione impianti.",
 "Regola ferrea: nessun componente di manutenzione dietro superfici chiuse senza botola ispezionabile."),
s("Arredi su misura", "Il disegno esecutivo dei mobili su misura",
 "Il mobile su misura è micro-architettura: il disegno esecutivo (pianta, prospetti, sezioni, quotatura completa, specifica materiali e ferramenta) è il contratto tra progettista e falegname; senza di esso ogni mobile è una sorpresa.",
 "Contenuto minimo di ogni scheda mobile: quote esterne e interne per vano, spessori dei pannelli, aperture sportelli (verso, battuta, ammortizzatori), ferramenta specificata (cerniere, guide cassetti con portata), finiture (laccato, impiallacciato, laminato con codice), tolleranze di posa (5-10 mm dai muri non a squadra), impianti integrati (prese, LED, passacavi).",
 "Cucine, armadi, librerie, boiserie, scrivanie, arredi contract (hotel, negozi).",
 "Il disegno completo trasforma la litigiosità in produzione: chi produce ha tutto, chi verifica ha un riferimento oggettivo.",
 "Le varianti 'al volo' in corso di produzione (cambi colore, misure) sono costosissime se il disegno era vago: il disegno preciso protegge ENTRAMBE le parti.",
 "Progettazione mobile su misura: 150-400 € ad arredo nel contesto di un progetto completo; mobili su misura produzione: 700-1.500 €/m lineare cucina, armadi 400-900 €/m lineare.",
 "Libreria su misura: il disegno specificava 'fondo 2 cm fisso, scaffali 4 cm con luce LED integrata'; il falegname aveva proposto 'tutto standard'; il risultato eseguito col disegno è durato 8 anni senza un'appartenenza storta.",
 "Nessuna norma sul disegno del mobile; UNI EN 16122/16121 (mobili domestici: requisiti di sicurezza e resistenza).",
 "Frase da inculcare al LLM: 'se il disegno non dice spessore, apertura e finitura, il mobile NON È PROGETTATO'."),
s("Capitolato interior", "Il capitolato di interior: documento contrattuale",
 "Il capitolato (o schedule of finishes) dell'interior elenca per ogni ambiente: materiali, prodotti con marca/modello o equivalente, colori con codice, modalità di posa, standard di qualità, esclusioni; è la difesa di entrambe le parti e la base della contabilità.",
 "Struttura per ambiente: pavimenti (prodotto, formato, posa, battiscopa), pareti (finitura, altezza), soffitto, illuminazione (corpi modello o scheda tecnica), arredi (scheda per ogni pezzo: misure, materiale, fornitore, prezzo), impianti speciali (domotica, audio); allegati: campioni approvati firmati, moodboard approvata, disegni esecutivi numerati; clausole: 'a campionario approvato', equivalentza autorizzata solo per iscritto prima dell'acquisto.",
 "Commesse private, contract hospitality/retail, gare di allestimento.",
 "Il capitolato chiaro previene il 90% dei contenziosi: 'è quello scritto' batte sempre 'l'avevamo detto a voce'.",
 "Redigerlo richiede tempo e precisione: il capitolato vago ('pavimento in gres di pregio') è un invito alla quotazione più bassa e alla delusione finale.",
 "Tempo di redazione: 2-5 giorni per una commessa media; struttura il prezzo della progettazione (non è un favore, è il lavoro).",
 "Allestimento negozio: contestazione su 'rivestimento bancone in Corian'; il capitolato nominava il prodotto e lo spessore: l'impresa aveva quotato un solido surface economico; la clausola ha risolto la sostituzione a carico dell'impresa in 48 ore.",
 "Nessuna norma specifica; prassi contrattuale e deontologia professionale (CNPI/CNPIA).",
 "Per il LLM: saper BOZZARE un capitolato interior è tra le competenze più richieste e meno diffuse — la scheda di ogni ambiente deve poter essere generata da una checklist."),
s("Tendenze interior", "Interior design: tendenze e innovazione 2024-2026",
 "Il quadro dell'innovazione negli interni: materiali bio-based e riciclati a parete (feltro, sughero, canapa, terrazzo veneziano ricomposto), superfici tattili (stucco, calce, marmorino), il ritorno del legno caldo e dei colori terra, il bagno-spa domestico (docce emozionali, materiali caldi anche in bagno), la cucina nascosta (trend 'invisible kitchen'), home office integrato e flessibile, arredi modulari e trasformabili, domotica e LED integrati invisibili.",
 "Fonti: Salone del Mobile e Fuorisalone Milano, Cersaie, report di colore (Pantone, WGSN per i professionisti), cataloghi dei produttori di arredo e materiali; traduzione operativa: per ogni tendenza valutare disponibilità, manutenzione e longevità (la doccia emozionale richiede manutenzione; la cucina nascosta costa di più e riduce la funzionalità).",
 "Aggiornamento offerte, consulenza clienti, ripensamento di arredi per vendita/locazione.",
 "Chi presenta soluzioni aggiornate vince le commesse: il cliente 'legge' il progettista dalla capacità di mostrare ciò che non sapeva di volere.",
 "Ogni innovazione ha un costo nascosto di manutenzione o usabilità: la doccia emozionale in un bagno di 4 m² privo di spazio tecnico è un guasto futuro, non un lusso.",
 "Materiali innovativi: +20-80% sui tradizionali; arredi trasformabili di qualità: 1,5-3 volte il fisso standard.",
 "Showroom aggiornato con campioni tattili (feltro, sughero, terrazzo) e una 'cucina nascosta' funzionante: la permanenza media dei clienti è raddoppiata e il tasso di conversione a preventivo è salito in modo marcato (misurato su 6 mesi).",
 "Nessuna norma cogente (le finiture rispettano le norme dei singoli materiali: fuoco, emissioni, UNI).",
 "Criterio critico per il LLM: proporre l'innovazione con la sua SCHEDA TECNICA d'uso — dove funziona, cosa costa, cosa richiede, quando evitarla."),
]

README = """# INTERIOR_PROGETTAZIONE_TECNICA_PACK — Progettazione tecnica degli interni

**Facoltà:** FACOLTA_ARCHITETTURA_DESIGN · **Livello:** L2 (intermedio, tecnico-operativo) · **Schede:** {n}

## Contenuto
La disciplina tecnica del progetto di interni: fondamenti e flusso di lavoro,
ergonomia domestica con le misure cardine, progettazione tecnica di cucina e bagno,
armadi e cabine armadio, illuminazione a strati, materiali per interni con la matrice
pregio/difetto/uso/prezzo, controsoffitti e sistemi a secco, disegno esecutivo dei mobili
su misura, capitolato di interior come documento contrattuale, tendenze e innovazione 2024-2026.

## Formato
- `schede/schede.jsonl` — una scheda per riga, 11 campi: categoria, nome, descrizione,
  tecnologia, applicazioni, vantaggi, limiti, costi_e_economia, casi_real_world, normative, note_cantiere.
- `COURSE.yaml` — metadati del corso.

## Uso per l'addestramento
Adatto a: progettazione di interni tecnica, dialogo con falegnami e posatori, stesura di
capitolati e schedule, verifica ergonomica delle planimetrie, consulenza materiali.
Le misure ergonomiche sono valori di riferimento per la popolazione europea media:
personalizzare sempre sul cliente reale e sulle norme di accessibilità (DM 236/89).
""".format(n=len(DATA))

COURSE = """corso: "Progettazione tecnica degli interni"
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
