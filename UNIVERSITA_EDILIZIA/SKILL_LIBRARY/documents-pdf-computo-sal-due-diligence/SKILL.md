---
name: documents-pdf-computo-sal-due-diligence
description: Acquisisce, indicizza, confronta e consegna documenti tecnici ed economici, PDF, computi, SAL e due diligence con catena di evidenza e limiti dichiarati.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: documenti ed evidenze
---

# Documenti, PDF, computo, SAL e due diligence

## Attivazione e input

Usa la skill per fascicoli immobiliari, capitolati, computi metrici, libretti misure, SAL, fatture, verbali, due diligence tecnica e conversione/controllo PDF. Richiedi scopo, destinatario, data di riferimento, elenco atteso, originali disponibili, riservatezza, formato di consegna e autorità che può attestare.

## Workflow

1. Acquisisci in sola lettura; non alterare l'originale e registra mittente, canale, data e hash.
2. Crea indice con identificativo, nome, tipo, revisione, pagine, autore, data, firma, leggibilità e stato.
3. Esegui OCR solo come livello derivato; conserva immagine e testo estratto, marcando incertezze.
4. Estrai fatti e numeri in una matrice con pagina/coordinate, unità e contesto.
5. Per computo e SAL confronta voci, unità, quantità, prezzi, avanzamento, verbali, fotografie e pagamenti; non confondere importo richiesto con importo approvato.
6. Per due diligence separa titolo, urbanistica, catasto, vincoli, stato fisico, contratti, costi e rischi; assegna stato e responsabile a ogni rilievo.
7. Genera output con collegamento all'evidenza, lista dei mancanti, contraddizioni e data di validità.
8. Esegui controllo pagina per pagina, calcolo indipendente mirato e verifica di apertura del PDF consegnato.

## Output

Fornisci indice, manifest hash, estratti citabili, matrice fatti/assunzioni, confronto numerico, registro incongruenze, checklist mancanti, report due diligence e PDF finale. Mantieni separati dato sorgente, interpretazione, ipotesi e raccomandazione.

## Quality gates

- Ogni importo o quantità critica ha fonte, unità, pagina e revisione.
- Il PDF è leggibile, paginato, non troncato e non contiene allegati persi senza dichiarazione.
- OCR e trascrizioni sono verificati sui passaggi che alimentano conclusioni.
- Computo/SAL espongono formula, arrotondamenti, prezziario e data, se disponibili.
- Nessuna conclusione di conformità nasce da assenza di documento: lo stato è "non verificato".

## Evidenza e provenienza

Usa SHA-256, percorso relativo, data di accesso e catena di trasformazioni. Per PDF firmati conserva originale e verifica firma con strumento appropriato; un PDF visualmente corretto non dimostra autenticità. Registra chi ha confermato un dato e quando.

## Confini professionali e legali

La skill non è perizia, revisione contabile, collaudo, attestazione urbanistica, validazione di SAL o parere legale. Non rimuovere firme, protezioni, metadati o pagine. Tratta dati personali, catastali, bancari e contrattuali come riservati e condividili solo con autorizzazione.

## Failure modes

- **Scansione illeggibile:** segnala pagina e richiedi nuovo originale.
- **OCR errato:** confronta visuale e testo; non correggere senza traccia.
- **Versioni multiple:** conserva tutte e identifica l'attuale con fonte.
- **Prezzo senza listino/date:** non "normalizzare" con un valore inventato.
- **Documento mancante:** non colmare il vuoto con una ricerca generica; registra impatto.

## Strumenti

Usa parser PDF, OCR, viewer con coordinate, foglio di calcolo, checksum, validatori PDF/A, strumenti di firma e repository con accessi. Gli script devono produrre report e non sovrascrivere gli originali.

## Fonti ufficiali e diritti

- [ISO — ISO 32000-2:2020](https://www.iso.org/standard/75839.html): specifica PDF con accesso/licenza propri; non copiare il testo.
- [ISO — ISO 19005-1:2005](https://www.iso.org/standard/38920.html): PDF/A; usare come riferimento e verificare edizione/applicabilità.
- [Normattiva — D.Lgs. 36/2023, art. 15](https://www.normattiva.it/uri-res/N2Ls?urn%3Anir%3Astato%3A2023%3B36~art15%21vig=): riferimento pubblico da verificare nel testo vigente.

La skill descrive una catena di evidenza originale; non attribuisce valore probatorio o professionale a un estratto automatico.
