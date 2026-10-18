---
name: construction-robotics-industrialization
description: Valutazione operativa di robot e processi industrializzati per costruzione, dal caso d'uso a simulazione, FAT/SAT, sicurezza e fallback; non autorizza macchine o sostituisce valutazione dei rischi e responsabili di cantiere.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: robotics, automazione e industrializzazione
---

# Robotics e industrializzazione controllata in cantiere

## Attivazione e input

Attiva questa skill quando un robot, cobot, sistema di deposizione, prefabbricazione automatizzata o digital workcell deve passare da demo a processo ripetibile. È una faccetta di readiness, sicurezza e trasferimento in produzione distinta da materials-construction-methods-prefab, cad-autocad-freecad e blender-3d-render: non comanda una macchina né sostituisce il datore di lavoro o il valutatore della conformità.

Prima raccogli obiettivo, elemento e tolleranza, ambiente e interferenze, materiale e variabilità, ciclo, produttività richiesta, alimentazione, operatori, manutenzione, interfacce BIM/PLC, dati di addestramento, modalità manuale, emergenza, recinzioni, marcatura e documentazione del fabbricante. Se sito, compito, analisi dei rischi, responsabile o fallback non sono definiti, lo stato è blocked.

## Workflow

1. **Gate del caso d'uso:** definisci task, input, output accettabile, envelope, takt, rework e KPI; separa ciclo simulato, prova in laboratorio e produttività reale.
2. **Gate della cella:** mappa robot, utensile, materiale, sensori, energia, rete, zona operativa, persone e vie di fuga; identifica pinch/crush, collisioni, caduta carico, polvere, rumore e clima.
3. **Gate del dato e del modello:** congela geometria, origine, tolleranze, coordinate, versioni di percorso e post-processore; registra mismatch tra modello, pezzo, supporto e posa reale.
4. **Gate di simulazione:** esegui collisione, reachability, singolarità, tempo, variabilità, errore sensore e perdita comunicazione; dichiara assunzioni e non convertire la simulazione in KPI di cantiere.
5. **Gate di prova:** definisci dry run, sample, FAT, SAT e prova di capacità con criteri pass/fail, misure, campione, operatore e stop conditions. Una demo del vendor non è FAT/SAT del sito.
6. **Gate sicurezza e conformità:** verifica istruzioni, protezioni, arresto, modo manuale, formazione, manutenzione, modifiche e valutazione dei rischi con i responsabili competenti; non bypassare interlock o consenso.
7. **Gate di industrializzazione:** emetti istruzione di lavoro, controllo qualità, manutenzione, ricambi, gestione versioni, piano di fallback e criteri di sospensione. Il processo è pronto solo se può fermarsi in sicurezza e ripartire tracciato.

## Output

Consegna un robotics_readiness_record con caso d'uso, layout, asset e versioni, assunzioni, simulazioni, rischi, prove FAT/SAT, KPI misurati, deviazioni, formazione, manutenzione, fallback, approvazioni e stato pilot, conditional o blocked. Collega ogni KPI a campione, ambiente, strumento e criterio.

## Quality gates

- Il KPI distingue simulazione, laboratorio, sito pilota e produzione.
- Cella, operatori, materiali, interfacce e vie di fuga sono identificati.
- Arresto, modo sicuro, interlock, manutenzione e fallback sono provati o marcati non verificati.
- FAT e SAT hanno criteri, campioni, log e responsabili differenti.
- Il percorso macchina e il modello hanno versione, origine e tolleranza riconciliate.
- L'automazione non autorizza l'esercizio e non chiude la valutazione dei rischi.

## Evidenza e provenienza

Registra manuali e dichiarazioni del fabbricante, configurazione, seriali, firmware, codice/percorso, modello geometrico, simulazione, log, video contestualizzati, misure, checklist, incidenti/quasi incidenti, formazione e approvazioni. I dati di sicurezza e i file del vendor sono accessibili secondo contratto; non estrarre o redistribuire software proprietario oltre la licenza.

## Fonti ufficiali e diritti

- [Regolamento (UE) 2023/1230 sulle macchine](https://eur-lex.europa.eu/eli/reg/2023/1230/oj): testo ufficiale e data di applicazione da verificare per il prodotto e il ruolo nella catena.
- [ISO 10218-1:2025](https://www.iso.org/standard/73933.html): riferimento ufficiale per requisiti di sicurezza dei robot industriali; consultare il testo con licenza e la parte applicabile.
- [ISO 10218, accesso Online Browsing Platform](https://www.iso.org/obp/ui?_escaped_fragment_=iso%3Apub%3APUB200102): riferimento editoriale per l'identificazione della serie; non è autorizzazione a copiare il contenuto.

Fonti UE e identificativi sono provenance ufficiale; gli standard ISO sono restricted. Procedura, gate, record e KPI di esempio sono originali e non riproducono manuali o clausole protette. Stato diritti della skill: reference_only; la responsabilità di conformità resta al fabbricante, datore di lavoro e professionisti competenti.

## Confini professionali e limiti

La skill non certifica macchina, marcatura CE, sicurezza funzionale, conformità del cantiere, qualità del prodotto o capacità produttiva. Non bypassa interlock, non impartisce comandi operativi e non sostituisce valutazione dei rischi, coordinamento sicurezza, fabbricante, integratore o manutentore. Simulazione e demo non provano condizioni ambientali, persone reali o variabilità di produzione.

## Failure modes

- **Demo del vendor scambiata per SAT:** riapri test con layout, operatori, materiali e criteri del sito.
- **Interlock bypassato per velocità:** stop immediato, ripristino configurazione sicura e revisione del rischio.
- **Ciclo simulato presentato come produttività:** misura tempi, setup, rifornimento, rework e fermi sul campione reale.
- **Modello e pezzo non allineati:** congela la versione, rifai calibrazione e verifica tolleranze.
- **Fallback assente:** blocca pilot e definisci procedura manuale sicura e soglia di sospensione.
- **Firmware o percorso non tracciati:** ritira l'esito, registra configurazione e ripeti prove interessate.

## Strumenti

Usa simulatore con report, digital twin versionato, checklist FAT/SAT, registro rischi, issue tracker e KPI di produzione con campione. Automatizza collisioni, versioni e completezza dei log; l'automazione non prende decisioni di sicurezza senza supervisione autorizzata.
