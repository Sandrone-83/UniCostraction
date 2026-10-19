---
name: construction-traffic-logistics-safety
description: Progetta e controlla viabilità interna, consegne, segregazione pedoni-mezzi e interfacce con traffico pubblico in cantiere, senza sostituire piano sicurezza, ente proprietario o autorità stradale.
metadata:
  library: UniCostraction/AuraTrix-AulaFIX
  version: 0.1.0
  domain: logistica e sicurezza del traffico di cantiere
---

# Logistica e sicurezza del traffico di cantiere

## Attivazione e input

Attiva questa skill quando accessi, consegne, mezzi d'opera, pedoni, carichi, retromarce o cantieri stradali devono essere coordinati con layout e fase del lavoro. È distinta da construction-site-safety, che governa il sistema generale di sicurezza, e da road-infrastructure-bridge-engineering, che tratta progettazione dell'infrastruttura.

Raccogli planimetria e fase, cancelli, percorsi, dimensioni e portanza, pendenze, visibilità, interferenze, traffico esterno, turni, mezzi, carichi, consegne, zone carico/scarico, pedoni, emergenze, fornitori, segnaletica, barriere, spotter, meteo, permessi e contatti con ente proprietario o gestore. Se accesso, flusso, fase o responsabile non sono definiti, lo stato è blocked.

## Workflow

1. **Gate della domanda:** mappa movimenti, volumi, finestre, origine/destinazione, carichi eccezionali e conflitti con lavoro, emergenza, residenti e traffico pubblico.
2. **Gate del layout:** separa pedoni e mezzi, riduci retromarcia, definisci senso unico, aree di attesa, carico/scarico, attraversamenti, rifugi, illuminazione e accessi soccorritori.
3. **Gate della capacità:** verifica larghezze, raggi, pendenze, portanza, stabilità, visibilità e limiti di carico rispetto ai mezzi reali; non usare una planimetria non aggiornata.
4. **Gate della consegna:** prenota slot, istruzioni ingresso, velocità, DPI, contatto, immobilizzazione, carico/scarico, divieto pedoni e gestione veicolo in avaria.
5. **Gate dell'interfaccia pubblica:** collega segnalamento, occupazione, deviazioni, barriere e comunicazione alle autorizzazioni dell'ente, senza inventare schemi o titoli.
6. **Gate dell'esercizio:** briefing a conducenti e lavoratori, verifica spotter competente quando necessario, controlla condizioni giornaliere e registra quasi incidenti.
7. **Gate della revisione:** aggiorna per nuova fase, mezzo, scavo, meteo, incidente, modifica stradale o cambio di accesso; prova la risposta a blocco e emergenza.

## Output

Produci un site_traffic_logistics_record con fase, mappa, flussi, mezzi, segregazione, consegne, segnaletica, permessi, briefing, osservazioni e stato ready, conditional o blocked. Il record deve mostrare le interfacce con il traffico pubblico e le misure temporanee con scadenza.

## Quality gates

- Layout, flussi, mezzi, carichi, accessi, pendenze, visibilità e portanza sono verificati in campo.
- Pedoni, mezzi, soccorritori e visitatori hanno percorsi e regole comprensibili.
- Retromarcia, carico/scarico, attesa e avaria hanno controlli, owner e piano di contenimento.
- Segnaletica e barriere corrispondono a fase, autorizzazione e condizioni reali.
- Conducenti, spotter e lavoratori sono informati, formati e autorizzati secondo ruolo.
- Incidenti, near miss e modifiche aggiornano layout, briefing e controlli prima della ripresa.

## Evidenza e provenienza

Conserva planimetrie revisionate, sopralluoghi e foto, swept path o verifiche dimensionali, registro mezzi, consegne, briefing, permessi, segnaletica, controlli giornalieri, manutenzioni, near miss, meteo e comunicazioni con enti. Marca osservato, previsto, temporaneo e approvato. Minimizza targhe, nominativi e dati di localizzazione non necessari.

## Fonti ufficiali e diritti

- [EU-OSHA — workplace transport](https://eguides.osha.europa.eu/vehicle-safety/themes/workplace-transport-safety): principi istituzionali per layout, separazione e piano traffico.
- [Normattiva — D.Lgs. 81/2008](https://www.normattiva.it/eli/id/2008/04/30/008G0104/CONSOLIDATED): sicurezza di cantiere, attrezzature e viabilità, da verificare alla data.
- [Normattiva — Codice della strada](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1992-04-30;285!vig=): disciplina della circolazione e delle interferenze con strada pubblica.
- [INAIL — sicurezza nei cantieri stradali](https://www.inail.it/content/dam/inail-hub-site/documenti/catalogo-generale/2016/06/La%20sicurezza%20sul%20lavoro%20nei%20cantieri%20stradali.%20Opuscolo%20informativo%20per%20i%20lavoratori.pdf): riferimento informativo istituzionale, senza riprodurne il testo.

Piano operativo, mappe e checklist sono originali. Diritti: official_reference_only_no_text_reproduced; fonti legali pubbliche, manuali mezzi, segnaletica e documenti di enti restano soggetti a versione e diritti propri.

## Confini professionali e legali

La skill non autorizza occupazione suolo, deviazioni, chiusure, trasporti eccezionali o segnaletica pubblica, non sostituisce PSC/POS, datore di lavoro, coordinatore, ente proprietario, polizia stradale o responsabile viabilità. Non ordina manovre in area pericolosa e non certifica portanza, visibilità o sicurezza senza verifica competente.

## Failure modes

- **Layout teorico:** sopralluogo e chiusura preventiva della rotta non verificata.
- **Pedoni nel raggio di manovra:** fermare il movimento, ristabilire segregazione e aggiornare briefing.
- **Consegna fuori slot:** respingere o mettere in attesa secondo procedura, senza improvvisare in carreggiata.
- **Segnalamento fuori fase:** sospendere la configurazione e coinvolgere ente/autorità.
- **Spotter assente o non competente:** vietare retromarcia e assegnare controllo autorizzato.
- **Meteo o fondo alterato:** rivalutare aderenza, visibilità, drenaggio e capacità prima di riprendere.

## Strumenti

Usa traffic management plan, site logistics map, delivery slot register, vehicle/pedestrian matrix, swept-path check, permit register, daily inspection, driver briefing, incident/near-miss log e change tracker. Automatizza slot, versioni e notifiche; non autorizzare accessi o modificare segnalamento reale senza responsabile.
