---
name: autocad-api-drawing-qa
description: Automatizza operazioni AutoCAD via API e sottopone i disegni a QA riproducibile su geometria, proprietà, riferimenti e pubblicazione; non sostituisce rilievo, progetto o firma.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: AutoCAD API e drawing QA
---

# AutoCAD API, automazione e QA del disegno

## Attivazione e input

Attiva questa skill quando serve leggere, modificare, generare o controllare DWG/DXF tramite AutoLISP, ActiveX/COM, .NET/ObjectARX, ObjectDBX o automazioni equivalenti. È una faccetta operativa di `cad-autocad-freecad`: non decide la geometria di progetto e non tratta una macro eseguita come prova di correttezza.

Prima di operare raccogli file originale e copia di lavoro, release AutoCAD/API, sistema operativo, unità, UCS/WCS, scala, standard layer/naming, xref, font, plotter, misura campione, obiettivo, autorizzazione di scrittura e formato atteso. Registra se il job deve aprire AutoCAD o può usare ObjectDBX/strumenti offline.

## Workflow

1. Crea un `job.json` con input, API target, versione, comando, parametri, timestamp, operatore e hash; rifiuta input non identificati.
2. Esegui un inventario non distruttivo: header, unità, extents, layer, blocchi, proxy, xref, annotazioni, layout, viewport, stili, errori di apertura e oggetti non nativi.
3. Applica una matrice `regola -> selettore -> aspettativa -> severità -> evidenza`; ogni modifica deve avere un comando o script versionato e un output separato.
4. Esegui in transazione o su copia: salva, chiudi e riapri il DWG; non usare `purge`, audit, bind, explode o conversioni senza log delle perdite e approvazione.
5. Calcola controlli indipendenti: distanza/area su geometrie campione, chiusura polilinee, duplicati, layer vietati, testi fuori tavola, xref irrisolti, scale annotative, plot e naming.
6. Confronta pre/post con report machine-readable e vista indipendente. Un controllo `pass` significa solo che la regola è passata sul file testato.
7. Pubblica PDF/DXF o package solo dopo il gate umano; conserva sorgente, script, log, report, output e hash collegati alla stessa revisione.

## Output

Consegna un registro job, inventario iniziale, script o comando riproducibile, DWG/DXF derivato, report QA con `pass/fail/non_verificabile`, snapshot o immagini delle anomalie, PDF di plot e manifest SHA-256. Elenca esplicitamente gli oggetti non letti, le API non disponibili e le proprietà non controllate.

## Quality gates

- La release AutoCAD/API e il riferimento di compatibilità sono dichiarati; l'automazione non presume che COM, .NET e ObjectARX siano intercambiabili.
- Una misura nota e un punto di controllo confermano unità, coordinate e verso degli assi.
- Il file viene riaperto dopo il salvataggio e il PDF viene esaminato a scala dichiarata.
- I controlli geometrici distinguono errori sintattici, violazioni dello standard grafico e giudizi di progetto.
- Ogni trasformazione ha copia originale, log, codice di ritorno e risultato riproducibile.
- Un fail, un proxy o un xref mancante blocca la pubblicazione se impatta l'uso richiesto.

## Evidenza e provenienza

Conserva hash e percorso relativo dell'originale, versione API, DLL/TLB/add-in, script, variabili di sistema, locale, driver di stampa, dipendenze e log. Per ogni violazione salva handle/entità, layer, coordinate o pagina, regola applicata e screenshot quando il testo non basta. Se un controllo è euristico dichiaralo.

## Confini professionali e legali

API e QA non certificano il rilievo, la conformità urbanistica, la sicurezza, la stabilità o la titolarità del disegno. Non firmare, timbrare, inviare o sovrascrivere il master senza autorizzazione. Verifica licenze Autodesk, SDK, font, blocchi, immagini, xref e codice di terzi prima di redistribuire un package. Non riprodurre testo protetto della documentazione ufficiale.

## Failure modes

- **API/versione incompatibile:** ferma il job, registra la combinazione reale e riprova solo con target dichiarato.
- **COM apre un documento diverso:** verifica titolo, percorso canonico e handle prima di modificare.
- **Unità o UCS impliciti:** non correggere a occhio; usa punti di controllo e trasformazione registrata.
- **Audit/purge modifica dati:** ripristina dalla copia e segnala l'impatto, senza occultare la perdita.
- **QA solo visivo:** aggiungi controllo numerico e riapertura indipendente; il render di una tavola non basta.
- **Xref/font/proxy assenti:** marca il risultato come parziale e non sostituire silenziosamente l'asset.

## Strumenti

Usa l'API prevista dalla release, PowerShell/.NET o AutoLISP solo in ambienti autorizzati, un viewer indipendente, parser DXF, PDF viewer e checksum. Verifica prima la documentazione Autodesk per la release effettiva:

- [Autodesk — AutoCAD Developer and ObjectARX Help](https://help.autodesk.com/view/OARX/2027/ENU/): API .NET, ObjectARX, ActiveX e AutoLISP; riferimento ufficiale da versione.
- [Autodesk — Managed .NET compatibility](https://help.autodesk.com/cloudhelp/2026/ENU/AutoCAD-Customization/files/GUID-A6C680F2-DE2E-418A-A182-E4884073338A.htm): matrice di compatibilità; non inferire compatibilità dal solo nome del plugin.
- [Autodesk — ActiveX API migration](https://help.autodesk.com/cloudhelp/2026/ENU/AutoCAD-ActiveX/files/GUID-FF023966-A01D-4B64-8957-7C0F02BF8162.htm): riferimenti alle type library e release.

## Fonti ufficiali e diritti

Autodesk ObjectARX e AutoCAD API: https://help.autodesk.com/view/OARX/2027/ENU/

Le fonti Autodesk sono riferimenti ufficiali alla documentazione e alle API, non autorizzazioni a redistribuire SDK, codice, font o file proprietari. La procedura e i controlli qui descritti sono originali; verificare sempre termini, release e licenze dell'ambiente reale.
