---
name: construction-waste-soil-management
description: Gesta classificazione, provenienza, tracciabilità e destino di rifiuti da cantiere e terre/rocce da scavo senza sostituire responsabile ambientale, laboratorio, trasportatore autorizzato o autorità.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: rifiuti di cantiere e terre/rocce
---

# Rifiuti di cantiere e terre/rocce: tracciabilità operativa

## Attivazione e input

Attiva questa skill quando demolizioni, scavi, materiali di risulta, terre, rocce, imballaggi o rifiuti misti devono essere classificati, separati, stoccati, trasportati, riutilizzati o conferiti. È una faccetta di catena documentale e decisione sul flusso distinta da environmental-resilience-lca-diagnostics, circular-materials-lca-inventory e construction-site-safety: non assegna codici rifiuto, non dichiara sottoprodotto o cessazione della qualifica e non autorizza trasporto o riutilizzo.

Prima raccogli opera e cantiere, origine e scavo, stratigrafia e uso del suolo, quantità e contaminanti sospetti, codice e stato del materiale, analisi, deposito, separazione, trasportatore, impianto/destino, formulari e registri, autorizzazioni, titolare e date. Distingui rifiuto, sottoprodotto, materiale riutilizzato e terreno nell'ambito applicabile. Se origine, composizione, volume, destino o regime giuridico sono ignoti, lo stato è blocked.

## Workflow

1. **Gate dell'origine:** mappa area, fase, processo e materiale prodotto; separa scavo, demolizione, manutenzione, imballaggio, terre naturali, materiali miscelati e contaminati.
2. **Gate della caratterizzazione:** definisci campioni rappresentativi, compositi/discreti, parametri, laboratorio, profondità, frequenza, catena di custodia e confronto con limiti o criteri applicabili; non usare un campione per un lotto non dimostrato.
3. **Gate della qualifica:** documenta ragionamento per rifiuto, sottoprodotto, riutilizzo o fine qualifica e l'eventuale obbligo di analisi, notifica, piano o autorizzazione; mantieni una matrice requisito-evidenza.
4. **Gate della segregazione:** assegna area, contenitore, etichetta, lotto, quantità, incompatibilità, copertura, drenaggio, accesso e tempo; previeni miscelazione e perdita di identità.
5. **Gate del movimento:** riconcilia peso/volume, carico, trasportatore, targa, formulario, registro, impianto autorizzato, viaggio e data; verifica che destino e autorizzazione coprano davvero il materiale.
6. **Gate della qualità del terreno:** traccia riutilizzo in sito, sito di destino, volumetria, bilancio, contaminazione, geologia e condizioni; non chiamare terra pulita un materiale non campionato o miscelato.
7. **Gate della chiusura:** confronta quantità prodotte, stoccate, riutilizzate, trasferite e residue; archivia evidenze, anomalie, autorizzazioni e responsabilità per ogni lotto.

## Output

Consegna un waste_soil_traceability_record con lotti, origine, caratterizzazione, regime, quantità, separazione, deposito, movimento, destinatario, documenti, anomalie, autorizzazioni e stato traced, conditional o blocked. Ogni flusso ha un owner e una regola di chiusura; i documenti mancanti non sono riempiti con stime.

## Quality gates

- Origine, lotto, composizione, quantità, data e destinazione sono identificati.
- Campionamento, laboratorio, catena di custodia e limiti applicabili sono tracciati.
- Rifiuto, sottoprodotto, riutilizzo e fine qualifica non sono usati come sinonimi.
- Segregazione, deposito, copertura, drenaggio e incompatibilità sono verificati in sito.
- Viaggi, trasportatore, impianto, formulari/registri e autorizzazioni sono riconciliati.
- Nessun materiale viene dichiarato pulito, riutilizzabile o escluso dai rifiuti senza base e soggetto competente.

## Evidenza e provenienza

Conserva planimetrie e foto dei lotti, rilievi, scavi, stratigrafie, campioni, rapporti di laboratorio, pesate, formulari, registri, contratti, autorizzazioni, visure del destinatario, viaggi, quantità, hash e log delle correzioni. Marca osservato, misurato, dichiarato, stimato e approvato. Coordinate di contaminazione e dati aziendali sono limitati per ruolo.

## Fonti ufficiali e diritti

- [D.Lgs. 152/2006 su Normattiva](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2006-04-03;152!vig=): quadro italiano ambientale e rifiuti, da verificare per testo vigente e fattispecie.
- [DPR 120/2017 su Normattiva](https://www.normattiva.it/eli/id/2017/08/07/17G00135/CONSOLIDATED/20210730): disciplina delle terre e rocce da scavo, inclusi regimi e condizioni da applicare al caso concreto.
- [Direttiva 2008/98/CE su EUR-Lex](https://eur-lex.europa.eu/eli/dir/2008/98/oj): quadro europeo sui rifiuti e gerarchia di gestione.
- [ISPRA](https://www.isprambiente.gov.it/it): riferimenti e dati istituzionali ambientali da selezionare per matrice e territorio.

Le fonti normative, linee guida e dataset si consultano presso l'autorità e non si riproducono oltre diritti e licenze. Lotti, matrici, catena di evidenza e procedura sono originali. Stato diritti: official_reference_only_no_text_reproduced; analisi, formulari e dati di terzi restano soggetti a contratto e privacy.

## Confini professionali e legali

La skill non assegna definitivamente codice rifiuto, non certifica analisi, non dichiara sottoprodotto o end-of-waste, non autorizza deposito/trasporto/scarico e non sostituisce produttore, responsabile ambientale, geologo, laboratorio, trasportatore, gestore dell'impianto o autorità. Una scheda completa non sana un'operazione non autorizzata e non prova assenza di contaminazione oltre il campione.

## Failure modes

- **Campione non rappresentativo:** blocca il lotto e ridisegna campionamento, profondità e frequenza.
- **Volume stimato senza bilancio:** separa stima, peso, densità e misura e conserva lo scarto.
- **Terreno naturale miscelato con demolizione:** congela il lotto, indaga contaminazione e non riutilizzare automaticamente.
- **Destino autorizzato per altro codice o materiale:** cambia stato in blocked e verifica titolo e condizioni.
- **Deposito senza separazione o drenaggio:** segnala rischio di miscela e contaminazione e attiva il responsabile.
- **Formulario usato come prova di conformità:** riconcilia produzione, viaggio, impianto e autorizzazioni, senza confondere ricevuta e qualifica.

## Strumenti

Usa GIS e planimetrie di lotti, registro materiali, campionamento con catena di custodia, laboratorio qualificato, bilancia/pesate, registro viaggi, document repository e dashboard di quantità. Automatizza ID, bilanci, scadenze, duplicati e riconciliazioni; non automatizzare qualifica giuridica, autorizzazioni o decisioni ambientali.
