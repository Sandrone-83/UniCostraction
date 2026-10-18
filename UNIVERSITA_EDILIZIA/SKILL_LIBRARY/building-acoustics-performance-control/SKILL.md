---
name: building-acoustics-performance-control
description: Controlla requisiti, dettagli, misure e incertezze dell'acustica edilizia per involucro, partizioni, impianti e rumore senza sostituire il tecnico competente o certificare la conformità.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: acustica edilizia
---

# Controllo prestazionale dell'acustica edilizia

## Attivazione e input

Attiva questa skill quando il progetto o l'edificio deve dimostrare isolamento, rumore da impatto, facciata, riverberazione o rumore degli impianti con dati di progetto e misure in opera. È una faccetta di specifica e controllo dell'evidenza distinta da mep-energy-systems, architecture-project-workflow e environmental-resilience-lca-diagnostics: non emette una relazione firmata, non assegna agibilità e non valuta da sola il disturbo ambientale.

Prima raccogli destinazione e categorie degli ambienti, sorgenti e ricettori, geometria, stratigrafie e ponti acustici, impianti e orari, clima/rumore di fondo, requisiti contrattuali e normativi, stato del progetto o as-built, strumenti e calibrazioni, periodo di misura e criterio di accettazione. Se confini, uso, sorgente, ricettore o requisito sono ignoti, lo stato è blocked.

## Workflow

1. **Gate del problema:** classifica trasmissione per via aerea, impatto, facciata, impianto, riverbero o rumore esterno; separa requisito di progetto, misura di diagnosi e limite amministrativo.
2. **Gate dei percorsi:** mappa partizioni, giunti, facciate, serramenti, attraversamenti, cavedi, strutture e impianti; segna ponti acustici e percorsi laterali che un dettaglio isolato non rappresenta.
3. **Gate del modello:** congela stratigrafie, masse, elasticità, disaccoppiamenti, posa, tolleranze e dettagli esecutivi; registra dati mancanti e non sostituire una prestazione misurata con una scheda di prodotto.
4. **Gate della misura:** definisci posizione microfoni, sorgente, fondo, durata, bande, condizioni operative, rumore estraneo e ripetizioni; controlla calibrazione prima/dopo e tracciabilità dell'operatore.
5. **Gate dell'incertezza:** registra correzioni, campo di frequenza, ripetibilità, rumore di fondo e limiti dell'indice sintetico; distingui valore misurato, stima, previsione e tolleranza.
6. **Gate della causa:** confronta progetto, misura e rilievo del dettaglio; formula ipotesi ordinate per percorso e verifica con prova mirata. Non attribuire il difetto al materiale senza escludere posa e fiancheggiamenti.
7. **Gate della decisione:** consegna azione correttiva, costo/impatti, prova di conferma e responsabilità; la dichiarazione di conformità resta al tecnico competente e al committente autorizzato.

## Output

Consegna un acoustic_performance_record con ambienti, sorgenti/ricettori, requisiti, percorsi, stratigrafie, misure, strumenti, incertezza, diagnosi, gap, rimedio e stato measured, conditional o blocked. Ogni numero conserva unità, bande, posizione, condizioni, fonte e criterio di confronto.

## Quality gates

- Requisito e regime applicabile sono distinti da diagnosi e rumore ambientale.
- Sorgente, ricettore, geometria e percorsi laterali sono identificati.
- Strumento, calibrazione, posizioni, durata, fondo e condizioni sono registrati.
- Misure e previsioni riportano banda, indice, incertezza e campo di validità.
- La causa viene verificata con prova mirata e non dedotta dalla sola prestazione nominale.
- Nessun rapporto viene presentato come certificazione o attestazione firmata senza tecnico autorizzato.

## Evidenza e provenienza

Conserva elaborati e revisioni, schede tecniche, dettagli di posa, foto, mappe dei percorsi, file di misura grezzi, calibrazioni, log, condizioni ambientali, calcoli, script e hash. Marca dati del fabbricante, misura indipendente, assunzione e interpretazione. Le registrazioni audio, planimetrie e dati degli occupanti sono minimizzati e custoditi secondo autorizzazioni e privacy.

## Fonti ufficiali e diritti

- [Gazzetta Ufficiale — DPCM 5 dicembre 1997](https://www.gazzettaufficiale.it/atto/serie_generale/caricaDettaglioAtto/originario?atto.codiceRedazionale=97A10190&atto.dataPubblicazioneGazzetta=1997-12-22&elenco30giorni=false): requisiti acustici passivi degli edifici; verificare ambito e aggiornamenti applicabili.
- [ISO 16283-1](https://www.iso.org/standard/55997.html?browse=ics): riferimento ufficiale per misure in opera dell'isolamento acustico per via aerea.
- [ISO/TC 43/SC 2 Building acoustics](https://www.iso.org/committee/48558/x/catalogue/): catalogo ufficiale degli standard di acustica edilizia; scegliere edizione e parte pertinenti.

Norme ISO e norme tecniche editoriali sono restricted: si citano identificativi e scopo senza copiare clausole o tabelle. Il workflow, il record di misura e la matrice dei percorsi sono originali. Stato diritti: official_reference_only_no_text_reproduced; schede e registrazioni di terzi restano soggette a licenza.

## Confini professionali e legali

La skill non certifica requisiti acustici, non attribuisce responsabilità per disturbo, non firma relazioni, non autorizza lavori e non sostituisce tecnico competente in acustica, progettista, laboratorio o autorità. Una misura di ambiente o una previsione di calcolo vale solo per configurazione, strumento, condizioni e metodo registrati; non garantisce il comportamento dell'intero edificio.

## Failure modes

- **Valore nominale usato come misura in opera:** riapri posa, ponti e verifica sul campo.
- **Fondo superiore al segnale:** marca il dato non dimostrato e ripeti in condizioni controllate.
- **Un solo ambiente generalizzato all'edificio:** esplicita campionamento e seleziona ambienti rappresentativi.
- **Ponte laterale ignorato:** mappa i percorsi e pianifica prova o dettaglio di conferma.
- **Indice sintetico senza bande/incertezza:** conserva spettro, metodo, correzioni e limite di interpretazione.
- **Rumore ambientale confuso con requisito edilizio:** separa la procedura e indirizza al tecnico competente.

## Strumenti

Usa checklist dei percorsi, modello stratigrafico versionato, fonometro e sorgente calibrati, logger con file grezzo, foglio di calcolo riproducibile e issue tracker. Automatizza unità, completezza, confronto e grafici; non automatizzare certificazione, attribuzione della causa o giudizio amministrativo.
