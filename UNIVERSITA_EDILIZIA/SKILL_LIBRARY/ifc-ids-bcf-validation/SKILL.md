---
name: ifc-ids-bcf-validation
description: Valida modelli IFC contro requisiti IDS e gestisce issue BCF con evidenza, coordinate, responsabilità e stato di chiusura; non certifica il progetto o il contratto.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: IFC, IDS e BCF
---

# Validazione IFC con IDS e workflow BCF

## Attivazione e input

Attiva questa skill per validare proprietà, classificazioni, relazioni, unità e geometria di un IFC rispetto a requisiti machine-checkable e per trasformare i risultati in issue BCF. È più stretta di `bim-ifc-openbim`: non redige l'intero EIR/BEP e non sostituisce la federazione o l'accettazione contrattuale.

Richiedi IFC originale, schema e MVD, IDS/XSD e versione, requisiti contrattuali collegati, coordinate e sistema di riferimento, disciplina, milestone, software/exporter, CDE, BCF version/API, responsabili, severità e criterio di chiusura. Se manca il requisito normativo o contrattuale, produci una verifica informativa limitata e non una non-conformità.

## Procedura originale

1. Registra file, hash, schema IFC, exporter, timestamp, IDS/BCF version e configurazione checker in una busta di consegna immutabile.
2. Esegui preflight: parse schema, unità, coordinate, project/site/building/storey, GUID univoci, relazioni, oggetti senza classe, proprietà duplicate e geometrie non leggibili.
3. Interpreta ogni requisito IDS in quattro colonne distinte: presenza, cardinalità, valore/formato e provenienza/responsabile. Non trasformare un requisito descrittivo in un test inventato.
4. Esegui il checker e salva risultato per requisito e oggetto con `pass/fail/blocked/not_applicable`, versione della regola e falso positivo possibile.
5. Per ogni issue crea topic BCF con GUID, titolo neutro, severità, componente/GUID IFC, viewpoint, camera/selection, snapshot, descrizione del fatto, requisito, owner, scadenza e criterio verificabile di chiusura.
6. Non modificare l'IFC durante il test. Se si richiede una correzione, genera una nuova revisione collegata all'originale e riesegui l'intero sottoinsieme interessato.
7. Chiudi un issue solo quando il nuovo modello supera il test e un revisore conferma la corrispondenza tra evidenza, requisito e stato; mantieni la cronologia BCF.

## Output

Consegna manifest degli input, log di validazione, report per requisito/entità, IDS usato, elenco issue BCF, viewpoints e snapshot, matrice owner/scadenze, diff tra revisioni e verbale di accettazione informativa con eccezioni approvate. Distingui sempre `non verificato` da `fallito`.

## Quality gates

- IFC e IDS sono identificati per release e schema; un parser che tollera errori non rende valido il file.
- La trasformazione delle coordinate è documentata e verificata su elementi noti, non stimata dalla sola vista.
- Ogni fail rimanda a un requisito e a un'entità o relazione individuabile.
- Un issue senza viewpoint o criterio di chiusura resta aperto, anche se la descrizione è plausibile.
- I dati machine-checkable e la revisione dell'intento progettuale restano separati.
- La chiusura è sulla revisione corretta del modello, non su uno screenshot o su un export non collegato.

## Evidenza e provenienza

Conserva IFC/IDS/BCF originali, hash, versione del checker, ambiente, log completo, query/regole, timestamp e operatore. Per ogni esito conserva GUID IFC, percorso di proprietà, valore osservato, valore atteso e fonte del requisito. Per i viewpoint registra camera, selezione e coordinate; uno snapshot senza modello non è evidenza sufficiente.

## Confini professionali e diritti

IFC, IDS e BCF verificano scambio e gestione delle informazioni; non certificano calcolo strutturale, sicurezza, conformità urbanistica, prestazione o esecuzione. Non pubblicare modelli con dati personali, sicurezza critica o proprietà intellettuale senza autorizzazione. Standard e specifiche possono avere licenze proprie: non copiare schema, testo o asset oltre quanto consentito.

## Failure modes

- **IDS senza fonte o troppo permissivo:** sospendi la non-conformità e chiedi requisito, responsabile e release.
- **GUID cambiati in export:** non collegare automaticamente le issue; esegui una mappa di equivalenza revisionata.
- **Coordinate locali incoerenti:** blocca viewpoint e clash finché il sistema di riferimento non è concordato.
- **Pass del checker con geometria illeggibile:** classifica come `blocked`, non come pass.
- **Issue duplicata o senza owner:** deduplica per requisito/entità/fase, preservando la storia.
- **Eccezione approvata usata come conformità:** mantieni separati `pass`, `waived` e `not_applicable`.

## Strumenti e fonti ufficiali

Usa validator IFC e IDS versionati, parser schema, viewer con supporto BCF, API BCF e CDE con audit. Verifica le release effettive presso:

- [buildingSMART — IFC schema specifications](https://technical.buildingsmart.org/standards/ifc/ifc-schema-specifications/): release e schema IFC ufficiali.
- [buildingSMART — Information Delivery Specification](https://technical.buildingsmart.org/projects/information-delivery-specification-ids/): IDS come specifica machine-readable dei requisiti informativi.
- [buildingSMART — BCF API repository](https://github.com/buildingSMART/BCF-API): API e versioni open per issue e coordinamento.
- [ISO — ISO 19650](https://www.iso.org/standard/68078.html): riferimento di gestione informativa, a pagamento/restricted; non riprodurre il testo.

## Stato dei diritti

IFC, IDS e BCF sono riferimenti ufficiali/open da verificare per release, licenza e implementazione; ISO 19650 è riferimento ufficiale con accesso/licenza propri. La procedura di validazione e il modello di issue sono originali e non equivalgono a una certificazione buildingSMART o ISO.
