---
name: site-fire-emergency-management
description: Organizza piani di emergenza, prevenzione incendio e prove per cantieri in evoluzione, senza sostituire valutazione, formazione, comando dell'emergenza o adempimenti del datore di lavoro.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: sicurezza antincendio e piani di emergenza di cantiere
---

# Sicurezza antincendio e piani di emergenza di cantiere

## Attivazione e input

Attiva questa skill quando il cantiere cambia fase, layout, accessi, lavorazioni a caldo, deposito di combustibili o disponibilità di impianti e deve essere aggiornato il controllo operativo dell'emergenza. È una faccetta di pianificazione e prova del piano, distinta da fire-engineering-performance-verification, che tratta la dimostrazione prestazionale dell'opera, e da construction-site-safety, che tratta il sistema generale di sicurezza.

Raccogli almeno: area e fasi di lavoro, planimetria aggiornata, accessi per soccorritori, vie di esodo e punti di raccolta, presenza e numero variabile di addetti, imprese e turni, sorgenti di innesco, depositi e gas, lavorazioni a caldo, recinzioni, impianti provvisori, allarmi, mezzi estinguenti, contatti, condizioni meteo e interfacce con edifici occupati o viabilità pubblica. Se mancano layout, ruoli, fase o destinatari del piano, lo stato è blocked.

## Workflow

1. **Gate della fase:** congela la configurazione del giorno o della fase, i rischi introdotti e le condizioni che rendono nullo il piano precedente.
2. **Gate delle responsabilità:** mappa datore di lavoro, coordinamento, preposti, addetti antincendio e primo soccorso, imprese, visitatori e referente del sito; collega ogni azione a un sostituto e a un canale verificabile.
3. **Gate della mappa operativa:** traccia percorsi realmente liberi, cancelli, chiavi, punti di raccolta, accesso dei Vigili del Fuoco, ostacoli, mezzi e aree interdette; allega data, revisione e foto localizzate.
4. **Gate delle sorgenti:** registra lavori a caldo, bombole, carburanti, rifiuti combustibili, ricariche, impianti provvisori e separazioni; applica permesso di lavoro, presidio, estinzione e controllo post-lavorazione quando previsto dal responsabile.
5. **Gate della risposta:** definisci rilevazione, allarme, chiamata, primo intervento entro competenza, evacuazione, assistenza a persone vulnerabili, conteggio al punto di raccolta e divieto di rientro.
6. **Gate della prova:** esegui briefing o esercitazione proporzionata, osserva tempi e ostacoli senza simulare azioni pericolose, registra partecipanti, deviazioni e azioni correttive.
7. **Gate della transizione:** riemetti il piano dopo cambio di fase, incendio mancato, near miss, modifica di accesso, nuova impresa, meteo severo o indisponibilità di una misura; conserva la versione ritirata.

## Output

Produci un emergency_site_record con fase, planimetria revisionata, matrice ruoli-contatti, scenari ragionevoli, istruzioni operative, risorse, briefing/prove, osservazioni, azioni e stato ready, conditional o blocked. Il record deve indicare ciò che è verificato sul posto e ciò che richiede decisione del responsabile dell'emergenza.

## Quality gates

- Fase, presenza, layout, accessi e interfacce con terzi sono datati e approvati dal responsabile.
- Vie di esodo, punti di raccolta e accesso soccorritori sono liberi, identificabili e controllati in campo.
- Ruoli, sostituzioni, numeri e procedure di chiamata sono testati senza usare numeri inventati.
- Permessi e controlli per lavori a caldo e depositi temporanei hanno owner e scadenza.
- Addetti, imprese e visitatori ricevono informazione coerente con lingua, turno e rischio.
- Ogni prova o evento aggiorna un registro di deviazioni; un piano non provato non è presentato come efficace.

## Evidenza e provenienza

Conserva planimetrie con revisione, sopralluoghi, foto con posizione e data, registro imprese e presenze, autorizzazioni ai lavori a caldo, controlli estintori e allarmi, verbali di briefing/prova, tempi osservati, chiamate di test autorizzate, near miss e chiusure. Marca dati osservati, dichiarati, simulati e approvati. Minimizza nominativi e numeri personali; limita il piano completo a chi ne ha bisogno.

## Fonti ufficiali e diritti

- [Normattiva — D.Lgs. 81/2008](https://www.normattiva.it/eli/id/2008/04/30/008G0104/CONSOLIDATED): base nazionale di salute e sicurezza, da verificare nella consolidazione vigente.
- [Gazzetta Ufficiale — DM 2 settembre 2021](https://www.gazzettaufficiale.it/eli/gu/2021/10/04/237/sg/html): gestione della sicurezza antincendio in esercizio ed emergenza e formazione degli addetti.
- [Vigili del Fuoco — prevenzione incendi](https://www.vigilfuoco.it/servizi-le-aziende-e-i-professionisti/prevenzione-incendi): portale istituzionale e regole tecniche da verificare per l'attività.
- [ISO 22320](https://www.iso.org/standard/50038.html): riferimento ufficiale per gestione degli incidenti, consultato senza riprodurne il testo.

La procedura, la matrice operativa e i record sono originali. Diritti della skill: official_reference_only_no_text_reproduced; fonti legali pubbliche da verificare alla data, standard ISO e manuali VVF soggetti ai rispettivi diritti. Non sono inclusi moduli o illustrazioni di terzi.

## Confini professionali e legali

La skill non redige una valutazione del rischio firmata, non determina l'assoggettabilità, non autorizza lavorazioni, non sostituisce il datore di lavoro, il RSPP, il coordinatore, gli addetti, il professionista antincendio, i Vigili del Fuoco o il comando dell'emergenza. Non ordina evacuazioni reali né invita a rientrare. Ogni istruzione di campo va adattata e approvata secondo ruoli, formazione, sito e normativa applicabile.

## Failure modes

- **Planimetria obsoleta:** sospendi il piano, fai sopralluogo e riemetti la revisione.
- **Addetto assente:** blocca la dichiarazione di copertura e assegna sostituzione o misura temporanea autorizzata.
- **Lavoro a caldo senza presidio:** interrompi in sicurezza, informa il responsabile e riapri solo con permesso e controlli.
- **Punto di raccolta occupato:** segnala l'ostacolo, definisci alternativa verificata e aggiorna la mappa.
- **Prova trasformata in azione reale:** termina il test, chiarisci la simulazione e separa esercitazione da evento.
- **Numero di emergenza non verificato:** usa solo canali istituzionali e locali confermati; non inventare contatti.

## Strumenti

Usa checklist di fase, planimetria annotata, registro permessi, matrice ruoli-contatti, QR o copie controllate del piano, modulo prova, issue log e dashboard di scadenze. Automatizza versioni, promemoria e completezza dei campi; non automatizzare ordini di evacuazione, chiamate ai soccorsi o dichiarazioni di conformità.
