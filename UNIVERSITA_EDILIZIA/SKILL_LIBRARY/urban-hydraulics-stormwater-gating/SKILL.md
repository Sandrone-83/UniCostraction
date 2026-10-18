---
name: urban-hydraulics-stormwater-gating
description: Imposta il controllo operativo di drenaggio urbano e stormwater con bacini, eventi, reti, invasi, qualità e manutenzione senza sostituire il progettista idraulico o l'autorità di bacino.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: idraulica urbana, drenaggio e stormwater
---

# Gating di idraulica urbana e stormwater

## Attivazione e input

Attiva questa skill quando una trasformazione urbana, una strada, un lotto o un edificio deve gestire piogge, ruscellamento, fognatura, laminazione, infiltrazione, scarico o qualità delle acque. È una faccetta di bilancio, scenario e verificabilità distinta da environmental-resilience-lca-diagnostics, mep-energy-systems e italian-urban-planning-cadastre-pa: non autorizza lo scarico, non dimensiona definitivamente la rete e non sostituisce il progettista.

Prima raccogli bacino e sottobacini, coordinate e quote, modello digitale, suoli, permeabilità, uso del suolo, rete e recapito, vincoli, piogge di progetto e periodo di ritorno, maree o rigurgiti, falda, qualità, manutenzione, fasi e cambiamento climatico. Registra ente gestore, autorità di bacino, regione/comune, dati storici, periodo e criterio di accettazione. Se quota, recapito, evento o giurisdizione sono ignoti, lo stato è blocked.

## Workflow

1. **Gate del bacino:** delimita area contribuente, superfici, pendenze, punti bassi, connessioni e vie di deflusso; separa rete pubblica, proprietà privata e percorso di emergenza.
2. **Gate della base topografica:** riconcilia rilievo, quote chiave, sezioni, sottoservizi e modello digitale; controlla che gli scarichi e i volumi abbiano stesso datum verticale.
3. **Gate dell'evento:** registra serie pluviometrica, curva intensità-durata-frequenza, durata, periodo di ritorno, distribuzione temporale, perdite, infiltrazione e scenario climatico; non usare una pioggia generica come progetto locale.
4. **Gate del modello:** documenta superfici e coefficienti, conduzioni, rugosità, nodi, condotte, invasi, pompe, orifizi, valvole e condizioni al contorno. Versiona input, discretizzazione, solver e soglie numeriche.
5. **Gate delle alternative:** confronta drenaggio convenzionale, superfici permeabili, rain garden, tetti verdi, trincee, vasche e controllo alla fonte con volume, picco, qualità, manutenzione, sicurezza e spazio realmente disponibile.
6. **Gate dello stress:** prova evento di progetto, evento superiore, occlusione, mancata pompa, rigurgito, falda alta e fuori servizio; mappa allagamento, profondità, velocità, durata e beni esposti.
7. **Gate della consegna:** collega ogni misura a autorizzazione, gestore, manutentore e fase; prepara piano di monitoraggio, pulizia, ispezione e risposta. Un buon calcolo non rende le opere autorizzate o mantenute.

## Output

Consegna uno stormwater_control_record con bacini, quote, dati di pioggia, modello, scenari, alternative, volumi/picchi, mappe di rischio, qualità, manutenzione, autorizzazioni da verificare e stato screened, conditional o blocked. Riporta sempre evento, durata, periodo di ritorno, confini e assunzioni.

## Quality gates

- Bacino, quote, recapito, rete e proprietà sono identificati e riconciliati.
- Evento pluviometrico, periodo di ritorno, durata, perdite e scenario climatico hanno fonte e versione.
- Bilancio di massa, condizioni al contorno, volumi, picchi e risultati di scenario sono riproducibili.
- Sono valutati rigurgito, occlusione, fuori servizio, manutenzione e percorso di emergenza.
- Quantità e qualità dell'acqua, sicurezza e accessibilità manutentiva non vengono ridotte al solo picco di portata.
- L'esito non viene presentato come autorizzazione idraulica, nulla osta, sicurezza idraulica o progetto firmato.

## Evidenza e provenienza

Conserva rilievi e modelli altimetrici, serie pioggia e metadata, mappe e fotografie, inventario rete, file di calcolo, versioni del solver, parametri, output grezzi, hash e verbali. Marca dati osservati, proxy, interpolati e assunti. Coordinate di reti e aree allagate sono dati sensibili per sicurezza: limita accesso e distribuzione.

## Fonti ufficiali e diritti

- [Direttiva 2007/60/CE su EUR-Lex](https://eur-lex.europa.eu/legal-content/IT/ALL/?uri=CELEX%3A32007L0060): valutazione e gestione del rischio di alluvioni a livello europeo.
- [D.Lgs. 152/2006 su Normattiva](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2006-04-03;152!vig=): disciplina ambientale italiana, acque e scarichi da verificare per ambito e aggiornamento.
- [ISPRA](https://www.isprambiente.gov.it/it): dati, linee guida e riferimenti istituzionali ambientali da selezionare per tema e territorio.

Le fonti legislative e istituzionali sono riferimenti, non licenza generale di riproduzione. Il workflow, i registri, i gate e la matrice degli scenari sono originali. Stato diritti: official_reference_only_no_text_reproduced; dati pluviometrici, cartografie e modelli di terzi restano soggetti a licenza.

## Confini professionali e legali

La skill non firma progetti, non dichiara inedificabilità o sicurezza idraulica, non autorizza scarichi, non sostituisce autorità di bacino, gestore, geologo, ingegnere idraulico o ente locale e non impartisce istruzioni di emergenza per persone in pericolo. Un risultato è valido solo per dati, evento, modello, manutenzione e confini dichiarati; non garantisce assenza di allagamento.

## Failure modes

- **Datum verticali discordanti:** blocca il modello e riconcilia quote, soglie e recapiti.
- **Pioggia generica applicata al territorio:** richiedi serie, curva e autorità competente e marca il risultato screening.
- **Recapito assunto libero:** verifica capacità, rigurgito, autorizzazione e gestione del proprietario.
- **Picco corretto ma volume o qualità ignorati:** riapri bilancio, trattamento, infiltrazione e manutenzione.
- **Scenario di occlusione omesso:** simula fuori servizio e traccia percorso di emergenza.
- **Opera verde senza manutenzione:** non conteggiare prestazione a regime senza accesso, ispezione e responsabilità.

## Strumenti

Usa GIS, rilievo e modello altimetrico, database di piogge, modello idrologico/idraulico versionato, foglio di bilancio, mappe di profondità/velocità e registro manutenzione. Automatizza unità, quote, bilanci e confronti di scenario; non automatizzare autorizzazioni, responsabilità o comunicazioni di emergenza.
