---
name: cad-autocad-freecad
description: Pulisce, costruisce, controlla e pubblica elaborati CAD AutoCAD/FreeCAD con unità, layer, riferimenti esterni, coordinate, revisioni e output verificabili.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: CAD
---

# CAD, AutoCAD e FreeCAD

## Attivazione e input

Usa la skill per DWG/DXF, FCStd, tavole 2D, modelli parametrici, xref, layer, blocchi, layout, stampa e conversioni. Prima chiedi file originali, versione applicativo, unità, sistema di coordinate, scala, standard grafico, riferimento di rilievo, obiettivo e formati di consegna.

## Workflow

1. Duplica l'originale in area di lavoro e registra percorso, versione, data e hash.
2. Ispeziona unità, origine, extents, layer, blocchi, xref, proxy, font, stili, geometrie corrotte e oggetti non supportati.
3. Definisci regole di pulizia senza cancellare elementi non compresi; conserva report prima/dopo.
4. Modifica in modo parametrico o con comandi riproducibili; nomina revisioni e note di cambiamento.
5. Verifica quote, snap, chiusura polilinee, scala annotativa, spessori, layout e viewport.
6. Esporta PDF e, se richiesto, DXF/IFC/STEP con impostazioni documentate.
7. Riapri il risultato con un viewer indipendente e controlla tavola, unità, layer e leggibilità.

## Output

Consegna file sorgente, copia pubblicata, PDF, plot config quando necessario, report di conversione, elenco oggetti non trasferiti e registro revisioni. Per FreeCAD includi struttura dell'albero, dipendenze, macro/add-on usati e stato di ricomputazione.

## Quality gates

- Unità e scala sono controllate su almeno una misura nota.
- La stampa è stata vista a 100% e nella scala dichiarata.
- Xref, font, immagini e texture mancanti sono esplicitati.
- Nessun "purge" o conversione elimina dati senza backup e log.
- Il file è leggibile nella versione dichiarata o la limitazione è evidente.

## Evidenza e provenienza

Registra applicativo, versione, plugin, impostazioni, file sorgente, file derivati e hash. Se una conversione cambia geometria o proprietà, indica cosa è andato perso e perché.

## Confini professionali e legali

Un DWG pulito non dimostra rilievo corretto, conformità urbanistica o sicurezza. Non firmare, timbrare, certificare o attribuire titolarità. Verifica licenze AutoCAD, add-on, font, blocchi, immagini e dati di terzi prima della redistribuzione.

## Failure modes

- **Unità imperiali/metri confuse:** sospendi e confronta una quota di controllo.
- **Proxy o font assenti:** non sostituire silenziosamente; segnala impatto visivo.
- **Esportazione da solver non supportato:** conserva originale e report delle perdite.
- **Coordinate traslate a mano:** usa trasformazione dichiarata e punti di controllo.
- **PDF corretto ma sorgente errata:** controlla entrambi, non solo l'output.

## Strumenti

Usa AutoCAD o viewer autorizzato, FreeCAD ufficiale, script di inventario, validatori DXF, PDF viewer e checksum. Automatizza controlli meccanici, non la scelta di cosa sia geometria valida.

## Fonti ufficiali e diritti

- [Autodesk — AutoCAD 2026 Help](https://help.autodesk.com/view/ACD/2026/ENU/index.html): manuale ufficiale; non riprodurre contenuti o marchi.
- [Autodesk Support — mappe delle versioni](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Where-to-find-the-online-help-for-Autodesk-AutoCAD.html): riferimento ufficiale; verificare versione installata.
- [FreeCAD — User hub](https://wiki.freecad.org/User_hub): documentazione del progetto open source; verificare licenza della documentazione e degli add-on separatamente.

La skill descrive controlli originali e non garantisce l'integrità geometrica senza confronto con la fonte.
