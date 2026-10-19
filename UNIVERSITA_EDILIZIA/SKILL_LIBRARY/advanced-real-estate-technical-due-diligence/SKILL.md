---
name: advanced-real-estate-technical-due-diligence
description: Conduce due diligence tecnica immobiliare multi-dominio su stato fisico, titoli, impianti, rischi e costi con registro evidenze, senza rilasciare pareri legali, certificazioni o garanzie di valore.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: due diligence tecnica immobiliare avanzata
---

# Due diligence tecnica immobiliare avanzata

## Attivazione e input

Attiva questa skill quando un acquirente, finanziatore, proprietario o gestore deve valutare condizioni, rischi, capex, conformità documentale e priorità di un immobile prima di acquisizione, rifinanziamento, sviluppo o contenzioso tecnico. È distinta da italian-urban-planning-cadastre-pa, che tratta il quadro urbanistico-catastale, e da documents-pdf-computo-sal-due-diligence, che tratta estrazione e confronto documentale.

Raccogli immobile, diritto e uso previsto, incarico e data, titoli e planimetrie, rilievi, stato autorizzato/realizzato, catasto come evidenza non sostitutiva, vincoli, strutture, involucro, impianti, incendio, energia, accessibilità, amianto/contaminanti, manutenzione, contratti, CAPEX/OPEX, eventi, assicurazioni e accesso al sito. Se perimetro, data, destinazione o documenti critici sono incerti, lo stato è blocked.

## Workflow

1. **Gate del mandato:** definisci scopo, standard di review, data di riferimento, esclusioni, assunzioni, confidenza, destinatario e uso del report.
2. **Gate dell'identità:** riconcilia indirizzo, particelle, unità, superfici, volumetrie, disegni, foto, modelli e accessi; registra discrepanze senza normalizzarle.
3. **Gate del titolo tecnico:** confronta stato autorizzato, stato catastale, stato rilevato, opere, destinazioni, vincoli, agibilità, impianti e manutenzione; separa dato pubblico, dichiarazione e osservazione.
4. **Gate dell'ispezione:** pianifica walkthrough per sistemi, sicurezza, involucro, struttura apparente, MEP, incendio, acqua, energia, accessibilità e condizioni nascoste; registra limitazioni e campioni.
5. **Gate del rischio:** classifica issue per probabilità, conseguenza, urgenza, costo, evidenza e dipendenza; separa difetto osservato, non conformità da verificare, rischio e opportunità.
6. **Gate economico:** stima ordine di grandezza di CAPEX/OPEX, priorità, indagini e downtime con base, data e range; non trasformare un budget preliminare in valore immobiliare.
7. **Gate del report:** prepara executive risk register, evidenze, gap, azioni e decisioni richieste; sottoponi aspetti legali, strutturali, ambientali e impiantistici ai professionisti competenti.

## Output

Produci un property_technical_due_diligence_record con asset identity, scope, document register, site observations, system findings, risks, missing evidence, cost ranges, priority, assumptions, limitations e stato screened, conditional o blocked. Distingui sempre conformità verificata, coerenza documentale, evidenza assente e parere specialistico necessario.

## Quality gates

- Immobile, diritto, uso, data di riferimento, superfici e perimetro sono riconciliati.
- Fonti, revisioni, sopralluoghi, accessi negati e aree non osservabili sono registrati.
- Urbanistica, catasto, struttura, MEP, incendio, energia, ambiente e accessibilità sono separati per competenza.
- Ogni finding ha evidenza, severità, incertezza, owner e prossimo controllo.
- Costi hanno inclusioni/esclusioni, base date, range e non doppio conteggio.
- Report e fotografie proteggono riservatezza e non dichiarano garanzie o certificazioni non emesse.

## Evidenza e provenienza

Conserva incarico, checklist, titoli, tavole, report, foto localizzate, rilievi, certificati, libretti, manutenzioni, contratti, interviste, misure, issue log, cost workbook e revisioni. Marca originale, copia, dichiarazione, osservazione, inferenza e raccomandazione. Proteggi dati dell'immobile, occupanti, accessi, sicurezza e informazioni commerciali.

## Fonti ufficiali e diritti

- [Normattiva — DPR 380/2001](https://www.normattiva.it/atto/caricaDettaglioAtto?atto.articolo.numero=0&atto.codiceRedazionale=001G0429&atto.dataPubblicazioneGazzetta=2001-10-20): quadro edilizio nazionale da verificare nella consolidazione vigente.
- [Agenzia delle Entrate — servizi catastali e ipotecari](https://www.agenziaentrate.gov.it/portale/schede/pagamenti/servizi-catastali-e-ipotecari): fonte istituzionale per dati e servizi, con verifica di accesso e valore.
- [ISO 55001](https://www.iso.org/standard/83054.html): contesto ufficiale per gestione dell'asset e ciclo di vita.
- [Vigili del Fuoco — prevenzione incendi](https://www.vigilfuoco.it/servizi-le-aziende-e-i-professionisti/prevenzione-incendi): fonti e procedimenti antincendio quando pertinenti.

Il workflow, il risk register e le checklist sono originali. Diritti: official_reference_only_no_text_reproduced; atti, planimetrie, certificati, banche dati, foto del sito e report di terzi restano soggetti a privacy, licenza e autorizzazione.

## Confini professionali e legali

La skill non certifica conformità urbanistica, catastale, strutturale, energetica o antincendio, non determina valore di mercato, non rilascia agibilità, non interpreta definitivamente titoli o contratti e non sostituisce architetto, ingegnere, geologo, impiantista, tecnico antincendio, legale, agente o autorità.

## Failure modes

- **Catasto trattato come stato legittimo:** separa banca dati, titolo e rilievo.
- **Foto scambiata per ispezione completa:** registra accessi, limiti e indagini mancanti.
- **Dichiarazione venditore non verificata:** marca fonte e richiedi prova indipendente.
- **Issue multidominio assegnata a un solo tecnico:** scomponi responsabilità e interfacce.
- **CAPEX puntuale senza scope:** usa range, base date, esclusioni e confidenza.
- **Report usato come garanzia:** ribadisci data, limitazioni, incarico e approvazione specialistica.

## Strumenti

Usa asset identity sheet, document register, due diligence checklist, room/system matrix, photo log, issue/risk register, cost range workbook, GIS/model viewer e report template controllato. Automatizza indicizzazione, gap, scadenze e collegamenti; non concludere conformità o valore in autonomia.
