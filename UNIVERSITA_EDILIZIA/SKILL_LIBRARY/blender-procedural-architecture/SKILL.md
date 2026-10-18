---
name: blender-procedural-architecture
description: Genera scene architettoniche procedurali Blender con script, seed, asset, scala, camere e render riproducibili; separa visualizzazione, ricostruzione e rilievo.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: Blender procedurale e automazione architettonica
---

# Blender procedurale per scene architettoniche e render automation

## Attivazione e input

Attiva questa skill quando la scena deve essere costruita o rigenerata da parametri, dati CAD/IFC, rilievo, cataloghi o varianti e il render deve essere riproducibile. È una faccetta distinta da `blender-3d-render`: privilegia generazione deterministica e automazione, non la sola composizione visiva.

Raccogli obiettivo (studio, didattica, vendita o verifica), fonte geometrica, unità/origine/nord, parametri e range, seed, versione Blender, motore, GPU/CPU, risoluzione, frame, formato, percorso output, asset, texture, HDRI, font, persone, diritti e livello di fedeltà richiesto. Identifica cosa è misurato, dedotto, completato o puramente illustrativo.

## Workflow

1. Crea un file di configurazione versionato con schema, valori, seed, unità, coordinate, release Blender e hash degli input; fallisci se un parametro obbligatorio è implicito.
2. Genera una scena factory-clean: collezioni per sorgenti, geometria procedurale, asset, camere, luci, annotazioni e output; non dipendere da preferenze locali.
3. Costruisci moduli con funzioni pure o operatori isolati, nomi stabili e metadati `source_kind`, `source_id`, `confidence` e `generated_by`; limita la casualità al seed dichiarato.
4. Importa la fonte e confronta bounding box, misura campione, quota di riferimento e orientamento. Marca i completamenti parametrici senza farli apparire osservati.
5. Crea camere e luci separate dalla geometria; salva impostazioni di colore, samples, denoise, engine, frame e versione. Produce almeno un render diagnostico e uno finale.
6. Esegui in background con script tracciato, salva `.blend` e log, esporta output con percorsi relativi o package completo. Non sovrascrivere la sorgente.
7. Verifica riapertura in ambiente pulito, asset mancanti, bounding box, camera, alpha, colori, frame e checksum; confronta due run con lo stesso seed prima di pubblicare una variante.

## Output

Consegna script/config, `.blend`, eventuale package asset, render diagnostico/finale, pass tecnici o maschere, manifest di provenienza, log di esecuzione, versioni, seed, metriche di scala, elenco placeholder e dichiarazione di finalità. Un output deve dire se è `illustrativo`, `ricostruito`, `misurato` o `non verificato`.

## Quality gates

- Due esecuzioni con stesso input e seed producono la stessa topologia e risultati equivalenti secondo una tolleranza dichiarata.
- La scena si apre senza path assoluti del computer autore, asset silenziosi o add-on non dichiarati.
- La scala è controllata su almeno una dimensione nota e il nord/orientamento è visibile nel report.
- Le varianti cambiano solo i parametri richiesti; il diff di configurazione spiega ogni differenza.
- Render e pass tecnici non mascherano lacune geometriche, materiali ipotizzati o incertezze del rilievo.

## Evidenza e provenienza

Registra hash di input, script, config, `.blend`, asset e render; conserva versione Blender, motore, device, seed, locale, dipendenze e log. Per ogni asset segna autore, URL, licenza, data di accesso, modifica e uso previsto. Per fotogrammetria o AI annota copertura, punti non osservati e metodo, senza chiamare il risultato rilievo.

## Confini professionali e legali

Una scena procedurale o un render non è progetto, rilievo, collaudo, computo o prova di conformità. Non presentare come esistente una superficie generata da regole. Blender, add-on, modelli, texture, HDRI, font, persone e musica hanno diritti separati: autorizza e attribuisci prima della consegna pubblica.

## Failure modes

- **Seed non registrato:** marca la variante non riproducibile e rigenera da configurazione esplicita.
- **Path locale o asset mancanti:** interrompi il package; non incorporare sostituzioni senza traccia.
- **Scala corretta solo nella camera:** controlla bounding box e misura nel mondo, non l'apparenza prospettica.
- **Script dipendente dal contesto UI:** sposta la logica in funzioni testabili e prova `--background`.
- **Variazione casuale che cambia il messaggio:** limita RNG a stream nominati e confronta il diff.
- **Render scambiato per stato di fatto:** aggiungi overlay e nota di natura rappresentativa.

## Strumenti

Usa Blender ufficiale, Python `bpy`, esecuzione `--background --python`, viewer immagini/glTF e checksum. Prima di assumere API o flag verifica:

- [Blender Python API](https://docs.blender.org/api/current/): API della release in uso.
- [Blender — esecuzione da riga di comando](https://docs.blender.org/manual/en/latest/advanced/command_line/arguments.html): modalità background e parametri ufficiali.
- [Blender — scripting](https://docs.blender.org/manual/en/latest/advanced/scripting/index.html): ambienti e limiti di automazione.
- [Blender — license](https://www.blender.org/about/license/): licenza del software; verificare separatamente asset e add-on.

## Fonti ufficiali e diritti

Blender Python API: https://docs.blender.org/api/current/

La documentazione Blender è riferimento ufficiale; il software è distribuito secondo la licenza dichiarata dal progetto, mentre gli asset e i file esterni non sono automaticamente liberi. La procedura, lo schema di provenienza e i controlli di determinismo sono originali.
