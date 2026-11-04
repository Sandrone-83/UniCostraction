# -*- coding: utf-8 -*-
"""Giro AP: genera RETAIL_CENTRI_COMMERCIALI_PACK (12 schede)."""
import json, os

PACK = 'RETAIL_CENTRI_COMMERCIALI_PACK'
ROOT = os.path.join('UNIVERSITA_EDILIZIA', PACK)
K = ['categoria','nome','descrizione','tecnologia','applicazioni','vantaggi','limiti',
     'costi_e_economia','casi_real_world','normative','note_cantiere']

def S(categoria, nome, descrizione, tecnologia, applicazioni, vantaggi, limiti,
      costi_e_economia, casi_real_world, normative, note_cantiere):
    d = dict(zip(K, [categoria, nome, descrizione, tecnologia, applicazioni, vantaggi,
                     limiti, costi_e_economia, casi_real_world, normative, note_cantiere]))
    assert d['costi_e_economia'].startswith('Ordini di grandezza indicativi: '), nome
    return d

SCHEDE = [

S('Formati e autorizzazioni', 'Formati retail e quadro autorizzatorio del commercio',
  'Il retail edilizio si classifica per formato: esercizi di vicinato, medie strutture di vendita, grandi strutture di vendita (supermercati, ipermercati, grandi magazzini), centri commerciali (aggregazione unitaria di esercizi intorno a una galleria comune con parcheggi condivisi), retail park e factory outlet. Ogni formato ha una soglia dimensionale e un diverso iter autorizzatorio: piu\u0300 il formato cresce, piu\u0300 l\u2019autorizzazione si sposta dalla SCIA comunale all\u2019autorizzazione regionale, con studi di impatto commerciale e verifiche di compatibilita\u0300 con i piani commerciali.',
  'Classificazione ex D.Lgs 114/1998: medie strutture (superficie di vendita oltre 150 m2 e fino a 1.500 m2 nei comuni fino a 10.000 abitanti, oltre 250 m2 e fino a 2.500 m2 nei comuni oltre 10.000 abitanti), grandi strutture oltre le soglie delle medie, grandi strutture oltre le soglie delle medie; centro commerciale = insieme progettato e gestito unitariamente, con galleria comune, parcheggi e dotazioni collettive. Le regioni fissano soglie, tetti e procedure nei piani commerciali territoriali: le soglie esatte vanno verificate regione per regione.',
  'Nuovi insediamenti commerciali, ampliamenti, riconversioni di immobili esistenti a uso vendita, verifica di fattibilita\u0300 urbanistica prima dello studio di fattibilita\u0300 economica.',
  'Quadro autorizzatorio definito fin dal preliminare; dimensionamento coerente con bacino e piani commerciali; evita investimenti su siti non compatibili.',
  'Normativa commerciale fortemente regionalizzata: le soglie nazionali sono un riferimento, ma le leggi regionali possono differire sensibilmente; i piani commerciali possono prevedere moratorie o tetti comunali; tempi di autorizzazione lunghi (mesi-anni) per grandi strutture.',
  'Ordini di grandezza indicativi: studio di impatto commerciale e fattibilita\u0300 20-80 k€; istruttoria autorizzativa grande struttura 12-36 mesi; oneri di urbanizzazione e opere a scomputo variabili per comune, spesso 5-15% del costo di costruzione.',
  'Caso tipo: sviluppo di un retail park su area ex industriale dismessa; il piano commerciale regionale impone lo studio di impatto sul commercio insediato; ottenuta l\u2019autorizzazione con prescrizioni su viabilita\u0300 e mitigazione, il cantiere parte a 18 mesi dal deposito.',
  'D.Lgs 26/3/1998 n. 114 (riforma del commercio); D.Lgs 26/3/2010 n. 59 (SCIA e attivita\u0300 commerciali); leggi regionali di attuazione e piani commerciali territoriali (da verificare per la regione); DPR 380/2001 per i titoli edilizi.',
  'Prima di comprare un\u2019area o firmare un preliminare per un retail, fai verificare al tecnico la compatibilita\u0300 col piano commerciale comunale e regionale: un sito perfetto urbanisticamente puo\u0300 essere invendibile autorizzativamente per tetto di superficie.'),

S('Masterplan e layout', 'Masterplan, layout e tenant mix del centro commerciale',
  'Il layout di un centro commerciale nasce dal masterplan: posizione dell\u2019anchor (ipermercato o grande magazzino), conformazione della galleria (lineare, a L, a T, a corte centrale), distribuzione delle unita\u0300 medie e piccole, food court, accessi e collegamenti con i parcheggi. Il tenant mix (composizione merceologica) e la geometria della galleria determinano i flussi pedonali e il rendimento commerciale: la progettazione edilizia deve servire la strategia commerciale, non viceversa.',
  'Parametri tipici: GLA (superficie lorda affittabile) da 5.000 m2 (centro di prossimita\u0300) a oltre 60.000 m2 (regionale); galleria larga 8-16 m con altezze libere 4-7 m; court centrale come nodo visivo e distributivo; rapporto parcheggi/GLA indicativo 4-6 posti per 100 m2 secondo standard regionali e comunali; percorsi pedonali con pavimentazioni continue e luce naturale da lanterne o shed sulla galleria.',
  'Centri commerciali di nuova costruzione, retail park, ampliamenti di gallerie esistenti, ripensamento dei flussi in occasione di restyling.',
  'Layout chiaro = flussi equilibrati e canoni sostenibili; galleria come spazio pubblico coperto aumenta tempi di permanenza; anchor ben posizionate trainano le unita\u0300 minori.',
  'Errori di layout sono quasi irrecuperabili senza demolizioni; gallerie troppo lunghe generano zone morte a basso traffico; doppi carichi di progetto (commerciale + impianti + finiture ricche) alzano i costi della galleria ben oltre quelli dei box.',
  'Ordini di grandezza indicativi: progettazione masterplan e concept 1,5-3% del costo dell\u2019opera; costo costruzione galleria comune finita 1.500-2.500 €/m2; box in shell 700-1.200 €/m2.',
  'Caso tipo: centro commerciale a galleria lineare con anchor ai due estremi; la court centrale dimezza la distanza percettiva e concentra i servizi (food court, toilette, info point); le unita\u0300 in prossimita\u0300 della court registrano i canoni piu\u0300 alti.',
  'D.Lgs 114/1998 (centro commerciale come gestione unitaria); D.M. 236/1989 (accessibilita\u0300 percorsi); NTC D.M. 17/1/2018 (sovraccarichi gallerie 4-5 kN/m2 secondo categoria); standard parcheggi da normativa regionale e comunale (da verificare).',
  'Congela la maglia strutturale solo dopo il tenant mix preliminare: cambiare un anchor in corsa vuol dire rifare luci, carichi e impianti. Prevedi giunti e tolleranze per box divisibili: i negozi si aggregano e si dividono di continuo.'),

S('Prevenzione incendi', 'Antincendio nelle grandi superfici commerciali',
  'Le attivita\u0300 commerciali aperte al pubblico con superficie oltre soglia sono soggette al controllo dei Vigili del Fuoco e alla progettazione secondo il Codice di prevenzione incendi. I nodi critici sono: esodo in presenza di grande affollamento (migliaia di occupanti, molti non familiari col luogo), controllo di fumi e calore in galleria (spazi alti e comunicanti), compartimentazione tra box e galleria, protezione delle corsie di carico e dei magazzini.',
  'Strategie del Codice D.M. 3/8/2015: esodo orizzontale verso spazi scoperti o compartimenti adiacenti, larghezze di uscita dimensionate sull\u2019affollamento ipotizzato (persone/m2 per tipo di attivita\u0300), SEFC (sistemi di evacuazione forzata di fumi e calore) in galleria secondo UNI EN 12101, sprinkler secondo UNI EN 12845, reazione al fuoco dei materiali di finitura (classi europee UNI EN 13501-1), rivelazione automatica e impianto di allarme vocale (EVAC) per la gestione ordinata dell\u2019esodo.',
  'Centri commerciali, ipermercati, grandi magazzini, retail park, outlet; anche singoli negozi oltre le soglie di soggezione ai controlli di prevenzione incendi.',
  'Approccio prestazionale del Codice consente soluzioni su misura per gallerie e grandi volumi; SEFC ben progettato mantiene gli strati liberi da fumi per i tempi di esodo; sprinkler riduce drasticamente il danno atteso.',
  'Costi impiantistici rilevanti (sprinkler, SEFC, EVAC possono valere il 10-15% del costo impianti); gestione e manutenzione obbligatorie e continuative; in galleria la compartimentazione tra box e spazio comune condiziona serramenti e finiture.',
  'Ordini di grandezza indicativi: sprinkler 40-80 €/m2 protetti; SEFC in galleria 20-50 k€ per serranda/gruppo; EVAC per centro medio 80-250 k€; pratica VVF con aggiornamento attivita\u0300 3-10 k€ di parcelle.',
  'Caso tipo: ampliamento di una galleria con nuova court; la soluzione prestazionale dimostra, con simulazione di esodo e fumi, che le uscite esistenti piu\u0300 una nuova uscita di compartimento garantiscono l\u2019esodo nei tempi richiesti, evitando un tunnel antincendio di 60 m.',
  'DPR 151/2011 (attivita\u0300 soggette ai controlli: attivita\u0300 commerciali aperte al pubblico oltre 400 m2); D.M. 3/8/2015 (Codice prevenzione incendi) e regola tecnica specifica per le attivita\u0300 commerciali (verificare versione vigente); UNI EN 12101 (controllo fumi); UNI EN 12845 (sprinkler); UNI EN 13501-1 (reazione al fuoco).',
  'Non lasciare la progettazione antincendio alla fine: larghezze di esodo, SEFC e vani impianto cambiano la geometria della galleria. E verifica sempre chi gestisce: un impianto perfetto senza manutenzione programmata e una responsabilita\u0300 penale, non una protezione.'),

S('Strutture', 'Strutture di grande luce per il retail',
  'Le grandi superfici di vendita richiedono luci libere di 16-32 m per lasciare flessibilita\u0300 agli scaffali e ai layout: le soluzioni tipiche sono telai in c.a. prefabbricato con travi precompresse, capriate metalliche reticolari o a traliccio, e per la copertura elementi alveolari, lamiera grecata collaborante o pannelli sandwich. La maglia pilastri (tipicamente 8x16 m o 16x16 m) e\u0300 scelta con il committente perche\u0300 condiziona layout, scaffalature e parcheggi.',
  'Prefabbricato in c.a.: pilastri a bicchiere o con piastra, travi a I o a T precompresse luce 16-24 m, tegoli alveolari o TT; acciaio: capriate reticolari luce 24-40 m con arcarecci, controventi di parete e di falda; fondazioni: plinti o platea a seconda del terreno; pavimentazione industriale in cls fibrorinforzato 18-25 cm con giunti segati o armati, planarieta\u0300 controllata per scaffalature e carrelli.',
  'Ipermercati e supermercati, box dei retail park, brico e DIY, cash & carry, grandi magazzini; anche palestre e cinema inseriti nei centri (vasche e sale richiedono strutture dedicate).',
  'Grand luci senza pilastri intermedi = massima flessibilita\u0300 commerciale; prefabbricazione = tempi rapidi e qualita\u0300 controllata; coperture metalliche leggere riducono le azioni sismiche.',
  'Il prefabbricato impone nodi e appoggi da dettagliare bene (appoggi travi, bicchieri, neoprene); coperture metalliche soffrono condensa se non corrette in stratigrafia; la pavimentazione industriale e\u0300 critica: errori di planarieta\u0300 o giunti sbagliati si pagano per decenni.',
  'Ordini di grandezza indicativi: struttura prefabbricata in c.a. con copertura 180-300 €/m2 coperti; capriata metallica con lamiera e pannello 100-180 €/m2; pavimento industriale armato con giunti 45-80 €/m2.',
  'Caso tipo: ipermercato 12.000 m2 con maglia 16x8 m, pilastri a bicchiere e travi precompresse da 20 m; la copertura a tegoli TT consente gli impianti a vista sottotrave; il pavimento con fibre e giunti armati regge il traffico dei transpallet da 20 anni.',
  'NTC D.M. 17/1/2018 (azioni neve, vento, sisma; sovraccarichi vendita); Eurocodici EN 1990-1994 e NA nazionali; UNI EN 1090 (esecuzione strutture metalliche, marcatura CE); D.M. 14/1/2008 revocato ma storicamente rilevante per opere esistenti.',
  'Definisci subito con il committente la planimetria dei carichi (scaffali, magazzino, celle frigo): un solaio pensato per 5 kN/m2 non regge il magazzino da 15. E controlla le tolleranze dei bicchieri prima del getto di completamento: recuperare un pilastro fuori piombo costa piu\u0300 del pilastro.'),

S('Involucro', 'Involucro del retail: facciate, vetrate, pensiline e ingressi',
  'L\u2019involucro commerciale ha tre anime: la facciata architettonica (immagine e brand, spesso in facciata continua o rivestimenti metallici/ventilati), le vetrate di ingresso e vetrina (trasparenza, sicurezza), e gli elementi funzionali (pensiline, portali, segni distintivi, chiusure tecniche). Deve rispondere a requisiti energetici, acustici, di sicurezza (vetri di sicurezza, evacuazione) e manutentivi: i materiali scelti per l\u2019effetto devono sopravvivere a trolley, pulizie e micro-atti vandalici.',
  'Facciate continue montanti-traversi o cellule (UNI EN 13830) con vetri camera basso-emissivi; facciate ventilate in lamiera, HPL, gres o alucobond-type (attenzione alla reazione al fuoco dei compositi: verificare classe e posa); vetrate di sicurezza secondo UNI 7697 (stratificato/temprato a seconda della posizione); porte automatiche scorrevoli e portali; pensiline in acciaio-vetro con scarichi dedicati; involucro opaco in pannelli coibentati o sistemi a secco con verifica termoigrometrica.',
  'Ingressi e court, vetrine di galleria, facciate esterne di ipermercati e retail park, rivestimenti dei volumi tecnici, pensiline di carico e pedonali.',
  'Facciata continua = velocita\u0300 di montaggio e prestazioni certificate; vetrine ampie supportano le vendite; sistemi ventilati proteggono la struttura e consentono rebranding con rifacimento limitato.',
  'Grand vetrate = problemi energetici e abbagliamento da governare (schermature, vetri selettivi); pannelli compositi con reazione al fuoco non idonea hanno causato disastri noti: la classe dei materiali va verificata in progetto e in cantiere; la sostituzione di lastre grandi e costosa e va prevista logisticamente.',
  'Ordini di grandezza indicativi: facciata continua vetrata 400-800 €/m2; facciata ventilata 180-400 €/m2; pensiline acciaio-vetro 600-1.200 €/m2; portali automatici 8-25 k€/cad.',
  'Caso tipo: restyling di un centro degli anni \u201990: si mantengono struttura e galleria e si sostituisce l\u2019involucro con facciata continua e lamiera microforata retroilluminata; il centro resta aperto con fasi notturne, nessuna interruzione delle vendite.',
  'UNI EN 13830 (facciate continue); UNI 7697 (criteri di sicurezza per vetri); UNI EN 13501-1 e decreti di classificazione (reazione al fuoco); D.Lgs 192/2005 (prestazione energetica involucro); NTC D.M. 17/1/2018 (azione vento su pensiline e facciate).',
  'Fai approvare i campioni veri (mock-up) prima dell\u2019ordine: il colore del pannello sul catalogo e quello in opera sono due materiali diversi. E prevedi i punti di ancoraggio per la manutenzione (binari, ganci): una facciata non manutenibile diventa brutta in cinque anni.'),

S('Impianti', 'Impianti HVAC e refrigerazione commerciale',
  'Il retail climatizza grandi volumi con ricambi elevati (porte sempre aperte, affollamento variabile) e, nei food, gestisce la refrigerazione dei banchi e delle celle: due mondi impiantistici distinti ma integrabili, con forte attenzione ai consumi (l\u2019energia e\u0300 tra le prime voci di costo gestionale) e alla qualita\u0300 dell\u2019aria.',
  'HVAC: unita\u0300 rooftop (packaged) o UTA con free cooling per gallerie e superfici vendita, laminazione con barriere d\u2019aria agli ingressi, recuperatori; refrigerazione food: centrali a CO2 transcritica con recupero di calore per ACS e post-riscaldamento, banchi chiusi con porte, telecontrollo fughe refrigerante; gestione BMS centralizzata con monitoraggio consumi e tariffe orarie.',
  'Supermercati e ipermercati (refrigerazione + comfort), gallerie commerciali (comfort e IAQ), food court (estrazione fumi di cucina con scrubber o precipitatori), palestre e cinema interni.',
  'CO2 transcritica = refrigerante naturale a basso GWP, conforme alla stretta F-gas; recupero di calore riduce caldaie; rooftop = manutenzione in copertura senza disturbare le vendite; BMS = diagnosi e risparmio continui.',
  'CO2 transcritica richiede frigoristi formati e componenti rated per alte pressioni (fino a ~90 bar lato gas cooler); il free cooling funziona solo con gestione entalpica ben regolata; le barriere d\u2019aria mal dimensionate fanno spifferi o consumi inutili.',
  'Ordini di grandezza indicativi: HVAC rooftop/UTA per superficie vendita 60-130 €/m2 serviti; centrale CO2 transcritica supermercato 2.000-4.000 m2: 300-700 k€; BMS centro commerciale 5-15 €/m2; recupero calore su ACS con payback spesso 3-6 anni.',
  'Caso tipo: supermercato che sostituisce centrale HFC con CO2 transcritica e banchi chiusi; il recupero di calore copre ACS e post-riscaldamento, i consumi elettrici complessivi calano di oltre il 20% e la carica di refrigerante fluorurato si azzera.',
  'Reg. (UE) 517/2014 e Reg. (UE) 2024/573 (gas fluorurati, divieti e quote); D.Lgs 192/2005 (requisiti impianti); UNI EN 378 (sicurezza impianti frigoriferi); D.Lgs 152/2006 (emissioni in atmosfera per cucine); norme CEI per la parte elettrica.',
  'Fai collaudare la CO2 da personale con abilitazione specifica e verifica i certificati delle saldature ad alta pressione: un giunto debole lato transcritico e\u0300 un rischio serio. E prevedi la telemetria fughe da subito: il registro F-gas e\u0300 obbligatorio e controllato.'),

S('Aree esterne', 'Aree esterne, parcheggi a raso e viabilità di contorno',
  'Nel retail le aree esterne sono parte del prodotto: parcheggi a raso capienti e leggibili, viabilita\u0300 di accesso e svincoli, percorsi pedonali protetti dai varchi alle gallerie, aree di carico separate dai flussi clienti, verde e mitigazione. La progettazione deve gestire picchi di traffico (weekend, promozioni), sicurezza pedonale e drenaggio di grandi superfici impermeabili.',
  'Parcheggi a raso con stalli 2,50x5,00 m, corsie e isole di manovra dimensionate per i picchi; pavimentazioni flessibili (conglomerato bituminoso) o rigide (cls) secondo traffico e carichi, con drenaggio e sistemi di prima pioggia; pensiline fotovoltaiche su campate di stallo; segnaletica orizzontale e verticale, illuminazione a LED con controllo; separazione netta tra rete pedonale e veicolare; opere di mitigazione viaria a carico del promotore (rotatorie, svincoli) spesso in convenzione.',
  'Centri commerciali e retail park (grandi parcheggi di superficie), supermercati di prossimita\u0300, drive-in e curbside pickup, piazzali di carico con dock.',
  'Parcheggio a raso = costo basso per posto e flessibilita\u0300 d\u2019uso; pensiline fotovoltaiche producono energia e ombra; buona viabilita\u0300 interna riduce incidenti e contenziosi.',
  'Grandi superfici impermeabili impongono opere idrauliche (vasche di laminazione, invarianza) costose; i parcheggi a raso consumano suolo e sono esposti a vincoli paesaggistici e di mitigazione; la manutenzione di bituminosi e segnaletica e\u0300 continua.',
  'Ordini di grandezza indicativi: parcheggio a raso completo (fondazione, pavimento, drenaggio, segnaletica) 35-70 €/m2, cioe\u0300 900-1.800 €/posto; pensilina fotovoltaica su stalli 1.500-2.500 €/posto (conta come impianto FV); vasca di laminazione 80-200 €/m3.',
  'Caso tipo: retail park con 1.400 posti a raso; la convenzione urbanistica finanzia una rotatoria e l\u2019attraversamento pedonale sopraelevato; le pensiline fotovoltaiche coprono il 30% dei consumi elettrici e fanno ombra estiva.',
  'L. 122/1989 e standard comunali/regionali per la dotazione (per il commerciale: standard regionali e comunali, da verificare); D.Lgs 285/1992 (viabilita\u0300); D.Lgs 152/2006 (acque, prima pioggia); D.M. 236/1989 (percorsi pedonali accessibili); rinvio a PARCHEGGI_AUTORIMESSE_PACK per geometria e dettagli.',
  'Separa fisicamente carichi e clienti: un dock che scarica nel flusso pedonale e\u0300 un incidente annunciato. E non risparmiare sul drenaggio del piazzale: l\u2019allagamento del parcheggio nel weekend di punta e\u0300 il peggior biglietto da visita possibile.'),

S('Retro-logistica', 'Retro-logistica, baie di carico e magazzino vendita',
  'Dietro la superficie vendita sta la macchina logistica: piazzali per mezzi pesanti, baie di carico con dock levellers, magazzino scorte, celle frigo, aree resi e rifiuti. Dimensionarla male vuol dire consegne lente, mezzi in manovra tra i clienti e costi operativi permanenti; dimensionarla bene e\u0300 invisibile al cliente ma decisiva per i margini.',
  'Piazzali in cls per mezzi fino a 44 t con raggi di manovra per autoarticolati; baie con pedane elettroidrauliche, portali sezionali coibentati e paracolpi; tunnel di carico isotermici per il fresco; magazzino con scaffalature e altezza utile 6-9 m; celle frigo positive e negative con pannelli e pavimenti coibentati; area rifiuti con compattatori e celle per organico; percorsi separati da quelli pedonali e recintati.',
  'Supermercati e ipermercati (fresco e secco), brico e DIY (carichi pesanti e lunghi), grandi magazzini con e-commerce interno (dark store), centri con raccolta centralizzata.',
  'Baie ben progettate = tempi di scarico dimezzati e meno danni; tunnel isotermici proteggono la catena del freddo; separazione flussi = sicurezza e assicurazioni piu\u0300 serene.',
  'Il piazzale cls costa piu\u0300 del bituminoso ma dura sotto i carrelli; le baie sono vincoli geometrici rigidi (altezze, pendenze max 10% di avvicinamento) che non si recuperano; sottodimensionare il magazzino sposta scorte in vendita e peggiora il negozio.',
  'Ordini di grandezza indicativi: piazzale cls per mezzi pesanti 60-100 €/m2; baia completa (pedana, portale, paracolpi, tunnel) 8-20 k€/cad.; cella frigo industriale 500-1.200 €/m3; compattatori e area rifiuti attrezzata 30-100 k€.',
  'Caso tipo: ipermercato con 8 baie di cui 2 isotermiche per il fresco; l\u2019avvicinamento in leggera contro-pendenza verso il dock e la pedana a scomparsa consentono lo scarico in 20 minuti per bilico; il magazzino a 7 m utili ospita le scorte promozionali.',
  'D.Lgs 81/2008 (luoghi di lavoro, movimentazione); UNI EN 349 e Direttiva Macchine 2006/42/CE (pedane e sicurezza); normativa igienico-sanitaria per celle e catena del freddo (HACCP); rinvio a EDILIZIA_INDUSTRIALE_LOGISTICA_PACK per magazzini e dock avanzati.',
  'Prova la manovra con l\u2019automezzo piu\u0300 grande previsto prima di gettare: le sagome di manovra su carta non bastano. E metti paracolpi seri e luci di segnalazione alle baie: il primo bilico distratto li ripaga tutti.'),

S('Titoli e agibilità', 'Titoli edilizi, agibilità e autorizzazioni di esercizio',
  'Un centro commerciale e\u0300 un incrocio di titoli: titolo edilizio per la costruzione, autorizzazione commerciale per il formato, agibilita\u0300 per l\u2019uso, SCIA antincendio per le attivita\u0300 soggette, pareri sanitari per food e benessere, insegne e pubblicita\u0300. Aprire senza uno di questi atti vuol dire sanzioni, chiusura o impossibilita\u0300 di contratti seri con i tenant.',
  'Sequenza tipica: autorizzazione commerciale (regionale o comunale secondo formato e legge regionale), PdC o SCIA edilizia coerente, collaudi statici e impianti, SCIA antincendio con esito dei controlli VVF, segnalazione certificata di agibilita\u0300, autorizzazioni sanitarie per somministrazione, comunicazioni per insegne; per i tenant: SCIA di subingresso o variazione, adeguamenti impiantistici certificati.',
  'Nuove costruzioni retail, ampliamenti, cambi di destinazione d\u2019uso verso commerciale, aperture e subingressi di negozi, food court e sale giochi.',
  'Sequenza corretta = apertura senza sorprese e finanziabilita\u0300; agibilita\u0300 e antincendio chiariscono responsabilita\u0300 tra gestore e tenant.',
  'Iter lunghi e non paralleli: un ritardo VVF blocca l\u2019apertura stagionale; il cambio destinazione d\u2019uso puo\u0300 richiedere standard e opere non previsti; ogni variante commerciale puo\u0300 richiedere adeguamento del titolo edilizio.',
  'Ordini di grandezza indicativi: pratiche autorizzative complesse per centro medio 50-200 k€ di parcelle tecniche; SCIA antincendio e aggiornamenti 3-15 k€; varianti in corso d\u2019opera con impatto autorizzativo possono costare mesi piu\u0300 che euro.',
  'Caso tipo: apertura di un retail park a novembre; la SCIA antincendio era stata depositata con un layout superato; il controllo VVF prescrive adeguamenti che slittano l\u2019apertura a febbraio: il danno commerciale supera di gran lunga il costo della pratica corretta.',
  'DPR 380/2001 (titoli edilizi, agibilita\u0300 art. 24, cambi destinazione art. 23-ter); D.Lgs 114/1998 e D.Lgs 59/2010 (autorizzazioni e SCIA commerciali); DPR 151/2011 (SCIA antincendio); normativa sanitaria regionale per somministrazione (da verificare); Codice della strada e norme pubblicita\u0300 per insegne.',
  'Tieni un cronoprogramma delle autorizzazioni separato da quello dei lavori: il cantiere finisce, le carte no. E fai firmare ai tenant un allegato tecnico che chiarisce chi fa cosa su impianti e pratiche del box.'),

S('Fit-out', 'Fit-out dei negozi e capitolari landlord/tenant',
  'Il gestore consegna i box in shell & core (o in grezzo avanzato) e il conduttore realizza il fit-out: pavimenti, controsoffitti, impianti dedicati, arredi, insegne interne. Il capitolato tecnico del landlord definisce cosa e\u0300 a carico di chi, le prestazioni minime (carichi, potenze, allacci, finiture proibite) e le procedure di approvazione dei progetti dei negozi: e\u0300 il documento che evita il contenzioso quotidiano.',
  'Capitolato tipico: carichi ammessi sui solai e pavimentazioni, potenze elettriche e allacci (contatori dedicati), punti di scarico idrici e grasso per food, limiti per canalizzazioni e attraversamenti della galleria, altezze e materiali delle vetrine e delle serrande, ore di lavoro consentite, regole antincendio per materiali e arredi, ripristino a fine contratto (exit).',
  'Tutti i centri commerciali e retail park gestiti unitariamente; vale anche per gallerie di stazioni e aeroporti e per gli shop-in-shop dei grandi magazzini.',
  'Capitolato chiaro = fit-out veloci e omogenei; ripartizione dei costi esplicita; tutela dell\u2019immagine complessiva e delle prestazioni degli impianti comuni.',
  'Capitolati troppo rigidi scoraggiano i tenant; la gestione delle approvazioni richiede un ufficio tecnico del gestore sempre attivo; i ripristini di fine contratto sono la prima causa di lite.',
  'Ordini di grandezza indicativi: fit-out negozio standard 400-900 €/m2; food e ristorazione con cucina 1.200-2.500 €/m2; contributo fit-out del landlord (ove previsto) 100-400 €/m2; redazione capitolato e gestione approvazioni 20-80 k€/centro.',
  'Caso tipo: centro che introduce un capitolato tecnico standard con template di progetto; i tempi medi di approvazione dei fit-out passano da 90 a 30 giorni e i lavori in galleria avvengono solo in fascia notturna concordata.',
  'Contratti di locazione commerciale (L. 392/1978) e clausole tecniche; regolamento di gestione del centro; norme antincendio e igieniche richiamate nel capitolato; D.Lgs 81/2008 per i lavori di fit-out in ambienti aperti al pubblico (DUVRI e coordinamento).',
  'Imponi sopralluogo congiunto a inizio e fine lavori con verbale fotografico: lo stato dei luoghi e\u0300 l\u2019unico modo di chiudere bene (e farsi pagare) il ripristino. E non far partire nessun fit-out senza approvazione scritta del progetto antincendio del box.'),

S('Riqualificazione', 'Riqualificazione e riconversione dei centri esistenti',
  'Molti centri commerciali di prima generazione sono obsoleti: format superati, involucri energetici pessimi, anchor fallite. La riqualificazione spazia dal restyling (facciate, galleria, servizi) alla riconversione funzionale (de-malling verso retail park, inserimento di sanita\u0300, logistica urbana, residenziale) fino alla demolizione parziale. E\u0300 il mercato in crescita piu\u0300 interessante del retail edilizio.',
  'Restyling: nuova facciata, rifacimento galleria (pavimenti, luci, servizi), efficientamento impianti e fotovoltaico; riconversione: riduzione GLA e introduzione di funzioni non retail (palestre, cliniche, uffici, dark store), con cambi di destinazione d\u2019uso e verifiche di standard; retrofit energetico: cappotto o ventilate, sostituzione gruppi frigo, BMS, pensiline fotovoltaiche.',
  'Centri degli anni \u201980-\u201990 da ripensare, ipermercati con eccesso di superficie, gallerie svuotate dall\u2019e-commerce, siti con vincoli che premiavano il riuso rispetto al nuovo.',
  'Il riuso conserva posizione, viabilita\u0300 e bacino gia\u0300 consolidati; spesso costa meno del nuovo e ha iter autorizzativi piu\u0300 rapidi; il mix di funzioni stabilizza i flussi oltre il weekend.',
  'Strutture datate impongono adeguamenti (sismico, antincendio, accessibilita\u0300) che possono mangiare il margine; i cambi di destinazione d\u2019uso incontrano vincoli di piano commerciale; la gestione del cantiere a centro aperto e\u0300 complessa e costosa.',
  'Ordini di grandezza indicativi: restyling inviluppo + galleria 300-700 €/m2 trattati; retrofit energetico profondo 150-400 €/m2; riconversione parziale con opere strutturali 800-1.500 €/m2 riconvertiti; sempre da confrontare col valore d\u2019uso, non col solo costo.',
  'Caso tipo: centro anni \u201990 con anchor dismessa: si riduce la galleria, si converte l\u2019anchor in polo sanitario e fitness, si rifanno facciata e copertura con fotovoltaico; il centro torna pieno con mix retail-servizi e canoni rivalutati.',
  'DPR 380/2001 (ristrutturazione, cambi destinazione d\u2019uso art. 23-ter); normativa antisismica per adeguamento/miglioramento (NTC D.M. 17/1/2018); normativa antincendio per le nuove attivita\u0300; D.Lgs 192/2005 e Direttiva (UE) 2024/1275 EPBD per il retrofit energetico.',
  'Prima di promettere una riconversione, fai la diagnosi vera: struttura, amianto eventuale, antincendio e destinazioni d\u2019uso esistenti. Il rilievo laser scan del centro esistente si ripaga evitando varianti ogni settimana.'),

S('Economia', 'Economia del retail: costi, canoni e redditività',
  'Il retail edilizio si giudica sulla redditivita\u0300 immobiliare: costo di sviluppo (area, costruzione, autorizzazioni, fit-out incentives), ricavi (canoni base + overage sul fatturato, service charge per spazi comuni) e valore finale (rendimento da locazione). Chi progetta deve sapere che ogni scelta tecnica (luci, impianti, manutenibilita\u0300) entra nel piano economico e nel canone sostenibile.',
  'Struttura dei costi per format: retail park shell 600-1.000 €/m2, centro commerciale con galleria 1.000-1.600 €/m2 di GLA complessiva (shell + comuni), fit-out a carico tenant con eventuale contributo landlord; service charge 15-40 €/m2/mese secondo servizi; canoni variabili per formato e posizione con overage 3-8% del fatturato oltre soglia; valutazione per capitalizzazione del reddito con yield di mercato (da verificare per piazza e momento).',
  'Studi di fattibilita\u0300 di nuovi sviluppi, negoziazioni con anchor e tenant, piani di riqualificazione, due diligence per compravendita di centri esistenti.',
  'Il modello shell & core ripartisce i costi tra gestore e tenant; gli overage allineano gli interessi; la manutenibilita\u0300 progettata abbassa le service charge e rende il centro competitivo.',
  'I costi delle parti comuni (galleria, parcheggi, impianti) sono tutti a carico del gestore e non producono canone diretto; i capex di medio periodo (coperture, facciate, impianti) sono sottovalutati nei piani; l\u2019e-commerce comprime i canoni dei format deboli.',
  'Ordini di grandezza indicativi: sviluppo retail park 10.000 m2 GLA: 8-15 M€ opere piu\u0300 area; centro commerciale 30.000 m2 GLA: 40-70 M€; due diligence tecnica per acquisizione 30-100 k€; piano capex decennale prudente 5-10 €/m2/anno.',
  'Caso tipo: acquisizione di un centro semivuoto; la due diligence tecnica quantifica in 6 M€ i capex necessari (copertura, impianti, facciata) e il piano di re-letting con nuovo mix riporta l\u2019occupancy sopra il 90% in tre anni.',
  'L. 392/1978 (locazioni commerciali); normativa contabile e fiscale per valorizzazioni (da verificare con il fiscalista); standard valutativi internazionali (RICS) per le perizie; nessun riferimento normativo edilizio specifico: e\u0300 materia economico-gestionale.',
  'Quando stimi un retail, non fermarti al costo di costruzione: chiedi sempre il piano service charge e il capex decennale. Un centro costruito a basso costo con impianti energivori e\u0300 un affare che si svaluta da solo.'),
]

def main():
    os.makedirs(os.path.join(ROOT, 'schede'), exist_ok=True)
    with open(os.path.join(ROOT, 'schede', 'schede.jsonl'), 'w', encoding='utf-8', newline='\n') as f:
        for d in SCHEDE:
            f.write(json.dumps(d, ensure_ascii=False) + '\n')

    course = f'''corso: "Edilizia retail e centri commerciali: formati e autorizzazioni (D.Lgs 114/1998), masterplan e tenant mix, antincendio grandi superfici (DPR 151/2011, D.M. 3/8/2015), strutture di grande luce, involucro e facciate, HVAC e refrigerazione CO2, aree esterne e parcheggi a raso, retro-logistica e baie, titoli edilizi e agibilita', fit-out e capitolari landlord/tenant, riqualificazione e riconversione, economia del retail"
facolta: "FACOLTA_TECNOLOGIA_E_COSTRUZIONE"
livello: "L1-L2"
schede: {len(SCHEDE)}
formato: "JSONL"
lingua: "it"
schema_campi: [categoria, nome, descrizione, tecnologia, applicazioni, vantaggi, limiti, costi_e_economia, casi_real_world, normative, note_cantiere]
fonti: "D.Lgs 114/1998, D.Lgs 59/2010, DPR 151/2011, D.M. 3/8/2015, UNI EN 12101, UNI EN 12845, UNI EN 13501-1, NTC D.M. 17/1/2018, UNI EN 1090, UNI EN 13830, UNI 7697, D.Lgs 192/2005, Reg. (UE) 517/2014 e 2024/573, UNI EN 378, DPR 380/2001, L. 392/1978, L. 122/1989, D.Lgs 81/2008, Direttiva (UE) 2024/1275 EPBD; standard regionali e comunali citati come da verificare"
nota_metodologica: "Corso tipologico sull'edilizia per il commercio: formati e quadro autorizzatorio (D.Lgs 114/1998, soglie regionali da verificare), masterplan e tenant mix (GLA, gallerie, anchor, dotazione parcheggi), antincendio grandi superfici (Codice, SEFC, sprinkler, EVAC), strutture di grande luce (prefabbricato c.a., capriate metalliche, pavimenti industriali), involucro (facciate continue, ventilate, vetri di sicurezza), impianti (rooftop, CO2 transcritica, F-gas, BMS), aree esterne (parcheggi a raso, drenaggio, pensiline FV, rinvio a PARCHEGGI_AUTORIMESSE_PACK), retro-logistica (dock, celle, rinvio a EDILIZIA_INDUSTRIALE_LOGISTICA_PACK), titoli e agibilita', fit-out e capitolari landlord/tenant, riqualificazione (restyling, de-malling, retrofit), economia (costi per format, canoni, service charge). NON ridondante: i soli titoli esistenti con 'retail/commerciale' sono ILLUMINAZIONE_TECNICA_PACK (illuminotecnica) e MASTER_DESIGN_PACK (retail design estetico); qui la progettazione edilizia, antincendio, strutturale, impiantistica, autorizzativa ed economica della tipologia. Norme solo di consolidata certezza; prezzi come fasce indicative; nessun nome di azienda."
'''
    with open(os.path.join(ROOT, 'COURSE.yaml'), 'w', encoding='utf-8', newline='\n') as f:
        f.write(course)

    readme = f'''# Edilizia retail e centri commerciali

Corso L1-L2 della Facolta di Tecnologia e Costruzione: la grande distribuzione e il commercio organizzato come tipologia edilizia completa — formati e quadro autorizzatorio (D.Lgs 114/1998, soglie regionali), masterplan, layout e tenant mix (GLA, gallerie, anchor, court), antincendio nelle grandi superfici aperte al pubblico (DPR 151/2011, Codice D.M. 3/8/2015, SEFC, sprinkler, EVAC), strutture di grande luce (prefabbricato in c.a., capriate metalliche, pavimenti industriali), involucro commerciale (facciate continue e ventilate, vetrate di sicurezza, pensiline), impianti HVAC e refrigerazione commerciale a CO2 (F-gas, recupero calore, BMS), aree esterne e parcheggi a raso (drenaggio, pensiline fotovoltaiche, viabilita'), retro-logistica e baie di carico, titoli edilizi, agibilita' e autorizzazioni di esercizio, fit-out dei negozi e capitolari landlord/tenant, riqualificazione e riconversione dei centri esistenti (restyling, de-malling, retrofit) ed economia del retail (costi per format, canoni, service charge, capex).

**Schede: {len(SCHEDE)}**

Non ridondante con ILLUMINAZIONE_TECNICA_PACK (progetto illuminotecnico), MASTER_DESIGN_PACK (retail design ed esperienza), EDILIZIA_INDUSTRIALE_LOGISTICA_PACK (magazzini, cui si rinvia per la logistica avanzata) e PARCHEGGI_AUTORIMESSE_PACK (geometria della sosta, cui si rinvia): qui la tipologia commerciale completa — autorizzativa, strutturale, antincendio, impiantistica ed economica — assente altrove.
'''
    with open(os.path.join(ROOT, 'README.md'), 'w', encoding='utf-8', newline='\n') as f:
        f.write(readme)

    # self-check
    for d in SCHEDE:
        assert list(d.keys()) == K
        s = json.dumps(d, ensure_ascii=False)
        assert 'aplicazioni' not in s and 'tegnologia' not in s
    print('OK', PACK, len(SCHEDE), 'schede')

if __name__ == '__main__':
    main()
