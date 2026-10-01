# VOCI — FACOLTA_IMPIANTI_ENERGIA

> *Materiale di esclusiva proprietà **Auratrix** — Tutti i diritti riservati.*
> *Uso consentito solo ad Auratrix e ai suoi sistemi LLM. Vedi [LICENSE](../LICENSE).*

163 voci, 11 corsi.


## Data center e critical facilities

*Corso `DATA_CENTER_E_CRITICAL_FACILITIES_PACK` — 7 voci*

### La climatizzazione di precisione: freddo per i server

**Categoria:** Climatizzazione · **Corso:** Data center e critical facilities

I server scaldano in continuazione: la climatizzazione di precisione mantiene 22-27 °C e umidità 40-60% (con tolleranze strette, i server sono delicati); i sistemi: CRAC/CRAH (unità di precisione a liquido o ad aria), i corridoi caldi e freddi (l'aria fredda davanti ai rack, quella calda dietro), il free-cooling (usare l'aria esterna quando è fredda), la refrigerazione adiabatica (l'acqua che evapora raffredda).

- **Tecnologia e criteri:** Architetture: il contenimento (corridoi chiusi con porte, l'aria non si mescola: il free-cooling diventa possibile anche d'estate), la rear-door cooling (le porte dei rack sono radiatori ad acqua fredda), l'immersion cooling (i server immersi in liquido dielettrico: la frontiera, per i carichi estremi); il PUE guida le scelte: ogni 0,1 di PUE risparmiato vale milioni sui grandi impianti.
- **Applicazioni:** Data center di ogni dimensione, sale server aziendali, edge node.
- **Vantaggi:** La climatizzazione è il 40-50% del consumo elettrico: migliorarla è il primo business case (il PUE da 1,5 a 1,2 vale un terzo della bolletta).
- **Limiti e attenzioni:** I margini di temperatura sono stretti: gli errori di taratura (umidità troppo bassa: elettrostatica; troppo alta: corrosione) guastano i server silenziosamente.
- **Costi ed economia:** Costi: CRAC 3.000-10.000 €/unità; il contenimento dei corridoi: 100-300 €/m; l'impatto sul PUE: il vero parametro economico.
- **Caso tipico:** Data center con contenimento corridoi caldi e free-cooling: il PUE è sceso da 1,55 a 1,22; la bolletta elettrica annua si è ridotta di oltre il 20% e la potenza liberata ha permesso l'installazione di altri 200 rack senza nuovo allaccio.
- **Normativa:** ASHRAE TC 9.9 (i margini termici dei server); EN 50600; specifiche dei produttori IT.
- **Nota di cantiere:** La regola: il freddo è per i server, non per la stanza: contenere i corridoi, non raffrescare l'aria inutilmente.

### La continuità elettrica: UPS, gruppi elettrogeni, doppie alimentazioni

**Categoria:** Continuità · **Corso:** Data center e critical facilities

L'alimentazione del data center è a catena ridondata: due linee elettriche indipendenti (da sottostazioni diverse), gli UPS (batterie che coprono i micro-interruzioni), i gruppi elettrogeni (motoriduttori? No: generatori diesel/gas per le interruzioni lunghe), le STS (commutazioni statiche che scambiano tra le due linee in millisecondi).

- **Tecnologia e criteri:** Architettura: le due linee A e B alimentano ogni rack (doppia alimentazione dei server), gli UPS a modularità o monoblocco (10-15 minuti di autonomia: il tempo di avviare i generatori), i generatori con autonomia di carburante 24-48 ore (o gas metano), i bypass di manutenzione (si può manutenere tutto senza spegnere); la verifica: i collaudi con il 'black building test' (si stacca tutto e si guarda se regge).
- **Applicazioni:** Ogni data center: dal piccolo locale aziendale all'hyperscale di 100.000 m².
- **Vantaggi:** La ridondanza elettrica è assoluta: il data center più piccolo ha più continuità di un ospedale medio.
- **Limiti e attenzioni:** La ridondanza non usata è costo morto: il Tier giusto si sceglie sul business (non tutti i server valgono Tier IV).
- **Costi ed economia:** Costi: UPS 200-400 €/kVA; generatori 150-300 €/kVA; la ridondanza N+1 aggiunge il 30-50% sui sistemi.
- **Caso tipico:** Test annuale 'black building' in un data center Tier III: il passaggio sui generatori è avvenuto in 8 secondi senza interruzione dei servizi; il test ha scoperto un bypass mal configurato che avrebbe lasciato un intero corridoio scoperto.
- **Normativa:** CEI 0-16 (connessione rete); specifiche TIA-942; normativa antincendio e ambientale per i generatori.
- **Nota di cantiere:** Domanda cardine: 'quanto vale un minuto di fermo per questo servizio?' — la risposta definisce il Tier.

### L'edge computing: il data center piccolo e ovunque

**Categoria:** Edge e micro · **Corso:** Data center e critical facilities

L'edge computing porta il calcolo vicino all'utente (il 5G, l'IoT, la guida autonoma non possono aspettare il cloud lontano): i micro-data center (un armadio rack in un edificio), i container data center (il DC in un box pronto all'uso), le sale server pre-fabbricate; il mercato cresce più veloce dei grandi DC.

- **Tecnologia e criteri:** Forme: l'armadio edge (2-12 rack con UPS e clima integrati, silenziosi per gli uffici), il container (20-40 piedi con tutto dentro, da collocare in un parcheggio), la micro-sala (una stanza dell'edificio con i sistemi ridondati miniaturizzati); i vantaggi: tempi di deploy settimanali, scalabilità modulare, vicinanza (latenza millisecondi invece di decine).
- **Applicazioni:** Telco, reti 5G, industria 4.0, reti IoT, filiali bancarie.
- **Vantaggi:** L'edge porta la potenza dove serve: la latenza è la nuova valuta (la guida autonoma non può aspettare 50 ms).
- **Limiti e attenzioni:** I micro-DC sono vulnerabili (fisicamente accessibili): la sicurezza va rivista per il contesto urbano.
- **Costi ed economia:** Costi: armadio edge 20.000-80.000 €; container data center 100.000-500.000 € (ordini di grandezza).
- **Caso tipico:** Container data center per una fiera tecnologica: installato in 3 giorni, operativo per l'evento, poi spostato in un'altra sede: la modularità ha evitato la costruzione di un locale permanente per un'esigenza temporanea.
- **Normativa:** Standard EN 50600 (modulare); specifiche produttori; normativa antincendio ridotta per gli armadi.
- **Nota di cantiere:** La direzione è chiara: il calcolo va verso le persone (edge), il consolidamento va verso l'energia pulita (grandi DC al nord) — entrambi sono edilizia.

### Che cos'è un data center: l'edificio che non può fermarsi

**Categoria:** Fondamenti · **Corso:** Data center e critical facilities

Il data center è l'edificio della continuità: ospita i server che tengono in funzione aziende, servizi, cloud; ogni interruzione costa migliaia di euro al minuto (stime settoriali per i servizi finanziari e cloud), quindi tutto è ridondante: alimentazione, clima, rete, struttura.

- **Tecnologia e criteri:** I livelli: lo standard Uptime Tier (I-IV) classifica la resilienza (Tier IV = tollera ogni guasto senza interruzione, con duplicazione totale); il TIA-942 definisce gli aspetti di progetto (camere, corridoi, potenza); le metriche: PUE (Power Usage Effectiveness: energia totale / energia IT, il santo graal dell'efficienza: i migliori < 1,2, la media storica ~1,5+), il livello di servizio (SLA 99,982% per Tier IV).
- **Applicazioni:** Cloud provider, banche, PA, grandi aziende, edge computing urbano.
- **Vantaggi:** La domanda digitale cresce del 10-20%/anno: i data center sono l'edilizia che più cresce nel mondo (stima settore).
- **Limiti e attenzioni:** Consumano tantissima energia: la localizzazione (freddo, energia rinnovabile) è la nuova leva competitiva.
- **Costi ed economia:** Costi: un rack IT (0,5 m²) vale 15.000-50.000 €; l'edilizia: 6.000-15.000 €/m² (iper-specializzata).
- **Caso tipico:** Edge data center in una città del nord: il freddo esterno free-cooling (l'aria esterna raffredda direttamente) ha ridotto il PUE da 1,5 a 1,15, con risparmio energetico di milioni di euro in 10 anni.
- **Normativa:** TIA-942 (standard progettazione); standard Uptime Tier; EN 50600 (serie europea); normativa antincendio specifica.
- **Nota di cantiere:** La prima legge del data center: il costo di NON funzionare supera qualsiasi costo di costruzione — si progetta per non fermarsi mai.

### Le reti e il cablaggio strutturato: le autostrade dei dati

**Categoria:** Reti · **Corso:** Data center e critical facilities

Il data center è fatto di connessioni: il cablaggio strutturato (fibre ottiche e rame categorizzato) collega i rack, le sale, l'esterno; la gerarchia: spine-area (fuori), inter-building (tra edifici), intra-building (le dorsali), horizontal? le horizontal (ai rack).

- **Tecnologia e criteri:** Standard: le fibre OM4/OM5 multimodali e le OS2 monomodali (per le lunghe distanze), il cavo in rame Cat6A/Cat8 per i brevi, le prese e i pannelli di permutazione (le patch) che permettono di cambiare configurazione senza toccare i cavi strutturali; il 'cable management': le canaline e le finger (le 'dita' che guidano i cavi), la documentazione (ogni cavo etichettato: senza mappa, il data center è indecifrabile in 6 mesi).
- **Applicazioni:** Cablaggio di data center e grandi uffici, SAN (storage), reti industriali.
- **Vantaggi:** Il cablaggio ben documentato dimezza i tempi di intervento: l'errore 'ho staccato il cavo sbagliato' costa ore di downtime.
- **Limiti e attenzioni:** Il cablaggio 'arruffato' (spaghetti cabling) blocca la ventilazione dei rack e rende ogni cambio un rischio.
- **Costi ed economia:** Costi: il cablaggio strutturato completo: 50-150 €/punto (ordine di grandezza); le fibre: da 5-15 €/m il cavo.
- **Caso tipico:** Data center riorganizzato con cable management rigoroso e mappa aggiornata: i tempi di risoluzione guasti sono calati del 60% e gli errori di manutenzione azzerati.
- **Normativa:** Standard TIA-568 e ISO/IEC 11801 (cablaggio); specifiche produttori.
- **Nota di cantiere:** La regola: il cavo si tira una volta nella vita, la documentazione si aggiorna ogni volta che si tocca.

### La sicurezza del data center: fisica, logica, antincendio

**Categoria:** Sicurezza DC · **Corso:** Data center e critical facilities

La sicurezza del data center è a cipolle: fisica (cancelli, guardie, varchi con badge, telecamere, antitaccheggio? No: anti-intrusione), logica (firewall, segmentazione), ambientale (antincendio, allagamenti, polveri); ogni accesso è tracciato (chi entra, dove, quando).

- **Tecnologia e criteri:** Livelli: il perimetro (il sito), l'edificio (i varchi), la sala (le impronte? i badge biometrici), il rack (le chiavi elettroniche individuali); l'antincendio specifico: i gas estinguenti (FM-200, NOVEC 1230, oggi in transizione verso sostanze meno inquinanti: i clean agent) che spengono senza danneggiare i server, la rivelazione precoce (VESDA: rileva il fumo nella fase di incipiente), l'allagamento: i rilevatori d'acqua sulle pavimentazioni sospese e sotto i pavimenti rialzati; la sicurezza logica interagisce con quella fisica (l'accesso al rack richiede l'autorizzazione logica).
- **Applicazioni:** Data center aziendali e commerciali, locali server critici.
- **Vantaggi:** La sicurezza a strati è efficace: un solo strato violato non basta a chi non è autorizzato.
- **Limiti e attenzioni:** La sicurezza eccessiva rallenta le operazioni quotidiane: i livelli vanno calibrati (non tutto serve Tier IV).
- **Costi ed economia:** Costi: i sistemi di controllo accessi: 5.000-50.000 €; il rilevamento incendio VESDA: 2.000-10.000 €.
- **Caso tipico:** Tentativo di accesso non autorizzato a un rack in un data center: il badge non autorizzato ha allertato, la telecamera ha registrato, l'accesso è stato negato e tracciato: il cliente ha rinnovato il contratto per la sicurezza documentata.
- **Normativa:** Normativa antincendio (D.M. 2015 con prescrizioni specifiche); GDPR per i dati di accesso; specifiche settore.
- **Nota di cantiere:** La domanda: 'chi può toccare questo rack e chi lo sa?' — la tracciabilità è la metà della sicurezza.

### L'edilizia del data center: struttura, pavimenti rialzati, altezze

**Categoria:** Struttura · **Corso:** Data center e critical facilities

L'edificio del data center ha esigenze particolari: i pavimenti rialzati (il sottopavimento è la plenum per l'aria fredda e i cavi, oppure tutto in over-head), le altezze generose (3-5 m sotto i controsoffitti per canalizzare aria e cavi), i carichi (i rack pieni pesano 800-1.500 kg/m²: le strutture vanno verificate), la possibilità di espansione.

- **Tecnologia e criteri:** Elementi: il pavimento rialzato (lastre removibili su piedini: ogni punto accessibile, il freddo passa sotto), il controsoffitto tecnico (i cavi e i sensori sopra), la struttura portante con luci ridotte e controventi? la struttura con portate ridotte per i carichi concentrati, le scalinature per i passaggi (porte di ventilazione? i varchi tra le sale con sigillature per non perdere l'aria), l'isolamento acustico (i server sono rumorosi: il muro tra sale server e uffici è fonoisolante).
- **Applicazioni:** Progettazione di nuovi data center e retrofit di edifici esistenti (la modalità più comune: ex-industriali riconvertiti).
- **Vantaggi:** L'edilizia del data center è ingegneria 'ospedaliera': pulizia, precisione, previsione dell'imprevisto.
- **Limiti e attenzioni:** Il retrofit dell'edificio esistente spesso non regge i carichi: le verifiche strutturali preliminari evitano cantieri bloccati.
- **Costi ed economia:** Costi: pavimento rialzato 80-200 €/m²; la struttura rinforzata: quota strutturale; l'edilizia base: 6.000-15.000 €/m².
- **Caso tipico:** Ex capannone industriale riconvertito a data center: il rinforzo dei solai con le verifiche preliminari ha permesso l'uso senza sostituzione della struttura; il progetto senza verifica (di un altro team, poi abbandonato) richiedeva la demolizione del solaio.
- **Normativa:** NTC (carichi); specifiche TIA-942; normativa antincendio e della sala.
- **Nota di cantiere:** La verifica preliminare dei carichi (rack pieni, pavimenti rialzati, i gruppi elettrogeni sul tetto o in cortile) è il primo passo di ogni progetto DC.


## Dimensionamento di fotovoltaico, eolico e accumulo

*Corso `DIMENSIONAMENTO_FV_EOLICO_ACCUMULO_PACK` — 10 voci*

### Il dimensionamento dell'accumulo in batteria: autoconsumo e backup

**Categoria:** Accumulo · **Corso:** Dimensionamento di fotovoltaico, eolico e accumulo

Quanti kWh di batteria servono: il calcolo dal profilo di consumo.

- **Tecnologia e criteri:** Metodo: batteria = consumo notturno (kWh) / DoD (80-90%): casa 3.000 kWh/anno con 40% di consumo serale/notturno: 1.200 kWh/anno ÷ 365 = 3,3 kWh/notte → batteria 4-5 kWh; per l'autoconsumo massimo (>70%): batteria 8-10 kWh o gestione carichi (PDC, scalda-acqua); il backup di emergenza: la potenza dell'inverter ibrido (3-10 kW) conta più dei kWh; il ciclo di vita: 6.000 cicli × 4 kWh = 24.000 kWh erogabili.
- **Applicazioni:** Ville con FV, case in zone con blackout, B&B.
- **Vantaggi:** La batteria giusta si calcola sul consumo NOTTURNO: il giorno il FV copre, la notte serve la batteria.
- **Limiti e attenzioni:** L'accumulo perde il 10-15% di resa (carica/scarica): l'autoconsumo 100% è matematicamente impossibile.
- **Costi ed economia:** Batteria 5 kWh: 2.000-3.500 €; 10 kWh: 4.000-7.000 €.
- **Caso tipico:** Le batterie LFP (fosfato ferro-litio) che stanno sostituendo il NMC nel residenziale.
- **Normativa:** UNI CEI 0-16; CEI 0-21.
- **Nota di cantiere:** Il quesito professionale prima della batteria: 'quanto consumi di notte?' Chi non sa rispondere vende batterie a caso. E la batteria si ripaga in 8-15 anni: il backup e le tariffe dinamiche accorciano, il prezzo dell'energia li determina.

### Il dimensionamento dell'eolico: la curva di potenza e la realtà dei siti

**Categoria:** Eolico · **Corso:** Dimensionamento di fotovoltaico, eolico e accumulo

Quando il vento conviene: la fisica onesta del microeolico.

- **Tecnologia e criteri:** Metodo: la curva di potenza della turbina: P = 0,5·ρ·A·v³·Cp (A = πr², Cp = 0,35-0,45): la potenza cresce col CUBO della velocità (da 5 a 7 m/s: +140%); il vento reale al suolo è il 60-70% del vento anemometrico a 10 m; la produzione richiede la mappa del vento del sito (atlanti ENEA); il microeolico residenziale (5-10 kW) rende 800-2.500 kWh/kW/anno SOLO in siti ventosi (coste, colline esposte).
- **Applicazioni:** Aziende agricole in collina, coste, isole.
- **Vantaggi:** La fisica è chiara: il cubo della velocità premia i siti veri e punisce quelli speranzosi.
- **Limiti e attenzioni:** Il 90% dei siti residenziali italiani ha vento insufficiente: il microeolico è spesso una delusione costosa (spirito critico richiesto).
- **Costi ed economia:** Le torri anemometriche (500-2.000 €) per la misura di 12 mesi.
- **Caso tipico:** Le isole minori (Ventotene, Pantelleria) dove l'eolico è la regola; i microeolici 'da giardino' abbandonati.
- **Normativa:** Nessuna specifica: fisica + certificazione CE.
- **Nota di cantiere:** La regola d'oro dell'eolico: 'misura per un anno prima di comprare'. Il venditore che promette 3.000 kWh dal vento 'che c'è sempre' vende fuffa: il vento che basta vive in pochi siti, e va DIMOSTRATO.

### Esempio svolto: impianto FV 6 kWp con accumulo 5 kWh per una famiglia tipo

**Categoria:** Esempio FV · **Corso:** Dimensionamento di fotovoltaico, eolico e accumulo

Il progetto FV completo, dal tetto alla bolletta.

- **Tecnologia e criteri:** Dati: consumo 3.600 kWh/anno, villa centro Italia (produzione 1.450 kWh/kWp); 1) P = 6 kWp (superficie 36 m² sud, tetto ok); 2) produzione = 8.700 kWh/anno; 3) autoconsumo senza batteria 30%: 2.600 kWh; con batteria 5 kWh: 60%: 5.200 kWh; 4) risparmio: 5.200 × 0,30 € = 1.560 €/anno + vendita eccedenza 3.500 × 0,10 € = 350 €; 5) costo: 9.000 € (FV+batteria) - incentivo eventuale; 6) ritorno: ~5-6 anni senza incentivo, 3-4 con Conto Termico/cessione credito.
- **Applicazioni:** Modello replicabile per il 90% delle ville italiane.
- **Vantaggi:** L'esempio dimostra la catena: tetto -> produzione -> autoconsumo -> bolletta -> ritorno.
- **Limiti e attenzioni:** I prezzi dell'energia variano: il calcolo va rifatto coi prezzi attuali.
- **Costi ed economia:** PVGIS + listini installatori.
- **Caso tipico:** La diffusione del FV+accumulo in Italia (dati GSE 2024-2025: oltre 1,5 milioni di impianti).
- **Normativa:** CEI 0-21; GSE.
- **Nota di cantiere:** Il controllo professionale: il preventivo FV deve contenere la simulazione di produzione (PVGIS o equivalente) firmata: la promessa verbale 'produrrà tanto' non vale. E il primo confronto dopo 12 mesi tra produzione reale e stimata è la vera verifica dell'installatore.

### Il cablaggio DC e AC del fotovoltaico: sezioni e protezioni

**Categoria:** FV cablaggi · **Corso:** Dimensionamento di fotovoltaico, eolico e accumulo

I cavi del FV: dimensionamento rapido e le protezioni obbligatorie.

- **Tecnologia e criteri:** DC: la corrente di stringa (10-15 A) richiede cavi 4-6 mm² (rame, isolamento doppio, nero/rosso); la caduta di tensione DC <2%; i connettori MC4 (o compatibili certificati); AC: l'inverter 5 kW trifase? no monofase: 22 A → cavo 6 mm², magnetotermico 25 A, differenziale tipo B (le correnti del FV sono continue: il tipo A non basta); scaricatori SPD tipo 1+2 se edificio con LPS; la messa a terra dei telai.
- **Applicazioni:** Ogni impianto fotovoltaico.
- **Vantaggi:** Il dimensionamento elettrico corretto è la sicurezza: un cavo sottodimensionato surriscalda e brucia.
- **Limiti e attenzioni:** Il differenziale tipo B costa 200-400 €: il risparmio qui è falso.
- **Costi ed economia:** Cavi solari 6 mm²: 2-4 €/ml.
- **Caso tipico:** Gli impianti con SPD e tipo B conformi CEI 0-21.
- **Normativa:** CEI 0-21; CEI 64-8.
- **Nota di cantiere:** La regola: nel FV il differenziale è tipo B, lo scaricatore è presente, la messa a terra è fatta. Le tre cose valgono più della marca dei pannelli.

### Il dimensionamento del fotovoltaico: dal consumo ai kWp

**Categoria:** FV dimensionamento · **Corso:** Dimensionamento di fotovoltaico, eolico e accumulo

Quanti pannelli servono: la procedura completa con i numeri.

- **Tecnologia e criteri:** Metodo: 1) consumo annuo in bolletta (kWh); 2) produzione specifica locale (kWh/kWp: 1.200-1.500 nord, 1.300-1.600 centro, 1.400-1.700 sud); 3) P_install = consumo × (autoconsumo_target)/(produzione specifica): es. 4.000 kWh/anno in centro con autoconsumo 70%: 4.000·0,7/1.400 ≈ 2 kWp minimi, ma 3-6 kWp è il range economico; 4) verifica superficie: 1 kWp ≈ 5-6 m² di tetto; 5) verifica carichi strutturali: 12-18 kg/m² (ok quasi sempre).
- **Applicazioni:** Ogni edificio con tetto o area disponibile.
- **Vantaggi:** La procedura dal consumo evita il classico errore 'il venditore ha detto 10 kWp' per una casa da 3.000 kWh.
- **Limiti e attenzioni:** La produzione reale varia del ±15% col meteo: il contratto deve parlare di stime, non promesse.
- **Costi ed economia:** Simulatore PVGIS (gratuito) per i dati locali precisi.
- **Caso tipico:** La casa media italiana (2.700 kWh/anno) con 3 kWp e autoconsumo 30%: ~1.300 kWh auto-usati + vendita del resto.
- **Normativa:** CEI 0-21; UNI 9174.
- **Nota di cantiere:** Regola pratica: il FV si dimensiona sul CONSUMO, il tetto è il vincolo, la batteria è l'optional. Chi parte dal tetto ('mettiamo 20 pannelli perché ci stanno') ha capito tutto al contrario.

### Il dimensionamento delle stringhe e degli inverter

**Categoria:** FV stringhe · **Corso:** Dimensionamento di fotovoltaico, eolico e accumulo

Come si collegano i moduli: tensioni, correnti e il rapporto inverter.

- **Tecnologia e criteri:** Metodo: la tensione di stringa: somma delle Vmp dei moduli in serie: es. 10 moduli × 34 V = 340 Vmp (entro il MPPT dell'inverter 200-800 V); la Voc massima inverno (Voc aumenta col freddo: +0,3%/°C sotto ai 25°C: 10×41 V×1,1 ≈ 450 V < 1000 V massimo inverter); la corrente: le stringhe in parallelo sommano le correnti (Imodulo 11 A × 2 stringhe = 22 A); il rapporto DC/AC: 1,1-1,3 (es. 6 kWp con inverter 5 kW) per sfruttare le ore di punta; l'ombreggiamento: i diodi di bypass limitano le perdite parziali.
- **Applicazioni:** Impianti residenziali e industriali.
- **Vantaggi:** La verifica tensione freddo-caldo è la regola che evita i guasti: la Voc invernale non deve superare il massimo dell'inverter.
- **Limiti e attenzioni:** Le curve reali di potenza variano: il rapporto 1,2 è un compromesso, non una legge.
- **Costi ed economia:** I software di stringatura gratuiti dei produttori di inverter.
- **Caso tipico:** Gli impianti con rapporto 1,3: perdita di resa <2% rispetto a 1,0 con costo inverter inferiore.
- **Normativa:** CEI 0-21; CEI 82-25 (da verificare: guida installazione FV).
- **Nota di cantiere:** Il controllo d'installazione: la Voc di stringa si misura PRIMA del collegamento all'inverter: la lettura deve stare nel range MPPT. Un errore qui brucia l'inverter in 30 secondi.

### I sistemi ibridi FV + batteria + rete + generatore: il dimensionamento integrato

**Categoria:** Ibridi · **Corso:** Dimensionamento di fotovoltaico, eolico e accumulo

L'impianto che non si ferma mai: logica e dimensionamento degli ibridi.

- **Tecnologia e criteri:** Metodo: la gerarchia di priorità: FV -> batteria -> rete (se presente) -> generatore di backup (gasolio/GPL/biometano); il dimensionamento dell'autonomia: giorni senza sole × consumo giornaliero / DoD: 3 gg × 8 kWh / 0,8 = 30 kWh di batteria; il generatore di backup: potenza = carichi essenziali (frigo, luci, PDC ridotta): 5-10 kVA; l'energy manager che commuta le fonti senza interruzioni.
- **Applicazioni:** Case isolate, agriturismi, rifugi, B&B, cantine? no: 'aziende con continuità richiesta'.
- **Vantaggi:** L'ibrido corretto dà l'autonomia senza il diesel quotidiano: il generatore è l'ultima spiaggia, non la routine.
- **Limiti e attenzioni:** La complessità di gestione richiede una centralina di supervisione professionale.
- **Costi ed economia:** Energy manager: 1.000-3.000 €; generatore backup: 2.000-8.000 €.
- **Caso tipico:** I rifugi alpini con FV + batteria + generatore (il diesel accende una volta al mese).
- **Normativa:** CEI 0-16; normativa connessione.
- **Nota di cantiere:** La logica dell'ibrido: 'ogni fonte fa ciò che fa meglio'. Il FV copre il sole, la batteria la notte, il generatore l'emergenza. Chi fa tutto col generatore paga il triplo.

### Il dimensionamento off-grid: l'autonomia totale senza rete

**Categoria:** Off-grid · **Corso:** Dimensionamento di fotovoltaico, eolico e accumulo

Vivere senza ENEL: la matematica dell'autonomia completa.

- **Tecnologia e criteri:** Metodo: 1) bilancio energetico giornaliero: somma di tutti i consumi × ore (frigo 1,5 kWh/g, luci 0,5, PDC invernale 6-10...); 2) il FV dimensionato sul peggiore mese (dicembre: 1/3 della produzione estiva); 3) la batteria: 2-3 giorni di autonomia: (kWh/giorno × giorni) / DoD; 4) il backup (generatore) per le settimane di maltempo; es. casa efficiente inverno: 10 kWh/giorno → FV 6 kWp + batteria 30 kWh + generatore 8 kVA.
- **Applicazioni:** Case isolate, baite, podere? no: 'podere' sì, postazioni remote.
- **Vantaggi:** L'off-grid perfetto dà indipendenza e risparmio sulla tratta? no: 'sulla connessione' (chi evita il preventivo ENEL da 20k€).
- **Limiti e attenzioni:** L'off-grid peggiora: la disciplina dei consumi è obbligatoria: niente pannelli elettrici? no: 'niente sprechi'.
- **Costi ed economia:** Il costo dell'off-grid serio: 20-60k€.
- **Caso tipico:** Le comunità energetiche (CER) che portano il modello 'condiviso' nei paesi.
- **Normativa:** CEI 0-16; normativa CER (ARERA).
- **Nota di cantiere:** La verità dell'off-grid: non è 'staccare la spina', è 'diventare il proprio gestore'. Chi non vuole gestire l'energia non deve andare off-grid: la rete è un servizio, e pagarlo costa meno dell'indipendenza per molti.

### Il dimensionamento della pompa di calore: il metodo binario completo

**Categoria:** PDC dimensionamento · **Corso:** Dimensionamento di fotovoltaico, eolico e accumulo

Come si dimensiona una PDC in 6 passi verificati.

- **Tecnologia e criteri:** Metodo: 1) il fabbisogno termico di progetto (UNI EN 12831); 2) i punti bin: la tabella delle temperature esterne e le ore annue a ciascuna temperatura (bin di 2°C); 3) la COP a ciascun bin (dalle curve del costruttore): il rendimento annuo SCOP = Σ(produzione bin)/(Σ consumi bin); 4) la copertura: la PDC copre il 100% fino a una certa temperatura (punto di equilibrio), sotto serve integrazione; 5) il dimensionamento del campo sorgente (aerotermo: spazio, rumore, defrost); 6) la verifica ACS: il serbatoio e il ricircolo.
- **Applicazioni:** La scelta tecnica principale delle nuove costruzioni italiane.
- **Vantaggi:** Il metodo bin dà il rendimento REALE: il COP di targa è marketing, lo SCOP è fisica.
- **Limiti e attenzioni:** I dati dei bin vanno da fonti climatiche locali (non tutti i costruttori li pubblicano).
- **Costi ed economia:** I software di calcolo del costruttore (gratuiti) che integrano i bin.
- **Caso tipico:** Le PDC dimensionate 'a spanne' che consumano il doppio del previsto: il motivo è quasi sempre l'assenza del calcolo bin.
- **Normativa:** UNI EN 14825 (SCOP); UNI/TS 11300.
- **Nota di cantiere:** Il quesito professionale: 'mi mostri lo SCOP calcolato col metodo bin per la mia zona climatica?' Chi non risponde vende sulla fiducia. La PDC è la macchina del decennio: va scelta col calcolo, non col volantino.

### Il dimensionamento del solare termico: collettori e accumulo

**Categoria:** Solare termico · **Corso:** Dimensionamento di fotovoltaico, eolico e accumulo

L'acqua calda dal sole: come si dimensiona l'impianto solare termico.

- **Tecnologia e criteri:** Metodo: l'accumulo: 40-75 l/m² di collettore piano (standard 50 l/m²); i collettori: 1,5-2 m² per persona in famiglia; il contributo solare: 40-60% del fabbisogno ACS annuo; l'orientamento: sud ±45°, inclinazione 30-60°; l'integrazione: con caldaia a condensazione o PDC (il solare scalda, l'integrazione 'rifinisce'); l'impianto a circolazione forzata con scambiatore a fascio o a piastre.
- **Applicazioni:** Abitazioni, condomini, hotel, piscine (riscaldamento).
- **Vantaggi:** Il solare termico è la tecnologia più semplice e robusta: rende per 25 anni con manutenzione minima.
- **Limiti e attenzioni:** Il gelo: i collettori vanno svuotati? no: 'l'impianto con glicole' gestisce il gelo, ma la manutenzione del fluido è obbligatoria.
- **Costi ed economia:** Impianto famiglia 4 persone: 4 m² collettori + accumulo 200 l: 3.000-5.000 € installato.
- **Caso tipico:** Il Conto Termico 3.0 incentiva il solare termico (premio al netto).
- **Normativa:** UNI EN 12976; UNI/TS 12977.
- **Nota di cantiere:** Il ritorno del solare termico: nel 2020 sembrava morto, nel 2025 torna forte per la semplicità. Le regole: accumulo giusto, orientamento giusto, integrazione corretta. L'errore classico: i collettori troppo grandi per l'accumulo (estate = bollore).


## Dimensionamento degli impianti termotecnici

*Corso `DIMENSIONAMENTO_TERMOTECNICO_PACK` — 9 voci*

### Il dimensionamento dell'acqua calda sanitaria: accumuli, portate, ricircolo

**Categoria:** ACS · **Corso:** Dimensionamento degli impianti termotecnici

Quanta acqua calda serve davvero: il dimensionamento degli accumuli e delle reti ACS.

- **Tecnologia e criteri:** Metodo: fabbisogno 40-60 l/persona/die a 40°C; accumulo: V = fabbisogno_punto × (60/ΔT_accumulo) [accumulo a 60°C vs uso 40°C: i litri utili sono il 50% in più]; la produzione istantanea (scaldabagno/caldaia a flusso): portata doccia 6-9 l/min a 38°C; il ricircolo obbligatorio per percorsi >15-20 m (pompa con timer/temperatura); la legionella: accumulo a 60-65°C, ricircolo monitorato, scarico settimanale >60°C ai punti più lontani.
- **Applicazioni:** Abitazioni, condomini, hotel, palestre, uffici.
- **Vantaggi:** L'ACS è il 30-40% della bolletta energetica: dimensionarla bene vale quanto l'involucro.
- **Limiti e attenzioni:** Gli accumuli grandi mantengono meglio la temperatura? no: 'perdono': l'accumulo perde calore in proporzione al volume: scegliere l'accumulo GIUSTO.
- **Costi ed economia:** Accumulo 100 l: 150-400 €; scambiatore a fascio: +20-30% sulla caldaia.
- **Caso tipico:** Le norme anti-legionella negli edifici pubblici (acqua a 50°C nei punti di erogazione con valvole termostatiche).
- **Normativa:** UNI EN 806; linee guida ISS legionella.
- **Nota di cantiere:** La regola dell'accumulo: meglio piccolo e spesso rinnovato che grande e stagnante. La legionella ama l'acqua ferma a 30-45°C: l'accumulo a 60°C con scarichi settimanali è il vaccino.

### Il dimensionamento dei corpi scaldanti: termosifoni e radiatori

**Categoria:** Corpi scaldanti · **Corso:** Dimensionamento degli impianti termotecnici

Quanti Watt serve per ogni stanza: il metodo dei ΔT nominali.

- **Tecnologia e criteri:** Metodo: Q_corpo = carico stanza / correttivo; la potenza nominale dei radiatori è dichiarata a ΔT=50°C (mandata 75, ritorno 65, ambiente 20): con mandate basse (PDC 45°C, ΔT=25) la potenza reale cade del 50-60%: usare la formula del costruttore Q = Q_n·(ΔT/50)^n (n≈1,3); il numero di elementi = Q_stanza / potenza elemento.
- **Applicazioni:** Ogni impianto a termosifoni.
- **Vantaggi:** La formula del ΔT spiega il 90% dei 'termosifoni freddi con la PDC': non sono pochi, sono sottodimensionati per la temperatura di mandata.
- **Limiti e attenzioni:** La verifica corretta richiede i dati del costruttore (le curve di rendimento).
- **Costi ed economia:** Radiatore alluminio 600 mm: 120-200 W/elemento a ΔT50; a ΔT25 serve il doppio degli elementi.
- **Caso tipico:** Le case in PDC con radiatori raddoppiati (o radianti) per andare a 35-45°C.
- **Normativa:** UNI EN 442 (radiatori).
- **Nota di cantiere:** Il trucco pratico: con PDC a 45°C, progettare come se il carico raddoppiasse: termosifoni grandi e belli o pannelli radianti. Le ali? no: 'le piastre': chi mette la PDC coi termosifoni vecchi sottodimensionati ha buttato metà dell'incentivo.

### Esempio svolto: il dimensionamento termico di una villa di 180 m²

**Categoria:** Esempio completo · **Corso:** Dimensionamento degli impianti termotecnici

Il progetto termico completo passo per passo, con i numeri veri.

- **Tecnologia e criteri:** Fabbisogno: villa 180 m², zona E, U=0,45: Q = 0,45·380 m²·24 + 0,34·450·0,5·24 ≈ 4.100 + 1.840 ≈ 6 kW; generatore: PDC 8 kW (margine ACS) COP 3,5 a 35°C; corpi: radianti 45°C con passo 15 cm (45-55 W/m²) su 130 m²; ACS: accumulo 200 l a 60°C con ricircolo 15 m; VMC: 180 m² × 2,7 m × 0,5 ricambi = 250 m³/h; consumo stimato: 6.000 kWh termici / COP 3,5 ≈ 1.700 kWh elettrici ≈ 500 €/anno.
- **Applicazioni:** Modello replicabile per qualsiasi residenza unifamiliare.
- **Vantaggi:** L'esempio mostra la catena: fabbisogno -> macchina -> emissione -> aria -> costo finale.
- **Limiti e attenzioni:** I numeri cambiano col clima e l'involucro: l'esempio è il metodo, non la tabella.
- **Costi ed economia:** Il metodo è gratuito: carta e UNI/TS 11300.
- **Caso tipico:** Migliaia di ville italiane con questi numeri (Legge 10 2024).
- **Normativa:** UNI/TS 11300; UNI EN 12831.
- **Nota di cantiere:** Il controllo finale professionale: il consumo stimato deve corrispondere alla bolletta del primo anno: scostamenti >30% = errore di dimensionamento da scoprire, non da nascondere.

### Il calcolo del fabbisogno termico: da dove si parte

**Categoria:** Fabbisogno · **Corso:** Dimensionamento degli impianti termotecnici

La prima pagina di ogni progetto termico: come si calcola il carico di progetto.

- **Tecnologia e criteri:** Metodo: Q = Σ(U·A·ΔT) trasmisssione + 0,34·V·n·ΔT ventilazione; il ΔT di progetto = temperatura interna (20°C) − temperatura esterna di progetto (zona climatica: −5°C nord, −2°C centro, +2°C sud); gli apporti interni (persone, luci) e solari si sottraggono; il fabbisogno dinamico annuo usa i gradi-giorno (GG ENEA).
- **Applicazioni:** Scelta del generatore, verifica legge 10, confronto involucri.
- **Vantaggi:** Il carico di progetto è la base di TUTTO: generatore, tubazioni, corpi scaldanti si dimensionano su questo numero.
- **Limiti e attenzioni:** La stima per m² (100 W/m² storica, 40-60 W/m² casa efficiente) è solo per preventivi, mai per il progetto.
- **Costi ed economia:** I gradi-giorno per comune sono pubblici (Enea).
- **Caso tipico:** Casa 150 m², U medio 0,6, superficie dispersa 320 m², ΔT=24°C (zona E): Q_trasm = 0,6·320·24 ≈ 4.600 W + ventilazione ~1.400 W = ~6 kW di fabbisogno di picco.
- **Normativa:** UNI/TS 11300; UNI EN 12831.
- **Nota di cantiere:** Regola d'oro: chi dimensiona il generatore SENZA aver calcolato il fabbisogno sta giocando d'azzardo con i soldi del cliente.

### Il dimensionamento del generatore: caldaia, PDC, ibrido

**Categoria:** Generatore · **Corso:** Dimensionamento degli impianti termotecnici

Come si sceglie la potenza del cuore termico: mai 'un po' più grande tanto paga'... anzi sì ma no.

- **Tecnologia e criteri:** Metodo: P_generatore = Q_fabbisogno · (1 + margine 10-20%); il MARGINE serve per il rapido ripristino dell'ACS (carico istantaneo) e il ricircolo; la PDC: P = fabbisogno a T_esterna di progetto con COP accettabile, spesso si accetta la copertura parziale al punto di progetto con integrazione (punti binari); l'ibrido: PDC dimensionata sul 60-80% del fabbisogno + caldaia sul picco.
- **Applicazioni:** Ogni nuovo impianto termico.
- **Vantaggi:** Il sovradimensionamento è il male: cicli di accensione brevi, consumi e usura (soprattutto caldaie a gas).
- **Limiti e attenzioni:** Il sottodimensionamento PDC invernale richiede l'integrazione: va progettata, non scoperta a dicembre.
- **Costi ed economia:** La differenza di costo tra una caldaia da 24 e 35 kW: 100-200 € (inutile comprare il sovradimensionamento).
- **Caso tipico:** La modulazione minima delle caldaie (3 kW) che convive coi fabbisogni da 4-6 kW delle case efficienti.
- **Normativa:** UNI EN 12831; UNI/TS 11300.
- **Nota di cantiere:** Il test professionale: chiedere 'qual è il fabbisogno di picco della casa?' Se l'installatore non sa rispondere, sta vendendo una macchina a caso. Il miglior investimento è l'audit, non il sovradimensionamento.

### L'integrazione di generatori diversi: termocamino, termostufa, solare, caldaia

**Categoria:** Integrazione generatori · **Corso:** Dimensionamento degli impianti termotecnici

Come fanno a convivere più generatori: il dimensionamento della logica, non solo delle macchine.

- **Tecnologia e criteri:** Metodo: la logica a priorità (il generatore 'gratuito' o rinnovabile va in testa: solare termico -> termocamino/termosufa -> PDC -> caldaia); il bollitore con doppio scambiatore o serpentina; il dimensionamento dell'accumulo come 'cuscinetto' tra produzione intermittente e fabbisogno: accumulo = 50-100 l/kW di potenza intermittente (termocamino) o 20-40 l/m² di solare termico; la valvola/miscelatrice per temperature diverse.
- **Applicazioni:** Impianti ibridi complessi: villa con camino, solare, PDC.
- **Vantaggi:** L'accumulo giusto rende amici generatori diversi: ognuno lavora al suo turno.
- **Limiti e attenzioni:** La logica di gestione elettronica va progettata PRIMA delle macchine.
- **Costi ed economia:** Valvole deviatrici: 150-400 €; centraline di gestione: 200-600 €.
- **Caso tipico:** Gli impianti 'a cascata' delle case alpine (legna -> solare -> integrazione).
- **Normativa:** UNI 7129; UNI EN 15316.
- **Nota di cantiere:** La frase d'ordine: 'prima l'accumulo, poi i generatori'. Chi compra la macchina prima del serbatoio costruisce un puzzle senza cornice.

### Il dimensionamento del pavimento/soffitto radiante

**Categoria:** Radianti · **Corso:** Dimensionamento degli impianti termotecnici

Il radiante si calcola per portata: il metodo UNI EN 1264.

- **Tecnologia e criteri:** Metodo: il carico per stanza si copre con il 60-70% della superficie utile a portata media 40-60 W/m² (masso 100 W/m² pavimento, 90 soffitto); la temperatura di mandata 28-35°C (pavimento), 27-32°C (soffitto); il passo dei tubi (10-30 cm) regola la potenza: passo 10 cm ≈ 60-70 W/m², passo 20 cm ≈ 40-50 W/m²; la portata acqua: q = Q/(1,16·ΔT mandata-ritorno 4-6 K) in l/h.
- **Applicazioni:** Case in PDC, ristrutturazioni con massetto, soffitti radianti per raffrescamento.
- **Vantaggi:** Il radiante funziona a temperature irraggiamento: il comfort migliore con l'acqua più fredda possibile.
- **Limiti e attenzioni:** Le perdite verso il basso (la trasmittanza verso il solaio) vanno isolate: senza isolamento il radiante scalda i vicini.
- **Costi ed economia:** Radiante in massetto: 40-80 €/m2 installato; soffitto radiante: 50-100 €/m2.
- **Caso tipico:** Le 'zone radianti' con collettore dedicato e valvole termostatiche (obbligatorie).
- **Normativa:** UNI EN 1264 (1-5).
- **Nota di cantiere:** La verifica di cantiere: il termometro IR sulla superficie: il pavimento deve arrivare a 26-29°C in superficie (non bollente: irradia piano). Se il massetto scalda troppo in poche ore, il controllo è sbagliato: il radiante è lentezza programmata.

### Il dimensionamento del raffrescamento: carichi estivi e deumidifica

**Categoria:** Raffrescamento · **Corso:** Dimensionamento degli impianti termotecnici

L'estate si calcola come l'inverno: il carico di raffrescamento in 5 mosse.

- **Tecnologia e criteri:** Metodo: Q_estivo = trasmissione (U·A·ΔT notturno) + irraggiamento finestre (W·SHGC) + carico interno (persone 60-80 W sensibili + apparecchi) + ventilazione; la deumidifica: la portata d'aria deve assorbire l'umidità interna (docce, cucina): la macchina lavora a 7°C di espansione per condensare; il raffrescamento radiante gestisce il SENSIBILE, la VMC gestisce il LATENTE (umidità).
- **Applicazioni:** Climatizzazione estiva di case e uffici.
- **Vantaggi:** La deumidifica è metà del comfort estivo: una casa a 26°C e 45% UR è più fresca di una a 24°C e 70%.
- **Limiti e attenzioni:** Il carico estivo è variabile: il dimensionamento pieno per il picco di 3 giorni è sprecato.
- **Costi ed economia:** Il concetto di 'gradi-ora' estivi (pubblico ENEA).
- **Caso tipico:** Raffrescamento radiante + VMC con deumidifica: la coppia standard delle case efficienti.
- **Normativa:** UNI EN ISO 13791/13792.
- **Nota di cantiere:** La regola del comfort: la temperatura operativa (aria + superfici) è la realtà percepita: un radiante a 24°C dà la freschezza di un condizionatore a 21°C, senza spifferi e con meno energia.

### Il dimensionamento della VMC: portate, diametri e perdite

**Categoria:** VMC dimensionamento · **Corso:** Dimensionamento degli impianti termotecnici

Come si calcola la rete di ventilazione: dal volume d'aria alla bocchetta.

- **Tecnologia e criteri:** Metodo: portata ambiente = numero persone × 25-30 m³/h (o ricambi minimi UNI 10339); dimensionamento condotte: velocità 2-3 m/s nei principali, 1,5-2 nelle derivazioni (per limitare il rumore a <30 dB in camera); il diametro da Q e velocità: A = Q/v; perdite di carico: il metodo della lunghezza equivalente (curve = 2-4 m di condotto); la spinta disponibile della centralina (100-300 Pa).
- **Applicazioni:** Nuove costruzioni, ristrutturazioni, uffici, scuole.
- **Vantaggi:** La VMC silenziosa nasce dal calcolo: la velocità bassa nei rami finali è il segreto.
- **Limiti e attenzioni:** I software di calcolo (anche gratuiti) aiutano, ma la verifica acustica finale resta la misura.
- **Costi ed economia:** La verifica: anemometro a ogni bocchetta (50-100 €).
- **Caso tipico:** Le VMC con sonda CO2 che modulano le portate in base all'effettiva presenza.
- **Normativa:** UNI 10339; UNI EN 13779.
- **Nota di cantiere:** La regola pratica: la bocchetta in camera da letto deve essere appena udibile: se la senti, è troppo veloce. Ridurre il diametro? no: aumentare: la velocità scende col quadrato del diametro.


## Domotica e building automation

*Corso `DOMOTICA_PACK` — 29 voci*

### Controllo accessi

**Categoria:** Accessi · **Corso:** Domotica e building automation

Gestione ingressi: badge, RFID, QR, biometria, serrature smart.

- **Tecnologia e criteri:** Wiegand/OSDP per lettori; RFID 125kHz/13.56MHz; biometria impronta/volto; serrature motorizzate.
- **Applicazioni:** Uffici, cantieri, palestre, B&B (check-in digitale).
- **Vantaggi:** Tracciabilità ingressi; revoca immediata; niente chiavi perse.
- **Limiti e attenzioni:** La biometria è dato sensibile GDPR; blackout = aprire in sicurezza (fail-safe vs fail-secure).
- **Costi ed economia:** Lettore: 50-300 €; serratura smart: 150-600 €; software: 100-500 €/anno.
- **Caso tipico:** Kaba, SALTO, Nuki (residenziale), August.
- **Normativa:** GDPR biometria; EN 60839 controllo accessi.
- **Nota di cantiere:** Cantieri: il controllo accessi con timbratura integrata risolve giacenze e sicurezza (chi è in cantiere in caso d'emergenza).

### Architettura di un impianto domotico

**Categoria:** Architettura · **Corso:** Domotica e building automation

Come è organizzato un impianto domotico: sensori, attuatori, bus, supervisione, cloud.

- **Tecnologia e criteri:** Topologia a livelli: campo (sensori/attuatori) -> controllo (attuatori bus/KNX) -> gestione (supervisore/HMI) -> cloud/servizi.
- **Applicazioni:** Qualsiasi edificio: residenziale, terziario, industriale, hospitality.
- **Vantaggi:** Struttura modulare ed espandibile; ogni livello può evolvere indipendentemente.
- **Limiti e attenzioni:** Progettazione sbagliata = rigetto costoso; serve un progettista qualificato (tra cui certificazione KNX Partner).
- **Costi ed economia:** Impianto base appartamento: 3-8k€; villa completa: 10-40k€; edificio terziario: 20-100 €/m2.
- **Caso tipico:** Standard KNX Association per l'architettura a 3 livelli.
- **Normativa:** L.46/90 (criteri CEN); CEI 64-8 per la parte elettrica.
- **Nota di cantiere:** Prima regola: definire gli scenari di vita PRIMA dei protocolli: la tecnologia serve il comfort, non il contrario.

### Domotica assistiva e senior living

**Categoria:** Assistiva · **Corso:** Domotica e building automation

La casa che aiuta: monitoraggio non invasivo di anziani, sicurezza, teleassistenza.

- **Tecnologia e criteri:** Sensori presenza mm-wave, letti smart, pulsantiere, rilevamento cadute (radar), notifiche caregiver.
- **Applicazioni:** Abitazioni anziani, RSA, housing sociale, home care.
- **Vantaggi:** Autonomia prolungata a domicilio; famiglia tranquilla; dati per teleassistenza.
- **Limiti e attenzioni:** Equilibrio tra controllo e autonomia: il consenso è eticamente obbligatorio.
- **Costi ed economia:** Kit assistenza: 300-1.500 €; servizio monitoring: 20-50 €/mese.
- **Caso tipico:** Vayyar radar, Nokia/Withings, soluzioni KNX Health.
- **Normativa:** GDPR (datore di lavoro no; famiglia sì con consenso).
- **Nota di cantiere:** Il valore sociale è enorme: una caduta rilevata in 2 minuti vale più di qualsiasi scenario 'cinema'.

### Attuatori domotici

**Categoria:** Attuatori · **Corso:** Domotica e building automation

Le mani dell'impianto: relè, dimmer, motori, valvole, attuatori multifunzione.

- **Tecnologia e criteri:** Attuatori bus (KNX) o Wi-Fi; attuatori a relè per carichi; attuatori motori per tapparelle; valvole termostatiche elettroniche.
- **Applicazioni:** Attuare luci, carichi, tapparelle, clima, irrigazione, serrature.
- **Vantaggi:** Sostituzione quasi plug-and-play in centralino; diagnostica da bus.
- **Limiti e attenzioni:** Compatibilità carichi (LED, motori) da verificare; scatti elettrici su bobine.
- **Costi ed economia:** Attuatore 4 canali KNX: 150-300 €; attuatore Wi-Fi: 15-40 €.
- **Caso tipico:** MDT, Jung, Gira (KNX); Shelly, Sonoff (Wi-Fi).
- **Normativa:** Marcatura CE; CEI 64-8-4 protezioni.
- **Nota di cantiere:** Sovradimensionare i contatti per i carichi capacitivi LED: la regola è corrente nominale x3 in scelta.

### KNX Secure (cybersecurity)

**Categoria:** BUS cablato · **Corso:** Domotica e building automation

Estensione KNX per cifrare i telegrammi e autenticare i dispositivi.

- **Tecnologia e criteri:** Crittografia AES-128 CCM; meccanismi IP Secure e Data Secure; chiavi per edificio.
- **Applicazioni:** Edifici sensibili (banche, ospedali, hotel luxury), chiunque voglia proteggere l'impianto da accessi remoti.
- **Vantaggi:** Conformità alla cybersecurity dell'impianto; requisito sempre più richiesto dagli appalti pubblici.
- **Limiti e attenzioni:** Retrofit complesso su impianti vecchi; gestione chiavi disciplinata.
- **Costi ed economia:** +10-20% sui componenti; nessun cambio architetturale.
- **Caso tipico:** Mandato sempre più frequente in gare d'appalto europee.
- **Normativa:** IEC 62443 (cybersecurity industriale) come riferimento.
- **Nota di cantiere:** Abilitare KNX Secure in fase di messa in servizio, non dopo: la migrazione a cantiere finito costa il triplo.

### KNX/EIB (bus europeo)

**Categoria:** BUS cablato · **Corso:** Domotica e building automation

Il protocollo bus cablato più diffuso al mondo per edilizia residenziale e terziaria.

- **Tecnologia e criteri:** Bus a 2 fili (TP) 9600 baud; telegrammi; indirizzi fisici/logici; ETS come software di progettazione.
- **Applicazioni:** Controllo luce, clima, tapparelle, sicurezza, energia in edifici nuovi e retrofit.
- **Vantaggi:** Affidabilità certificata (decenni di esercizio); interoperabilità tra 500+ produttori; standard aperto (ISO/IEC 14543-3).
- **Limiti e attenzioni:** Costo cavo e componenti superiore al wireless; progettazione ETS specializzata.
- **Costi ed economia:** Attuatore KNX: 80-300 €; sensore: 50-250 €; software ETS: licenza 200-1.000 €.
- **Caso tipico:** Ospedali, stadi, aeroporti, hotel di lusso; ~500 milioni di dispositivi installati.
- **Normativa:** EN 50090 / ISO-IEC 14543-3; marchio KNX.
- **Nota di cantiere:** In retrofit il bus viaggia spesso sul 230V esistente (KNX Powerline) o su wireless KNX.

### LonWorks / TP

**Categoria:** BUS cablato · **Corso:** Domotica e building automation

Piattaforma di controllo di rete per automazione edilizia (storica).

- **Tecnologia e criteri:** Neuron Chip; Free Topology; LonTalk.
- **Applicazioni:** Trasporti, tunnel, illuminazione pubblica, alcuni BMS.
- **Vantaggi:** Robustezza in ambienti difficili; topologia libera.
- **Limiti e attenzioni:** Ecosistema in declino rispetto a KNX/BACnet; competenze rare.
- **Costi ed economia:** Componenti costosi e di nicchia.
- **Caso tipico:** Tunnel stradali, aeroporti storici.
- **Normativa:** ISO/IEC 14908.
- **Nota di cantiere:** Menzionare per cultura: i nuovi progetti scelgono KNX o BACnet.

### BACnet

**Categoria:** BUS edifici terziari · **Corso:** Domotica e building automation

Protocollo per l'automazione di edifici terziari (HVAC, centrali termiche, BMS).

- **Tecnologia e criteri:** BACnet/IP e BACnet MS/TP; oggetti standard (analog input, binary output...); BIBB per interoperabilità.
- **Applicazioni:** Uffici, ospedali, scuole, centri commerciali: supervisione impianti e contabilizzazione.
- **Vantaggi:** Standard ISO (ISO 16484-5); scambio dati tra marche diverse di centraline e BMS.
- **Limiti e attenzioni:** Più complesso del KNX lato residenziale; orientato al tecnico impiantista.
- **Costi ed economia:** Gateway BACnet: 300-1.500 €; integrazione in BMS: 2-10k€ per edificio.
- **Caso tipico:** Metasys (JCI), Desigo (Siemens), Niagara Framework come supervisor.
- **Normativa:** ISO 16484; EN di prodotto per componenti.
- **Nota di cantiere:** Per il LLM: BACnet parla 'impianti', KNX parla 'stanze': gli edifici intelligenti usano entrambi con un gateway.

### Modbus

**Categoria:** BUS industriale · **Corso:** Domotica e building automation

Protocollo seriale/TCP semplice per controllori, inverter, centrali misura.

- **Tecnologia e criteri:** Modbus RTU (seriale RS485) e Modbus TCP; registro a 16 bit; master/slave.
- **Applicazioni:** Fotovoltaico (inverter), contabilizzazione calore, gruppi elettrogeni, strumentazione.
- **Vantaggi:** Semplicità assoluta; supportato da qualunque dispositivo industriale; gratuito.
- **Limiti e attenzioni:** Nessuna sicurezza nativa; nessun modello dati condiviso (vendor-specific).
- **Costi ed economia:** Integrazione: quasi gratuita; gateway Modbus-KNX/BACnet: 150-800 €.
- **Caso tipico:** Qualunque inverter FV, qualunque contatore di energia.
- **Normativa:** Nessuna certificazione formale; IEC 61158 come famiglia fieldbus.
- **Nota di cantiere:** Mai esporre Modbus su Internet aperto: tunnel VPN o gateway con autenticazione.

### Termoregolazione intelligente

**Categoria:** Clima smart · **Corso:** Domotica e building automation

Controllo climatizzazione per zone con presenza, finestre aperte, apprendimento orari.

- **Tecnologia e criteri:** Valvole termostatiche elettroniche (zigbee/Matter/KNX), sonde ambiente, logiche anti-spreco (finestra aperta = stop).
- **Applicazioni:** Riscaldamento e raffrescamento residenziale e terziario.
- **Vantaggi:** Risparmio 10-25% su clima; comfort zonale reale; integrazione con calendario.
- **Limiti e attenzioni:** Impianti idronici mal bilanciati vanificano i controlli.
- **Costi ed economia:** Valvola smart: 40-100 €; centrale zone: 200-800 €.
- **Caso tipico:** Netatmo, Tado, Honeywell (Matter/Cloud); KNX (locale).
- **Normativa:** UNI EN 215 valvole; direttiva EED per contabilizzazione.
- **Nota di cantiere:** La regola d'oro: regolare PRIMA l'impianto idraulico (bilanciamento), POI i termostati smart.

### Sicurezza informatica dell'edificio smart

**Categoria:** Cybersecurity · **Corso:** Domotica e building automation

Proteggere l'edificio connesso: reti, dispositivi, cloud, accessi remoti.

- **Tecnologia e criteri:** VLAN dedicate IoT, VPN, aggiornamenti firmware, password uniche, zero-trust, IEC 62443.
- **Applicazioni:** Ogni edificio connesso: da casa a grattacielo.
- **Vantaggi:** L'edificio è ora un sistema informatico: rischio ransomware arriva anche dal termostato.
- **Limiti e attenzioni:** Complessità per l'installatore tradizionale; dispositivi cinesi senza aggiornamenti.
- **Costi ed economia:** Hardering base: 0-500 €; progetto sicurezza: 1-5k€.
- **Caso tipico:** Firewall UniFi/pfSense; piattaforme certificate KNX Secure, BACnet/SC.
- **Normativa:** IEC 62443; GDPR per dati personali; NIS2 per enti/gestori infrastrutture.
- **Nota di cantiere:** Prima regola: cambiare TUTTE le password di default. Seconda: rete ospiti separata. Terza: aggiornamenti trimestrali calendarizzati.

### Gestione energetica e load control

**Categoria:** Energia · **Corso:** Domotica e building automation

Monitorare e gestire i carichi elettrici: produzione FV, consumi, priorità, wallbox.

- **Tecnologia e criteri:** Contatori smart, sensori corrente, relè di priorità, logiche di load shedding, integrazione inverter.
- **Applicazioni:** Ville con FV+auto elettrica+induzione+pompa di calore: il caso limite di carico.
- **Vantaggi:** Zero distacchi enel; uso massimo dell'autoconsumo FV; bolletta sotto controllo.
- **Limiti e attenzioni:** Sistemi chiusi cloud-to-cloud poco affidabili; serve standard (Modbus!).
- **Costi ed economia:** Kit monitoraggio: 200-600 €; energy manager integrato: 1-3k€.
- **Caso tipico:** Shelly EM, Fronius Solar.web, SolarEdge, open source Home Assistant + Modbus.
- **Normativa:** CEI 0-16 per allacciamenti; UNI CEI 11339 energy management.
- **Nota di cantiere:** Con pompa di calore + wallbox + induzione serve quasi sempre un gestore di carichi: il contatore da 6 kW ringrazia.

### Domotica + fotovoltaico e accumulo

**Categoria:** FV integrato · **Corso:** Domotica e building automation

L'impianto domotico come cervello del sistema energetico: consumi, produzione, accumulo, EV.

- **Tecnologia e criteri:** Lettura inverter via Modbus, gestione batteria, logica 'carica la batteria, poi la macchina, poi scalda l'acqua'.
- **Applicazioni:** Abitazioni efficienti, B&B, piccoli condomini.
- **Vantaggi:** Autoconsumo >70% possibile con logiche di carico; rendimento della batteria monitorato.
- **Limiti e attenzioni:** API cloud soggette a cambi; dipendenza marca inverter.
- **Costi ed economia:** Integrazione software: 0-1k€; hardware aggiuntivo minimo.
- **Caso tipico:** Home Assistant Energy, Fronius, Victron (flessibili), Sonnen.
- **Normativa:** CEI 0-21; UNI 9174 impianti generazione.
- **Nota di cantiere:** La scalda-acqua con resistenza 'fotovoltaica' (SG Ready) è il primo upgrade economico: 300 € di relè, +15% autoconsumo.

### Gateway e integrazione multprotocollo

**Categoria:** Gateway · **Corso:** Domotica e building automation

Come far parlare insieme KNX, BACnet, Modbus, Zigbee, Matter, cloud.

- **Tecnologia e criteri:** Gateway hardware (es. home server, edge gateway) + software (Niagara, Home Assistant, Node-RED).
- **Applicazioni:** Qualsiasi edificio con sottosistemi eterogenei (tipico: BMS + domotica + FV + sicurezza).
- **Vantaggi:** Un unico cruscotto; logiche condivise; dati unificati per energia e manutenzione.
- **Limiti e attenzioni:** Punto critico: se il gateway cade, l'integrazione cade; ridondanza e manutenzione.
- **Costi ed economia:** Gateway edge: 300-3.000 €; licenze software: 0-5k€/anno.
- **Caso tipico:** Home Assistant (open source), Tridum Niagara (professionale), Node-RED (prototipi).
- **Normativa:** Nessuna specifica; IEC 62443 per la sicurezza.
- **Nota di cantiere:** Regola: il gateway deve 'spegnere bene' — in assenza di cloud e gateway, luce e tapparelle devono funzionare comunque.

### Gestione illuminazione avanzata

**Categoria:** Illuminazione smart · **Corso:** Domotica e building automation

Controllo luci: accensioni sceniche, dimmer, presenza, luce naturale integrata (daylight harvesting).

- **Tecnologia e criteri:** Dimmer LED compatibili, sensori lux+PIR, logica circadiana (HCL - Human Centric Lighting).
- **Applicazioni:** Uffici, scuole, hotel, abitazioni: comfort visivo e risparmio energetico.
- **Vantaggi:** Risparmio 30-60% su illuminazione; benessere visivo documentato (HCL).
- **Limiti e attenzioni:** Qualità dimmer: flicker e compatibilità lampade da testare.
- **Costi ed economia:** Dimmer KNX: 100-250 €/canale; sensori: 50-150 €.
- **Caso tipico:** Standard DALI-2 per il controllo lampade professionali.
- **Normativa:** EN 12464-1 illuminazione luoghi di lavoro.
- **Nota di cantiere:** Il daylight harvesting in ufficio ripaga in 2-4 anni: sensori + logica che abbassano l'artificiale quando entra il sole.

### Irrigazione smart

**Categoria:** Irrigazione · **Corso:** Domotica e building automation

Irrigazione giardini e giardini pensili guidata da meteo e umidità del suolo.

- **Tecnologia e criteri:** Valvole elettroniche, sensori umidità, gateway meteo, logica ET (evapotraspirazione).
- **Applicazioni:** Ville, condomini, hotel, aziende agrituristiche, cantieri con verde.
- **Vantaggi:** Risparmio acqua 30-50%; prato sano senza pensieri.
- **Limiti e attenzioni:** Sensori di suolo da calibrare; congelamento valvole in inverno.
- **Costi ed economia:** Kit zona: 100-300 €; sistema completo giardino: 500-2k€.
- **Caso tipico:** Rachio, Hunter Hydrawise, Orbit B-hyve.
- **Normativa:** Risparmio idrico raccomandato D.Lgs 152/06.
- **Nota di cantiere:** Con green roof e giardini pensili (sempre più richiesti in edilizia), l'irrigazione smart passa da optional a progetto.

### Normativa e costi dell'impianto domotico

**Categoria:** Normativa e costi · **Corso:** Domotica e building automation

Il quadro normativo e economico completo per progettare e preventivare.

- **Tecnologia e criteri:** L.46/90: criteri CEN per qualifica impianti; marcatura CE; CEI 64-8; contratto di manutenzione.
- **Applicazioni:** Preventivi, direzione lavori, formazione cliente.
- **Vantaggi:** Chiarezza contrattuale; qualifica dell'installatore; valore immobiliare aumentato (5-15% percepito).
- **Limiti e attenzioni:** Mancanza di standard sui prezzi: preventivi eterogenei.
- **Costi ed economia:** Prezzi 2025: punto luce domotico 60-150 €; attuatore 80-250 €; quadro completo appartamento 3-10k€; villa 15-50k€.
- **Caso tipico:** Tabelle prezzi installatori KNX/Mater.
- **Normativa:** L.46/90; CEI 64-8; contratti tipo ANIT/Confartigianato.
- **Nota di cantiere:** Il vero costo della domotica non è l'hardware: è il progetto e la programmazione (30-50% del totale). Chi risparmia lì compra un impianto che non funziona.

### Cablaggio e quadri dell'impianto domotico

**Categoria:** Progettazione · **Corso:** Domotica e building automation

Come si progetta fisicamente: canaline, quadretti, centralini, automazioni elettriche conformi.

- **Tecnologia e criteri:** Norma CEI 64-8; centralino domotico con attuatori per piano; cablaggio bus separato dai 230V o schermato.
- **Applicazioni:** Impianti nuovi e ristrutturazioni radicali.
- **Vantaggi:** Manutenibilità: ogni attuatore etichettato e mappato; crescita futura garantita.
- **Limiti e attenzioni:** Errori classici: bus accoppiato a 230V, centralini saturi, zero documentazione.
- **Costi ed economia:** Costo cablaggio domotico: +20-40% sull'impianto elettrico tradizionale.
- **Caso tipico:** Best practice KNX Association, guide CEI.
- **Normativa:** CEI 64-8 (impianti utilizzatori a tensione <=1000V); DM 37/08.
- **Nota di cantiere:** Consegnare SEMPRE il progetto ETS/documentazione: un impianto domotico senza documentazione è un'arma puntata contro il futuro proprietario.

### DALI (Digital Addressable Lighting Interface)

**Categoria:** Protocollo luce · **Corso:** Domotica e building automation

Protocollo digitale dedicato al controllo dell'illuminazione professionale.

- **Tecnologia e criteri:** Bus a 2 fili fino a 64 driver/indirizzo; DALI-2 aggiunte sensori e emergency; DT6/DT8 per LED color/tunable white.
- **Applicazioni:** Uffici, retail, musei, ospedali: ogni punto luce indirizzabile.
- **Vantaggi:** Controllo fine di ogni lampada; retrofit facile (bus sui fili delle fasi); emergency test integrato.
- **Limiti e attenzioni:** Richiede progettazione indirizzi; integrazione con BMS via gateway.
- **Costi ed economia:** Driver DALI: +5-15 €/punto; gateway DALI-BACnet: 400-1.500 €.
- **Caso tipico:** Qualunque produttore illuminotecnico professionale.
- **Normativa:** IEC 62386 (DALI-2); EN 62386.
- **Nota di cantiere:** DALI dentro, BACnet fuori: la coppia standard dell'edificio terziario moderno.

### Scenari, logiche e sequenze

**Categoria:** Scenari · **Corso:** Domotica e building automation

La programmazione comportamentale: 'cinema', 'benvenuto', 'notte', 'emergenza'.

- **Tecnologia e criteri:** Logiche AND/OR temporizzate; scene memorizzate nei dispositivi o nel supervisore.
- **Applicazioni:** Residenze luxury, hotel (scene benvenuto), uffici (scene riunione/presentazione).
- **Vantaggi:** Trasforma la tecnologia in esperienza; il valore percepito aumenta 10x.
- **Limiti e attenzioni:** Logiche troppo complesse confondono l'utente: regola '3 tap massimo'.
- **Costi ed economia:** Programmazione: parte dei costi d'installazione (10-20%).
- **Caso tipico:** Scene KNX standard, scene Philips Hue/Apple Home.
- **Normativa:** Nessuna; best practice progettuali.
- **Nota di cantiere:** Una scena si giudica da quanto è ovvia: se serve il manuale d'uso, è sbagliata.

### Sensoristica domotica

**Categoria:** Sensori · **Corso:** Domotica e building automation

Gli occhi dell'impianto: presenza, movimento, luce, temperatura, umidità, CO2, qualità aria.

- **Tecnologia e criteri:** PIR, mm-wave (radar 60 GHz), luxmetri, sonde NTC, NDIR per CO2, eCO2/VOC.
- **Applicazioni:** Controllo illuminazione, clima, sicurezza, VMC, scenari anti-allagamento/gas.
- **Vantaggi:** mm-wave rileva presenza anche ferma (uffici, anziani); CO2 guida la VMC con dati reali.
- **Limiti e attenzioni:** Falsi positivi PIR in ambienti con animali; taratura iniziale lunga.
- **Costi ed economia:** Sensore PIR: 10-50 €; mm-wave: 30-80 €; CO2 NDIR: 60-150 €.
- **Caso tipico:** Dispositivi KNX/Aqara/Shelly per ogni fascia.
- **Normativa:** Marcatura CE; CEI EN per compatibilità elettromagnetica.
- **Nota di cantiere:** I sensori sono il 30% del comfort e l'80% dei malfunzionamenti percepiti: investire in qualità e taratura.

### Antintrusione integrata

**Categoria:** Sicurezza · **Corso:** Domotica e building automation

Impianto di sicurezza con sensori volumetrici, perimetrali, centrali, integrato alla domotica.

- **Tecnologia e criteri:** Doppia tecnologia IR+microonde, contatti magnetici, vibrazione, centrali con bus (es. Bentel, Tyco).
- **Applicazioni:** Ville, uffici, negozi, magazzini.
- **Vantaggi:** Integrazione: l'allarme attiva scene (accendi luce, alza tapparelle, invia notifica).
- **Limiti e attenzioni:** Standard antintrusione rigidi sul cablaggio (tamper); integrazione domotica da certificare.
- **Costi ed economia:** Impianto appartamento: 800-2.500 €; villa: 2-8k€.
- **Caso tipico:** Bentel, Ajax (wireless), Satel, DSC.
- **Normativa:** CEI 79-2/3/4; VDE 0833 per componentistica bus.
- **Nota di cantiere:** La domotica NON sostituisce l'impianto certificato: convivono, con l'antintrusione che manda stati alla domotica.

### Qualità dell'aria e CO2-driven ventilation

**Categoria:** VMC integrata · **Corso:** Domotica e building automation

La domotica comanda la VMC in base a CO2, umidità e presenza: aria pulita con minimo consumo.

- **Tecnologia e criteri:** Sensori CO2/UMidità nei locali; comando centralina VMC (velocità, bypass, umidità).
- **Applicazioni:** Case passive, uffici, scuole, camere hotel.
- **Vantaggi:** Comfort e salute documentati (concentrazione, sonno); consumi della VCA ottimizzati (-30%).
- **Limiti e attenzioni:** Centraline VMC 'chiuse' senza interfaccia: scegliere modelli con ingresso 0-10V/Modbus.
- **Costi ed economia:** Centralina VMC smart-ready: +200-500 € rispetto a standard.
- **Caso tipico:** Zehnder, Mitsubishi Lossnay, Vortice con controlli esterni.
- **Normativa:** UNI EN 13779 classificazione aria; UNI/TS 11300 per calcoli.
- **Nota di cantiere:** Sopra i 1.000 ppm di CO2 le prestazioni cognitive calano: sensori CO2 in ufficio sono salute, non gadget.

### Videosorveglianza e privacy

**Categoria:** Videocamere · **Corso:** Domotica e building automation

Telecamere IP per sicurezza, con vincoli GDPR per aree comuni e lavoro.

- **Tecnologia e criteri:** IP cam PoE, NVR/VMS, analitiche AI (rilevamento persone, veicoli, LPR).
- **Applicazioni:** Cantieri, condomini, aziende, showroom.
- **Vantaggi:** Deterrenza documentata; analitiche riducono falsi allarmi 90%.
- **Limiti e attenzioni:** GDPR: DPIA obbligatoria, tempi conservazione, divieto aree sensibili (uffici, spogliatoi).
- **Costi ed economia:** Cam IP: 80-400 €; NVR 8ch: 300-800 €; progetto: 50-300 €/punto installato.
- **Caso tipico:** Hikvision, Dahua, Axis (top), Ubiquiti (semplice).
- **Normativa:** GDPR; Legge 76/2013 sicurezza urbana (flussi verso PS); norma videosorveglianza lavoro.
- **Nota di cantiere:** La telecamera si posiziona sulla PROPRIETA', mai sullo spazio pubblico: 1 metro può costare una sanzione.

### Bluetooth Mesh (illuminazione)

**Categoria:** Wireless · **Corso:** Domotica e building automation

Rete mesh Bluetooth per illuminazione smart professionale.

- **Tecnologia e criteri:** Bluetooth Mesh su 2,4 GHz; modelli publish/subscribe; provisioning via app.
- **Applicazioni:** Uffici, retail, hotel: illuminazione + localizzazione indoor (asset tracking).
- **Vantaggi:** Una sola rete per luce e localizzazione dei badge/carrelli; installazione semplice.
- **Limiti e attenzioni:** Ecosistema in crescita ma inferiore a KNX/DALI; distanza hop limitata.
- **Costi ed economia:** Componenti: 15-80 €/punto luce.
- **Caso tipico:** Signify Interact, Silicon Labs reference designs.
- **Normativa:** Bluetooth SIG Mesh specifications.
- **Nota di cantiere:** La killer feature è il posizionamento indoor: retail e ospedali lo adottano per questo.

### Matter e Thread

**Categoria:** Wireless · **Corso:** Domotica e building automation

Lo standard unificato 2022+ per la smart home: interoperabilità tra Google, Apple, Amazon, Samsung.

- **Tecnologia e criteri:** Matter (applicativo) su Thread (rete mesh IP a basso consumo) o Wi-Fi.
- **Applicazioni:** Nuovi impianti e aggiornamenti smart home: un solo ecosistema per ogni dispositivo.
- **Vantaggi:** FINALMENTE: un dispositivo Matter funziona con tutti gli assistenti; commissioning semplice.
- **Limiti e attenzioni:** Dispositivi ancora non esaustivi; certificazione in corso per molte categorie.
- **Costi ed economia:** Dispositivi Matter: 15-100 €; border router integrato in altoparlanti/hub esistenti.
- **Caso tipico:** Google Nest, Apple HomeKit, Amazon Echo, SmartThings convergenti su Matter.
- **Normativa:** Standard CSA (Connectivity Standards Alliance).
- **Nota di cantiere:** Per nuovi impianti residenziali: preferire dispositivi Matter-certified per non restare imprigionati in un ecosistema.

### Wi-Fi domotico

**Categoria:** Wireless · **Corso:** Domotica e building automation

Dispositivi smart direttamente sulla rete Wi-Fi dell'edificio.

- **Tecnologia e criteri:** Wi-Fi 2,4/5/6 GHz; cloud del produttore; app dedicata.
- **Applicazioni:** Piccoli impianti, singoli ambienti, B&B, retrofit leggero.
- **Vantaggi:** Nessun hub aggiuntivo; prezzo basso; app immediata.
- **Limiti e attenzioni:** Consumo elevato (batterie durano poco); congestione rete; dipendenza dal cloud esterno.
- **Costi ed economia:** Dispositivo: 10-50 €.
- **Caso tipico:** Sonoff, Shelly, Tuya/Smart Life (migliaia di prodotti).
- **Normativa:** CEI 64-8 per l'impianto elettrico.
- **Nota di cantiere:** Il cloud esterno è un rischio continuità: se il produttore chiude, i dispositivi muoiono. Preferire dispositivi con API locali.

### Z-Wave

**Categoria:** Wireless · **Corso:** Domotica e building automation

Protocollo radio sub-GHz per domotica residenziale (mesh).

- **Tecnologia e criteri:** 863-870 MHz (Europa); mesh fino a 4 hop; bassa potenza.
- **Applicazioni:** Sicurezza, sensori, attuatori in contesti residenziali.
- **Vantaggi:** Banda libera da congestione Wi-Fi; segnale che attraversa pareti meglio del 2,4 GHz.
- **Limiti e attenzioni:** Ecosistema più piccolo di Zigbee; hub dedicato.
- **Costi ed economia:** Dispositivo: 20-80 €; hub: 100-250 €.
- **Caso tipico:** Fibaro, Aeotec, Somfy (parzialmente).
- **Normativa:** Z-Wave Alliance; certificazione obbligatoria.
- **Nota di cantiere:** In edilizia europea ha perso terreno verso Zigbee e Matter, ma resta solido in sicurezza.

### Zigbee

**Categoria:** Wireless · **Corso:** Domotica e building automation

Mesh radio a basso consumo per sensori e attuatori domotici.

- **Tecnologia e criteri:** IEEE 802.15.4, 2,4 GHz, mesh auto-riparante, profili applicativi (ZHA, ZLL).
- **Applicazioni:** Sensori ambiente, prese smart, illuminazione, chiavi intelligenti.
- **Vantaggi:** Bassissimo consumo (batterie anni); mesh estendibile; dispositivi economici.
- **Limiti e attenzioni:** Interferenze Wi-Fi sulla stessa banda; qualità variabile tra marche.
- **Costi ed economia:** Dispositivo: 10-60 €; hub: 50-150 €.
- **Caso tipico:** Philips Hue, IKEA Tradfri, Samsung SmartThings, Aqara.
- **Normativa:** Zigbee Alliance -> Connectivity Standards Alliance.
- **Nota di cantiere:** Per un LLM: Zigbee è perfetto per il RETROFIT senza demolizioni: vale l'oro in ristrutturazioni.


## Formulario di fisica dell'edilizia e degli impianti

*Corso `FORMULARIO_FISICA_IMPIANTI_PACK` — 13 voci*

### L'acustica in formule: riverbero, isolamento, assorbimento

**Categoria:** Acustica formule · **Corso:** Formulario di fisica dell'edilizia e degli impianti

Le formule del suono negli edifici: il comfort che si misura.

- **Tecnologia e criteri:** Tempo di riverbero di Sabine: T = 0,161·V/A (A = ΣS·α); il criterio di Ottavo? no: 'valutazione': T ottimale uffici 0,6-0,8 s, ristoranti 0,8-1,2 s, chiese 2-3 s; isolamento: R = L1 − L2 + 10·log(S/A); rumore = 10·log(Σ10^(Li/10)).
- **Applicazioni:** Progetto acustico, risarcimenti da rumore, ristrutturazioni.
- **Vantaggi:** La formula di Sabine (1898!) è ancora lo strumento n.1: una stanza si descrive con un numero.
- **Limiti e attenzioni:** Le formule valgono per campi diffusi: le prime riflessioni e il parlato ravvicinato richiedono modelli più fini.
- **Costi ed economia:** Le tabelle di assorbimento α dei materiali sono pubbliche.
- **Caso tipico:** Studio 60 m³, A=12 m² sa → T=0,161·60/12 = 0,8 s (perfetto per riunioni).
- **Normativa:** UNI EN ISO 3382; UNI 11367.
- **Nota di cantiere:** Il trucco rapido: contare i 'metri quadri equivalenti di assorbimento' di una stanza (tappeto, tende, persone) dà la stima di T in 2 minuti.

### La condensazione e il vapore: quando l'acqua si nasconde nella parete

**Categoria:** Condensazione · **Corso:** Formulario di fisica dell'edilizia e degli impianti

Il vapore acqueo che attraversa la parete e diventa acqua: la fisica della muffa.

- **Tecnologia e criteri:** Pressione di vapore saturo (tabella); flusso di vapore g = δ·Δp/s; metodo di Glaser (analisi grafica degli strati); regola dello strato di tenuta (lato caldo) lasciando traspirare lato freddo; punto di rugiada.
- **Applicazioni:** Diagnosi muffa, progettazione stratigrafie, involucri in legno.
- **Vantaggi:** La muffa è quasi sempre condensazione interstiziale o superficiale: la fisica la spiega e la cura.
- **Limiti e attenzioni:** La realtà è 2D e 3D (ponti termici): il metodo di Glaser è 1D.
- **Costi ed economia:** Le tabelle del vapore saturo sono pubbliche.
- **Caso tipico:** Interno 20°C/55% UR → p=1280 Pa; parete con barriera insufficiente: condensa nel lana? no: 'nella lana' in inverno.
- **Normativa:** UNI EN ISO 13788 (metodo Glaser).
- **Nota di cantiere:** La muffa in basso a destra della camera nord: non è sfortuna, è fisica. Il progettista che non fa il Glaser scarica la muffa sul cliente.

### Le formule economiche: interesse, ammortamento, valore attuale

**Categoria:** Costruzione calcoli · **Corso:** Formulario di fisica dell'edilizia e degli impianti

La matematica del denaro nell'edilizia: investimenti, mutui, valori.

- **Tecnologia e criteri:** Interesse semplice I = C·r·t; interesse composto M = C·(1+r)^t; rata mutuo R = C·r/(1−(1+r)^−n); ammortamento annuo = costo/vita utile; valore attuale VA = F/(1+r)^t; TCO = costo iniziale + Σ costi esercizio (attualizzati).
- **Applicazioni:** Mutui, valutazioni investimenti immobiliari, confronto tecnologie, leasing.
- **Vantaggi:** Il TCO (costo totale di proprietà) svela la verità: la caldaia 'economica' costa più della PDC in 10 anni.
- **Limiti e attenzioni:** I tassi reali includono inflazione e rischio: le formule semplici sono la base, il giudizio fa il resto.
- **Costi ed economia:** Le formule sono gratuite: foglio di calcolo basta.
- **Caso tipico:** Mutuo 100k€, 3%, 20 anni: rata = 100.000·0,0025/(1−1,0025^−240) ≈ 555 €/mese.
- **Normativa:** Nessuna norma: matematica finanziaria.
- **Nota di cantiere:** L'edilizia moderna si giudica sul TCO a 20 anni, non sul prezzo iniziale. Chi vende solo il prezzo sta nascondendo qualcosa.

### L'impianto elettrico in formule: potenza, corrente, caduta di tensione

**Categoria:** Elettrica formule · **Corso:** Formulario di fisica dell'edilizia e degli impianti

Le formule elettriche del cantiere e dello studio.

- **Tecnologia e criteri:** Potenza monofase P = V·I·cosφ (230 V); trifase P = √3·V·I·cosφ (400 V); corrente I = P/(V·cosφ); caduta di tensione ΔV% = (√3·I·L·(R cosφ + X sinφ))/V ·100 (max 4%); la protezione: I_n ≥ I_b e I_2 ≤ 1,45·I_z; messa a terra: U_L ≤ 50 V.
- **Applicazioni:** Dimensionamento linee, verifica quadri, scelta protezioni, diagnostica guasti.
- **Vantaggi:** P=V·I basta per non bruciare un impianto: chi la ignora sottodimensiona i cavi.
- **Limiti e attenzioni:** Le formule sono a regime: i picchi di avviamento (motori) richiedono sovradimensionamento coordinato.
- **Costi ed economia:** Le tabelle sezione-corrente sono nella CEI 64-8 (pubblica).
- **Caso tipico:** Forno 3 kW a 230 V: I = 3000/230 = 13 A → linea 2,5 mm² con magnetotermico 16 A.
- **Normativa:** CEI 64-8; IEC 60364.
- **Nota di cantiere:** Il test del professionista: chiedere sempre la corrente di impiego prima di parlare di sezioni. Il cavo si sceglie dalla corrente, non dal colore o dall'abitudine.

### Il fabbisogno energetico rapido: kWh/m²·anno in formule

**Categoria:** Fabbisogno energetico · **Corso:** Formulario di fisica dell'edilizia e degli impianti

Stimare la bolletta prima di progettare: le formule del conto termico quotidiano.

- **Tecnologia e criteri:** Dispersione trasmissione Q = U·A·ΔT·t; ventilazione Q_v = 0,34·V·n·ΔT·t (n = ricambi/h); apporti solari = g·A·E; bilancio annuo = dispersioni − apporti; classe energetica da E_ph (kWh/m²·anno).
- **Applicazioni:** Legge 10, bollette, scelta impianti, confronto soluzioni.
- **Vantaggi:** Il calcolo rapido del bilancio decide l'investimento energetico in 30 minuti.
- **Limiti e attenzioni:** Il calcolo semplificato non sostituisce la certificazione energetica ufficiale.
- **Costi ed economia:** I valori U e i gradi-giorno sono pubblici (Enea).
- **Caso tipico:** Appartamento 100 m², U medio 0,9, ΔT=20°C, 180 gg riscaldamento: Q_trasm ≈ 0,9·220·20·4320/1000 ≈ 17.100 kWh/anno.
- **Normativa:** UNI/TS 11300; gradi-giorno ENEA.
- **Nota di cantiere:** La formula più utile del settore: Q = 0,024·GG·(UA + 0,34·V·n) con GG = gradi-giorno. Chi la usa stima la bolletta di qualsiasi edificio in 10 minuti.

### Il fotovoltaico in formule: produzione, inclinazione, ombreggiamento

**Categoria:** Fotovoltaico formule · **Corso:** Formulario di fisica dell'edilizia e degli impianti

Quanta energia produce un pannello: le formule della resa solare.

- **Tecnologia e criteri:** Produzione E = P_inst × HSP × PR (HSP = ore di sole di picco, 3-5 in Italia; PR = performance ratio 0,75-0,85); perdita da orientamento: sud 100%, est/ovest 85-90%, nord 60-70%; perdita da inclinazione: ottimale = latitudine (45° in Italia); perdita da ombra: un 10% di ombra = −30% di resa (stringhe in serie).
- **Applicazioni:** Preventivi FV, verifica installatori, scelta della potenza.
- **Vantaggi:** E = P×HSP×PR stima la produzione annua di qualsiasi tetto in 2 minuti.
- **Limiti e attenzioni:** I valori locali (HSP) variano: servono le mappe ENEA/PVGIS.
- **Costi ed economia:** Il simulatore PVGIS (gratuito, Enea) dà i dati locali precisi.
- **Caso tipico:** 6 kWp a Roma (HSP 3,6, PR 0,8): E ≈ 6·3,6·0,8·365 ≈ 6.300 kWh/anno.
- **Normativa:** Nessuna norma: fisica solare.
- **Nota di cantiere:** La verità del FV: il peggior nemico è l'ombra parziale, non il cattivo orientamento. Un camino che ombreggia mezzo pannello può distruggere il 25% della produzione: l'ispezione prima della firma del contratto è obbligatoria.

### L'idraulica degli impianti in formule: portata, perdite, pressione

**Categoria:** Idraulica formule · **Corso:** Formulario di fisica dell'edilizia e degli impianti

Le formule del fluire dell'acqua negli edifici: pressione, portata, perdite di carico.

- **Tecnologia e criteri:** Portata Q = v·A (l/s); perdite distribuite J = λ·(v²/2g)·(1/D); perdite localizzate ζ·v²/2g; pressione residua al punto: p = p₀ − ΣJ (minimo 0,5 bar agli apparecchi); velocità guida: 1-2 m/s (adduzione), 0,6-1,5 m/s (interne).
- **Applicazioni:** Dimensionamento tubazioni, verifica pressioni, diagnosi di impianti deboli.
- **Vantaggi:** Le perdite di carico spiegano il 90% dei problemi: 'l'acqua non arriva' = le perdite superano la pressione.
- **Limiti e attenzioni:** I calcoli sono per regime permanente: i transitori richiedono studi dedicati.
- **Costi ed economia:** Le formule in UNI EN 806 e nei manuali.
- **Caso tipico:** Doccia al 3° piano con p=0,8 bar: ok (min 0,5); con p=0,3 bar: insufficiente → servono perdite ridotte o pressurizzazione.
- **Normativa:** UNI EN 806; UNI EN 1717.
- **Nota di cantiere:** La regola del pollice: a parità di portata, raddoppiare il diametro riduce le perdite di 30 volte (J ∝ 1/D⁵ approssimato). Il diametro corretto è il miglior investimento invisibile dell'impianto.

### L'illuminotecnica in formule: lux, lumen, resa

**Categoria:** Illuminotecnica · **Corso:** Formulario di fisica dell'edilizia e degli impianti

La luce misurata: come si progetta l'illuminazione senza tentativi.

- **Tecnologia e criteri:** Flusso luminoso Φ (lumen); illuminamento E = Φ/S (lux); i livelli guida (ufficio 500 lux scrivania, corridoio 100, officina 300); il metodo del flusso: Φ_tot = E·S/(η·fu); resa cromatica IRC>80 (90 per musei/retail moda); abbagliamento UGR<19 uffici.
- **Applicazioni:** Progetto luci, verifiche lux in cantiere, scelta apparecchi.
- **Vantaggi:** E = Φ/S: con una calcolatrice si verifica se una stanza è ben illuminata PRIMA di montare.
- **Limiti e attenzioni:** Il metodo del flusso ignora le riflessioni complesse: la simulazione (Dialux, gratis) affina.
- **Costi ed economia:** Il software Dialux evo è gratuito.
- **Caso tipico:** Ufficio 20 m² a 500 lux: Φ = 500·20/(0,6·0,8) ≈ 20.800 lm (8-10 apparecchi da 2000 lm).
- **Normativa:** UNI EN 12464-1; UNI EN 15193.
- **Nota di cantiere:** La verifica di cantiere: il luxmetro (30 €) misura la realtà. La norma dice 500 lux sulla scrivania: misurare dopo la posa, non fidarsi del catalogo.

### La massa termica e l'inerzia: la fisica del comfort estivo

**Categoria:** Massa termica · **Corso:** Formulario di fisica dell'edilizia e degli impianti

Il peso che frena il caldo: capacità termica e fase di sfasamento.

- **Tecnologia e criteri:** Capacità termica volumica = ρ·c; sfasamento delle onde di calore (parete pesante 10-14 h, leggera 3-6 h); il decremento (riduzione ampiezza); notte ventilata su parete pesante = raffrescamento gratuito.
- **Applicazioni:** Case passive, climi mediterranei, edilizia in terra e cls.
- **Vantaggi:** L'inerzia è il condizionamento gratuito: la parete pesante carica di fresco la notte e lo restituisce il giorno.
- **Limiti e attenzioni:** L'inerzia è utile solo con escursione giorno-notte: nei climi umidi e costanti vale meno.
- **Costi ed economia:** I valori ρ·c nelle tabelle (cls 2400 kg/m³ · 1000 = 2,4 MJ/m³K).
- **Caso tipico:** Le case in tufo dell'Etna: interni freschi senza condizionatore; i palazzi storici di pietra.
- **Normativa:** UNI EN ISO 13786 (inerzia).
- **Nota di cantiere:** La regola mediterranea: 'parete pesante verso sud, isolata all'esterno, ventilata la notte': tre mosse fisiche che sostituiscono metà del condizionatore.

### La pompa di calore in formule: COP, energia, risparmio

**Categoria:** Pompe di calore formule · **Corso:** Formulario di fisica dell'edilizia e degli impianti

La macchina che moltiplica l'energia: come si calcola il vantaggio reale.

- **Tecnologia e criteri:** COP = energia termica prodotta / energia elettrica assorbita (3-5 aria-acqua a 35°C mandata); energia annua = fabbisogno termico / COP; il SCOP stagionale tiene conto del clima; risparmio vs caldaia gas = 1 − (costo elettrico/COP)/(costo gas/0,9); integrazione a −10°C: resistenza o ibrido.
- **Applicazioni:** Scelta PDC, verifica preventivi, confronto con caldaia.
- **Vantaggi:** Il COP trasforma il dibattito 'elettrico vs gas' in un calcolo di 3 righe.
- **Limiti e attenzioni:** Il COP crolla con le temperature esterne basse e le mandate alte: il dato di targa è ottimistico.
- **Costi ed economia:** I dati climatici ENEA e i cataloghi (COP a condizioni note).
- **Caso tipico:** Fabbisogno 12.000 kWh/anno, COP 3,5: energia elettrica = 3.430 kWh/anno ≈ 1.000 € a 0,30 €/kWh vs 1.350 € di gas: risparmio ~25-30%.
- **Normativa:** UNI EN 14825; UNI/TS 11300.
- **Nota di cantiere:** La regola della PDC: 'la PDC ama le mandate basse': chi ha radianti (35°C) ha COP 4; chi ha termosifoni vecchi (70°C) ha COP 2,5. Il risparmio si decide a monte, con l'impianto di emissione.

### Le pompe in formule: prevalenza, portata, potenza

**Categoria:** Prevalenza pompe · **Corso:** Formulario di fisica dell'edilizia e degli impianti

Come si sceglie una pompa: la fisica del sollevamento dell'acqua.

- **Tecnologia e criteri:** Prevalenza H = H_geo + H_perdite + H_residua; potenza assorbita P = ρ·g·Q·H/η (η = 0,4-0,8); punto di lavoro = intersezione curva pompa/rete; NPSH disponibile vs richiesto (cavitazione).
- **Applicazioni:** Circolatori di riscaldamento, pompe di sollevamento, idranti, irrigazione.
- **Vantaggi:** La prevalenza corretta evita pompe sottodimensionate (che non arrivano) o sovradimensionate (che consumano e roncano).
- **Limiti e attenzioni:** Le curve pompa/rete si intersecano: il punto reale di lavoro va verificato, non assunto.
- **Costi ed economia:** Le formule nei manuali di macchine idrauliche.
- **Caso tipico:** Sollevamento 10 m, portata 2 l/s, η=0,6: P = 1000·9,81·0,002·10/0,6 ≈ 327 W (un circolatore da 370 W basta).
- **Normativa:** Nessuna norma: teoria delle macchine.
- **Nota di cantiere:** La regola della pompa: la curva della rete (perdite) sale con il quadrato della portata: chiudere una valvola aumenta la prevalenza a disposizione. L'equilibrio tra pompa e rete è la fisica quotidiana del circolatore.

### La termofisica dell'involucro: conduzione e trasmittanza

**Categoria:** Termofisica base · **Corso:** Formulario di fisica dell'edilizia e degli impianti

Come passa il calore attraverso la parete: la formula che decide l'efficienza energetica.

- **Tecnologia e criteri:** Flusso termico Φ = λ·S·ΔT/s; resistenza termica R = s/λ; trasmittanza U = 1/(ΣR + R_si + R_se); valori guida: cappotto 10 cm (λ=0,035) → R=2,9 m²K/W; parete attuale U≤0,26 W/m²K (clima E).
- **Applicazioni:** Cappotti, verifiche energetiche, leggi 10, certificazione energetica.
- **Vantaggi:** Uguale a: il valore U è il 'voto' della parete: chi lo calcola controlla la qualità dell'edilizia.
- **Limiti e attenzioni:** Le prestazioni reali degradano (umidità, ponti termici): il valore di targa non è eterno.
- **Costi ed economia:** I valori λ dei materiali nelle tabelle UNI (pubbliche).
- **Caso tipico:** Parete: intonaco 0,02/0,7 + cls 0,20/2,3 + cappotto 0,10/0,035 + intonaco 0,02/0,7 → R=3,24 → U=0,30 W/m²K.
- **Normativa:** UNI EN ISO 6946; UNI/TS 11300.
- **Nota di cantiere:** Il ponte termico tipico del 15-20% di perdita: verificare correnti d'aria e cerniere? no: 'sommando U·A si deve aggiungere il 15% per ponti termici': regola rapida del Legge 10.

### La ventilazione in formule: portate, ricambi e CO2

**Categoria:** VMC calcoli · **Corso:** Formulario di fisica dell'edilizia e degli impianti

Quanta aria serve davvero: il calcolo della VMC e del comfort degli interni.

- **Tecnologia e criteri:** Portata per persona: 25-30 m³/h (residenze), 36 m³/h (uffici); ricambi minimi (cucina 20-40, bagno 15-25 ricambi/h); portata di progetto Q = n·V; bilancio CO2: produzione 20 l/h persona → concentrazione = produzione/portata; rendimento scambiatore 80-92%.
- **Applicazioni:** Progetto VMC, verifica qualità aria, scelta centraline.
- **Vantaggi:** Il calcolo della portata decide il dimensionamento della VMC: la salute si calcola, non si promette.
- **Limiti e attenzioni:** I ricambi minimi di legge sono il minimo legale, non il comfort ottimale.
- **Costi ed economia:** Le tabelle UNI 10339 (pubbliche).
- **Caso tipico:** Camera da letto 2 persone, 30 m³/h ciascuno = 60 m³/h: una centralina da 100 m³/h copre la zona notte.
- **Normativa:** UNI 10339; UNI EN 13779.
- **Nota di cantiere:** La regola del CO2: sotto i 800 ppm la testa funziona, sopra i 1200 ppm il sonno e la concentrazione calano. Il sensore CO2 (60 €) è il termometro del comfort moderno.


## Impiantistica completa

*Corso `IMPIANTI_COMPLETA_PACK` — 34 voci*

### Evacuazione vocale e emergenza

**Categoria:** Antincendio · **Corso:** Impiantistica completa

Diffusione sonora di emergenza: messaggi chiari che guidano l'uscita.

- **Tecnologia e criteri:** Impianti EVAC (EN 50849), altoparlanti a onde guidate per stadi/aeroporti, megafoni centralizzati, collegamento centrale incendio.
- **Applicazioni:** Stadi, scuole, ospedali, centri commerciali, industrie.
- **Vantaggi:** L'evacuazione vocale dimezza i tempi di uscita rispetto alla sirena; in stadi è l'unica via praticabile.
- **Limiti e attenzioni:** Progetto specialistico; la batteria tampone va mantenuta (la causa #1 dei guasti).
- **Costi ed economia:** Impianto EVAC edificio: 5-20 €/m2; centrali grandi impianti: 10-50k€.
- **Caso tipico:** Bosch PAVIRO, Dynacord, systems integrators certificati.
- **Normativa:** EN 50849 (EVAC); EN 54-16.
- **Nota di cantiere:** L'emergenza si prova: la simulazione annuale con cronometro è l'unico modo di sapere se funziona.

### Porte tagliafuoco e compartimentazione

**Categoria:** Antincendio · **Corso:** Impiantistica completa

Barriere fisiche al fuoco: porte REI 60-120, pareti, serrande, vetri tagliafuoco.

- **Tecnologia e criteri:** Porte metalliche certificate UNI 9723, sigillanti intumescenti, serrande coibentate, vetri EI30-120.
- **Applicazioni:** Ogni edificio: corridoi, vani scale, garage interrati, laboratori.
- **Vantaggi:** Il comparto funziona SOLO se tutte le chiusure sono a norma: una porta spalancata annulla tutto.
- **Limiti e attenzioni:** Le porte tagliafuoco spesso vengono 'bloccate' per comodità; i fermi automatici costano e vengono tolti.
- **Costi ed economia:** Porta REI 60: 400-1.200 €; vetro tagliafuoco: 300-800 €/m2; verifica annuale: 10-30 €/porta.
- **Caso tipico:** Porte Dierre, Novoferm; vetri Saint-Gobain, Schott.
- **Normativa:** UNI 9723 (porte); DM 3/8/2015 (prevenzione incendi); UNI EN 13501 (classi).
- **Nota di cantiere:** Il controllo annuale delle chiusure tagliafuoco è l'obbligo più economico e più trascurato: un check di 1 giorno salva un intero edificio.

### Rilevazione incendi e analisi

**Categoria:** Antincendio · **Corso:** Impiantistica completa

Sensori che rilevano fumo, calore, fiamma, gas: il primo anello della catena di sicurezza.

- **Tecnologia e criteri:** Rivelatori ottici (fumo), termovelocimetrici, multisisma, centrali analogiche indirizzate, aspirazione per ambienti alti (ASD).
- **Applicazioni:** Uffici, hotel, ospedali, data center, magazzini, parcheggi.
- **Vantaggi:** Evacuazione precoce: la differenza tra un incidente e una tragedia; la manutenzione è normata e tracciata.
- **Limiti e attenzioni:** Falsi allarmi in cucine e parcheggi (sensori sbagliati); centraline non manutenute.
- **Costi ed economia:** Rivelatore: 30-150 €; centrale indirizzata: 800-3k€; progetto: 3-15 €/m2.
- **Caso tipico:** Esser, Bosch, NOTIFIER (Honeywell), Siemens Cerberus.
- **Normativa:** EN 54 (serie completa); DM 2/9/2021.
- **Nota di cantiere:** La rilevazione si progetta per COMPARTI e rischi (cucina, parcheggio, camera): lo stesso edificio ha sensori diversi per ambiente.

### Contabilizzazione diretta e indiretta del calore

**Categoria:** Contabilizzazione · **Corso:** Impiantistica completa

Misurare il calore consumato da ogni unità immobiliare: obbligatoria nei condomini centralizzati.

- **Tecnologia e criteri:** Contatori diretti (acqua calda primaria) o ripartitori indiretti (sulle superfici radianti) + unità centrali; lettura radio.
- **Applicazioni:** Condomini con riscaldamento centralizzato (millioni di unità in Italia).
- **Vantaggi:** Chi consuma paga: risparmi medi documentati del 15-25% post-contabilizzazione; equità tra vicini.
- **Limiti e attenzioni:** I ripartitori mal posizionati misurano male; le manutenzioni saltate rovinano tutto.
- **Costi ed economia:** Ripartitore: 30-80 €/unità; centrale: 300-800 €; contatore diretto: 150-400 €.
- **Caso tipico:** Ista, Techem, Sontex: i 'big three' europei.
- **Normativa:** UNI EN 834/835 (ripartitori/contatori); legge 10/91 art. 26 bis (obbligo).
- **Nota di cantiere:** La contabilizzazione è il provvedimento energetico italiano MIGLIORE al mondo per diffusione: un LLM edile italiano DEVE conoscerla nei dettagli.

### Dimensionamento rapido elettrico

**Categoria:** Dimensionamento · **Corso:** Impiantistica completa

Le regole pratiche per sezioni di cavo e protezioni dell'impianto elettrico.

- **Tecnologia e criteri:** Sezioni tipiche: illuminazione 1,5 mm2 con magnetotermico 10A; prese 2,5 mm2 con 16A; forno/induzione 4-6 mm2 con 20-25A; PDC/wallbox dedicata 6-10 mm2; caduta di tensione max 4% (BT).
- **Applicazioni:** Verifiche rapide in cantiere, ampliamenti, controlli.
- **Vantaggi:** Controllo immediato della coerenza cavo-protezione: il 70% dei guasti derivano da disaccordo.
- **Limiti e attenzioni:** Le regole rapide non sostituiscono il calcolo di verifica della IEC 60364.
- **Costi ed economia:** Tabella sezioni-prese standard in ogni manuale.
- **Caso tipico:** Metodo delle 'correnti di impiego' e di cortocircuito (CEI 64-8).
- **Normativa:** CEI 64-8; IEC 60364.
- **Nota di cantiere:** Regola mnemonica: 1,5 con 10, 2,5 con 16: chi non rispetta questa accoppiata è in errore. Poi: una linea = un magnetotermico dedicato.

### Dimensionamento rapido idraulico

**Categoria:** Dimensionamento · **Corso:** Impiantistica completa

Le regole pratiche per dimensionare tubazioni e portate senza software.

- **Tecnologia e criteri:** Portata per tipologia: lavabo 0,10-0,15 l/s, doccia 0,15-0,20, vasca 0,20-0,30, WC 0,10-0,12; tubo multistrato 16mm = 1 punto erogazione, 20mm = 2-3 punti, 25-26mm = colonnina piano.
- **Applicazioni:** Preventivi rapidi, verifiche di progetto, piccole ristrutturazioni.
- **Vantaggi:** Velocità immediata di stima; coerenza tra tubo e punti d'uso.
- **Limiti e attenzioni:** Resta una stima: il calcolo di norma (UNI EN 806) serve per gli edifici complessi.
- **Costi ed economia:** Tabella portate disponibile in ogni manuale tecnico.
- **Caso tipico:** Metodo del 'carico di somma' (DIN 1988-300).
- **Normativa:** UNI EN 806-3.
- **Nota di cantiere:** Regola mnemonica: 'un tubo 16 per ogni becco, 20 per due, 26 per la colonna' copre il 90% delle abitazioni ordinarie.

### Cabina di trasformazione MT/BT

**Categoria:** Elettrica · **Corso:** Impiantistica completa

Il cuore elettrico di edifici grandi: trasformazione da media tensione a bassa tensione.

- **Tecnologia e criteri:** Celle MT (sezionatori, interruttori, trasformatore 15-20/0,4 kV), celle BT, sistema SG, misura ENEL in cabina.
- **Applicazioni:** Condomini grandi, uffici, hotel, industrie, data center.
- **Vantaggi:** Autonomia gestionale; tariffe MT più convenienti; continuità di servizio.
- **Limiti e attenzioni:** Manutenzione obbligatoria con personale abilitato; spazio e costi iniziali.
- **Costi ed economia:** Cabina 630-1000 kVA: 40-120k€ chiavi in mano; manutenzione: 3-8k€/anno.
- **Caso tipico:** Cabine standardizzate 15/20 kV secondo norma CEI.
- **Normativa:** CEI 0-16 (allacciamenti); DPR 462/01 (esercizio); leggi gioco? no: L.186/68.
- **Nota di cantiere:** La gestione della cabina richiede un 'esercente' nominato: molti condomini lo ignorano e rischiano sanzioni e blackout.

### Cavidotti e canaline

**Categoria:** Elettrica · **Corso:** Impiantistica completa

Distribuzione dei cavi elettrici in canaline, tubi protettivi, sottotraccia.

- **Tecnologia e criteri:** Tubi corrugati 16-25 mm, canaline 25x40+, sottoservizi; cavi FG16OR16, N07V-K; il posatoio va nella muratura secondo norma.
- **Applicazioni:** Ogni edificio: posa in opera dei cavi.
- **Vantaggi:** Sistematicità e tracciabilità; il sottotraccia è invisibile ed esteticamente perfetto.
- **Limiti e attenzioni:** Tubi troppo pieni (>40% riempimento) surriscaldano; canaline esteticamente critiche se non progettate.
- **Costi ed economia:** Posa punto luce in traccia: 60-120 €; canalina 25x40: 3-6 €/ml.
- **Caso tipico:** Sistemi a secco: canaline esterne certificate CEI.
- **Normativa:** CEI 64-8-2 (posa); CEI 64-8-5 (selezione cavi).
- **Nota di cantiere:** La regola 40% di riempimento tubo non è burocratica: un tubo pieno surriscalda il cavo e degrada l'isolante in anni.

### Impianto TV, satellitare e broadcast

**Categoria:** Elettrica · **Corso:** Impiantistica completa

Distribuzione segnali TV terrestri/satellitari, DAB, streaming strutturato.

- **Tecnologia e criteri:** Antenne UHF, parabole, centralini d'antenna, prese multimediali (TV+SAT+DATA), amplificatori, matrici.
- **Applicazioni:** Condomini, hotel, ospedali (sistemi SMATV).
- **Vantaggi:** La presa multimediale unificata semplifica ogni locale; matrici per hospitality.
- **Limiti e attenzioni:** Le vecchie reti cascata degradano: i condomini storici hanno impianti TV pessimi.
- **Costi ed economia:** Impianto condominiale: 30-80 €/appartamento; matrice hotel: 1-5k€.
- **Caso tipico:** Centralini Fracarro, IKUSI, Televes.
- **Normativa:** Legge 249/97 (Telecom); CEI 28-1.
- **Nota di cantiere:** In ristrutturazione: passare cavo coassiale 5E + LAN in ogni stanza: il 'cordone' mediale della casa moderna.

### Impianto di terra (SG)

**Categoria:** Elettrica · **Corso:** Impiantistica completa

Dispersore di terra: protezione di persone e cose dai guasti elettrici e fulmini.

- **Tecnologia e criteri:** Piazzola dispersori (aste/spire rame), conduttore di terra PE, morsettiera, interruttore differenziale coordinato.
- **Applicazioni:** Tutti gli edifici, obbligatorio per legge.
- **Vantaggi:** La messa a terra è IL sistema che rende efficaci i differenziali; resistenza <40 ohm (valore tipico) o secondo progetto.
- **Limiti e attenzioni:** Realizzata male nei cantieri (bastano poche decine di ohm in più per non funzionare).
- **Costi ed economia:** Messa a terra casa: 200-600 €; misura con protocollo: 150-300 €.
- **Caso tipico:** Piazzole con aste da 1,5-2 m in terreno omogeneo.
- **Normativa:** CEI 64-8; CEI EN 61936.
- **Nota di cantiere:** Ogni ristrutturazione radicale = nuova verifica del dispersore (obbligatoria) con VERBALE: niente verbale, niente conformità.

### Protezione da sovratensioni (SPD)

**Categoria:** Elettrica · **Corso:** Impiantistica completa

Difesa da fulmini e manovre rete: scaricatori di sovratensione.

- **Tecnologia e criteri:** SPD Tipo 1+2 (testa 10/350 μs) a monte, Tipo 2 nei quadri di zona, Tipo 3 vicino ai carichi sensibili.
- **Applicazioni:** Edifici con impianto fulmini, zone fulminose, impianti elettronici/FV.
- **Vantaggi:** Protegge elettronica, quadri KNX, inverter FV, elettrodomestici: danni da fulmine costano 10x gli SPD.
- **Limiti e attenzioni:** Spesso omessi per risparmio; installati male (cavi troppo lunghi).
- **Costi ed economia:** SPD Tipo 1+2: 100-300 €; installazione compresa: 200-500 €.
- **Caso tipico:** Dehn, ABB, Citel.
- **Normativa:** CEI 64-8-4; CEI EN 61643.
- **Nota di cantiere:** L'impianto fulmini senza SPD interni protegge l'involucro, non l'elettronica: dopo un fulmine i danni tipici sono sul domotica/FV. Gli SPD costano meno di un inverter.

### Quadro generale di bassa tensione

**Categoria:** Elettrica · **Corso:** Impiantistica completa

Distribuzione e protezione dell'energia elettrica di un edificio.

- **Tecnologia e criteri:** Interruttore generale, magnetotermici (MCB), differenziali (RCD 30 mA / 300 mA selettivi), barre, quadri modulari DIN.
- **Applicazioni:** Qualsiasi edificio: dal monolocale alla torre.
- **Vantaggi:** Selettività e protezione delle persone; manutenibilità modulare.
- **Limiti e attenzioni:** Quadri pieni zeppi e mal etichettati: incubo decennale; aggiunte abusive.
- **Costi ed economia:** Quadro appartamento completo: 300-900 € materiali; quadro condominiale: 1-5k€.
- **Caso tipico:** Componenti ABB, Schneider, Gewiss, Siemens.
- **Normativa:** CEI 64-8; CEI EN 61439 (quadri).
- **Nota di cantiere:** Il differenziale 30 mA salva la vita: ogni ambiente bagnato deve avere protezione dedicata. Punto non negoziabile.

### Rete dati LAN strutturata

**Categoria:** Elettrica · **Corso:** Impiantistica completa

Cablaggio dati ethernet dell'edificio: dorsali e punti rete in ogni ambiente.

- **Tecnologia e criteri:** Cavo Cat6/Cat6A FTP, armadietti rack con patch panel, switch PoE, Wi-Fi access point cablati.
- **Applicazioni:** Abitazioni (ufficio smart working), uffici, hotel, scuole.
- **Vantaggi:** La dorsale di dati è la 'ferrovia' della domotica moderna: ogni dispositivo IP ci passa.
- **Limiti e attenzioni:** Wi-Fi mesh senza dorsale cablata = colli di bottiglia.
- **Costi ed economia:** Punto rete posato: 80-150 €; switch PoE 8 porte: 100-300 €; AP Wi-Fi 6: 100-400 €.
- **Caso tipico:** Standard Cat6A per dorsali (10 Gbit-ready); PoE per camere e AP.
- **Normativa:** ISO/IEC 11801; CEI EN 50174.
- **Nota di cantiere:** Regola moderna: 2 prese dati per camera + 1 per TV + dorsale al router. Il Wi-Fi si aggiunge SOPRA la dorsale, mai al suo posto.

### Accumulo batterie domestico

**Categoria:** FER · **Corso:** Impiantistica completa

Batterie agli ioni di litio per accumulare il FV e usarlo di sera: l'autoconsumo oltre il 60-80%.

- **Tecnologia e criteri:** LiFePO4 (sicuri, lunghi cicli), modulari 5-20 kWh, ibridi o retrofit AC/DC, gestione con inverter ibrido.
- **Applicazioni:** Abitazioni con FV, B&B, piccoli terziari, condomini con CER.
- **Vantaggi:** Massimizza l'autoconsumo; backup di emergenza per blackout (funzione islanding).
- **Limiti e attenzioni:** Il ROI puro è lungo (8-15 anni se non c'è incentivo); la batteria degrada (80% dopo 6.000 cicli).
- **Costi ed economia:** Batteria 10 kWh: 4.000-8.000 € installata; costo/kWh in calo continuo.
- **Caso tipico:** Tesla Powerwall, BYD, Pylontech, Sonnen (tedesco, servizi CER).
- **Normativa:** UNI CEI 0-16 (connessi BT); regole CEI 0-21 aggiornate per accumulo.
- **Nota di cantiere:** L'accumulo conviene davvero con: prezzi elettricità alti, incentivi, backup desiderato. Altrimenti la PDC consuma il surplus di giorno: 'batteria termica' gratis.

### Colonnine di ricarica veicoli elettrici

**Categoria:** FER · **Corso:** Impiantistica completa

Infrastruttura di ricarica privata e condominiale: la nuova frontiera degli edifici.

- **Tecnologia e criteri:** Wallbox 7-22 kW AC, colonnine DC per flotte, gestione carichi (dynamic load management), prese tipo 2, contabilizzazione (RFID).
- **Applicazioni:** Box auto, parcheggi condominiali, uffici, hotel, aziende.
- **Vantaggi:** L'edificio diventa 'distributore': servizio ai residenti/dipendenti; richiesto sempre più spesso in vendita/affitto.
- **Limiti e attenzioni:** I quadri elettrici condominiali non sono pronti: serve load management; i condomini litigano sul costo dell'energia comune.
- **Costi ed economia:** Wallbox 7 kW: 400-1.200 € + posa; colonnina DC 50 kW: 15.000-25.000 €.
- **Caso tipico:** Wallbox Pulsar, Zaptec, ABB Terra; gestione: monta o openWB.
- **Normativa:** CEI EN 61851; CEI 0-21 per connessione.
- **Nota di cantiere:** La regola d'oro condominiale: wallbox con dynamic load management + contabilizzazione RFID (chi consuma paga). Nessun attrito, nessuna guerra tra condomini.

### Fotovoltaico: stringhe, inverter e connessione

**Categoria:** FER · **Corso:** Impiantistica completa

Generazione elettrica da sole: il cuore della transizione energetica degli edifici.

- **Tecnologia e criteri:** Moduli (400-600 Wp, TOPCon/IBC oggi), inverter stringa o microinverter/ottimizzatori, stringbox, connessione BT con CEI 0-21/0-16, metering bidirezionale.
- **Applicazioni:** Tetti di abitazioni, capannoni, facciate, carport, agrivoltaico.
- **Vantaggi:** Il costo è crollato (70% in 15 anni); il risparmio in bolletta è immediato con autoconsumo; incentivi (Ritiro Dedicato, CER).
- **Limiti e attenzioni:** La resa dipende da orientamento/inclinazione/ombreggiamenti; la burocrazia (GSE) scoraggia.
- **Costi ed economia:** Impianto 6 kWp residenziale: 7.000-12.000 € (2025) installato; capannone 100 kWp: 60.000-90.000 €.
- **Caso tipico:** Moduli: LONGi, Jinko, Trina; inverter: SolarEdge, Fronius, Huawei, SMA.
- **Normativa:** CEI 0-21 (BT), CEI 0-16 (MT); UNI 9174; D.Lgs 28/2011.
- **Nota di cantiere:** Il vero rendimento di un FV si decide al sopralluogo: alberi, comignoli, antenne possono distruggere la produzione di un tetto 'bello'.

### Adduzione gas metano e GPL

**Categoria:** Gas · **Corso:** Impiantistica completa

Reti interne gas: dal contatore agli apparecchi, con sicurezza attiva e passiva.

- **Tecnologia e criteri:** Tubi acciaio, rame, multistrato con marcatura gas, valvole di sicurezza VS, rilevatori gas certificati (UNI 11144).
- **Applicazioni:** Abitazioni, ristoranti, laboratori, industrie.
- **Vantaggi:** Il VS chiude in 2 s in caso di fuga: salva vite (incidenti domestici).
- **Limiti e attenzioni:** Le vecchie reti in gomma sono pericolo reale; verifica triennale da professionista abilitato.
- **Costi ed economia:** Rete interna appartamento: 300-900 €; ristorante: 1-3k€; rilevatore certificato: 60-150 €.
- **Caso tipico:** Valvole di sicurezza ora OBBLIGATORIE in nuovi impianti e in caso di ristrutturazione.
- **Normativa:** UNI 7129; UNI 7131; legge reg. gas (DPR 144/2000).
- **Nota di cantiere:** Norma chiara: in ristrutturazione l'impianto gas va MESSO A NORMA INTEGRALMENTE, non a pezzi: è l'occasione giusta per rivedere tutto.

### Caldaia a condensazione

**Categoria:** HVAC · **Corso:** Impiantistica completa

Generatore di calore a gas a rendimento 90-109%: il punto di riferimento europeo.

- **Tecnologia e criteri:** Bruciatore a modulazione, condensatore che recupera calore latente, scarico a bassa temperatura (materiali PP).
- **Applicazioni:** Riscaldamento e ACS per abitazioni, condomini, terziario.
- **Vantaggi:** Efficienza reale con ritorni freddi (pannelli radianti); compatibile con Conto Termico.
- **Limiti e attenzioni:** Compatibile solo con impianti a bassa temperatura; con radianti alti spreca.
- **Costi ed economia:** Caldaia a camera aperta 24-32 kW: 1.200-2.800 € installata; manutenzione annuale 80-150 €.
- **Caso tipico:** Modulazione 1:10 per convivere con le micro-richieste delle case efficienti.
- **Normativa:** UNI EN 483; Ecodesign ERP; UNI 10389 (verifiche).
- **Nota di cantiere:** La caldaia si dimensiona sull'INVOLUCRO, non sulla metratura: una casa efficiente da 150 m2 in montagna può bastare 15 kW.

### Climatizzazione VRF/VRV multisplit

**Categoria:** HVAC · **Corso:** Impiantistica completa

Sistemi di climatizzazione multisplit evoluti: una sola unità esterna per decine di interni.

- **Tecnologia e criteri:** Refrigerante variabile (R32/R410A in uscita), inverter su ogni interno, recupero di calore tra le zone (simultaneo caldo/freddo).
- **Applicazioni:** Uffici, hotel, ristoranti, grandi abitazioni, condomini.
- **Vantaggi:** Simultaneità caldo/freddo (uffici con facciate diverse) con recupero: efficienza estrema; nessun gas di scarico in locale.
- **Limiti e attenzioni:** Costo iniziale; manutenzione F-gas certificata; la refrigerante distribuita in edifici è dibattuta (norme in aggiornamento).
- **Costi ed economia:** Impianto VRF ufficio: 60-120 €/m2 installato; manutenzione: 5-15 €/m2/anno.
- **Caso tipico:** Daikin VRV, Mitsubishi VRF, LG Multi V, Samsung DVM.
- **Normativa:** F-gas; EN 378 (sicurezza refrigeranti).
- **Nota di cantiere:** Il VRF con recupero totale è la scelta dei terziari premium: chi progetta uffici lo deve saper dimensionare per zone e simultaneità.

### Pannelli radianti a pavimento/parete/soffitto

**Categoria:** HVAC · **Corso:** Impiantistica completa

Distribuzione del calore (e fresco) per irraggiamento: il comfort termico più efficiente.

- **Tecnologia e criteri:** Tubi PE-Xa/PERT in massetto (spessore 5-8 cm sopra i tubi) o sistemi a secco (predalles, ponteggio radiante); mandata 28-35°C.
- **Applicazioni:** Abitazioni nuove, ristrutturazioni con massetto, soffitti radianti per raffrescamento.
- **Vantaggi:** Confort superiore (uniformità ±0,5°C), riduzione polveri (no convezione), perfetto per PDC e caldaie a condensazione.
- **Limiti e attenzioni:** Inerzia termica: lenta a reagire (va con prognosi meteo, non con accensioni manuali); attenzione in massetti con parquet.
- **Costi ed economia:** Pavimento radiante: 40-80 €/m2 materiali+posa (massetto escluso); soffitto radiante: 50-100 €/m2.
- **Caso tipico:** Sistemi a bassa inerzia (secco) per il retrofit; sistemi in massetto per le nuove.
- **Normativa:** UNI EN 1264; UNI 1264-4 calcoli.
- **Nota di cantiere:** Il radiante si controlla con curve climatiche e sonde esterne: il termostato in ogni stanza è quasi un danno col radiante. Da spiegare al cliente.

### Pompa di calore aria-acqua

**Categoria:** HVAC · **Corso:** Impiantistica completa

Macchina frigorifera inversa che scalda (e raffresca) usando l'aria esterna: 1 kWh elettrico -> 3-5 kWh termici.

- **Tecnologia e criteri:** Unità esterna (sorgente) + unità idronica interna; compressori inverter R32; produzione ACS con accumulo; integrazione FV.
- **Applicazioni:** Nuove abitazioni, ristrutturazioni profonde, piccoli terziari, case in montagna.
- **Vantaggi:** Riduzione consumi 50-70% vs caldaia a gas; raffrescamento incluso; abbinamento perfetto a pannelli radianti e FV.
- **Limiti e attenzioni:** Rumorosità unità esterna da gestire; performance che calano sotto -10°C (serve integrazione o dimensionamento prudente).
- **Costi ed economia:** PDC aria-acqua 8-12 kW: 6.000-12.000 € installata; PDC aria-aria multisplit: 1.500-4.000 € per zona.
- **Caso tipico:** Mitsubishi, Daikin, Vaillant, Panasonic: le 'big' del settore residenziale.
- **Normativa:** F-gas Reg. UE 517/2014 (manutenzione obbligatoria); UNI 11300 per calcoli.
- **Nota di cantiere:** La PDC è la scelta di default 2025+ in Italia (anche per il Conto Termico 3.0): il progettista deve saperla dimensionare con il metodo bin (temperature esterne di progetto).

### Pompe di calore ibrido (integrazione)

**Categoria:** HVAC · **Corso:** Impiantistica completa

Combinazione caldaia a gas + pompa di calore: la PDC copre il 90% del fabbisogno, la caldaia i picchi.

- **Tecnologia e criteri:** Gestione intelligente del punto di switch (economica o termica), unico accumulo ACS, integrazione con tariffe dinamiche.
- **Applicazioni:** Ristrutturazioni dove la rete elettrica non basta o il clima è severo; chi vuole il meglio dei due mondi.
- **Vantaggi:** Massimo risparmio senza rinunciare alla sicurezza del picco; derating elettrico ridotto.
- **Limiti e attenzioni:** Doppio generatore da mantenere; controllo integrato da marca unica.
- **Costi ed economia:** Ibrido PDC+caldaia: 8.000-15.000 € installato (PDC + caldaia a condensazione compatte).
- **Caso tipico:** Daikin Hybrid, Vaillant aroTHERM hybrid, Mitsubishi Ecodan Hydro.
- **Normativa:** F-gas + UNI 7129 (gas); Conto Termico 3.0 ammissibile.
- **Nota di cantiere:** L'ibrido è la risposta prudente per il retrofit del patrimonio italiano (4,6 milioni di caldaie a gas obsolete): il mio LLM deve conoscerlo bene.

### VMC: ventilazione meccanica controllata

**Categoria:** HVAC · **Corso:** Impiantistica completa

Ricambio d'aria con recupero di calore: obbligatoria (di fatto) nelle case efficienti e passive.

- **Tecnologia e criteri:** Centralina con scambiatore entalpico o controflusso (rendimento 80-92%), reti di distribuzione aria, bocchette a flusso continuo o variabile.
- **Applicazioni:** Nuove costruzioni, ristrutturazioni profonde, scuole, uffici (legge obbliga ricambio).
- **Vantaggi:** Fino al 90% del calore recuperato; umidità e CO2 controllate; niente muffa da condensa.
- **Limiti e attenzioni:** La manutenzione filtri è obbligatoria e trascurata; le reti mal progettate sono rumorose.
- **Costi ed economia:** VMC centralizzata casa: 3.000-8.000 € installata; VMC decentralizzata (monoblocco parete): 500-1.500 €/locale.
- **Caso tipico:** Zehnder, Zehnder ComfoAir; Mitsubishi Lossnay; Vortice.
- **Normativa:** UNI EN 13779; UNI/TS 11300-2; DM 26/06/2015 (requisiti energetici, ventilazione).
- **Nota di cantiere:** La VMC decentralizzata è il compromesso giusto per il retrofit: il 70% del beneficio a 1/4 del costo e senza opere murarie.

### Ventilazione ambienti di lavoro e capannoni

**Categoria:** HVAC · **Corso:** Impiantistica completa

Aspirazione e ricambio nei luoghi di lavoro: salute obbligatoria e spesso progettata male.

- **Tecnologia e criteri:** Capiato (ventilatori a tetto), ventilatori a parete, sistemi di destratificazione, condizionatori evaporativi.
- **Applicazioni:** Capannoni, officine, magazzini, cucine industriali, laboratori.
- **Vantaggi:** Riduzione stress termico (protezione lavoratori); in estate i capannoni senz'aria sono fermi produttivi.
- **Limiti e attenzioni:** La destratificazione nei capannoni alti ripaga in 1-2 anni ma pochi la fanno.
- **Costi ed economia:** Ventilatore a tetto 1.500 mm: 400-1.000 €; sistema destratificazione capannone: 5-15 €/m2.
- **Caso tipico:** Big Ass Fans, standard industriale.
- **Normativa:** D.Lgs 81/08 allegato XVII (microclima); UNI EN ISO 7730 (comfort).
- **Nota di cantiere:** Prima di installare il condizionatore in un capannone, chiedi: il tetto è coibentato? Un tetto caldo annulla qualsiasi climatizzazione (soffitti radianti 60-70°C in estate).

### Addolcimento e trattamento acque

**Categoria:** Idraulica · **Corso:** Impiantistica completa

Condizionamento chimico e fisico delle acque: durezza, ferro, sedimenti, legionella.

- **Tecnologia e criteri:** Addolcitori a resine (Na+), dosatori polifosfati, filtri a sedimenti/carbone, sistemi UV, trattamenti shock per legionella.
- **Applicazioni:** Zone molto dure (>30 °F), caldaie, torri evaporative, ospedali, piscine, laboratori.
- **Vantaggi:** Riduce incrostazioni (+20% efficienza caldaia); protegge scambiatori e rubinetteria.
- **Limiti e attenzioni:** L'acqua addolcita non è potabile: ramo separato; manutenzione resine.
- **Costi ed economia:** Addolcitore domestico: 400-1.200 €; industriale: 2-10k€; analisi acqua: 50-150 €.
- **Caso tipico:** Addolcimento standard in gran parte del Centro-Sud Italia (acque >25-35 °F).
- **Normativa:** DPR 236/88 (qualità acque potabili); UNI EN 806.
- **Nota di cantiere:** Prima di qualsiasi trattamento: ANALISI dell'acqua (60 €) che determina tutto il resto. Mai vendere un addolcitore senza analisi.

### Adduzione acqua potabile

**Categoria:** Idraulica · **Corso:** Impiantistica completa

Distribuzione acqua fredda e calda sanitaria (ACS) dall'allaccio ai punti di erogazione.

- **Tecnologia e criteri:** Tubi multistrato (PE-Xb/Al/PE-Xb), PPR, acciaio inox pressato; collettori con valvole di regolazione e detentori; circolazione ACS per grandi impianti.
- **Applicazioni:** Abitazioni, uffici, alberghi, ospedali, laboratori.
- **Vantaggi:** Multistrato: rapidità di posa e nessuna ossidazione; collettori: bilanciamento e manutenzione puntuale.
- **Limiti e attenzioni:** PPR richiede attrezzatura di saldatura; la circolazione ACS costa se non isolata bene.
- **Costi ed economia:** Multistrato 16-20mm: 1,5-4 €/ml; collettore 8 vie: 60-150 €; installazione punto acqua: 150-350 €.
- **Caso tipico:** Impianti a collettore (impianto a 'pettine') ora standard nelle abitazioni moderne.
- **Normativa:** UNI EN 806; D.M. 174/2004 (requisiti acque potabili interni); D.Lgs 18/2023 (edilizia).
- **Nota di cantiere:** L'ACS deve arrivare <25 s e >50°C (anti-legionella): percorso max 15-20 m dal generatore o inserire circolazione.

### Protezione contro rischio di contaminazione (sistemi a tenuta di rifiuto)

**Categoria:** Idraulica · **Corso:** Impiantistica completa

Dispositivi antinquinamento per evitare risalite nei punti d'acqua: zone di protezione.

- **Tecnologia e criteri:** Vasi di espansione con membrane conformi, dispositivi BA (break tank), rubinetti termostatici con limitazione.
- **Applicazioni:** Ospedali, dentisti, laboratori, cucine industriali, idromassaggio.
- **Vantaggi:** Previene contaminazioni chimiche e batteriche (legionella inclusa).
- **Limiti e attenzioni:** Sottovalutato dai piccoli artigiani; controlli sanitari severi negli edifici pubblici.
- **Costi ed economia:** Dispositivi: 50-400 €/punto; progetto zone: da 200 €.
- **Caso tipico:** Zone di protezione secondo EN 1717.
- **Normativa:** UNI EN 1717 (fondamentale); circolari ministeriali legionella.
- **Nota di cantiere:** Ogni punto d'acqua deve avere la giusta 'zona di protezione': è il requisito più trascurato e più sanzionato negli esercizi pubblici.

### Scarichi acque nere e grigie

**Categoria:** Idraulica · **Corso:** Impiantistica completa

Evacuazione acque reflue: colonne di scarico, rami orizzontali, ventilazione.

- **Tecnologia e criteri:** PVC-U e PP silenziosi, HTEM ad alta temperatura per lavatrici/ospedali; vasi a sifone e pilette; colonna con attacco ventilazione.
- **Applicazioni:** Bagni, cucine, lavanderie, laboratori, condomini.
- **Vantaggi:** Il PP silenzioso riduce il rumore di scarico di 10-15 dB: comfort notturno.
- **Limiti e attenzioni:** Pendenze errate = intasamenti cronici; curve eccessive vietate.
- **Costi ed economia:** Tubo PP silenzioso 110: 6-12 €/ml; posa verticale: 30-60 €/ml compreso accessori.
- **Caso tipico:** Colonne a ventilazione secondaria negli edifici alti (norma).
- **Normativa:** UNI EN 12056; EN 1329 (PVC); UNI 9494 (pilette).
- **Nota di cantiere:** Mai ridurre il diametro verso il basso: la colonna va calcolata sul numero di apparecchi scaricanti contemporaneamente (UNI EN 12056).

### Scarichi pluviali

**Categoria:** Idraulica · **Corso:** Impiantistica completa

Collezioni e smaltimento acque meteoriche: tetti, lastrici, cortili.

- **Tecnologia e criteri:** Pluviali in PVC/PP, caditoie per lastrici solari, vasche di prima pioggia (per reintegro), fognatura separata.
- **Applicazioni:** Tetti, terrazzi, piazzali, parcheggi interrati (con vasche di laminazione).
- **Vantaggi:** Separazione acque piovane/recupero: riduzione bolletta idrica e rischio allagamenti.
- **Limiti e attenzioni:** Fognatura mista satura = rigurgiti; vasche di laminazione grandi da pulire.
- **Costi ed economia:** Pluviale 80-110: 3-8 €/ml; caditoia lastrico: 30-80 €/pz; vasca laminazione: 80-200 €/m3.
- **Caso tipico:** Sistemi di recupero acque piovane con cisterna e riuso per irrigazione/WC.
- **Normativa:** UNI EN 12056-3; D.Lgs 152/06 (tutela acque).
- **Nota di cantiere:** Su lastrici e cortili: caditoie + disconnessione fognaria nera sono la prima difesa contro gli allagamenti urbani.

### Impianto a sprinklers

**Categoria:** Idraulica antincendio · **Corso:** Impiantistica completa

Spegnimento automatico a pioggia: la protezione antincendio più efficace al mondo.

- **Tecnologia e criteri:** Teste sprinkler a bulbo termico (57-141°C), reti calcolate a portata, centrale di allarme-valvole, serbatoio/gruppo pompe dedicato.
- **Applicazioni:** Magazzini, archivi, parcheggi, hotel, ospedali, data center, cucine industriali.
- **Vantaggi:** Riduce morti e danni del 80-90% quando attivo; abbassa polizze assicurative.
- **Limiti e attenzioni:** Costo iniziale; acqua danni su beni non protetti; progetto certificato (VdS/FM o UNI).
- **Costi ed economia:** Impianto: 15-40 €/m2 per capannoni (tubi nudi) a 40-80 €/m2 per uffici con controsoffitti.
- **Caso tipico:** Sistemi NFPA 13/EN 12845; teste 'fast response' per hotel e ospedali.
- **Normativa:** UNI EN 12845; NFPA 13; UNI 9490 (progettazione).
- **Nota di cantiere:** I sprinkler si progettano SULLA FALSO SOFFITTO definitivo: cambiare il controsoffitto dopo = rifare l'impianto. Coordinamento col cartongesso è critico.

### Impianto idranti e naspi

**Categoria:** Idraulica antincendio · **Corso:** Impiantistica completa

Rete antincendio a presidi manuali: idranti UNI 45 e avvolgibili (naspi).

- **Tecnologia e criteri:** Rete dedicata in acciaio zincato/saldato, idranti a colonna o a parete, naspo 30 m DN25/45, quadro di alimentazione e pressurizzazione.
- **Applicazioni:** Condomini, uffici, scuole, musei, esercizi commerciali.
- **Vantaggi:** Spegnimento immediato con personale addestrato; costo contenuto.
- **Limiti e attenzioni:** Richiede addestramento dei residenti; manutenzione semestrale obbligatoria.
- **Costi ed economia:** Idrante UNI 45: 150-400 €; naspo: 80-200 €; quadro antincendio con 2 elettropompe: 2-6k€.
- **Caso tipico:** Ogni condominio italiano >10.000 m3 (o >24 m altezza) secondo norma.
- **Normativa:** UNI 9484; NFPA 14 (per avvolgibili); DM 2 settembre 2021.
- **Nota di cantiere:** Gli idranti richiedono portata: verificare la rete idrica condominiale prima di installarli (spesso serve quadro di pressurizzazione).

### Conto Termico 3.0, CEE e detrazioni per impianti

**Categoria:** Incentivi · **Corso:** Impiantistica completa

Gli incentivi 2025+ per la riqualificazione energetica e gli impianti efficienti.

- **Tecnologia e criteri:** Conto Termico 3.0 (2025): incentivi a premio per pompe di calore, caldaie a biomassa, solare termico; CEE (certificati bianchi) per scambi termici e VMC; detrazioni fiscali se disponibili.
- **Applicazioni:** Ristrutturazioni di involucro e impianti: la maggior parte degli interventi rientra in qualcosa.
- **Vantaggi:** Gli incentivi cambiano la bancabilità degli interventi: la PDC con CT3.0 diventa la scelta quasi obbligata.
- **Limiti e attenzioni:** Le regole cambiano spesso (il LLM deve sapere di verificare sempre il testo vigente); le pratiche richiedono professionisti abilitati.
- **Costi ed economia:** Premio CT3.0: percentuali sul costo (fino a 40-50% per le PDC in sostituzione caldaia); i valori esatti vanno verificati su GSE.
- **Caso tipico:** Portale GSE; EGE (esperti in gestione energetica) per le pratiche grandi.
- **Normativa:** DM Conto Termico 3.0 (2025); direttive CEE ARERA; normativa fiscale annuale.
- **Nota di cantiere:** Regola critica per il LLM: MAI citare cifre di incentivi come certe: indicare SEMPRE la fonte (GSE/ENEA) e la data di verifica — gli incentivi sono la causa #1 di informazioni datate nel settore.

### D.Lgs 37/08: appalti e gestione impianti

**Categoria:** Normativa impianti · **Corso:** Impiantistica completa

La legge italiana dell'impiantistica: installazione, manutenzione, abilitazioni dei professionisti.

- **Tecnologia e criteri:** Requisiti dei progettisti/installatori (abilitazione DM), Dichiarazione di Conformità (DiCo), libretto impianto, verifiche periodiche.
- **Applicazioni:** Ogni intervento su impianti: dal nuovo impianto alla sostituzione della caldaia.
- **Vantaggi:** Tutto tracciato e legale; il libretto è il 'libro sanitario' dell'edificio.
- **Limiti e attenzioni:** Sanatorie e abusi comuni (lavori senza DiCo); il compratore di casa poi paga.
- **Costi ed economia:** Costo DiCo e pratiche: 100-400 €; verifica energetica (legge 10): 300-900 €.
- **Caso tipico:** Pratiche standardizzate per legge 10, CPI, prevenzione incendi.
- **Normativa:** D.Lgs 37/08; DM 37/08; Legge 10/91 (energetica).
- **Nota di cantiere:** Chi compra casa DEVE chiedere libretti e DiCo di tutti gli impianti: l'immobile senza documentazione vale meno, punto.

### Legge 10/91 e certificazione energetica (APE)

**Categoria:** Normativa impianti · **Corso:** Impiantistica completa

La normativa energetica degli edifici: requisiti, calcoli, attestato di prestazione energetica.

- **Tecnologia e criteri:** Calcolo dei fabbisogni (UNI/TS 11300), metodologia energetica nazionale (decreto requisiti), APE in vendita/affitto, CTU progettazione.
- **Applicazioni:** Nuove costruzioni, ristrutturazioni importanti, compravendite.
- **Vantaggi:** L'APE orienta compratori e affittuari; i requisiti spingono l'efficienza (involucro, impianti).
- **Limiti e attenzioni:** Calcoli spesso 'di facciata' per chiudere pratica; il valore APE 'alla rovescia' è un rischio legale.
- **Costi ed economia:** Progetto legge 10 + APE: 300-900 €; pratica edilizia energetica grande: 1-3k€.
- **Caso tipico:** Software Namirial, Logical Soft, MC4, Blumatica.
- **Normativa:** Legge 10/91; D.Lgs 192/2005 (EPBD); D.Lgs 48/2020 aggiornato.
- **Nota di cantiere:** Da quando esiste la 'scheda descrittiva' dell'APE (2023), l'attestato è diventato uno strumento di marketing: l'LLM deve saper leggere e spiegare le classi (A4-G).


## Tecnologia delle macchine termiche

*Corso `MACCHINE_TERMICHE_TECNOLOGIA_PACK` — 9 voci*

### La caldaia a condensazione: il circuito della condensa

**Categoria:** Caldaie · **Corso:** Tecnologia delle macchine termiche

Come la caldaia moderna recupera il calore latente dei fumi: i componenti aggiuntivi.

- **Tecnologia e criteri:** Scambiatore secondario (condensatore) in acciaio inox o alluminio-silicio; scarico condensa in PVC/PP (acido, pH 3-5); il sifone con collegamento alla rete fognaria; la modulazione 1:6-1:10; il rendimento 90-109% (su potere calorifico inferiore).
- **Applicazioni:** Nuove installazioni e sostituzioni obbligatorie (incentivi Conto Termico 3.0).
- **Vantaggi:** Il recupero di calore vale il 10-15% in più: sul gas risparmia 100-200 €/anno.
- **Limiti e attenzioni:** La condensa va smaltita correttamente: lo scarico a pioggia è vietato e corrosivo.
- **Costi ed economia:** Sostituzione caldaia a condensazione: 1.500-3.000 € installata.
- **Caso tipico:** Le caldaie a condensazione installate in Italia: oltre 10 milioni (dati Anima).
- **Normativa:** Ecodesign ERP; UNI 7129.
- **Nota di cantiere:** La caldaia a condensazione rende AL MASSIMO con impianti a bassa temperatura (pannelli radianti, termosifoni dimensionati per 55-60°C): con radiatori vecchi a 80°C perde metà del vantaggio.

### La caldaia murale a gas: anatomia completa delle componenti

**Categoria:** Caldaie · **Corso:** Tecnologia delle macchine termiche

Cosa c'è dentro la caldaia che scalda la maggior parte delle case italiane.

- **Tecnologia e criteri:** Componenti: scambiatore principale (monotermico o bitermico per ACS), bruciatore a modulazione (minimo 3-8 kW), pompa di circolazione, vaso di espansione (6-8 l), valvola di sicurezza 3 bar, sonda fumi/analisi combustione, ventilatore, scambiatore di condensazione (solo a condensazione), centralina elettronica (sensore mandata, flusso, pressione).
- **Applicazioni:** Riscaldamento e ACS di abitazioni e piccoli condomini.
- **Vantaggi:** Conoscere i componenti = diagnosticare il guasto: il 90% dei 'guasti caldaia' sono componenti da 30-150 €.
- **Limiti e attenzioni:** L'elettronica moderna richiede assistenza autorizzata per la garanzia.
- **Costi ed economia:** Componenti di ricambio: 30-300 €; scambiatore: 150-400 €.
- **Caso tipico:** Le caldaie a camera stagna vs aperta: la scelta dipende dal tiraggio del camino (verifica UNI 7129).
- **Normativa:** UNI 7129; schede tecniche costruttori (Baxi, Vaillant, Ariston).
- **Nota di cantiere:** Prima prova in caso di 'non scalda': verificare pressione impianto (1-1,5 bar) e flusso ACS: il 40% dei guasti sono idraulici, non elettronici.

### Canne fumarie e camini: materiali e tiraggio

**Categoria:** Canne fumarie · **Corso:** Tecnologia delle macchine termiche

Il camino corretto: acciaio inox 316L, coibentazione e il calcolo del tiraggio.

- **Tecnologia e criteri:** Materiali: acciaio inox 316L (resistenza acidi condensa), coibentato (doppia parete, isolamento in lana di roccia); sezioni: caldaia 110-130 mm, stufa pellet 80 mm, camino aperto secondo sezione focolare (≥1/10-1/15 del focolare); il tiraggio dipende da altezza (min 4 m sopra il generatore) e temperatura.
- **Applicazioni:** Ogni generatore a fiamma (caldaia, stufa, camino, termocamino).
- **Vantaggi:** La canna fumaria giusta garantisce sicurezza ed efficienza: il tiraggio insufficiente soffoca la fiamma e riempie di monossido.
- **Limiti e attenzioni:** Le canne fumarie esistenti in muratura spesso non sono idonee per a condensazione (acido corrosivo).
- **Costi ed economia:** Canna fumaria coibentata: 60-150 €/ml installata.
- **Caso tipico:** Le verifiche periodiche dei camini (spazzacamino) e le norme antincendio (UNI 10683? no: 'requisiti canne fumarie da verificare').
- **Normativa:** UNI 7129; UNI EN 1856 (canne fumarie metalliche).
- **Nota di cantiere:** Il test del tiraggio: fiamma accesa alla base della canna (tiraggio 'a candela'): se la fiamma vira verso l'interno, la canna va rifatta. Mai operare 'a tentativi' con i generatori a fiamma.

### Il condizionatore (split): anatomia del ciclo frigorifero

**Categoria:** Climatizzatori · **Corso:** Tecnologia delle macchine termiche

Come funziona la macchina che raffresca: compressore, condensatore, espansione, evaporatore.

- **Tecnologia e criteri:** Il ciclo di Rankine inverso: compressore (rotativo o scroll), condensatore (scarica calore all'esterno), dispositivo di espansione (capillare o valvola elettronica EEV), evaporatore (assorbe calore dall'interno); il gas refrigerante R32 (GWP 675, obbligatorio dal 2025 per nuove macchine); l'inverter (modulazione continua del compressore).
- **Applicazioni:** Raffrescamento estivo e riscaldamento invernale (pompa di calore 'aria-aria').
- **Vantaggi:** Il ciclo frigorifero è lo stesso di tutte le macchine termiche: capirlo una volta = capirle tutte.
- **Limiti e attenzioni:** Il rendimento crolla con le temperature esterne estreme (raffrescamento a +40°C, riscaldamento a −10°C).
- **Costi ed economia:** Split 12000 BTU (3,5 kW): 600-1.500 € installato; manutenzione: 80-150 €/anno.
- **Caso tipico:** Il mercato italiano del condizionatore (oltre 10 milioni di split, dati ANTA? no: 'dati settore').
- **Normativa:** Reg. UE 517/2014 (F-gas); UNI EN 378.
- **Nota di cantiere:** La potenza si sceglie sul fabbisogno REALE (isolamento), non sui m2: una stanza ben coibentata da 25 m2 basta 9000 BTU, una vetrata esposta sud ne vuole 18000.

### La pompa di calore: il circuito frigorifero al servizio dell'acqua

**Categoria:** Pompe di calore · **Corso:** Tecnologia delle macchine termiche

L'anatomia della macchina del futuro: refrigerazione + idronica.

- **Tecnologia e criteri:** Componenti: compressore (rotativo, scroll o R290? no: 'a doppio stadio per climi freddi'), scambiatore esterno (evaporatore a piastre o 'aerotermo con ventole'), valvola a quattro vie (inversione caldo/freddo), scambiatore interno (a piastre saldobrasate o 'tubo in tubo'), modulo idronico (pompa, vaso espansione, valvole, sonda flusso), resistenza ausiliaria, centralina con modulazione.
- **Applicazioni:** Riscaldamento invernale, raffrescamento estivo e ACS (aria-acqua).
- **Vantaggi:** Una sola macchina per tutto: riscaldamento, raffrescamento, ACS con rendimento 300-500%.
- **Limiti e attenzioni:** La complessità elettronica richiede installatori certificati F-gas e formazione specifica.
- **Costi ed economia:** PDC aria-acqua 8 kW: 4.000-8.000 € installata (prima degli incentivi).
- **Caso tipico:** Le PDC R32 e R290 (propano, GWP basso) della nuova generazione 2024-2026.
- **Normativa:** F-gas; EN 378; UNI 11300.
- **Nota di cantiere:** Il componente più delicato: il compressore. La causa n.1 di guasto prematuro è l'installazione idraulica sbagliata (acqua sporca, aria nell'impianto): il filtro a Y e il spurgo accurato valgono più della marca del compressore.

### Lo scaldabagno: a gas, elettrico e a pompa di calore

**Categoria:** Scaldabagni · **Corso:** Tecnologia delle macchine termiche

La produzione di ACS punto per punto: le tre tecnologie a confronto.

- **Tecnologia e criteri:** A gas: camera aperta (tiraggio camino) o stagna (tiraggio forzato), scambiatore a fascio tubiero, bruciatatore con modulazione; elettrico: resistenza da 1,5-2,5 kW e serbatoio coibentato; a pompa di calore: compressore + scambiatore da 250-300 l, rendimento 2,5-3.
- **Applicazioni:** Abitazioni senza impianto centralizzato, secondi bagni, B&B.
- **Vantaggi:** Lo scaldabagno a gas istantaneo non ha accumulo: energia infinita ma portata limitata (11-17 l/min).
- **Limiti e attenzioni:** Lo scaldabagno a gas in camera da letto è vietato (norma UNI 7129: solo camera stagna o ambienti idonei).
- **Costi ed economia:** Scaldabagno a gas: 400-900 €; elettrico: 150-400 €; a PDC: 800-1.800 €.
- **Caso tipico:** Lo standard italiano dello scaldabagno a gas (milioni installati); il boom dello scaldabagno a PDC per i balconi? no: 'per l'ACS efficiente'.
- **Normativa:** UNI 7129; ecodesign.
- **Nota di cantiere:** Il dimensionamento rapido ACS: 1 persona = 40-60 l a 40°C di accumulo. Una famiglia di 4 con docce serali: accumulo 100-150 l (scaldabagno) o 150-200 l (scaldacqua centralizzato).

### Il termocamino: il focolare che diventa generatore idraulico

**Categoria:** Termocamini · **Corso:** Tecnologia delle macchine termiche

Il camino che scalda l'acqua: potenza 15-25 kW con accumulo obbligatorio.

- **Tecnologia e criteri:** Componenti: focolare in ghisa o acciaio, scambiatore ad acqua intorno alla camera di combustione (il 'serpentino' o la camera d'acqua), sportello a tenuta, presa aria esterna, valvola di sfogo termico (sicurezza contro il bollore), collegamento a serbatoio di accumulo (500-1000 l).
- **Applicazioni:** Case con camino frequente e impianto idronico esistente.
- **Vantaggi:** Combina atmosfera del fuoco visibile e integrazione con riscaldamento centralizzato.
- **Limiti e attenzioni:** SENZA accumulo il termocamino è vietato per norma (bollore istantaneo: la potenza del fuoco supera sempre l'assorbimento istantaneo).
- **Costi ed economia:** Termocamino: 3.000-8.000 €; accumulo 1000 l: 800-1.500 €.
- **Caso tipico:** Le installazioni central-europee (Austria, Germania) dove il termocamino+accumulo è lo standard.
- **Normativa:** UNI 7129 (accumulo obbligatorio); UNI 10683? no: 'da verificare' camini.
- **Nota di cantiere:** La regola d'oro: accumulo = 50-100 l per kW di potenza del focolare. Chi vende il termocamino senza accumulo vende un impianto fuorilegge.

### La termostufa a pellet: anatomia del ciclo del combustibile

**Categoria:** Termostufe · **Corso:** Tecnologia delle macchine termiche

La stufa che scalda l'acqua: serbatoio, coclea, braciere, scambiatore.

- **Tecnologia e criteri:** Componenti: serbatoio pellet (10-30 kg), coclea di dosaggio (alimentazione continua), braciere con crogiolo (accensione elettronica), scambiatore a fumi (a fascio tubiero o a piastre), ventilatore tiraggio, canna fumaria in acciaio inox 316L (diam 80 mm), centralina con sonda temperatura e modulazione.
- **Applicazioni:** Integrazione riscaldamento di ville e appartamenti (fino a 15-20 kW termici).
- **Vantaggi:** Rendimento 85-92%: il pellet è il bio-combustibile più efficiente per residenziale.
- **Limiti e attenzioni:** La canna fumaria è il punto critico: pulizia annuale obbligatoria (incrostazioni che riducono il tiraggio).
- **Costi ed economia:** Termostufa: 2.500-6.000 € installata; pellet: 280-350 €/t.
- **Caso tipico:** Il mercato italiano del pellet (oltre 3 milioni di stufe installate).
- **Normativa:** UNI 14785 (stufe a pellet); UNI 7129 per il collegamento idraulico.
- **Nota di cantiere:** La termostufa scalda L'ACQUA dell'impianto, non è una stufa d'ambiente: richiede sempre vaso di espansione, pompa e valvola di sicurezza come una caldaia (impianto a norma).

### La VMC centralizzata: anatomia della macchina e della rete

**Categoria:** VMC tecnologia · **Corso:** Tecnologia delle macchine termiche

Cosa c'è dentro la centralina e come è fatta la rete di distribuzione.

- **Tecnologia e criteri:** Componenti centralina: scambiatore (controflusso in polipropilene o entalpico con membrana), due ventilatori EC (mandata e ripresa), filtri G4/F7, bypass estivo (sblocco gratuito), sonda umidità/CO2 opzionale, serranda anti-ritorno; rete: canalizzazione in acciaio zincato/flessibile o rigida (Ø 75-160 mm), bocchette a flusso continuo (camera 30-60 m³/h, servizi 20-40 m³/h), silenziatori.
- **Applicazioni:** Case nuove e ristrutturazioni profonde (obbligo quasi-passivo).
- **Vantaggi:** Il cuore della casa sana: recupera l'80-92% del calore e cambia l'aria senza aprire le finestre.
- **Limiti e attenzioni:** La rete mal progettata (curve strette, diametri sbagliati) rende rumorosa e inefficiente la macchina migliore.
- **Costi ed economia:** VMC centralizzata casa 150 m²: 3.000-7.000 € installata.
- **Caso tipico:** Le VMC a flusso continuo con bocchette a regolazione (standard italiano).
- **Normativa:** UNI 10339; DM 26/06/2015.
- **Nota di cantiere:** Il controllo essenziale a fine installazione: misura del portata con anemometro a ogni bocchetta (deve corrispondere al progetto ±10%). Senza misura non c'è collaudo.


## Materiali e componenti dell'impiantistica

*Corso `MATERIALI_COMPONENTI_IMPIANTISTICA_PACK` — 9 voci*

### I collettori (maschio/femmina) e la distribuzione a pettine

**Categoria:** Collettori · **Corso:** Materiali e componenti dell'impiantistica

Il cuore della distribuzione moderna: il collettore e i vantaggi del pettine.

- **Tecnologia e criteri:** Collettore in ottone o acciaio inox con 2-12 uscite; ogni uscita con valvola di detenzione e sfiato; la logica 'un tubo per punto' (nessuna giunzione intermedia nel solaio); il dimensionamento: 1 uscita per punto erogazione.
- **Applicazioni:** Impianti idraulici residenziali moderni (docce, bagni, cucine).
- **Vantaggi:** Una perdita futura colpisce un solo punto, non tutto il solaio: manutenibilità assoluta.
- **Limiti e attenzioni:** Il consumo di tubo è maggiore (30-50% in più di metri lineari).
- **Costi ed economia:** Collettore 8 vie: 60-150 €.
- **Caso tipico:** Lo standard tedesco/italiano della distribuzione a pettine dagli anni 2000.
- **Normativa:** UNI EN 1264? no: 'prassi progettuali'.
- **Nota di cantiere:** Il collaudo della rete a pettine: la prova in pressazione si fa settore per settore con il collettore: isolare una zona alla volta trova il problema in minuti, non in giorni.

### I componenti elettrici dell'impiantista: quadri, magnetotermici, differenziali

**Categoria:** Componenti elettrici · **Corso:** Materiali e componenti dell'impiantistica

L'hardware elettrico che ogni impiantista tocca ogni giorno.

- **Tecnologia e criteri:** Magnetotermico (protezione sovraccarico+corto: 6-63 A, curve B/C/D); differenziale (salvavita 30 mA, selettivo 300 mA per grossi impianti); contattore (comanda carichi potenti da circuiti di comando); relè termico (protezione motori); portafusibili; i cavi (H07V-K 1,5/2,5/4/6 mm², colori: nero/fase, blu/neutro, giallo-verde/tierra); i tubi corrugati 16-20 mm.
- **Applicazioni:** Quadri impianto, quadri pompe, automazioni, VMC.
- **Vantaggi:** Conoscere i componenti elettrici base permette all'idraulico di dialogare con l'elettricista (e viceversa).
- **Limiti e attenzioni:** L'impiantista NON certifica l'impianto elettrico (serve abilitazione): il confine professionale è netto.
- **Costi ed economia:** Magnetotermico: 5-30 €; differenziale: 30-80 €; contattore: 15-60 €.
- **Caso tipico:** I quadri di zona con differenziale dedicato (obbligatorio per bagni e cucine).
- **Normativa:** CEI 64-8.
- **Nota di cantiere:** La regola dell'impiantista: ogni macchina che tocca l'acqua (pompe, lavatrici, scaldabagni) deve essere alimentata da un differenziale 30 mA dedicato: la vita vale più del risparmio di un quadretto.

### L'isolamento delle tubazioni: spessori e materiali

**Categoria:** Isolamento tubazioni · **Corso:** Materiali e componenti dell'impiantistica

Il cappotto dei tubi: dove obbligatorio, di quanto e con cosa.

- **Tecnologia e criteri:** Materiali: elastomero espanso (gomma, spessore 6-13 mm), polietilene espanso (PE-X, 6-20 mm), lana minerale (impianti industriali); obbligatorio su: tubazioni ACS (contro perdite e crescita legionella), tubazioni riscaldamento in locale non riscaldato, tubazioni frigorifere (contro condensa); il fattore λ isolante ≤0,045 W/mK.
- **Applicazioni:** Impianti idraulici e termici di ogni edificio.
- **Vantaggi:** Un tubo non isolato in solaio perde il 10-20% del calore: l'isolamento ripaga in 1-2 anni.
- **Limiti e attenzioni:** L'isolamento mal posato (giunti scoperti) vale meno della metà.
- **Costi ed economia:** Isolamento tubo: 2-5 €/ml materiale.
- **Caso tipico:** Le prescrizioni UNI/TS 11300-2 sulle perdite dei tubi (fino al 20% della resa).
- **Normativa:** UNI EN ISO 12241 (isolamento termico).
- **Nota di cantiere:** L'acqua calda deve arrivare in 25 secondi e a temperatura: i tubi lunghi senza isolamento e senza ricircolo sono il male assoluto dell'energia e del comfort.

### Pompe e circolatori: come funzionano e come si scelgono

**Categoria:** Pompe e circolatori · **Corso:** Materiali e componenti dell'impiantistica

Il cuore che muove l'acqua nei circuiti chiusi.

- **Tecnologia e criteri:** Il circolatore ad alta efficienza (classe A): corpo bagnato o a rotore asciutto, modulazione PWM 0-10V; la curva pompa-carico: prevalenza = perdite di carico del circuito; le 3 velocità storiche vs la modulazione continua; l'installazione in mandata o ritorno con valvola non ritorno.
- **Applicazioni:** Riscaldamento, raffrescamento, ACS con ricircolo, solare termico.
- **Vantaggi:** Il circolatore modulante corretto riduce i consumi elettrici dell'80% rispetto ai vecchi a 3 velocità.
- **Limiti e attenzioni:** Un circolatore sovradimensionato consuma e ronca; uno sottodimensionato non scalda l'ultimo termosifone.
- **Costi ed economia:** Circolatore A: 150-500 €; a rotore asciutto: 200-600 €.
- **Caso tipico:** La sostituzione dei circolatori vecchi in Italia (milioni all'anno).
- **Normativa:** Ecodesign ERP per circolatori.
- **Nota di cantiere:** La regola di Tarabella? no: 'la pompa non si dimensiona sulla portata massima, ma sul punto di lavoro reale': chiedere SEMPRE la curva carico-pressione del circuito, non 'quanti kW serve'.

### I raccordi: pressare, saldare, a innesto, filettare

**Categoria:** Raccordi · **Corso:** Materiali e componenti dell'impiantistica

Come si uniscono i tubi: le 4 tecniche e quando usarle.

- **Tecnologia e criteri:** Pressare (multistrato e rame): pinza a pressare, curve 10-80 €; saldare (rame con cannello, PP-R con polifusore 50-150 €): giunzione a tenuta chimica; a innesto (PEX con manicotto e anello): rapido ma non smontabile; filettare (acciaio): teflon e attrezzatura classica.
- **Applicazioni:** Ogni giunzione di ogni impianto idraulico e gas.
- **Vantaggi:** La pressatura moderna: un operaio giunziona 50 punti al giorno con affidabilità testata.
- **Limiti e attenzioni:** La pressatura sbagliata (ganasce sporche, tubo non a fondo) è la perdita n.1 dei cantieri moderni.
- **Costi ed economia:** Pinza a pressare: 100-400 €.
- **Caso tipico:** Le pressacavi? no: le presse radiali e le presse a morsetto per multistrato.
- **Normativa:** UNI 11344 (pressione minima per giunzioni).
- **Nota di cantiere:** La regola del professionista: una giunzione visibile vale dieci nascoste. E una giunzione inaccessibile deve essere pressata DUE volte (sicurezza) o saldata.

### I tubi per l'acqua: rame, multistrato, PEX, PP-R, acciaio

**Categoria:** Tubi acqua · **Corso:** Materiali e componenti dell'impiantistica

I materiali della rete idraulica: dove usarli e dove evitarli.

- **Tecnologia e criteri:** Rame (rigido e flessibile): eterno, batteriostatico, costoso (6-15 €/m), attenzione alla corrosione per contatto con cls/acciaio; multistrato PEX-Al-PEX (16-32 mm): il più usato in residenziale (1,5-4 €/m), posa rapida con raccordi a pressare; PEX (rosso/blu): economico, per pannelli radianti; PP-R (saldato a caldo): economico e resistente, per esterno e industriale; acciaio zincato/inox: per reti antincendio e industriali.
- **Applicazioni:** Adduzione acqua potabile, scarichi tecnici, antincendio, irrigazione.
- **Vantaggi:** Ogni materiale ha il suo posto: il multistrato in residenziale, il rame in pregiato, il PP-R in industriale.
- **Limiti e attenzioni:** Il rame rubato nei cantieri: valutare alternative nei luoghi a rischio.
- **Costi ed economia:** Prezzi indicativi al metro per diametro 16-20.
- **Caso tipico:** Le reti in multistrato a collettore 'a pettine' nelle case moderne.
- **Normativa:** UNI EN 1057 (rame); UNI 11344 (multistrato); UNI EN ISO 15874 (PP-R).
- **Nota di cantiere:** Il multistrato NON si lascia all'aria nel solaio: protezione UV e meccanica obbligatoria. La guaina corrugata non è optional.

### I tubi per il gas: acciaio, rame, multistrato marcato

**Categoria:** Tubi gas · **Corso:** Materiali e componenti dell'impiantistica

La rete gas: i materiali ammessi e le regole di posa.

- **Tecnologia e criteri:** Acciaio (saldato o filettato): il tradizionale eterno; rame con marcatura gialla 'GAS'; multistrato con marcatura specifica gas (verde/giallo); i giunti a pressare ammessi in nuova installazione; la verifica di tenuta obbligatoria a fine lavori (UNI 11144).
- **Applicazioni:** Reti gas interne per caldaie, cucine, termostufe.
- **Vantaggi:** La tenuta della rete gas è vita: i materiali giusti e le prove giuste sono non negoziabili.
- **Limiti e attenzioni:** Le reti esistenti in gomma o ferro vecchio sono pericolo reale.
- **Costi ed economia:** Rete gas interna appartamento: 300-900 €; rilevatore gas certificato: 60-150 €.
- **Caso tipico:** Le verifiche triennali obbligatorie (legge gas).
- **Normativa:** UNI 7129; UNI 11144 (rilevatori).
- **Nota di cantiere:** Ogni nuova rete gas va provata in pressione (aria) con manometro: 15 minuti senza caduta. Chi non fa la prova non ha installato: ha messo in pericolo.

### Le valvole dell'impianto idraulico: sfera, detentore, termostatica, miscelatrice

**Categoria:** Valvole · **Corso:** Materiali e componenti dell'impiantistica

I rubinetti che regolano l'acqua: i 6 tipi che devi conoscere.

- **Tecnologia e criteri:** Valvola a sfera (apertura/chiusura totale, il nuovo standard); valvola di detenzione (regolazione fine del flusso); valvola termostatica (testina a cera/liquido, mantiene la temperatura di mandata dei corpi scaldanti); valvola miscelatrice (mescola caldo/freddo per l'ACS antiscottatura); valvola di non ritorno (senso unico obbligatorio su circolatori e sistemi); valvola di sfogo aria (sfiato automatico nei punti alti).
- **Applicazioni:** Collettori, corpi scaldanti, impianti ACS, idronici.
- **Vantaggi:** Le valvole giuste al posto giusto: il 50% dei malfunzionamenti idronici sono valvole sbagliate o assenti.
- **Limiti e attenzioni:** Le testine termostatiche vanno disattivate in estate? no: 'i detentori chiusi lasciano l'aria': ogni valvola ha la sua logica d'uso.
- **Costi ed economia:** Valvole: 10-80 €/pz; testine termostatiche: 15-60 €.
- **Caso tipico:** I collettori con valvole di detenzione e sfiato (standard multistrato).
- **Normativa:** UNI EN 215 (testine termostatiche).
- **Nota di cantiere:** Ogni impianto idronico va 'svuotabile': una valvola a sfera in basso e uno sfiato in alto per ogni zona. Chi non prevede lo svuotamento ha progettato un impianto non manutenibile.

### Il vaso di espansione: il componente che salva l'impianto

**Categoria:** Vasi espansione · **Corso:** Materiali e componenti dell'impiantistica

Come assorbire la dilatazione dell'acqua calda: dimensionamento e manutenzione.

- **Tecnologia e criteri:** Vaso a membrana (10-100 l residenziale): gas (azoto o aria) pre-carica 0,5-1,5 bar; dimensionamento rapido: 8-10 l per ogni kW di potenza installata (o 5% del volume d'acqua); la precarica va verificata ogni 2 anni; il vaso aperto in solaio è obsoleto e sconsigliato.
- **Applicazioni:** Ogni impianto idronico chiuso (riscaldamento, raffrescamento, PDC, solare termico).
- **Vantaggi:** Il vaso espansione è la protezione n.1 contro il sovrappressione: l'impianto senza vaso muore in anni.
- **Limiti e attenzioni:** La membrana perde gas nel tempo: la pressione cala e la valvola di sicurezza perde.
- **Costi ed economia:** Vaso espansione 12 l: 40-80 €; 24 l: 60-120 €.
- **Caso tipico:** La causa n.1 dei 'perdita dalla valvola di sicurezza': vaso espansione morto (da verificare).
- **Normativa:** UNI 7129; prassi costruttive.
- **Nota di cantiere:** Il test di 10 secondi: toccare il vaso in funzione: la metà inferiore deve essere fredda (acqua), la superiore tiepida (gas). Se tutto freddo o tutto caldo: membrana rotta, sostituire.


## Piscine e centri wellness

*Corso `PISCINE_E_WELLNESS_PACK` — 7 voci*

### Saune e bagni di vapore: il calore terapeutico

**Categoria:** BeniEssere sauna · **Corso:** Piscine e centri wellness

La sauna finlandese (aria secca 80-100 °C, umidità bassa) e il bagno turco (hammam: vapore 40-50 °C, umidità quasi 100%) sono gli ambienti wellness classici: si costruiscono con materiali che resistono a calore e umidità (legno resinoso per la sauna, ceramica/mosaico per l'hammam) con le barriere al vapore rigorose.

- **Tecnologia e criteri:** La sauna: il rivestimento in legno (abet, cedro: non resinose? le conifere non resinose), la stufa con le pietre (il löyly: l'acqua gettata sulle pietre), la ventilazione (l'aria rinnovata senza perdere calore), la porta in vetro temprato; l'hammam: la struttura in muratura o compositi, il generatore di vapore, la tenuta al vapore assoluta (la barriera vapore sotto il rivestimento, le porte con i sigilli), il pavimento con la pendenza verso il scarico e le pedane antiscivolo.
- **Applicazioni:** Hotel, SPA, centri benessere, ville di pregio.
- **Vantaggi:** La sauna e l'hammam trasformano una casa o un hotel: il valore percepito (e commerciale) sale immediatamente.
- **Limiti e attenzioni:** La tenuta al vapore dell'hammam è critica: i vapori che scappano dietro il rivestimento marcisco la struttura in pochi anni.
- **Costi ed economia:** Costi: sauna 5.000-15.000 €; hammam 8.000-25.000 € (finiture comprese).
- **Caso tipico:** Hammam in hotel con la barriera vapore continua e la camera di espansione del vapore: dopo 8 anni, la struttura intatta; l'hammam gemello con la barriera 'parziale' ha rifatto il controsoffitto adiacente per muffa a 4 anni.
- **Normativa:** Normativa antincendio (le saune sono locali a rischio); specifiche costruttive; igiene (le saune pubbliche hanno regole).
- **Nota di cantiere:** La regola dell'hammam: il vapore è più insidioso dell'acqua: dove arriva il vapore, serve la barriera assoluta.

### Bordi, impianti di massaggio e accessori: la finitura conta

**Categoria:** Bordo vasca · **Corso:** Piscine e centri wellness

Il bordo vasca e gli accessori completano l'opera: i bordi in pietra o gres antiscivolo, gli skimmer invisibili (a sfioro: il livello dell'acqua al bordo), gli impianti idromassaggio (le bocchette d'aria), i giochi d'acqua (cascate, getti), l'illuminazione subacquea.

- **Tecnologia e criteri:** Elementi: il bordo a sfioro (l'acqua arriva al livello del bordo: estetica massima ma richiede il vaschetta di compenso), gli skimmer classici (più pratici, meno eleganti), i rivestimenti dei bordi (gres antiscivolo classe 3, la pietra naturale trattata), l'idromassaggio (l'aria soffiata dalle bocchette: richiede il compressore e le canaline), l'illuminazione LED subacquea (il trasformatore a norma piscina, i cavi speciali), le docce solari e i giochi d'acqua.
- **Applicazioni:** Piscine di pregio, hotel, centri benessere.
- **Vantaggi:** Il bordo ben fatto trasforma la piscina da 'vasca' a 'opera': l'acqua che tocca il bordo è un effetto scenico permanente.
- **Limiti e attenzioni:** L'estetica senza funzione genera manutenzione: il bordo a sfioro richiede il controllo del livello e la pulizia della vaschetta.
- **Costi ed economia:** Costi: bordo a sfioro +30-50% sul bordo classico; l'idromassaggio: +1.000-3.000 €; l'illuminazione subacquea: 500-2.000 €.
- **Caso tipico:** Piscina con bordo a sfioro e illuminazione LED: l'effetto scenico notturno è il punto forte dell'hotel (le recensioni lo citano); la manutenzione extra (la vaschetta) è stata organizzata in 10 minuti settimanali.
- **Normativa:** Normative elettriche (CEI 64-8 per le piscine: le zone 0-1-2); specifiche produttori.
- **Nota di cantiere:** La domanda di progetto: 'l'estetica richiesta quanta manutenzione in più comporta?' — la risposta va scritta nel contratto.

### Le coperture della piscina: proteggere e risparmiare

**Categoria:** Coperture · **Corso:** Piscine e centri wellness

La copertura della piscina non è un optional: mantiene il calore (il 70% delle perdite è evaporazione), mantiene pulita l'acqua (le foglie e la polvere), aumenta la sicurezza (i bambini e gli animali), prolunga la vita dell'impianto.

- **Tecnologia e criteri:** Tipi: la copertura estiva (a bolle, la più economica: mantiene il calore), quella invernale (telone fissato ai bordi: protegge dalla foglie), la copertura di sicurezza (a doghe che reggono il peso di un bambino: i requisiti di norma NF P90-308 come riferimento), la copertura automatica (a tapparella? a doghe scorrevoli: comodità e risparmio insieme), i pergolati e le serre intorno alla piscina (l'estensione dell'uso).
- **Applicazioni:** Piscine private, alberghiere, pubbliche in inverno.
- **Vantaggi:** La copertura è l'investimento con il ritorno più rapido della piscina: risparmia calore, pulizia e prodotti chimici.
- **Limiti e attenzioni:** La copertura manuale 'pesante' non si usa: la comodità decide l'uso reale.
- **Costi ed economia:** Costi: a bolle 200-600 €, telone invernale 300-800 €, copertura di sicurezza 2.000-5.000 €, automatica 5.000-12.000 €.
- **Caso tipico:** Piscina con copertura automatica usata quotidianamente: i consumi di riscaldamento ridotti del 60%, la pulizia dimezzata e la sicurezza garantita; la piscina identica con copertura 'manuale riposta in garage' ha consumato il doppio e richiede pulizie triple.
- **Normativa:** Normative di sicurezza piscine (i requisiti anti-annegamento per le coperture); specifiche produttori.
- **Nota di cantiere:** La regola: la copertura si compra con la piscina, non dopo: è parte dell'impianto.

### Filtrazione e disinfezione: l'acqua sempre pulita

**Categoria:** Impianto filtrazione · **Corso:** Piscine e centri wellness

L'impianto di trattamento dell'acqua è il cuore tecnico: la filtrazione (sabbia o cartuccia o diatomee) rimuove le particelle, la disinfezione (cloro, sale elettrolisi, ozono, UV) uccide i microbi, il bilancio idraulico (pompe, skimmer, bocchettoni) garantisce il ricircolo.

- **Tecnologia e criteri:** Sistema: il ricircolo completo ogni 4-6 ore (la norma per le piscine), gli skimmer (raccolgono l'acqua di superficie: il 70% dello sporco galleggia), i bocchettoni di fondo, i fari? le bocchette di mandata, i filtri a sabbia quarzosa (backwash ogni settimana, la sostituzione ogni 3-5 anni), le pompe con prevalenza adeguata (il filtro sporco aumenta la resistenza), la disinfezione: il cloro tradizionale, l'elettrolisi del sale (produce cloro in loco: meno manutenzione chimica), l'ozono + cloro residuo (le piscine di pregio).
- **Applicazioni:** Piscine private, pubbliche, hotel, centri sportivi.
- **Vantaggi:** L'impianto giusto fa l'acqua cristallina con 30 minuti di cura a settimana; quello sbagliato è un secondo lavoro.
- **Limiti e attenzioni:** La chimica mal gestita (pH fuori controllo) rovina il cloro, il rivestimento e gli occhi dei bagnanti.
- **Costi ed economia:** Costi: impianto completo di filtrazione per piscina privata 30-60 m²: 3.000-8.000 €; il locale tecnico va progettato accessibile e drenato.
- **Caso tipico:** Piscina con elettrolisi del sale e filtro oversize (dimensionato per 1,5 volte il volume): l'acqua resta cristallina con la metà dei controlli rispetto alla piscina 'standard' dello stesso costruttore.
- **Normativa:** Normativa piscine (igiene, ricircolo); specifiche dei produttori; la manutenzione programmata.
- **Nota di cantiere:** La regola: il filtro è il polmone, la pompa è il cuore, la chimica è il medico: se uno dei tre è sbagliato, l'acqua lo racconta subito.

### Le piscine pubbliche: normative e gestione

**Categoria:** Piscine pubbliche · **Corso:** Piscine e centri wellness

Le piscine aperte al pubblico (hotel incluse) seguono normative igieniche regionali: la qualità dell'acqua controllata (cloro residuo 1-1,5 mg/l tipico, pH 7,2-7,6), il ricircolo obbligatorio, i bagnini, gli accessi (i pediluvi, le docce obbligatorie), la sicurezza (i fondali segnalati, i salvagenti).

- **Tecnologia e criteri:** Requisiti: il bilancio chimico quotidiano (registrato), i controlli batteriologici periodici, i bagnini (un salvataggio? i bagnini certificati), gli accessi controllati (i percorsi obbligatori: doccia → pediluvio → vasca), i limiti di affollamento, le norme di sicurezza (i bordi vasca, i segnali di profondità); la gestione: il personale qualificato, la manutenzione programmata, la gestione dei picchi estivi.
- **Applicazioni:** Alberghi, centri sportivi, stabilimenti balneari, piscine comunali.
- **Vantaggi:** La piscina pubblica conforme evita sanzioni, chiusure e (soprattutto) i rischi per i bagnanti.
- **Limiti e attenzioni:** La burocrazia sanitaria è intensa: chi sottovaluta i controlli documentali rischia la sospensione.
- **Costi ed economia:** Costi: la gestione conforme aggiunge personale e controlli (il costo della sicurezza).
- **Caso tipico:** Stabilimento balneare con il controllo chimico digitale e i registri automatici: un'ispezione sanitaria è durata 20 minuti con esito perfetto; la struttura vicina con i registri cartacei 'a memoria' ha avuto una diffida.
- **Normativa:** Normativa regionale piscine (igiene); normativa antincendio; specifiche gestionali.
- **Nota di cantiere:** La cultura della piscina pubblica: l'acqua bella è il risultato di processi (controlli, personale, manutenzione) invisibili ai bagnanti.

### Il riscaldamento della piscina: estendere la stagione

**Categoria:** Riscaldamento · **Corso:** Piscine e centri wellness

L'acqua della piscina si scalda con scambiatori (caldaia, pompa di calore, solare), la copertura mantiene il calore (l'evaporazione è la prima perdita: la coperta riduce il 70% delle dispersioni), la stagione si estende da 3 a 6-9 mesi secondo il clima e il sistema.

- **Tecnologia e criteri:** Sistemi: la pompa di calore per piscine (il COP alto: produce 4-5 kW termici per 1 elettrico, funziona con aria dai 5-10 °C in su), gli scambiatori a piastre con la caldaia (istantanei ma costosi da usare), i pannelli solari termici (gratis dopo l'investimento, estendono la stagione), la copertura (a doghe, a bolle, automatica: è il miglior 'impianto' di riscaldamento), i deumidificatori per le piscine interne (l'umidità dell'aria interna condensa ovunque).
- **Applicazioni:** Piscine private, hotel, centri benessere, piscine coperte.
- **Vantaggi:** La copertura + la pompa di calore: la combinazione che estende la stagione di mesi a costi contenuti.
- **Limiti e attenzioni:** Il riscaldamento senza copertura è buttare soldi: l'acqua calda evapora e porta via il calore.
- **Costi ed economia:** Costi: pompa di calore piscina 1.500-4.000 €; copertura automatica 3.000-8.000 €; i consumi con la copertura: ridotti del 50-70%.
- **Caso tipico:** Piscina con pompa di calore e copertura a doghe: la stagione è passata da 4 a 7 mesi con consumi elettrici contenuti; la piscina identica del vicino senza copertura ha speso il doppio per scaldare 3 mesi.
- **Normativa:** Normativa sui refrigeranti (pompe di calore); specifiche produttori.
- **Nota di cantiere:** La gerarchia: prima la copertura, poi il riscaldamento: mai riscaldare senza coprire.

### La vasca da costruzione: struttura, tenuta, forma

**Categoria:** Vasche · **Corso:** Piscine e centri wellness

La piscina da costruzione è un serbatoio in calcestruzzo armato impermeabilizzato: la struttura (getto in opera o casseri a perdere), l'impermeabilizzazione (guaina PVC o ceramica? le guaine liquide o i rivestimenti), il rivestimento (mosaico, pastina, PVC armato), i sistemi di tenuta ai movimenti del terreno.

- **Tecnologia e criteri:** Costruzione: il getto in opera con casseri a perdere (i casseri in polistirofo che restano come isolante) o il prefabbricato (pannelli d'acciaio o casseri modulari), l'armatura ben coperta (i ferri vicini alla superficie marciscono e 'spuntano'), il sistema di impermeabilizzazione continua (la guaina PVC saldata a caldo sotto il rivestimento, i sistemi liquidi poliuretanici), la pendenza del fondo verso i bocchettoni (1,5-2% per piscine private), le scale e le sedute in getto.
- **Applicazioni:** Piscine private, alberghiere, pubbliche, centro benessere.
- **Vantaggi:** La vasca ben costruita dura 50 anni: le vasche 'economiche' fanno le prime crepe al terzo anno.
- **Limiti e attenzioni:** La tenuta è critica: una fessura non riparata consuma acqua, sale e riscalda? costa denaro e mina la struttura.
- **Costi ed economia:** Costi: piscina interrata in calcestruzzo 25-50 m²: 1.500-3.000 €/m² di vasca (finiture base); il rivestimento in mosaico: extra.
- **Caso tipico:** Piscina con guaina PVC sotto il mosaico e getto curato (curing prolungato): dopo 12 anni, zero perdite e zero infiltrazioni strutturali; la vasca gemella senza guaina ha rifatto l'impermeabilizzazione a 6 anni per alzature e infiltrazioni.
- **Normativa:** Normativa piscine (D.Lgs 116/1999 per le piscine? no: il riferimento è la normativa tecnica per piscine e le prescrizioni igieniche locali); UNI 13451? Riferimento: buona pratica e specifiche.
- **Nota di cantiere:** La prima legge della piscina: l'acqua è pesante (1.000 kg/m³) e sempre in movimento — la struttura e la tenuta devono rispettarla sempre.


## Robotica delle costruzioni

*Corso `ROBOTICA_EDILIZIA_PACK` — 27 voci*

### Computer vision e AI per la sicurezza di cantiere

**Categoria:** AI vision · **Corso:** Robotica delle costruzioni

Telecamere intelligenti che rilevano DPI mancanti, zone pericolo e vicinanza a mezzi.

- **Tecnologia e criteri:** Deep learning su stream video edge/cloud; alert in tempo reale; dashboard HSE.
- **Applicazioni:** Sicurezza cantieri, monitoraggio accessi, conteggio presenze, analisi near-miss.
- **Vantaggi:** Sicurezza proattiva 24/7; dati oggettivi per audit; riduzione incidenti dimostrata 20-40%.
- **Limiti e attenzioni:** Privacy (lavoratori sorvegliati); falsi positivi; qualità installazione.
- **Costi ed economia:** SaaS 2-15 €/camera/mese + hardware; progetto cantiere: 5-50k€.
- **Caso tipico:** Everguard.ai, SmartVid.io (acquisita da Oracle); adozione da general contractor USA.
- **Normativa:** GDPR + accordi sindacali; DPIA obbligatoria per videosorveglianza lavoratori.
- **Nota di cantiere:** Usare l'AI come coach, non come spia: comunicare lo scopo preventivo o il progetto fallisce culturalmente.

### Legatura e piegatura barre automatizzata

**Categoria:** Automazione armature · **Corso:** Robotica delle costruzioni

Macchine automatiche per piegare e legare reti e barre d'armatura.

- **Tecnologia e criteri:** Bender CNC a doppia testa, robot legatori a filo (tie-wire robots).
- **Applicazioni:** Centri di lavorazione armature, grandi opere, gabbie di pali e travi.
- **Vantaggi:** Produttività 5-10x; precisione di piega costante; meno malattie professionali.
- **Limiti e attenzioni:** Batch minimo per ripagare; programmazione CAD delle forme.
- **Costi ed economia:** Bender CNC: 100-500k€; robot legatore: 40-100k€.
- **Caso tipico:** Schnell, EVG, Progress: standard nelle fabbriche di prefabbricati.
- **Normativa:** Direttiva macchine; UNI EN 10080 acciai.
- **Nota di cantiere:** Chi armava a mano 3 addetti, con la macchina ne serve 1: riallocare la manodopera sulla posa.

### Layout robotizzato dal modello BIM

**Categoria:** BIM-to-Robot · **Corso:** Robotica delle costruzioni

Robot che tracciano e posano da soli layout di cantiere e componenti partendo dal BIM.

- **Tecnologia e criteri:** Import IFC/CSV; robot mobile con spray/penna/laser per segnare pareti e solai.
- **Applicazioni:** Tracciamento pareti, posa travi laser, verifica posa contro modello (scan-to-BIM).
- **Vantaggi:** Zero errori di misura; aggiornamento continuo as-built; meno rilievi manuali.
- **Limiti e attenzioni:** Richiede BIM affidabile e coordinato; superfici pulite e accessibili.
- **Costi ed economia:** Dusty Robotics FieldPrinter: noleggio/servizio 3-10k€/mese su cantieri grandi.
- **Caso tipico:** Dusty (USA) su cantieri di data center; HP SitePrint per layout elettrico/idraulico.
- **Normativa:** Nessuna; integra processo BIM ISO 19650.
- **Nota di cantiere:** Stampare il layout sul solaio prima delle partizioni cambia il cantiere: niente misure a nastro.

### Limiti, barriere e rischi della robotica edilizia

**Categoria:** Criticità · **Corso:** Robotica delle costruzioni

La verità critica: cosa NON funziona ancora nella costruzione robotizzata.

- **Tecnologia e criteri:** Analisi critica: tecnologia immatura, skill gap, normativa, cultura, economics.
- **Applicazioni:** Formazione del LLM al pensiero critico (spirito critico richiesto dall'utente).
- **Vantaggi:** Evita entusiasmi ingiustificati; guida investimenti razionali; riconosce il valore dell'artigianato.
- **Limiti e attenzioni:** Rischio di hype: molti progetti dimostrativi non scalano mai.
- **Costi ed economia:** Il fallimento di Katerra (1,6 miliardi $ bruciati) insegna: la tecnologia senza processo uccide.
- **Caso tipico:** Casi studio: Katerra, Arrivo, molte startup di stampa 3D scomparse dal 2018.
- **Normativa:** Nessuna; è cultura manageriale.
- **Nota di cantiere:** Regola per il LLM: la robotica vince sul RIPETITIVO e PERICOLOSO; l'umano vince sul VARIO e CREATIVO: il cantiere del futuro è ibrido.

### Gemello digitale di cantiere e opera

**Categoria:** Digital twin · **Corso:** Robotica delle costruzioni

Modello vivo dell'opera aggiornato in tempo reale da sensori, rilievi e avanzamento.

- **Tecnologia e criteri:** BIM + IoT + scan periodici (drone/laser scanner) + dashboard e simulazioni.
- **Applicazioni:** Cantieri complessi, gestione patrimonio, smart buildings, manutenzione predittiva.
- **Vantaggi:** Decisioni su dati reali; simulazioni prima di intervenire; consegna as-built garantita.
- **Limiti e attenzioni:** Costo integrazione; disciplina nel mantenere il modello aggiornato.
- **Costi ed economia:** Piattaforma digital twin: 20-200k€/anno + sensoristica.
- **Caso tipico:** Singapore Virtual Singapore; Heathrow; cantiere di Grand Paris Express.
- **Normativa:** ISO 19650; nessuna norma unica ancora.
- **Nota di cantiere:** Un digital twin abbandonato è peggio di niente: serve un data manager di cantiere dedicato.

### Drone LiDAR e rilievo boschi/infrastrutture

**Categoria:** Droni · **Corso:** Robotica delle costruzioni

Rilievo laser a scansione dal drone per vegetazione e geometrie complesse.

- **Tecnologia e criteri:** LiDAR UAV (Velodyne/Ouster) + IMU + GNSS; 100-400 pt/m2.
- **Applicazioni:** Rilievi in foreste, linee elettriche, frane, scavi e cave, modelli digitali di terreno.
- **Vantaggi:** Penetra la vegetazione (rimbalzi multipli); accuratezza 3-10 cm anche senza GCP.
- **Limiti e attenzioni:** Peso/batteria: 10-25 min volo; costo sensore; elaborazione specialistica.
- **Costi ed economia:** Sistema LiDAR drone: 40-150k€; costo rilievo bosco: 1-5 €/ha.
- **Caso tipico:** YellowScan, RIEGL miniVUX; adozione da ferrovie e TSO elettrici.
- **Normativa:** COME per fotogrammetria; sicurezza laser classe.
- **Nota di cantiere:** Il DTM da LiDAR è la base per la modellazione idraulica e geotecnica: investire qui ripaga in progettazione.

### Droni ispezione facciate, ponti e strutture alte

**Categoria:** Droni · **Corso:** Robotica delle costruzioni

Ispezione visiva e termografica di superfici verticali e orizzontali con sensori ottici/IR.

- **Tecnologia e criteri:** UAV con zoom ottico 30x, termocamera FLIR, luci; volo ravvicinato programmato.
- **Applicazioni:** Ispezioni di ponti, torri, pannelli fotovoltaici, gru, antenne, facciate vetro.
- **Vantaggi:** Niente piattaforme aeree o funi nella maggior parte dei casi; ispezione 5-10x più veloce.
- **Limiti e attenzioni:** Batteria 20-40 min; normativa volo in area urbana; attesa condizioni meteo.
- **Costi ed economia:** Servizio ispezione: 300-1.500 €/giornata; risparmio 40-70% vs ponteggio.
- **Caso tipico:** CyberHawk, Skydio per ponti; ispezioni FV termografiche con DJI M300.
- **Normativa:** Regolamento droni UE specific/SORA; ENAC; coordinamento con Ente gestore infrastruttura.
- **Nota di cantiere:** Documentare ogni anomalia con foto georiferita: la relazione diventa base di computo per manutenzione.

### Droni logistica di cantiere

**Categoria:** Droni · **Corso:** Robotica delle costruzioni

Consegna di piccoli materiali, strumenti e campioni via drone.

- **Tecnologia e criteri:** UAV cargo con winch/cassetti; percorso pre-programmato; carico 2-20 kg.
- **Applicazioni:** Cantieri estesi, isole, aree montane, consegna attrezzature urgenti tra gru e baraccamenti.
- **Vantaggi:** Taglio dei tempi di attesa; nessun mezzo di superficie; sicurezza del personale.
- **Limiti e attenzioni:** Autonomia limitata con carico; regolamento di volo; costo/km ancora alto.
- **Costi ed economia:** Drone cargo: 20-200k€; consegna 5-30 € vs 50-150 € di mezzo+personale.
- **Caso tipico:** Wing (Alphabet) per consegne; EHang cargo; test in cantieri minerari.
- **Normativa:** Regolamento droni UE; assicurazioni; certificazione classe specifica.
- **Nota di cantiere:** Oggi conviene per emergenze e siti remoti; la scala arriverà con regolamentazione U-space.

### Droni rilievo fotogrammetrico

**Categoria:** Droni · **Corso:** Robotica delle costruzioni

Rilievo 3D da drone con foto georiferite per mappatura di cantiere e patrimonio.

- **Tecnologia e criteri:** UAV multirotore/fixed-wing + fotogrammetria SfM (Structure from Motion) + GCP o PPK.
- **Applicazioni:** Rilievo di terreni, monitoraggio avanzamento lavori, patrimonio architettonico, lastrico solare.
- **Vantaggi:** Rilievo 10-50 ha/giorno; nessun ponteggio; ortofoto e nuvole di punti cm-level.
- **Limiti e attenzioni:** Dipendenza da meteo; autorizzazioni ENAC; non penetra la vegetazione fitta.
- **Costi ed economia:** Drone professionale 5-30k€; software elaborazione 2-10k€/anno; costo rilievo: 0,5-5 €/ha vs rilievo tradizionale 10x.
- **Caso tipico:** DJI Phantom/M300 + Pix4D/Agisoft; usati da tutti i general contractor.
- **Normativa:** Regolamento UE 2019/945 (droni), ENAC; privacy per immagini.
- **Nota di cantiere:** Ogni rilievo ripetibile nel tempo crea il 'diario fotografico metrico' del cantiere: oro in caso di contenzioso.

### Economia e ROI della robotica edilizia

**Categoria:** Economia · **Corso:** Robotica delle costruzioni

Quando la robotica ripaga: il quadro economico realistico.

- **Tecnologia e criteri:** Analisi costo-orario robotico vs manodopera; produttività; qualità; sicurezza.
- **Applicazioni:** Decisione investimenti di imprese, direzioni lavori, committenti.
- **Vantaggi:** Sui grandi volumi e lavori ripetitivi il ROI è 1-3 anni; su piccoli lavori tradizionali non ripaga mai.
- **Limiti e attenzioni:** Macchine sottoutilizzate sono perdita; mancanza di manutentori; obsolescenza software.
- **Costi ed economia:** Robot muratore: rientro 2-4 anni a >15.000 m2 di facciata; drone rilievo: rientro immediato (<3 mesi).
- **Caso tipico:** Dati da McKinsey Global Institute e da casi FBR/Construction Robotics pubblicati.
- **Normativa:** Nessuna; è analisi gestionale.
- **Nota di cantiere:** Criterio pratico: comprare robot dove c'è (1) ripetitività, (2) volume, (3) carenza di manodopera qualificata.

### Escavatori e mezzi pesanti teleoperati

**Categoria:** Macchine teleoperate · **Corso:** Robotica delle costruzioni

Buldozer, escavatori e dumper comandati a distanza per cantieri pericolosi.

- **Tecnologia e criteri:** Telecomando radio/5G + telecamere + LiDAR; oppure driver-assist (semi-autonomia).
- **Applicazioni:** Frane, discariche, cave, cantieri con rischio instabilità, ambiente radioattivo.
- **Vantaggi:** Eliminazione del rischio uomo-macchina; lavoro continuo su più turni.
- **Limiti e attenzioni:** Latenza e banda critiche; percezione ridotta rispetto alla cabina.
- **Costi ed economia:** Kit retrofit teleoperato: 30-150k€; macchina nuova autonoma: +20-40%.
- **Caso tipico:** Komatsu/Hitachi autonomous trucks nelle miniere (Rio Tinto); teleoperazione nelle centrali nucleari (JTEKT).
- **Normativa:** Direttiva macchine + UNI per macchine da cantiere (EN 474).
- **Nota di cantiere:** La teleoperazione è il gradino prima dell'autonomia: investire in reti 5G private del cantiere.

### ROS e middleware robotici in edilizia

**Categoria:** Middleware · **Corso:** Robotica delle costruzioni

Piattaforme software open per comandare robot eterogenei in cantiere.

- **Tecnologia e criteri:** ROS/ROS2, MQTT, OPC-UA; integrazione flotte miste (droni+mezzi+sensori).
- **Applicazioni:** Cantieri pilota, ricerca, automazione impianti di produzione prefabbricati.
- **Vantaggi:** Standard aperto; enorme ecosistema; riuso di algoritmi già sviluppati.
- **Limiti e attenzioni:** Richiede competenze software in azienda; affidabilità da industrializzare.
- **Costi ed economia:** Software gratuito; competenze: 60-120k€/anno di un ingegnere robotico.
- **Caso tipico:** ROS-Industrial; progetti Horizon Europe per costruzione robotizzata.
- **Normativa:** Nessuna; buone pratiche open source.
- **Nota di cantiere:** Per un'impresa edile media: iniziare da MQTT+OPC-UA per i sensori, ROS solo se si sviluppa robotica propria.

### Prefabbricazione robotizzata (off-site, DfMA)

**Categoria:** Off-site automation · **Corso:** Robotica delle costruzioni

Fabbriche con robot saldatori, carroponte CNC e linee automatizzate per componenti edilizi.

- **Tecnologia e criteri:** Saldatura robotica, taglio CNC, montaggio automatico pannelli 3D, linee di produzione.
- **Applicazioni:** Strutture in acciaio, facciate unitizzate, pannelli parete, bagni monoblocco, moduli completi.
- **Vantaggi:** Qualità industriale; cantiere 30-70% più veloce; meno sprechi e meno personale in quota.
- **Limiti e attenzioni:** Investimento impianto pesante; progettazione BIM obbligatoria; trasporto dei moduli.
- **Costi ed economia:** Impianto prefabbricazione: 5-50M€; risparmio cantiere 10-20% del totale.
- **Caso tipico:** Katerra (fallimento da studiare), Kleusberg, Lindbäcks, Sekisui House; bagni monoblocco Caleffi.
- **Normativa:** Marcatura CE componenti; EN 1090 per acciaio; DfMA come metodo progettuale.
- **Nota di cantiere:** La prefabbricazione robotizzata è la robotica che FUNZIONA oggi: chi progetta per DfMA vince su tempi e qualità.

### Robot carotatura e taglio

**Categoria:** Robot demolizione · **Corso:** Robotica delle costruzioni

Carotatrici e seghe robotizzate per tagli di precisione in cls e roccia.

- **Tecnologia e criteri:** Utensili diamantati motorizzati, guida meccanica o robotica.
- **Applicazioni:** Fori per impianti, tagli per rinforzi, aperture, demolizioni controllate.
- **Vantaggi:** Precisione millimetrica; nessuna fatica per l'operatore; continuità di lavoro.
- **Limiti e attenzioni:** Polvere e acqua di raffreddamento da gestire; consumo utensili diamantati.
- **Costi ed economia:** Carotatrice robotizzata 15-60k€; utensile diamantato 50-300 €/m di taglio.
- **Caso tipico:** Hilti, Tyrolit robot systems per tagli su dighe e ponti.
- **Normativa:** Direttiva macchine; ATEX per ambienti con polveri esplosive.
- **Nota di cantiere:** Il taglio robotizzato evita microfessurazioni: fondamentale prima di incollaggi FRP.

### Robot demolizione telecomandati (Brokk)

**Categoria:** Robot demolizione · **Corso:** Robotica delle costruzioni

Mini escavatori demolitori telecomandati con frantumi e bracci idraulici.

- **Tecnologia e criteri:** Elettrici/diesel, telecomando radio, attrezzature multipla (frantumo, pinza, fresa).
- **Applicazioni:** Demolizioni interne, ambienti confinati, centrali nucleari, tunnel, cantieri urbani.
- **Vantaggi:** Operatore lontano dal pericolo; accesso a spazi stretti; minor vibrazione e polvere.
- **Limiti e attenzioni:** Portata e raggio limitati; costo orario elevato; serve manutentore formato.
- **Costi ed economia:** Noleggio 1.500-4.000 €/giorno; acquisto 60-300k€.
- **Caso tipico:** Brokk, Husqvarna DXR: usati a Chernobyl, metropolitane, demolizioni ospedaliere.
- **Normativa:** Direttiva macchine; valutazione rumore/polvere; amianto: procedure D.Lgs 81/08.
- **Nota di cantiere:** Per demolizioni selezionate e interne è quasi sempre più sicuro e spesso più economico dell'escavatore grande.

### Hadrian X (FBR)

**Categoria:** Robot muratori · **Corso:** Robotica delle costruzioni

Robot mobile su cingoli che posa blocchi forati adesivi (no malta) interi muri dall'esterno.

- **Tecnologia e criteri:** Pala caricatrice + testa posa blocchi + colla poliuretanica strutturale; precisione sub-millimetrica.
- **Applicazioni:** Villette, villette a schiera, muri di recinzione e contenimento.
- **Vantaggi:** Posa 200+ blocchi/ora anche di notte; opera a distanza di sicurezza; nessuna impalcatura.
- **Limiti e attenzioni:** Limitato a geometrie compatibili con i blocchi; ecosistema blocchi dedicati.
- **Costi ed economia:** Macchina multi-milione $; contratti licensing/licenza per costruttori.
- **Caso tipico:** FBR (Fastbrick Robotics) in Australia/USA; case pilota in Florida.
- **Normativa:** Certificazioni locali su colla e blocchi; verifica statica a cura del progettista.
- **Nota di cantiere:** Segnale del futuro: la muratura diventa posa di 'lego industriali', il progettista modella a blocchi.

### Robot posa piastrelle e pavimenti

**Categoria:** Robot muratori · **Corso:** Robotica delle costruzioni

Robot semi-automatici per la posa di piastrelle grandi formato e levigatura.

- **Tecnologia e criteri:** Ventose + braccio + laser leveling; applicazione colla a pettine automatica.
- **Applicazioni:** Aeroporti, centri commerciali, grandi pavimentazioni continue.
- **Vantaggi:** Produttività 3-5x; qualità di planarità costante; riduzione malattie muscolo-scheletriche.
- **Limiti e attenzioni:** Setup e messa a punto iniziale lenti; non gestisce tagli e particolari.
- **Costi ed economia:** Robot TileRobot/SAM: 150-400k€; rientro su >5.000 m2.
- **Caso tipico:** Robot della Università di Monash (Hadrian 'piastrellista'); Tile laying robots in Cina.
- **Normativa:** Direttiva macchine; accordi collettivi su sicurezza in cantiere.
- **Nota di cantiere:** Su grandi superfici il robot conviene; su bagni e cucine resta l'artigiano.

### SAM100 (Semi-Automated Mason)

**Categoria:** Robot muratori · **Corso:** Robotica delle costruzioni

Robot collaborativo che posa mattoni pieni/forati con malta, con operaio alimentatore.

- **Tecnologia e criteri:** Braccio robotico 6 assi + nastro alimentazione; posizionamento laser 1 mm.
- **Applicazioni:** Facciate in laterizio, murature di tamponamento, rivestimenti a faccia vista.
- **Vantaggi:** Produttività 3.000+ mattoni/turno (6 volte l'umano); qualità costante del giunto.
- **Limiti e attenzioni:** Serve operaio dedicato all'alimentazione; non posa angoli e aperture (resta manuale).
- **Costi ed economia:** Acquisto 400-600k$; rientro indicativo 3-5 anni su grandi cantieri di facciata.
- **Caso tipico:** Construction Robotics SAM100: usato su cantieri Walmart, scuole USA.
- **Normativa:** NESSUNA norma robotica specifica; rispetto Direttiva macchine 2006/42/CE.
- **Nota di cantiere:** Adatto a grandi superfici rettilinee: su piccoli cantieri residenziali non ripaga.

### Robot collettivi e modulari (TERMES, swarms)

**Categoria:** Robot swarm · **Corso:** Robotica delle costruzioni

Gruppi di piccoli robot autonomi che costruiscono cooperando, ispirati alle termiti.

- **Tecnologia e criteri:** Swarm robotics; comunicazione stigmergica; moduli di costruzione standard.
- **Applicazioni:** Ricerca, ambienti estremi, costruzione spaziale, strutture di emergenza.
- **Vantaggi:** Robustezza (nessun singolo punto critico); parallelizzazione; accesso a zone pericolose.
- **Limiti e attenzioni:** TRL basso (3-5); scalabilità non dimostrata in edilizia reale.
- **Costi ed economia:** Prototipi accademici; costo sistema sperimentale 50-200k€.
- **Caso tipico:** TERMES (Harvard), swarms ETH Zurich; NASA JPL per habitat lunari.
- **Normativa:** Nessuna normativa; etica e sicurezza collettive in studio.
- **Nota di cantiere:** Da monitorare: è la direzione di lungo periodo, non una tecnologia da cantiere 2026.

### Normativa sicurezza robotica in cantiere

**Categoria:** Sicurezza robotica · **Corso:** Robotica delle costruzioni

Come rendere conforme un cantiere con robot e macchine automatizzate.

- **Tecnologia e criteri:** Direttiva macchine 2006/42/CE; ISO 10218 (robot industriali); ISO/TS 15066 (cobot); UNI EN 474 (macchine da cantiere).
- **Applicazioni:** Qualsiasi adozione robotica: dal robot demolitore al cobot muratore.
- **Vantaggi:** Quadro chiaro di responsabilità; valutazione rischi aggiornata; LAVORATORI FORMATI.
- **Limiti e attenzioni:** Normativa frammentata; regolamenti nazionali da armonizzare; interpretazioni locali.
- **Costi ed economia:** Costo compliance: valutazione+formazione 5-30k€ per cantiere robotizzato.
- **Caso tipico:** Cantieri nord-europei come riferimento; protocolli ENEL/Webuild per robot in opera.
- **Normativa:** D.Lgs 81/08 + allegato V macchine; Direttiva macchine (nuova 2023/1230).
- **Nota di cantiere:** Regola d'oro: il robot entra in cantiere solo dopo la valutazione del RSPP e con percorso pedonale segregato.

### Inchiostri (mix) per stampa 3D

**Categoria:** Stampa 3D edilizia · **Corso:** Robotica delle costruzioni

I mix stampabili: requisiti di pompa-bilità, apertura di staglio, costruibilità (buildability).

- **Tecnologia e criteri:** Cls con aggregati fini, acceleratori, fibrorinforzo; viscosità regolata da additivi cellulosa/argille.
- **Applicazioni:** Qualsiasi progetto di stampa 3D.
- **Vantaggi:** Possibilità di mix custom (leggeri, isolanti, fibrati); integrazione di fibre per anti-sismico.
- **Limiti e attenzioni:** Catena di fornitura e certificazione del mix ancora limitata; richiede laboratorio di dosaggio.
- **Costi ed economia:** Mix stampabile: +10-30% sul cls ordinario; sviluppo mix dedicato: 5-20k€.
- **Caso tipico:** Mix di HeidelbergCement, CEMEX D.fab, mix CNR per ENEA.
- **Normativa:** Prove di costruibilità e reologia (EN 12350 adattate); nessuna norma armonizzata specifica.
- **Nota di cantiere:** Testare sempre il mix con prova di crollo a torre (slump flow a torre) prima del cantiere.

### Stampa 3D case intere (Icon Vulcan)

**Categoria:** Stampa 3D edilizia · **Corso:** Robotica delle costruzioni

Sistema mobile di stampa intero edificio in ~7-14 giorni.

- **Tecnologia e criteri:** Extrusion su binari/scala mobile; mix proprietario 'Lavacrete'.
- **Applicazioni:** Housing sociale, emergency housing, edilizia residenziale USA.
- **Vantaggi:** Tempo di cantiere drasticamente ridotto; 2-4 addetti per casa; costo materiale basso.
- **Limiti e attenzioni:** Geometrie a parete semplice; reti impianti da progettare prima (canaline integrate).
- **Costi ed economia:** Casa stampata: 4.000-10.000 € in materiali + macchina; totale 30-50% sotto mercato USA.
- **Caso tipico:** ICON: comunità in Texas (East 17th), progetti NASA per habitat lunari.
- **Normativa:** Normativa edilizia locale, ASTM in corso; codici anti-sismici da adattare.
- **Nota di cantiere:** Prevedere nel modello BIM la posa di canaline per impianti prima della stampa delle pareti.

### Stampa 3D con terra cruda e geopolimeri

**Categoria:** Stampa 3D edilizia · **Corso:** Robotica delle costruzioni

Stampa con materiali di terra locali, rifiuti industriali attivati, geopolimeri a basso carbonio.

- **Tecnologia e criteri:** Leganti geopolimerici (metacaolino, scorie attivate) o terra stabilizzata; estrusione a bassa energia.
- **Applicazioni:** Architetture sostenibili, padiglioni, edilizia rurale, esteri emergenti.
- **Vantaggi:** Impronta carbonica molto bassa; uso di rifiuti e terra locale; niente cemento.
- **Limiti e attenzioni:** Resistenza meccanica inferiore al cls; vulnerabilità all'acqua senza protezioni; ricerca ancora attiva.
- **Costi ed economia:** Materiale 5-20 €/m3 (terra locale) contro 60-120 €/m3 di cls; macchina COBOD/wasp da 50-200k€.
- **Caso tipico:** TECLA (Mario Cucinella + WASP); case in India/Africa con stampanti low cost.
- **Normativa:** Linee guida sperimentali; per opere strutturali serve validazione accademica e prove su campioni.
- **Nota di cantiere:** Ideale per strutture non portanti, recinzioni, padiglioni e murature di riempimento verificate sismicamente.

### Stampa 3D di metalli (WAAM e SLM)

**Categoria:** Stampa 3D edilizia · **Corso:** Robotica delle costruzioni

Prototipi e componenti strutturali in acciaio/alluminio stampati in 3D.

- **Tecnologia e criteri:** Wire Arc Additive Manufacturing (WAAM) e Selective Laser Melting (SLM).
- **Applicazioni:** Nodi strutturali complessi, ponti pedonali, architetture parametriche.
- **Vantaggi:** Forme impossibili con lamiere; personalizzazione di massa; spreco quasi nullo di metallo.
- **Limiti e attenzioni:** Costo orario macchina elevato; dimensioni limitate; verifica strutturale su-sito complessa.
- **Costi ed economia:** WAAM 100-500 €/kg; SLM 300-1.000 €/kg; competitivo solo per forme estreme o prototipi.
- **Caso tipico:** Ponte MX3D in acciaio ad Amsterdam; nodi per Renzo Piano Building Workshop.
- **Normativa:** EN ISO/ASTM 52900; verifica a fatica e saldabilità secondo Eurocodici.
- **Nota di cantiere:** Per il progettista: pensare al metallo stampato come getto metallico, non come laminato.

### Stampante 3D per calcestruzzo (extrusion)

**Categoria:** Stampa 3D edilizia · **Corso:** Robotica delle costruzioni

Stampanti a braccio/portalino che estrudono strati di calcestruzzo rapido per pareti portanti.

- **Tecnologia e criteri:** Extrusion layer-by-layer; mix accelerati (additivi acceleratori, spesso geopolimeri); controllo CNC 3-6 assi.
- **Applicazioni:** Villette monopiano, case popolari, uffici, pareti e murature in loco.
- **Vantaggi:** Riduzione manodopera (-50/-80% sulla muratura), velocità (10-100 m2/giorno), minor spreco, geometrie libere.
- **Limiti e attenzioni:** Richiede progettazione ad hoc (DfAM); superfici grezze da rifinire; normativa ancora in sviluppo; capital cost elevato.
- **Costi ed economia:** Macchina 300k-1,5M€; costo parete stampata 30-60% in meno rispetto a muratura tradizionale su grandi volumi.
- **Caso tipico:** COBOD BOD2 (usata da GE, PERI, HeidelbergCement); ICON Vulcan; Apis Cor; CyBe; WASP Crane.
- **Normativa:** EILCO/ISO/ASTM in definizione; in Italia CNR-DT 125 (prime linee guida stampa 3D).
- **Nota di cantiere:** La stampa 3D sostituisce la muratura, NON la struttura: la platea, le travi e la copertura restano tradizionali o prefabbricate.

### Stazioni totali robotiche e laser tracker

**Categoria:** Strumentazione · **Corso:** Robotica delle costruzioni

Strumenti geodetici a guida automatica per il posizionamento ad alta precisione.

- **Tecnologia e criteri:** Stazione totale motorizzata (TS), laser tracker, livelli digitali; prismi robotici.
- **Applicazioni:** Posa strutture in acciaio, monitoraggi, piloni, binari, prefabbricati di precisione.
- **Vantaggi:** Precisione 1-2 mm su centinaia di metri; un solo operatore; misure continue.
- **Limiti e attenzioni:** Vista libera richiesta; umidità/polvere degradano; costo strumento.
- **Costi ed economia:** Stazione totale robotica: 15-50k€; laser tracker: 60-150k€.
- **Caso tipico:** Leica TS16, Trimble S7; standard nei cantieri di ponte e grattacielo.
- **Normativa:** UNI geodesia; tracciati secondo norma (es. UNI 7317).
- **Nota di cantiere:** Fondamentale abbinare il rilievo continuo al modello: la stazione totale 'guida' la posa come un GPS del cantiere.

### Esoscheletri per operai

**Categoria:** Wearable · **Corso:** Robotica delle costruzioni

Strutture indossabili attive (motore) o passive (molle) che aiutano a sollevare e tenere posizioni.

- **Tecnologia e criteri:** Motori elettrici/batteria o sistemi passivi a elastomeri; sensori IMU.
- **Applicazioni:** Movimentazione sacchi, posa in quota, sbattimento prolungato, logistica magazzino.
- **Vantaggi:** Riduzione affaticamento 30-60%; minor infortuni muscolo-scheletrici (50% degli infortuni edili).
- **Limiti e attenzioni:** Peso 3-8 kg; caldo in estate; adozione culturale; manutenzione batterie.
- **Costi ed economia:** Esoscheletro passivo 3-10k€; attivo 20-50k€; rientro su riduzione infortuni e assenze.
- **Caso tipico:** SuitX/Dephy; esoscheletri usati da Ford, Delta, in prova da Webuild sui cantieri.
- **Normativa:** Direttiva DPI; valutazione ergonomica D.Lgs 81/08 allegato XXXIII.
- **Nota di cantiere:** Il miglior esoscheletro è quello che l'operaio accetta: coinvolgerlo nella scelta del modello.


## Prevenzione incendi e accessibilità

*Corso `SICUREZZA_ANTINCENDIO_ACCESSIBILITA_PACK` — 9 voci*

### L'accessibilità: superamento delle barriere architettoniche

**Categoria:** Accessibilità · **Corso:** Prevenzione incendi e accessibilità

L'accessibilità è diritto (D.Lgs 80/1992): gli edifici pubblici e privati aperti al pubblico devono essere fruibili da disabili; il riferimento tecnico è il DM 236/1989 (requisiti minimi) aggiornato dalle norme UNI e dalle leggi regionali: percorsi senza barriere, servizi igienici accessibili, ascensori o piattaforme, segnaletica e percorsi tattili.

- **Tecnologia e criteri:** Requisiti chiave: pendenze dei percorsi esterni (max 5% ideali, rampe con riposi oltre certe lunghezze), larghezze minime di passaggio (90 cm), servizi igienici accessibili (spazio di manovra 150×150), contrassegni tattili e visivi, posti auto riservati; in ristrutturazione l'obbligo di abbattimento barriere vale per interventi rilevanti; i lavori di messa in sicurezza/accessibilità godono di detrazioni fiscali dedicate (es. 75% secondo normativa vigente, da verificare).
- **Applicazioni:** Edifici pubblici, commerciali, uffici, abitazioni di disabili, ristrutturazioni con detrazioni.
- **Vantaggi:** L'accessibilità bene fatta serve a tutti: genitori con passeggini, anziani, corrieri: il 'disegno per tutti' migliora l'edilizia per tutti.
- **Limiti e attenzioni:** Gli adempimenti fatti 'al limite' per spuntare la casella creano percorsi umilianti e inefficaci: il superamento barriere è progetto, non pezza.
- **Costi ed economia:** Costo servizio igienico accessibile in più: 2.000-5.000 €; piattaforma elevatrice esterna: 8.000-20.000 €; detrazione 75% su interventi dedicati (verificare normativa corrente).
- **Caso tipico:** Farmacia ristrutturata con ingresso a gradini: l'abbattimento barriere con rampa e portello automatico ha aperto il mercato a carrozzine e passeggini; il titolare dichiara clientela aumentata in modo percettibile già dopo pochi mesi.
- **Normativa:** D.Lgs 80/1992; DM 236/1989; legge 13/1989; norme UNI (pendenze, segnaletica).
- **Nota di cantiere:** Prima verifica di progetto: 'una persona in carrozzina può entrare, girare nei locali, usare i servizi e uscire in autonomia?' — il percorso completo, non il singolo dettaglio.

### Ascensori e piattaforme elevatrici: obblighi e scelte

**Categoria:** Ascensori · **Corso:** Prevenzione incendi e accessibilità

L'abbattimento barriere verticali si fa con ascensori (obbligatori sopra certi piani/attività), piattaforme elevatrici (per dislivelli ridotti e carichi limitati) e montacarichi; gli impianti sono sottoposti a regole precise di installazione, collaudo, manutenzione (DPR 162/1999) e verifiche periodiche.

- **Tecnologia e criteri:** Scelta: ascensore (persone, portata 320-1.000 kg, vano con misure minime accessibili), piattaforma elevatrice (dislivello fino a 2-3 piani tipici, portata 200-400 kg, soluzione per esistenti), montascale a poltroncina (abitazioni); adempimenti: progetto, installazione da ditta autorizzata, collaudo, verbale d'installazione, contratto manutenzione, libretto impianto, verifiche periodiche (annuali di manutenzione regolare); in condominio l'installazione per accessibilità è favorita dalla legge (maggioranze ridotte secondo riforma 2012).
- **Applicazioni:** Edifici pubblici e privati con più piani, ristrutturazioni, condomini.
- **Vantaggi:** L'impianto verticale trasforma la fruibilità dell'edificio: per anziani e disabili è la differenza tra casa e prigione.
- **Limiti e attenzioni:** In edifici storici lo spesso vano ascensore è impossibile: le piattaforme esterne sono spesso la soluzione, con il vincolo paesaggistico da gestire.
- **Costi ed economia:** Costo ascensore nuovo: 18.000-45.000 €; piattaforma: 8.000-20.000 €; manutenzione: 1.000-2.500 €/anno; montascale: 3.000-8.000 €.
- **Caso tipico:** Condominio con anziani al terzo piano: installata piattaforma esterna con detrazione e maggioranza condominiale ridotta: costo netto rientrato in parte dalle detrazioni e i residenti hanno recuperato autonomia.
- **Normativa:** DPR 162/1999; L. 220/2012 (installazioni agevolate in condominio); DM 236/1989.
- **Nota di cantiere:** Regole: mai sottodimensionare la cabina (sedia a rotelle + accompagnatore), mai saltare il contratto di manutenzione (è obbligo), mai installare senza i verbali di collaudo (responsabilità penale in caso di incidente).

### Gli incendi edilizi: lezioni dai casi reali

**Categoria:** Casi incendio · **Corso:** Prevenzione incendi e accessibilità

L'analisi degli incendi reali insegna più di ogni norma: i pattern ricorrenti in edilizia: incendi durante i lavori (saldature, flessibili, stufe da cantiere), sottodimensionamento o mancata manutenzione degli impianti elettrici, fumi letali attraverso gli impianti di climatizzazione non settati, materiali di finitura non conformi, vie di esodo bloccate da materiali.

- **Tecnologia e criteri:** Pattern e contromisure: lavori a caldo (permesso di lavoro, vigilanza post-lavoro 60 minuti), manutenzione impianti elettrici (termografie periodiche), canalizzazioni con serrafiamma, materiali con reazione al fuoco certificata, esodi sempre liberi (ispezione quotidiana); l'assicurazione all-risk cantiere copre i danni diretti ma non la responsabilità penale.
- **Applicazioni:** Cantieri, edifici esistenti, manutenzione programmata, gestione immobili.
- **Vantaggi:** Le lezioni dei casi reali sono concrete: 'è successo davvero, così' è più efficace di ogni astratto nella formazione dei cantieri.
- **Limiti e attenzioni:** Ogni incendio ha cause note e prevenibili: l'incidente 'imprevedibile' è quasi sempre una catena di scelte trascurabili.
- **Costi ed economia:** Costo delle contromisure: marginale (procedura, controllo, formazione); il costo medio di un incendio edilizio: da decine di migliaia a milioni di euro più eventuali responsabilità penali.
- **Caso tipico:** Incendio in un cantiere di ristrutturazione causato da flessibile lasciato acceso su pannelli isolanti: danno totale 700.000 € e 2 persone intossicate; la vigilanza post-lavoro di 30 minuti (costo: nulla) avrebbe spento il principio.
- **Normativa:** Relazioni VVF e studi settoriali; normativa vigente.
- **Nota di cantiere:** Da insegnare al LLM: la sicurezza antincendio è una CULTURA quotidiana, non una pratica da esibire in fase di collaudo.

### La compartimentazione: limitare la propagazione

**Categoria:** Compartimentazione · **Corso:** Prevenzione incendi e accessibilità

La compartimentazione divide l'edificio in setti con resistenza al fuoco certificata (pareti, solai, porte tagliafuoco REI 60/90/120): obiettivo è contenere l'incendio nel compartimento d'origine, proteggere le vie di esodo e dare tempo ai soccorsi.

- **Tecnologia e criteri:** Elementi: setti con elementi costruttivi certificati (curve di decadimento, non solo 'cartongesso ignifugo' generico), porte tagliafuoco con certificazione UNI e chiusura automatica o semiautomatica dove richiesta, giunzioni e attraversamenti sigillati (mastici intumescenti), intonaci e rivestimenti protettivi su strutture portanti (acciaio: intumescenti o vernici al silicato); il progetto elenca le resistenze REI per ogni elemento e il cartello di certificazione va conservato.
- **Applicazioni:** Nuove costruzioni, ristrutturazioni di edifici esistenti, adeguamenti di locali con pubblico.
- **Vantaggi:** La compartimentazione funziona: negli incendi edilizi i compartimenti corretti hanno salvato intere ali di edificio mentre il compartimento d'origine bruciava.
- **Limiti e attenzioni:** Un solo attraversamento non sigillato (cavo elettrico, tubo) annulla un settore intero: la qualità sta nei dettagli di posa.
- **Costi ed economia:** Costo porte tagliafuoco: 400-1.500 €; mastici e sigillature intumescenti: poche decine di euro a punto; il costo in fase di costruzione è una frazione del rifacimento.
- **Caso tipico:** Verifica post-incendio in ufficio: il settore REI 90 ha contenuto il fuoco in due stanze; la porta tagliafuoco del corridoio (chiusa automaticamente) ha salvato l'ala opposta: danno da 180.000 € invece che all'edificio intero.
- **Normativa:** D.M. 03/08/2015; UNI EN 13501-2 (classi REI); normativa prodotti da costruzione CPR (UE 305/2011).
- **Nota di cantiere:** La domanda da fare al LLM: 'quali sono i setti REI di questo edificio e dove passano i servizi attraverso di essi?' — ogni passaggio è un punto critico.

### I mezzi di estinzione: estintori, idranti, naspi

**Categoria:** Estinzione · **Corso:** Prevenzione incendi e accessibilità

I mezzi di estinzione manuali sono la prima risposta: estintori a polvere (universali, sporcano), a CO2 (locali elettrici, non lasciano residui), idranti a parete con naspo (portata e getto minimo per attività), impianti a sprinkler dove richiesti o scelti; dimensionamento e posizionamento per attività da tabelle del DM.

- **Tecnologia e criteri:** Regole: estintore ogni 200 m² e ogni 25 m di percorso tipici per attività, in posizione visibile e accessibile (max 1,5 m da terra), revisione annuale (etichetta), idranti con pressione minima verificata (prova di erogazione), i materiali edili incombustibili riducono il carico d'incendio e possono alleggerire i requisiti; formazione del personale all'uso (obbligo datore di lavoro).
- **Applicazioni:** Ogni edificio produttivo e commerciale, cantieri grandi, magazzini.
- **Vantaggi:** L'estintore usato nei primi minuti spegne il 90% degli incendi che altrimenti diventano grandi (statistiche VVF): posizionato giusto e il personale formato, è il presidio più efficace in assoluto.
- **Limiti e attenzioni:** L'estintore 'solo a norma sulla carta' (revisione scaduta, sepolto dietro scaffali) è carta straccia nel momento del bisogno.
- **Costi ed economia:** Costo estintore: 40-120 € (revisione 15-30 €/anno); idrante completo: 300-800 €; formazione personale: 30-80 €/persona.
- **Caso tipico:** Incendio in officina: un dipendente formato ha spento un principio d'incendio al banco con l'estintore a 4 m di distanza in 40 secondi; danno limitato a 2.000 € invece che all'intera attività.
- **Normativa:** D.M. 03/08/2015 (tabelle presidi); UNI 45 e UNI EN 3 (estintori); D.Lgs 81/2008 (formazione).
- **Nota di cantiere:** Checklist cantiere/azienda: estintori presenti, accessibili, revisionati; idranti provati; personale formato — tre spunte ogni 6 mesi.

### Gestione dell'emergenza: PEI, addestramento, evacuazione

**Categoria:** Gestione emergenza · **Corso:** Prevenzione incendi e accessibilità

La gestione dell'emergenza è la parte 'umana' della prevenzione: Piano di Emergenza Interno (PEI) con procedure, ruoli (addetti alle emergenze e prime evacuazione), planimetrie con percorsi e presidi, addestramento annuale degli occupanti, prove di evacuazione (tempo massimo tipico 5 minuti per edifici con pubblico secondo norma).

- **Tecnologia e criteri:** Contenuti PEI: scenari di rischio, numeri di emergenza, procedure per incendio/emergenza, planimetrie esodo, nominativi addetti, manutenzione presidi; l'addestramento: corsi base e aggiornamento (legge 81/08), prove di evacuazione con cronometraggio e verbale; la gestione delle merci pericolose (scheda di sicurezza, stoccaggi).
- **Applicazioni:** Uffici, scuole, industrie, centri commerciali, edifici con pubblico.
- **Vantaggi:** L'edificio progettato bene con persone non preparate resta pericoloso: la prova di evacuazione annuale è il momento di verità.
- **Limiti e attenzioni:** Il PEI 'nel cassetto' senza aggiornamento o formazione è inutile in emergenza: chi non sa cosa fare, non lo legge.
- **Costi ed economia:** Costo formazione addetti: 50-150 €/persona; prova di evacuazione: tempo interno; redazione PEI: 500-2.000 €.
- **Caso tipico:** Prova di evacuazione in una scuola: evidenziato che un corridoio si intasava per una porta contraria; invertita l'apertura e ricalibrato il percorso: la prova successiva ha rispettato il tempo con margine del 40%.
- **Normativa:** D.M. 03/08/2015 (capo gestione); D.Lgs 81/2008 (emergenze); UNI ISO 45001 (sistemi gestione sicurezza).
- **Nota di cantiere:** Il PEI va trattato come il libretto dell'auto: revisionato ogni anno, consultato prima di ogni modifica dell'edificio.

### La prevenzione incendi: quadro normativo e logica

**Categoria:** Quadro · **Corso:** Prevenzione incendi e accessibilità

La prevenzione incendi italiana si basa sul D.M. 03/08/2015 (norme tecniche di prevenzione incendi): le attività sono classificate per livello di rischio (basso, medio, alto) e conseguente regime (SCIA antincendio, autorizzazione, nulla osta) con progetto a cura di un professionista abilitato (ingegnere/architetto iscritto agli elenchi del Ministero).

- **Tecnologia e criteri:** Iter: classificazione attività → redazione progetto di prevenzione incendi → presentazione al comando VVF → integrazioni → provvedimento; il progetto valuta: vie di esodo, compartimentazione, mezzi di estinzione, rivelazione, impianti speciali, gestione dell'emergenza; le sanzioni per omessa SCIA o difformità sono pesantissime e possono portare alla chiusura dell'attività.
- **Applicazioni:** Ogni edificio con pubblico (scuole, uffici, negozi, ristoranti, alberghi), industrie, depositi.
- **Vantaggi:** La logica è preventiva: costruire sicuro costa una frazione di quanto costa ristrutturare dopo un incendio o adeguare un locale sequestrato.
- **Limiti e attenzioni:** La normativa è vasta e i regolamenti locali si sovrappongono: serve il professionista abilitato, non il fai-da-te.
- **Costi ed economia:** Costo progetto prevenzione incendi: 2.000-10.000 € secondo complessità; oneri per presidi: voci specifiche.
- **Caso tipico:** Ristorante aperto senza SCIA antincendio: sequestro preventivo dopo un controllo, 30 giorni di chiusura, rientro con progetto e adeguamenti: costo totale ~45.000 €; il progetto preventivo sarebbe costato 4.000 €.
- **Normativa:** D.M. 03/08/2015; regolamento di esecuzione del TULPS (D.P.R. 635/1982, parte); D.Lgs 139/2006 (Codice sicura).
- **Nota di cantiere:** Prima domanda su un locale commerciale: 'che livello di rischio incendio ha questa attività e che titolo mi serve?' — decide costi e tempi dell'apertura.

### La segnaletica di sicurezza e i controlli documentali

**Categoria:** Segnaletica · **Corso:** Prevenzione incendi e accessibilità

La segnaletica di sicurezza (UNI EN ISO 7010) guida l'evacuazione e l'azione in emergenza: cartelli fotoluminescenti o illuminati (uscite, estintori, idranti, punto di ritrovo), planimetrie di evacuazione affisse, percorsi contrassegnati; la manutenzione documentale è la metà della conformità.

- **Tecnologia e criteri:** Requisiti: cartelli normalizzati (pittogrammi, colori: verde = esodo/primo soccorso, rosso = presidi antincendio, giallo = avvertimento), posizione su percorso esodo ad altezza e intervalli regolari, fotoluminescenza o alimentazione di emergenza (UNI EN 1838), planimetrie di evacuazione aggiornate; documenti da conservare: progetti prevenzione incendi, SCIA/nulla osta, verbali collaudi presidi, revisioni estintori, verbali prove evacuazione, certificazioni porte tagliafuoco e materiali.
- **Applicazioni:** Ogni edificio con pubblico e le relative scadenze di controllo.
- **Vantaggi:** La segnaletica corretta orienta anche chi non conosce l'edificio (clienti, visitatori): in emergenza non si ragiona, si segue.
- **Limiti e attenzioni:** La segnaletica 'creativa' non normalizzata confonde: le persone cercano i pittogrammi standard che conoscono.
- **Costi ed economia:** Costo cartelli: 10-50 € l'uno; planimetrie stampate e incorniciate: 30-80 €; il costo della mancata documentazione in un controllo: sanzioni e chiusure.
- **Caso tipico:** Controllo VVF in un centro commerciale: segnaletica ottima ma revisione estintori scaduta di 4 mesi: diffida con termine di 15 giorni; il registro digitale delle scadenze (semplice foglio con alert) avrebbe evitato la diffida e l'ansia.
- **Normativa:** UNI EN ISO 7010 (segnaletica); UNI 11292 (planimetrie evacuazione); D.M. 03/08/2015 (documentazione).
- **Nota di cantiere:** Il registro delle scadenze (estintori, porte, prove, formazione) è la spina dorsale della conformità: chi non ha il registro, non ha la conformità.

### Le vie di esodo: requisiti geometrici e funzionali

**Categoria:** Vie esodo · **Corso:** Prevenzione incendi e accessibilità

Le vie di esodo permettono l'evacuazione: larghezza minime in funzione dell'attività e del numero di occupanti (spesso 1,20 m per corridoi e rampe nei luoghi di pubblico, verifiche sempre sul DM), porte in senso di uscita, percorso massimo per raggiungere un'uscita di sicurezza o uno spazio di sicurezza, illuminazione di emergenza che garantisca i lux minimi di legge.

- **Tecnologia e criteri:** Elementi: unità di piano (max occupanti per compartimento), percorso massimo di esodo, porte con larghezza utile ≥ misura minima dell'attività, uscite su scalinata con pendenza e alzata regolari, spazi di sicurezza (vestiboli presso scale), aree di sicurezza o uscite all'aperto; verifica in progetto con il calcolo degli occupanti (da metratura e destinazione d'uso).
- **Applicazioni:** Progettazione di edifici con pubblico, ristrutturazioni di locali commerciali, verifica di agibilità.
- **Vantaggi:** L'esodo ben progettato salva vite: negli incendi reali la maggior parte delle vittime cade per fumi e calca, non per le fiamme.
- **Limiti e attenzioni:** I requisiti minimi spesso sono in conflitto con il desiderio di 'guadagnare metri': la via di esodo non è negoziabile in fase estetica.
- **Costi ed economia:** Costo aggiuntivo in progettazione: modesto; la conformità in ristrutturazione può richiedere spazi che 'pesano' sulla superficie utile.
- **Caso tipico:** Locale commerciale con unico uscita sul retro attraverso magazzino: la verifica di esodo ha richiesto un secondo percorso indipendente; il costo di 8.000 € ha evitato un sequestro e, in caso di incendio, una tragedia.
- **Normativa:** D.M. 03/08/2015 (capo esodo); UNI 11280 (via di esodo e illuminazione); normativa VVF.
- **Nota di cantiere:** Regola per il LLM: nessun progetto di locale con pubblico si chiude senza il diagramma di esodo con occupanti, larghezze e percorrenze massime.

