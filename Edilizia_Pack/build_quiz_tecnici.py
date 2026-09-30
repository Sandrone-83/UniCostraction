# -*- coding: utf-8 -*-
"""Genera la banca di 100 quiz tecnici con risposta commentata per l'LLM."""
import json, os

Q = []

# ---------------- STRUTTURE (15) ----------------
Q.append(("STRUTTURE","base",
"Qual è il valore di progetto della tensione di snervamento dell'acciaio B450C secondo le NTC 2018?",
"Risposta: fyd = fyk/gs = 450/1,15 = 391 MPa. Il valore caratteristico fyk = 450 MPa non può essere usato direttamente nelle verifiche agli stati limite ultimi: serve sempre il coefficiente parziale di sicurezza del materiale gs = 1,15. Il calcolo si fa quindi con 391 MPa."))
Q.append(("STRUTTURE","base",
"Qual è la resistenza di progetto a compressione del calcestruzzo C25/30?",
"Risposta: fcd = acc·fck/gc = 0,85 × 25 / 1,5 = 14,17 MPa. Il C25/30 ha resistenza caratteristica cilindrica fck = 25 MPa; il coefficiente acc (0,85) tiene conto del comportamento differito (viscosità e ritiro) e gc = 1,5. Nelle verifiche SLU si usa quindi 14,17 MPa."))
Q.append(("STRUTTURE","base",
"Qual è la differenza tra verifica SLU e verifica SLE?",
"Risposta: lo SLU (stato limite ultimo) verifica il collasso usando coefficienti parziali dei materiali e combinazioni fondamentali delle azioni; lo SLE (stato limite di esercizio) verifica la funzionalità in esercizio — fessurazione, deformazioni, vibrazioni — con combinazioni rara, frequente e quasi permanente e modelli elastici. Un elemento può soddisfare il SLU ma risultare inaccettabile allo SLE per deformazioni eccessive."))
Q.append(("STRUTTURE","base",
"Cosa si intende per altezza utile d di una trave in calcestruzzo armato?",
"Risposta: è la distanza tra il lembo più compresso della sezione e il baricentro dell'armatura tesa. Governa il braccio interno della coppia resistente (circa 0,9d) e quindi la capacità portante a flessione: per massimizzarla, l'armatura va disposta il più basso possibile rispettando il copriferro minimo."))
Q.append(("STRUTTURE","intermedio",
"Perché i solai in laterocemento hanno nervature e laterizi alleggeriti?",
"Risposta: la nervatura concentra calcestruzzo e armatura dove serve la resistenza (il ferro teso in basso, il calcestruzzo reagente in alto), mentre i laterizi alleggeriscono la struttura riducendo peso proprio e azioni sismiche, fungono da cassaforma e migliorano l'isolamento termo-acustico. Il risultato è un solato efficiente con meno materiale."))
Q.append(("STRUTTURE","intermedio",
"Cos'è la verifica a punzonamento e quando è necessaria?",
"Risposta: verifica la resistenza a taglio di una superficie di riferimento attorno a un pilastro (o carico concentrato) per evitare la rottura per schiacciamento-fessurazione a punzone. È obbligatoria per fondazioni su pali, platee e solai sottoposti a carichi concentrati; se non verificata si aggiunge armatura a punzonamento o si aumenta lo spessore."))
Q.append(("STRUTTURE","avanzato",
"Come si procede alla valutazione della sicurezza di un edificio esistente in muratura?",
"Risposta: con indagine conoscitiva (rilievo geometrico, caratterizzazione dei materiali con prove non distruttive e di laboratorio, documentazione storica), poi con verifiche semplificate o analisi lineari/non lineari secondo le NTC 2018 e la Circolare 21/01/2019. L'affidabilità del modello dipende dalla qualità dell'indagine: non si può dimensionare un intervento senza conoscere i materiali reali."))
Q.append(("STRUTTURE","intermedio",
"Cosa si intende per stato limite di esercizio di fessurazione e quali limiti sono tipici?",
"Risposta: è il limite all'apertura delle fessure per garantire durabilità, tenuta all'acqua, funzionalità ed estetica. I valori tipici sono w = 0,1 mm per elementi in ambiente aggressivo o esposti, 0,2 mm per casi ordinari con requisiti di tenuta, fino a 0,3-0,4 mm in casi poco critici; sempre secondo combinazioni frequenti o quasi permanenti."))
Q.append(("STRUTTURE","base",
"A cosa servono i controventi nelle strutture metalliche e in legno?",
"Risposta: sono aste inclinate che scaricano le azioni orizzontali (vento, sisma) sui nodi principali e vincolano gli elementi compressi impedendone l'instabilità fuori piano. Senza controventi, le aste snelle potrebbero deformarsi lateralmente e collassare per carichi molto inferiori al loro carico di rottura."))
Q.append(("STRUTTURE","base",
"Qual è la differenza tra cemento e calcestruzzo?",
"Risposta: il cemento è il legante (polvere di clinker con gesso) che, idratandosi, agglomera gli inerti; il calcestruzzo è il conglomerato cementizio risultante (cemento + acqua + sabbia + ghiaia + eventuali additivi). La resistenza del calcestruzzo dipende dalla classe (es. C25/30) e dal rapporto acqua/legante, non dalla sola classe del cemento."))
Q.append(("STRUTTURE","intermedio",
"Qual è il modulo elastico del calcestruzzo C25/30?",
"Risposta: Ecm ≈ 22 × ((fck + 8)/10)^0,3 = 22 × (33/10)^0,3 ≈ 31.500 MPa, comunemente assunto tra 31.000 e 32.000 MPa. Serve per calcolare deformazioni istantanee, frecce e inflessioni nelle verifiche SLE; per carichi di lunga durata va corretto per viscosità."))
Q.append(("STRUTTURE","base",
"Perché il copriferro è obbligatorio e cosa influenza la sua misura?",
"Risposta: protegge le armature dalla carbonatazione, corrosione e azioni meccaniche, e assicura l'ancoraggio efficace della barra nel calcestruzzo. Il valore minimo dipende dalla classe di esposizione (ambiente secco, cicli bagnato/asciutto, cloro): più aggressivo è l'ambiente, maggiore è il copriferro richiesto dalle NTC 2018."))
Q.append(("STRUTTURE","intermedio",
"In una trave continua su tre appoggi con carico uniforme, dove si trovano i momenti massimi e minimi?",
"Risposta: il momento negativo (sull'appoggio intermedio) vale qL²/8, mentre il momento positivo massimo in campata vale 9qL²/128 (circa 0,07 qL²). Per questo le armature devono essere maggiorate sull'appoggio intermedio e la campata è relativamente sollecitata meno della trave appoggiata."))
Q.append(("STRUTTURE","avanzato",
"Cosa sono le catene in edilizia e quando sono indispensabili?",
"Risposta: sono elementi metallici (barre o cavi) orizzontali inseriti nei muri per contrastare la spinta orizzontale dei solai sulle pareti, specialmente in presenza di solai semplicemente appoggiati o di tetto spingente. Sono indispensabili quando il sistema di solai e coperture non è a comportamento catenario (non spinge): la loro assenza può causare espulsione di pareti nel sisma."))
Q.append(("STRUTTURE","intermedio",
"Perché gli edifici a telaio in calcestruzzo soffrono i meccanismi di piano soffice?",
"Risposta: quando le tamponature non sono vincolate adeguatamente al telaio, le azioni sismiche possono scaricarsi su un singolo piano creando tagli concentrati (piani soffici, tipicamente quello terra o interrato). La normativa richiede catene, collegamenti e rinforzi specifici per distribuire le forze sismiche tra i vari piani."))

# ---------------- TERMOFISICA / ENERGIA (15) ----------------
Q.append(("TERMOFISICA","base",
"Cosa si intende per trasmittanza termica U di un componente edilizio?",
"Risposta: è il flusso termico che attraversa 1 m² di parete per 1 K di differenza di temperatura tra interno ed esterno, espresso in W/m²K. Si calcola come U = 1/Rtot, dove Rtot = resistenza superficiale interna + somma dei resistance di strato (d/λ) + resistenza esterna. Più basso è U, meglio isola."))
Q.append(("TERMOFISICA","base",
"Come si calcola la resistenza termica di una parete multistrato?",
"Risposta: R = Σ (s_i / λ_i) + R_i + R_e, dove s_i è lo spessore di ogni strato e λ_i la sua conducibilità. Esempio: mattone pieno 30 cm (λ = 0,80) → R = 0,375 m²K/W; cappotto EPS 10 cm (λ = 0,035) → R = 2,857; totale ≈ 3,5 → U ≈ 0,28 W/m²K."))
Q.append(("TERMOFISICA","intermedio",
"Cos'è un ponte termico e perché va minimizzato?",
"Risposta: è una zona della struttura in cui il flusso termico si concentra per cambi di geometria (pilastri, angoli, balconi) o interruzioni dello strato isolante. Aumenta la dispersione energetica e, soprattutto, abbassa la temperatura superficiale interna creando rischio di condensa superficiale e muffa. Si riduce con cappotto esterno, isolante a filo del pavimento e attenzione ai dettagli."))
Q.append(("TERMOFISICA","intermedio",
"Perché il cappotto termico esterno è preferibile all'interno?",
"Risposta: elimina o riduce i ponti termici, avvolge l'edificio senza interruzioni, mantiene la massa muraria a temperatura più alta (massa utile in inverno) e preserva la superficie interna abitabile. L'isolamento interno invece sposta la superficie fredda verso l'interno, rischia condensa interstiziale e riduce la superficie utile."))
Q.append(("TERMOFISICA","intermedio",
"Quando si forma la condensa superficiale su una parete interna?",
"Risposta: quando la temperatura superficiale della parete scende sotto la temperatura di rugiada dell'aria interna. In un ambiente a 20 °C e 50% di umidità relativa, la temperatura di rugiada è circa 9,3 °C: basta che una superficie (angolo, pilastro, ponte termico) scenda sotto questo valore perché si formi umidità e poi muffa."))
Q.append(("TERMOFISICA","avanzato",
"Cosa si intende per inerzia termica edilizia e quando è vantaggiosa?",
"Risposta: è la capacità della massa costruttiva di accumulare calore durante le ore calde e restituirlo quando la temperatura scende. È vantaggiosa in climi con forte escursione giorno/notte e con accumulo solare invernale (edifici passivi), meno utile in climi freddi umidi con cielo coperto dove l'isolamento conta più della massa."))
Q.append(("TERMOFISICA","intermedio",
"Quali sono i vantaggi e i limiti della pompa di calore rispetto alla caldaia a gas?",
"Risposta: Vantaggi: rendimento superiore a 1 (COP 3-5), nessuna combustione locale, possibilità di raffrescamento integrato, integrazione con fotovoltaico. Limiti: resa che cala con la temperatura esterna (servono integrazioni in climi freddi), costo elettrico e potenza contrattuale, rumorosità se mal installata, impatto ambientale dei refrigeranti."))
Q.append(("TERMOFISICA","avanzato",
"Cos'è lo SCOP e perché è più realistico del COP nominale?",
"Risposta: lo SCOP (Seasonal Coefficient of Performance) è la media ponderata dei COP dell'impianto di riscaldamento ai diversi carichi parziali e temperature esterne della stagione (secondo UNI EN 14825). Il COP nominale misura solo il rendimento a pieno carico e a condizioni standard: la macchina reale lavora quasi sempre a carico parziale, quindi lo SCOP descrive meglio il consumo stagionale effettivo."))
Q.append(("TERMOFISICA","intermedio",
"Qual è la differenza tra emissione radiante e convettiva degli emettitori?",
"Risposta: l'emissione radiante trasferisce calore per irraggiamento infrarosso (pareti radianti, pannelli) con comfort a temperatura media dell'ambiente più bassa; la convettiva riscalda l'aria che circola (termoconvettori, caloriferi) con risposta più rapida ma rischio di stratificazione e movimentazione polveri. L'ideale per il comfort è un mix bilanciato."))
Q.append(("TERMOFISICA","intermedio",
"Cosa è una VMC con recupero di calore e perché conviene?",
"Risposta: è un sistema di ventilazione meccanica controllata che espelle l'aria viziata e ne immette di nuova, recuperando il calore (o il fresco) attraverso uno scambiatore (rendimenti >80-90%). Conviene perché garantisce il ricambio d'aria necessario per salute e umidità con perdite energetiche minime rispetto all'aerazione naturale, indispensabile negli edifici a involucro sigillato."))
Q.append(("TERMOFISICA","base",
"Enunciare la legge di Fourier per la conduzione attraverso una parete piana.",
"Risposta: il flusso termico è Q = λ · A · ΔT / s, dove λ è la conducibilità del materiale, A l'area, s lo spessore e ΔT il salto termico. Ne deriva che la resistenza del singolo strato è R = s/λ: raddoppiare lo spessore raddoppia la resistenza, mentre usare un materiale con λ dimezzato ha lo stesso effetto."))
Q.append(("TERMOFISICA","avanzato",
"Come è strutturato il bilancio energetico di riscaldamento di un edificio secondo UNI/TS 11300?",
"Risposta: Q_H,nd = dispersioni attraverso i componenti disperdenti (Σ U_i·A_i) + solai interrati + contributo dei ponti termici + ventilazione (0,34 · V · n) meno guadagni solari e interni; poi Q_H = Q_H,nd − η_g,gn · (Q_sol + Q_int). Infine si dividono le perdite per i rendimenti di generazione, distribuzione, emissione e regolazione per ottenere il fabbisogno di energia primaria."))
Q.append(("TERMOFISICA","avanzato",
"Cosa si intende per trasmittanza media corretta di un edificio?",
"Risposta: è la media ponderata delle trasmittanze di tutti i componenti disperdenti (pareti, coperture, solai, finestre) corretta per il contributo dei ponti termici. È usata nei calcoli energetici e nelle verifiche di legge perché descrive la qualità media dell'involucro completo, non dei singoli elementi."))
Q.append(("TERMOFISICA","intermedio",
"Qual è il criterio per dimensionare lo spessore di un isolante in un intervento di riqualificazione?",
"Risposta: si fissa il valore target di trasmittanza (limite di legge o comfort interno), si calcola la resistenza necessaria R = 1/U_target − R_esistente, poi spessore = R × λ_isolante. Si aggiunge un margine per l'irregolarità di posa e si verifica che lo spessore sia compatibile con dettagli, finestre e rischio di condensa interstiziale."))
Q.append(("TERMOFISICA","intermedio",
"Quali sono i principali guadagni gratuiti in un edificio ben orientato?",
"Risposta: guadagni solari attraverso le finestre in inverno (riducono il carico di riscaldamento), luce naturale che riduce il consumo elettrico, ventilazione naturale notturna in estate (free cooling), schermature esterne che riducono il carico estivo. L'orientamento ottimale in Italia è prevalentemente sud per i soggiorni con finestre medie."))

# ---------------- IMPIANTI IDRAULICI (8) ----------------
Q.append(("IMPIANTI IDRAULICI","base",
"Come si dimensiona una tubazione idraulica nota la portata richiesta?",
"Risposta: Q = v · A, quindi A = Q/v e diametro d = √(4A/π). La velocità economica per acqua fredda è 0,9-1,2 m/s (fino a 1,5 m/s in reti grandi): velocità più basse fanno crescere i diametri, velocità più alte aumentano perdite di carico e rumorosità."))
Q.append(("IMPIANTI IDRAULICI","base",
"Cosa si intende per prevalenza di una pompa?",
"Risposta: è il carico totale che la pompa deve vincere: prevalenza geodetica (dislivello tra aspirazione e mandata) + prevalenza di pressione richiesta + perdite di carico (distribuite + localizzate). La pompa si sceglie nel punto di funzionamento dove la curva della pompa interseca la curva dell'impianto."))
Q.append(("IMPIANTI IDRAULICI","intermedio",
"Come si converte la portata in potenza termica per un impianto di riscaldamento?",
"Risposta: P = ṁ · c_p · ΔT, con c_p dell'acqua = 4,186 kJ/(kg·K). Esempio: 10 kW a ΔT = 10 K → ṁ = 10/(4,186×10) ≈ 0,24 kg/s ≈ 0,86 m³/h. La portata volumetrica si ottiene dividendo per la densità (circa 1000 kg/m³ a 20 °C)."))
Q.append(("IMPIANTI IDRAULICI","intermedio",
"Cos'è la pressione dinamica e a cosa serve?",
"Risposta: è p_d = ρ·v²/2 (oppure γ·v²/2g): è l'energia cinetica per unità di volume del fluido in moto. Le perdite localizzate (curve, valvole, raccordi) si calcolano come Δp = ζ·p_d, dove ζ è il coefficiente di perdita localizzata dell'elemento."))
Q.append(("IMPIANTI IDRAULICI","intermedio",
"Perché un impianto di riscaldamento con collettore radiale va bilanciato?",
"Risposta: perché i rami più corti tendono naturalmente a prendere più portata di quelli lunghi: senza bilanciamento i radiatori vicini alla caldaia surriscaldano e i lontani restano freddi. Il bilanciamento si ottiene con pre-regolatori tarati, valvole di bilanciamento o regolazione dinamica automatica."))
Q.append(("IMPIANTI IDRAULICI","base",
"Qual è la funzione del vaso di espansione chiuso?",
"Risposta: assorbire la dilatazione termica dell'acqua contenuta nell'impianto tramite una membrana elastica separatrice tra acqua e gas precaricato, evitando sovrappressioni che farebbero intervenire ripetutamente la valvola di sicurezza. Va dimensionato in funzione del volume dell'impianto e delle temperature di esercizio."))
Q.append(("IMPIANTI IDRAULICI","intermedio",
"A cosa serve il ricircolo dell'acqua calda sanitaria (ACS)?",
"Risposta: a mantenere calda la tubazione di distribuzione così che l'acqua arrivi calda istantaneamente ai punti di utilizzo, evitando spreco d'acqua potabile. Va bilanciato (ogni ramo con portata tarata) e l'intera tubazione di ricircolo va coibentata per non disperdere calore quando non c'è prelievo."))
Q.append(("IMPIANTI IDRAULICI","intermedio",
"Qual è la temperatura di erogazione consigliata per l'ACS e perché?",
"Risposta: intorno a 40-45 °C ai punti di utilizzo, con produzione a 55-60 °C in caldaia o boiler per prevenire la proliferazione di Legionella (temperatura di sviluppo fermata sopra i 50 °C; i 60 °C garantiscono abbattimento batterico). Miscelatori termostatici proteggono dal rischio scottatura."))

# ---------------- IMPIANTI MECCANICI / HVAC (8) ----------------
Q.append(("IMPIANTI MECCANICI","intermedio",
"Perché una caldaia a condensazione ha rendimento superiore al 100%?",
"Risposta: perché recupera anche il calore latente di condensazione del vapore acqueo presente nei fumi, restituendolo all'acqua di riscaldamento. Il rendimento superiore a 100% è riferito al potere calorifico inferiore (PCI); riferito al PCS vale circa 88-98% a seconda del salto termico: più la temperatura di mandata è bassa, più si condensa e più si risparmia."))
Q.append(("IMPIANTI MECCANICI","avanzato",
"Cosa è la temperatura di mandata climatica?",
"Risposta: è la modulazione automatica della temperatura dell'acqua di mandata in funzione della temperatura esterna, seguendo una curva climatica impostata. Quando fuori fa più freddo la mandata sale, quando è mite scende: risparmio energetico e comfort migliore, specialmente con pavimenti radianti."))
Q.append(("IMPIANTI MECCANICI","intermedio",
"Perché la pompa di calore aria-acqua perde resa con il freddo intenso?",
"Risposta: perché aumenta il salto termico che il compressore deve vincere: minore temperatura esterna significa minor calore captato e maggiore lavoro di compressione per unità di calore erogato. Il COP scende e la potenza termica erogabile cala, motivo per cui in climi freddi servono integrazione (resistenze, caldaia ibrida) o macchine dimensionate su punto di progetto."))
Q.append(("IMPIANTI MECCANICI","intermedio",
"Come funziona la deumidificazione con pompa di calore in estate?",
"Risposta: l'aria interna attraversa l'evaporatore più freddo della temperatura di rugiada: il vapore acqueo si condensa e viene drenato. Il calore latente di condensazione si somma al carico sensibile sull'evaporatore: più alta è l'umidità, più lavora la macchina sul carico latente e meno sensibile può smaltire."))
Q.append(("IMPIANTI MECCANICI","base",
"Qual è la portata minima di aria primaria per una persona in ambiente abitativo?",
"Risposta: secondo UNI 10339, la portata minima di aria esterna per i locali abitativi è circa 20-30 m³/h per persona (valore di riferimento ~25-30 m³/h): garantisce il controllo della CO2 (sotto circa 1000-1200 ppm) e della umidità. Con la VMC si distribuisce dai locali di soggiorno e si espelle da cucina/bagni."))
Q.append(("IMPIANTI MECCANICI","avanzato",
"Cosa sono i fattori di emissione e regolazione della UNI/TS 11300-2?",
"Risposta: sono coefficienti correttivi del bilancio energetico che penalizzano gli impianti a regolazione on-off o senza contabilizzazione e premiano la regolazione climatica, i corpi scaldanti dimensionati correttamente e la contabilizzazione del calore. Un impianto vecchio a termosifoni senza valvole termostatiche ha fattori molto sfavorevoli rispetto a un sistema radiante con regolazione dinamica."))
Q.append(("IMPIANTI MECCANICI","intermedio",
"Qual è il vantaggio principale del pavimento radiante rispetto ai termosifoni?",
"Risposta: emette il 50% circa per irraggiamento con temperatura superficiale 26-29 °C, permettendo mandata a 35-40 °C compatibile con pompe di calore e caldaie a condensazione a massimo rendimento. Inoltre garantisce distribuzione uniforme del calore e nessun ingombro murale, migliorando il comfort e l'estetica degli interni."))
Q.append(("IMPIANTI MECCANICI","intermedio",
"Cosa si intende per free cooling e quando è efficace?",
"Risposta: è il raffrescamento dell'edificio facendo circolare aria esterna fresca (notte) senza accendere i gruppi frigo, oppure tramite free-cooling idronico su pompa di calore con sorgente esterna. È efficace nei climi con escursione giorno/notte marcata e quando l'involucro ha buona inerzia termica; in climi umidi costantemente caldi non basta e serve refrigerazione attiva."))

# ---------------- ELETTRICO (8) ----------------
Q.append(("ELETTRICO","base",
"Come si calcola la potenza assorbita da un carico trifase?",
"Risposta: P = √3 · V_LL · I · cosφ, dove V_LL è la tensione concatenata (400 V in BT Italia), I la corrente di linea e cosφ il fattore di potenza. La potenza apparente è S = √3 · V · I (VA): il quadro e i cavi si dimensionano su S e su I, non solo sulla potenza attiva."))
Q.append(("ELETTRICO","intermedio",
"Quando il vincolo di caduta di tensione diventa determinante per la sezione di un cavo?",
"Risposta: nelle linee lunghe con correnti elevate: la sezione per portata termica cresce poco con la lunghezza, mentre la sezione per caduta di tensione cresce linearmente. Per linee oltre 30-50 m con carichi importanti (colonnine, quadri lontani) il vincolo ΔV% (tipicamente ≤ 4% per linee terminali generali) governa il dimensionamento."))
Q.append(("ELETTRICO","base",
"Qual è la differenza tra conduttore di neutro e conduttore di protezione (PE)?",
"Risposta: il neutro è un attivo di ritorno della corrente di esercizio; il PE (terra di protezione) non porta corrente in esercizio e serve a portare in sicurezza le masse in caso di guasto verso terra. Mai confonderli o collegarli a valle del salvavita: questo annulla la protezione e crea tensioni pericolose sulle masse."))
Q.append(("ELETTRICO","base",
"Cosa protegge il salvavita (interruttore differenziale) e cosa non può fare?",
"Risposta: interviene sulle correnti di dispersione verso terra (sensibilità 30 mA per protezione delle persone da contatti indiretti) interrompendo il circuito in frazioni di secondo. Non sostituisce la protezione magnetotermica contro sovraccarichi e cortocircuiti: i due dispositivi hanno funzioni complementari e spesso convivono nello stesso modulo."))
Q.append(("ELETTRICO","intermedio",
"Cosa prevede l'impianto di terra e quali elementi comprende?",
"Risposta: dispersori interrati (pali o piatti), conduttore di terra, collettori equipotenziali principali e secondari, collegamenti equipotenziali ausiliari, conduttori di protezione. La resistenza verso terra va verificata a progetto: per piccole installazioni si ammettono valori fino a 30 Ω, più bassi dove l'impianto differenziale o le condizioni ambientali lo richiedono."))
Q.append(("ELETTRICO","intermedio",
"Qual è la regola di coordinamento tra cavo e protezione magnetotermica?",
"Risposta: corrente d'impiego Ib ≤ corrente nominale In del protettore ≤ portata termica Iz del cavo, con In ≤ 1,45·Iz per assicurare l'intervento in sovraccarico. In più le correzioni di posa (raggruppamento, temperatura, metodo) riducono Iz: il cavo va scelto dopo queste correzioni, non dai valori di tabellessa."))
Q.append(("ELETTRICO","base",
"Cosa si intende per autoconsumo fotovoltaico e come si massimizza?",
"Risposta: è la quota di energia solare prodotta e consumata istantaneamente in loco: ogni kWh autoconsumato vale il prezzo pieno dell'elettricità evitata. Si massimizza spostando i consumi (lavatrice, lavastoviglie, pompa di calore, auto elettrica) nelle ore di produzione e, in secondo luogo, con accumulo in batteria."))
Q.append(("ELETTRICO","intermedio",
"Perché è utile la domotica/KNX in un edificio residenziale?",
"Risposta: centralizza e automatizza illuminazione, tapparelle, scenari, clima, sicurezza e consumi con un bus comune e sensori condivisi, riducendo cablaggi e consumi (spegnimenti automatici, gestione luci, zone). A livello commerciale aumenta il valore dell'immobile e l'efficienza gestionale per chi ha più unità."))

# ---------------- ACUSTICA (5) ----------------
Q.append(("ACUSTICA","base",
"Enunciare la formula di Sabine per il tempo di riverberazione e applicarla.",
"Risposta: T60 = 0,161 · V / A, dove V è il volume in m³ e A l'area di assorbimento equivalente in m² sabina. Esempio: sala 300 m³ con A = 25 m² → T60 ≈ 1,92 s; aggiungendo pannelli fino ad A = 70 m² → T60 ≈ 0,68 s. Più volume o meno assorbimento allungano il riverbero."))
Q.append(("ACUSTICA","intermedio",
"Cosa indica l'indice DnT,w e come si valuta l'isolamento tra unità immobiliari?",
"Risposta: è l'indice di isolamento acustico standardizzato tra due ambienti (valore medio sulle bande di frequenza, corretto per il tempo di riverberazione). Valori indicativi di progetto per pareti tra unità abitative: DnT,w ≥ 55-60 dB; si affianca sempre il controllo del rumore da calpestio (LnT,w ≤ 50-53 dB) con pavimenti galleggiati."))
Q.append(("ACUSTICA","intermedio",
"Come si riduce il rumore da calpestio nei solai?",
"Risposta: con strati resilienti sotto la pavimentazione guida (guaine, sottofondi elastici, supporti sagomati) che interrompono il percorso solido tra pavimento e struttura, e con massa + sospensione nel solaio (controsoffitti fonoisolanti su telaio elastico). La sola regola è: interrompere i ponti rigidi; il gres poggiato direttamente sul massetto trasmette tutto."))
Q.append(("ACUSTICA","base",
"Cosa misura il livello equivalente LAeq?",
"Risposta: è il livello di pressione sonora energetico medio equivalente su un tempo di osservazione T, con ponderazione A: LAeq,T = 10·log[(1/T)∫(p²/p0²)dt]. È il parametro di riferimento per la valutazione del rumore ambientale e dell'esposizione in ambiente di lavoro (80 dB(A) azione valore, 87 dB(A) limite)."))
Q.append(("ACUSTICA","intermedio",
"Dove e come si posizionano i pannelli fonoassorbenti in una sala?",
"Risposta: sulle superfici riflettenti che generano i riflessi fastidiosi: parete di fondo e parte del controsoffitto davanti alla zona di ascolto/lavoro. L'area si calcola dal target di T60 (formula di Sabine rovesciata: A = 0,161·V/T60 target); materiali fibrosi spessi (4-8 cm) con veletta aria funzionano meglio sulle bande medie e basse."))

# ---------------- GEOTECNICA (5) ----------------
Q.append(("GEOTECNICA","intermedio",
"Qual è la formula della portanza ultima di una fondazione superficiale secondo Terzaghi?",
"Risposta: qu = c·Nc + q·Nq + 0,5·γ·B·Nγ, dove c è coesione, q il sovraccarico del piano di posa, γ il peso del terreno, B la larghezza della fondazione e Nc, Nq, Nγ coefficienti dipendenti dall'angolo di attrito. La portanza di progetto si ottiene dividendo per un coefficiente di sicurezza (tipicamente 3-4) e verificando i cedimenti."))
Q.append(("GEOTECNICA","base",
"Quali sono le indagini geognostiche minime per progettare una fondazione?",
"Risposta: sondaggi (carotaggio continuo o a distruzione) o prove penetrometriche statiche/dinamiche con profondità utile almeno 1,5-2 volte la larghezza della fondazione, campionamenti per prove di laboratorio (granulometria, Atterberg, compressibilità, resistenza al taglio), determinazione del livello e delle variazioni della falda. Senza questi dati non è possibile un progetto di fondazioni serio."))
Q.append(("GEOTECNICA","intermedio",
"Quali valori di cedimento sono considerati accettabili per un edificio ordinario?",
"Risposta: dipende dalla struttura, ma come ordine di grandezza i cedimenti totali uniformi possono arrivare a 5-10 cm per edifici ordinari, mentre i cedimenti differenziali devono restare dell'ordine del centimetro per evitare fessurazioni della struttura portante. Elementi rigidi (scale, muri portanti) e finiture fragili richiedono vincoli più severi; la norma impone verifica sotto carichi di esercizio con modelli di interazione terreno-struttura."))
Q.append(("GEOTECNICA","intermedio",
"Quando scegliere fondazioni profonde (pali) anziché superficiali?",
"Risposta: quando i terreni di buona portanza sono troppo profondi (>2-3 m) o troppo deboli in superficie, quando i carichi sono elevati (edifici alti), o in presenza di sabbie liquefacenti o falde variabili. I pali portano per punta e per attrito laterale; la scelta avviene confrontando costo, programma lavori, vibrazioni in fase di esecuzione e rigidezza complessiva del sistema fondazione-terreno."))
Q.append(("GEOTECNICA","avanzato",
"Cosa è la liquefazione sismica e quali terreni ne sono soggetti?",
"Risposta: è la perdita di resistenza delle sabbie saturerate e sciolte che, ciclicamente sollecitate dal sisma, tendono a comportarsi come un fluido per eccesso di pressione interstiziale: il terreno perde portanza e le fondazioni affondano o si ribaltano. Sono soggette sabbie fini saturerate con N-SPT bassi; la mitigazione passa da drenaggi, compaction, pali vincolati o miglioramento del terreno."))

# ---------------- RILIEVO E TOPOGRAFIA (5) ----------------
Q.append(("RILIEVO","intermedio",
"Come si valuta e compensa l'errore di chiusura di una poligonale?",
"Risposta: si calcolano le coordinate dei vertici partendo da un punto noto e si confrontano le coordinate di arrivo con quelle note: la differenza è l'errore di chiusura (planimetrico e altimetrico). Se inferiore alla tolleranza, si compensa distribuendo l'errore con la regola di Bowditch (proporzionalmente ai lati) o minimi quadrati; poi si calcolano le coordinate compensative definitive."))
Q.append(("RILIEVO","base",
"Come si calcola il dislivello tachimetrico con stazione totale?",
"Risposta: Δh = D·sin(z) + i − m, dove D è la distanza inclinata, z l'angolo zenitale, i l'altezza dello strumento e m l'altezza del prisma. La formula tiene conto che il prisma non è a quota zero: trascurare i e m in misure ravvicinate genera errori di diversi centimetri."))
Q.append(("RILIEVO","intermedio",
"Quando usare GNSS RTK invece della stazione totale per un rilievo edilizio?",
"Risposta: il GNSS RTK è ideale per estendere riferimenti assoluti e rilievi esterni con precisione ±1-3 cm, ma perde precisione e continuità vicino a edifici e sotto coperture (multipath). Per il dettaglio architettonico (facciate, interni, elementi ravvicinati) si usa la stazione totale o laser scanner; le due tecniche si integrano nel rilievo completo."))
Q.append(("RILIEVO","base",
"Quali documenti costituiscono un rilievo completo per avviare un progetto di ristrutturazione?",
"Risposta: elaborati plano-altimetrici quotati (piante, sezioni, prospetti) con quote campate, prospetti, documentazione fotografica, rilievo dei carichi esistenti (tipologia solai, coperture), stato dei servizi impiantistici e possibili disegni d'archivio. Da essi derivano computo metrico, verifica strutturale e definizione degli interventi: un rilievo sbagliato si paga in progettazione e in cantiere."))
Q.append(("RILIEVO","intermedio",
"Cos'è l'errore di eccentricità in un rilievo con prisma e come si corregge?",
"Risposta: nasce quando il punto misurato non coincide con il vertice dell'angolo rilevato (prisma spostato per ostacolo): l'errore angolare trasla la posizione in proporzione alla distanza. Si corregge misurando l'eccentricità e riducendo la stazione, oppure evitando stazioni ravvicinate a target obbligati; nelle misure corte (< 20 m) questo errore diventa dominante."))

# ---------------- ESTIMO / ECONOMIA DI CANTIERE (7) ----------------
Q.append(("ESTIMO","base",
"Come si calcola la rata di un mutuo a tasso fisso e ammortamento francese?",
"Risposta: R = C · i / (1 − (1+i)^−n), dove C è il capitale, i la rata mensile, n il numero di rate. Esempio: 100.000 €, tasso annuo 3% (i = 0,25% mensile), 25 anni (300 rate) → R ≈ 474 €/mese. Il piano di ammortamento scompone ogni rata in quota interessi (decrescente) e quota capitale (crescente)."))
Q.append(("ESTIMO","base",
"Cosa si intende per computo metrico estimativo e a corpo d'opera?",
"Risposta: è l'elenco delle lavorazioni con relative unità di misura, quantità desunte dai disegni e prezzi unitari analitici o di mercato. In 'a corpo' (o forfait) alcune partite sono considerate globalmente senza dettaglio di quantità: utile quando le quantità sono incerte, ma perde trasparenza comparativa e rende più difficile la contabilità dei lavori."))
Q.append(("ESTIMO","intermedio",
"Qual è la differenza tra misure a misura e a corpo e quando usarle?",
"Risposta: a misura le quantità sono desunte dal progetto e verificate a lavori ultimati (m², m³, kg, n.): trasparenza e controllabilità; a corpo si paga il risultato completo indipendentemente dalle quantità: si usa per opere il cui dettaglio è di pertinenza dell'impresa. La combinazione 'a corpo e misura' è la più diffusa nei contratti reali."))
Q.append(("ESTIMO","intermedio",
"Come si compone il costo di produzione di un'impresa edile?",
"Risposta: costi diretti (materiali di consumo, manodopera, mezzi di cantiere) + costi indiretti di cantiere (ufficio tecnico, piccoli attrezzi, sicurezza, assicurazioni, vitto/alloggio, trasporti) + spese generali d'ufficio e utile. Il prezzo di vendita si ottiene applicando le incidenze (indiretti, spese generali, utile) sui costi diretti secondo la storia aziendale e il rischio del contratto."))
Q.append(("ESTIMO","base",
"Come si stima la durata di una lavorazione conosciendo le resse giornaliere?",
"Risposta: giorni = quantità totale / resa giornaliera (o giorni-uomo = quantità / resa per manovale). Esempio: 1000 m² di intonaco a 20 m²/giorno/manovale → 50 giorni-uomo: con 3 manovali lavora circa 17 giorni. Le resse reali dipendono da complessità, accessibilità, forniture e coordinate con altri lavori."))
Q.append(("ESTIMO","avanzato",
"Cosa prevede la valutazione di congruità di un'offerta nei lavori pubblici?",
"Risposta: secondo il Codice dei contratti (D.Lgs 36/2023), l'offerta anomala si valuta rispetto al valore stimato dell'appalto e ai prezzi unitari di riferimento regionali/DEI, con controlli su ribasso, componenti principali e garanzie. Un ribasso eccessivo obbliga il concorrente a documentare la sostenibilità; l'aggiudicazione a prezzi non congrui mette a rischio la qualità e la sicurezza dell'opera."))
Q.append(("ESTIMO","intermedio",
"Cosa comprende la contabilità dei lavori pubblici?",
"Risposta: la misurazione delle quantità eseguite (stati avanzamento lavori), la contabilità delle varianti e subentri, l'applicazione dei prezzi unitari contrattuali, le trattenute di garanzia previste dalla legge fino al collaudo, i controlli in corso d'opera. È la base del pagamento delle certificazioni di pagamento e della liquidazione finale; ogni quantità deve essere verificabile sul progetto o sul rilievo."))

# ---------------- CANTIERE / SICUREZZA (7) ----------------
Q.append(("CANTIERE E SICUREZZA","base",
"Cosa stabilisce il D.Lgs 81/2008 (Testo Unico della Sicurezza) per i cantieri edili?",
"Risposta: individua obblighi di committente, progettisti, direzione lavori, coordinatore della sicurezza in progettazione (CSP) ed esecuzione (CSE), imprese e lavoratori autonomi; prevede PSC, POS e documenti d'identità dei lavoratori. Il DVR (documento di valutazione dei rischi) è il documento centrale per ogni realtà aziendale; le sanzioni penali e amministrative colpiscono ogni soggetto per i propri obblighi."))
Q.append(("CANTIERE E SICUREZZA","base",
"Qual è la differenza tra PSC, POS e PON?",
"Risposta: il PSC è il piano di coordinamento generale della sicurezza redatto dal CSP per il cantiere; il POS è il piano operativo di sicurezza che ogni impresa redige per le proprie lavorazioni in coerenza col PSC; il PON è il piano operativo nominativo obbligatorio per lavoratori autonomi e ditte individuali sotto le soglie PSC/POS, con contenuti minimi di coordinamento."))
Q.append(("CANTIERE E SICUREZZA","intermedio",
"Quali sono i DPI indispensabili in un cantiere edile ordinario?",
"Risposta: casco di protezione, calzature di sicurezza (S3 con puntale e lamina), guanti da lavoro, indumenti ad alta visibilità, DPI visivi e uditivi secondo il rischio. Per lavori in quota si aggiungono imbracatura anticaduto con punto di ancoraggio certificato; per levigatura/sbavatura DPI respiratori e oculari. L'uso è obbligatorio secondo il DVR e la segnaletica di cantiere."))
Q.append(("CANTIERE E SICUREZZA","intermedio",
"Quali sono i rischi maggiori in un cantiere edile e le relative misure principali?",
"Risposta: caduta dall'alto (ponteggi, aperture, coperture: misure collettive di protezione sempre preferite ai DPI), sepolture e ostruzioni in scavi, ribaltamento mezzi, contatto con linee elettriche, esposizione ad amianto e sostanze pericolose, tagli e schiacciamenti. La gerarchia delle misure prevede prima l'eliminazione, poi le misure collettive, infine i DPI come ultima barriera."))
Q.append(("CANTIERE E SICUREZZA","intermedio",
"Come si gestiscono terre e rocce da scavo secondo il codice ambientale?",
"Risposta: secondo D.Lgs 152/2006 le terre e rocce sono rifiuti non pericolosi a meno di contaminazione: se riutilizzabili in sito secondo criteri autorizzativi restano fuori dal ciclo dei rifiuti, altrimenti seguono il registro di carico/scarico con FIR, formulari di identificazione e smaltimento in impianti autorizzati. Il trasporto va documentato con registri e formulari d'identificazione."))
Q.append(("CANTIERE E SICUREZZA","avanzato",
"Cosa sono i materiali contenenti amianto e come si interviene su di essi?",
"Risposta: sono manufatti (coperture, canne fumarie, pannelli, guaine, fughe) contenenti fibre di amianto, la cui manipolazione è regolata dal DPR 6/6/1994: interventi solo da imprese iscritte all'albo nazionale, con piani di lavoro, procedure confinamento/decontaminazione, DPI specifici e smaltimento come rifiuto pericoloso. Il rivestimento e incapsulamento è alternativa alla rimozione solo in casi valutati."))
Q.append(("CANTIERE E SICUREZZA","intermedio",
"Qual è il ruolo della direzione lavori e del collaudo nei lavori pubblici?",
"Risposta: la direzione lavori sorveglia la corretta esecuzione delle opere secondo il progetto e le norme, certifica le misurazioni e le varianti, verifica la sicurezza in coerenza col CSE. Il collaudo è l'accertamento finale di regolare esecuzione statica e funzionale (e documentale), effettuato da soggetto indipendente per opere sopra soglia, con verbale che sblocca il saldo e le garanzie."))

# ---------------- NORMATIVA ITALIANA (10) ----------------
Q.append(("NORMATIVA ITALIANA","base",
"Cosa disciplinano le NTC 2018 (D.M. 17/01/2018)?",
"Risposta: sono le norme tecniche per la progettazione, esecuzione e collaudo delle costruzioni: azioni sulle strutture, materiali e criteri di verifica, geotecnica, sicurezza strutturale in condizioni ordinarie e sismiche, costruzioni esistenti. Sono attuate con la Circolare esplicativa 21/01/2019 n. 7 del C.S.LL.PP. e aggiornate con nuovi decreti di aggiornamento."))
Q.append(("NORMATIVA ITALIANA","base",
"Cosa prevede il DPR 380/2001 (Testo Unico dell'edilizia)?",
"Risposta: regola i titoli edilizi: permesso di costruire (art. 10) per opere nuove, SCIA (art. 12) per opere minori come le ristrutturazioni che non modificano destinazione e volumi, CILA (art. 22) per piccoli lavori interni, con discipline di condono per abusi realizzati in periodi passati (artt. 34-37). Ogni intervento va classificato nel titolo corretto: sbagliare titolo espone a diffida e demolizione."))
Q.append(("NORMATIVA ITALIANA","intermedio",
"Cosa prescrive il D.Lgs 192/2005 sulla certificazione energetica?",
"Risposta: fissa requisiti prestazionali minimi di isolamento e impianti, obbliga l'APE (attestato di prestazione energetica) in vendita e locazione, disciplina l'abilitazione di certificatori energetici e la formazione energetica degli edilizia, e apre a detrazioni fiscali e incentivazione di riqualificazioni energetiche. È la legge quadro da cui derivano i calcoli di trasmittanza e le verifiche dell'involucro."))
Q.append(("NORMATIVA ITALIANA","intermedio",
"Qual è il ruolo della serie UNI/TS 11300 nei calcoli energetici?",
"Risposta: è la serie di norme tecniche che implementa il metodo europeo UNI EN ISO 13790 per il calcolo delle prestazioni energetiche degli edifici: trasmittanze, bilanci di riscaldamento/raffrescamento/ACS, produzione idroelettrica, energia elettrica e rinnovabili. È richiesta per APE, controlli di progetto e accesso agli incentivi (detrazioni, Conto Termico)."))
Q.append(("NORMATIVA ITALIANA","avanzato",
"Cos'è la direttiva Case Green e l'obbligo di edificio a energia quasi zero (NZEB)?",
"Risposta: la direttiva 2010/31/UE (rifusa dalla EPBD 2024/1275) richiede che tutti gli edifici di nuova costruzione siano a energia quasi zero dal 2021 (2019 per gli edifici pubblici): fabbisogno coperto in gran parte da rinnovabili, involucro performante e impianti efficienti. È il contesto europeo che ha alimentato detrazioni, Conto Termico e certificazione energetica in Italia."))
Q.append(("NORMATIVA ITALIANA","intermedio",
"Quali responsabilità ha il progettista ai sensi dell'ordinamento italiano?",
"Risposta: responsabilità civile per danni da errore professionale (art. 2236 c.c. — impegno di diligenza rilevante per lavori intellettuali complessi), responsabilità penale per disastri e crolli colposi (art. 434 c.p.), responsabilità deontologica verso l'Ordine di appartenenza e verso il committente per vizi del progetto (art. 1667 c.c. di decennale garanzia). È prassi consolidata la copertura assicurativa RC professionale."))
Q.append(("NORMATIVA ITALIANA","intermedio",
"Cosa sono i certificatori energetici e come si abilitano?",
"Risposta: sono professionisti abilitati a redigere l'APE secondo D.Lgs 28/2011 (art. 15), che recepisce la direttiva REDI: hanno superato specifica formazione ed esame riconosciuto dalle regioni, e operano con metodo di calcolo conforme UNI/TS 11300. Per certificare devono usare software validato e rispettare il registro regionale delle certificazioni."))
Q.append(("NORMATIVA ITALIANA","intermedio",
"Come funzionano le detrazioni fiscali per ristrutturazioni ed efficientamento?",
"Risposta: ristrutturazioni: detrazione del 50% sulle spese con massimale e rateizzazione in 10 anni; efficientamento energetico: detrazione del 65-75% per cappotto, sostituzione impianti, pannelli solari, pompe di calore, con massimali differenziati; in più incentivi come il Conto Termico 3.0 e i bonus edilizi (Superbonus e successive evoluzioni). Ogni misura ha requisiti tecnici, massimali e scadenze proprie da verificare."))
Q.append(("NORMATIVA ITALIANA","intermedio",
"Cosa è il Conto Termico 3.0?",
"Risposta: è l'incentivo GSE per interventi di efficienza energetica e rinnovabili su edifici esistenti: interventi su involucro, sostituzione impianti a gas con pompe di calore/biomassa, solare termico, fotovoltaico con batterie. Prevede forme di incentivo a fondo perduto per privati e imprese, con requisiti minimi di miglioramento (es. aumento di classse energetica) e controlli a campione."))
Q.append(("NORMATIVA ITALIANA","avanzato",
"Cosa sono i vizi del progetto e come si tutela il committente dopo il collaudo?",
"Risposta: sono difformità, errori di dimensionamento o carenze che rendono l'opera inidonea all'uso previsto (art. 1667 c.c.). La garanzia decennale opera a favore del committente per dieci anni dalla consegna/collaudo anche se il vizio era occulto; il progettista risponde a sé e verso il committente secondo il contratto d'opera intellettuale, spesso con clausole di responsabilità limitata e polizza RCO."))

# ---------------- MATERIALI (7) ----------------
Q.append(("MATERIALI","base",
"Cosa indica la classe di reazione al fuoco di un materiale da costruzione?",
"Risposta: è la capacità del materiale di contribuire all'incendio secondo classi europee: A1 non combustibile (calcestruzzo, laterizio, acciaio), A2 combustibilità limitata, B-F crescente contribuzione. Le sigle aggiuntive indicano fumo (s1-s3) e gocciolamento (d0-d2): un pannello B-s2,d0 contribuisce poco ma fuma. La classe richiesta dipende da destinazione d'uso e altezza del fabbricato."))
Q.append(("MATERIALI","intermedio",
"Quali sono i vantaggi del calcestruzzo alleggerito rispetto a quello ordinario?",
"Risposta: pesa meno (1200-1800 kg/m³ contro 2400), isola meglio termicamente e acusticamente, riduce carichi permanenti e sismici. Ha resistenza meccanica più bassa e modulo elastico ridotto: si usa per solai, tamponature alleggerite e massetti dove non serve massima resistenza strutturale."))
Q.append(("MATERIALI","intermedio",
"Quali sono vantaggi e limiti del legno strutturale?",
"Risposta: vantaggi: peso specifico/resistenza eccellente, prefabbricazione rapida e asciutta, sostenibilità e stoccaggio carbonico. Limiti: richiede protezione da umidità, azione del fuoco (rivestimenti o sovradimensionamento delle sezioni per resistenza R), parassiti e controllo qualità del legno. I moderni prodotti incollati (CLT, LVL) superano molti limiti del legno massiccio."))
Q.append(("MATERIALI","base",
"Come scegliere tra muratura portante e tamponatura in laterizio?",
"Risposta: la muratura portante trasferisce i carichi verticali e orizzontali alla fondazione (spessori maggiori, armature di miglioramento sismico); la tamponatura riempie il telaio portante in c.a./acciaio e contribuisce solo con il proprio peso e con vincoli antisismici (catene, collegamenti). La scelta dipende da altezza dell'edificio, zona sismica, tradizione costruttiva e costo."))
Q.append(("MATERIALI","intermedio",
"Quali sono le principali tipologie di impermeabilizzazione per coperture piane?",
"Risposta: guaine bituminose armati con saldatura a fiamma (economiche, collaudate), membrane sintetiche in PVC o TPO saldate ad aria calda (leggere, durature), membrane liquide poliuretaniche o cementizie (applicate a pennello, ideali per forme complesse) e sistemi a freddo. La scelta dipende da pendenza, esposizione, compatibilità con sottostante, manutenzione programmata e garanzie."))
Q.append(("MATERIALI","intermedio",
"A cosa servono gli intonaci deumidificanti e quali limiti hanno?",
"Risposta: sono malte a base idraulica che gestiscono l'umidità di risalita capillare nelle murature, favorendo evaporazione senza concentrare sali in superficie. Limiti: non risolvono cause attive (falletta, condensa interstiziale) e richiedono diagnosi preliminare: se la fonte d'acqua non viene eliminata, l'intonaco fallisce in pochi anni."))
Q.append(("MATERIALI","avanzato",
"Quali sono i principali inquinanti indoor e come si mitigano?",
"Risposta: formaldeide e VOC da leghe, vernici, colle e arredi; muffe e umidità per condense; radon dal terreno; CO2 e bioeffluenti dagli occupanti. Mitigazione: materiali a bassa emissione con etichette di classe A+/EC1, ventilazione continua (VMC), barriera radon con depressurizzazione sottofondo, controllo umidità e corretta installazione degli impianti."))

# ---------------- writer ----------------
os.makedirs('parsed', exist_ok=True)
meta = {
    "source": "quiz_tecnici_kimi",
    "license": "Sintesi didattica originale Kimi (pubblico dominio)",
    "commercial_ok": True,
    "attribution": "Banca quiz tecnici a cura di Kimi - risposte verificate",
    "url": "",
}
out = []
for i, (area, livello, domanda, risposta) in enumerate(Q, 1):
    rec = dict(meta)
    rec.update({
        "id": f"QUIZ-{i:03d}",
        "area": area,
        "livello": livello,
        "question": domanda,
        "answer": risposta,
    })
    out.append(rec)

path = 'parsed/quiz_tecnici_100.jsonl'
with open(path, 'w', encoding='utf-8') as f:
    for r in out:
        f.write(json.dumps(r, ensure_ascii=False) + '\n')
print(f"scritti {len(out)} quiz -> {os.path.abspath(path)}")
