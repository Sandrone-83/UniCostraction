---
name: training-competence-operational-handover
description: Progetta verifica di competenze, briefing, addestramento e handover operativo per asset e processi di cantiere, senza certificare abilitazioni o sostituire datore di lavoro e responsabili tecnici.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: formazione, competenza e handover operativo
---

# Formazione, competenza e handover operativo

## Attivazione e input

Attiva questa skill quando un nuovo processo, impianto, macchina, fase o asset passa dalla progettazione/costruzione all'esercizio e occorre dimostrare che le persone assegnate sanno operare, isolare, reagire e mantenere il sistema. È distinta da commissioning-facility-asset-handover, che governa il pacchetto dati dell'asset, e da training generico: qui il focus è la competenza osservabile legata a una funzione e a un handover.

Raccogli ruoli e responsabilità, mansioni, prerequisiti, qualifiche obbligatorie, lingua e accessibilità, procedure, manuali e as-built, rischi, scenari normali/anomali/emergenza, matrice competenze, trainer qualificato, prove, osservazioni, limiti di autorizzazione, turni, reperibilità, manutenzione e criteri di accettazione. Se ruolo, attività o fonte della competenza non sono definiti, lo stato è blocked.

## Workflow

1. **Gate del ruolo:** collega persona o gruppo a compiti, responsabilità, autorizzazioni, escalation e divieti; separa familiarizzazione, addestramento, supervisione e abilitazione legale.
2. **Gate della gap analysis:** confronta competenze richieste e dimostrate per fase, modalità, rischio e lingua; non usa la presenza a una lezione come prova di capacità.
3. **Gate del piano:** definisci obiettivi osservabili, contenuti minimi, trainer, materiali controllati, pratica, teoria, assessment e refresh dopo modifica o evento.
4. **Gate della pratica:** esegui dimostrazione e prova su scenari normali, anomali, arresto, isolamento, allarme e recovery, in condizioni sicure e con supervisione.
5. **Gate della valutazione:** registra criteri, tentativi, errori, feedback, accomodamenti e risultato; un esito non raggiunto produce retraining o limitazione, non una firma automatica.
6. **Gate dell'handover:** collega asset, procedure, setpoint, allarmi, spares, contatti, warranty, registri e training; esegui walkthrough e domande di ritorno del gestore.
7. **Gate operativo:** rilascia solo capacità dimostrata, owner e canale di escalation; programma refresh, osservazione sul lavoro e verifica dopo turnover, modifica o incidente.

## Output

Produci un competence_handover_record con ruolo, task, requisito, gap, corso/briefing, prova osservata, trainer, materiali, autorizzazioni, asset collegati, limitazioni e stato trained, competent_observed, supervised_only o blocked. Conserva separati attendance, learning check, practical demonstration e authorization.

## Quality gates

- Ruoli, compiti, prerequisiti, lingua, accessibilità e livello di autorizzazione sono espliciti.
- Procedure, manuali, as-built e allarmi usati nella formazione sono revisionati e coerenti con l'asset.
- Prova pratica osserva condizioni operative e di anomalia, con criteri pass/fail e sicurezza.
- Trainer, valutatore e approvatore hanno competenza e indipendenza proporzionate.
- Handover include contatti, escalation, isolamenti, manutenzione, dati e limiti, non solo una riunione.
- Turnover, modifica, near miss o prestazione debole riaprono la verifica e il refresh.

## Evidenza e provenienza

Conserva competency matrix, job/task analysis, learning objectives, materiali e revisioni, attendance, quiz, checklist pratica, osservazioni, feedback, registri di autorizzazione, manuali, as-built, asset register, contatti, punch list e change log. Minimizza dati personali e sanitari, limita accessi e conserva il periodo necessario secondo regole dell'organizzazione.

## Fonti ufficiali e diritti

- [ISO 10015:2019](https://www.iso.org/cms/live/live/en/sites/isoorg/contents/data/standard/06/94/69459.html): linee guida ufficiali per gestione delle competenze e sviluppo delle persone.
- [INAIL — formazione](https://www.inail.it/portale/formazione/it.html): riferimenti istituzionali per formazione e sicurezza sul lavoro.
- [Normattiva — D.Lgs. 81/2008](https://www.normattiva.it/eli/id/2008/04/30/008G0104/CONSOLIDATED): obblighi e ruoli di salute e sicurezza, da verificare nella versione vigente.
- [ISO 41001](https://www.iso.org/cms/%20render/live/en/sites/isoorg/contents/data/standard/06/80/68021.html): contesto ufficiale per gestione di facility e servizi nel passaggio all'esercizio.

Matrice, prove, registri e handover package sono originali. Diritti: official_reference_only_no_text_reproduced; standard, manuali dei fabbricanti, procedure del committente, materiali formativi e dati personali restano soggetti a licenza, riservatezza e autorizzazione.

## Confini professionali e legali

La skill non rilascia patentini, abilitazioni, idoneità sanitaria, qualifiche professionali o autorizzazioni legali; non sostituisce datore di lavoro, formatore qualificato, RSPP, medico competente, responsabile tecnico, gestore, manutentore o autorità. Un training record non prova da solo competenza continuativa, sicurezza dell'asset o conformità normativa.

## Failure modes

- **Presenza scambiata per competenza:** richiedi prova osservata e criterio.
- **Manuale obsoleto:** sospendi il handover, riallinea revisioni e ripeti briefing pertinente.
- **Valutatore non competente:** invalida l'esito o lo rende condizionato e assegna riesame.
- **Procedura solo teorica:** aggiungi scenario pratico sicuro, supervisione e recovery.
- **Turnover non gestito:** aggiorna matrice, nomina sostituti e limita accesso operativo.
- **Dati personali eccessivi:** minimizza, separa risultati sanitari e applica accesso per ruolo.

## Strumenti

Usa role/task matrix, competency gap register, controlled training materials, attendance log, practical assessment sheet, authorization matrix, asset handover checklist, contact/escalation card e refresh calendar. Automatizza scadenze, revisioni e coverage; non rilasciare autorizzazioni operative o attestazioni legali in autonomia.
