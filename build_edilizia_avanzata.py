# -*- coding: utf-8 -*-
"""Edilizia avanzata: impianti speciali + strutture estreme (grattacieli e oltre)."""
import json, os

S = []

# ============ IMPIANTI SPECIALI (8) ============
S.append(("impianti_speciali","piscine",
"PISCINE - COSTRUZIONE E IMPIANTI",
"""Le piscine sono impianti idraulico-edilizi complessi con vincoli di sicurezza specifici:

1. STRUTTURA: vasca in calcestruzzo armato impermeabilizzato (o vasche prefabbricate in vetroresina/acciaio), con camera d'acqua, sistema di filtrazione e disinfezione, bordo di sfioro o skimmer.

2. IMPIANTI: ricircolo forzato (pompe, filtri a sabbia o a cartuccia), disinfezione (cloro, sali, ozono, UV), riscaldamento (pompa di calore, scambiatori solari), illuminazione subacquea (12 V per sicurezza).

3. IMPIANTISTICA ELETTRICA: tensione di sicurezza 12 V sott'acqua, differenziali ad alta sensibilità (10 mA), messa a terra equipotenziale, sezionatori di emergenza.

4. NORME: UNI 10637 (piscine), DL 26/2017 per la sicurezza dei bagnanti (normativa balneare per piscine pubbliche), prevenzione infortuni in immersione.

5. COSTRUZIONE: getto monolitico o con giunti stagno, prova di tenuta, rivestimento (mosaico, PVC, piastrelle), bordo con sistemi di sicurezza (coperture, allarmi, scale di emergenza)."""))
S.append(("impianti_speciali","cucine_professionali",
"CUCINE PROFESSIONALI E RISTORAZIONE COLLETTIVA",
"""Le cucine professionali hanno impianti dedicati per portate, ventilazione e sicurezza:

1. VENTILAZIONE: cappe con aspirazione meccanica dedicata, con filtri a carbone per odori e grassi, separazione dei flussi (aria di cattura pulita), portata calcolata sui fuochi installati.

2. GAS: reti di distribuzione con valvole di sicurezza (VGU), rivelazione fughe gas, interblocco con la ventilazione, certificazione UNI 7129 (impianti gas domestici) e UNI 11344 (impianti gas professionali).

3. IDRAULICA: acque nere e chiare separate, lavelli con sistemi di triturazione, addolcitori per lavastoviglie, scarichi con trappole antiodore dimensionate.

4. ELETTRICO: linee dedicate per forni, piani cottura e frigoriferi, potenza installata elevata (30-100 kW), differenziali dedicati.

5. IGIENE SANITARIA: superfici lavabili (acciaio inox), pavimenti antiscivolo, drenaggi canalina con sifoni, controllo HACCP per la sicurezza alimentare."""))
S.append(("impianti_speciali","sale_server",
"SALE SERVER E DATA CENTER EDILIZI",
"""Le sale server sono ambienti con requisiti termici, elettrici e antincendio speciali:

1. RAFFREDDAMENTO: unita' di precisione (CRAC) a espansione diretta o ad acqua refrigerata, con distribuzione aria pavimento (raised floor), ridondanza N+1, temperatura 22-24 °C e umidita' 40-60%.

2. CARICO ELETTRICO: potenza installata 500-2.000 W/m² (fino 3.000 W/m² per HPC), alimentazione ridondata (UPS online, generatori), distribuzione a rack (PDU), misura PUE (Power Usage Effectiveness) < 1,5 per efficienza.

3. ANTINCENDIO: rivelazione precoce (VESDA - Very Early Smoke Detection Apparatus), spegnimento a gas (FM-200, Novec 1230, inerti) senza residui, compartimentazione e porte REI, controllo di accesso.

4. EDILIZIA: pavimenti sopraelevati per cablaggi, controsoffitti tecnici, sezioni antiurto, sorveglianza continua, messa a terra equipotenziale dedicata.

5. NORME: EN 50600 (data center), ISO/IEC 27001 (sicurezza informatica), Tier standard (Uptime Institute) per i livelli di ridondanza."""))
S.append(("impianti_speciali","trattamento_acque",
"ADDOLCITORI, DEPURAZIONE E TRATTAMENTO ACQUE EDILIZIE",
"""Il trattamento delle acque garantisce qualita' e protezione degli impianti:

1. ADDOLCIMENTO: scambio ionico per eliminare calcio e magnesione (durezza), protegge caldaie e scambiatori, dimensionamento su portata e durezza dell'acqua.

2. FILTRAZIONE: sabbia, carboni attivi (cloro, odori, micropolluenti), microfiltrazione per particellato, ultrafiltrazione per acque speciali.

3. DISINFEZIONE: UV, ozono, cloro per acque di processo o di reintegro piscine.

4. OSMOSI INVERSA: per acque di alimentazione speciale (laboratori, cucine professionali, batterie), con portate da 100 a 10.000 L/h.

5. NORME: DPR 236/1988 (acque destinate al consumo umano), DL 31/2001, UNI 8065 (addolcitori), verifica batteriologica per acque potabili.

6. MANUTENZIONE: rigenerazione resine, sostituzione cartucce, controllo portate e pressioni, monitoraggio chimico."""))
S.append(("impianti_speciali","ascensori",
"ASCENSORI, MONTACARICHI E PIATTAFORME ELEVATRICI",
"""Gli impianti di sollevamento verticali hanno regole di progetto e sicurezza specifiche:

1. TIPI: ascensori elettrici (a fune, idraulici), piattaforme elevatrici (disabili, montacarichi), scale mobili, montascale, ascensori esterni (vetro/panoramici).

2. REQUISITI EDILIZI: vano corsa con dimensioni minime, sopracorsa e fossa, porte con interblocco, cabina con dimensioni per 13 persone minimo in edilizia pubblica (900 kg), carico nominale 320-1.600 kg.

3. SICUREZZA: doppia protezione del sollevamento (freni, paracadute), interblocco porte, pulsantiere di emergenza, linea telefonica, illuminazione di emergenza, batterie tampone per black-out.

4. NORME: UNI EN 81-20/50 (safety rules for the construction and installation of lifts), CEI 11-27 (impianti elettrici), DPR 162/1999 (norme antinfortunistiche per ascensori), verifiche periodiche obbligatorie (semestrali per uso pubblico).

5. BARRIERE ARCHITETTONICHE: accessibilita' disabili (DM 236/1989), porte 90 cm, pulsanti a braille, cabina con corrimano."""))
S.append(("impianti_speciali","ricarica_elettrica",
"INFRASTRUTTURE DI RICARICA PER VEICOLI ELETTRICI",
"""La ricarica dei veicoli elettrici e' il nuovo impianto edilizio obbligatorio in molti contesti:

1. LIVELLI DI RICARICA: Lento (AC, 3,7-22 kW, wallbox domestici e aziendali), Fast (DC, 50-150 kW, stazioni stradali), Ultra-fast (DC, 150-350 kW).

2. EDILIZIA RESIDENZIALE: wallbox monofase/trifase in box privati, con messa a terra dedicata, protezione differenziale tipo B o DC, sezionatore di emergenza.

3. EDILIZIA CONDOMINIALE: installazione in proprietà comuni con diritto di installazione (art. 1125-bis c.c.), gestione dei conteggi energia (contabilizzazione, subentro), potenza contrattuale condominiale.

4. EDILIZIA COMMERCIALE: colonnine con gestione accessi (RFID, app), contabilizzazione utenti, integrazione fotovoltaico e batterie.

5. NORME: CEI 0-21 (collegamento in bassa tensione), CEI EN 61851 (sistemi di ricarica), D.Lgs 28/2011 (obbligo pre-cablaggio nei nuovi edifici), Direttiva AFIR per le infrastrutture stradali."""))
S.append(("impianti_speciali","domotica_avanzata",
"DOMOTICA AVANZATA, KNX E BUILDING AUTOMATION",
"""La domotica integra gli impianti dell'edificio in un unico sistema gestibile:

1. SISTEMI: KNX (standard europeo, bus dedicato), BACnet (edilizia terziaria), Modbus (industriale), Zigbee/Z-Wave/Matter (wireless consumer), HomeKit/Google Home (consumer).

2. FUNZIONI: illuminazione scenografica, gestione tapparelle e serramenti, climatizzazione integrata, sicurezza (videosorveglianza, sensori, allarmi), gestione energetica (contabilizzazione, ottimizzazione fotovoltaico-batteria), accessi.

3. VANTAGGI ENERGETICI: spegnimento automatico luci, controllo temperatura per zone, ottimizzazione carichi, integrazione con VMC e pompe di calore (10-30% risparmio).

4. PROGETTAZIONE: cablaggio dedicato (BUS KNX a 2 fili) o wireless, attuatori e sensori per ogni funzione, supervisione centrale, programmazione scenari.

5. NORME: EN 50090 (sistemi KNX), CEI 64-8 (impianti elettrici), certificazione KNX per installatori."""))
S.append(("impianti_speciali","impianti_gas",
"IMPIANTI A GAS METANO E GPL EDILIZI",
"""Gli impianti a gas alimentano cucine, caldaie e generatori con vincoli di sicurezza severi:

1. RETE: tubi in acciaio, rame, multistrato o PE (interrati), con valvole di intercettazione generali e per singolo apparecchio, prove di tenuta obbligatorie.

2. SICUREZZA: valvole di massima (VGU) che chiudono in assenza di fiamma (termocoppia), valvole di sicurezza per sovrapressione, rilevatori fughe gas (metano/GPL) con elettrovalvole di blocco.

3. LOCALI: aerazione naturale (griglie) e forzata per locali caldaia (UNI 7129), sfiato fumi con tiraggio adeguato, tenuta all'aria per stanze con apparecchi a gas.

4. NORME: UNI 7129 (impianti gas domestici), UNI 11344 (impianti gas professionali), UNI 11144 (esercizio e manutenzione), verifiche obbligatorie con DPR 462/2001 per gli impianti domestici.

5. NUOVI SVILUPPI: gas tecnici (idrogeno, biometano), contabilizzazione con misuratori intelligenti (smart meter), rete gas smart."""))

# ============ STRUTTURE AVANZATE (8) ============
S.append(("strutture_avanzate","grattacieli",
"GRATTACIELI - PROGETTAZIONE DELLE TORRI ALTE",
"""Il grattacielo (superalto, >300 m; megatall, >600 m) e' la sfida massima dell'ingegneria strutturale:

1. AZIONI DOMINANTI: il vento diventa l'azione di progetto principale (non il sisma, nei siti non sismici). Vortici di scia (vortex shedding), raffica, turbolenza urbana, comfort umano (accelerazioni < 0,15-0,25 m/s²).

2. SISTEMI STRUTTURALI:
   - Telaio a shear walls (pareti di taglio) in c.a. o acciaio.
   - Sistema tubolare (tube): la facciata e' la struttura (World Trade Center, Hancock).
   - Sistema a megacolonne con brace (diagrid): reticolato esterno (CCTV, Hearst Tower).
   - Outrigger e belt truss: travi di collegamento al nucleo ascendente.
   - Core centrali in c.a. con pareti accoppiate.

3. NUCLEO: il nucleo centrale (scale, ascensori, impianti) funge da parete di taglio; in acciaio o c.a., con sistema outrigger ogni 15-30 piani.

4. MATERIALI: acciaio ad alta resistenza (S460-S690), calcestruzzo ad alta resistenza (C80-C130), compositi acciaio-calcestruzzo.

5. ESEMPI: Burj Khalifa (828 m, sistema a torre con contrafforti 'buttressed core'), Shanghai Tower (632 m, torre a spirale con doppia facciata), Taipei 101 (508 m, con smorzatore di massa sintonizzato da 660 ton)."""))
S.append(("strutture_avanzate","vento_comfort",
"AZIONI DEL VENTO E COMFORT NELLE COSTRUZIONI ALTE",
"""Il vento e' l'azione dominante per le costruzioni alte e snelle:

1. MECCANISMI: pressione frontale (drag), raffica (gust), vortici alterni di scia (vortex shedding) che generano oscillazioni trasversali, instabilita' aeroelastica (flutter, galloping).

2. VELOCITA' DI PROGETTO: calcolata con analisi probabilistica (rapporto di ritorno 50 anni per edifici ordinari, 100-500 anni per opere importanti), con profili verticali in funzione della rugosita' del terreno.

3. ANALISI: tunnel del vento (prova sperimentale su modello aerodinamico), analisi numerica (CFD - Computational Fluid Dynamics), analisi dinamica modale (spettro di risposta, time-history).

4. COMFORT UMANO: le accelerazioni del piano devono essere limitate (0,15-0,25 m/s² per uffici, 0,10-0,15 per residenziale); si ottengono aumentando la rigidezza o la massa, o con smorzatori.

5. MITIGAZIONI: forme aerodinamiche (sezioni affusolate, smussi, fori), smorzatori (vedi scheda dedicata), massi sintonizzati, controventi."""))
S.append(("strutture_avanzate","isolatori_sismici",
"ISOLATORI SISMICI E PROGETTAZIONE ALL'ISOLAMENTO DI BASE",
"""L'isolamento di base separa la struttura dal terreno durante il sisma:

1. PRINCIPIO: dispositivi interposti tra fondazione e struttura allungano il periodo proprio (da 0,5-1 s a 2-3 s), riducendo l'accelerazione trasmessa alla sovrastruttura (fino 3-5 volte).

2. TIPI DI ISOLATORI:
   - Elastomerici (LRB - Lead Rubber Bearings): gomma con piombo fuso al centro, forniscono elasticita' e smorzamento.
   - Friccionali (FPS - Friction Pendulum System): superficie curva con attrito, movimento pendolare.
   - Slider: appoggi a basso attrito con ritorno elastico.

3. VANTAGGI: protegge contenuti e impianti, riduce il danno strutturale, consente progettazione a domanda limitata, funziona anche per eventi moderati.

4. PROBLEMATICHE: costo aggiuntivo (5-15% struttura), vincolo di spazio per il cunicolo di isolamento, problemi di stabilita' verticale, necessita' di verifiche orizzontali e verticali.

5. APPLICAZIONI: edifici strategici (ospedali, datacenter), edifici storici e musei, ponti (appoggi antisismici), edifici residenziali in Giappone, Cile, Italia (basilica di San Francesco ad Assisi)."""))
S.append(("strutture_avanzate","smorzatori",
"SMORZATORI VISCOSI E MASSI SINTONIZZATI",
"""Gli smorzatori riducono le oscillazioni delle strutture al vento e sisma:

1. SMORZATORI VISCOUSI: cilindri oleodinamici che dissipano energia per attrito viscoso del fluido, utilizzati nei tiranti, nelle pareti o come appoggi; riducono le vibrazioni senza aumentare la rigidezza.

2. SMORZATORI VISCOELASTICI: lastre di polimeri che deformandosi dissipano energia, usati come vincoli tra struttura e fondazione o tra elementi.

3. MASSI SINTONIZZATI (TMD - Tuned Mass Damper): massa (0,5-2% della massa modale) sospesa con molle e smorzatori, sintonizzata sulla frequenza della struttura; assorbe l'energia vibratoria. Esempi: Taipei 101 (660 t), Shanghai Tower, John Hancock Boston.

4. SMORZATORI DI ATTRITO: dispositivi a sezioni d'attrito controllato, dissipano energia per attrito Coulombiano.

5. APPLICAZIONI: grattacieli, ponti sospesi e strallati, torri industriali, antenne, turbine eoliche, edifici in zona sismica."""))
S.append(("strutture_avanzate","analisi_nonlineare",
"ANALISI NON LINEARE: PUSHOVER E TIME-HISTORY",
"""Le analisi non lineari valutano il comportamento della struttura oltre il campo elastico:

1. ANALISI STATICA NON LINEARE (PUSHOVER): la struttura e' sottoposta a distribuzione di forze orizzontali crescenti (modale o uniforme) fino al collasso; fornisce la curva capacita' (spinta vs spostamento), il punto di performance (confronto con domanda sismica), i meccanismi di rottura.

2. ANALISI DINAMICA NON LINEARE (TIME-HISTORY): integrazione passo-passo delle equazioni del moto con accelerogrammi reali o artificiali, con modelli isteretici (plasticita' concentrata o diffusa); la piu' raffinata ma costosa.

3. MODELLI COSTITUTIVI: plastic hinges (moment-curvature), fibre, elementi con danno, link elements per dispositivi di isolamento e smorzamento.

4. VERIFICHE PERFORMANCE-BASED: stati limite di operativita' (IO), vita (LS), prevenzione collasso (CP) secondo FEMA 356, ASCE 41, NTC 2018 (per le verifiche non lineari degli esistenti).

5. UTILIZZO: progettazione antisismica avanzata, valutazione degli esistenti, strutture con dispositivi di controllo, strutture irregolari."""))
S.append(("strutture_avanzate","grandi_luci",
"TENSOSTRUTTURE, RETICOLI E GRANDI LUCI",
"""Le coperture di grande luce (50-300 m) usano sistemi reticolari e tensionati:

1. RETICOLI SPAZIALI (space frames): nodi sferici o cilindrici con aste tubolari, coprono 20-100 m con struttura leggera e rigida; usati per capannoni, palazzetti, hangar.

2. TRAVI RETICOLARI (trusses): per luce 30-80 m, con catena superiore e inferiore (Warren, Pratt, Howe); in acciaio o legno.

3. TENSOSTRUTTURE: membrane (PVC/PVDF/PTFE) tese tra cavi o strutture, luce 10-150 m; leggerissime (2-5 kg/m²), traslucide, forme anticlastiche; esempi: stadi, coperture temporanee, tensostrutture a cavi (Denver Airport).

4. SISTEMI A CAVO (cable nets): reti di cavi tesi con nodi, coprono luci maggiori con spessori minimi (es. copertura olimpionica).

5. PNEUMATICHE: membrane gonfie con aria pressurizzata, luce 10-100 m, uso temporaneo o semi-permanente.

6. PROGETTAZIONE: forma funzionale (tensioni nel cavo/asta), verifiche di instabilita' locale, giunzioni nodali critiche, messa in tensione controllata."""))
S.append(("strutture_avanzate","strutture_speciali",
"TORRI INDUSTRIALI, SERBATOI E SILOS",
"""Le strutture speciali (torri, serbatoi, silos) hanno vincoli di funzionamento e sicurezza specifici:

1. TORRI: torri di raffreddamento (iperboloidi in c.a. o acciaio), torri metalliche per antenne (tralicci), torri di processo chimico; azioni: vento, sisma, carichi di esercizio, gradienti termici.

2. SERBATOI: contenitori di liquidi (acqua, olii, combustibili) in c.a., acciaio o GRP; verifiche di tenuta, sollecitazioni idrostatiche, solaio di copertura, scale di ispezione, sistemi di rilevamento livello e tracimazione.

3. SILOS: contenitori di materiali sfusi (cereali, cemento, concimi); azioni: peso proprio, spinta del contenuto (Janssen), carichi eccentrici, flessione, instabilita' del guscio, corrosione da abrasione.

4. NORME: EN 1993-4-1 (silos e serbatoi in acciaio), EN 1991-4 (azioni nei silos), API 650 (serbatoi petroliferi), NTC 2018 per le azioni.

5. PROBLEMATICHE: fatica, corrosione, instabilita' del guscio (EBU - elephant foot buckling), messa in opera, giunzioni."""))
S.append(("strutture_avanzate","strutture_composite",
"STRUTTURE IBRIDE ACCIAIO-CALCESTRUZZO E LEGNO-CLT",
"""Le strutture ibride combinano i materiali per ottimizzare prestazioni e costi:

1. ACCIAIO-CALCESTRUZZO (SRC - Steel Reinforced Concrete): colonne e travi con anime metalliche ingabbiate in c.a., connettori a taglio (shear studs); sfrutta la resistenza a compressione del c.a. e a trazione dell'acciaio.

2. COMPOSITO PONTE: impalcato con travi in acciaio e soletta collaborante in c.a. (con shear studs); la sezione composita aumenta la rigidezza del 30-50%.

3. LEGNO-CALCESTRUZZO (Timber-Concrete Composite, TCC): solai in legno con calcestruzzo collaborante, con connettori; aumenta la rigidezza e il masso del solaio, riducendo l'altezza.

4. LEGNO-ACCiAiO (Hybrid Timber Steel): telai con colonne in acciaio e travi in legno (o viceversa), per edifici con grandi luci e finiture in legno.

5. VANTAGGI: ottimizzazione dei materiali, riduzione dei pesi, aumento della rigidezza, velocita' di costruzione, estetica."""))

# ============ writer ============
os.makedirs('parsed', exist_ok=True)
meta = {
    "source": "edilizia_avanzata_kimi",
    "license": "Sintesi didattica originale Kimi (pubblico dominio)",
    "commercial_ok": True,
    "attribution": "Corpus edilizia avanzata a cura di Kimi",
    "url": "",
}
out = []
for i, (cat, tema, titolo, testo) in enumerate(S, 1):
    rec = dict(meta)
    rec.update({"id": f"AVA-{i:03d}", "categoria": cat, "tema": tema, "title": titolo, "text": testo.strip()})
    out.append(rec)

path = os.path.join('Edilizia_Pack', 'parsed', 'edilizia_avanzata.jsonl')
os.makedirs(os.path.dirname(path), exist_ok=True)
with open(path, 'w', encoding='utf-8') as f:
    for r in out:
        f.write(json.dumps(r, ensure_ascii=False) + '\n')
print(f"scritte {len(out)} schede edilizia avanzata -> {os.path.abspath(path)}")
