# -*- coding: utf-8 -*-
# Giro AG (2026-10-25): genera IMPERMEABILIZZAZIONI_SPECIALI_PACK (12 schede, L2-L3,
# FACOLTA_TECNOLOGIA_E_COSTRUZIONE)
import json, io, os

BASE = r'UNIVERSITA_EDILIZIA/IMPERMEABILIZZAZIONI_SPECIALI_PACK'
os.makedirs(os.path.join(BASE, 'schede'), exist_ok=True)

KEYS = ['categoria','nome','descrizione','tecnologia','applicazioni','vantaggi','limiti',
        'costi_e_economia','casi_real_world','normative','note_cantiere']

S = []
def add(**kw):
    assert list(kw.keys()) == KEYS, list(kw.keys())
    assert kw['costi_e_economia'].startswith('Ordini di grandezza indicativi: '), kw['nome']
    S.append(kw)

add(
 categoria="Fondamenti",
 nome="Acqua e strutture: pressione positiva, pressione negativa e la scelta della strategia",
 descrizione="Impermeabilizzare non significa 'mettere una guaina': significa decidere da che parte spinge l'acqua, con che pressione, per quanti anni e con quali accessi di manutenzione. La strategia (barriera stagna, sistema drenante, struttura impermeabile di per se') si decide prima del materiale.",
 tecnologia="Meccanismi: pressione idrostatica positiva (acqua che spinge contro l'opera: pareti contro terra, vasche piene) — la barriera va sul lato di arrivo dell'acqua; pressione negativa (umidita' che spinge dall'interno della struttura verso il rivestimento, es. parete interrata rivestita dall'interno) — pochissimi sistemi reggono: servono malte osmotiche o sistemi a iniezione progettati per contropelo; umidita' capillare e condensa: problemi diversi, soluzioni diverse (barriere chimiche, ventilazione, isolamento); strategie: (a) barriera continua esterna (membrane, liquidi, bentonite); (b) struttura impermeabile (cls impermeabile con giunti progettati, waterstop, cristallizzanti in massa); (c) sistema drenante/cavedio ispezionabile che accetta infiltrazioni controllate e le espelle; spesso la risposta giusta e' una combinazione (es. parete con membrana + intercapedine drenante).",
 applicazioni="Ogni opera interrata o contenente acqua: box interrati, platee, vasche, ascensori contro terra, locali tecnici, gallerie, coperture piane e rovescie.",
 vantaggi="La diagnosi del regime idraulico (falda presente? stagionale? spinta?) riduce drasticamente i dissesti; scegliere la strategia giusta costa meno che riparare quella sbagliata; il sistema drenante ispezionabile rende manutenibile cio' che la barriera cieca rende definitivo.",
 limiti="La falda si misura, non si indovina: servono piezometri o indagini stagionali; la barriera esterna su opera esistente spesso non e' applicabile senza scavo perimetrale (costo enorme); la pressione negativa e' il nemico numero uno dei rivestimenti interni: la maggior parte delle membrane non regge in contropelo.",
 costi_e_economia="Ordini di grandezza indicativi: indagine su falda (piezometro + misure stagionali) 1-4 k€; la differenza di costo tra barriera esterna e sistema drenante su un piano interrato di 1.000 m2 puo' valere 30-80 k€; un dissesto da pressione negativa su parete rivestita costa 100-300 euro/m2 di ripristino.",
 casi_real_world="Caso tipo: autorimessa interrata di due piani con pareti umide: la diagnosi mostra falda stagionale con spinta positiva d'inverno; invece della membrana interna (destinata a scollare) si realizza intercapedine drenante ispezionabile con pozzetto e pompa: dieci anni senza infiltrazioni visibili.",
 normative="UNI EN 1504-2 (protezione superficiale del calcestruzzo) per i sistemi su strutture; NTC (D.M. 17/1/2018) per la progettazione delle opere interrate e le azioni idrauliche; per i materiali a contatto con terreno e acqua: marcatura CE delle membrane e schede tecniche (UNI EN 13956, UNI EN 13967).",
 note_cantiere="Prima di proporre qualsiasi prodotto, chiedi: la falda e' stata misurata? In che stagione? Se la risposta e' 'di solito e' bassa', fermati: il 90% dei dissesti degli interrati nasce da una falda 'di solito bassa' che un inverno arriva al pavimento."
)

add(
 categoria="Membrane",
 nome="Membrane bituminose per opere speciali: APP/SBS oltre la copertura piana",
 descrizione="Le membrane bitume-polimero sono il cavallo da tiro dell'impermeabilizzazione italiana: ma su opere speciali (interrati, vasche, rovescie) le regole del tetto piano non bastano: servono armature portanti, protezioni meccaniche e giunti eseguiti a regola.",
 tecnologia="Materiali: compound APP (plastomero, resiste al caldo, saldatura a fiamma) e SBS (elastomero, flessibile al freddo); armature: velo vetro (leggera), poliestere (standard), poliestere rinforzato con armatura portante per opere sotto spinta e sotto getti; stratigrafie a doppio strato con giunti sfalsati e sormonti 10-15 cm; finiture: ardesiate per esposto, sabbiato/talco sotto protezione; accessori: primer bituminoso su supporto minerale, guaine di ripresa su emergenze, profili di sormonto; in opera interrata: la membrana va protetta subito (pannelli di protezione o getto di riempimento leggero) prima del rinterro con materiali senza punte; verifiche: saldatura dei giunti a fiamma controllata (prova di strappo su provini di cantiere), spessori e sormonti documentati con foto georeferenziate prima della copertura.",
 applicazioni="Platee e pareti contro terra nuove; coperture rovescie sotto ghiaia o pavimentazione; vasche di laminazione con fondo in cls; opere dove il cantiere vuole un sistema tradizionale con manodopera reperibile ovunque.",
 vantaggi="Costo contenuto e filiera di posatori capillare; riparabilita' locale a fiamma anche dopo anni; doppio strato con giunti sfalsati molto tollerante ai piccoli errori; resistenza meccanica buona sotto protezione.",
 limiti="I giunti sono il punto debole (migliaia di metri di sormonto = migliaia di possibilita' di errore); non aderiscono in continuita' su supporti umidi o freddi; in pressione negativa scollano; l'invecchiamento UV senza protezione e' rapido; il rinterro frettoloso con terreno a punte fora la membrana.",
 costi_e_economia="Ordini di grandezza indicativi: doppio strato APP/SBS 4+4 mm posato su platea/parete 30-50 euro/m2; primer e accessori inclusi; protezione meccanica (pannelli o cls leggero) 8-20 euro/m2; provini di giunto e documentazione fotografica: poche centinaia di euro, la migliore assicurazione del cantiere.",
 casi_real_world="Caso tipo: platea contro terra di 1.400 m2 con doppio strato SBS 4+4 mm, giunti sfalsati e pannelli di protezione prima del rinterro con sabbia selezionata: flood test di 72 ore sulla platea prima del solaio superato; nessuna infiltrazione in esercizio.",
 normative="UNI EN 13707 (definizioni delle membrane bituminose flessibili per coperture) e UNI EN 13969 (membrane bituminose per opere interrate) per i requisiti di prodotto; UNI EN 1928 (prova di tenuta all'acqua); Dichiarazione di Prestazione (DoP) secondo Reg. UE 305/2011 (CPR).",
 note_cantiere="Fotografa OGNI sormonto prima della copertura e archivia le foto per lotto: tra tre anni, se compare un'infiltrazione, quelle foto decidono chi paga. E il rinterro lo dirigi tu: un solo badile di terreno con pietre appuntite butta via il lavoro di una settimana."
)

add(
 categoria="Membrane",
 nome="Membrane sintetiche PVC-P, FPO/TPO ed EPDM: leggerezza, grandi superfici, serbatoi",
 descrizione="Le membrane sintetiche coprono i campi dove il bitume fatica: grandi superfici continue, serbatoi, geometrie complesse, esposizione UV. Sono sistemi di marca e di posa certificata: il cantiere giusto o niente.",
 tecnologia="Famiglie: PVC-P (cloruro di polivinile plastificato: saldatura ad aria calda, segnaletica bicolore che mostra le forature, lunga tradizione su coperture e serbatoi); FPO/TPO (poliolefine: senza plastificanti, piu' rigide, ottima resistenza UV); EPDM (gomma: elasticita' estrema, giunti incollati non saldati — punto critico); spessori 1,2-2,0 mm; posa: meccanicamente fissata (sotto carico vento), zavorrata (ghiaia/verde/piastrelle su supporti), aderente con colla; accessori: prefabbricati per angoli, emergenze, scarichi; controllo qualita': i giunti saldati ad aria calda si verificano con sonda e con prova di strappo; le membrane bicolore (strato superiore chiaro) evidenziano le lesioni per ispezione visiva.",
 applicazioni="Coperture industriali di grande superficie; tetti giardino e rovescie (strato a contatto radicanti solo con versioni specifiche anti-radice); serbatoi irrigui e vasche antincendio; coperture con geometrie complesse e molte emergenze.",
 vantaggi="Giunti saldati omogenei (il giunto diventa membrana): tenuta superiore al sormonto a fiamma; peso ridotto (1,5-2 kg/m2 contro 8-10 del doppio strato bituminoso); posa rapida su grandi superfici; bicolore = manutenzione visiva semplice.",
 limiti="Dipendenza totale dalla certificazione della squadra di posa (una saldatrice mal regolata invalida chilometri di giunto); il PVC-P perde plastificante a contatto con bitume e polistirene (serve velo di separazione); EPDM con giunti incollati invecchia male sui giunti stessi; punture da rinterro o da attrezzi: va protetta e ispezionata.",
 costi_e_economia="Ordini di grandezza indicativi: PVC-P/FPO 1,5 mm posata aderente o meccanica su copertura 35-60 euro/m2; per serbatoi e vasche (dettagli, prefabbricati, collaudi) 45-75 euro/m2; EPDM 40-70 euro/m2; verifica dei giunti con sonda e strappi: in genere inclusa nel contratto di posa certificata.",
 casi_real_world="Caso tipo: serbatoio irriguo collinare di 2.500 mc in cls impermeabilizzato con PVC-P bicolore 1,5 mm e prefabbricati sui 40 spigoli: collaudo a riempimento con controllo visivo (lo strato chiaro mostra subito due microlesioni di posa, riparate in giornata); in esercizio senza perdite.",
 normative="UNI EN 13956 (membrane flessibili polimeriche per coperture: requisiti e DoP); UNI EN 13361/13362 per le geosintetiche in serbatoi e canali quando in forma di geomembrana; D.M. 174/2004 se a contatto con acqua potabile (idoneita' del materiale); Reg. UE 305/2011 (CPR).",
 note_cantiere="Pretendi il certificato della squadra di posa del produttore e la registrazione dei parametri della saldatrice (temperatura, velocita') per turno: il giunto saldato a freddo si apre dopo due inverni, e a quel punto il posatore lo cerchi invano."
)

add(
 categoria="Membrane",
 nome="Impermeabilizzazioni liquide: poliuretano, PMMA e poliurea a spruzzo senza giunti",
 descrizione="Dove le membrane incontrano troppi dettagli (sfiati, emergenze, ringhiere, geometrie curve) la risposta moderna e' il liquido: si applica a rullo o a spruzzo e polimerizza in un manto continuo senza un solo giunto.",
 tecnologia="Famiglie: poliuretanico monocomponente a rullo (balconi, terrazzi, coperture con dettagli; con armatura in fibra nel primo strato su supporti fessurabili; spessori 1,5-2,5 mm in 2-3 mani); PMMA bicomponente (polimerizzazione rapidissima anche a freddo: rifacimenti con tempi stretti, rampe, balconi in condomini abitati); poliurea pura a spruzzo bicomponente a caldo (gel in pochi secondi, spessori 2-3 mm in un'unica applicazione, macchina bicomponente e posatori specializzati: vasche, coperture, ponti, opere interrate); preparazione: il supporto deve essere asciutto, coeso, con umidita' residua entro i limiti del produttore (misura carburo di calcio): su cls umido i liquidi fanno bolle; primer specifico per ogni supporto; risvolti e dettagli con armatura locale.",
 applicazioni="Balconi e terrazzi sotto pavimento o calpestabili; coperture con molte emergenze; vasche e cisterne; manti di ponti e parcheggi interrati; rifacimenti rapidi dove il tempo di fermo costa piu' del materiale.",
 vantaggi="Continuita' assoluta: zero giunti = zero punti deboli planari; aderenza totale al supporto (niente percorsi d'acqua sotto il manto); poliurea: cantiere velocissimo (centinaia di m2 al giorno) e calpestabilita' quasi immediata; riparabile localmente con la stessa chimica.",
 limiti="Sensibilissimi al supporto: umidita' residua, polvere, distacchi = bolle e scollamenti; gli spessori a rullo dipendono dalla mano (misurarli a film umido); la poliurea richiede macchina e squadra dedicate (non improvvisabili); esposizione UV: i poliuretanici aromatici ingialliscono e vanno protetti con finitura alifatica.",
 costi_e_economia="Ordini di grandezza indicativi: poliuretanico armato a rullo su balconi/terrazzi 35-60 euro/m2; PMMA su rifacimenti rapidi 50-90 euro/m2; poliurea a spruzzo 2-3 mm su superfici ordinarie 40-80 euro/m2 (mobilitazione della macchina: 2-5 k€, incide sulle piccole superfici).",
 casi_real_world="Caso tipo: parcheggio interrato con soletta di copertura da rifare senza demolire la pavimentazione esistente: fresatura, primer e poliurea 2,5 mm in quattro giorni su 1.100 m2, con riapertura al traffico in una settimana invece del mese stimato per il sistema tradizionale.",
 normative="EAD 030350-00-0402 (valutazione europea dei kit liquidi per coperture, ex ETAG 005) per l'idoneita' d'uso; UNI EN 14891 per i prodotti liquidi sotto piastrellatura; UNI EN 1504-2 per la protezione superficiale del calcestruzzo; schede tecniche e DoP (Reg. UE 305/2011).",
 note_cantiere="Misura l'umidita' del supporto col carburo di calcio e annotala nel verbale: il liquido applicato su soletta umida fa bolle il primo pomeriggio di sole, e senza quel numero al verbale la colpa e' sempre di chi ha posato."
)

add(
 categoria="Opere interrate",
 nome="Bentonite e sistemi idroespansivi: la barriera autosigillante contro terra",
 descrizione="Le membrane bentonitiche sfruttano un principio elegante: l'argilla a contatto con l'acqua si espande e autosigilla le piccole lesioni. Contro terra nuova sono un sistema provato; richiedono pero' confinamento permanente: la bentonite che si espande libera va altrove.",
 tecnologia="Sistemi: teli geosintetici con bentonite sodica tra due geotessili (agugliati o incollati), posati a secco su platea e pareti prima dei getti; fissaggio meccanico con rondelle sulle pareti; sormonti 10-15 cm con bentonite libera nei giunti; waterstop idroespansivi in barrette o paste nei giunti di getto e nelle riprese (sempre confinati: espansione libera = rottura del giunto); requisiti: confinamento permanente (il getto o il terreno compatto devono impedire l'espansione libera), assenza di contatto prematuro con l'acqua prima del confinamento (cantiere sotto pioggia = disastro), terreno di rinterro senza punte e compattato a strati; limiti chimici: acque aggressive (solfati, salinita' alta) riducono l'espansione della bentonite sodica: verificare l'analisi dell'acqua di falda.",
 applicazioni="Platee e pareti contro terra di nuova costruzione con falda; opere dove i giunti di getto sono tanti e il waterstop tradizionale in PVC e' difficile da posare; risanamento di giunti con iniezioni idroespansive.",
 vantaggi="Posa a secco rapida anche su supporti non perfetti; autosigillatura delle microlesioni; i giunti idroespansivi nei getti risolvono il punto storico piu' debole delle opere in cls; nessuna saldatura a fiamma o ad aria calda.",
 limiti="Il confinamento e' condizione di funzionamento, non un dettaglio: parete non controgettata o rinterro lasco = espansione libera; il contatto con l'acqua prima del getto gonfia i teli (stoccaggio e posa sotto pioggia vietati); su falde chimicamente aggressive servono bentoniti modificate o altro sistema.",
 costi_e_economia="Ordini di grandezza indicativi: telo bentonitico posato su platea/parete 20-35 euro/m2; waterstop idroespansivo in barretta 8-20 euro/m posato; pasta idroespansiva per giunti e attraversamenti 10-25 euro/m; il sistema compete col doppio strato bituminoso con protezione.",
 casi_real_world="Caso tipo: palazzo con due piani interrati in zona di falda alta: platea e pareti con teli bentonitici, giunti di getto verticali delle pareti con barretta idroespansiva fissata e confinata dal getto successivo; pozzetto ispezionabile sul perimetro: dieci anni di esercizio asciutto.",
 normative="Le membrane bentonitiche rientrano nella famiglia delle geosintetiche barriera (GCL): requisiti di prodotto e DoP secondo le norme di serie EN applicabili e schede tecniche del produttore (verificare la marcatura e i campi d'uso dichiarati); NTC (D.M. 17/1/2018) per la progettazione dell'opera interrata.",
 note_cantiere="Con la bentonite il nemico e' il meteo: posa solo con previsione asciutta per le 48 ore successive e copri immediatamente con il getto o con teli. Ho visto una platea bentonitica sotto un temporale: sembrava un campo di popcorn, e si e' rifatta da zero."
)

add(
 categoria="Opere interrate",
 nome="Platee e pareti contro terra su esistente: vesciche, cavedii drenanti e risanamento dall'interno",
 descrizione="Sull'esistente non si scava: il 90% degli interrati italiani va impermeabilizzato dall'interno, cioe' in pressione negativa. E' il terreno dove si giocano (e si perdono) piu' soldi: malte osmotiche, iniezioni, cavedii ispezionabili.",
 tecnologia="Diagnosi prima di tutto: origine (falda in spinta? umidita' di risalita? condensa? perdita da rete?) con misure strumentali (igrometro, termografia, analisi sali); soluzioni in pressione negativa: (a) malte e boiacche osmotiche/cristallizzanti su supporto rugginato e saturo: reggono la contropelo dichiarata in scheda (valori tipici 1,5-5 bar secondo prodotto: leggere la scheda, non la brochure); (b) iniezioni: resine o microemulsioni in cortina dietro la parete (fori a quinconce, packer, pompa) o nel giunto parete-platea; (c) cavedio drenante ispezionabile: controparete con camera d'aria e canaletta perimetrale che raccoglie l'infiltrazione ammessa e la espelle (pozzetto con pompa e allarme): il sistema accetta che la parete vecchia non sia stagnabile e gestisce l'acqua invece di combatterla; (d) vespai aerati orizzontali solo dove la geometria lo consente; pompe: sempre ridondate e con allarme (la pompa unica e' un'alluvione annunciata).",
 applicazioni="Cantine, garage e vani tecnici interrati esistenti; risanamento di edifici storici (scavo impossibile); giunti parete-platea infiltranti; ascensori e fosse contro terra.",
 vantaggi="Intervento dall'interno senza scavi (spesso l'unica via); il cavedio drenante e' ispezionabile e manutenibile per sempre; le osmotiche serie hanno decenni di casi documentati in contropelo; le iniezioni nei giunti sono mirate ed economiche.",
 limiti="La contropelo e' la condizione peggiore: ogni prodotto ha un limite di pressione dichiarato e i supporti deboli fanno fallire anche il prodotto giusto; le iniezioni a cortina richiedono consumi e resa imprevedibili in terreni eterogenei; il cavedio riduce l'area utile e dipende dalla pompa (energia, allarmi, manutenzione).",
 costi_e_economia="Ordini di grandezza indicativi: ciclo osmotico su parete 40-80 euro/m2; iniezioni nei giunti 80-200 euro/m lineare di giunto; cortina a iniezione 150-400 euro/m2 di parete (consumo dipendente dal terreno); cavedio drenante con controstruttura e pozzetto 200-400 euro/m2 di parete attrezzata.",
 casi_real_world="Caso tipo: caveau interrato con pareti perimetrali umide da falda stagionale: rinuncia alla barriera interna (supporto troppo debole), realizzazione di cavedio drenante ispezionabile sui quattro lati con due pompe ridondate e allarme remoto: ambiente asciutto e sistema controllabile a ogni sopralluogo.",
 normative="UNI EN 1504-9 (principi per la protezione e riparazione del calcestruzzo) e UNI EN 1504-2 per i sistemi di superficie; le osmotiche si scelgono sulle schede con pressione negativa dichiarata; per le pompe di pozzetto: CEI 64-8 e D.M. 37/2008 per la parte elettrica.",
 note_cantiere="Prima di proporre l'osmotico, gratta il supporto: se l'intonaco o il cls si sfarinano sotto la punta, nessuna malta regge la contropelo: si raschia fino al sano o si cambia strategia. E metti SEMPRE l'allarme sulla pompa: la pompa silenziosa e' quella che non funziona."
)

add(
 categoria="Coperture",
 nome="Coperture rovescie e pensili carrellabili: la membrana sotto tutto",
 descrizione="Nella copertura rovescia la membrana lavora sotto l'isolante e sotto il carico: invisibile, piu' protetta dagli shock termici, ma irraggiungibile senza smontare tutto. Progetto, posa e collaudo devono essere perfetti la prima volta.",
 tecnologia="Stratigrafia rovescia: soletta (pendenze >= 1,5-2%), membrana (bituminosa doppio strato o sintetica anti-radice se sotto verde), isolante XPS a posa libera (l'XPS resiste all'acqua sopra la membrana), strato di separazione/filtrante, protezione (ghiaia, pavimentazione su supporti regolabili, verde); carrellabile: platea/soletta in cls o pavimentazione su supporti con carichi e verifiche; punti critici: scarichi che attraversano la stratigrafia (bocchettoni a due livelli per rovescia con drenaggio superficiale e profondo), risvolti superiori al livello di calpestio finito di almeno 15 cm (sotto la pioggia battente il livello sale), emergenze e pali ringhiera fissati PRIMA della membrana o con dettagli certificati; collaudo: flood test o ispezione elettronica PRIMA di coprire; regola d'oro: tutto cio' che copre la membrana deve essere rimovibile per isole (manutenzione futura).",
 applicazioni="Terrazzi calpestabili di edifici residenziali; parcheggi e rampe in copertura; tetti giardino; piazze sopra garage interrati (il caso piu' diffuso e piu' dissestato d'Italia).",
 vantaggi="La membrana sotto l'isolante lavora a temperatura quasi costante: invecchia lentamente; la stratigrafia protetta tollera il traffico; la pavimentazione su supporti permette ispezione e riparazione per isole senza demolizioni.",
 limiti="Una lesione sotto 30 cm di stratigrafia si trova a settimane di distanza dalla traccia interna; i supporti regolabili pongono carichi concentrati (protezione della membrana sotto i puntali); il bocchettone a due livelli mal posato allaga l'interfaccia; il rifacimento totale costa 3-5 volte la posa iniziale.",
 costi_e_economia="Ordini di grandezza indicativi: stratigrafia rovescia completa (membrana doppio strato + XPS + ghiaia) 80-130 euro/m2; con pavimentazione su supporti 120-200 euro/m2; piazza sopra garage carrellabile con membrana, isolante, platea alleggerita e pavimentazione 150-300 euro/m2; flood test: 1-3 k€ e li vale tutti.",
 casi_real_world="Caso tipo: piazza pedonale sopra due piani di autorimessa: rifacimento con membrana sintetica anti-radice, XPS, platea alleggerita e pavimentazione su supporti; i bocchettoni a due livelli confluiscono in un collettore ispezionabile; le isole di supporti si smontano a mano per la manutenzione: dopo il rifacimento, zero infiltrazioni negli allagamenti sotto flood test periodici.",
 normative="UNI 11493-1 per le pavimentazioni ceramiche eventualmente incollate; UNI EN 13956/UNI EN 13707 e DoP per le membrane; NTC (D.M. 17/1/2018) per i carichi delle solette di copertura carrellabili; UNI 11235 per gli strati a verde se presenti.",
 note_cantiere="Prima di coprire la membrana fai il flood test o la scansione elettronica e lo firmi a verbale con DL e impresa: 'coperto senza collaudo' e' la frase che ritroverai nella perizia tra dieci anni. E i pali della ringhiera si fissano alla soletta, MAI attraverso la membrana finita."
)

add(
 categoria="Vasche e serbatoi",
 nome="Vasche di laminazione, serbatoi antincendio e acqua potabile: tenuta e idoneita'",
 descrizione="Le vasche devono tenere l'acqua dentro (serbatoi) o gestirla in sicurezza (laminazione): due problemi diversi con gli stessi materiali. Se poi l'acqua e' potabile, entra in gioco l'idoneita' sanitaria del materiale, non solo la tenuta.",
 tecnologia="Tipologie: vasca di laminazione (opera idraulica: terra armata o cls con geomembrana; tenuta per non erodere le sponde, non per conservare acqua); serbatoio antincendio (cls impermeabile o rivestimento: la tenuta garantisce la riserva: UNI EN 12845 per l'impianto, la vasca come sua parte); serbatoio irriguo (geomembrana PVC-P/EPDM/FPO su letto di posa in sabbia o geotessile: il terreno punzonante e' il primo nemico); acqua potabile: solo materiali con idoneita' al contatto secondo D.M. 174/2004 (resine e membrane certificate per potabile: la scheda deve dirlo esplicitamente); dettagli: attraversamenti con flange e guaine prefabbricate, giunti di dilatazione con waterstop, spigoli arrotondati per i rivestimenti liquidi, collaudo a riempimento graduale (25-50-75-100% con misura dei livelli nel tempo: abbassamento ammissibile secondo progetto/collaudo, tenendo conto di evaporazione e temperatura).",
 applicazioni="Opere idrauliche urbane (laminazione, first flush); riserve antincendio aziendali; serbatoi irrigui agricoli; cisterne di accumulo con riuso potabile o irriguo.",
 vantaggi="La geomembrana su vasca in terra rende economici volumi grandi (migliaia di mc a costo contenuto); il collaudo a riempimento graduale documenta la tenuta in modo incontestabile; i materiali certificati per potabile aprono il riuso idrico.",
 limiti="Il letto di posa imperfetto fora la geomembrana al primo riempimento; il controllo dell'evaporazione durante il collaudo fa discutere se non e' previsto nel metodo; i materiali generici NON possono stare a contatto con potabile (idoneita' da certificato, non da somiglianza); il gelo sulle sponde scoperte danneggia le membrane non protette.",
 costi_e_economia="Ordini di grandezza indicativi: geomembrana su vasca in terra con letto di posa e ancoraggio perimetrale 25-50 euro/m2; rivestimento vasca in cls per antincendio (liquido o membrana con dettagli) 45-80 euro/m2; ciclo per potabile certificato D.M. 174/2004 50-90 euro/m2; collaudo a riempimento con misure: 1-3 k€.",
 casi_real_world="Caso tipo: vasca di laminazione urbana da 3.000 mc in terra rimodellata con geomembrana FPO 2 mm su letto di sabbia e geotessile, ancoraggio in trincea perimetrale: collaudo con riempimento a stadi e misura livelli corretta per evaporazione; in funzione da anni con ispezione annuale visiva.",
 normative="D.M. 174/2004 (materiali a contatto con acqua potabile); UNI EN 12845 (impianti antincendio sprinkler: la riserva idrica ne e' parte); serie EN sulle geosintetiche per barriere idrauliche; D.Lgs 152/2006 per le opere idrauliche e il loro inquadramento.",
 note_cantiere="Al collaudo a riempimento misura il livello ogni 12 ore a pari temperatura e con vasca schermata dal vento, e scrivi nel verbale il metodo di correzione per evaporazione: senza quel metodo concordato PRIMA, il collaudo finisce in disputa sulla pioggia e sul sole."
)

add(
 categoria="Infrastrutture",
 nome="Ponti e viadotti: l'impermeabilizzazione sotto il manto stradale",
 descrizione="Sotto l'asfalto di un ponte c'e' un impacco che protegge il cls e le armature dall'acqua e dai sali disgelanti: quando fallisce, il degrado arriva alle armature e il conto diventa strutturale. E' la scheda che manca a quasi tutti i manuali edili.",
 tecnologia="Stratigrafia classica: soletta in cls (finitura di getto rugginata, pendenza trasversale), primer, membrana (bituminosa ad alta resistenza termica per ricevere l'asfalto a 150-180 °C, o liquida, o sistemi misti), strato di protezione dove previsto, manto bituminoso (binder + tappetino); requisiti: aderenza al supporto e al manto, resistenza alla punzonatura, compatibilita' termica col getto d'asfalto; punti critici: giunti di dilatazione (l'impermeabilizzazione continua sotto il giunto con dettagli dedicati o si interrompe con risvolti nel giunto: mai lasciare il cls nudo), cordoli e canali di gronda, attraversamenti; controlli: prova di aderenza (pull-off) su provini, spessori del manto, verifica pendenze; la patologia tipica: infiltrazioni al giunto di dilatazione -> sali -> carbonatazione e cloruri -> degrado spalla/pulvino: la manutenzione del giunto E' manutenzione strutturale.",
 applicazioni="Viabilita' comunale su sottopassi e sovrappassi; parcheggi in copertura con traffico veicolare (analogia tecnica); ponti pedonali; opere di gestori (strade, ferrovie) con capitolati propri.",
 vantaggi="La protezione corretta allunga la vita della struttura di decenni (i sali disgelanti sono il killer n.1 dei ponti in cls); la diagnosi precoce (giunti che perdono) costa centinaia di euro, il ripristino strutturale centinaia di migliaia; i sistemi moderni reggono il getto d'asfalto senza protezione aggiuntiva.",
 limiti="Lavorare sotto traffico o con finestre di cantiere strette impone sistemi rapidi (piu' costosi); la compatibilita' membrana-asfalto va dichiarata dal produttore (temperatura di applicazione); l'accesso ai giunti richiede fermi di carreggiata: la manutenzione programmata dei giunti e' politica di gestione, non solo tecnica.",
 costi_e_economia="Ordini di grandezza indicativi: impermeabilizzazione di impalcato con membrana idonea al getto d'asfalto 40-70 euro/m2 (senza manto); rifacimento completo con scarifica e manto 100-180 euro/m2; rifacimento di un giunto di dilatazione 800-2.500 euro/m secondo tipo; il costo del degrado non prevenuto su spalle e pulvini: ordini di grandezza superiori.",
 casi_real_world="Caso tipo: cavalcavia comunale con macchie di umidità ed efflorescenze sotto i giunti: ispezione mostra giunti non piu' stagni e membrana interrotta; intervento a carreggiate alternate con rifacimento giunti, ripristino membrana in aderenza e nuovo manto: eliminata la via d'ingresso dei sali prima del degrado delle spalle.",
 normative="EN 14695 (membrane flessibili per l'impermeabilizzazione di impalcati in calcestruzzo e superfici carrabili: requisiti e prove); capitolati speciali dei gestori infrastrutturali (da verificare caso per caso); NTC (D.M. 17/1/2018) e linee guida sulle opere esistenti per la parte strutturale.",
 note_cantiere="Sui ponti il giunto di dilatazione e' il rubinetto dei sali: metti in contratto l'ispezione dei giunti ogni anno e il lavaggio delle spalle in primavera dopo la stagione del disgelo. Costa poche centinaia di euro e vale piu' di qualsiasi membrana."
)

add(
 categoria="Infrastrutture",
 nome="Gallerie: impermeabilizzazione tra paramento e rivestimento definitivo",
 descrizione="In galleria l'acqua di montagna cerca il calcestruzzo: la membrana a losanga tra il rivestimento provvisorio e quello definitivo, con il drenaggio che la accompagna, decide se la galleria vivra' asciutta o perdera' per sempre.",
 tecnologia="Schema: spritz/rivestimento provvisorio -> geotessile di protezione -> membrana impermeabile (losanga in PVC-P o similari fissata a dischetti sul paramento, teli saldati ad aria calda con piste di controllo) -> rivestimento definitivo in cls; drenaggio: la membrana non regge la spinta della montagna ma GUIDA l'acqua ai dreni di piede (gallette laterali, tubi forati, geocompositi): il sistema e' 'impermeabile + drenante', mai solo impermeabile; compartimentazione: la losanga puo' essere settorizzata con waterstop iniettabili per localizzare le perdite future; dettagli: pozzi, nicchie, canaline impianti, giunti di avanzamento del getto; verifiche: controllo delle saldature (sonda, prova ad aria sui giunti doppi con camera di prova), tracciabilita' dei teli; la gestione delle acque di falda in galleria ha inquadramento ambientale (scarichi, autorizzazioni: D.Lgs 152/2006).",
 applicazioni="Gallerie stradali e ferroviarie nuove; risanamento di gallerie esistenti con controvolte; sottopassi e opere in sotterraneo assimilabili.",
 vantaggi="Il sistema losanga+dreni e' consolidato e documentato; la compartimentazione permette di localizzare e iniettare le perdite future senza demolire; la saldatura con pista doppia permette la prova pneumatica del giunto (controllo certo).",
 limiti="E' un cantiere specializzato: squadre, attrezzature e ritmi non improvvisabili; il paramento irregolare strappa i teli se il geotessile e' sottodimensionato; la perdita localizzata senza compartimentazione costringe a caccia al buco su chilometri; la manutenzione dei dreni (calcare) e' la voce dimenticata: dreni ostruiti = spinta idraulica sul rivestimento.",
 costi_e_economia="Ordini di grandezza indicativi: sistema losanga (geotessile + membrana + posa specializzata) 45-80 euro/m2; compartimentazione con waterstop iniettabili a scacchiera 10-25 euro/m2 aggiuntivi; manutenzione e lavaggio dreni: voce annuale da preventivare nella gestione dell'opera.",
 casi_real_world="Caso tipo: galleria stradale di 800 m con losanga compartimentata ogni 50 m e waterstop iniettabili: a due anni dall'apertura compare una stilla a una nicchia; la compartimentazione la localizza in un pomeriggio e l'iniezione la chiude senza chiusure al traffico.",
 normative="Per i materiali: schede e DoP delle membrane (serie EN applicabili); per l'opera: capitolati dei gestori e normativa sulle gallerie (verificare il quadro specifico dell'opera); D.Lgs 152/2006 per la gestione e lo scarico delle acque di falda drenate.",
 note_cantiere="Pretendi la prova pneumatica su TUTTI i giunti doppi e la mappatura dei teli con numero di rotolo: quando tra dieci anni compare una stilla, la mappa dei teli e delle prove vale piu' del collaudo. E ricorda: la membrana guida l'acqua, non la combatte — i dreni vanno curati come la membrana."
)

add(
 categoria="Dettagli",
 nome="Giunti, risvolti e dettagli: dove nascono il 90% dei dissesti",
 descrizione="Le membrane non perdono quasi mai in campo aperto: perdono ai giunti di getto, ai risvolti, alle emergenze, agli attraversamenti. I dettagli sono il vero prodotto dell'impermeabilizzazione: disegnarli, ordinarli e collaudarli e' meta' del lavoro.",
 tecnologia="Punti critici canonici: giunti di getto orizzontali e verticali (waterstop in PVC interno/esterno, barrette idroespansive confinate, nastri bentonitici, tubi iniettabili reiniettabili); risvolti su pareti (altezza minima sopra il calpestio, profilo di sormonto, copertina o contromanto); emergenze (pilastri, pali, raccordi) con prefabbricati o guaine di ripresa; attraversamenti (tubi, cavi) con flange e calotte; spigoli vivi (mai: raccordare con sagoma o rinvio inclinato per liquidi e membrane); scarichi (bocchettoni a tenuta sulla membrana, non appoggiati sopra); movimenti: giunti strutturali che si muovono richiedono waterstop a bulbo o sistemi a sovrapposizione calcolata sul movimento atteso (indicare in progetto il movimento di progetto in mm: il prodotto si sceglie su quel numero); regole d'oro: il dettaglio si DISEGNA in tavola, si ORDINA come articolo (nome del prefabbricato, non 'guaina a raccordo'), si FOTOGRAFA prima della copertura.",
 applicazioni="Ogni sistema: bituminoso, sintetico, liquido, bentonitico; opere interrate, coperture, vasche, ponti; la tavola dei dettagli tipici del progetto come documento contrattuale.",
 vantaggi="I prefabbricati di dettaglio eliminano l'improvvisazione in quota; il waterstop giusto nel giusto giunto rende il cls stesso impermeabile (riduzione degli strati); la documentazione fotografica dei dettagli decide le garanzie.",
 limiti="Il dettaglio lasciato alla mano del posatore e' una lotteria; i waterstop interni mal fissati si spostano sotto la vibrazione del getto (e si scopre dopo il rinterro); i sistemi reiniettabili costano di piu' e si ripagano solo su opere strategiche; ogni famiglia di membrane ha i SUOI accessori: mescolare marche sui dettagli invalida le garanzie.",
 costi_e_economia="Ordini di grandezza indicativi: waterstop in PVC 6-15 euro/m fornito, posato 12-30 euro/m; barretta idroespansiva 8-20 euro/m posata; sistema reiniettabile 40-90 euro/m; prefabbricato di emergenza 15-60 euro/cad; la tavola dettagli del progettista: qualche ora di lavoro che vale piu' di qualsiasi sovrapprezzo di materiale.",
 casi_real_world="Caso tipo: vasca in cls con giunti di ripresa verticali ogni 6 m: progetto con waterstop a bulbo esterno + tubo reiniettabile sui giunti; al collaudo a riempimento due giunti stillano: iniezione dai tubi senza svuotare oltre il giunto, collaudo superato alla seconda prova senza demolizioni.",
 normative="Serie UNI EN 1504 per protezione e riparazione del cls; schede tecniche e istruzioni di posa dei produttori di waterstop (requisito: movimento ammissibile dichiarato); per i dettagli in copertura: buone pratiche di settore e norme di prodotto delle membrane.",
 note_cantiere="In riunione di cantiere, prima del primo getto, metti sul tavolo la sezione del giunto con il waterstop fissato: dove passa, come e' fissato, chi vibra il getto vicino. Il waterstop trovato 'arrotolato in fondo allo scavo' dopo il getto e' la storia piu' vecchia dell'edilizia, e succede ancora."
)

add(
 categoria="Collaudo",
 nome="Controlli e collaudo di tenuta: flood test, prove elettroniche, termografia",
 descrizione="Un'impermeabilizzazione non collaudata e' un'ipotesi. I metodi di prova esistono, costano poco rispetto all'opera e trasformano la consegna da fiducia a documento: il collaudo di tenuta va in contratto, non tra i desideri.",
 tecnologia="Metodi: flood test (allagamento della copertura/vasca con 5-10 cm d'acqua per 48-72 ore, tappando i bocchettoni con otturatori a tenuta: misura livelli e ispezione dei sottostanti); prova elettronica delle membrane (holiday test a spazzola o arco su membrane su supporto conduttivo: trova fori e pori; su coperture esistenti la scansione a impulsi/localizzazione bagnato); termografia al tramonto per mappare zone umide sotto la finitura (richiede condizioni di irraggiamento favorevoli); misure di umidita' nei supporti (carburo di calcio, igrometri capacitivi: documentano il supporto prima della posa); prove sui giunti (strappo su provini di cantiere per bituminose e sintetiche, prova pneumatica sui doppi giunti delle losagne); documentazione: verbale con metodo, durata, livelli, foto, condizioni meteo; la firma del collaudo di tenuta e' la condizione per coprire l'opera.",
 applicazioni="Consegna di ogni copertura piana o rovescia, vasca, platea impermeabilizzata; diagnosi di infiltrazioni su esistente; verifiche periodiche in gestione.",
 vantaggi="Il flood test costa poco e prova tutto il sistema (campo e dettagli) nelle condizioni reali; le prove elettroniche trovano la lesione al centimetro invece che per tentativi; la documentazione di collaudo protegge tutti: impresa, DL, committente.",
 limiti="Il flood test richiede struttura verificata per il carico dell'acqua (5-10 cm = 50-100 kg/m2: verificare la soletta!) e previsione meteo stabile; le prove elettroniche richiedono supporto conduttivo o condizioni specifiche (non universali); la termografia dipende dal meteo e dall'operatore; nessun metodo sostituisce la manutenzione.",
 costi_e_economia="Ordini di grandezza indicativi: flood test di copertura 1-3 k€ (allestimento, misure, verbale); scansione elettronica/holiday test 2-6 euro/m2 con minimo di cantiere 1,5-4 k€; termografia di copertura 1-3 k€; provini di giunto: poche centinaia di euro; tutto insieme: 1-3% del costo dell'opera, a fronte di garanzie decennali.",
 casi_real_world="Caso tipo: copertura rovescia di 900 m2 collaudata con scansione elettronica prima dell'XPS: individuate 7 microlesioni di posa (tracce di attrezzi), riparate in giornata; rifatto il test sulle riparazioni; la copertura consegnata con mappa delle prove allegata al certificato di collaudo.",
 normative="UNI EN 1928 (tenuta all'acqua delle membrane: metodo di prova di prodotto); buone pratiche e manuali di settore per flood test e prove elettroniche (nessuna norma cogente unica: il metodo va prescritto in contratto); la verifica strutturale del carico di prova secondo NTC (D.M. 17/1/2018).",
 note_cantiere="Scrivi nel capitolato: 'la copertura dell'impermeabilizzazione e' subordinata a collaudo di tenuta positivo documentato'. Una riga cosi' cambia i comportamenti di tutto il cantiere piu' di qualsiasi richiamo verbale. E prima del flood test, fai firmare la verifica della soletta al carico dell'acqua."
)

# --- scrittura schede.jsonl ---
p_jsonl = os.path.join(BASE, 'schede', 'schede.jsonl')
out = io.open(p_jsonl, 'w', encoding='utf-8', newline='\n')
for s in S:
    out.write(json.dumps(s, ensure_ascii=False) + '\n')
out.close()

# --- COURSE.yaml ---
course = """corso: "Impermeabilizzazioni speciali: opere interrate, vasche, ponti e collaudi di tenuta"
facolta: "FACOLTA_TECNOLOGIA_E_COSTRUZIONE"
livello: "L2-L3"
schede: 12
formato: "JSONL"
lingua: "it"
schema_campi: [categoria, nome, descrizione, tecnologia, applicazioni, vantaggi, limiti, costi_e_economia, casi_real_world, normative, note_cantiere]
fonti: "UNI EN 13707, UNI EN 13956, UNI EN 13969, UNI EN 1928, UNI EN 13967, UNI EN 14891, UNI EN 1504-2/1504-9, EAD 030350-00-0402 (ex ETAG 005), EN 14695, UNI 11235, UNI 11493-1, D.M. 174/2004, UNI EN 12845, Reg. UE 305/2011 (CPR), NTC D.M. 17/1/2018, D.Lgs 152/2006, D.Lgs 81/2008, D.M. 37/2008, CEI 64-8"
nota_metodologica: "Impermeabilizzazioni oltre il tetto piano: regimi idraulici (pressione positiva/negativa), membrane bituminose per opere speciali, sintetiche (PVC-P/FPO/EPDM), liquidi (poliuretano/PMMA/poliurea), bentonite, interrati su esistente (osmotiche, iniezioni, cavedii), coperture rovescie e carrellabili, vasche e serbatoi (anche potabili), ponti sotto manto, gallerie, dettagli e giunti (waterstop), controlli e collaudi di tenuta. Distinto da TETTI_E_COPERTURE_PACK (coperture ordinarie) e POSA_IN_OPERA_PACK (liquidi per zone umide/balconi). Prezzi come fasce indicative; norme solo di consolidata certezza; nessun nome di azienda."
"""
open(os.path.join(BASE, 'COURSE.yaml'), 'w', encoding='utf-8').write(course)

# --- README.md ---
readme = """# Impermeabilizzazioni speciali: opere interrate, vasche, ponti e collaudi di tenuta

Corso di livello L2-L3 (FACOLTA_TECNOLOGIA_E_COSTRUZIONE) sull'impermeabilizzazione oltre la copertura piana ordinaria: regimi idraulici (pressione positiva vs negativa, falda, capillarità), membrane bituminose per opere speciali (doppio strato, protezioni, rinterri), membrane sintetiche (PVC-P, FPO/TPO, EPDM) per grandi superfici e serbatoi, impermeabilizzazioni liquide (poliuretano, PMMA, poliurea a spruzzo), bentonite e sistemi idroespansivi contro terra, risanamento di interrati esistenti in pressione negativa (osmotiche, iniezioni, cavedii drenanti), coperture rovescie e carrellabili, vasche di laminazione e serbatoi (antincendio, irrigui, acqua potabile con D.M. 174/2004), impalcati da ponte sotto manto stradale (EN 14695) e giunti di dilatazione, gallerie (losanga + drenaggio), dettagli e giunti (waterstop, prefabbricati, movimenti di progetto), controlli e collaudi di tenuta (flood test, prove elettroniche, termografia, provini di giunto).

**Schede: 12** — formato JSONL con le 11 chiavi standard dell'Università dell'Edilizia.

Regola metodologica: non ridondante con TETTI_E_COPERTURE_PACK (coperture ordinarie) e POSA_IN_OPERA_PACK (liquidi per zone umide/balconi): qui opere interrate, infrastrutture, vasche e collaudi. Prezzi come fasce indicative con unità; norme solo di consolidata certezza; nessun nome di aziende.
"""
open(os.path.join(BASE, 'README.md'), 'w', encoding='utf-8').write(readme)

# --- verifica finale ---
rows = [json.loads(l) for l in open(p_jsonl, encoding='utf-8') if l.strip()]
assert len(rows) == 12, len(rows)
for r in rows:
    assert list(r.keys()) == KEYS, r['nome']
    assert 'aplicazioni' not in r and 'tegnologia' not in r
print('OK:', p_jsonl, '-', len(rows), 'schede, chiavi e ordine corretti')
