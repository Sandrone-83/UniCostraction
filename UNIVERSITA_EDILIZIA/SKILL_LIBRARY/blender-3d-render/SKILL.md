---
name: blender-3d-render
description: Costruisce scene Blender e render tecnici o narrativi con scala, materiali, camera, luce, versioni e provenienza degli asset controllati.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: 3D e rendering
---

# Blender, 3D e render

## Attivazione e input

Usa la skill per modellazione da rilievo o CAD, materiali, illuminazione, animazioni, render, walkthrough e asset glTF. Chiedi scopo dell'immagine, fonte geometrica, scala, coordinate, livello di dettaglio, camera, target, formati, hardware e diritti su immagini, texture, HDRI, font e audio.

## Workflow

1. Crea una scena pulita con unità e origine dichiarate; collega le fonti senza sovrascriverle.
2. Importa geometria e misura un riferimento; marca elementi ricostruiti o completati artisticamente.
3. Organizza collezioni, nomi, materiali, UV, asset e versioni; evita modifiche distruttive finché non approvate.
4. Imposta camera, luce e render engine in base alla domanda; registra seed, colore, risoluzione e campioni.
5. Separa pass tecnici, maschere, overlay e render finale; usa annotazioni quando l'immagine deve informare.
6. Esporta immagini/video/glTF e verifica colori, alpha, frame, texture e percorsi relativi.
7. Consegna un contact sheet o preview, impostazioni chiave e nota sui limiti di rappresentazione.

## Output

Consegna .blend, asset collegati o pacchetto impacchettato, immagini/render, eventuali pass, impostazioni di scena, elenco fonti e licenze, più una dichiarazione chiara di ciò che è misurato, ricostruito o illustrativo.

## Quality gates

- Una misura campione e l'orientamento sono coerenti con la fonte.
- Mancanze geometriche e sostituzioni materiali sono marcate.
- La scena si apre senza percorsi rotti o add-on non dichiarati.
- Il render è controllato a piena risoluzione e in scala di grigi se la leggibilità è critica.
- Il risultato non usa luce, profondità o texture per mascherare incertezza.

## Evidenza e provenienza

Registra sorgente di ogni asset, autore, URL, licenza, data di accesso, modifica apportata e hash del pacchetto. Per fotogrammetria o AI annota metodo, copertura e punti non osservati.

## Confini professionali e legali

Un render non è rilievo, collaudo, progetto o prova di conformità. Non rappresentare come esistente ciò che è ipotizzato; non usare persone, immobili, marchi, texture o musica senza diritti e consensi. Il software Blender ha una licenza distinta da quella degli asset e dell'opera finale.

## Failure modes

- **Scala implicita:** misura un elemento noto prima di illuminare o arredare.
- **Materiali "fotorealistici" non documentati:** sostituisci con nota di incertezza.
- **Asset incorporato senza licenza:** quarantena l'asset e chiedi autorizzazione.
- **Texture mancante:** non impacchettare un file che appare corretto solo sul computer autore.
- **Render usato come planimetria:** allega fonte 2D/3D e dichiara la finalità.

## Strumenti

Usa Blender ufficiale, Python interno solo con script tracciato, viewer glTF, ImageMagick o strumenti equivalenti per controllo immagini e FFmpeg per video. Mantieni separati file di lavoro e deliverable.

## Fonti ufficiali e diritti

- [Blender Manual](https://docs.blender.org/manual/en/latest/): documentazione ufficiale; non copiare tutorial o testo.
- [Blender — license](https://www.blender.org/about/license/): software GPL; verificare add-on e asset separati.
- [Khronos — glTF](https://www.khronos.org/gltf/): standard aperto; verificare release e termini degli strumenti.

La skill è procedura originale di produzione e controllo visuale; non assegna diritti sugli asset.
