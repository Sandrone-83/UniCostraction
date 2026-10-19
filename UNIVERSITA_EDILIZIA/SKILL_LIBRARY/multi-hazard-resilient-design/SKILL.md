---
name: multi-hazard-resilient-design
description: Struttura analisi di robustezza e resilienza multi-pericolo per sisma, alluvione e vento, collegando hazard, vulnerabilità e continuità senza sostituire progettista, calcolo firmato o autorità.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: progettazione resiliente a sisma, alluvione e vento
---

# Progettazione resiliente a sisma, alluvione e vento

## Attivazione e input

Attiva questa skill quando un edificio, infrastruttura o cantiere deve mantenere sicurezza, funzionalità o rapidità di recupero sotto sisma, alluvione, vento forte o combinazioni di pericoli. È distinta da structural-civil-engineering, che tratta analisi strutturale generale, e da environmental-resilience-lca-diagnostics, che tratta resilienza ambientale e diagnosi più ampia.

Raccogli sito, uso e occupanti, vita nominale, classi di conseguenza, suolo e falda, dati idrologici/idraulici, quota e drenaggio, vento e esposizione, hazard map e return period, geometria, materiali, connessioni, impianti, elementi non strutturali, opere provvisionali, vulnerabilità, interdipendenze, soglie di prestazione, recovery target, vincoli e manutenzione. Se hazard, uso, prestazione o modello di riferimento mancano, lo stato è blocked.

## Workflow

1. **Gate del rischio:** definisci hazard, esposizione, vulnerabilità, conseguenza e livello di servizio; separa pericolo naturale da difetti di progettazione o manutenzione.
2. **Gate del sito:** verifica fonti ufficiali, microzonazione o idraulica locale, quote, drenaggio, terreno, vento, accessi e infrastrutture dipendenti; marca risoluzione e data.
3. **Gate dello scenario:** costruisci matrici sisma-alluvione-vento, sequenze e combinazioni credibili, inclusi perdita alimentazione, acqua, accesso e contaminazione.
4. **Gate del sistema:** mappa struttura, involucro, ancoraggi, impianti, riserve, vie di esodo, materiali mobili e funzioni critiche; identifica failure path e ridondanze.
5. **Gate delle prestazioni:** collega scenario a soglia di danno, sicurezza, operabilità, downtime, recovery e decisione; non usare “resiliente” senza criterio misurabile.
6. **Gate delle misure:** confronta prevenzione, protezione, adattamento, monitoraggio, manutenzione e piano di risposta con costo, fattibilità e residual risk.
7. **Gate della validazione:** sottoponi calcoli, rilievi, modelli, prove e assunzioni al progettista e alle autorità; riapri dopo modifica, evento o nuova informazione hazard.

## Output

Produci un multi_hazard_resilience_record con sito, hazard, scenario, esposizione, vulnerabilità, prestazioni, misure, residual risk, recovery target, evidenze e stato screened, conditional, designed_by_professional o blocked. Riporta limiti di scala, periodo e manutenzione.

## Quality gates

- Uso, occupanti, vita, hazard, dati sito e livello prestazionale sono definiti e datati.
- Scenari includono interdipendenze e condizioni di guasto, non solo il pericolo principale.
- Modello, dati geotecnici/idraulici, combinazioni e criteri sono riconciliati con progetto.
- Elementi non strutturali, impianti, accessi, drenaggio e continuità sono inclusi quando pertinenti.
- Residual risk, recovery, manutenzione e trigger sono espliciti e assegnati.
- Nessuna parola “resiliente”, “antisismico” o “alluvione-proof” viene usata come certificazione senza verifica competente.

## Evidenza e provenienza

Conserva mappe e dataset hazard con fonte/data/scala, sopralluoghi, quote, sondaggi, modelli, calcoli, revisioni, foto, prove, scenari, assunzioni, manutenzioni, recovery exercise e decision log. Distingui osservato, modellato, assunto, simulato e approvato. Proteggi mappe di vulnerabilità, occupanti e infrastrutture critiche.

## Fonti ufficiali e diritti

- [JRC — EN Eurocodes family](https://eurocodes.jrc.ec.europa.eu/en-eurocodes/eurocodes-family): Eurocode 8 e riferimenti europei per azione sismica e progettazione.
- [JRC — EN Eurocodes concepts](https://eurocodes.jrc.ec.europa.eu/en-eurocodes-about-en-eurocodes/major-concepts-en-eurocodes): azioni, robustezza, durabilità e affidabilità.
- [Dipartimento della Protezione Civile](https://www.protezionecivile.gov.it/it/): dati, allerte e pianificazione nazionale di protezione civile da verificare localmente.
- [ISPRA — dissesto idrogeologico](https://www.isprambiente.gov.it/it/attivita/suolo-e-territorio/dissesto-idrogeologico): dati istituzionali su pericolosità e territorio.

Matrice degli scenari, record e procedure sono originali. Diritti: official_reference_only_no_text_reproduced; Eurocodici, mappe, dataset e modelli di terzi restano soggetti a licenza e condizioni di riuso. I dati ufficiali non sostituiscono autorizzazione o progetto firmato.

## Confini professionali e legali

La skill non esegue progettazione strutturale, geotecnica, idraulica o aerodinamica firmata, non dichiara sicurezza, agibilità, conformità o autorizzazione e non ordina evacuazioni. Non sostituisce ingegnere, geologo, geotecnico, idraulico, protezione civile, gestore o autorità. Un modello di scenario non garantisce esito reale né elimina il rischio residuo.

## Failure modes

- **Hazard map fuori scala:** blocca l'inferenza e richiede dato idoneo al sito.
- **Evento singolo:** riapri per multi-hazard, interdipendenze e recovery.
- **Resilienza ridotta a struttura:** includi involucro, impianti, accessi, occupanti e manutenzione.
- **Return period trattato come previsione:** chiarisci probabilità, incertezza e non-stazionarietà.
- **Misura compensativa non mantenuta:** assegna inspection, trigger, owner e test periodico.
- **Calcolo presentato come certificazione:** cambia stato e instrada a professionista/autorità.

## Strumenti

Usa hazard register, GIS, site survey, scenario matrix, fragility/performance table, dependency map, recovery plan, monitoring trigger register e review log. Automatizza versioni, coordinate e coverage; non certificare né modificare progetto o piano di emergenza senza approvazione.
