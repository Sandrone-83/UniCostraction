---
name: life-cycle-embodied-carbon
description: Imposta valutazioni LCA e carbon embodied di prodotti e opere con unità funzionale, confini, dati, scenari e review tracciabili, senza sostituire EPD, verifica indipendente o decisione progettuale.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: ciclo di vita e carbon embodied
---

# Valutazione del ciclo di vita e carbon embodied

## Attivazione e input

Attiva questa skill quando si devono confrontare materiali, sistemi o alternative progettuali considerando emissioni incorporate, uso, sostituzione, fine vita e scenari di ciclo di vita. È distinta da circular-materials-lca-inventory, che organizza inventari di circolarità e materiali, e da site-water-energy-carbon-accounting, che tratta consumi operativi del cantiere.

Raccogli obiettivo e pubblico, unità funzionale o dichiarata, riferimento e flusso, confini A-D o equivalenti, durata, prestazioni, quantità, distinta materiali, EPD o dataset, trasporti, energia, manutenzione, sostituzioni, riuso/riciclo, fine vita, mix geografico e temporale, fattori GWP, scenari, cut-off, allocazioni, qualità dati, sensitività e necessità di critical review. Se unità, confini o funzione non sono definiti, lo stato è blocked.

## Workflow

1. **Gate dello scopo:** definisci domanda, comparabilità, decisione, unità funzionale, reference study period e destinatari; separa screening, LCA comparativa e claim pubblico.
2. **Gate dei confini:** mappa processi, moduli, flussi, scenari e inclusioni/esclusioni; registra infrastrutture, perdite, trasporti, manutenzione e fine vita omessi.
3. **Gate dei dati:** collega quantità, prestazioni e origine a EPD, dichiarazioni, database o stime; valuta rappresentatività tecnologica, geografica e temporale.
4. **Gate dell'inventario:** normalizza unità, densità, conversioni, quantità e sostituzioni; evita doppio conteggio tra prodotto assemblato, componenti e trasporti.
5. **Gate dell'impatto:** applica metodo, GWP e fattori versionati; separa biogenico, fossile, land-use, carbon storage, removals e compensazioni secondo il metodo.
6. **Gate degli scenari:** testa durata, manutenzione, mix energetico, riuso, riciclo, recupero, trasporto e fine vita; documenta sensitività e intervalli, non solo il valore puntuale.
7. **Gate della decisione:** prepara confronto omogeneo, incertezza e limiti; richiedi review o verifica indipendente quando l'uso o il claim lo richiedono.

## Output

Produci un lca_embodied_carbon_record con goal/scope, unità funzionale, confini, inventario, fonti, quantità, metodo, fattori, risultati per modulo, scenari, sensitività, qualità dati, review e stato screening, conditional, reviewed o blocked. Un numero senza funzione, confini e qualità dati non è un risultato comparativo.

## Quality gates

- Funzione, reference study period, unità, confini e destinatari sono approvati.
- Alternative comparate hanno prestazioni, servizio e durata equivalenti o differenze esplicite.
- Dati, EPD, dataset, fattori, versioni, geografie e periodi sono tracciabili.
- Inventario e sostituzioni sono riconciliati con computo e modello senza doppio conteggio.
- Risultati separano contributi, incertezza, scenari e compensazioni.
- Claim pubblici, CAM, EPD o dichiarazioni di prodotto sono sottoposti a review/verification appropriata.

## Evidenza e provenienza

Conserva goal/scope sheet, quantità, specifiche, EPD, dataset e licenze, fatture o dichiarazioni, trasporti, scenari, fattori, formule, software/versione, sensitivity, review e decision log. Marca misurato, dichiarato, modellato, proxy, scenario e valore verificato. Non incorporare dataset proprietari oltre la licenza e proteggi informazioni commerciali.

## Fonti ufficiali e diritti

- [ISO 14040/14044 — ISO/TC 207](https://www.iso.org/committee/54854/x/catalogue/): principi, quadro e requisiti LCA, da consultare senza riprodurre testo protetto.
- [ISO 14067](https://www.iso.org/standard/71206.html): carbon footprint dei prodotti e relazione con LCA.
- [Commissione europea — Product Environmental Footprint](https://environment.ec.europa.eu/topics/circular-economy/product-environmental-footprint_en): metodo e iniziative ufficiali UE.
- [EPD International](https://www.environdec.com/): programma EPD e regole pubblicate, da verificare per PCR, validità e licenza.

Workflow, matrice dei confini e record sono originali. Diritti: official_reference_only_no_text_reproduced; ISO, PEF, EPD, dataset e software LCA restano soggetti a copyright, licenze e condizioni d'uso. Non si copiano EPD o fattori proprietari nel corpus.

## Confini professionali e legali

La skill non emette EPD, verifica di parte terza, dichiarazione ambientale, conformità CAM, claim di carbon neutrality o decisione di progetto. Non sostituisce LCA practitioner, verificatore, progettista, fabbricante, organismo di certificazione o autorità. Un confronto modellato non prova prestazione reale, salubrità, durabilità o convenienza economica.

## Failure modes

- **Unità funzionali diverse:** blocca confronto e riallinea servizio, durata e prestazioni.
- **EPD fuori scope o scaduta:** tratta la fonte come non applicabile e ricerca versione/programma corretti.
- **Dato proxy nascosto:** marca proxy, quantifica incertezza e prova sensibilità.
- **Moduli o trasporti omessi:** riapri confini e documenta l'effetto.
- **Carbon storage usato come compensazione:** separa stock temporaneo, emissioni e claim.
- **Valore singolo pubblicato come fatto:** aggiungi scenario, qualità, review e limiti.

## Strumenti

Usa goal/scope matrix, model inventory, quantity take-off, EPD/dataset register, factor/version register, LCA software, uncertainty/sensitivity workbook e review log. Automatizza unità, coverage, duplicati e versioni; non generare claim o comparazioni pubbliche senza controllo umano.
