---
name: circular-materials-lca-inventory
description: Inventario operativo di materiali, contenuti circolari e dati LCA con tracciabilità di unità, confini e scenari; non dichiara carbon neutrality, conformità CAM o prestazioni ambientali senza verifica competente.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: circolarità, materiali e LCA operativa
---

# Inventario circolare e LCA operativa per costruzioni

## Attivazione e input

Attiva questa skill quando un capitolato, BOQ, modello, EPD, passaporto materiale o piano di demolizione deve diventare un inventario verificabile per circolarità o LCA. È una faccetta di dati e scenari distinta da environmental-resilience-lca-diagnostics e materials-construction-methods-prefab: non assegna certificazioni, CAM o dichiarazioni ambientali definitive.

Prima raccogli unità funzionale, oggetto e scala, confini del sistema, periodo e località, quantità e perdite, distinta materiali, componenti riusabili, contenuto riciclato, durabilità, manutenzione, trasporti, energia, fine vita, dati primari/secondari, EPD e regole di allocazione. Se funzione, unità, confini, fonte o data non sono noti, lo stato è blocked.

## Workflow

1. **Gate della domanda:** scrivi il confronto da supportare, unità funzionale, riferimento temporale e decisione; separa screening da LCA comparativa e non cambiare funzione per ottenere un valore migliore.
2. **Gate del materiale:** normalizza codice, componente, massa/volume, composizione, provenienza, contenuto riciclato/riusato, prestazione e quantità installata; conserva quantità misurata e assunta.
3. **Gate dei dati:** classifica ogni dato come primario, EPD/PKD, database o proxy; registra periodo, geografia, tecnologia, versione, unità, cut-off e qualità. Un valore percentuale senza base e denominatore è incompleto.
4. **Gate dei confini:** mappa moduli e flussi di produzione, trasporto, posa, uso, sostituzione, demolizione, recupero e smaltimento secondo il metodo scelto; esplicita esclusioni e infrastrutture fuori confine.
5. **Gate dello scenario:** crea scenario base, riuso, riciclo e fine vita alternativo con ipotesi di resa, distanza, perdita, durata e credito. Non sommare benefici di riuso e riciclo sullo stesso flusso.
6. **Gate di bilancio:** riconcilia quantità con BOQ, modello o pesatura; controlla unità, densità, conversioni, doppio conteggio, massa in ingresso/uscita e indicatori per unità funzionale.
7. **Gate della decisione:** consegna risultati con incertezza, sensibilità, dati mancanti, qualità e data; separa inventario verificato da claim, comunicazione o certificazione da approvare.

## Output

Produci un circular_lca_inventory con catalogo componenti, massa e quantità, fonte e qualità dati, matrice confini/scenari, bilancio, ipotesi, indicatori, sensibilità, gap, diritti e stato ready, conditional o blocked. Ogni claim ha formula, denominatore, periodo, scenario e collegamento alla fonte.

## Quality gates

- Unità funzionale, confini, periodo, geografia e regole di allocazione sono dichiarati.
- Quantità e materiali sono riconciliati con una fonte di progetto e non solo con dichiarazioni.
- Primario, EPD, database, proxy e assunzione sono distinti.
- Riuso, riciclo, recupero e smaltimento non ricevono crediti cumulativi senza giustificazione.
- EPD, contenuto riciclato e claim ambientali sono verificati per prodotto, validità e scope.
- Il risultato non usa “carbon neutral”, “zero waste” o “circolare” come conclusioni automatiche.

## Evidenza e provenienza

Registra BOQ o estratto modello, codici prodotto, pesate, schede tecniche, EPD e dichiarazioni di prestazione, database/versione, fattori, distanze, durata, scenari, formule, script, hash e revisore. Conserva copia o riferimento solo entro licenze e contratto; dati commerciali e di fornitura sono accessibili per ruolo.

## Fonti ufficiali e diritti

- [European Commission Level(s)](https://environment.ec.europa.eu/topics/circular-economy/levels_en): quadro europeo per valutare prestazioni di sostenibilità degli edifici e del ciclo di vita; usare la guida/versione pertinente.
- [European Commission: construction and demolition waste](https://environment.ec.europa.eu/topics/waste-and-recycling/construction-and-demolition-waste_en): riferimento istituzionale per rifiuti da costruzione e demolizione e gerarchia applicabile.
- [ISO 14040](https://www.iso.org/standard/37456.html): riferimento ufficiale ai principi e al quadro LCA; il testo completo è soggetto a licenza.
- [JRC European Platform on LCA](https://eplca.jrc.ec.europa.eu/): piattaforma e metodi/dataset europei; verificare licenza, versione e adeguatezza del dataset.

Le fonti EC e JRC si usano come riferimento e provenance; i testi ISO e i dataset possono essere restricted. La matrice, le formule di riconciliazione e la procedura sono originali. Stato diritti della skill: reference_only; nessun logo, EPD o claim di terzi viene ripubblicato senza autorizzazione.

## Confini professionali e limiti

La skill non esegue verifica indipendente di EPD, non certifica LCA, CAM, tassonomia, carbon neutrality, salubrità o conformità rifiuti e non sostituisce LCA practitioner, progettista ambientale, direzione lavori o autorità. Un inventario completo non equivale a una dichiarazione ambientale verificata; fattori proxy e dati vecchi restano limitazioni.

## Failure modes

- **Percentuale riciclata senza denominatore:** sospendi il claim e richiedi massa, base, prodotto e periodo.
- **EPD fuori prodotto o validità:** marca non applicabile e non trasferire il risultato per analogia.
- **Doppio credito di riuso/riciclo:** separa i flussi e ricalcola lo scenario.
- **BOQ non riconciliato:** conserva differenza e stato conditional; non colmare con quantità inventate.
- **Confini cambiati tra alternative:** blocca il confronto e allinea unità, periodo e moduli.
- **Claim marketing assoluto:** sostituisci con risultato condizionato, fonte, incertezza e revisione.

## Strumenti

Usa registro materiali, foglio o database versionato, parser BOQ/BIM, bilancio di massa, calcolo riproducibile e grafici di sensibilità. Automatizza unità, duplicati e riconciliazioni; non automatizzare l'interpretazione di un claim o l'approvazione di una certificazione.
