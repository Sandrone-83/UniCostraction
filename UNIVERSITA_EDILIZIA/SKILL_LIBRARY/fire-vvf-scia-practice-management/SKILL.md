---
name: fire-vvf-scia-practice-management
description: Governa il ciclo documentale delle pratiche VVF, valutazione progetto, SCIA, rinnovo e integrazioni per attività soggette, senza sostituire professionista antincendio, Comando o progetto prestazionale.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: prevenzione incendi, pratiche VVF e SCIA
---

# Prevenzione incendi: pratiche VVF e SCIA

## Attivazione e input

Attiva questa skill quando un'attività deve essere inquadrata ai fini della prevenzione incendi e deve gestire valutazione progetto, SCIA, rinnovo periodico, voltura, integrazioni, controlli o chiusura presso il Comando VVF. È distinta da fire-engineering-performance-verification, che tratta analisi prestazionale, e da site-fire-emergency-management, che tratta piani e risposta di emergenza in cantiere.

Raccogli attività e codice DPR 151/2011, titolare, sede, categoria, capacità/superfici/quantità, stato autorizzato, progetto, regola tecnica, approccio ordinario/prestazionale, impianti, compartimenti, esodo, accesso VVF, professionista, asseverazioni/certificazioni, modulistica PIN, portale, protocolli, sopralluoghi, prescrizioni, rinnovi e varianti. Se attività, categoria, regola tecnica o pratica precedente sono incerti, lo stato è blocked.

## Workflow

1. **Gate dell'assoggettabilità:** identifica attività, parametri, categoria e Comando competente; registra esclusioni e assunzioni da verificare, senza dichiarare l'esenzione.
2. **Gate dell'assetto:** riconcilia stato di fatto, titoli, layout, impianti, carichi incendio, affollamento, accessi, compartimenti e attività interferenti con elaborati e sopralluogo.
3. **Gate della procedura:** seleziona valutazione progetto, SCIA, rinnovo, voltura, non aggravio o integrazione secondo pratica e stato; controlla modulistica PIN e versione vigente.
4. **Gate del fascicolo:** verifica relazione, tavole, asseverazioni, certificazioni, dichiarazioni di corretta installazione, prodotti, impianti, resistenza al fuoco, imposte, deleghe e firma del soggetto competente.
5. **Gate dell'invio:** controlla Comando, portale/PEC, pagamento, file, nominativi, protocollo e ricevute; separa ricevuta di presentazione, controllo formale, sopralluogo e atto.
6. **Gate dei controlli:** registra richieste, visita, prescrizioni, esito, non conformità, termini e azioni; non chiudere una pratica da una ricevuta o da un rapporto incompleto.
7. **Gate del mantenimento:** imposta scadenza rinnovo, registro controlli, manutenzioni, modifiche, cambio titolare, aggravio rischio e trigger per nuova valutazione.

## Output

Produci un fire_vvf_practice_record con attività, categoria, titolare, Comando, pratica, versione PIN, document register, professionista, firme, ricevute, stato istruttoria, prescrizioni, scadenze, manutenzione, issue e stato screened, conditional, ready_for_authorized_submission, filed, approved_or_received o blocked. Non chiamare la pratica CPI, SCIA efficace o conformità senza fonte e stato verificati.

## Quality gates

- Attività, parametri e categoria sono documentati con fonte e data.
- Stato di fatto, progetto, impianti, esodo, accesso, compartimenti e carichi sono coerenti.
- Modulo, regola tecnica, asseverazione, certificazioni, firme e competenze sono pertinenti.
- Invio, ricevuta, protocollo, controllo, sopralluogo, prescrizione ed esito sono distinti.
- Rinnovi, modifiche, aggravio rischio, manutenzioni e titolare hanno owner e scadenze.
- Nessuna pratica è firmata, inviata o presentata come autorizzata senza approvazione professionale e del titolare.

## Evidenza e provenienza

Conserva planimetrie, relazioni, calcoli, regole tecniche, modulistica PIN, visure/nomine, asseverazioni, certificazioni REI, dichiarazioni prodotti/impianti, ricevute, protocolli, verbali, prescrizioni, registro manutenzioni e rinnovi. Marca fonte VVF/norma, dato del titolare, elaborato tecnico, certificato di terzi, assunzione e issue. Proteggi dati dell'attività, elaborati di sicurezza e credenziali del portale; non riprodurre moduli o guide oltre i diritti applicabili.

## Fonti ufficiali e diritti

- [Normattiva - D.P.R. 1 agosto 2011, n. 151](https://www.normattiva.it/atto/caricaDettaglioAtto?atto.codiceRedazionale=011G0193&atto.dataPubblicazioneGazzetta=2011-09-22): procedimenti, categorie e controlli di prevenzione incendi.
- [Vigili del Fuoco - modulistica prevenzione incendi](https://www.vigilfuoco.it/servizi-le-aziende-e-i-professionisti/servizi-line-di-prevenzione-incendi/modulistica): modelli PIN aggiornati per valutazione progetto, SCIA e documenti collegati.
- [Vigili del Fuoco - testi coordinati delle regole tecniche](https://www.vigilfuoco.it/servizi-le-aziende-e-i-professionisti/prevenzione-incendi/testi-coordinati-di-prevenzione/testi-coordinati-di-prevenzione-regole-tecniche-suddivise-per-attivita?page=28): regole tecniche e chiarimenti da verificare per attività.
- [Vigili del Fuoco - raccolta norme e circolari](https://www.vigilfuoco.it/servizi-le-aziende-e-i-professionisti/prevenzione-incendi/testi-coordinati-di-prevenzione/testi-coordinati-di-prevenzione-regole-tecniche-suddivise-per-attivita?page=28): riferimento istituzionale per aggiornamenti e professionisti antincendio.

La procedura, i registri e le matrici sono originali. Diritti: `official_public_legal_text_verify_current_consolidation` per il regolamento e `official_reference_only_no_text_reproduced` per VVF, modulistica e regole; PIN, moduli, marchi, relazioni, certificati, software e documenti del cliente mantengono diritti e licenze propri.

## Confini professionali e legali

La skill non determina la categoria in via vincolante, non progetta misure antincendio, non assevera, non certifica resistenza o impianti, non firma, non presenta SCIA, non rilascia CPI e non autorizza l'esercizio. Non sostituisce professionista antincendio, progettista, installatore, manutentore, titolare, Comando VVF o autorità. La ricevuta della pratica non è una garanzia di sicurezza o di esito.

## Failure modes

- **Categoria copiata da pratica vecchia:** riapri parametri, destinazione, soglie e regola vigente.
- **SCIA confusa con CPI o approvazione:** registra titolo, controllo, esito e condizioni separatamente.
- **Asseverazione senza certificazioni:** blocca e richiedi evidenza dei prodotti, impianti e prove.
- **Modifica trattata come irrilevante:** verifica aggravio rischio e trigger di nuova pratica.
- **Modulo PIN superato:** usa la modulistica VVF vigente e conserva versione.
- **Rinnovo dimenticato:** crea registro scadenze, manutenzioni, titolare e responsabilità.

## Strumenti

Usa activity/category matrix, fire-practice register, PIN document checklist, source/version ledger, drawing-to-site checklist, signature/delegation register, VVF submission log, prescription tracker, renewal calendar e maintenance evidence register. Automatizza completezza e scadenze; non inviare pratiche o dichiarare conformità in autonomia.
