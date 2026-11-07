# -*- coding: utf-8 -*-
"""Giro AS: genera UFFICI_E_TERZIARIO_PACK (12 schede)."""
import json, os

PACK = 'UFFICI_E_TERZIARIO_PACK'
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

S('Normativa', 'Requisiti igienico-edilizi dei luoghi di lavoro in ufficio',
  'Gli uffici sono luoghi di lavoro: oltre al titolo edilizio devono rispettare i requisiti igienico-edilizi della normativa sulla sicurezza del lavoro (altezze, superfici e volumi per addetto, aerazione e illuminazione naturale ove possibile, microclima, servizi igienici) e i regolamenti edilizi e di igiene locali. Chi converte un immobile a ufficio deve verificare questi parametri prima del contratto di locazione: un open space che non li rispetta non e\u0300 sanabile con l\u2019arredamento.',
  'Riferimenti: D.Lgs 81/2008 Titolo II con allegato IV (requisiti dei luoghi di lavoro: altezze minime, superfici e volumi per addetto, aerazione, microclima; i valori puntuali vanno verificati nel testo vigente perche\u0300 aggiornati), DPR 303/1956 (norme generali di igiene del lavoro, storico riferimento per gli uffici), regolamenti comunali di igiene (altezze minime abitabili, rapporti aeroilluminanti); per le destinazioni d\u2019uso, la classificazione urbanistica locale e i requisiti di agibilita\u0300 (DPR 380/2001).',
  'Nuove costruzioni terziarie, cambi di destinazione d\u2019uso verso uffici, fit-out con aumento del numero di postazioni, verifiche pre-contrattuali (due diligence).',
  'Parametri chiari e verificabili in fase di rilievo; la conformita\u0300 igienico-edilizia e\u0300 anche argomento contrattuale (garanzie del locatore); previene prescrizioni ASL e contenziosi.',
  'Negli edifici esistenti altezze e rapporti aeroilluminanti sono spesso insufficienti e non sanabili; i regolamenti locali differiscono tra comuni; la conversione di immobili industriali a ufficio richiede attenzione particolare ai requisiti.',
  'Ordini di grandezza indicativi: verifica di conformita\u0300 con rilievo 2-8 k€; pratica di cambio destinazione d\u2019uso con adeguamenti 10-60 k€ di parcelle piu\u0300 opere.',
  'Caso tipo: conversione di un ex deposito in uffici: il rilievo mostra altezza 2,55 m sotto travi: il progetto ridistribuisce le postazioni nelle campate piu\u0300 alte e destina le zone basse ad archivio e servizi, ottenendo l\u2019agibilita\u0300.',
  'D.Lgs 81/2008 (Titolo II e allegato IV, valori da verificare nel testo vigente); DPR 303/1956 (igiene del lavoro); DPR 380/2001 (titoli e agibilita\u0300); regolamenti edilizi e di igiene comunali (da verificare).',
  'Prima di firmare qualsiasi locazione per uffici, misura: altezze libere sotto travi e controsoffitti, rapporti finestra/pavimento, numero di servizi. Il bello dell\u2019open space passa, la prescrizione ASL resta.'),

S('Ergonomia', 'Postazioni di lavoro al videoterminale ed ergonomia',
  'La postazione al videoterminale e\u0300 la cellula base dell\u2019ufficio moderno: la normativa fissa requisiti per schermo, tastiera, piano di lavoro, seduta, spazio per le gambe, illuminamento e pause di lavoro. L\u2019ergonomia corretta riduce disturbi muscolo-scheletrici e affaticamento visivo: e\u0300 obbligo di legge e produttivita\u0300, non comfort accessorio.',
  'Requisiti: schermo posizionabile (inclinazione, altezza, senza riflessi), tastiera dissociata e inclinabile, piano con spazio frontale per gli avambracci, seduta regolabile in altezza e con schienale regolabile, poggiapiedi se serve, illuminamento tipico 500 lux sul piano per lavoro al videoterminale con abbagliamento controllato (UGR limitato secondo UNI EN 12464-1), spazio minimo per addetto e percorrenze; per i lavoratori VDT: definizione (uso sistematico almeno 20 ore settimanali), sorveglianza sanitaria e pause (15 minuti ogni 120 di applicazione continuativa secondo D.Lgs 81/2008).',
  'Progettazione di nuove postazioni, verifica di open space esistenti, acquisto di arredi tecnici, valutazione dei rischi (DVR) per uffici.',
  'Postazioni conformi riducono assenze e reclami; l\u2019arredo regolabile serve utenti diversi (hot desking); i requisiti VDT sono oggettivi e documentabili nel DVR.',
  'L\u2019hot desking senza regolazioni rapide vanifica l\u2019ergonomia; gli arredi estetici non regolabili sono il primo vizio degli uffici di rappresentanza; il controllo dei riflessi richiede scelte di illuminazione e finitura coordinate.',
  'Ordini di grandezza indicativi: postazione completa conforme (piano, seduta ergonomica, supporti) 800-2.500 €/posto; seduta operativa di qualita\u0300 300-900 €; consulenza ergonomica per ufficio medio 3-10 k€.',
  'Caso tipo: ufficio di 120 postazioni con mal di schiena ricorrenti: audit ergonomico, sostituzione delle sedute, bracci porta-monitor e riposizionamento rispetto alle finestre: i reclami calano dell\u201980% in sei mesi.',
  'D.Lgs 81/2008 (Titolo VII videoterminali e Titolo VI movimentazione); UNI EN 12464-1 (illuminazione luoghi di lavoro); norma UNI sulle postazioni VDT (da verificare nelle parti applicabili).',
  'Quando collaudi un ufficio, siediti a una postazione vera per un\u2019ora con lo schermo acceso contro finestra: riflessi, abbagliamento e posture sbagliate saltano fuori subito. Le schede tecniche degli arredi non bastano.'),

S('Workplace', 'Tipologie di workplace: cell office, open space, activity-based',
  'Il layout degli uffici e\u0300 cambiato: dall\u2019ufficio chiuso (cell office) all\u2019open space, fino all\u2019activity-based working (postazioni non assegnate, zone per focus, collaborazione, riunioni, phone booth) accelerato dal lavoro agile. Ogni modello ha esigenze edilizie e impiantistiche diverse: densita\u0300 di occupazione, acustica, ricambi d\u2019aria, prese e reti. Il progetto deve seguire il modello organizzativo del committente, non una moda.',
  'Parametri: densita\u0300 tipica 8-15 m2 lordi/posto secondo modello (cell office piu\u0300 alto, desk sharing piu\u0300 basso); zone: focus, collaborazione, meeting room piccole e grandi, phone booth acustiche, break e caffetteria, reception e sale clienti; requisiti acustici differenziati (ISO 3382-3 per gli open plan); infrastrutture: prese a pavimento o soffitto, reti Wi-Fi dense, armadietti personali per l\u2019hot desking; prenotazione postazioni e sale con sensori di occupazione.',
  'Fit-out di nuovi uffici, riorganizzazione post-smart working, sedi direzionali multi-tenant, uffici pubblici in riqualificazione.',
  'L\u2019activity-based riduce i metri quadrati per addetto (con il lavoro ibrido) e aumenta la qualita\u0300 degli spazi; le zone acustiche dedicate proteggono il lavoro concentrato; i dati dei sensori guidano le scelte di spazio.',
  'Open space mal progettati (densita\u0300 alta, acustica assente) sono la prima causa di insoddisfazione; l\u2019hot desking richiede pulizia e gestione; la riduzione delle scrivanie senza cambio culturale crea conflitti.',
  'Ordini di grandezza indicativi: phone booth acustica 5-15 k€/cad.; sensore occupazione e prenotazione 100-300 €/posto; riorganizzazione layout con partizioni 150-400 €/m2 trattati.',
  'Caso tipo: direzione che passa da 400 scrivanie assegnate a 280 postazioni activity-based con 30% di lavoro agile: liberati 1.200 m2, la sede assorbe un\u2019altra direzione e l\u2019affitto del piano liberato copre il progetto.',
  'L. 81/2017 (lavoro agile); D.Lgs 81/2008 (requisiti luoghi di lavoro); ISO 3382-3 (acustica open plan); contratti collettivi e accordi aziendali per il lavoro ibrido (da verificare).',
  'Non progettare mai la densita\u0300 sul numero di dipendenti: progetta sui picchi di presenza reale (il martedi\u0300-giovedi\u0300 dell\u2019ufficio ibrido). E l\u2019acustica delle zone focus va provata a ufficio pieno, non a cantiere vuoto.'),

S('Comfort', 'Comfort termoigrometrico e acustico negli uffici',
  'Il comfort negli uffici ha due fronti misurabili: microclima (temperatura, umidita\u0300, velocita\u0300 dell\u2019aria, asimmetrie radianti) e acustica (rumore di fondo, distrazione del parlato, privacy). Entrambi incidono su produttivita\u0300 e salute e sono regolati da norme di riferimento: il progetto impiantistico e di partizione deve portare i valori dentro le fasce, non solo \u2018fare aria\u2019.',
  'Microclima: condizioni invernali ed estivali secondo UNI EN ISO 7730 (categorie A/B/C), velocita\u0300 dell\u2019aria contenuta (tipicamente sotto 0,15-0,25 m/s secondo stagione e categoria), controllo delle asimmetrie (finestre fredde, soffitti radianti); acustica: ISO 3382-3 per open plan (parametri di distrazione e privacy), livelli di rumore degli impianti contenuti (NR orientativamente 30-40 secondo funzione), partizioni con isolamento e soffitti assorbenti, phone booth e sale riunioni con pareti adeguate.',
  'Progetto impianti e partizioni di nuovi uffici, diagnosi di reclami (troppo caldo/freddo, troppo rumore), retrofit di open space, misurazioni post-operatorie.',
  'Il comfort misurato chiude i reclami con i numeri; le categorie ISO consentono di contrattualizzare la prestazione; l\u2019acustica open space ben progettata sostiene davvero la concentrazione.',
  'I sistemi ad aria ad alta velocita\u0300 generano spifferi e reclami; l\u2019open space profondo con soffitto riflettente e\u0300 acusticamente ingestibile; la privacy del parlato richiede distanza, assorbimento e mascheramento sonoro insieme.',
  'Ordini di grandezza indicativi: misurazione comfort (microclima + acustica) su piano tipo 5-20 k€; controsoffitto acustico di qualita\u0300 60-120 €/m2; parete divisoria con prestazione acustica 250-500 €/m.',
  'Caso tipo: open space con 40 reclami/anno: sondaggi di soddisfazione e misurazioni mostrano soffitto riflettente e velocita\u0300 d\u2019aria doppia del limite; nuovo controsoffitto assorbente e ritaratura delle bocchette chiudono la vertenza.',
  'UNI EN ISO 7730 (microclima); ISO 3382-3 (acustica open plan); D.Lgs 81/2008 allegato IV (microclima e rumore nei luoghi di lavoro); rinvio a ACUSTICA_EDILIZIA_PACK e DIMENSIONAMENTO_TERMOTECNICO_PACK.',
  'I reclami di comfort si risolvono con le misurazioni, non con le opinioni: data logger di temperatura e fonometro per una settimana valgono piu\u0300 di dieci riunioni. E ricorda: il soffitto e\u0300 la prima superficie acustica dell\u2019open space.'),

S('Illuminazione', 'Illuminazione degli uffici: luce naturale e artificiale',
  'La luce negli uffici e\u0300 requisito di legge e leva di qualita\u0300: illuminamento adeguato sulle postazioni, controllo dell\u2019abbagliamento (specialmente con videoterminali), resa cromatica, integrazione con la luce naturale che la normativa privilegia ove possibile. Il progetto illuminotecnico coordina finestre, schermature, corpi illuminanti e domotica: sbagliarlo vuol dire affaticamento visivo e reclami quotidiani.',
  'Parametri: illuminamento tipico 500 lux sul piano di lavoro per scrittura/VDT (UNI EN 12464-1), UGR limitato (tipicamente <19 per lavoro al videoterminale), resa cromatica Ra >= 80; luce naturale: la normativa sui luoghi di lavoro richiede, ove possibile, luce naturale con schermature; corpi illuminanti a LED con ottiche a basso abbagliamento, regolazione DALI per zone, sensori di presenza e luce diurna; manutenzione programmata (flusso residuo).',
  'Nuovi uffici, rifacimento impianti luce a LED, retrofit con domotica, verifica di conformita\u0300 su postazioni esistenti.',
  'Il LED ben progettato dimezza i consumi e migliora la qualita\u0300; la regolazione su luce naturale sfrutta le facciate; i valori normativi danno un contratto oggettivo con il committente.',
  'Gli apparecchi economici senza controllo UGR producono abbagliamento a schermo; la luce naturale non schermata e\u0300 peggio della sua assenza (riflessi, surriscaldamento); la domotica mal configurata fa spegnere le luci sulla testa delle persone.',
  'Ordini di grandezza indicativi: impianto luce LED con regolazione per piano tipo 25-60 €/m2; schermature solari interne/esterne 80-250 €/m2 di finestra; progetto illuminotecnico con verifica di campo 3-10 k€.',
  'Caso tipo: retrofit LED di una sede anni \u201990 con apparecchi UGR<19, sensori luce diurna e scenari: i consumi luce calano del 55% e i reclami di affaticamento visivo si azzerano.',
  'UNI EN 12464-1 (illuminazione luoghi di lavoro indoor); D.Lgs 81/2008 allegato IV (illuminazione); rinvio a ILLUMINAZIONE_TECNICA_PACK per il progetto completo.',
  'Verifica l\u2019abbagliamento con i monitor veri accesi nelle ore critiche (mattina con sole basso): il calcolo illuminotecnico non vede lo schermo. E configura i sensori con gli utenti presenti: il ritardo di spegnimento sbagliato fa disattivare tutto.'),

S('Torri direzionali', 'Torri direzionali: struttura, core e facciata',
  'La torre direzionale e\u0300 la tipologia simbolo del terziario: piani liberi (free plan) attorno a un nucleo centrale di servizi (core), struttura a maglia regolare, facciata continua vetrata, impianti centralizzati a piani. Il progetto bilancia flessibilita\u0300 degli affitti (pochi pilastri, plant flessibili), efficienza (rapporto core/superficie) e prestazione energetica della facciata: le scelte strutturali condizionano il valore immobiliare per decenni.',
  'Parametri: maglia strutturale tipica 7,5-9 m (compatibile col parcheggio interrato sottostante), interpiano 3,60-4,20 m lordo per ospitare pavimento sopraelevato e controsoffitto tecnico; core con ascensori, scale, servizi e vani impianto, rapporto core/piano orientativamente 15-25%; facciata continua a cellule o montanti-traversi (UNI EN 13830) con vetri selettivi e schermature; strutture in c.a. o acciaio, verifiche sismiche e di vento per edifici alti; copertura tecnica con centrali e gruppi.',
  'Nuove torri direzionali, riqualificazione di torri esistenti (facciate e impianti), conversione di edifici industriali in terziario verticale, valutazioni di acquisto (due diligence tecnica).',
  'Il free plan con core centrale massimizza l\u2019affittabilita\u0300 multi-tenant; la facciata a cellule industrializza la posa e consente sostituzioni puntuali; l\u2019interpiano generoso assorbe ogni futura riconfigurazione impiantistica.',
  'La facciata vetrata e\u0300 il punto critico energetico e acustico: schermature e vetri selettivi non sono optional; il core sovradimensionato mangia superficie affittabile; gli edifici alti concentrano costi di esercizio (ascensori, pressurizzazione, manutenzione facciata).',
  'Ordini di grandezza indicativi: costruzione torre direzionale 1.800-3.000 €/m2 di superficie lorda; facciata continua performante 450-900 €/m2; riqualificazione facciata+impianti di torre esistente 400-800 €/m2.',
  'Caso tipo: riqualificazione di torre anni \u201970: sostituzione della facciata con cellule a doppia pelle selettiva, nuove centrali e ascensori a destinazione: la classe energetica sale di tre livelli e i canoni tornano al top di mercato.',
  'NTC D.M. 17/1/2018 (vento su edifici alti, sisma); UNI EN 13830 (facciate continue); D.Lgs 192/2005 (prestazione energetica); D.Lgs 81/2008 (luoghi di lavoro); normativa ascensori (rinvio a ASCENSORI_E_MOVIMENTAZIONE_VERTICALE_PACK).',
  'In una torre controlla subito tre cose: altezza libera del piano tipo, rapporto core/piano e stato della facciata. Sono i tre numeri che decidono se l\u2019edificio ha futuro o solo passato.'),

S('Impianti e flessibilità', 'Impianti per uffici: flessibilità e tecnologie',
  'L\u2019impianto degli uffici vive di riconfigurazioni: i tenant cambiano, le postazioni si spostano, i carichi crescono. Le tecnologie chiave sono il pavimento sopraelevato (distribuzione elettrica e dati accessibile), i controsoffitti tecnici (impianti ispezionabili), i sistemi di climatizzazione zonizzabili (VAV, fan coil, travi fredde) e il BMS che governa tutto: la flessibilita\u0300 impiantistica e\u0300 la prima forma di valore per chi affitta.',
  'Tecnologie: pavimento sopraelevato 15-60 cm con pannelli smontabili e passaggi certificati; controsoffitto tecnico ispezionabile; climatizzazione: VAV (portata variabile) per grandi piani, fan coil a 4 tubi per flessibilita\u0300, travi fredde (chilled beam) per comfort silenzioso con ventilazione primaria; illuminazione DALI; cablaggio strutturato Cat 6A e dorsali in fibra; BMS con regolazione per zone e telegestione; ricambi d\u2019aria dimensionati sulla densita\u0300 reale.',
  'Nuovi edifici terziari, riqualificazione impiantistica di sedi esistenti, fit-out multi-tenant, adeguamento a densita\u0300 variabili post-ibrido.',
  'Il pavimento sopraelevato rende ogni riconfigurazione un lavoro di ore, non di settimane; la zonizzazione riduce i consumi nei piani a mezzo servizio; il BMS documenta la prestazione (utile per certificazioni e contratti).',
  'Il pavimento sopraelevato richiede interpiano e attenzione ai carichi; le travi fredde esigono controllo dell\u2019umidita\u0300 (condensa) e manutenzione; il BMS senza manutenzione diventa un soprammobile costoso.',
  'Ordini di grandezza indicativi: pavimento sopraelevato 40-90 €/m2; climatizzazione VAV per piano tipo 100-180 €/m2; travi fredde con ventilazione primaria 130-220 €/m2; BMS 5-15 €/m2.',
  'Caso tipo: sede multi-tenant con pavimento sopraelevato e VAV: i tre subaffitti dell\u2019ultimo biennio sono stati riconfigurati in un weekend ciascuno, senza opere murarie e con la climatizzazione riadattata dal BMS.',
  'CEI 64-8 (impianti elettrici); normativa sul cablaggio strutturato (serie ISO/IEC 11801); D.Lgs 192/2005 (requisiti impianti); D.Lgs 81/2008 (microclima); rinvio a IMPIANTI_COMPLETA_PACK.',
  'Pretendi le mappe dei passaggi sotto il pavimento sopraelevato aggiornate a ogni variante: tra cinque anni nessuno ricordera\u0300 dove passano i cavi. E metti i plenum di ispezione dove servono davvero, non dove comodo al disegnatore.'),

S('Fit-out', 'Fit-out degli uffici: Cat A, Cat B e capitolari',
  'Il mercato distingue la consegna shell & core, il Cat A (spazi base: pavimento sopraelevato, controsoffitto, impianti al piano, servizi finiti) e il Cat B (fit-out del tenant: partizioni, arredi, sale riunioni, brand, cablaggio). La distinzione contrattuale dei livelli di finitura evita il contenzioso piu\u0300 frequente del terziario: chi consegna cosa, a quali prestazioni e con quali ripristini a fine locazione.',
  'Capitolato tipo: Cat A con specifiche di prestazione (carichi pavimento sopraelevato, portate impianti per postazione, livelli luce, acustica di base), Cat B a carico tenant con regole del landlord (attraversamenti, appendici, ore di lavoro, materiali ammessi), ripristino a fine locazione (reinstatement) definito in contratto; collaudi impiantistici e certificazioni (DVR del tenant, prevenzione incendi se varia la distribuzione).',
  'Locazioni direzionali nuove ed esistenti, subentri di tenant, ristrutturazioni di piani, accordi quadro multi-sede.',
  'Livelli di consegna chiari accelerano le trattative e riducono i lavori inutili; il tenant progetta solo il proprio strato; il landlord protegge l\u2019asset con regole uniformi.',
  'Il Cat A senza specifiche di prestazione genera aspettative sbagliate; il ripristino a fine locazione e\u0300 la voce piu\u0300 litigata (chi paga la rimozione del fit-out); i lavori del tenant in edificio occupato richiedono coordinamento e permessi.',
  'Ordini di grandezza indicativi: Cat A 250-500 €/m2 (se non incluso nel core); Cat B ufficio standard 500-1.000 €/m2, direzionale 1.000-2.000 €/m2; ripristino 50-150 €/m2.',
  'Caso tipo: grande sede multi-tenant che adotta un capitolato Cat A/B standard con matrice delle responsabilita\u0300 e template di reinstatement: i tempi medi di subentro passano da 9 a 5 mesi e le liti di fine locazione si dimezzano.',
  'Contratti di locazione e capitolari (materia privatistica); D.Lgs 81/2008 (DUVRI per i lavori del tenant); DPR 151/2011 e prevenzione incendi per le variazioni di layout (verificare la classificazione dell\u2019attivita\u0300); DPR 380/2001 per eventuali titoli.',
  'Fai firmare il verbale di consegna con foto e stato impianti, metro alla mano: il ripristino tra sei anni si decide oggi. E prima del fit-out verifica portate elettriche e frigorifere residue del piano: il Cat B che scopre i limiti del Cat A paga due volte.'),

S('Sostenibilità', 'Certificazioni di sostenibilità: LEED, BREEAM, WELL',
  'Le certificazioni volontarie di sostenibilita\u0300 e benessere (LEED, BREEAM, WELL e simili) sono diventate linguaggio di mercato del terziario: classificano energia, acqua, materiali, qualita\u0300 indoor, trasporti e gestione, e influenzano canoni, finanziabilita\u0300 e attrattivita\u0300 per i tenant. Per il progettista sono protocolli prestazionali con crediti verificabili: si progettano, si documentano e si collaudano, non si dichiarano.',
  'Meccanismo: protocolli a crediti con livelli (base/silver/gold/platinum secondo schema), requisiti prerequisito e crediti a scelta; temi: energia (modellazione e misurazione), qualita\u0300 dell\u2019aria (materiali a basse emissioni, monitoraggio), luce e vista, acqua, materiali e ciclo di vita, gestione del cantiere sostenibile; processo: integrazione in progettazione, documentazione in costruzione, verifica e commissioning, monitoraggio in esercizio (le certificazioni in-use misurano le prestazioni reali).',
  'Nuove sedi direzionali, riqualificazioni di edifici esistenti, richieste di tenant corporate, accesso a finanziamenti vincolati a criteri ESG.',
  'Le certificazioni danno un contratto prestazionale oggettivo tra sviluppatore, tenant e finanziatore; il commissioning obbligato migliora davvero gli impianti; il mercato premia gli edifici certificati in locazione e in vendita.',
  'Costi di processo e documentazione non banali; il rischio \u2018paper certification\u2019 (punteggio senza prestazione reale) e\u0300 noto: servono misurazioni in esercizio; i requisiti evolvono e la certificazione ha scadenza (specie in-use).',
  'Ordini di grandezza indicativi: processo di certificazione per edificio medio (fee consulenza + registrazione + commissioning) 80-250 k€; sovracosto costruttivo tipico 2-8% secondo livello; monitoraggio in esercizio 10-30 k€/anno.',
  'Caso tipo: riqualificazione di sede con certificazione oro: il protocollo guida le scelte (materiali a basse emissioni, monitoraggio CO2, commissioning): l\u2019edificio attrae un tenant corporate con locazione lunga che ripaga il sovracosto.',
  'Protocolli volontari LEED/BREEAM/WELL (schemi privati, da verificare nelle versioni vigenti); Direttiva (UE) 2024/1275 EPBD (quadro europeo di prestazione); tassonomia UE delle attivita\u0300 sostenibili per i finanziamenti (da verificare).',
  'Non vendere mai la certificazione come bollino: costruisci la documentazione durante il cantiere (foto, certificati materiali, collaudi), non dopo. E metti nel contratto di gestione il monitoraggio: il livello si perde in esercizio, non in fase di progetto.'),

S('Retrofit', 'Retrofit e riconversione del patrimonio terziario',
  'Gran parte del patrimonio uffici italiano e\u0300 obsoleto: classi energetiche basse, impianti al limite, layout rigidi. Il retrofit spazia dall\u2019efficientamento (facciata, impianti, BMS) alla riconversione funzionale (ufficio-residenza, ufficio-hotel, ufficio-servizi) fino alla demolizione e ricostruzione. La domanda ibrida ha polarizzato il mercato: gli edifici migliori si affittano, gli altri restano vuoti: il retrofit decide da che parte stare.',
  'Strategie: diagnosi energetica e rilievo (anche laser scan), retrofit dell\u2019involucro (facciata nuova o overcladding, copertura), sostituzione centrali con pompe di calore e rinnovabili, BMS e contabilizzazione, rifacimento servizi e hall (prima impressione), certificazione di risultato; riconversione: verifica di fattibilita\u0300 urbanistica (destinazioni, standard), strutturale (carichi, luci) e igienico-edilizia (altezze, aeroilluminazione) per il nuovo uso; le conversioni ufficio-residenza seguono normative regionali specifiche (da verificare).',
  'Edifici terziari anni \u201960-\u201990, sedi dismesse di grandi aziende e PA, conversioni in centri urbani, riposizionamento di asset immobiliari.',
  'Il retrofit conserva posizione e struttura e costa meno del nuovo a parita\u0300 di prodotto; le conversioni assorbono il surplus di uffici obsoleti; gli incentivi energetici (ove applicabili) migliorano i ritorni.',
  'Vincoli geometrici (altezze, luci, maglia) possono impedire la conversione; l\u2019amianto e i materiali datati sono la sorpresa abituale; il retrofit profondo con edificio occupato moltiplica tempi e costi di cantiere.',
  'Ordini di grandezza indicativi: retrofit energetico-impiantistico profondo 400-900 €/m2; conversione ufficio-residenza 1.000-1.800 €/m2; demolizione e ricostruzione terziario 1.800-3.000 €/m2.',
  'Caso tipo: ex sede aziendale degli anni \u201970 convertita a residenze: la maglia regolare e l\u2019altezza sufficiente consentono appartamenti con balconi ricavati nel passo della facciata; il core diventa distribuzione comune; l\u2019operazione si chiude in 30 mesi.',
  'DPR 380/2001 (cambi di destinazione d\u2019uso, art. 23-ter); leggi regionali sulle conversioni (da verificare); D.Lgs 192/2005 e Direttiva (UE) 2024/1275 EPBD (retrofit energetico); D.Lgs 42/2004 ove vincolato; normativa amianto (L. 257/1992).',
  'Prima di comprare un ufficio da convertire, fai tre verifiche: altezza libera, profondita\u0300 del piano (la luce naturale arriva a 5-6 m dalla finestra) e stato delle facciate. Se una delle tre non torna, il business plan non torna.'),

S('Sicurezza ed emergenza', 'Sicurezza, emergenza ed evacuazione negli edifici per uffici',
  'L\u2019edificio per uffici e\u0300 un luogo di lavoro con pubblico: il datore di lavoro deve valutare i rischi (DVR), designare addetti alle emergenze e al primo soccorso, predisporre il piano di emergenza ed evacuazione e mantenerlo efficace con prove periodiche. In edifici multi-tenant e con appalti in esercizio (pulizie, manutenzioni, lavori) il coordinamento documentale (DUVRI) e\u0300 la regola: la sicurezza degli uffici si gioca piu\u0300 sulla gestione che sulle opere.',
  'Elementi: DVR aggiornato alle postazioni reali (anche lavoro ibrido), piano di emergenza con planimetrie di esodo, addetti antincendio e primo soccorso in numero proporzionato alle presenze, prove di evacuazione almeno annuali con verbale, estintori e presidi con manutenzione programmata, illuminazione di emergenza e segnaletica, controllo accessi e registrazione visitatori (anche per l\u2019emergenza: sapere chi e\u0300 dentro), gestione degli appalti in sede con DUVRI e permessi di lavoro.',
  'Ogni edificio per uffici in esercizio, sedi multi-tenant, torri direzionali con gestione centralizzata, cantieri di fit-out in edifici occupati.',
  'Le prove periodiche mantengono reale il piano (le persone ricordano la strada); il coordinamento documentale tra tenant e fornitori chiarisce le responsabilita\u0300; il controllo accessi moderno fornisce la lista presenze utile in emergenza.',
  'Nei multi-tenant la responsabilita\u0300 si frammenta e i piani restano disallineati; le prove di evacuazione vissute come perdita di tempo degradano la preparazione; i presidi senza manutenzione (estintori scaduti, porte tagliafuoco bloccate) sono il rilievo piu\u0300 frequente.',
  'Ordini di grandezza indicativi: redazione/aggiornamento DVR per sede media 1-5 k€; piano di emergenza con planimetrie 1-4 k€; formazione addetti per sede media 2-8 k€/ciclo; manutenzione presidi antincendio 2-10 €/estintore/anno.',
  'Caso tipo: torre multi-tenant che unifica il piano di emergenza con coordinatore unico, prove semestrali congiunte e lista presenze da controllo accessi: l\u2019ultima verifica ispettiva si chiude senza rilievi.',
  'D.Lgs 81/2008 (Titolo I: DVR, designazioni, formazione; Titolo III: presidi; decreti sugli addetti emergenze e primo soccorso); DPR 151/2011 per le attivita\u0300 soggette (verificare la classificazione); D.M. 3/8/2015 (Codice prevenzione incendi).',
  'Controlla tre cose a ogni sopralluogo: porte tagliafuoco chiuse e libere, estintori in data, planimetrie di esodo affisse e aggiornate al layout reale. Sono i tre rilievi che costano meno prevenirli e di piu\u0300 spiegarli dopo.'),

S('Economia', 'Economia del terziario: canoni, costi e valore',
  'Il valore degli uffici si legge con i numeri: canone per metro quadrato, service charge, capex programmati, costi di fit-out e di locazione (rent free, contributi), tasso di sfitto e valore di capitalizzazione. Il tecnico che progetta o valuta deve conoscere questa grammatica: la qualita\u0300 edilizia (classe energetica, comfort, flessibilita\u0300) e\u0300 oggi direttamente prezzata dal mercato.',
  'Voci: canoni di mercato per classe di edificio (grade A/B/C) e piazza (fortemente variabili, da verificare su osservatori e banche dati); service charge 20-50 €/m2/anno secondo servizi; capex di mantenimento 5-15 €/m2/anno; condizioni di locazione: rent free 1-3 mesi/anno di durata, contributi fit-out; valutazione: reddito netto capitalizzato con yield di mercato, sensibilita\u0300 alla durata contrattuale e al merito del tenant; rischio obsolescenza (edifici non conformi ESG con sconto crescente).',
  'Studi di fattibilita\u0300 di sviluppi terziari, due diligence di acquisto, piani di riposizionamento, negoziazioni di locazione con supporto tecnico.',
  'La grammatica economica allinea progetto e investimento; la qualita\u0300 edilizia misurabile (certificazioni, classi) difende il valore; i piani capex evitano il degrado competitivo progressivo.',
  'La domanda ibrida ha alzato il rischio di sfitto sugli edifici medi; i costi di esercizio crescenti (energia, manutenzione) erodono i margini; le conversioni richiedono capitali pazienti e iter urbanistici.',
  'Ordini di grandezza indicativi: sviluppo terziario nuovo 1.800-3.000 €/m2; due diligence tecnica per acquisizione 20-80 k€; piano capex decennale per sede media 1-3 M€.',
  'Caso tipo: fondo che acquisisce una sede anni \u201880 sotto prezzo: la due diligence quantifica il retrofit (facciata, impianti, hall) e il piano di certificazione; a lavori finiti il canone riparte al top di zona e l\u2019asset si rivaluta.',
  'Standard valutativi (IVS, RICS; banche dati e osservatori immobiliari, da verificare); normativa contabile e fiscale per le valorizzazioni (con il fiscalista); tassonomia UE ESG per l\u2019accesso ai capitali (da verificare).',
  'Quando presenti un retrofit, traduci sempre le scelte tecniche in canone e sfitto: meno consumi, meno vacancy, canone piu\u0300 alto. E aggiorna il piano capex ogni anno: l\u2019edificio che non si mantiene perde il tenant migliore per primo.'),
]

def main():
    os.makedirs(os.path.join(ROOT, 'schede'), exist_ok=True)
    with open(os.path.join(ROOT, 'schede', 'schede.jsonl'), 'w', encoding='utf-8', newline='\n') as f:
        for d in SCHEDE:
            f.write(json.dumps(d, ensure_ascii=False) + '\n')

    course = f'''corso: "Uffici e terziario: requisiti igienico-edilizi (D.Lgs 81/2008 Titolo II, DPR 303/1956), postazioni VDT ed ergonomia (Titolo VII, 500 lux, UNI EN 12464-1), workplace (cell office, open space, activity-based, L. 81/2017), comfort termoigrometrico e acustico (UNI EN ISO 7730, ISO 3382-3), illuminazione uffici, torri direzionali (maglia, core, facciate UNI EN 13830), impianti e flessibilita' (pavimento sopraelevato, VAV, travi fredde, BMS), fit-out Cat A/Cat B e capitolari, certificazioni LEED/BREEAM/WELL, sicurezza ed emergenza (DVR, piano di evacuazione, DUVRI), retrofit e riconversioni ufficio-residenza, economia del terziario (canoni, service charge, capex, yield)"
facolta: "FACOLTA_TECNOLOGIA_E_COSTRUZIONE"
livello: "L1-L2"
schede: {len(SCHEDE)}
formato: "JSONL"
lingua: "it"
schema_campi: [categoria, nome, descrizione, tecnologia, applicazioni, vantaggi, limiti, costi_e_economia, casi_real_world, normative, note_cantiere]
fonti: "D.Lgs 81/2008 (Titoli II, VI, VII; allegato IV), DPR 303/1956, UNI EN 12464-1, UNI EN ISO 7730, ISO 3382-3, UNI EN 13830, CEI 64-8, ISO/IEC 11801, D.Lgs 192/2005, Direttiva (UE) 2024/1275 EPBD, DPR 380/2001, L. 81/2017, L. 257/1992, protocolli LEED/BREEAM/WELL (da verificare nelle versioni); regolamenti comunali e leggi regionali citati come da verificare"
nota_metodologica: "Corso tipologico su uffici e terziario: requisiti igienico-edilizi (altezze, superfici, aeroilluminazione, con valori da verificare nel testo vigente), ergonomia VDT (schermo, seduta, 500 lux, pause 15/120), workplace (densita' 8-15 m2/posto, activity-based, smart working L. 81/2017), comfort (UNI EN ISO 7730, velocita' aria, ISO 3382-3 open plan, NR), illuminazione (UNI EN 12464-1, UGR<19), torri direzionali (maglia 7,5-9 m, core 15-25%, interpiano 3,60-4,20 m, facciate), impianti (pavimento sopraelevato, VAV, travi fredde, Cat 6A, BMS), fit-out (Cat A/B, capitolari, reinstatement), certificazioni (LEED/BREEAM/WELL come processo), retrofit (overcladding, conversioni ufficio-residenza), economia (canoni, service charge, capex, yield). NON ridondante: solo schede singole in ACUSTICA, ILLUMINAZIONE, MASTER_DESIGN e EDILIZIA_INDUSTRIALE; qui la tipologia edilizia completa. Norme di consolidata certezza con valori puntuali marcati da verificare; prezzi come fasce indicative; nessun nome di azienda."
'''
    with open(os.path.join(ROOT, 'COURSE.yaml'), 'w', encoding='utf-8', newline='\n') as f:
        f.write(course)

    readme = f'''# Uffici e terziario

Corso L1-L2 della Facolta di Tecnologia e Costruzione: l'edificio per uffici come tipologia edilizia completa — requisiti igienico-edilizi dei luoghi di lavoro (D.Lgs 81/2008 Titolo II e allegato IV, DPR 303/1956, regolamenti comunali), postazioni al videoterminale ed ergonomia (Titolo VII, 500 lux, sedute regolabili, pause), modelli di workplace (cell office, open space, activity-based, lavoro agile L. 81/2017), comfort termoigrometrico e acustico (UNI EN ISO 7730, ISO 3382-3 open plan, NR degli impianti), illuminazione naturale e artificiale (UNI EN 12464-1, UGR, DALI), torri direzionali (maglia strutturale, core, interpiano, facciate continue UNI EN 13830), impianti e flessibilita' (pavimento sopraelevato, controsoffitti tecnici, VAV, fan coil, travi fredde, BMS), fit-out Cat A/Cat B e capitolari landlord/tenant (reinstatement), certificazioni di sostenibilita' (LEED, BREEAM, WELL come processi prestazionali), sicurezza ed emergenza (DVR, piani di evacuazione e prove, DUVRI e multi-tenant), retrofit e riconversioni (overcladding, ufficio-residenza, obsolescenza) ed economia del terziario (canoni, service charge, capex, valutazioni).

**Schede: {len(SCHEDE)}**

Non ridondante: gli uffici compaiono solo in schede singole (ACUSTICA_EDILIZIA_PACK per gli open space, ILLUMINAZIONE_TECNICA_PACK per la luce, MASTER_DESIGN_PACK per il workplace design, EDILIZIA_INDUSTRIALE_LOGISTICA_PACK per gli uffici di stabilimento). Qui la tipologia edilizia completa: normativa del lavoro, comfort, struttura, impianti, fit-out, certificazioni ed economia.
'''
    with open(os.path.join(ROOT, 'README.md'), 'w', encoding='utf-8', newline='\n') as f:
        f.write(readme)

    for d in SCHEDE:
        assert list(d.keys()) == K
        s = json.dumps(d, ensure_ascii=False)
        assert 'aplicazioni' not in s and 'tegnologia' not in s
    print('OK', PACK, len(SCHEDE), 'schede')

if __name__ == '__main__':
    main()
