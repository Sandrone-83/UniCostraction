---
name: geotechnical-foundation-data-gating
description: Controllo della sufficienza e della tracciabilità dei dati geotecnici prima di confrontare terreni, fondazioni e cedimenti; non dimensiona opere né sostituisce la relazione geologica o geotecnica.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: geotecnica, fondazioni e dati di sottosuolo
---

# Gating dei dati geotecnici per fondazioni

## Attivazione e input

Attiva questa skill quando un progetto, una variante, un computo o una diagnosi chiede di scegliere o confrontare fondazioni a partire da sondaggi, prove in sito, laboratorio, falda o dati storici. È una faccetta di sufficienza, correlazione e controllo dati distinta da structural-civil-engineering: non produce portanza, armature, pareri o calcoli firmabili.

Prima raccogli ubicazione e coordinate, stratigrafia, quota e sistema di riferimento, cronologia, uso e geometria dell'opera, azioni e combinazioni disponibili, livello di progettazione, categoria del terreno, falda e drenaggio, sismicità applicabile, indagini eseguite, laboratorio, campioni, prove, incertezza e licenza dei dati. Se mancano estensione dell'area indagata, coordinate/quote o scopo progettuale, lo stato è blocked.

## Workflow

1. **Gate del contesto:** definisci fondazione, carichi, fasi costruttive, scavi, edifici vicini e fenomeni da controllare; separa dato osservato, parametro correlato e assunzione.
2. **Gate spaziale:** georiferisci ogni sondaggio, prova e falda a un riferimento comune; verifica profondità, quota testa foro, inclinazione e copertura rispetto all'impronta e ai bordi sensibili.
3. **Gate stratigrafico:** costruisci una sezione interpretativa versionata, marcando cambi litologici, discontinuità, rifiuti, riempimenti, livelli organici e zone non osservate. Non interpolare continuità solo perché due colonne hanno nomi simili.
4. **Gate della qualità:** associa campione, metodo, data, laboratorio, calibrazione e catena di custodia a ogni risultato; controlla unità, limiti di rilevabilità, outlier e differenza tra prova in sito e prova su campione disturbato.
5. **Gate parametro -> decisione:** per ogni parametro registra origine, profondità, trasformazioni e intervallo; traccia quali dati supportano drenato/non drenato, cedimento, liquefazione, stabilità o scavo. Se il correlato non è applicabile, non convertirlo automaticamente.
6. **Gate di scenari:** confronta almeno scenario centrale, sfavorevole e dati mancanti; evidenzia falda stagionale, consolidazione, variabilità laterale e costruzione per fasi. Un valore medio non cancella il caso debole localizzato.
7. **Gate di handoff:** consegna registro fonti, carta delle indagini, sezioni, anomalie e domande al progettista geotecnico. Solo il professionista determina modello geotecnico, verifiche e fondazione.

## Output

Produci una geotechnical_data_gate con inventario indagini, mappa di copertura, stratigrafie versionate, matrice parametro-origine-profondità, controlli di qualità, assunzioni, scenari, gap e stato ready, conditional o blocked. Ogni raccomandazione deve indicare l'evidenza che la sostiene e la verifica ancora necessaria.

## Quality gates

- Ogni dato ha posizione, quota/profondità, data, metodo, unità e origine.
- Sondaggio, prova in sito, laboratorio e correlazione non sono mescolati in un unico campo.
- L'area realmente indagata è distinta dalle superfici interpolate o estrapolate.
- Falda, variabilità, rifiuti, campioni disturbati e dati storici hanno un trattamento esplicito.
- Le decisioni non usano un singolo valore medio senza scenario sfavorevole.
- La consegna non presenta il gate come calcolo o attestazione di sicurezza.

## Evidenza e provenienza

Conserva riferimenti a rapporto di prova, registro di campo, log macchina, certificato di laboratorio, coordinate, quote, fotografie, file originale e hash quando possibile. Registra chi ha interpretato la stratigrafia, versione del modello, data di accesso e modifiche. I dati del committente e del sottosuolo possono essere riservati: applica accesso per ruolo e non pubblicare planimetrie o coordinate senza autorizzazione.

## Fonti ufficiali e diritti

- [JRC Eurocode 7](https://eurocodes.jrc.ec.europa.eu/EN-Eurocodes/eurocode-7-geotechnical-design): portale ufficiale europeo di riferimento per Eurocodice 7; consultare l'edizione applicabile e l'adozione nazionale.
- [NTC su Gazzetta Ufficiale](https://www.gazzettaufficiale.it/eli/id/2018/02/20/18A00716/sg): decreto e allegati ufficiali per le norme tecniche italiane; verificare modifiche, circolari e applicabilità temporale.
- [Normattiva](https://www.normattiva.it/): testo vigente e multivigente degli atti italiani; non sostituisce l'esame degli allegati tecnici e delle responsabilità professionali.

Le fonti sono riferimenti ufficiali e non vengono riprodotte. Il modello di gate, le matrici di sufficienza e la procedura sono originali. Stato diritti: reference_only per standard e atti; eventuali norme tecniche editoriali restano restricted e si consultano tramite copia autorizzata.

## Confini professionali e limiti

La skill non esegue indagini, non interpreta definitivamente il terreno, non sceglie fondazioni, non calcola portanza/cedimenti, non valuta stabilità o rischio sismico e non firma relazioni. Non sostituisce geologo, ingegnere geotecnico, direttore lavori o laboratorio qualificato. Dati storici, correlazioni generiche e immagini non sono prova sufficiente di sicurezza.

## Failure modes

- **Sondaggio fuori impronta trattato come rappresentativo:** segnala distanza, scala e differenza geomorfologica; richiedi integrazione.
- **Rifiuto di penetrazione letto come strato competente:** separa rifiuto, ostacolo e resistenza e cerca verifica indipendente.
- **Falda puntuale trattata come falda stabile:** registra stagione, durata di lettura, drenaggio e scenario alto.
- **Campione disturbato usato per parametro sensibile:** riduci confidenza e richiedi prova idonea.
- **Media che nasconde lente debole:** conserva variabilità e scenario locale sfavorevole.
- **Gate scambiato per dimensionamento:** cambia stato in blocked e inoltra al professionista responsabile.

## Strumenti

Usa GIS/CAD per copertura, foglio o database per tracciabilità dei campioni, calcolo riproducibile dei controlli e report con grafici delle variabilità. Automatizza controlli di unità, coordinate e completezza, non il giudizio geotecnico.
