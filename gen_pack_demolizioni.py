# -*- coding: utf-8 -*-
"""Giro AM (2026-11-01): genera DEMOLIZIONI_FINE_VITA_PACK (12 schede).
Tema: demolizioni tecniche e fine vita degli edifici — indagini, piano (art. 151
D.Lgs 81/2008), tecniche esecutive, metodi speciali, decostruzione operativa,
rifiuti CER 17, frantumazione in sito, impatti (polveri/rumore/vibrazioni),
contesto urbano, economia. NON ridondante con EDILIZIA_CIRCOLARE_LCA_PACK
(LCA/passaporti) e BONIFICA_SITI_AMBIENTALI_EDILIZIA_PACK (contaminazione)."""
import json, os

BASE = os.path.join('UNIVERSITA_EDILIZIA', 'DEMOLIZIONI_FINE_VITA_PACK')
KEYS = ["categoria","nome","descrizione","tecnologia","applicazioni","vantaggi","limiti","costi_e_economia","casi_real_world","normative","note_cantiere"]

S = []

S.append({
 "categoria": "Demolizioni — indagini e pianificazione",
 "nome": "Le indagini conoscitive pre-demolizione: rilievo, materiali, servizi e vincoli",
 "descrizione": "La fase zero di ogni demolizione: capire COSA si demolisce prima di decidere COME. Comprende il rilievo geometrico e strutturale, l'identificazione dei materiali e delle sostanze pericolose, la mappatura dei servizi attivi e dei distacchi, la ricerca documentale e lo stato dei luoghi condiviso con i terzi. E' il presupposto tecnico dell'obbligo di verifica di stabilita' dell'art. 150 del D.Lgs 81/2008.",
 "tecnologia": "Rilievo metrico tradizionale o laser scanner con nuvola di punti; prove pacometriche e carotaggi su elementi strutturali incerti; ricerca archivistica (Genio Civile, concessioni storiche, catasto); censimento amianto e materiali pericolosi con campionamenti; indagine su serbatoi, cisterne e vani interrati; mappa dei distacchi utility (energia, gas, acqua, fognature, telefonia) con verbali dei gestori; fotodocumentazione datata dello stato dei luoghi e dei dissesti degli edifici adiacenti.",
 "applicazioni": "Obbligatoria di fatto prima di qualsiasi demolizione, parziale o totale; critica in edifici industriali dismessi (serbatoi, sostanze chimiche), in edilizia storica (strutture miste non documentate) e in contesti urbani con adiacenze sensibili.",
 "vantaggi": "Elimina la gran parte degli imprevisti di cantiere (amianto nascosto, servizi attivi, strutture diverse dai disegni); rende affidabili il piano di demolizione, il computo e il bilancio di massa dei rifiuti; documenta lo stato pre-opera a tutela da contestazioni dei terzi.",
 "limiti": "Su edifici privi di documentazione e con vani non accessibili una quota di incertezza resta sempre: va gestita con margine nel piano, non ignorata; i campionamenti sono puntuali e possono non intercettare sacche localizzate di materiale pericoloso.",
 "costi_e_economia": "Ordini di grandezza indicativi: rilievo e indagine conoscitiva su edificio ordinario di 500-3.000 m2: 1.500-8.000 euro; complessi industriali con indagini strutturali e ambientali estese: 10.000-40.000 euro; analisi di laboratorio per amianto: 80-200 euro a campione. Pesa tipicamente l'1-3% del valore della demolizione e ne evita sopravvenienze del 20-50%.",
 "casi_real_world": "Caso tipo: condominio anni '60 da demolire per ricostruzione; il rilievo con pacometro sui solai rivela travetti latero-cemento con orditura diversa dai disegni di archivio: la sequenza di demolizione prevista a macchina dal solaio viene riscritta con lavorazione da terra, evitando il rischio di crollo intempestivo.",
 "normative": "D.Lgs 81/2008, art. 150 (verifica delle condizioni di conservazione e stabilita' prima dell'inizio dei lavori) e Titolo IX per l'amianto; L. 257/1992 (amianto); D.P.R. 380/2001 (titolo abilitativo dell'intervento); NTC D.M. 17/1/2018 per la valutazione di stabilita' nelle fasi transitorie.",
 "note_cantiere": "Pretendi sempre la mappa firmata dei distacchi utility PRIMA di far entrare le macchine: una condotta gas 'dimenticata' attiva sotto il piazzale e' l'incidente piu' banale e piu' grave delle demolizioni. Fotografa i dissesti dei vicini con data certa: ti serviranno."
})

S.append({
 "categoria": "Demolizioni — indagini e pianificazione",
 "nome": "Il piano di demolizione allegato al POS: sequenze, puntellamenti e zone di ricaduta",
 "descrizione": "Documento tecnico-operativo obbligatorio che descrive come la struttura viene 'smontata' in sicurezza: analisi del manufatto, scelta delle tecniche, successione ordinata delle lavorazioni, opere di rafforzamento e puntellamento, attrezzature impiegate, zone di esclusione e di ricaduta. L'art. 151 del D.Lgs 81/2008 ne prescrive il contenuto nel POS, in coerenza con il PSC quando presente.",
 "tecnologia": "Analisi stratigrafica dell'edificio (abaco degli elementi portanti e non); piano dei tagli e delle sezioni; sequenza top-down o per blocchi con diagrammi di fase; calcolo dei puntellamenti e dei contrafforti provvisionali; schema di posizionamento e rotazione dei mezzi con raggi di lavoro e zone vietate; cronoprogramma; piano di convogliamento dei materiali (canali ex art. 153); previsione delle fasi a rischio aggravato (elementi precompressi, serbatoi, adiacenze).",
 "applicazioni": "Ogni cantiere di demolizione con lavoratori (il POS e' sempre dovuto per l'impresa esecutrice); coordinamento con il PSC del committente in presenza di piu' imprese; base per autorizzazioni, comunicazioni preliminari e verifiche degli organi di vigilanza.",
 "vantaggi": "Trasforma la demolizione da attivita' improvvisata a processo controllato: riduce crolli intempestivi, ottimizza i tempi dei mezzi, e' prova documentale di diligenza per DL, CSE e organi di vigilanza; allinea squadra, mezzi e contabilita' sulle stesse fasi.",
 "limiti": "Un piano generico 'copia-incolla' non risponde all'art. 151 e non protegge nessuno: va calato sul manufatto reale; ogni deviazione in corso d'opera (struttura diversa dal previsto) impone aggiornamento formale del documento, con tempi e costi di revisione.",
 "costi_e_economia": "Ordini di grandezza indicativi: redazione del piano su edificio semplice: 1.000-5.000 euro; strutture complesse o industriali con supporto di calcolo strutturale: 5.000-20.000 euro. In gara il costo del piano e' irrisorio rispetto al rischio: la sua assenza o genericita' e' tra le prime cause di sospensione dei lavori.",
 "casi_real_world": "Caso tipo: capannone industriale con copertura in elementi precompressi; il primo piano di demolizione non considerava l'instabilita' degli elementi dopo il distacco dei vincoli: il piano viene integrato con imbragatura preventiva degli elementi e discesa controllata a gru prima della demolizione delle strutture verticali.",
 "normative": "D.Lgs 81/2008: art. 150 (rafforzamento delle strutture), art. 151 (ordine delle demolizioni e programma nel POS), art. 89 comma 1 lett. h) (contenuto del POS), Sezione VIII artt. 150-156 nel complesso; Titolo IV Capo I per PSC e figure di coordinamento.",
 "note_cantiere": "Appendi in baracca le tavole di sequenza in formato grande e segnaci ogni giorno dove siete arrivati: la squadra che VEDE la fase successiva non improvvisa. E se la struttura risponde diversamente dal piano, fermati e aggiorna il piano: l'improvvisazione in demolizione si paga in croci."
})

S.append({
 "categoria": "Demolizioni — tecniche esecutive",
 "nome": "Demolizione meccanica con mezzi pesanti: pinze, martelli demolitori e high-reach",
 "descrizione": "La tecnica piu' diffusa per l'abbattimento di edifici: macchine operatrici equipaggiate con attrezzature idrauliche di frantumazione e taglio che aggrediscono la struttura dall'alto verso il basso, su letto di materiale di risulta che attutisce le cadute. Per gli edifici alti si usano bracci high-reach dedicati.",
 "tecnologia": "Escavatori da 15-80 t con pinze frantumatrici e polverizzatori (pezzatura gestita in boccate da 300-800 kg), martelli demolitori per fondazioni e conglomerati tenaci, benne di rincalzo; bracci high-reach con sbraccio corrente 20-45 m (macchine speciali oltre 60 m); letto di macerie come cuscino di caduta; irrorazione continua per l'abbattimento polveri; cesoie idrauliche per carpenteria metallica.",
 "applicazioni": "Edifici isolati o con spazi di ricaduta disponibili, capannoni, opere in c.a. ordinario, demolizioni complete di edifici fino a 8-10 piani con high-reach; meno adatta ad adiacenze sensibili, strutture in muratura portante degradata con vincoli, interni.",
 "vantaggi": "Produttivita' elevata (50-300 m3/giorno per macchina su edifici ordinari), parco mezzi diffuso e noleggiabile, personale standard, buona compatibilita' con la selezione grossolana dei materiali direttamente in cantiere.",
 "limiti": "Vibrazioni e rumore elevati (limita l'uso vicino a edifici sensibili); polveri senza irrorazione efficace; rischio di proiezioni; il peso del braccio high-reach impone verifica della portata dei piazzali e dei solai su cui la macchina staziona; non praticabile con il pubblico a ridosso senza schermi.",
 "costi_e_economia": "Ordini di grandezza indicativi: demolizione meccanica completa di edificio ordinario 15-45 euro/m3 lordo (mezzi e manodopera, smaltimento escluso); noleggio escavatore con pinza 350-700 euro/giorno; operatore specializzato 40-60 euro/h; macchina high-reach 1.000-2.500 euro/giorno. Su volumi oltre 10.000 m3 il prezzo unitario scende sensibilmente.",
 "casi_real_world": "Caso tipo: ex stabilimento produttivo di 12.000 m3 in area periferica: due macchine (una con pinza, una con martello sulle fondazioni) completano l'abbattimento in 6 settimane lavorando su letto di risulta, con selezione in sito di ferro e conglomerato.",
 "normative": "D.Lgs 81/2008: Sezione VIII artt. 150-156 (in particolare art. 154 sbarramento della zona e art. 155 rovesciamento, ammesso solo entro 5 m di altezza e con le cautele indicate), Titolo III attrezzature di lavoro; Direttiva Macchine 2006/42/CE (marcatura CE di macchine e attrezzature); NTC D.M. 17/1/2018 per gli effetti dinamici su manufatti adiacenti.",
 "note_cantiere": "Non far mai lavorare la pinza sopra la verticale della cabina e mantieni il letto di macerie davanti alla macchina: e' il tuo cuscino e il tuo spartitraffico. Con il vento forte sospendi la frantumazione in alto: le proiezioni leggere arrivano oltre lo sbarramento."
})

S.append({
 "categoria": "Demolizioni — tecniche esecutive",
 "nome": "Taglio controllato: filo diamantato, seghe a disco e carotaggi per il dissezionamento",
 "descrizione": "Famiglia di tecniche 'chirurgiche' che separano la struttura in conci di peso controllato invece di frantumarla: permettono demolizioni precise, quasi prive di vibrazioni, anche su spessori elevati e in strutture armate.",
 "tecnologia": "Filo diamantato a perline (tagli di qualsiasi spessore e geometria, velocita' tipiche 1-4 m2/h su c.a. armato); seghe murali a disco (diametri 600-1.600 mm) e tagliasolai; carotaggi diamantati da 20 a 500 mm per trafilature, alleggerimenti e giunti di taglio; raffreddamento ad acqua (10-20 l/min) con raccolta dei fanghi di taglio; sezionamento in conci imbragati e verificati in peso prima del sollevamento.",
 "applicazioni": "Dissezionamento di ponti e viadotti, aperture e demolizioni parziali in edifici esistenti, interventi in ospedali e siti sensibili al rumore/vibrazioni, taglio di fondazioni e testate di pali, rimozione di elementi precompressi da recuperare.",
 "vantaggi": "Precisione millimetrica e vibrazioni trascurabili (adatto a strutture adiacenti sensibili); gestisce qualsiasi spessore; produce conci regolari facilmente movimentabili e valorizzabili; bassa rumorosita' rispetto al martello demolitore.",
 "limiti": "Costo unitario alto rispetto alla meccanica; gestione obbligatoria di acque e fanghi di taglio (rifiuto da trattare); necessita di punti di ancoraggio e di verifica statica dei conci (un concio piu' pesante del previsto e' un rischio grave in sollevamento); produttivita' bassa su grandi volumi.",
 "costi_e_economia": "Ordini di grandezza indicativi: taglio a filo diamantato 80-250 euro/m2 di sezione tagliata (crescente con spessore e densita' di armatura); taglio a disco 60-150 euro/m2; carotaggi 20-80 euro/m lineare a seconda del diametro; squadra di taglio completa 600-1.200 euro/giorno.",
 "casi_real_world": "Caso tipo: rimozione di una campata di viadotto su strada aperta: taglio a filo in conci da 25 t durante finestre notturne, conci imbragati e calati a gru su piazzale attrezzato, riapertura al traffico al mattino; fanghi raccolti in vasca e smaltiti come rifiuto speciale.",
 "normative": "D.Lgs 81/2008 Sezione VIII (demolizioni) e Titolo III (attrezzature); Direttiva Macchine 2006/42/CE; D.Lgs 152/2006 per la gestione di fanghi e acque di processo; D.Lgs 81/2008 Titolo VI per la movimentazione dei conci (apparecchi di sollevamento).",
 "note_cantiere": "Pesa (o calcola con densita' verificata sul posto) OGNI concio prima dell'ultimo passaggio di filo e imbraga pensando al baricentro reale, non a quello geometrico: il concio che ruota in sollevamento e' l'incidente classico del sezionamento."
})

S.append({
 "categoria": "Demolizioni — metodi speciali",
 "nome": "La demolizione con esplosivo: implosioni controllate di torri, camini e grandi volumi",
 "descrizione": "Tecnica specialistica che abbatte la struttura in pochi secondi innescando il crollo per gravita' mediante cariche esplosive poste sugli elementi portanti critici, con direzionalita' di caduta progettata. Riservata a manufatti alti e isolati o a grandi volumi dove la meccanica sarebbe lunga e costosa.",
 "tecnologia": "Progetto della direzionalita' (cedimento pilotato con cerniere plastificate); preindebolimento con tagli e asportazioni preliminari; cariche sugli elementi critici (cariche specifiche di letteratura 0,5-2 kg/m3 sulle zone di cerniera) con detonatori a ritardo millimetrico per controllare la sequenza; letto di caduta in sabbia o macerie selezionate; schermi anti-proiezione (geotessili, stuoie); monitoraggio vibrazionale e delle polveri; doppia ispezione finale dell'edificio prima dell'innesco.",
 "applicazioni": "Camini e torri di raffreddamento, silos, serbatoi sopraelevati, edifici alti in aree con spazio di ricaduta disponibile, grandi strutture industriali dismesse lontane da recettori sensibili.",
 "vantaggi": "Rapidita' assoluta (l'abbattimento dura secondi, contro settimane o mesi); costo unitario su grandi volumi inferiore alla meccanica; elimina l'esposizione prolungata dei lavoratori alla struttura in degrado.",
 "limiti": "Iter autorizzativo complesso (pubblica sicurezza, enti locali); vibrazioni e onda d'urto aerea da monitorare; nube di polveri istantanea; impatto mediatico e sul vicinato; nessuna possibilita' di correzione dopo l'innesco: l'errore di progetto e' irreversibile; esclusa in presenza di adiacenze sensibili o spazi di ricaduta insufficienti.",
 "costi_e_economia": "Ordini di grandezza indicativi: su grandi volumi 5-15 euro/m3 di struttura abbattuta, ma con spese fisse di 40.000-150.000 euro per progetto, autorizzazioni, misure di pubblica sicurezza, monitoraggi e ripristini; camini e torri: 30.000-120.000 euro a intervento secondo altezza e contesto.",
 "casi_real_world": "Caso tipo: camino in muratura da 60 m in area industriale dismessa: caduta pilotata su letto di sabbia preparato nel cono di ricaduta, zona di esclusione di 150 m presidiata con le forze dell'ordine, monitoraggio sismografico sui capannoni adiacenti riutilizzati.",
 "normative": "R.D. 773/1931 TULPS e disposizioni attuative (detenzione, trasporto e impiego di esplosivi: autorizzazioni di pubblica sicurezza); ordinanze locali e prefettizie per lo sparo; D.Lgs 81/2008 Sezione VIII e Titolo XI (atmosfere esplosive) per la parte di cantiere. Per i dettagli amministrativi specifici: da verificare con questura e prefettura competenti.",
 "note_cantiere": "Il giorno dello sparo il cantiere lo governa la pubblica autorita': prepara per iscritto la conta delle persone, la doppia ispezione finale del manufatto e la procedura di 'misfire' (carica non esplosa) prima ancora di caricare i fori. Dopo il botto, primo ingresso solo al minatore con gas-detector e permesso scritto."
})

S.append({
 "categoria": "Demolizioni — metodi speciali",
 "nome": "Metodi speciali: agenti espansivi, idrodemolizione e robot radiocomandati",
 "descrizione": "Tre tecniche di nicchia che risolvono contesti dove meccanica ed esplosivo non sono praticabili: fessurazione senza vibrazioni con agenti espansivi, asportazione selettiva del calcestruzzo degradato con acqua ad altissima pressione, demolizione in spazi ristretti con macchine radiocomandate elettriche.",
 "tecnologia": "Agenti espansivi (malte o cartucce in fori da 30-50 mm, passo 30-60 cm, fessurazione in 4-24 ore per pressione di espansione crescente); idrodemolizione (pompe 1.000-2.500 bar, portate 100-260 l/min, asportano il cls ammalorato senza danneggiare l'armatura, produzione 0,2-1 m3/h); robot radiocomandati elettrici da 0,5-5 t con pinze o martelli, capaci di salire su solai e passare per aperture di un metro.",
 "applicazioni": "Espansivi: cave, centri storici, vicino a recettori sensibili alle vibrazioni. Idrodemolizione: ripristino di ponti, pile, gallerie, serbatoi. Robot: interni di ospedali e industrie in esercizio, solai di portata limitata, gallerie, ambienti confinati o contaminati.",
 "vantaggi": "Vibrazioni praticamente nulle (espansivi e idrodemolizione); accesso dove i mezzi tradizionali non entrano (robot); asportazione selettiva che preserva cio' che resta (idrodemolizione: non microfessura l'armatura, ideale prima del ripristino).",
 "limiti": "Produttivita' bassa e costo orario alto: antieconomici su grandi volumi; gli espansivi richiedono foratura accurata e tempi di attesa; l'idrodemolizione genera fanghi e acque pressurizzate da raccogliere e smaltire; i robot richiedono piano d'appoggio verificato e gestione dei cavi di alimentazione.",
 "costi_e_economia": "Ordini di grandezza indicativi: espansivi 60-150 euro/m3 demolito (materiale 10-60 euro/m3 + foratura); idrodemolizione 400-900 euro/m3 di conglomerato asportato (spessori tipici 5-15 cm); robot radiocomandato con operatore 80-150 euro/h.",
 "casi_real_world": "Caso tipo: ripristino delle pile di un viadotto autostradale senza chiusura della viabilita' sottostante: idrodemolizione notturna del copriferro ammalorato con raccolta separata dei fanghi, seguita da ricostruzione con malte tissotropiche.",
 "normative": "D.Lgs 81/2008 Titoli III e IV (attrezzature e cantieri); Direttiva Macchine 2006/42/CE (robot e pompe); D.Lgs 152/2006 Parte III (acque e fanghi di processo); schede di sicurezza dei prodotti espansivi (Reg. (CE) 1907/2006 REACH).",
 "note_cantiere": "Con gli espansivi non guardare MAI dentro il foro dopo il riempimento e rispetta tempi e distanze del produttore: l'espulsione improvvisa del tappo di malta espansiva ha accecato piu' di un operatore. Con l'idrodemolizione tratta il getto come un'arma: zona esclusa e DPI specifici, sempre."
})

S.append({
 "categoria": "Demolizioni — decostruzione e rifiuti",
 "nome": "Decostruzione selettiva operativa e strip-out: smontare prima di abbattere",
 "descrizione": "L'approccio inverso alla costruzione: prima delle macchine, il cantiere rimuove manualmente o con piccoli mezzi finiture, impianti e componenti recuperabili (strip-out), poi procede per strati verso le strutture. Qui il focus operativo di cantiere; gli aspetti di LCA e passaporto materiali sono trattati nel corso sull'edilizia circolare.",
 "tecnologia": "Sequenza tipo: bonifica impianti e distacchi; rimozione delle sostanze pericolose (amianto, oli, gas refrigeranti); serramenti e finiture; impianti; partizioni non portanti; strutture secondarie; strutture portanti. Magazzino di cantiere con schede materiale, imballo ed etichettatura dei componenti per il riuso; tracciabilita' fotografica piano per piano; piccoli mezzi elettrici per lavorare in spazi chiusi.",
 "applicazioni": "Edifici con componenti riutilizzabili (capriate lignee, serramenti, pavimenti pregiati, scale); bandi pubblici con requisiti CAM sulla demolizione selettiva; retrofit parziali in cui una parte dell'edificio resta in uso; centri storici.",
 "vantaggi": "Recupera valore dai componenti (crediti che riducono il costo netto); aumenta la quota di recupero e riduce i conferimenti; produce la documentazione fotografica delle percentuali di recupero richiesta in contabilita' e nei bandi CAM.",
 "limiti": "Tempi 1,5-3 volte quelli della demolizione meccanica pura; richiede manodopera piu' qualificata e coordinamento piu' stretto; il mercato del riuso e' ancora sottile e i prezzi dei componenti recuperati sono incerti; spazi di cantiere per il magazzino non sempre disponibili.",
 "costi_e_economia": "Ordini di grandezza indicativi: strip-out di finiture e impianti 15-50 euro/m2; decostruzione completa 40-90 euro/m3 contro 15-45 della meccanica tradizionale, parzialmente compensata da crediti per materiali recuperati (ordine 2-15 euro/m3 equivalenti, molto variabili) e da minori costi di conferimento.",
 "casi_real_world": "Caso tipo: ex scuola anni '30 in centro: recupero documentato di 400 m2 di pavimenti in graniglia, delle capriate lignee e dei serramenti in legno per riuso diretto in altri edifici pubblici; la quota di materiale avviato a recupero supera l'80% in peso.",
 "normative": "Direttiva 2008/98/CE (obiettivo del 70% di preparazione per il riutilizzo e riciclaggio dei rifiuti C&D non pericolosi); D.M. 11 ottobre 2017 (CAM Edilizia: criteri sulla demolizione selettiva negli appalti — percentuali e dettagli da verificare sul decreto vigente); D.Lgs 152/2006 Parte IV; L. 257/1992 (l'amianto si rimuove sempre prima di tutto il resto).",
 "note_cantiere": "Fai finire lo strip-out piano per piano e fotografa ogni fase PRIMA che entrino le macchine: quelle foto sono la prova delle percentuali di recupero che dovrai dichiarare in collaudo. E metti per iscritto chi e' proprietario dei materiali recuperati: e' la lite piu' frequente con la committenza."
})

S.append({
 "categoria": "Demolizioni — decostruzione e rifiuti",
 "nome": "Rifiuti da demolizione: codici CER 17, bilancio di massa e percorso documentale",
 "descrizione": "La demolizione e' un processo di produzione di rifiuti: ogni tonnellata deve avere un codice, un documento di trasporto e una destinazione tracciata. Il bilancio di massa stimato in fase di piano guida preventivo e cronoprogramma.",
 "tecnologia": "Piano rifiuti preliminare con bilancio di massa (ordini di letteratura: 0,8-1,5 t/m3 lordo per edilizia residenziale in c.a.; 1-2 t/m2 di superficie); attribuzione dei codici CER del capitolo 17 (170101 calcestruzzo, 170102 mattoni, 170107 misti di c.a., 170504 terre e pietre, 170201 legno, 170401-407 metalli, 170801 gesso, 170904 rifiuti misti C&D, 170601*/170605* materiali con amianto — codici con asterisco = pericolosi); deposito temporaneo; formulario di identificazione in 4 copie (art. 193); registri di carico/scarico (art. 190); MUD annuale.",
 "applicazioni": "Ogni cantiere di demolizione; obblighi in capo al produttore del rifiuto (committente o impresa secondo il contratto) e al trasportatore iscritto all'Albo Nazionale Gestori Ambientali.",
 "vantaggi": "Un piano rifiuti fatto bene evita sanzioni, fermi dell'impianto e contestazioni in contabilita'; la separazione alla fonte riduce i costi (il misto 170904 costa piu' dei codici separati) e aumenta la quota recuperata.",
 "limiti": "I carichi misti e male documentati sono la trappola tipica: codici errati, formulari incompleti, destinatari non autorizzati espongono l'impresa a sanzioni anche penali; la gestione documentale assorbe risorse amministrative dedicate.",
 "costi_e_economia": "Ordini di grandezza indicativi: conferimento di inerti non pericolosi 8-30 euro/t in impianto di recupero o discarica; trasporto 15-40 euro a viaggio su brevi distanze per autocarri da 25-30 t (ordine 0,10-0,25 euro/t·km su distanze maggiori); materiali pericolosi (es. contenenti amianto) 150-400 euro/t piu' imballo e filiera dedicata — per l'amianto si rinvia al corso sulle bonifiche.",
 "casi_real_world": "Caso tipo: demolizione urbana con quattro cassoni dedicati (conglomerato, ferro, legno, gesso): recupero documentato dell'82% in peso, sconto sul conferimento del conglomerato selezionato e zero contestazioni in contabilita' finale.",
 "normative": "D.Lgs 152/2006 Parte IV: artt. 184-189 (definizioni, classificazione e attribuzione del codice, responsabilita' del produttore art. 188), art. 190 (registri), art. 193 (formulario); Decisione 2000/532/CE (elenco europeo dei rifiuti); L. 257/1992 e normativa amianto per i codici 1706xx.",
 "note_cantiere": "Il codice CER si decide PRIMA di caricare il cassone, non davanti al cancello dell'impianto: foto del carico, pesata e formulario compilato bene ti salvano da contestazioni e respingimenti. Un cassone misto 'tanto poi si vede' e' un costo certo e un rischio penale."
})

S.append({
 "categoria": "Demolizioni — decostruzione e rifiuti",
 "nome": "Frantumazione in sito e riutilizzo degli inerti come aggregato riciclato",
 "descrizione": "Trasformare il risultante di demolizione in aggregato direttamente in cantiere, con impianto mobile: il materiale rientra in opera come sottofondo, rilevato o riempimento, riducendo trasporti, conferimenti e acquisto di materiali vergini.",
 "tecnologia": "Frantoi mobili a mascelle o a urto (produzione tipica 80-300 t/h), vagli vibranti, deferrizzatori magnetici per l'armatura, selezione manuale e ad aria; controllo di qualita' del frantumato: curva granulometrica, equivalente di sabbia, resistenza alla frammentazione (Los Angeles); campionamenti sistematici durante la produzione; stoccaggi separati per classe granulometrica.",
 "applicazioni": "Grandi demolizioni con riuso in sito (piattaforme industriali, rilevati stradali, sottofondi di piazzali), cantieri lontani dagli impianti di riciclaggio, interventi con obiettivi di recupero elevati.",
 "vantaggi": "Riduce drasticamente viaggi di camion, costi di conferimento e acquisto di aggregati vergini (risparmio complessivo tipico 30-60% sulla voce movimento materiali); documenta concretamente gli obiettivi di recupero; il ferro recuperato dal deferrizzatore genera un credito.",
 "limiti": "L'impianto mobile richiede spazio, autorizzazione e gestione di rumore e polveri; la qualita' del frantumato dipende dal materiale in ingresso (misto con gesso o legno = declassato); il quadro nazionale End of Waste per gli aggregati da C&D e' ancora da completare a livello nazionale (riferimento da verificare sul MASE): spesso si opera in regime di rifiuto con autorizzazioni regionali.",
 "costi_e_economia": "Ordini di grandezza indicativi: frantumazione mobile 6-18 euro/t frantumato (noleggio impianto 8.000-25.000 euro/mese o prezzo a t con impresa specializzata); valore evitato dell'aggregato vergine equivalente 8-15 euro/t franco cantiere; credito del ferro da recupero variabile col mercato dei rottami.",
 "casi_real_world": "Caso tipo: demolizione di una caserma da 40.000 m3: circa 28.000 t di conglomerato frantumato in sito e riusato come sottofondo dei nuovi piazzali, con oltre 1.000 viaggi di camion evitati e curva granulometrica certificata giorno per giorno.",
 "normative": "D.Lgs 152/2006 Parte IV (in particolare art. 184-ter sulla cessazione della qualifica di rifiuto); disciplina nazionale End of Waste per aggregati da C&D: adozione nazionale da verificare sul MASE — nel frattempo valgono discipline regionali e autorizzazioni caso per caso; UNI EN 13242 (aggregati per materiali non legati e legati idraulicamente) e Reg. (UE) 305/2011 se il frantumato e' immesso sul mercato come prodotto; Dir. 2008/98/CE (obiettivo 70% recupero).",
 "note_cantiere": "Campiona il frantumato ogni giorno di produzione e fai firmare le curve granulometriche al DL: un fascicolo di prove vale piu' di mille discussioni in collaudo. E separa SEMPRE gesso e legno prima della tramoggia: bastano pochi sacchi di cartongesso per buttare un intero cumulo."
})

S.append({
 "categoria": "Demolizioni — impatto e contesto",
 "nome": "Polveri, rumore e vibrazioni in demolizione: prevenzione alla fonte e monitoraggio",
 "descrizione": "I tre impatti fisici caratteristici del cantiere di demolizione. La norma prescrive l'abbattimento alla fonte delle polveri; il monitoraggio strumentale di vibrazioni e rumore tutela edifici vicini, recettori sensibili e l'impresa stessa dalle contestazioni.",
 "tecnologia": "Polveri: irrorazione continua con nebbie e cannoni nebulizzatori (l'art. 153 impone la riduzione del sollevamento), teli e schermi, lavaggio ruote. Vibrazioni: sismografi/vibrometri con misura della velocita' di picco delle particelle (PPV, mm/s); criteri di valutazione UNI 9916 e, come riferimento tecnico diffuso, DIN 4150-3; soglie di attenzione di letteratura 5-20 mm/s PPV a seconda della sensibilita' dell'edificio e della frequenza. Rumore: fonometri classe 1, baseline pre-opera, rispetto dei limiti di sorgente e degli orari comunali. Polveri PM10 con centraline in continuo nei cantieri sensibili.",
 "applicazioni": "Demolizioni urbane, adiacenze a edifici abitati, cliniche, laboratori con strumenti sensibili, edifici monumentali; obbligatorio di fatto quando il piano prevede mezzi pesanti a ridosso di terzi.",
 "vantaggi": "Il monitoraggio documentato e' la difesa tecnica e legale dell'impresa; le soglie di allarme permettono di correggere il metodo prima del danno; migliora drasticamente le relazioni con il vicinato e con gli enti di controllo.",
 "limiti": "Costi di strumentazione e di personale tecnico; falsi allarmi da traffico e lavori terzi (serve baseline pre-opera per distinguerli); i limiti normativi acustici si applicano alla sorgente, ma la percezione del vicino e' piu' severa dei numeri.",
 "costi_e_economia": "Ordini di grandezza indicativi: campagna combinata vibrazioni+acustica 1.500-8.000 euro; centralina polveri a noleggio 2.000-6.000 euro/mese; rilievo fonometrico pre/post 800-2.500 euro; sistemi di irrorazione 3.000-15.000 euro a cantiere secondo dimensione.",
 "casi_real_world": "Caso tipo: demolizione adiacente a una clinica privata: baseline vibrazionale di due settimane prima dell'apertura, soglia di allarme impostata a 5 mm/s con SMS al direttore dei lavori, nessun superamento documentato e zero richieste di risarcimento a fine lavori.",
 "normative": "D.Lgs 81/2008 art. 153 (riduzione del sollevamento polveri mediante irrorazione); L. 447/1995 (legge quadro sull'inquinamento acustico) e DPCM 14/11/1997 (valori limite delle sorgenti sonore); UNI 9916 (criteri di misura e valutazione degli effetti delle vibrazioni sugli edifici); regolamenti comunali su orari e cantieri; D.Lgs 152/2006 Parte V (emissioni in atmosfera).",
 "note_cantiere": "Prima di accendere le macchine fai il rilievo fotografico datato dei dissesti degli edifici vicini e una settimana di baseline strumentale: la prima crepa che 'compare' sara' attribuita a te, e solo i numeri registrati prima ti difendono. Nebulizza sul punto di impatto della pinza, non 'in generale'."
})

S.append({
 "categoria": "Demolizioni — impatto e contesto",
 "nome": "Demolizioni in contesto urbano e con terzi presenti: schermi, protezioni e viabilita'",
 "descrizione": "Demolire in citta' abitata significa lavorare con il pubblico a ridosso: pedoni, residenti, attivita' in esercizio, edifici adiacenti condivisi o accostati. Richiede protezioni fisiche, organizzazione delle finestre di lavoro e gestione attiva delle relazioni con i terzi.",
 "tecnologia": "Schermi e parapolvere su ponteggi di protezione, tunnel pedonali coperti, coperture provvisionali; delimitazione e sbarramento delle zone di caduta (art. 154); divieto di getto dall'alto con convogliamento in canali (art. 153); finestre orarie concordate per le fasi rumorose; piani di viabilita' e occupazione suolo pubblico; comunicazione preventiva ai residenti (date, orari, recapiti); coordinamento con i gestori dei servizi e con gli edifici adiacenti in comunione strutturale.",
 "applicazioni": "Demolizioni parziali con edificio parzialmente abitato, centri storici, fronti su strade aperte al traffico, adiacenze a scuole, ospedali, attivita' commerciali in esercizio.",
 "vantaggi": "Riduce a zero i contatti fisici con i terzi e quasi a zero il contenzioso; le finestre concordate evitano le sospensioni disposte d'urgenza; un cantiere 'educato' mantiene la viabilita' e la reputazione dell'impresa.",
 "limiti": "Produttivita' ridotta (fasce orarie limitate, divieto di getto, cicli piu' lenti); costi di protezione e di occupazione suolo pubblico; coordinamento complesso con molti interlocutori (comune, utility, vicini, attivita' commerciali).",
 "costi_e_economia": "Ordini di grandezza indicativi: protezioni pubbliche e tunnel pedonali 15-40 euro/m2 di fronte protetto; sovraccosto complessivo urbano +20-50% sul prezzo della demolizione in campo aperto; occupazioni di suolo pubblico secondo tariffari comunali (da verificare comune per comune).",
 "casi_real_world": "Caso tipo: demolizione piano per piano di un edificio anni '50 incuneato tra due condomini abitati: tunnel pedonale su tutto il fronte, divieto assoluto di getto con canali di convogliamento, fasi rumorose concentrate in due finestre giornaliere comunicate ai residenti; lavori conclusi senza sospensioni.",
 "normative": "D.Lgs 81/2008 artt. 153 (convogliamento del materiale, vietato il getto dall'alto) e 154 (sbarramento della zona di demolizione); D.P.R. 380/2001 (titolo abilitativo: demolizione e ricostruzione come ristrutturazione edilizia, art. 3; per la sola demolizione disciplina secondo norme regionali e comunali — da verificare); regolamenti edilizi e di polizia urbana locali.",
 "note_cantiere": "Il vicinato informato scrive meno esposti: una lettera con date, fasi rumorose e il cellulare del capocantiere riduce davvero le sospensioni. E controlla ogni mattina schermi e tunnel: un pannello spostato dal vento di notte, trovato da un pedone, ti chiude il cantiere."
})

S.append({
 "categoria": "Demolizioni — economia e contabilita'",
 "nome": "Economia e contabilita' della demolizione: prezzi, crediti da recupero ed errori di preventivo",
 "descrizione": "Come si forma davvero il costo di una demolizione e come va contabilizzata: la voce dominante non e' l'abbattimento ma la gestione dei materiali, e l'errore di preventivo piu' frequente e' la sottostima di trasporti e conferimenti.",
 "tecnologia": "Computo a m3 lordo, m2 o tonnellata con bilancio di massa di supporto; voci tipo: indagini e piano, ponteggi e protezioni, demolizione vera e propria, selezione e carico, trasporto, conferimento, ripristini e ripristino del verde; crediti da recupero (rottame ferroso ordine 100-250 euro/t con mercato molto volatile, metalli non ferrosi piu' pregiati); SAL agganciati alle pesate e ai formulari; contabilita' analitica per codice CER.",
 "applicazioni": "Preventivi e offerte di gara, contabilita' lavori in corso e a saldo, stime di commessa, piani economici di demolizione e ricostruzione.",
 "vantaggi": "Una struttura di prezzo corretta evita perdite nascoste e contestazioni finali; i crediti da recupero possono ribassare sensibilmente il costo netto; la contabilita' per codice CER documenta automaticamente le percentuali di recupero.",
 "limiti": "Volatilita' dei prezzi dei rottami e dei conferimenti (va previsto meccanismo di aggiornamento); sorprese da materiali pericolosi non indagati; i prezzi a corpo senza bilancio di massa sono scommesse, non computi.",
 "costi_e_economia": "Ordini di grandezza indicativi: demolizione 'chiavi in mano' di edificio ordinario 25-70 euro/m3 lordo tutto compreso; edilizia industriale semplice 15-40 euro/m3; demolizioni speciali (taglio controllato, contesti ospedalieri) 80-300 euro/m3; la voce smaltimento pesa tipicamente il 30-50% del totale.",
 "casi_real_world": "Caso tipo: gara con computo a sola voce 'demolizione meccanica 18 euro/m3' senza conferimenti: l'analisi con bilancio di massa porta il costo reale a 34 euro/m3; l'offerta viene corretta prima della presentazione, evitando una commessa in perdita certa.",
 "normative": "D.Lgs 36/2023 (Codice dei contratti pubblici: SAL e contabilita' negli appalti); D.Lgs 152/2006 Parte IV per la contabilita' documentale dei rifiuti (formulari e registri come allegati obbligati dei SAL); D.M. 11 ottobre 2017 (CAM) per i criteri economici di gara.",
 "note_cantiere": "Pesa tutto e conserva ogni formulario: in contabilita' finale ogni tonnellata senza formulario e' una contestazione garantita. E nel preventivo scrivi nero su bianco chi incassa i crediti dei rottami: il ferro vale, e se non e' scritto diventa la lite di fine lavori."
})

def main():
    os.makedirs(os.path.join(BASE, 'schede'), exist_ok=True)
    with open(os.path.join(BASE, 'schede', 'schede.jsonl'), 'w', encoding='utf-8') as f:
        for s in S:
            assert list(s.keys()) == KEYS, f"chiavi errate: {s['nome']}"
            f.write(json.dumps(s, ensure_ascii=False) + '\n')

    course = '''corso: "Demolizioni tecniche e fine vita degli edifici: indagini preliminari, piano di demolizione, tecniche esecutive e metodi speciali, decostruzione operativa, rifiuti CER 17 e frantumazione in sito, impatti, contesto urbano, economia"
facolta: "FACOLTA_TECNOLOGIA_E_COSTRUZIONE"
livello: "L1-L2"
schede: 12
formato: "JSONL"
lingua: "it"
schema_campi: [categoria, nome, descrizione, tecnologia, applicazioni, vantaggi, limiti, costi_e_economia, casi_real_world, normative, note_cantiere]
fonti: "D.Lgs 81/2008 (Titolo IV Capo II Sezione VIII Demolizioni artt. 150-156: art. 150 verifica e rafforzamento, art. 151 ordine e piano nel POS ex art. 89 co.1 lett. h, art. 152 misure di sicurezza, art. 153 convogliamento e irrorazione, art. 154 sbarramento, art. 155 rovesciamento), D.Lgs 152/2006 (Parte IV rifiuti: artt. 184-189, 190, 193, 184-ter End of Waste; Parte V aria), Decisione 2000/532/CE (codici CER 17), Dir. 2008/98/CE (obiettivo 70% recupero C&D), D.M. 11 ottobre 2017 (CAM Edilizia), L. 257/1992 e D.Lgs 81/2008 Titolo IX (amianto, di rinvio), R.D. 773/1931 TULPS (esplosivi), L. 447/1995 e DPCM 14/11/1997 (acustica), UNI 9916 (vibrazioni su edifici), UNI EN 13242 (aggregati), Reg. (UE) 305/2011 CPR, Direttiva Macchine 2006/42/CE, D.P.R. 380/2001 (titoli abilitativi), D.Lgs 36/2023 (contabilita' appalti), NTC D.M. 17/1/2018; decreto nazionale End of Waste aggregati C&D citato come da verificare"
nota_metodologica: "Corso operativo sul fine vita tecnico degli edifici: indagini conoscitive pre-demolizione (rilievo, servizi, amianto come presupposto), piano di demolizione allegato al POS (art. 151), demolizione meccanica (pinze, martelli, high-reach), taglio controllato (filo diamantato, dischi, carotaggi), esplosivo e implosioni, metodi speciali (espansivi, idrodemolizione, robot), decostruzione selettiva OPERATIVA e strip-out, rifiuti CER 17 con bilancio di massa e documenti, frantumazione in sito, polveri/rumore/vibrazioni (monitoraggio e limiti), contesto urbano con terzi presenti, economia e contabilita'. NON ridondante: EDILIZIA_CIRCOLARE_LCA_PACK tratta LCA, EPD, passaporti materiali e circolarita' di filiera; BONIFICA_SITI_AMBIENTALI_EDILIZIA_PACK tratta contaminazione e amianto: qui la TECNICA ESECUTIVA e la gestione del cantiere di demolizione. Norme solo di consolidata certezza (artt. 150-155 D.Lgs 81/2008 verificati su fonti concordanti 01/11/2026); prezzi come fasce indicative; nessun nome di azienda."
'''
    with open(os.path.join(BASE, 'COURSE.yaml'), 'w', encoding='utf-8') as f:
        f.write(course)

    readme = '''# Demolizioni tecniche e fine vita degli edifici

Corso L1-L2 della Facolta di Tecnologia e Costruzione: il cantiere di demolizione come processo tecnico controllato — indagini conoscitive preliminari (rilievo, servizi, presupposti per l'art. 150 D.Lgs 81/2008), piano di demolizione allegato al POS (art. 151), demolizione meccanica con pinze, martelli e bracci high-reach, taglio controllato con filo diamantato e carotaggi, implosioni con esplosivo, metodi speciali (agenti espansivi, idrodemolizione, robot radiocomandati), decostruzione selettiva operativa e strip-out, gestione documentale dei rifiuti CER 17 con bilancio di massa, frantumazione in sito e riutilizzo degli inerti, controllo di polveri/rumore/vibrazioni, demolizioni in contesto urbano con terzi presenti, economia e contabilita' della demolizione.

**Schede: 12**

Non ridondante con EDILIZIA_CIRCOLARE_LCA_PACK (LCA, EPD, passaporti dei materiali e circolarita' di filiera) e con BONIFICA_SITI_AMBIENTALI_EDILIZIA_PACK (contaminazione e amianto): qui la tecnica esecutiva, la sicurezza specifica (Sezione VIII Titolo IV D.Lgs 81/2008) e la gestione operativa del cantiere di demolizione.
'''
    with open(os.path.join(BASE, 'README.md'), 'w', encoding='utf-8') as f:
        f.write(readme)

    print(f"Creato {BASE}: {len(S)} schede")

if __name__ == '__main__':
    main()
