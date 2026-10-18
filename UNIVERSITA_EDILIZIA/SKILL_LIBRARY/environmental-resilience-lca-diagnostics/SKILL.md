---
name: environmental-resilience-lca-diagnostics
description: Imposta LCA, rischio climatico, diagnostica del costruito e recupero con confini, funzionali, evidenze, incertezze e priorità di intervento tracciati.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: ambiente, ciclo di vita, patologie e recupero edilizio
---

# Resilienza ambientale, LCA, diagnostica e recupero

## Attivazione

Usa la skill per valutare impatti di ciclo di vita, rischi climatici e ambientali, degrado, umidità, qualità del costruito, alternative di recupero, manutenzione e gestione dei rifiuti. Non usare un indicatore aggregato per dichiarare da solo salubrità, sicurezza, conformità o valore immobiliare.

## Input

Definisci edificio o infrastruttura, localizzazione, clima, uso, periodo, sistema di confine, unità funzionale, scenari, materiali, quantità, trasporti, energia, acqua, manutenzione, fine vita e qualità dei dati. Per diagnosi acquisisci rilievi, cronologia, stratigrafie, foto con posizione e data, misure, campioni, prove, sintomi e condizioni ambientali. Etichetta osservazioni, interpretazioni, ipotesi e dati mancanti.

## Workflow

1. Fissa obiettivo, destinatario, territorio, orizzonte temporale, unità funzionale, confini e criteri di confronto.
2. Costruisci inventario delle fonti e matrice di qualità: origine, rappresentatività geografica/temporale/tecnologica, completezza e incertezza.
3. Per resilienza mappa pericoli, esposizione, vulnerabilità, capacità di adattamento, soglie, interdipendenze e scenari futuri senza confondere rischio con evento certo.
4. Per diagnostica formula ipotesi alternative, pianifica rilievi e prove non distruttive/distruttive, controlla calibrazione e collega sintomo, causa probabile e confidenza.
5. Confronta recupero, sostituzione, manutenzione e non intervento su prestazione, impatto, costo, reversibilità, durabilità, rifiuti e rischio di spostamento dell'impatto.
6. Ordina interventi per urgenza, efficacia, dipendenze, accessibilità e responsabilità; definisci monitoraggio, trigger e riesame.

## Output

Consegna rapporto di scopo e confini, inventario dati e fonti, modello o foglio riproducibile, scenari e sensitività, mappa rischi, piano diagnostico, registro patologie, matrice opzioni di recupero, piano monitoraggio e lista di limiti/decisioni. Riporta sempre il livello di confidenza e ciò che non è stato osservato.

## Quality gates

- LCA espone unità funzionale, confini, periodo, mix energetico, scenari, fonti e regole di allocazione.
- Un confronto usa la stessa funzione e dichiara differenze di durata, manutenzione, sostituzione e fine vita.
- Rischi climatici riportano territorio, scenario, orizzonte, probabilità o assunzione e conseguenza.
- Diagnosi separa sintomo, causa ipotizzata, prova, confidenza e alternativa non esclusa.
- Recupero considera rifiuti, contaminazioni, sicurezza del cantiere, autorizzazioni e monitoraggio post-intervento.

## Provenienza ed evidenza

Archivia file originali, foto, coordinate, timestamp, strumenti e tarature, catena dei campioni, database o EPD con versione, assunzioni, formule, log, hash e revisioni. Una EPD, un database LCA o una termografia non è automaticamente rappresentativa dell'opera, del clima o del prodotto effettivamente installato.

## Controllo versione, territorio e data

Verifica versione e licenza di metodo, database, EPD, fattori di emissione, scenari climatici e legge ambientale. Indica territorio e data di ogni dato: mix elettrico, prezzi, rifiuti, clima e norme cambiano. Le conclusioni devono dire se valgono per Italia, altra giurisdizione o solo per lo scenario modellato; riapri il confronto quando cambiano confini o dati dominanti.

## Confini professionali e legali

La skill non rilascia certificazioni ambientali, diagnosi strutturali o igienico-sanitarie, bonifiche, autorizzazioni rifiuti, valutazioni di sicurezza o asseverazioni. Non prescrivere campionamenti pericolosi, demolizioni o lavori su contaminanti senza tecnico, laboratorio e piano autorizzato. La scelta finale di recupero richiede i professionisti e gli enti competenti.

## Failure modes

- **Green claim senza unità funzionale:** blocca il claim e ricostruisci funzione, durata e confini.
- **Database fuori territorio o periodo:** sostituisci o dichiara proxy, incertezza e sensibilità.
- **Causa dedotta da una foto:** formula ipotesi e pianifica prova mirata.
- **Rischio climatico generico:** specifica hazard, esposizione, scenario e orizzonte.
- **Recupero che nasconde rifiuti o manutenzione:** estendi il ciclo di vita e aggiorna il confronto.

## Strumenti

Usa GIS, rilievo fotografico e sensori, termografia/diagnostica con operatori qualificati, fogli LCA versionati, database autorizzati, gestione campioni, repository hashato e dashboard di monitoraggio. Ogni automazione deve conservare input, versione, formula e incertezza; non trasformare una mappa o un punteggio in una certificazione.

## Fonti ufficiali e diritti

- [ISO — ISO 14040](https://www.iso.org/standard/37456.html): `rights_state: official_standard_paid_or_restricted_reference_only`; riferimento normativo con accesso/licenza propri; non copiare il testo.
- [Commissione europea — Level(s)](https://environment.ec.europa.eu/topics/circular-economy/levels_en): `rights_state: official_reference_only_no_text_reproduced`; metodo istituzionale europeo e materiali di orientamento; verificare versione e condizioni d'uso.
- [Normattiva — D.Lgs. 152/2006](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2006-04-03;152!vig=): `rights_state: official_public_legal_text_verify_current_consolidation`; fonte legislativa pubblica italiana da controllare nel consolidato vigente.

La skill è una procedura originale di analisi. Database, EPD, immagini, report di laboratorio e standard conservano i propri diritti, licenze e limiti di riuso.
