---
name: photo-laserscan-asbuilt-control
description: Coordina fotografia tecnica, laser scan e confronto as-built con controllo di riferimento, accuratezza, revisioni e deviazioni, senza dichiarare conformità geometrica o sostituire topografo e direttore lavori.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: documentazione fotografica, laser scan e as-built control
---

# Documentazione fotografica, laser scan e controllo as-built

## Attivazione e input

Attiva questa skill quando serve acquisire e confrontare stato realizzato, avanzamento, coperture, sottoservizi, MEP o elementi nascosti tramite fotografie tecniche, nuvole di punti, scansioni, fotogrammetria o modelli as-built. È distinta da survey-geospatial-topography-control, che governa il rilievo e il controllo topografico, e da bim-4d-5d-planning-control, che usa il modello per tempo/costi.

Raccogli scopo e decisione, area, coordinate e datum, riferimento e target, tolleranze, superficie e occlusioni, dispositivo, calibrazione, setup, overlap, luce, scala, data/ora, operatori, permessi privacy, punti di controllo, modello di progetto, revisione, formato, densità, accuratezza attesa e destinazione del record. Se uso, sistema di riferimento, tolleranza o revisione non sono definiti, lo stato è blocked.

## Workflow

1. **Gate dello scopo:** definisci se l'immagine serve a documentare, misurare, confrontare o provare una deviazione; non trattare una foto illustrativa come rilievo.
2. **Gate del riferimento:** congela datum, coordinate, control points, target, unità, modello di progetto e tolleranza; verifica visibilità e stabilità dei riferimenti.
3. **Gate dell'acquisizione:** pianifica stazioni, overlap, campo visivo, luce, target, scale, meteo, accesso e aree nascoste; registra setup e condizioni.
4. **Gate della qualità:** verifica registrazione, drift, noise, coverage, occlusioni, scala, risoluzione, accuratezza e georeferenziazione; conserva raw data prima del filtraggio.
5. **Gate del confronto:** allinea dataset e modello revisionato, applica tolleranza dichiarata, classifica deviazioni e separa reale, non osservabile, fuori copertura e falso positivo.
6. **Gate del record:** collega foto/point cloud a coordinate, elemento, fase, issue e revisioni; registra operatori, strumenti, trasformazioni e hash o identificativo controllato.
7. **Gate dell'as-built:** aggiorna il modello o drawing solo da deviazione verificata e decisione autorizzata; mantieni originale, derivato, annotazione e approvazione separati.

## Output

Produci un asbuilt_capture_record con scopo, area, datum, setup, raw/derived data, coverage, qualità, confronto, tolleranze, issue, elementi non osservabili e stato documented, conditional o blocked. Un delta geometrico è un'indicazione da verificare, non una non conformità automatica.

## Quality gates

- Scopo, area, datum, coordinate, revisione, tolleranza e destinatario sono espliciti.
- Device, seriale, calibrazione, setup, target, operatore e condizioni sono registrati.
- Raw data, processing, filtri, registrazione, accuratezza e coverage sono valutati.
- Occlusioni, drift, superfici riflettenti, movimento, luce e accessi sono dichiarati.
- Confronto usa lo stesso riferimento, unità, revisione e criterio; falso positivo e non osservabile sono separati.
- As-built, drawing e issue hanno approvazione e non sovrascrivono l'originale senza audit trail.

## Evidenza e provenienza

Conserva originali fotografici e scansioni, metadata, control points, calibration, registration reports, processing scripts/settings, cloud/model version, coverage map, residuals, comparison output, issue log, access permits e approvazioni. Marca raw, derived, rendered, annotated e approved. Minimizza volti, targhe, interni sensibili e dati di sicurezza; conserva accessi e licenze.

## Fonti ufficiali e diritti

- [USGS — topographic lidar surveys](https://www.usgs.gov/special-topics/earth-mri/science/topographic-lidar-surveys): riferimento istituzionale su point cloud e qualità/uso del lidar.
- [buildingSMART — Information Delivery Manual](https://www.buildingsmart.org/standards/bsi-standards/information-delivery-manual/): flussi informativi e consegne, senza copiare contenuti protetti.
- [ISO 19650 — pagina ISO](https://www.iso.org/standard/68078.html): gestione dell'informazione e versionamento nel ciclo dell'asset.
- [Normattiva — Codice dei beni culturali, quando pertinente](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2004-01-22;42!vig=): vincoli e autorizzazioni da verificare per siti tutelati.

Workflow, schede di acquisizione e confronto sono originali. Diritti: official_reference_only_no_text_reproduced; immagini, nuvole di punti, software, dataset, modelli e documenti del committente restano soggetti a licenza, privacy e autorizzazione.

## Confini professionali e legali

La skill non esegue rilievo topografico certificato, non dichiara tolleranza o conformità edilizia, non firma as-built, collaudi, stati di consistenza o pratiche catastali e non autorizza accessi o riprese in aree sensibili. Non sostituisce topografo, progettista, direttore lavori, BIM manager, responsabile privacy o autorità. La precisione del sensore non prova la correttezza del riferimento o del confronto.

## Failure modes

- **Datum o revisione errati:** blocca confronto e riallinea riferimento/modello.
- **Nuvola bella ma non georeferenziata:** marca solo documentale e richiede controllo.
- **Occlusione trattata come assenza di elemento:** classifica non osservabile e pianifica nuova acquisizione.
- **Foto senza contesto:** collega scala, coordinate, direzione, data e elemento.
- **Scansione filtrata sovrascrive raw:** recupera originale e registra trasformazioni.
- **Delta automatico come NCR:** verifica tolleranza, causa, ripetizione e approvazione tecnica.

## Strumenti

Usa capture plan, camera/laser register, control-point sheet, metadata extractor, photogrammetry/point-cloud software, registration QA, coverage map, cloud-to-model comparison, issue tracker e as-built revision log. Automatizza checksum, metadata, coverage e report; non modificare asset ufficiali o dichiarare conformità senza approvazione.
