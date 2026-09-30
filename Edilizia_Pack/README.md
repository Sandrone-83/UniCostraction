# Edilizia_Pack — Training Pack per LLM del mondo costruzioni

Materiale di addestramento per costruire un LLM esperto di **edilizia, costruzioni,
progettazione, impiantistica, sicurezza cantieri, appalti, gestione del cantiere,
materiali, domotica/smart home, design, estetica, comfort abitativo e prezzi dei
materiali** — dall'artigiano al general contractor. **Tutto a licenza commerciale
libera, verificata una per una** (vedi `licenze_audit.json`).

## Cosa contiene

| Cartella / file | Contenuto | Licenza |
| --- | --- | --- |
| `parsed/manuali_us_gov.jsonl` | 13 manuali tecnici federali USA: impianti idraulici (US Navy Utilitiesman 1-2-3), carpenteria metallica (Steelworker x3), rilievo e disegno tecnico (Engineering Aid), calcestruzzo e dighe (US Bureau of Reclamation), legno strutturale (Wood Handbook USDA), antincendio (UFC 3-600-01) | Public domain |
| `parsed/ecfr_osha_1926.jsonl` | Regolamento completo OSHA 29 CFR 1926 sicurezza cantieri (607 record per sezione) | Public domain |
| `parsed/norme_italiane.jsonl` | **Normativa italiana completa**: D.Lgs 81/08 (1466 pp., ed. INL 2026), NTC 2018 (372 pp.), Circolare esplicativa 7/2019 (348 pp.), Ordinanza sismica 3274/2003, DPR 380/01 Testo Unico Edilizia, D.Lgs 36/2023 Codice Appalti | Atto pubblico / CC BY-SA |
| `parsed/ufgs_specs.jsonl` | 46 specifiche edilizie UFGS (US DoD, formato CSI) su tutte le divisioni: cantiere, strutture, finiture, impianti, infrastrutture | Public domain |
| `parsed/wiki_construction/` | 231 voci Wikipedia (EN+IT): strutture, materiali, geotecnica, impianti MEP, cantiere, infrastrutture + 2° giro: domotica/smart home (KNX, BACnet, Zigbee, Matter, MQTT, BMS), materiali e finiture, teoria del colore e design, stili architettonici, comfort termico/acustico/luminoso, economia dei prezzi | CC BY-SA 4.0 |
| `parsed/design_estetica.jsonl` | 11 trattati classici public domain: Vitruvio, Palladio (I quattro libri IT 1590 + EN 1736), Owen Jones, Ruskin (Seven Lamps + Stones of Venice), Dresser, Wharton & Codman, de Wolfe, Eastlake, Radford's Cyclopedia (home building/carpentry) | Public domain |
| `parsed/reports_us_gov.jsonl` | 48 NPS Preservation Briefs (restauro edilizio: muratura, coperture, serramenti, intonaci, ferro, accessibilità, umidità, antisismica) + FEMA P-749 progettazione sismica | Public domain |
| `parsed/materiali_prezzi.jsonl` | 11 serie storiche mensili PPI 1926-2026 (legname, cemento, calcestruzzo, acciaio, rame, gesso, isolanti…) con variazione anno su anno — l'occhio ai prezzi del LLM | Public domain (BLS/FRED) |
| `raw/bim_ifc/ifc_models/` | 6 modelli BIM IFC di edifici reali (casa, edificio alto, edificio grande, progetto avanzato) | MIT |
| `parsed/ifc_bim_index.jsonl` | Indice metadati dei modelli IFC (schema, entity types) | MIT |
| `raw/` | Testi grezzi sorgente (txt/xml/html estratti) | come sopra |
| `licenze_audit.json` | Audit completo licenze con attribuzioni e URL | — |
| `manifest.json` | Indice documenti e conteggi record | — |

## Formato dei record JSONL (training-ready)

Ogni riga di `parsed/*.jsonl` è un oggetto:

```json
{
  "doc_id": "manuali_us_gov_0042",
  "source": "manuali_us_gov",
  "license": "Public domain (opera del Governo federale USA)",
  "commercial_ok": true,
  "attribution": "Utilitiesman 1 (NAVEDTRA 14265) - U.S. Navy (1989)",
  "url": "https://archive.org/details/utilitiesmani024854mbp",
  "title": "...",
  "text": "...(~6000 caratteri, chunk su confini di paragrafo)"
}
```

## Volumi

- manuali US Gov: ~14,0 M caratteri (2.194 chunk, 14 manuali)
- OSHA 1926: ~2,8 M caratteri (607 chunk)
- norme italiane: ~8,5 M caratteri (1.680 chunk)
- specifiche UFGS: ~1,7 M caratteri (328 chunk, 46 sezioni)
- Wikipedia: 273 voci complete EN+IT, ~6,5 M caratteri (estendibile)
- classici design/estetica/home building: 11 trattati, ~5,0 M caratteri (938 chunk)
- rapporti NPS + FEMA: 49 documenti, ~3,0 M caratteri (745 chunk)
- prezzi materiali FRED: 11 serie, ~11.900 osservazioni mensili 1926-2026

## Rigenerare / estendere

```bash
python fetch_archive_texts.py    # aggiungere ID archive.org in cima allo script
python fetch_wiki_corpus.py      # riprende e completa le voci Wikipedia mancanti
python fetch_wiki_materiale_design.py  # 2° giro: domotica, materiali, design, comfort, prezzi
python fetch_ufgs.py             # scarica altre sezioni UFGS (elenco in discovery/wbdg_all.json, 1.582 disponibili)
python extract_pdf_text.py <pdf> # estrae testo da un nuovo PDF (riprendibile)
python extract_ufgs_text.py      # estrae testo da nuove specifiche UFGS scaricate
python serialize_edilizia.py     # rigenera parsed/ + manifest.json
```

## Fonti escluse (e perché)

Eurocodici, codici ICC, norme UNI/EN, prezzari (RSMeans, DEI), OpenCourseWare, LibreTexts
e le documentazioni **Home Assistant / ESPHome** sono esclusi per copyright o clausola NC
(non commerciale). Dettagli in `licenze_audit.json`.


## Aggiornamento 28/09/2026 — Conto Termico 3.0 e incentivi energetici

Nuovo blocco dedicato agli incentivi e alla cultura energetica per l'edilizia:

- **D.M. 7 agosto 2025 (Conto Termico 3.0), testo articolato completo** dalla Gazzetta
  Ufficiale (GU n. 224 del 26-9-2025), in `raw/norme_it/DM_7_8_2025_ContoTermico3.txt`
- **5 atti normativi aggiuntivi**: D.Lgs 28/2011 (FER), D.Lgs 102/2014 (efficienza, TEE),
  D.Lgs 192/2005 (APE), D.Lgs 199/2021 (CER/autoconsumo), D.L. 34/2020 (Superbonus 110%)
- **167 voci Wikipedia** (66 IT + 101 EN) in `parsed/wiki_incentivi/`: Conto Termico,
  bonus edilizi, detrazioni, pompe di calore, solare termico, FER, mercato elettrico,
  CER, fotovoltaico, accumuli, wallbox, ESCO (CC BY-SA 4.0)
- **14 schede tecniche redatte** in `parsed/conto_termico_3_0.jsonl`: inquadramento,
  beneficiari, interventi, percentuali e massimali, iter PortalTermico, catalogo
  apparecchi prequalificati, cumulabilita', transizioni 2.0-3.0, cronologia normativa,
  mappa completa degli incentivi italiani, quadro CER/autoconsumo
- `python fetch_wiki_incentivi.py` per estendere il corpus wiki incentivale
- `python build_conto_termico_sintesi.py` per rigenerare le schede tecniche

Tutto materiale addestrabile senza licenza commerciale: atti pubblici italiani,
CC BY-SA 4.0 (Wikipedia), pubblico dominio US Gov. Audit completo in `licenze_audit.json`.


## Aggiornamento 28/09/2026 (2a espansione) — Ingegneria strutturale, geotecnica, impianti, rilievo, BIM

- **472 voci Wikipedia** (211 IT + 261 EN, ~8,9 M caratteri) in `parsed/wiki_engineering/`:
  statica e scienza delle costruzioni, fondazioni e geotecnica, strade e pavimentazioni,
  impianti idraulici/meccanici/antincendio, rilievo e strumentazione (stazione totale, GNSS,
  laser scanner), BIM/CAD/disegno tecnico, sostenibilita' (LEED, BREEAM, ITACA, CasaClima),
  project management, appalti e contratti, diritto immobiliare, estimo e valutazioni
- **3 manuali NAVFAC/US Army** (public domain) in `raw/manuals_txt/`: meccanica del terreno
  DM-7.1, progettazione fondazioni DM 7.2, prove sui materiali TM 5-530 (geotecnica completa)
- **D.M. 26 giugno 2015 "Requisiti minimi"** (112 pp. con allegati): trasmittanze, EPgl,
  edificio di riferimento, NZEB, RTP e linee guida APE
- `python fetch_wiki_engineering.py` per estendere il corpus ingegneristico


## Aggiornamento 29/09/2026 — Glossario tecnico bilingue IT-EN

- **parsed/glossario_bilingue.jsonl** (505 coppie): termini IT con equivalente ufficiale EN
  dai collegamenti interlinguistici Wikipedia delle 892 voci del corpus, con dominio
  (edilizia, incentivi, ingegneria, design) e definizione di contesto
- **parsed/glossario_curato_kimi.jsonl** (82 schede): pratiche edilizie italiane
  (SCIA, CILA, SAL, asseverazione, CRE), contabilita' di cantiere, dettagli costruttivi
  (cassaforma, copriferro, controfalla, cordolo) e sinonimi UK/US diffusi nei software
  CAD/BIM (screed, rebar, formwork, footing, joist, stud, lintel, flashing, HVAC)
- `python build_glossario.py` / `python build_glossario_curato.py` per rigenerarli

---

## Aggiornamento 29/09/2026 (2a) — Esempi di calcolo svolti

Nuovo corpus `parsed/esempi_calcolo_svolti.jsonl`: **34 esercizi completamente svolti** in italiano, ciascuno con struttura PROBLEMA / DATI / SVOLGIMENTO numerato / RISULTATO / VERIFICA / NOTE PRATICHE.

Aree coperte:
- **Strutture**: travi in c.a. armata, solai in laterocemento, muratura portante, ancoraggi e getti (verifiche SLU/SLU, NTC 2018)
- **Termofisica edilizia**: trasmittanze pareti/coperture con e senza cappotto, ponti termici, bilanici energetici UNI/TS 11300
- **Impianti**: portate idrauliche, dimensionamento tubazioni, pompe di calore (COP/SCOP), distribuzione elettrica (sezioni cavi, calo di tensione)
- **Acustica**: criteri di reverberazione, indici di isolamento
- **Geotecnica**: fondazioni superficiali (portanza Terzaghi, cedimenti)
- **Rilievo e topografia**: compensazione poligonali, rilievi con stazione totale
- **Estimo ed economia di cantiere**: computi metrici, stime a corpo/partitario, rata di mutuo, incidenze
- **Misure di cantiere**: quantità, resse, produzioni giornaliere

Licenza: sintesi didattica originale (pubblico dominio). Riferimenti normativi citati: NTC 2018, D.M. 26/6/2015, UNI/TS 11300, prassi consolidata di cantiere.

Nota: valori e procedimenti sono didattici, con dati tipici di prezzario/cantiere; non sostituiscono i testi ufficiali UNI/NTC (esclusi per licenza).

---

## Aggiornamento 29/09/2026 (3a) — Banca di 100 quiz tecnici con risposta commentata

Nuovo corpus `parsed/quiz_tecnici_100.jsonl`: **100 domande tecniche** con risposta completa e ragionata, divise per area e livello (32 base, 54 intermedio, 14 avanzato).

Aree coperte (numero quiz): Strutture 15, Termofisica/Energia 15, Impianti idraulici 8, Impianti meccanici/HVAC 8, Impianti elettrici 8, Acustica 5, Geotecnica 5, Rilievo e topografia 5, Estimo ed economia di cantiere 7, Cantiere e sicurezza 7, Normativa italiana 10, Materiali 7.

Ogni record ha: id (QUIZ-001...100), area, livello, question, answer (con formula, valori numerici verificati e note pratiche), più i metadati licenza standard del pack.

Licenza: sintesi didattica originale (pubblico dominio) — fonte n. 24 dell'audit. I riferimenti normativi (NTC 2018, D.Lgs 81/2008, DPR 380/2001, UNI/TS 11300 ecc.) riflettono prassi consolidata; per citazioni letterali servono i testi ufficiali.

---

## Aggiornamento 29/09/2026 (4a) — Documenti tecnici reali + FAQ cliente

Due nuovi corpus:

**`parsed/documenti_tecnici.jsonl`** — 10 modelli di documenti con testo completo, sezioni e note redazionali: relazione strutturale (NTC 2018, valori fcd/fyd calcolati), relazione energetica (UNI/TS 11300, trasmittanze verificate), capitolato speciale ETICS, computo metrico con prezzi, PSC (Titolo IV D.Lgs 81/2008), lettera di incarico, preventivo impresa, pratica SCIA art. 12, verbale di collaudo statico, SAL con ritenute. Tutti con segnaposto [___] pronti per l'uso.

**`parsed/faq_cliente_80.jsonl`** — 80 domande di clienti privati con risposta professionale (media 501 caratteri): ampliamenti 8, bonus/detrazioni 10, confini/muri 8, pratiche/tempi 8, preventivi/costi 8, ristrutturazione/impianti 10, catasto 7, locazione/condominio 7, manutenzione/patologie 8, sicurezza/antisismica 6.

Licenza: sintesi didattica originale (pubblico dominio) — fonti n. 25 e 26 dell'audit. I contenuti tecnici riflettono prassi consolidata italiana; i riferimenti normativi citati (DPR 380/2001, D.Lgs 81/2008, NTC 2018, artt. c.c. citati) sono da verificare sui testi ufficiali prima di uso professionale.

---

## Aggiornamento 29/09/2026 (5a) — Restauro/patologie + sistemi costruttivi internazionali

**`parsed/restauro_patologie.jsonl`** — 9 schede: teoria del restauro (sintesi di Viollet-le-Duc, Boito, Beltrami, teorema di Brandi, Carta di Venezia/Atene/Krakow/Faro), D.Lgs 42/2004, patologie da umidità e strutturali, materiali storici (laterizio, calce, pietra, legno, metalli), tecniche di consolidamento (cerchiatura, intubamento, FRP, iniezioni), restauro del legno e delle coperture, architettura rurale.

**`parsed/sistemi_costruttivi.jsonl`** — 11 schede: timber frame, platform frame, CLT, steel stud, terra cruda (adobe, pisè, cob, BTC), case di paglia, costruzioni passive (Passivhaus, NZEB), tetti nordici, edilizia giapponese, costruzioni metalliche, costruzione modulare.

Licenza: sintesi didattica originale (pubblico dominio) — fonti n. 27 e 28 dell'audit. Per gli edifici vincolati fare sempre riferimento al Codice Beni Culturali e ai pareri della Soprintendenza.

---

## Aggiornamento 29/09/2026 (6a) — Impresa/appalti + antincendio + infrastrutture + lezioni dai fallimenti

Quattro nuovi corpus:

**`parsed/impresa_appalti.jsonl`** — 10 schede: costituzione impresa, SOA e certificazioni, contratto di appalto privato (artt. 1655 ss. c.c.), gare pubbliche D.Lgs 36/2023, personale CCNL/DURC/formazione, sicurezza organizzativa, assicurazioni (RCO, decennale postuma, cauzioni), contabilità e cash flow, costi di costruzione per tipologia (residenziale 900-3.500 €/m², industriale 400-900), marketing tecnico.

**`parsed/antincendio.jsonl`** — 8 schede: quadro normativo (D.M. 3/8/2015, VVF), resistenza REI e compartimentazione, vie di fuga e parametri geometrici, scenari d'incendio (curva ISO 834, carico d'incendio MJ/m²), rivelazione/allarme, spegnimento (sprinkler, idranti, gas), gestione emergenza, materiali e finiture.

**`parsed/infrastrutture.jsonl`** — 8 schede: ponti (tipologie, elementi, azioni LM1/LM2), calcestruzzo precompresso (pre-tensione e post-tensione), strade (sezioni, pavimentazioni), ferrovie, dighe, opere marittime, tunnel (NATM, TBM).

**`parsed/lezioni_fallimenti.jsonl`** — 6 schede: Morandi 2018, confronto Aquila/Norcia, crollo balconi, alluvioni e drenaggio, collassi in cantiere, i 7 errori di progettazione più costosi.

Licenza: sintesi didattica originale (pubblico dominio) — fonti n. 29-32. I riferimenti normativi e giurisprudenziali vanno verificati sui testi ufficiali prima dell'uso professionale.

---

## Aggiornamento 29/09/2026 (7a) — Edilizia avanzata + BIM/urbanistica

**`parsed/edilizia_avanzata.jsonl`** — 16 schede in 2 categorie:
- *Impianti speciali* (8): piscine, cucine professionali, sale server/data center, trattamento acque, ascensori, ricarica veicoli elettrici, domotica KNX, impianti a gas.
- *Strutture avanzate* (8): grattacieli (Burj Khalifa, sistema tubolare, outrigger), vento e comfort, isolatori sismici (LRB, FPS), smorzatori (TMD), analisi pushover/time-history, tensostrutture e grandi luci, torri/serbatoi/silos, strutture composite.

**`parsed/bim_urbanistica.jsonl`** — 14 schede in 2 categorie:
- *BIM e digitale* (7): metodologia BIM e LOD, IFC/openBIM, scan-to-BIM/GIS/digital twin, computo BIM 4D/5D, BIM in cantiere, contratti/EPC/IPD, facility management.
- *Urbanistica* (7): piani territoriali (PRG, PSC), progettare un quartiere/paese, reti tecnologiche urbane, standard edilizi, mobilità, paesaggio e ambiente, rigenerazione urbana.

Licenza: sintesi didattica originale (pubblico dominio) — fonti n. 33-34.

---

## Aggiornamento 29/09/2026 (8a) — Tecnica specialistica + metodo di cantiere avanzato

**`parsed/tecnica_specialistica.jsonl`** — 12 schede d'élite: facciate ventilate e BIPV, metodo di Glaser (condensa interstiziale), simulazione energetica dinamica (EnergyPlus, PMV/PPD), consolidamento terreni (micropali, jet grouting, muri di sostegno), calcestruzzi speciali (SCC, UHPC, FRC, bio-based), certificazioni green (LEED, BREEAM, ITACA, LCA), microzonazione sismica e condizioni di sito, dissipatori e progettazione dissipativa, ingegneria antincendio (FSE, CFD con FDS, evacuazione ASET/RSET), idraulica urbana sostenibile (LID/SUDS), impianti avanzati (VRF, geotermia, distretti termici), ricostruzione post-disastro (C.A.S.E., MAP).

**`parsed/metodo_cantiere.jsonl`** — 8 schede: lean construction (takt time, Last Planner), procurement e logistica di cantiere, megaprogetti e program management (EVM), claim e risoluzione alternativa delle dispute (ADR, dispute board), gestione qualità (ITP, NDT, collaudo avanzato), sicurezza di cantiere avanzata (rischi gravi, DVR tecnico), manutenzione del patrimonio (LCC), Energy Performance Contracting ed ESCo.

Licenza: sintesi didattica originale (pubblico dominio) — fonti n. 35-36.
