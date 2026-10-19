---
name: expropriation-easement-land-acquisition
description: Organizza il fascicolo tecnico-operativo per espropri, servitù e acquisizione di aree, collegando particelle, titoli, vincoli, fasi procedimentali e indennità senza sostituire autorità o consulenza legale.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: espropri, servitù e acquisizione aree
---

# Espropri, servitù e acquisizione di aree

## Attivazione e input

Attiva questa skill quando un'opera o un intervento richiede disponibilità di aree, occupazione temporanea, costituzione/modifica di servitù o trasferimento di diritti reali. È distinta da italian-urban-planning-cadastre-pa, che tratta titoli urbanistici e catasto, e da public-procurement-company-contracts, che tratta affidamento ed esecuzione del contratto.

Raccogli ente promotore, opera, finalità, territorio e giurisdizione, particelle e subalterni, intestazioni e quote, elaborati approvati, vincolo preordinato, dichiarazione di pubblica utilità, termini, occupazione, servitù richiesta, stato delle comunicazioni, stime, offerte, opposizioni, accordi, accessi e dati personali. Se particella, titolare, fase, atto o scadenza non sono verificabili, lo stato è blocked.

## Workflow

1. **Gate della giurisdizione:** identifica autorità competente, legge applicabile, data di riferimento, variante regionale e regole dell'opera; non assumere che un modello nazionale valga per ogni ente.
2. **Gate della disponibilità:** riconcilia visure, mappe, tipo di diritto, titolarità, quote, gravami, occupanti e rilievo con una tabella particella-attributo-fonte.
3. **Gate dell'opera:** collega ogni area a progetto, piano particellare, vincolo, dichiarazione di pubblica utilità, durata e uso temporaneo; segnala divergenze geometriche o procedimentali.
4. **Gate della sequenza:** costruisci timeline di comunicazioni, osservazioni, determinazioni, offerta, accettazione/non accettazione, decreto, immissione, trascrizione e restituzione, con responsabile e termine.
5. **Gate economico:** separa superficie, diritto acquisito, occupazione, danni, indennità provvisoria/definitiva, costi accessori e stima tecnica; registra metodo, data, fonte e soggetto abilitato.
6. **Gate dell'accordo:** prepara una matrice delle questioni aperte e degli allegati per il legale/ente; un accordo è pronto solo dopo verifica di poteri, identificazione, autorizzazioni e condizioni sospensive.
7. **Gate di chiusura:** controlla verbali, firme, pagamenti, registrazione/trascrizione, aggiornamento catastale, consegna area, ripristini e archivio della prova.

## Output

Produci un land_acquisition_record con giurisdizione, particella, diritto, fonte, stato procedimentale, mappa, soggetti, timeline, scadenze, stima, comunicazioni, rischi, documenti mancanti, escalation e stato screened, conditional, ready_for_authority_review o blocked. Non trasformare la scheda in decreto, offerta vincolante, accordo o parere.

## Quality gates

- Particelle, titolari, quote e confini sono riconciliati con fonti datate e non solo con una planimetria.
- Fase procedimentale, efficacia degli atti, termini e autorità sono verificati nella versione vigente e nel contesto territoriale.
- Acquisizione, servitù, occupazione temporanea e accesso sono separati per oggetto, durata e titolo.
- Ogni importo distingue dato, stima, indennità proposta, costo accessorio e decisione dell'autorità.
- Comunicazioni, ricevute, opposizioni, poteri e consenso/assenza di consenso hanno evidenza e custode.
- Nessun passaggio irreversibile è eseguito senza revisione professionale e autorizzazione del soggetto competente.

## Evidenza e provenienza

Conserva visure e mappe, titoli, estratti tavolari/ipotecari quando applicabili, piano particellare, rilievi, atti amministrativi, ricevute, protocolli, stime, fotografie, verbali, pagamenti e registro versioni. Marca fonte primaria, copia ricevuta, estrazione tecnica, inferenza e informazione da confermare. Le mappe e i dati personali sono accessibili solo ai ruoli necessari; non pubblicare nominativi o coordinate sensibili in esempi.

## Fonti ufficiali e diritti

- [Normattiva — D.P.R. 8 giugno 2001, n. 327](https://www.normattiva.it/atto/caricaDettaglioAtto?atto.codiceRedazionale=001G0372&atto.dataPubblicazioneGazzetta=2001-08-16): testo unico delle disposizioni su espropriazione per pubblica utilità; verificare testo vigente, regione e atto concreto.
- [Agenzia delle Entrate — servizi catastali e ipotecari](https://www.agenziaentrate.gov.it/portale/schede/pagamenti/servizi-catastali-e-ipotecari): canali ufficiali per dati e servizi, da usare secondo accesso e scopo autorizzati.
- [Normattiva — D.P.R. 380/2001](https://www.normattiva.it/atto/caricaDettaglioAtto?atto.articolo.numero=0&atto.codiceRedazionale=001G0429&atto.dataPubblicazioneGazzetta=2001-10-20): coordinamento con titoli edilizi quando pertinente.

La procedura, le tabelle e i record sono originali. Diritti: `official_public_legal_text_verify_current_consolidation` per testi normativi e `official_reference_only_no_text_reproduced` per pagine e servizi; visure, mappe, perizie, contratti e dati di terzi mantengono diritti, segreti e condizioni di accesso propri.

## Confini professionali e legali

La skill non dichiara pubblica utilità, non determina titolarità definitiva, non quantifica in modo vincolante l'indennità, non firma atti, non negozia rinunce e non dispone occupazioni o accessi. Non sostituisce autorità espropriante, avvocato, notaio, tecnico estimatore, topografo, gestore del bene o responsabile del procedimento. Una sovrapposizione cartografica non prova da sola un diritto reale né la validità dell'atto.

## Failure modes

- **Visura scambiata per titolo:** separa intestazione catastale, titolo di provenienza e verifica ipotecaria.
- **Vincolo o dichiarazione non vigente:** blocca la timeline e richiedi atto, data e pubblicazione verificabili.
- **Servitù descritta come acquisto:** chiarisci diritto, durata, utilità, fondo dominante/servente e manutenzione.
- **Offerta inviata senza potere:** prepara una bozza controllata e instrada al soggetto autorizzato.
- **Mappa non coerente col rilievo:** non dedurre superfici; apri issue geometrica e richiedi rilievo qualificato.
- **Scadenza persa:** registra data certa, fuso, fonte e responsabile; segnala escalation prima del termine.

## Strumenti

Usa registro particella-diritto-fonte, GIS/CAD con sistema di riferimento dichiarato, document register, timeline degli atti, matrice dei soggetti, issue log, calcolo superfici, stima versionata, protocollo e approval log. Automatizza controlli di coerenza e scadenze; non inviare PEC, firmare, pagare o registrare in autonomia.
