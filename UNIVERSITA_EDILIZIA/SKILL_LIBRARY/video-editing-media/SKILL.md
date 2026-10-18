---
name: video-editing-media
description: Organizza ingest, montaggio, audio, colore, sottotitoli, export e controllo diritti di contenuti video tecnici o formativi con deliverable riproducibili.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: video e media
---

# Video editing e media

## Attivazione e input

Usa la skill per lezioni, sopralluoghi, demo, interviste, render animati, brevi social e consegne tecniche. Chiedi scopo, pubblico, piattaforma, aspect ratio, frame rate, risoluzione, sorgenti, voce, musica, sottotitoli, diritti, privacy, durata e formato finale.

## Workflow

1. Inventaria i media in sola lettura: camera, codec, timecode, audio, autore, licenza/consenso, data e hash.
2. Crea progetto con cartelle, naming, proxy, backup e timeline master; non alterare gli originali.
3. Sincronizza e seleziona con marker; registra tagli sensibili, dati personali, volti, indirizzi e informazioni riservate.
4. Monta struttura narrativa e tecnica; collega claim a clip, documento o voce verificabile.
5. Mix audio, correggi colore, inserisci grafiche e sottotitoli; separa contenuto illustrativo da evidenza.
6. Esporta master e derivati con preset documentato; genera checksum e report codec.
7. Controlla video, audio, testi, sincronizzazione, silenzi, safe area, contrasto, sottotitoli e riproduzione su almeno due player.

## Output

Consegna progetto, master, derivati per canale, file WebVTT/SRT, lista fonti e diritti, note di montaggio, preset, changelog e report QC. Se manca una licenza o un consenso, consegna una preview interna marcata e blocca la pubblicazione.

## Quality gates

- Ogni asset ha diritto/consenso o stato di quarantena.
- Parlato tecnico e numeri sono verificati contro fonte o approvazione del responsabile.
- I sottotitoli sono sincronizzati, leggibili e coerenti con il parlato.
- Il master mantiene audio non distorto, livelli controllati e frame rate dichiarato.
- Il file finale è riproducibile e i derivati non contraddicono il master.

## Evidenza e provenienza

Conserva camera originali, progetto, proxy generati, plugin, font, musica, grafiche, autorizzazioni, versioni e hash. Per materiali da terzi annota licenza, territorio, durata, mezzi e attribuzione. Una URL di download non prova il diritto di riuso.

## Confini professionali e legali

Non pubblicare volti, voci, targhe, planimetrie, coordinate di sicurezza o documenti riservati senza base e autorizzazione. Il video non prova da solo una lavorazione corretta o una conformità. Non usare musica, immagini, loghi, filmati o font con licenza ignota; non alterare immagini in modo da confondere documentazione e ricostruzione.

## Failure modes

- **Codec non supportato:** conserva master e transcodifica con log, non ricomprimere a cascata.
- **Proxy scambiato per master:** etichetta file e controlla risoluzione/bitrate.
- **Sottotitoli automatici errati:** verifica nomi, misure, negazioni e unità manualmente.
- **Claim senza fonte:** sostituisci con formulazione prudente o rimuovi.
- **Diritto scaduto o territoriale:** blocca derivati pubblici e riapri la verifica.

## Strumenti

Usa editor autorizzato, DaVinci Resolve o equivalente, FFmpeg/ffprobe per ispezione, player indipendente, controllo loudness, OCR/trascrizione con revisione umana e repository con permessi.

## Fonti ufficiali e diritti

- [FFmpeg — documentation](https://www.ffmpeg.org/documentation.html): software e documentazione open source; verificare licenze dei codec e build.
- [Blackmagic Design — support](https://www.blackmagicdesign.com/support): manuali ufficiali DaVinci Resolve; non riprodurre testi o asset.
- [W3C — WebVTT](https://www.w3.org/TR/webvtt1/): specifica del formato; verificare stato della raccomandazione e termini.

La skill è una procedura originale di postproduzione e controllo diritti; non è consulenza copyright o privacy.
