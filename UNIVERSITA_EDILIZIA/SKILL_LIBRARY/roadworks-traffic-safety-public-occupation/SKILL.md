---
name: roadworks-traffic-safety-public-occupation
description: "Pianificazione controllata dei cantieri stradali e dell'occupazione di suolo pubblico, con schema di segnalamento, fasi di traffico, percorsi protetti e fascicolo autorizzativo."
metadata:
  library: "UNIVERSITA_EDILIZIA/SKILL_LIBRARY"
  version: "G31.1"
  domain: "sicurezza cantieri stradali e occupazione suolo"
---

# Cantieri stradali, traffico e occupazione di suolo

Questa skill prepara il piano operativo per lavori, depositi e cantieri sulla strada o nelle sue pertinenze e coordina la pratica di occupazione del suolo pubblico. E' una faccetta di interfaccia con strada, pedoni, ente proprietario e polizia: non e progettazione stradale e non coincide con la logistica interna di cantiere.

## Attivazione e input

Attivare per scavi, posa sottoservizi, manutenzione, ponteggi, gru o depositi che invadono carreggiata, marciapiede, banchina, pista ciclabile o area pubblica. Richiedere:

- strada, progressiva, classe, ente proprietario, centro abitato, limite, traffico e trasporto pubblico;
- planimetria georeferenziata, sezione, area e durata dell'occupazione, fasi, orari, mezzi e materiali;
- percorso pedonale e ciclabile, accessi, emergenza, disabili, passi carrabili, fermate e utenze interferenti;
- schema di segnalamento temporaneo, barriere, luci, movieri, deviazioni, gestione code e condizioni meteo/notturne;
- titolo lavori, ordinanza o autorizzazione richiesta, istanza comunale/ente strada, polizza, canone e responsabili.

Se ente proprietario, geometria dell'occupazione o durata non sono confermati, lo stato e `permit_pending`.

## Workflow

1. Identificare il titolare della strada e la competenza per autorizzazione/concessione, ordinanza di regolazione, occupazione suolo e ripristino. Separare i procedimenti e registrare protocollo, scadenza e prescrizioni.
2. Rilevare situazione esistente con foto, misure, traffico, percorsi e sottoservizi. Tracciare la fascia realmente occupata e le aree di sicurezza, senza usare una planimetria generica.
3. Scomporre i lavori in fasi e per ciascuna costruire schema di segnalamento coerente con categoria di strada, velocita, visibilita, senso alternato, deviazioni e presenza di pedoni.
4. Progettare separatamente protezione degli addetti esposti al traffico e continuita dell'utenza: barriere, distanze, zavorre, retro-riflettenza, luci, accessi, attraversamenti e soccorso.
5. Coordinare schema, cronoprogramma e istanza con ente proprietario, comune, polizia stradale/locale, gestori trasporto e sottoservizi. Non avviare lavori sulla sola ricevuta di invio se l'atto richiesto non e efficace.
6. Prima dell'apertura eseguire walk-through e foto georeferenziate; verificare che segnali temporanei e permanenti non siano in conflitto. Stabilire responsabile per ispezione a inizio turno, dopo eventi e a fine fase.
7. Gestire variazioni: riduzione carreggiata, cambio orario, pioggia, coda, incidente, ritardo, nuova interferenza o modifica della durata riaprono il controllo e possono richiedere nuova ordinanza.
8. Chiudere con rimozione ordinata del segnalamento, ripristino, pulizia, riapertura, verbale e prova fotografica. Conservare autorizzazione, log controlli, incidenti e comunicazioni.

## Output

Produrre un `roadwork_public_occupation_record` con `screening`, `permit_pending`, `ready_to_setup`, `live_with_inspections`, `phase_closed` o `blocked`; tavola e schemi per fase; matrice strada-ente-permesso; percorsi protetti; responsabili e turni; checklist di posa/ispezione; log variazioni, incidenti, ripristino e ricevute.

## Quality gates

- **Competenza**: ente proprietario, autorita di regolazione e ufficio occupazione sono confermati.
- **Spazio/tempo**: area, fasce di sicurezza, fasi, date e orari coincidono tra piano e istanza.
- **Segnalamento**: schema scelto dal disciplinare applicabile, coerente con strada e situazione reale.
- **Utenti vulnerabili**: percorso continuo e accessibile per pedoni, ciclisti, persone con disabilita e soccorso.
- **Addetti**: separazione dal traffico, visibilita, DPI, mezzi e procedure sono coordinati con il PSC/POS.
- **Autorizzazione**: concessione, ordinanza, nulla osta, canone e prescrizioni hanno stato verificabile.
- **Ispezione**: controllo iniziale, notturno/meteo, dopo urto e a fine fase hanno evidenza.
- **Chiusura**: segnalamento rimosso, strada ripristinata e verbale di riapertura archiviati.

## Evidenza e provenienza

Conservare rilievo, foto con data/posizione, planimetria e revisione, schemi di segnalamento, conteggi o fonti del traffico, istanze, ordinanze, autorizzazioni, comunicazioni, checklist, log di ispezione e verbali. Ogni segnale critico deve avere ragione, fase, responsabile e prova di posa. Una tavola teorica non prova la sicurezza della configurazione in strada.

## Fonti ufficiali e diritti

I contenuti della skill sono originali e sintetici: rispettare copyright, licenze, termini d'uso dei portali e diritti sugli asset; non redistribuire testi o allegati protetti.

- [D.Lgs. 285/1992, art. 21, su Normattiva](https://www.normattiva.it/uri-res/N2Ls?urn%3Anir%3Astato%3Adecreto.legislativo%3A1992-04-30%3B285~art21%21vig=): opere, depositi e cantieri stradali; `official_public_legal_text_verify_current_consolidation`.
- [D.P.R. 495/1992, art. 30, su Normattiva](https://www.normattiva.it/atto/caricaDettaglioAtto?atto.articolo.numero=30&atto.codiceRedazionale=092G0531&atto.dataPubblicazioneGazzetta=1992-12-28): segnalamento temporaneo e aggiornamenti; `official_public_legal_text_verify_current_consolidation`.
- [D.M. 10 luglio 2002 in Gazzetta Ufficiale](https://www.gazzettaufficiale.it/eli/id/2002/09/26/02A09965/sg): disciplinare tecnico e schemi per categoria di strada; `official_public_legal_text_verify_current_consolidation`.
- [D.M. 10 luglio 2002, allegato sul sito MIT](https://www.mit.gov.it/sites/default/files/media/normativa/2016-02/Decreto_Ministeriale_10-07-2002_all_1.pdf): copia di riferimento del disciplinare; `official_reference_only_no_text_reproduced`.
- [D.Lgs. 81/2008 su Normattiva](https://www.normattiva.it/eli/id/2008/04/30/008G0104/CONSOLIDATED): tutela degli addetti esposti al traffico; `official_public_legal_text_verify_current_consolidation`.

Regolamenti comunali, ordinanze e moduli di occupazione possono variare: sono fonti locali da identificare per ente e data. Non riprodurre testi protetti; registrare URL, protocollo e versione consultata.

## Confini professionali e legali

La skill non rilascia autorizzazione, ordinanza o concessione, non assume il ruolo dell'ente proprietario, del coordinatore sicurezza, del direttore lavori o del progettista della segnaletica. Non abilita l'apertura del cantiere e non garantisce la sicurezza solo perche lo schema e conforme sulla carta. Ogni lavoro su strada resta subordinato agli atti efficaci e alle verifiche sul posto.

## Failure modes

- Occupazione iniziata con sola istanza o silenzio non qualificato: bloccare e verificare l'efficacia dell'atto.
- Schema generico riusato su strada diversa: ricalcolare categoria, visibilita, velocita e fasi.
- Marciapiede chiuso senza percorso alternativo accessibile: bloccare l'allestimento.
- Segnali temporanei in conflitto con permanenti o mancata rimozione: aprire non conformita urgente.
- Fase, durata o deviazione cambiate senza comunicazione: rivalutare ordinanza e autorizzazione.
- Ispezione fatta solo all'avvio: introdurre controlli dopo pioggia, urto, notte e cambio turno.
- Traffico pubblico confuso con logistica interna: assegnare piani, responsabili e fonti distinti.

## Strumenti

Usare GIS/CAD, rilievo fotografico, schemi del disciplinare MIT, gestione permessi/protocollo, checklist mobile con timestamp, geofencing, registro turni, canale di escalation e archivio di ordinanze. L'automazione puo controllare coerenza geometrica e scadenze, ma non posare segnali, regolare il traffico o inviare istanze senza personale e autorita responsabili.
