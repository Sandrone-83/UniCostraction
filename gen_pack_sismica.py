# -*- coding: utf-8 -*-
"""Giro AN (2026-11-02): genera INGEGNERIA_SISMICA_ISOLAMENTO_PACK (12 schede).
Tema: ingegneria sismica come corso dedicato — pericolo, stati limite, analisi,
gerarchia delle resistenze, edifici esistenti, classificazione del rischio,
isolamento alla base, dissipazione, elementi non strutturali, cantiere del
miglioramento. NON ridondante: INGEGNERIA_STRUTTURALE ha 1 scheda di panorama;
RISANAMENTO ha il miglioramento sull'esistente lato recupero; qui il corso
tecnico completo con isolamento e dissipazione (assenti altrove)."""
import json, os

BASE = os.path.join('UNIVERSITA_EDILIZIA', 'INGEGNERIA_SISMICA_ISOLAMENTO_PACK')
KEYS = ["categoria","nome","descrizione","tecnologia","applicazioni","vantaggi","limiti","costi_e_economia","casi_real_world","normative","note_cantiere"]

S = []

S.append({
 "categoria": "Sismica — pericolo e azione",
 "nome": "La pericolosita' sismica in Italia: zonazione storica, PGA, spettri e periodi di ritorno",
 "descrizione": "Il punto di partenza di ogni progetto in zona sismica: capire QUANTO scuote il sito. In Italia l'azione sismica non si legge piu' sulla vecchia zonazione a 4 zone ma si ricava dalla pericolosita' di base su reticolo di calcolo: ad ogni sito corrispondono parametri che costruiscono lo spettro elastico di progetto.",
 "tecnologia": "Parametri dello spettro elastico: ag (accelerazione massima al suolo su roccia rigida), Fo (amplificazione spettrale massima), Tc* (periodo di inizio del tratto a velocita' costante), Ss (coefficiente stratigrafico di sottosuolo) e Cc; categorie di sottosuolo A-E (dalla roccia ai depositi soffici) e condizioni topografiche T1-T4 (rilievi pianeggianti vs pendii e creste, con coefficiente ST fino a 1,4); periodi di ritorno dell'azione: 30 anni (SLO), 50 (SLD), 475 (SLV), 712 (SLC) per costruzioni ordinarie; strumenti ufficiali di interrogazione del reticolo nazionale e indagini geognostiche per la categoria di sottosuolo.",
 "applicazioni": "Definizione dell'azione sismica di ogni nuova costruzione e di ogni valutazione dell'esistente; confronto tra siti in fase di scelta localizzativa; input di ogni analisi lineare e non lineare.",
 "vantaggi": "Approccio puntuale sito-specifico: addio agli scatti artificiali tra un comune e il confinante; lo spettro continuo consente analisi coerenti con il periodo proprio della struttura; la classificazione del sottosuolo obbliga a guardare il terreno, non solo la mappa.",
 "limiti": "La mappa di pericolosita' e' un modello probabilistico con incertezze; la categoria di sottosuolo stimata 'a sentimento' puo' spostare l'azione del 20-40%: serve almeno una prova penetrometrica o una Vs30 credibile; microzonazione comunale, quando esiste, prevale e va acquisita.",
 "costi_e_economia": "Ordini di grandezza indicativi: interrogazione del reticolo e analisi di pericolosita' di base: 300-1.500 euro a elaborato; indagine geognostica minima per categoria di sottosuolo (1 sondaggio + prove in foro): 3.000-10.000 euro; studi di microzonazione per singoli lotti strategici: 15.000-60.000 euro.",
 "casi_real_world": "Caso tipo: progetto di una scuola in comune dell'Appennino centrale: l'interrogazione del reticolo restituisce ag pari a 0,26 g su roccia, ma il sito e' su depositi alluvionali (categoria C): l'amplificazione stratigrafica porta l'azione di progetto a livelli che impongono di rivedere la scelta strutturale verso un telaio piu' duttile.",
 "normative": "D.M. 17/1/2018 (NTC 2018), Cap. 3 (azioni, con definizione dell'azione sismica) e Allegati di pericolosita'; Circolare 21/1/2019 n. 7 (applicazione); EN 1998-1 (Eurocodice 8: pericolosita' e spettri); L. 64/1974 (provvedimenti per le costruzioni in zone sismiche, impianto storico).",
 "note_cantiere": "Non progettare mai su una categoria di sottosuolo 'ereditata' dal progetto del vicino: chiedi la relazione geologica e, se manca, spingi per almeno una prova. Un Ss sbagliato non si vede a fine cantiere: si vede al primo terremoto."
})

S.append({
 "categoria": "Sismica — pericolo e azione",
 "nome": "Stati limite sismici e verifiche: SLO, SLD, SLV, SLC e gli spostamenti interpiano",
 "descrizione": "La logica prestazionale delle NTC: la struttura deve attraversare terremoti di intensita' crescente con prestazioni decrescenti ma controllate — operativita' piena, danno limitato, salvaguardia della vita, prevenzione del collasso. Ad ogni stato limite corrisponde un periodo di ritorno e una verifica specifica.",
 "tecnologia": "Stati limite di esercizio: SLO (TR 30 anni: nessuna interruzione d'uso) e SLD (TR 50 anni: danno limitato e riparabile), verificati sugli spostamenti interpiano con limiti tipici dello 0,5% dell'altezza per tamponamenti rigidamente connessi, 0,75% per connessioni deformabili, 1% in assenza di tamponamenti; stati limite ultimi: SLV (TR 475 anni: la struttura resiste senza collasso, con danno significativo) e SLC (TR 712 anni: prevenzione del collasso globale), verificati su resistenza, duttilita' e spostamento; rapporto tra domanda e capacita' espresso come ζE (rapporto accelerazioni) per le costruzioni esistenti.",
 "applicazioni": "Progetto di nuove opere, valutazione di sicurezza e miglioramento/adeguamento di edifici esistenti, perizie post-sisma, relazioni di calcolo depositate al Genio Civile.",
 "vantaggi": "Quadro prestazionale esplicito: il committente capisce che 'a norma' non significa indenne ma 'non crolla e riparabile'; la doppia verifica (resistenza a SLV, spostamenti a SLD) cattura sia il collasso sia il danno economico; ζE da' un numero sintetico confrontabile.",
 "limiti": "I limiti di drift sono convenzionali e dipendenti dai tamponamenti realmente presenti; la verifica SLD spesso governa il progetto piu' della resistenza; per l'esistente il ζE sintetizza ma nasconde i meccanismi locali, che vanno verificati a parte.",
 "costi_e_economia": "Ordini di grandezza indicativi: la verifica completa agli stati limite e' parte della relazione di calcolo (per edifici residenziali ordinari 15-40 euro/m2 di progettazione strutturale complessiva); soddisfare SLD con irrigidimento mirato costa tipicamente meno del 5% della struttura se pensato in fase di concezione, molto di piu' se corretto a progetto avanzato.",
 "casi_real_world": "Caso tipo: edificio in c.a. di 6 piani con tamponature in laterizio alveolato rigidamente connesse: la verifica SLV risulta soddisfatta con margini, ma lo 0,5% di drift a SLD impone di irrigidire due telai di facciata con setti: correzione fatta in fase preliminare con costo marginale.",
 "normative": "D.M. 17/1/2018 (NTC 2018), Cap. 2 (prestazioni) e Cap. 7 (opere in zona sismica: stati limite e verifiche); Circolare 21/1/2019 n. 7; EN 1998-1 e EN 1998-3 (valutazione degli esistenti).",
 "note_cantiere": "In fase di ricognizione conta le tamponature vere, non quelle dei disegni: se il committente ha tolto i tramezzi perimetrali nel 1985, il tuo limite di drift cambia. E ricorda ai committenti che lo 0,5% e' un limite di SICUREZZA del danno, non un capriccio del progettista."
})

S.append({
 "categoria": "Sismica — analisi",
 "nome": "Modellazione e metodi di analisi: forza laterale, modale, pushover e time-history",
 "descrizione": "Come si trasforma lo spettro in forze e spostamenti sulla struttura: dai metodi lineari semplificati per edifici regolari alla dinamica non lineare per valutazioni avanzate. La scelta del metodo non e' un gusto del progettista: la norma la vincola a regolarita' e tipologia.",
 "tecnologia": "Analisi lineare statica (metodo della forza laterale, ammessa per edifici regolari e bassi); analisi lineare dinamica modale con spettro di risposta (almeno l'85% di massa partecipante, combinazione CQC, azione sulle due direzioni principali con combinazione 1,00/0,30); analisi non lineare statica (pushover con distribuzioni di forze, curva di capacita', spostamento bersaglio); analisi dinamica non lineare (accelerogrammi coerenti con lo spettro, almeno 7 set per usare la media); coefficiente di struttura q con q0 di base maggiorato per il rapporto di sovraresistenza αu/α1; classi di duttilita' CD 'A' (alta) e CD 'B' (bassa) per il c.a.",
 "applicazioni": "Edifici nuovi in c.a., acciaio, muratura e legno; valutazione degli esistenti (dove pushover e dinamica non lineare sono la norma); verifica di strutture irregolari in pianta o in elevazione.",
 "vantaggi": "La modale lineare copre la stragrande maggioranza degli edifici nuovi con costi di calcolo contenuti; la pushover mostra il meccanismo di collasso e la sequenza di plasticizzazione, informazione preziosa per il miglioramento; il coefficiente q premia la duttilita' reale.",
 "limiti": "La forza laterale sottostima la risposta di edifici alti o irregolari; il pushover con distribuzione fissa puo' mancare i modi superiori; la time-history e' potente ma sensibile alla scelta degli accelerogrammi e richiede competenze che la media degli studi non ha; un modello 3D fatto male da' numeri precisi e sbagliati.",
 "costi_e_economia": "Ordini di grandezza indicativi: analisi modale lineare di edificio ordinario inclusa nella progettazione strutturale (15-40 euro/m2 complessivi); pushover su edificio esistente per valutazione di sicurezza: 8.000-30.000 euro per edifici di 1.000-5.000 m2; analisi dinamica non lineare avanzata: oltre 30.000-80.000 euro, tipica di opere strategiche.",
 "casi_real_world": "Caso tipo: valutazione sismica di un edificio scolastico anni '70 in c.a.: l'analisi pushover evidenzia plasticizzazione precoce dei pilastri del piano terra (piano debole): intervento mirato con incamiciatura dei soli pilastri critici invece del rinforzo globale, con risparmio di circa il 40% sull'adeguamento.",
 "normative": "D.M. 17/1/2018 (NTC 2018), Cap. 7 (criteri di progettazione, metodi di analisi, coefficiente di struttura) e Cap. 8 (costruzioni esistenti); Circolare 21/1/2019 n. 7; EN 1998-1 (metodi di analisi) e EN 1998-3 (valutazione e intervento sugli esistenti).",
 "note_cantiere": "Quando ricevi il modello dal progettista, controlla tre cose prima di crederci: masse partecipanti >=85% nelle due direzioni, vincoli delle scale (spesso modellate come 'non strutturali' ma rigide davvero), e i vincoli di piano. E in cantiere: le sovraresistenze degli acciai reali contano nella gerarchia — non fare sostituzioni di barre 'piu' grosse' senza chiedere."
})

S.append({
 "categoria": "Sismica — progetto delle opere nuove",
 "nome": "Gerarchia delle resistenze e dettagli costruttivi nel cemento armato",
 "descrizione": "Il cuore della progettazione antisismica del c.a.: far plasticizzare le travi prima dei pilastri, i meccanismi flessionali prima di quelli taglianti, e confinare dove la struttura deve deformarsi senza perdere resistenza. Il terremoto non perdona i dettagli fatti male.",
 "tecnologia": "Gerarchia delle resistenze: colonne piu' resistenti delle travi concorrenti (rapporto dei momenti), taglio da capacita' maggiorato rispetto alla flessione; zone critiche con staffatura ravvicinata e confinamento (passo delle staffe, ganci a 135 gradi, uncini rientranti); nodi trave-pilastro con armature ben ancorate e continuita' delle barre; regole di sovrapposizione fuori dalle zone critiche; limiti di snellezza e assialita' dei pilastri; CD 'A' con regole complete vs CD 'B' con regole ridotte e q piu' basso.",
 "applicazioni": "Telai e pareti in c.a. di nuova costruzione in tutte le zone sismiche; rilevante anche nella valutazione degli esistenti (le carenze tipiche anni '60-'80: staffe rade, ganci a 90 gradi, sovrapposizioni nei nodi, pilastri snelli).",
 "vantaggi": "Trasforma il materiale ordinario in struttura duttile: il danno si concentra dove puo' essere riparato; le regole di dettaglio costano poco in cantiere (staffe e piegature) e valgono gran parte del coefficiente q; riduce il rischio di crolli fragili per taglio.",
 "limiti": "Richiede manodopera che sappia leggere gli esecutivi: staffe al passo sbagliato o ganci a 90 gradi vanificano il progetto; congestionamento dei nodi con ferri grandi rende difficile il getto (rischio di nidi di ghiaia proprio dove serve il confinamento).",
 "costi_e_economia": "Ordini di grandezza indicativi: l'incidenza dei dettagli antisismici (staffe ravvicinate, ganci, ancoraggi) sul costo del c.a. in opera e' dell'ordine del 3-8%; l'incamiciatura in c.a. come riparazione di pilastri carenti su esistente: 400-900 euro/m2 di superficie di pilastro trattata.",
 "casi_real_world": "Caso tipo: edificio residenziale in CD 'A': durante il getto del primo solaio il direttore dei lavori riscontra staffe dei pilastri montate a passo doppio rispetto all'esecutivo nella zona critica; blocco del getto, rifacimento delle gabbie e verbale: l'errore corretto in cantiere avrebbe reso fittizia la duttilita' di progetto.",
 "normative": "D.M. 17/1/2018 (NTC 2018), Cap. 7 (criteri di progettazione e regole per le costruzioni in c.a. in zona sismica, classi di duttilita'); Circolare 21/1/2019 n. 7; EN 1998-1 (regole di dettaglio per duttilita').",
 "note_cantiere": "Prima di ogni getto controlla fisicamente: passo staffe nelle zone critiche, ganci a 135 gradi, lunghezze di ancoraggio nei nodi, posizione delle sovrapposizioni. Fai una foto a ogni gabbia chiusa: e' la prova che il confinamento esiste davvero, e il collaudatore la apprezza."
})

S.append({
 "categoria": "Sismica — progetto delle opere nuove",
 "nome": "Strutture in acciaio e in legno in zona sismica: duttilita' e connessioni",
 "descrizione": "Due materiali con comportamento sismico opposto nel peso ma simile nella logica: l'acciaio conta sulla duttilita' dei meccanismi dissipativi progettati, il legno sulla leggerezza e sulla dissipazione concentrata nelle connessioni meccaniche. In entrambi i casi il progetto sismico e' progetto dei giunti.",
 "tecnologia": "Acciaio: telai a mensole (dissipazione nelle travi), controventi concentrici (diagonali che snervano) ed eccentrici (link dissipativi), coefficienti q tra i piu' alti della norma, controllo della snellezza locale delle piastre, connessioni a saldatura piena penetrazione o bullonate precaricate; sovraresistenza del materiale controllata (γov e limiti fy/fu). Legno: pareti e diaframmi in CLT o telaio leggero, dissipazione affidata a chiodi, viti e staffe metalliche (il legno stesso e' elastico-fragile), ancoraggi al taglio e hold-down agli angoli, rapporto rigidezza/resistenza tra piano e piano; peso ridotto = azioni sismiche basse.",
 "applicazioni": "Capannoni e edifici a medio-grande luce (acciaio); edilizia residenziale fino a 6-8 piani e sopraelevazioni (legno e CLT); ampliamenti su edifici esistenti dove il peso aggiunto e' la variabile critica.",
 "vantaggi": "Acciaio: q elevati, controllo preciso dei meccanismi, ispezione e riparazione possibili dopo l'evento. Legno: masse sismiche ridotte (l'azione cresce col peso), cantieri rapidi a secco, ottime prestazioni documentate negli eventi italiani recenti per gli edifici CLT ben dettagliati.",
 "limiti": "Acciaio: controventi concentrici con duttilita' che dipende dal dettaglio dei nodi (flussi di forza complessi); instabilita' locale se i profili sono troppo snelli. Legno: la dissipazione dipende interamente dalle connessioni (viti autofilettanti sbagliate o assenti = comportamento fragile); protezione da umidita' e fuoco da curare in modo integrale.",
 "costi_e_economia": "Ordini di grandezza indicativi: struttura in acciaio antisismica per capannoni 60-120 euro/m2 di pianta (telaio e controventi, fondazioni escluse); edificio in CLT finito di struttura 300-600 euro/m2; connessioni metalliche speciali (hold-down, piastre) 20-80 euro/pezzo posate.",
 "casi_real_world": "Caso tipo: sopraelevazione di un edificio scolastico esistente in zona 2: scelta di due piani in X-Lam proprio per limitare le azioni sismiche aggiuntive sulla struttura esistente, con hold-down dimensionati e ancoraggi chimici certificati sul cordolo esistente; collaudo con prove di trazione a campione.",
 "normative": "D.M. 17/1/2018 (NTC 2018), Cap. 4 (costruzioni in acciaio e in legno) e Cap. 7 (regole sismiche specifiche per materiale); EN 1998-1 (telai dissipativi); EN 1993-1-8 (connessioni acciaio); EN 1995-1-1 (legno).",
 "note_cantiere": "Nel legno il sisma si vince con il montaggio: ogni hold-down stretto col dinamometrico, ogni pannello fissato col passo viti dell'esecutivo (mai 'a occhio'). Nell'acciaio: le saldature delle zone dissipative vanno certificate e controllate con UT — un cordone fatto male in un link dissipativo annulla il q di progetto."
})

S.append({
 "categoria": "Sismica — edifici esistenti",
 "nome": "La valutazione sismica degli edifici esistenti: livelli di conoscenza e fattori di confidenza",
 "descrizione": "L'80% del patrimonio italiano e' anteriore alle norme sismiche moderne: valutarlo significa lavorare con informazioni incomplete. Le NTC disciplinano l'incertezza con i livelli di conoscenza: piu' indagini fai, meno penalizzazione di sicurezza subisci.",
 "tecnologia": "Livelli di conoscenza LC1, LC2, LC3 (crescenti per rilievo geometrico, dettagli costruttivi e proprieta' dei materiali) con corrispondenti fattori di confidenza FC che riducono le resistenze: 1,35 (LC1), 1,20 (LC2), 1,00 (LC3); indagini minime crescenti (carotaggi, prove su acciaio, saggi su muratura, endoscopie, martinetti piatti); modelli a telaio equivalente o a elementi finiti per la muratura; verifica sia dei meccanismi globali sia di quelli locali (ribaltamenti); indicatore ζE come rapporto tra capacita' e domanda.",
 "applicazioni": "Due diligence immobiliari, pre-valutazioni per Sismabonus e classificazione di rischio, pratiche di miglioramento e adeguamento, verifiche post-evento, edifici scolastici e strategici (censimenti pubblici).",
 "vantaggi": "Metodo coerente e ripetibile: l'incertezza e' gestita con numeri (FC), non con giudizi vaghi; investire in indagini conviene quasi sempre (passare da LC1 a LC3 riduce la penalizzazione del 26%); fornisce il ζE necessario a classificazione e incentivi.",
 "limiti": "Le indagini estese costano e disturbano gli occupanti; il modello a telaio equivalente della muratura dipende dai criteri di rigidezza scelti; per edifici eterogenei (aggregati) la valutazione del singolo fabbricato puo' non bastare: servono verifiche di aggregato.",
 "costi_e_economia": "Ordini di grandezza indicativi: campagna indagini per LC2 su edificio di 1.000-3.000 m2: 10.000-30.000 euro (rilievo + 6-10 carotaggi + saggi); valutazione sismica completa (indagini + modello + relazione): 15-40 euro/m2; su edifici strategici o complessi: oltre 50.000 euro.",
 "casi_real_world": "Caso tipo: acquisto di un immobile direzionale anni '60: la due diligence sismica in LC2 (rilievo armature con pacometro su 30 pilastri, 8 carotaggi, prove di trazione su barre) stima ζE pari a 0,45: il prezzo di acquisto viene rinegoziato scontando il miglioramento stimato.",
 "normative": "D.M. 17/1/2018 (NTC 2018), Cap. 8 (costruzioni esistenti: livelli di conoscenza, fattori di confidenza, metodi di analisi); Circolare 21/1/2019 n. 7; EN 1998-3 (valutazione e adeguamento); D.M. 58/2017 (classificazione del rischio, che richiede la valutazione).",
 "note_cantiere": "Non lesinare sul rilievo: un solaio scoperto 'voltina' quando il modello ipotizzava laterocemento cambia le masse, i periodi e le verifiche. E archivia ogni prova con posizione e foto: il FC lo difendi solo se dimostri cosa hai visto."
})

S.append({
 "categoria": "Sismica — edifici esistenti",
 "nome": "Edifici in muratura e meccanismi locali: il nemico numero uno del patrimonio storico",
 "descrizione": "Nei centri storici italiani il danno sismico nasce quasi sempre da meccanismi locali: pareti che ribaltano fuori piano, facciate che si staccano, archi e volte che cedono. La verifica dei meccanismi locali e' obbligatoria e spesso governa l'intervento piu' della resistenza globale.",
 "tecnologia": "Cinematismi lineari (ribaltamento semplice, composto, svergolamento, arco-volta) verificati con analisi limite e moltiplicatori; catene e tiranti in acciaio con capochiavi (ripristino del collegamento muro-parete); cerchiature delle aperture; cordoli e anelli in c.a. o metallici alle quote di solaio; rinforzo delle connessioni parete-solaio e parete-parete; cuciture con malte o iniezioni; controllo dell'ammorsamento degli angoli e degli angoli di facciata.",
 "applicazioni": "Centri storici, edifici rurali, chiese e monumenti (con vincoli del D.Lgs 42/2004), aggregati edilizi, verifiche post-sisma e cantieri di miglioramento diffuso.",
 "vantaggi": "Interventi sui meccanismi locali sono poco invasivi, reversibili in buona parte e ad alto rendimento: catene e connessioni ben fatte spostano la classe di rischio piu' di rinforzi muscolari; preservano il valore storico e sono compatibili col restauro.",
 "limiti": "L'efficacia dipende dai dettagli esecutivi (un tirante su muratura disgregata non tiene); gli interventi 'puntuali' non risolvono la vulnerabilita' globale se la scatola non collabora; nei beni vincolati l'iter autorizzativo con la Soprintendenza allunga i tempi.",
 "costi_e_economia": "Ordini di grandezza indicativi: catene/tiranti posati 40-100 euro/m lineare (acciaio, capochiavi, perforazioni); cerchiatura di apertura 800-2.500 euro a vano; cordolo in c.a. 80-180 euro/m; iniezioni di consolidamento murario 150-400 euro/m3 di muratura trattata.",
 "casi_real_world": "Caso tipo: edificio storico in aggregato con facciata disassata dopo evento sismico minore: verifica del cinematismo di ribaltamento con analisi limite, intervento con quattro livelli di tiranti passanti e ripresa degli angoli con cuciture in malta: ζE del meccanismo locale portato da 0,3 a oltre 1,0 con intervento da circa 40.000 euro.",
 "normative": "D.M. 17/1/2018 (NTC 2018), Cap. 8 (costruzioni esistenti: meccanismi locali e cinematismi); Circolare 21/1/2019 n. 7 (analisi limite e fattori di confidenza per la muratura); D.Lgs 42/2004 per gli edifici vincolati (autorizzazioni); EN 1998-3.",
 "note_cantiere": "Prima di tendere un tirante, verifica COSA tiene all'altro capo: su muratura a sacco disgregata serve prima la cucitura o l'iniezione locale. E controlla che i fori passanti non taglino i servizi: negli edifici abitati i tubi sono sempre dove non dovrebbero essere."
})

S.append({
 "categoria": "Sismica — classificazione e incentivi",
 "nome": "La classificazione del rischio sismico degli edifici: classi da A+ a G, PAM e IS-V",
 "descrizione": "Il D.M. 58/2017 introduce una classificazione del rischio sismico analoga a quella energetica: otto classi (da A+ a G) assegnate da tecnici abilitati su due parametri: la perdita annua media attesa (PAM, economica) e l'indice di sicurezza della struttura allo stato limite di salvaguardia della vita (IS-V). E' la base tecnica del Sismabonus e degli strumenti assicurativi.",
 "tecnologia": "Due parametri: PAM (perdita annua media attesa in % del costo di ricostruzione, da curva di vulnerabilita') e IS-V (indice di sicurezza allo SLV = rapporto capacita'/domanda, assimilabile a ζE); la classe finale e' la peggiore tra quella da PAM e quella da IS-V; attestato di classificazione firmato da professionista abilitato; aggiornamento obbligatorio dopo interventi che modificano la struttura; metodo convenzionale semplificato per gli edifici ordinari.",
 "applicazioni": "Pratiche Sismabonus (classificazione ante e post intervento per documentare il salto di classe), polizze parametriche e catastrofali, rating degli immobili strategici, programmazione degli investimenti di mitigazione su portafogli immobiliari.",
 "vantaggi": "Rende il rischio sismico comunicabile a committenti, banche e assicurazioni (una lettera, non una relazione di 200 pagine); crea un mercato per il miglioramento documentato; il salto di classe e' verificabile e controllabile dall'AdE.",
 "limiti": "Il metodo convenzionale semplificato e' prudente ma grossolano (puo' classificare peggio edifici ben costruiti); la PAM dipende dai costi di ricostruzione assunti; la classe e' una fotografia: ammodernamenti impiantistici o cambi d'uso non la aggiornano automaticamente.",
 "costi_e_economia": "Ordini di grandezza indicativi: classificazione sismica di edificio residenziale ordinario 1.500-6.000 euro (con rilievo); per condomini complessi o immobili produttivi 5.000-20.000 euro; in genere compresa nella valutazione sismica se gia' in corso.",
 "casi_real_world": "Caso tipo: condominio anni '70 che esegue miglioramento sismico (cerchiature, FRP sui nodi, tiranti): classificazione ante-operam classe F, post-operam classe C documentata dai due attestati: accesso documentato alle detrazioni previste per il salto di rischio e valutazione immobiliare aggiornata.",
 "normative": "D.M. 28 febbraio 2017 n. 58 (linee guida per la classificazione del rischio sismico delle costruzioni); D.M. 28 febbraio 2017 n. 65 (linee guida per gli interventi di riduzione del rischio — collegamento col Sismabonus); D.M. 17/1/2018 (parametri di riferimento per la valutazione).",
 "note_cantiere": "Le due classificazioni (ante e post) vanno fatte dallo stesso tecnico con la stessa base conoscitiva: due metodi diversi producono salti di classe fittizi che l'Agenzia delle Entrate contesta. E conserva TUTTA la documentazione delle indagini: in caso di controllo e' la tua difesa."
})

S.append({
 "categoria": "Sismica — protezione avanzata",
 "nome": "L'isolamento sismico alla base: principi, dispositivi e progetto del gap sismico",
 "descrizione": "La strategia che 'scollega' l'edificio dal terreno: dispositivi flessibili orizzontalmente interposti tra fondazioni e sopraelevazione allungano il periodo proprio e riducono drasticamente le accelerazioni trasmesse. Tecnologia matura e codificata, usata in Italia su scuole, ospedali e edifici strategici.",
 "tecnologia": "Dispositivi: isolatori elastomerici a gomma naturale ad alto smorzamento (HDRB), elastomerici con nucleo di piombo (LRB), pendoli a scorrimento (FPS) a una o piu' superfici; combinazione isolamento+dissipazione; allungamento del periodo oltre 2-3 volte quello della struttura fissa; il GAP SISMICO (giunto di dilatazione perimetrale e vano tecnico) dimensionato sullo spostamento massimo di progetto: e' il punto critico del sistema; protezione antincendio e ispezionabilita' dei dispositivi; prove di accettazione in fabbrica e controlli in cantiere.",
 "applicazioni": "Ospedali, scuole, centri di emergenza, edifici strategici (dove l'operativita' post-sisma e' prioritaria); edifici nuovi su terreni ad alta pericolosita'; piu' raro e complesso in esistente (richiede il taglio alla base: 'base isolation retrofit').",
 "vantaggi": "Riduzione delle accelerazioni in sopraelevazione anche dell'80%: danni a struttura, tamponature, impianti e contenuti quasi annullati (protegge anche il valore del contenuto: archivi, apparecchiature); struttura che resta elastica; comfort e operativita' post-evento; soluzione spesso competitiva per edifici strategici.",
 "limiti": "Costo iniziale maggiore e interfaccia complessa con fondazioni, scale, ascensori e servizi (tutto cio' che attraversa il gap deve essere flessibile); richiede manutenzione programmata e ispezione dei dispositivi; non adatto a terreni molto soffici con spettri a lungo periodo senza analisi dedicate; retrofit su esistente tecnicamente possibile ma costoso e invasivo.",
 "costi_e_economia": "Ordini di grandezza indicativi: sovraccosto della struttura isolata vs tradizionale +8-15% sulla struttura (parzialmente compensato da sezioni ridotte in elevazione); dispositivi isolatori 1.500-6.000 euro/pz a seconda di taglia e prove; retrofit con taglio alla base su esistente: 300-800 euro/m2 di pianta.",
 "casi_real_world": "Caso tipo: nuovo ospedale in zona ad alta pericolosita': 120 isolatori HDRB su piastra di base con gap sismico perimetrale di 40 cm, giunti flessibili su tutti gli attraversamenti impiantistici; prove di accettazione su ogni lotto di dispositivi con curve forza-spostamento certificate prima della posa.",
 "normative": "D.M. 17/1/2018 (NTC 2018), Cap. 7 (sezione dedicata a strutture con isolamento e dissipazione); Circolare 21/1/2019 n. 7 (progetto, prove e accettazione); UNI EN 15129 (dispositivi antisismici: requisiti, prove e marcatura); EN 1998-1 e EN 1998-2 per il quadro europeo.",
 "note_cantiere": "Il gap sismico e' sacro: niente marciapiedi rigidi contro la parete mobile, niente scale fisse che lo attraversano, niente 'riempimenti' di cantiere dimenticati. Ispeziona ogni dispositivo prima della posa (niente bolle, giunti vulcanizzati integri) e archivia i certificati di prova per lotto: il collaudo statico li pretende."
})

S.append({
 "categoria": "Sismica — protezione avanzata",
 "nome": "La dissipazione energetica: dissipatori isteretici, viscosi, ad attrito e TMD",
 "descrizione": "L'altra strategia della protezione passiva: inserire nella struttura 'fusibili' meccanici che assorbono energia sismica deformandosi o scorrendo, proteggendo gli elementi portanti. Applicabile sia al nuovo sia — ed e' il suo punto di forza — al miglioramento dell'esistente.",
 "tecnologia": "Dissipatori isteretici metallici (snervamento controllato di acciaio, incluse le BRB — controventi ad instabilita' vincolata), dissipatori viscosi (olio, forza dipendente dalla velocita': non aggiungono forze statiche), dissipatori ad attrito e viscoelastici; posizionamento tipico nelle maglie di controvento o come link tra edifici; TMD (masse accordate) per il controllo dinamico di strutture snelle; modellazione con legami non lineari; prove di qualificazione e accettazione secondo UNI EN 15129.",
 "applicazioni": "Miglioramento sismico di edifici esistenti in c.a. e acciaio senza irrigidimento globale invasivo; ponti e opere civili; edifici snelli con problemi di comfort dinamico; protezione di contenuti sensibili (viscosi).",
 "vantaggi": "Sull'esistente evita il rinforzo 'muscolare' diffuso: i dissipatori si concentrano in poche maglie, cantieri piu' veloci e meno invasivi; le BRB sono sostituibili dopo l'evento (concetto di fusibile); i viscosi sono trasparenti ai carichi statici e termici.",
 "limiti": "Costo per dispositivo e ingegneria dedicata (modelli non lineari obbligatori); manutenzione e ispezione programmate; le connessioni tra dissipatore e struttura esistente sono il punto critico (aderenza ai valori di progetto delle resistenze di ancoraggio); disponibilita' e tempi di approvvigionamento dei dispositivi.",
 "costi_e_economia": "Ordini di grandezza indicativi: BRB 3.000-15.000 euro/pz installati a seconda della forza; dissipatori viscosi 2.000-8.000 euro/pz; intervento tipico di miglioramento con dissipatori su edificio di 2.000-5.000 m2: 100-300 euro/m2 contro 200-500 euro/m2 del rinforzo diffuso tradizionale (confronto indicativo, dipende dal caso).",
 "casi_real_world": "Caso tipo: palazzo direzionale anni '70 con telai in c.a. poco duttili: miglioramento con 24 BRB inseriti nelle maglie centrali delle facciate corte, senza toccare gli uffici operativi; analisi pushover prima/dopo: spostamento di collasso aumentato del 60%, cantiere concluso in 5 mesi senza sgomberare l'edificio.",
 "normative": "D.M. 17/1/2018 (NTC 2018), Cap. 7 (isolamento e dissipazione) e Cap. 8 (interventi su esistente); UNI EN 15129 (dispositivi antisismici: qualificazione e prove); EN 1998-1 e EN 1998-3.",
 "note_cantiere": "I dispositivi arrivano con curve certificate: fai coincidere numero di serie, posizione in pianta e verbale di posa. E non 'migliorare' gli ancoraggi dei dissipatori senza il progettista: se la piastra cede prima del dissipatore, hai pagato un fusibile che non puo' mai scattare."
})

S.append({
 "categoria": "Sismica — elementi non strutturali",
 "nome": "Tamponature, partizioni, impianti e contenuti: il danno che costa di piu'",
 "descrizione": "Nei terremoti moderni la struttura regge e il conto lo pagano gli elementi non strutturali: tamponature che si disarticolano, controsoffitti che cadono, impianti che si staccano, contenuti che si rovesciano. Le NTC impongono verifiche esplicite: la protezione del 'non strutturale' e' oggi parte del progetto.",
 "tecnologia": "Verifica degli elementi non strutturali agli spostamenti interpiano (SLD) e alle forze inerziali di piano (SLV) con coefficienti di amplificazione per quota e importanza; connessioni scorrevoli o deformabili delle tamponature (giunti perimetrali, profili di scorrimento); ancoraggio di controsoffitti, canalizzazioni e apparecchi sospesi; sistemi costruttivi a secco con telai scorrevoli; protezione di scale e vani (percorsi di esodo); dispositivi antisismici per contenuti (vincoli di arredi tecnici, mensole ancorate).",
 "applicazioni": "Ospedali e scuole (continuita' operativa), data center e archivi, edifici industriali con impianti di processo, musei e depositi (contenuti di valore), edilizia residenziale per la riduzione del danno e dei costi di riparazione.",
 "vantaggi": "Riduce drasticamente i costi di riparazione post-sisma (spesso superiori al danno strutturale); protegge le vie di esodo e la funzionalita'; le connessioni deformabili delle tamponature riducono anche le fessurazioni da vento e ritiro.",
 "limiti": "Dettagli esecutivi ancora poco conosciuti dalla filiera (giunti fatti 'come sempre' vanificano il progetto); leggero incremento dei costi di tamponatura; coordinamento progettuale strutture-architettura-impianti piu' impegnativo.",
 "costi_e_economia": "Ordini di grandezza indicativi: tamponatura con connessioni deformabili +10-25% sulla sola tamponatura (ordine 15-40 euro/m2 di parete); ancoraggi antisismici di impianti sospesi: 5-15 euro/kg sospeso installato; l'investimento tipico si ripaga con un solo evento SLD evitato.",
 "casi_real_world": "Caso tipo: scuola nuova in zona 1 progettata con tamponature su profili di scorrimento e controsoffitti ancorati: dopo evento sismico moderato la struttura e' integra e le uniche riparazioni sono locali (stuccature ai giunti), con riapertura immediata; il plesso gemello con dettagli tradizionali in zona 2 ha richiesto mesi di ripristino delle tamponature fessurate.",
 "normative": "D.M. 17/1/2018 (NTC 2018), Cap. 7 (verifiche degli elementi costruttivi non strutturali e degli impianti) e Cap. 3 (azione sismica sugli elementi non strutturali); EN 1998-1 (elementi non strutturali); UNI EN 15129 solo per i dispositivi.",
 "note_cantiere": "Il giunto perimetrale della tamponatura va lasciato LIBERO e sigillato con materiale elastico: se lo murano pieno 'per finire prima' hai reintrodotto il meccanismo fragile che il progetto eliminava. Passa in cantiere alla chiusura delle tamponature, non a fine lavori."
})

S.append({
 "categoria": "Sismica — cantiere e qualita'",
 "nome": "Il cantiere del miglioramento sismico: sequenze, controlli in opera ed errori tipici",
 "descrizione": "L'intervento antisismico sull'esistente si vince in cantiere: FRP che aderisce, betoncino con rete ben connessa, tiranti tesi, nodi ripresi. La qualita' esecutiva determina se la classe di rischio dichiarata e' vera o solo su carta.",
 "tecnologia": "Tecnologie principali: FRP (tessuti carbonio/vetro/basalto con resine epossidiche, preparazione del supporto, prove di aderenza pull-off), betoncino armato (malte o betoncini con rete elettrosaldata o in GFRP, connettori passanti), incamiciature in c.a. o acciaio, tiranti e catene, cuciture e iniezioni; controlli: prove di aderenza a strappo su FRP, prove di trazione su barre e connettori, saggi di verifica, verbali di nascosto (armature prima della copertura); sequenza tipica: opere preliminari, connessioni, rinforzi locali, rinforzi globali, ripristini.",
 "applicazioni": "Miglioramento e adeguamento di edifici residenziali, scolastici e produttivi esistenti; cantieri in edifici occupati (fasi e sicurezza); pratiche con classificazione del rischio ante/post.",
 "vantaggi": "Tecnologie leggere e rapide (FRP: pochi mm di spessore, nessun sovraccarico); cantieri compatibili con edifici parzialmente in uso; controlli in opera semplici e documentabili (pull-off, trazione) danno garanzia oggettiva al collaudatore.",
 "limiti": "L'aderenza al supporto e' il tallone d'Achille: supporto umido, polveroso o sfarinato = FRP che si distacca; le resine hanno finestre di temperatura e umidita' (cantieri invernali problematici); i costi reali dipendono dai ponteggi e dai ripristini piu' che dai materiali.",
 "costi_e_economia": "Ordini di grandezza indicativi: FRP installato 80-250 euro/m2 (supporto, tessuto, resina, protezione); betoncino armato 300-600 euro/m2; incamiciatura pilastri 400-900 euro/m2 di superficie pilastro; prove di aderenza 150-400 euro/serie; miglioramento sismico diffuso di edificio residenziale: 150-500 euro/m2 di pavimento secondo intensita' dell'intervento.",
 "casi_real_world": "Caso tipo: miglioramento sismico di una scuola con FRP sui nodi e betoncino sulle pareti corte: il protocollo di cantiere prevede pull-off su ogni 50 m2 di tessuto e prova di trazione su un connettore ogni 200; due lotti bocciati per aderenza insufficiente vengono rifatti prima della chiusura: il collaudo statico passa senza rilievi.",
 "normative": "D.M. 17/1/2018 (NTC 2018), Cap. 8 e Cap. 4 (materiali e controlli); Circolare 21/1/2019 n. 7; istruzioni CNR-DT 200 e serie (documenti tecnici su FRP — riferimenti tecnici consolidati); D.Lgs 81/2008 per il cantiere in edifici occupati; D.M. 58/2017 per la classificazione ante/post.",
 "note_cantiere": "Tre controlli non negoziabili: sandblast o idrosabbiatura e verifica del supporto prima della resina, pull-off documentato per lotti, e foto di ogni armatura PRIMA della chiusura. E attenzione alle finestre ambientali delle resine: un getto di FRP a 5 gradi e umidita' alta e' un lavoro da rifare, non da collaudare."
})

def main():
    os.makedirs(os.path.join(BASE, 'schede'), exist_ok=True)
    with open(os.path.join(BASE, 'schede', 'schede.jsonl'), 'w', encoding='utf-8') as f:
        for s in S:
            assert list(s.keys()) == KEYS, f"chiavi errate: {s['nome']}"
            f.write(json.dumps(s, ensure_ascii=False) + '\n')

    course = '''corso: "Ingegneria sismica e protezione sismica: pericolosita' e spettri, stati limite, analisi, gerarchia delle resistenze, acciaio e legno in sisma, valutazione degli esistenti, muratura e meccanismi locali, classificazione del rischio D.M. 58/2017, isolamento alla base, dissipazione, elementi non strutturali, cantiere del miglioramento"
facolta: "FACOLTA_INGEGNERIA"
livello: "L2-L3"
schede: 12
formato: "JSONL"
lingua: "it"
schema_campi: [categoria, nome, descrizione, tecnologia, applicazioni, vantaggi, limiti, costi_e_economia, casi_real_world, normative, note_cantiere]
fonti: "D.M. 17/1/2018 NTC 2018 (Cap. 2 prestazioni, Cap. 3 azione sismica, Cap. 7 opere in zona sismica, Cap. 8 costruzioni esistenti), Circolare 21/1/2019 n. 7, EN 1998-1 (progetto), EN 1998-3 (esistenti), EN 1993-1-8 (connessioni acciaio), EN 1995-1-1 (legno), UNI EN 15129 (dispositivi antisismici), D.M. 28/2/2017 n. 58 (classificazione del rischio sismico) e n. 65 (linee guida riduzione del rischio), L. 64/1974 (impianto storico), D.Lgs 42/2004 (vincoli), documenti tecnici CNR-DT 200 (FRP), D.Lgs 81/2008 (cantiere)"
nota_metodologica: "Corso tecnico completo di ingegneria sismica: pericolosita' (reticolo, ag/Fo/Tc*, sottosuolo A-E, TR 30/50/475/712), stati limite e drift (0,5-1%), metodi di analisi (forza laterale, modale 85%, pushover, time-history, q e CD A/B), gerarchia delle resistenze e dettagli c.a., acciaio e legno in sisma, edifici esistenti (LC1-LC3, FC 1,35/1,20/1,00), muratura e meccanismi locali (cinematismi), classificazione del rischio D.M. 58/2017 (classi A+→G, PAM, IS-V), isolamento alla base (HDRB/LRB/FPS, gap sismico), dissipazione (BRB, viscosi, attrito), elementi non strutturali (tamponature e impianti), cantiere del miglioramento (FRP, betoncino, controlli). NON ridondante: INGEGNERIA_STRUTTURALE_PACK ha 1 scheda di panorama sismico, FORMULARIO_STRUTTURE_PACK le formule, RISANAMENTO_E_RECUPERO_EDILIZIO_PACK il miglioramento lato recupero: qui il corso dedicato completo, con isolamento e dissipazione assenti altrove. Norme solo di consolidata certezza; prezzi come fasce indicative; nessun nome di azienda."
'''
    with open(os.path.join(BASE, 'COURSE.yaml'), 'w', encoding='utf-8') as f:
        f.write(course)

    readme = '''# Ingegneria sismica e protezione sismica

Corso L2-L3 della Facolta di Ingegneria: il progetto e la valutazione antisismica come disciplina completa — pericolosita' e spettri di progetto (reticolo nazionale, categorie di sottosuolo, periodi di ritorno), stati limite e spostamenti interpiano, metodi di analisi (lineare statica e modale, pushover, time-history) e coefficiente di struttura, gerarchia delle resistenze e dettagli costruttivi nel c.a., acciaio e legno in zona sismica, valutazione degli edifici esistenti (livelli di conoscenza LC1-LC3 e fattori di confidenza), meccanismi locali della muratura, classificazione del rischio sismico D.M. 58/2017 (classi A+→G, PAM, IS-V), isolamento sismico alla base (HDRB, LRB, FPS e gap sismico), dissipazione energetica (BRB, viscosi, attrito), verifica degli elementi non strutturali (tamponature, impianti, contenuti) e cantiere del miglioramento sismico (FRP, betoncino, controlli in opera).

**Schede: 12**

Non ridondante con INGEGNERIA_STRUTTURALE_PACK (1 scheda di panorama sismico), FORMULARIO_STRUTTURE_PACK (formule) e RISANAMENTO_E_RECUPERO_EDILIZIO_PACK (miglioramento lato recupero): qui il corso tecnico dedicato, inclusi isolamento e dissipazione, non trattati altrove.
'''
    with open(os.path.join(BASE, 'README.md'), 'w', encoding='utf-8') as f:
        f.write(readme)

    print(f"Creato {BASE}: {len(S)} schede")

if __name__ == '__main__':
    main()
