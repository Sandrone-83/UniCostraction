---
name: rail-transport-interface-safety
description: Coordina rischi e responsabilità alle interfacce ferroviarie e di trasporto tra infrastruttura, esercizio, lavori, sistemi e utenti senza sostituire impresa ferroviaria, gestore o autorità di sicurezza.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: ferrovie, trasporti e sicurezza di interfaccia
---

# Ferrovie e trasporti: sicurezza delle interfacce

## Attivazione e input

Attiva questa skill quando una modifica, un cantiere, un nuovo impianto o un esercizio di trasporto crea interfacce tra infrastruttura, veicolo, segnalamento, energia, stazione, passeggeri, manutenzione e imprese. È una faccetta di hazard log e gestione cooperativa del rischio distinta da construction-site-safety, mep-energy-systems e road-infrastructure-bridge-engineering: non autorizza l'esercizio, non firma una valutazione CSM e non impartisce comandi alla circolazione.

Prima raccogli sistema e confini, gestore dell'infrastruttura, impresa ferroviaria, detentore, appaltatori, asset, orari e possesso linea, interfacce fisiche/digitali/organizzative, requisiti tecnici, scenari di esercizio, lavori, manutenzione, utenti e lingua/competenza degli operatori. Registra autorità nazionale, versione di TSI/regolamento, proposer, assessor e criteri di accettazione. Se confini, responsabili o stato di esercizio sono ignoti, lo stato è blocked.

## Workflow

1. **Gate del sistema:** disegna confine, contesto operativo, modalità degradate, dipendenze e soggetti; separa responsabilità contrattuale, tecnica, operativa e di sicurezza.
2. **Gate delle interfacce:** enumera interfaccia e scambio: binario-veicolo, segnalamento-energia, cantiere-circolazione, stazione-passeggero, software-dati, manutenzione-esercizio. Ogni interfaccia ha owner, input/output e stato.
3. **Gate dell'hazard:** costruisci hazard log con evento, causa, barriera, conseguenza, severità, frequenza, evidenza, requisito e residual risk; includi errore umano, perdita di comunicazione, lavori simultanei e condizioni degradate.
4. **Gate della cooperazione:** convoca i soggetti interessati, concorda criteri, scenari, dati e misure; registra divergenze e non trasferire un rischio all'ente vicino senza accettazione documentata.
5. **Gate della modifica:** congela baseline di configurazione, software, segnalamento, mezzi, procedure, formazione e possesso linea; ogni modifica riapre hazard, test e piano di ritorno.
6. **Gate della dimostrazione:** pianifica analisi, simulazione, prova sul campo, fault injection controllata e test di comunicazione con precondizioni, protezioni, witness e stop conditions.
7. **Gate di entrata e monitoraggio:** prepara dossier di safety, competenze, manutenzione, indicatori, incident/near miss, audit e revisione post-avvio; l'autorizzazione finale resta ai ruoli e all'autorità competenti.

## Output

Consegna un rail_interface_safety_record con confini, attori, mappa interfacce, hazard log, requisiti, misure, baseline, test, evidenze, residual risk, ritorno sicuro e stato identified, conditional o blocked. Ogni hazard aperto ha owner, scadenza, barriera e criterio di chiusura.

## Quality gates

- Sistema, fase, possesso linea, autorità, proposer e soggetti di interfaccia sono identificati.
- Hazard, requisiti, barriere e responsabilità sono collegati e versionati.
- Modifica, configurazione, software, procedure e formazione hanno baseline.
- Test e dimostrazioni coprono esercizio normale, degradato, manutenzione e comunicazione persa.
- Residual risk, criteri di accettazione e indipendenza dell'assessor sono espliciti.
- Nessun dossier viene presentato come autorizzazione all'esercizio o come ordine di circolazione.

## Evidenza e provenienza

Conserva diagrammi di sistema, contratti/interfacce approvate, hazard log, specifiche, configurazioni, versioni software, registri di formazione, analisi, test, log di evento, verbali, firme, hash e audit trail. Marca fonte, autore, data, ambiente, configurazione e grado di indipendenza. Planimetrie, procedure operative e dati di sicurezza sono riservati e accessibili per ruolo.

## Fonti ufficiali e diritti

- [ERA — Common Safety Methods](https://www.era.europa.eu/domains/common-safety-methods): metodi comuni europei per gestione, valutazione e supervisione della sicurezza ferroviaria.
- [ERA — CSM risk evaluation and assessment](https://www.era.europa.eu/content/recommendation-common-safety-method-risk-evaluation-and-assessment_en): guida e riferimenti ufficiali per valutazione del rischio e organismi di valutazione.
- [Direttiva (UE) 2016/798 su EUR-Lex](https://eur-lex.europa.eu/eli/dir/2016/798/oj): quadro europeo di sicurezza ferroviaria da verificare per attuazione e ruolo.
- [ANSFISA](https://www.ansfisa.gov.it/): autorità italiana e riferimenti nazionali per sicurezza ferroviaria e trasporti.

Le fonti UE e istituzionali sono riferimenti di autorità; non si copiano testi, guide, TSI o procedure proprietarie. Il modello di interfaccia, l'hazard log e i gate sono originali. Stato diritti: official_reference_only_no_text_reproduced; standard e documenti tecnici possono essere restricted.

## Confini professionali e legali

La skill non autorizza circolazione, possesso linea, modifica del segnalamento, accesso in sede, lavori o ritorno all'esercizio. Non sostituisce impresa ferroviaria, gestore, ECM, responsabile sicurezza, proposer, assessor, manutentore, ANSFISA o altra autorità. Un hazard log completo non dimostra da solo sicurezza accettabile o conformità autorizzativa.

## Failure modes

- **Interfaccia assegnata a tutti e quindi a nessuno:** nomina owner, approvatore e soggetto di escalation.
- **Rischio trasferito al vicino:** registra interdipendenza e richiedi accettazione e barriera condivisa.
- **Test in configurazione diversa:** blocca il risultato e riconcilia software, asset, procedure e possesso linea.
- **Scenario degradato omesso:** aggiungi perdita comunicazione, energia, dati, formazione e lavori simultanei.
- **Hazard chiuso con una promessa:** richiedi barriera verificata, evidenza, owner e criterio di chiusura.
- **Dossier scambiato per autorizzazione:** cambia stato in blocked e indirizza all'autorità.

## Strumenti

Usa diagramma di sistema, interface control document, hazard log, requisito-traceability matrix, configuration register, test manager e registro competenze. Automatizza ID, link, versioni, scadenze e completezza; non automatizzare accettazione del rischio, comandi operativi o autorizzazione all'esercizio.
