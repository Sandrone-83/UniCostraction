---
name: occupational-health-exposure-hygiene
description: Imposta screening, campionamento e controllo delle esposizioni professionali in cantiere con metodo di igiene industriale, senza sostituire DVR, medico competente, laboratorio o decisione sanitaria.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: salute occupazionale, esposizioni e igiene industriale
---

# Salute occupazionale, esposizioni e igiene industriale

## Attivazione e input

Attiva questa skill quando una lavorazione può esporre persone a polveri, silice cristallina respirabile, fibre, fumi di saldatura, agenti chimici, rumore, vibrazioni, calore, agenti biologici o contaminanti di demolizione e serve trasformare un sospetto in un piano di controllo misurabile. Non è una diagnosi medica e non è il DVR.

Raccogli processo e sostanza, SDS e denominazione commerciale, mansioni e gruppi omogenei di esposizione, durata e frequenza, ventilazione, confinamento, meteo, attrezzature, controlli esistenti, incidenti, misure precedenti, laboratorio, analita, limite con giurisdizione e data, sorveglianza sanitaria aggregata e privacy. Se agente, popolazione, attività o metodo non sono identificati, lo stato è blocked.

## Workflow

1. **Gate della caratterizzazione:** separa sorgente, via, gruppo esposto, attività rappresentativa e periodo; considera picchi e attività non routinarie, non solo il turno medio.
2. **Gate del rischio iniziale:** usa SDS e fonti istituzionali per classificare pericolo e controlli; marca limite legale, valore guida, limite interno e incertezza senza mischiarli.
3. **Gate del piano di campionamento:** definisci personale/area, durata, numero, strategia, portata o dosimetria, laboratorio, bianco, catena di custodia, QA/QC e criteri di rappresentatività.
4. **Gate della gerarchia dei controlli:** privilegia eliminazione/sostituzione, confinamento e captazione, bagnatura o aspirazione, organizzazione e tempi; considera DPI come misura residua verificata.
5. **Gate della misura:** registra strumento, calibrazione pre/post, operatore, posizione, attività, anomalie e campione; non interpolare un risultato perso senza dichiararlo.
6. **Gate dell'interpretazione:** confronta risultato e incertezza con il limite corretto per la giurisdizione e l'analita, senza convertire una misura in diagnosi; tratta risultato non rappresentativo come informazione insufficiente.
7. **Gate della chiusura:** assegna azione, owner, scadenza, riesame e coinvolgimento di RSPP, medico competente, lavoratori, laboratorio e datore di lavoro secondo ruolo.

## Output

Produci un exposure_control_record con agente, gruppo, attività, metodo, dati grezzi, QA/QC, risultati, limiti/versioni, incertezza, gerarchia controlli, decisioni e stato characterized, controlled, conditional o blocked. I dati individuali sanitari restano fuori dal report operativo; usa solo aggregati autorizzati.

## Quality gates

- Agente, gruppo omogeneo, attività, durata e condizioni sono definiti e osservati.
- Piano e metodo sono adeguati alla frazione o al fenomeno, con laboratorio competente e catena di custodia.
- Calibrazione, bianchi, campioni invalidi, recuperi e incertezza sono documentati.
- Limite, unità, periodo di riferimento e versione sono espliciti; non si usa un TLV come automaticamente legale.
- La gerarchia dei controlli è verificata prima di affidarsi al DPI.
- Ogni superamento o risultato non rappresentativo genera rivalutazione e comunicazione ai ruoli competenti.

## Evidenza e provenienza

Conserva inventario di sostanze e SDS, osservazioni di processo, gruppo e turni, piano e schede di campionamento, calibrazioni, catena di custodia, rapporto del laboratorio, calcoli, limiti con data, foto delle sorgenti, formazione e azioni. Distingui dato analitico, stima, dichiarazione del fornitore e interpretazione. Proteggi identità, cartelle sanitarie e risultati individuali secondo minimizzazione e accesso per ruolo.

## Fonti ufficiali e diritti

- [Normattiva — D.Lgs. 81/2008](https://www.normattiva.it/eli/id/2008/04/30/008G0104/CONSOLIDATED): titoli su valutazione, agenti chimici, cancerogeni, rumore e vibrazioni, da verificare nella versione vigente.
- [INAIL — agenti chimici](https://www.inail.it/portale/prevenzione-e-sicurezza/it/come-fare-per/conoscere-il-rischio/agenti-chimici.html): orientamenti istituzionali e collegamenti ai rischi specifici.
- [INAIL — banca dati esposizione silice](https://www.inail.it/portale/prevenzione-e-sicurezza/it/come-fare-per/conoscere-il-rischio/banca-dati-esposizione-silice.html): dati istituzionali da usare come contesto, non come sostituto del campionamento locale.
- [EU-OSHA — legislation](https://osha.europa.eu/en/legislation): quadro europeo da filtrare per agente e periodo.

Workflow, schede e record sono originali. Diritti: official_reference_only_no_text_reproduced; le SDS, norme tecniche, metodi analitici, dati INAIL e rapporti di laboratorio conservano i diritti e le condizioni dei rispettivi titolari. Non si copiano valori o testi oltre il necessario riferimento.

## Confini professionali e legali

La skill non svolge diagnosi, sorveglianza sanitaria, idoneità, valutazione firmata del rischio, scelta definitiva del limite, analisi accreditata o prescrizione sanitaria. Non sostituisce datore di lavoro, RSPP, medico competente, igienista industriale qualificato, laboratorio o autorità. L'assenza di superamento non prova l'assenza di rischio se il campione è non rappresentativo o il controllo è cambiato.

## Failure modes

- **Campione comodo:** riapri la strategia e includi lavorazioni, picchi e gruppi realmente esposti.
- **Limite fuori giurisdizione:** sospendi il confronto e ricostruisci norma, data, unità e popolazione.
- **Calibrazione mancante:** marca il dato invalidato o condizionato e ripeti la misura.
- **SDS generica:** blocca la classificazione del prodotto e chiedi SDS aggiornata e fornitore.
- **DPI come unica risposta:** verifica sostituzione, captazione e manutenzione prima della selezione del DPI.
- **Privacy violata:** rimuovi identificativi, limita destinatari e usa risultati aggregati.

## Strumenti

Usa registro sostanze, matrice sorgente-via-gruppo, GHE register, schede di campionamento, calibratore/dosimetro, chain-of-custody, foglio di calcolo con unità, laboratorio e issue tracker. Automatizza controllo campi, versioni, scadenze e grafici; non automatizzare diagnosi, idoneità o decisioni di esposizione senza riesame competente.
