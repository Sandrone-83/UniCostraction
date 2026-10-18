---
name: architecture-project-workflow
description: Gestisce incarichi di architettura e progettazione edilizia dalla richiesta iniziale al pacchetto revisionato, mantenendo decisioni, revisioni, evidenze e limiti professionali espliciti.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: progettazione edilizia
---

# Architettura e workflow di progetto

## Attivazione

Usa questa skill quando la richiesta riguarda concept, rilievo, programma funzionale, layout, coordinamento di elaborati, capitolati descrittivi, iter di revisione o consegna progettuale. Non usarla per dichiarare conformità urbanistica, calcolare strutture, firmare elaborati o sostituire un professionista incaricato.

## Input minimo

- obiettivo, committente, uso dell'immobile e località;
- stato delle fonti: rilievi, foto, DWG/IFC/PDF, titoli, vincoli, prescrizioni;
- livello richiesto e formato di consegna;
- vincoli di costo, tempo, accessibilità, prestazioni e autorizzazione a modificare file.

Se mancano dati critici, crea una lista di assunzioni con stato "da verificare"; non trasformarla in requisito.

## Workflow

1. **Inquadra** incarico, destinatari, confini, criteri di successo e autorità decisionale.
2. **Inventaria** i documenti con percorso, autore, data, revisione, hash quando possibile e attendibilità.
3. **Separa** rilievo, fonte normativa, richiesta del committente, interpretazione progettuale ed esempio.
4. **Imposta** programma, matrici ambienti, requisiti, interfacce e coordinate di riferimento.
5. **Sviluppa** opzioni comparabili; per ogni opzione registra vantaggi, costi, rischi, dipendenze e decisione.
6. **Coordina** piante, sezioni, prospetti, dettagli, abachi e note; usa un codice revisione coerente.
7. **Verifica** quote, superfici, accessi, stratigrafie, aperture e coerenza tra tavole e relazione.
8. **Consegna** pacchetto con indice, changelog, assunzioni aperte, evidenze e approvazioni ricevute.

## Output

Produci, secondo necessità:

- brief strutturato e registro requisiti;
- matrice fonti/decisioni e registro rischi;
- elaborati nominati con revisione e data;
- relazione sintetica che distingue fatto, ipotesi e proposta;
- checklist di consegna e domande per il professionista o il committente.

## Quality gates

- Ogni dimensione o vincolo rilevante ha fonte o marcatura "assunto".
- La revisione citata nell'indice è presente in ogni file consegnato.
- Un controllo visivo e uno strutturale sui riferimenti incrociati non mostrano contraddizioni.
- La consegna è riproducibile da un altro operatore usando l'indice.
- Nessuna frase usa "conforme", "approvato", "agibile" o "a norma" senza evidenza e soggetto competente.

## Evidenza e provenienza

Conserva per ogni decisione id, descrizione, fonte, estratto/parafrasi, data di verifica, autore e stato (osservato, interpretato, proposto, approvato). Per i file binari registra almeno nome, revisione, dimensione e hash. Una fonte online è un riferimento, non prova dell'aggiornamento alla data del progetto.

## Confini professionali e legali

Il risultato è supporto tecnico e organizzativo. Titoli edilizi, relazioni asseverate, calcoli, direzione lavori, sicurezza, tutela paesaggistica e firme richiedono professionista abilitato, committente e autorità competenti. Verifica sempre testo vigente, regolamenti regionali/comunali e incarico. Non inviare istanze, non attestare diritti e non pubblicare dati personali senza autorizzazione.

## Failure modes

- **Rilievo incompleto:** blocca le quote dipendenti e prepara richiesta mirata.
- **Fonti discordanti:** non fare media; conserva entrambe, evidenzia la discordanza e chiedi verifica.
- **Revisione persa:** congela il pacchetto, recupera il log e non sovrascrivere l'originale.
- **Render scambiato per prova:** etichetta la visualizzazione come rappresentazione.
- **Scope creep:** apri una nuova richiesta con impatto su tempi, costi e responsabilità.

## Strumenti

Usa editor di testo, foglio di controllo, CAD/BIM, visualizzatore PDF e strumenti di hash. Automatizza rinomina, inventario e controlli ripetitivi; lascia a un umano le decisioni di merito e le approvazioni.

## Fonti ufficiali e diritti

- [Normattiva — DPR 380/2001](https://www.normattiva.it/atto/caricaDettaglioAtto?atto.articolo.numero=0&atto.codiceRedazionale=001G0429&atto.dataPubblicazioneGazzetta=2001-10-20): testo pubblico ufficiale; verificare consolidato vigente, nessun testo riprodotto.
- [ISO — ISO 19650-1](https://www.iso.org/standard/68078.html): standard con accesso/licenza propri; usare come riferimento, non copiare o redistribuire.
- [EU BIM Task Group — handbook](https://eubim.eu/handbook/): riferimento istituzionale; controllare termini di riuso e versione.

Questa skill sintetizza procedure originali. Le fonti non sono pareri legali, né autorizzano l'uso commerciale di contenuti di terzi.
