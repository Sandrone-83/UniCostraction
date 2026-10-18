---
name: mep-energy-systems
description: Definisce e coordina impianti MEP, rinnovabili, automazione e prestazioni energetiche con bilanci, interfacce, commissioning e confini professionali chiari.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: impianti meccanici, elettrici, idrici ed energia
---

# Impianti MEP e sistemi energetici

## Attivazione

Usa la skill per requisiti, concept, confronto di alternative, coordinamento, capitolati, submittal, messa in servizio e monitoraggio di HVAC, idrico-sanitario, elettrico, antincendio, automazione, fotovoltaico, accumulo e sistemi di gestione dell'energia. L'attivazione non autorizza il dimensionamento firmato o la dichiarazione di conformità.

## Input

Raccogli uso, occupazione, orari, territorio climatico, involucro, orientamento, rilievo dell'esistente, carichi, utenze, potenze disponibili, qualità dell'acqua, vincoli antincendio, rumore, accessi, manutenzione, budget e obiettivi energetici. Richiedi bollette o misure con periodo, apparecchiature, schemi, manuali, tariffe e dati di fabbrica. Marca misurato, documentato, assunto o da campagna.

## Workflow

1. Scrivi requisiti funzionali: comfort, salute, continuità, sicurezza, energia, controllo, rumore, manutenzione e resilienza.
2. Definisci confini del sistema e baseline: edificio, impianti inclusi, usi esclusi, periodo, clima, profili e condizioni iniziali.
3. Stima domanda e carichi con unità, ipotesi e sensibilità; separa potenza, energia, rendimento, fattore di contemporaneità e consumo misurato.
4. Confronta architetture e vettori energetici per prestazione, interfacce, regolazione, spazio, rumore, costi, manutenzione e fine vita.
5. Coordina schemi, locali tecnici, attraversamenti, scarichi, quadri, reti, accessi e modello informativo; registra interferenze e responsabilità.
6. Definisci specifiche, submittal, prove in fabbrica o cantiere, taratura, avviamento, bilanciamento, commissioning, formazione e as-built.
7. Imposta misure e KPI post-intervento, con periodo di osservazione, qualità del dato, soglie e gestione delle anomalie.

## Output

Produci registro requisiti, bilancio dei carichi e dell'energia, matrice alternative, schemi funzionali e delle interfacce, specifiche e submittal, piano prove/commissioning, registro contatori e KPI, piano manutenzione e decisioni aperte. Ogni conclusione deve indicare dati, modello, periodo e responsabile dell'approvazione.

## Quality gates

- Carichi, profili, unità, rendimenti e condizioni al contorno sono espliciti e riproducibili.
- Gli schemi includono protezioni, separazioni, accessi, drenaggi, regolazione, sicurezza e manutenzione pertinenti.
- Le prestazioni promesse distinguono calcolo, dichiarazione del fabbricante, prova e misura in esercizio.
- Commissioning verifica sequenze, allarmi, bilanciamento, sensori, setpoint, documenti e formazione.
- Baseline e KPI non confondono consumo dell'edificio con rendimento di un singolo componente.

## Provenienza ed evidenza

Conserva rilievi, bollette, data logger, schemi, versioni software, file di calcolo, datasheet, curve, verbali di prova, tarature, as-built e log BMS con hash e data. Indica qualità, copertura e buchi del dato. Un modello energetico o un render non dimostra la prestazione reale senza misura e periodo comparabile.

## Controllo versione, territorio e data

Verifica Stato membro, regione, zona climatica, data di progetto, recepimento nazionale e versione vigente di legge, norma, incentivo, tariffa e regola del gestore. Congela la data di riferimento per consumi e costi; riapri l'analisi se cambiano carichi, uso, involucro, incentivi o connessione. Non usare una guida GSE/ENEA o una scheda datata come requisito vigente senza controllo.

## Confini professionali e legali

La skill non sostituisce progettista impiantista, professionista antincendio, certificatore energetico, installatore abilitato, gestore di rete o manutentore. Non rilascia APE, dichiarazioni di conformità, diagnosi energetiche asseverate, pratiche incentivi o autorizzazioni. In caso di rischio elettrico, gas, incendio o acqua contaminata, sospendi l'azione e coinvolgi il soggetto competente.

## Failure modes

- **Bollette non confrontabili:** normalizza periodo, clima, occupazione e usi oppure dichiara il confronto non valido.
- **Potenza nominale trattata come resa reale:** verifica condizioni operative, curve, regolazione e misura.
- **Interferenza di cantiere:** blocca la chiusura, assegna owner e aggiorna schema/modello prima della posa.
- **KPI senza baseline:** definisci contatori, periodo e metodo prima di dichiarare un risparmio.
- **Incentivo scaduto:** congela la pagina ufficiale e verifica requisiti, data e documenti del caso.

## Strumenti

Usa fogli controllati, strumenti di calcolo energetico autorizzati, viewer BIM/MEP, analisi dati, logger, strumenti di commissioning, repository versionato e sistemi BMS con accesso tracciato. Ogni script deve mostrare unità, input, versione e log; non modificare setpoint o impianti reali senza autorizzazione.

## Fonti ufficiali e diritti

- [EUR-Lex — Direttiva (UE) 2024/1275](https://eur-lex.europa.eu/eli/dir/2024/1275/oj): `rights_state: official_public_legal_text_verify_current_consolidation`; testo pubblico europeo da verificare per recepimento e data applicabile.
- [Normattiva — D.Lgs. 192/2005](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2005-08-19;192!vig=): `rights_state: official_public_legal_text_verify_current_consolidation`; fonte legislativa pubblica italiana; controllare consolidato e decreti attuativi.
- [GSE — Efficienza energetica](https://www.gse.it/servizi-per-te/efficienza-energetica): `rights_state: official_reference_only_no_text_reproduced`; portale istituzionale; contenuti, incentivi e condizioni vanno verificati alla data dell'intervento.

Non riprodurre testi, tabelle o manuali delle fonti. Le prestazioni di prodotto e i programmi di incentivo restano soggetti a condizioni, licenze e verifica del caso concreto.
