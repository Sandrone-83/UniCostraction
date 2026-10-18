---
name: bim-ifc-openbim
description: Definisce requisiti informativi, coordina modelli IFC/openBIM e verifica consegne con controlli machine-checkable e revisione umana.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: BIM e interoperabilità
---

# BIM, IFC e openBIM

## Attivazione

Usa la skill per AIR/EIR, BEP, CDE, naming, classificazioni, federazione, clash/issue, IDS, scambio IFC e handover. Non assumere che un file IFC sia completo, conforme al contratto o idoneo a costruire senza requisiti e revisione.

## Input minimo

Richiedi obiettivi e usi BIM, attori, ruoli, milestone, requisiti informativi, formato/versione IFC, coordinate, classificazione, proprietà richieste, CDE, livelli di autorizzazione e criteri di accettazione.

## Workflow

1. Traduce gli obiettivi in requisiti verificabili con codice, responsabile, fase e fonte.
2. Definisce convenzioni di nomi, revisioni, coordinate, unità, origine, proprietà e stato di approvazione.
3. Costruisce IDS o checklist equivalente per gli attributi realmente richiesti; evita requisiti non necessari.
4. Riceve e inventaria file, applicativo, versione, esportatore, data e hash.
5. Esegue controlli schema, geometria, proprietà, relazioni, unità, coordinate, duplicati e federazione.
6. Apre issue con evidenza, severità, assegnatario, scadenza e criterio di chiusura.
7. Consegna report di conformità parziale o totale, eccezioni approvate e pacchetto riproducibile.

## Output

Produci EIR/AIR/BEP o estratti, matrice requisiti, IDS, registro file, report checker, issue list, mappa coordinate, federazione e handover con stato (bozza, in revisione, accettato, rifiutato, eccezione approvata).

## Quality gates

- Versione e schema IFC dichiarati; un modello non valido non viene "riparato" silenziosamente.
- Coordinate e unità sono verificate su riferimenti noti e su almeno una vista.
- Requisiti controllati distinguono presenza, valore, formato e responsabilità.
- Il report elenca pass, fail, non verificabile e falso positivo possibile.
- Accettazione e responsabilità sono registrate fuori dal solo risultato automatico.

## Evidenza e provenienza

Registra hash, software/exporter, versione schema, configurazione checker, log e data. Conserva gli input originali e non sostituire una consegna con un export corretto senza collegamento tra i due.

## Confini professionali e legali

IFC/IDS sono strumenti di scambio e verifica informativa, non certificazioni edilizie, strutturali o di sicurezza. ISO 19650, capitolato, contratto e regole dell'ente prevalgono nel progetto. Non pubblicare modelli contenenti dati personali, sicurezza critica o proprietà intellettuale senza autorizzazione.

## Failure modes

- **Versione IFC non concordata:** sospendi il confronto e concorda schema/semantica.
- **Clash visuale senza responsabilità:** trasformalo in issue con priorità e owner.
- **IDS troppo permissivo:** aggiungi solo requisiti fondati e testabili.
- **Coordinate locali incoerenti:** non correggere a occhio; chiedi trasformazione documentata.
- **Modello "BIM" senza dati:** segnala la copertura effettiva, non il nome del file.

## Strumenti

Usa CDE con audit, viewer IFC, validator schema, IDS checker, strumenti di federazione e report HTML/CSV. Il checker automatizza controlli ripetitivi; l'interpretazione di intenti, eccezioni e responsabilità resta umana.

## Fonti ufficiali e diritti

- [buildingSMART — IFC schema specifications](https://technical.buildingsmart.org/standards/ifc/ifc-schema-specifications/): standard e release ufficiali; verificare versione e termini di riuso.
- [buildingSMART — IDS](https://www.buildingsmart.org/standards/bsi-standards/information-delivery-specification-ids/): standard ufficiale; usare schema e licenza della release effettiva.
- [ISO — ISO 19650](https://www.iso.org/standard/68078.html): standard a pagamento/restricted; nessun testo copiato.

La skill è una procedura originale di gestione e controllo, non una certificazione BIM.
