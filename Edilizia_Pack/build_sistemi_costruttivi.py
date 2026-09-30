# -*- coding: utf-8 -*-
"""Genera il corpus Sistemi Costruttivi Internazionali."""
import json, os

C = []

C.append(("timber_frame",
"TIMBER FRAME - IL TELAIO IN LEGNO TRADIZIONALE INGLESE",
"""Il timber frame (telaio in legno) e' il sistema costruttivo tradizionale dell'Inghilterra medievale e delle regioni nordiche:

1. STRUTTURA: telaio portante in legno di quercia o abete, con travi incrociate a tenone e mortasa, triangoli di controventamento e riempimento in mattone o intonaco (wattle and daub, poi brick nogging).

2. VANTAGGI: flessibilita' planimetrica, rapidita' di costruzione, leggerezza strutturale, reversibilita' degli elementi.

3. PROBLEMATICHE: rischio incendio (i tetti di paglia o scandole erano la causa), umidita' di risalita (i muri in terra cruda o mattone non isolano), parassiti del legno.

4. EVOLUZIONE: dal telaio tradizionale si e' passati al platform frame (America del Nord) e al balloon frame, con elementi piu' standardizzati e giunti meccanici.

5. RESTAURO: il recupero del timber frame richiede la sostituzione selettiva dei pezzi degradati, il ripristino dei giunti tradizionali e l'inserimento di isolamento compatibile.

Il timber frame e' la radice della costruzione moderna in legno e la base della comprensione dei sistemi prefabbricati."""))

C.append(("platform_frame",
"PLATFORM FRAME - IL SISTEMA COSTRUTTIVO AMERICANO",
"""Il platform frame e' il sistema costruttivo standard dell'edilizia residenziale nordamericana dagli anni 1830:

1. STRUTTURA: pareti portanti in listelli di legno (studs) di sezione 2x4 o 2x6 pollici (38x89 o 38x140 mm), interasse 40 o 60 cm, con piastre orizzontali (piattabanda e basamento) e controventi in lastre di compensato (shear walls). Ogni piano poggia sul solaio del precedente (da qui 'platform').

2. VANTAGGI: uso efficiente del legno, costruzione sequenziale rapida, facile integrazione di isolamento (lana di vetro tra gli stud), standardizzazione delle componenti (2x4, 4x8 ft).

3. PROBLEMATICHE: resistenza al fuoco (richiede lastre di cartongesso rivestimento), isolamento termico (ponte termico degli stud, risolto con stud doppi o esterni), rischio sismico (richiede controventi e ancoraggi specifici nelle zone sismiche della California e del Pacifico).

4. VARIANTE: il balloon frame (studi continui dai 2 ai 3 piani) e' stato abbandonato per problemi di incendio e instabilita'.

5. DIFFUSIONE: Stati Uniti, Canada, Australia, Nuova Zelanda. E' il sistema piu' diffuso al mondo per l'edilizia residenziale."""))

C.append(("clt",
"CLT - CROSS LAMINATED TIMBER E L'EDILIZIA IN LEGNO CONTEMPORANEA",
"""Il CLT (Cross Laminated Timber) e' il pannello in legno multistrato incrociato che ha rivoluzionato l'edilizia in legno:

1. STRUTTURA: pannelli in listelli di legno (abeti, pino, larice) incollati a strati incrociati a 90 gradi, con spessori da 60 a 300 mm e dimensioni fino a 3x12 m. Le strutture portanti sono pareti e solai in pannelli CLT.

2. PRESTAZIONI: resistenza meccanica elevata (classe GL24-GL32), rigidita' sismica, stabilita' dimensionale (gli strati incrociati bilanciano l'umidita'), buon isolamento termo-acustico.

3. VANTAGGI: prefabbricazione di precisione, rapidita' di montaggio (una casa in 2-4 settimane), peso 1/5 del calcestruzzo (riduzione fondazioni e sisma), stoccaggio carbonico (-1 t CO2/m³ di legno), estetica calda.

4. PROBLEMATICHE: costo attualmente superiore al calcestruzzo in Italia (ma in calo), protezione dal fuoco (sovra-dimensionamento sezioni o rivestimenti intumescenti), umidita' in fase di cantiere, certificazione antisismica.

5. APPLICAZIONI: edifici residenziali e commerciali fino a 8-10 piani (in Austria e Norvegia si arriva a 18 piani con sistemi ibridi), scuole, palestre, hotel."""))

C.append(("steel_stud",
"STEEL STUD - IL TELAIO IN ACCIAIO LEGGERO",
"""Lo steel stud (telaio in acciaio leggero) e' l'alternativa metallica al platform frame in legno:

1. STRUTTURA: profili in acciaio zincato a freddo (C-profiles o U-profiles) di spessore 0,5-2 mm, interasse 40-60 cm, con pannelli di rivestimento in lastre di gesso (drywall) o cemento. I profili formano pareti portanti o tamponamenti.

2. VANTAGGI: leggerezza (un terzo del legno), immunita' da parassiti e umidita', non combustibilita' (A1), precisione dimensionale, riciclabilita'.

3. PROBLEMATICHE: ponte termico (gli stud metallici attraversano l'isolamento, risolto con stud esterni o doppi strati), corrosione in ambienti aggressivi, costo superiore al legno in molte zone.

4. APPLICAZIONI: tamponamenti interni, pareti divisorie, controsoffitti, tetti, edilizia commerciale e industriale, rinforzi strutturali in edilizia esistente.

5. SISTEMI: i sistemi piu' diffusi sono i profili C con flangia larga (34-92 mm) per pareti portanti e i profili C sottili (13-25 mm) per tamponamenti e controsoffitti."""))

C.append(("terra_cruda",
"LA COSTRUZIONE IN TERRA CRUDA - ADOBE, PISE' E MATTONI DI TERRA",
"""La costruzione in terra cruda e' una delle tecniche piu' antiche e attuali, con una rinascita sostenibile:

1. MATERIALI: terra cruda (argilla, sabbia, limo, fibra vegetale), talvolta con additivi naturali (paglia, segatura, calce).

2. TECNICHE:
   - Adobe: mattoni di terra essiccati al sole, impilati con malta di terra.
   - Pise' (rammed earth): terra compattata in casseforme a strati, con superficie stratificata caratteristica.
   - Cob: muri costruiti per aggiunta di impasto di terra e paglia.
   - Mattoni di terra compressa (BTC o CEB): prodotti con presse meccaniche, piu' resistenti degli adobe.

3. VANTAGGI: sostenibilita' (materiale di scavo o riciclo), regolazione igrometrica (assorbe e rilascia umidita'), isolamento termico, basso impatto ambientale, estetica naturale.

4. PROBLEMATICHE: resistenza meccanica (richiede consolidamenti o intonaci protettivi), sensibilita' all'acqua (richiede basamenti rialzati e coperture importanti), accettazione normativa (in Italia il progetto richiede validazioni specifiche).

5. APPLICAZIONI: edilizia rurale, case ecologiche, edilizia in contesti aridi, restauro di architettura tradizionale."""))

C.append(("costruzione_paglia",
"LE CASE DI PAGLIA - DALLA BAITA ALL'ARCHITETTURA CONTEMPORANEA",
"""La costruzione in paglia (straw bale building) e' una tecnica con una storia millenaria e una rinascita contemporanea:

1. TECNICHE:
   - Nebraska style: balle di paglia portanti, impilate come mattoni, con corde o stecche di legno.
   - Infill: balle di paglia come riempimento di un telaio portante in legno o acciaio.
   - Greccia (Italia): muri in paglia compressa con terra, tradizione toscana.

2. CARATTERISTICHE: isolamento termico eccellente (R 6-8 m²K/W per parete da 45-50 cm), regolazione igrometrica, disponibilita' del materiale (sottoprodotto agricolo), basso costo del materiale.

3. PROBLEMATICHE: sensibilita' all'umidita' (richiede coperture importanti e intonaci traspiranti), durabilita' nel tempo (richiede manutenzione degli intonaci), accettazione assicurativa e normativa.

4. PROGETTAZIONE: il punto critico e' la tenuta all'umidita' (base rialzata, grondaie, intonaci di calce o terra), la protezione dal fuoco (intonaci spessi, caminetti distanziati) e la protezione dai roditori (reti metalliche).

5. APPLICAZIONI: edilizia rurale, case ecologiche, edilizia sociale a basso costo, architettura contemporanea sostenibile."""))

C.append(("case_passive",
"LE COSTRUZIONI PASSIVE - DAL PASSIVHAUS AL NZEB",
"""L'edilizia passiva rappresenta lo stato dell'arte dell'efficienza energetica:

1. PRINCIPI: l'involucro (superisolamento, finestre performanti, eliminazione ponti termici) riduce le dispersioni a un livello tale che il fabbisogno e' coperto dai guadagni gratuiti (solare, corpi umani, elettrodomestici) e dal recupero di calore della ventilazione.

2. CRITERI PASSIVHAUS (standard tedesco):
   - Fabbiogno di riscaldamento <= 15 kWh/(m²a)
   - Fabbiogno di raffrescamento <= 15 kWh/(m²a)
   - Fabbiogno primario <= 120 kWh/(m²a)
   - Airtightness n50 <= 0,6 ricambi/h
   - Guadagni estivi con schermature e ventilazione notturna.

3. STRATEGIE: orientamento sud, forme compatte, isolamento continuo, finestre Uw <= 0,85-1,0 W/m²K, VMC con rendimento >= 75%, eliminazione ponti termici (psi <= 0,01 W/mK).

4. CONFRONTO CON NZEB: lo standard europeo NZEB richiede fabbisogni coperti da rinnovabili per una quota significativa, senza limiti quantitativi cosi' stringenti come il Passivhaus. Il Passivhaus e' piu' rigido sulle prestazioni, il NZEB piu' flessibile sulle soluzioni.

5. COSTI: in Italia il sovrapprezzo rispetto alla costruzione standard e' del 5-15%, con payback energetico di 10-15 anni."""))

C.append(("tetti_nordici",
"I TETTI NORDICI - FALDE, CAMERA D'ARIA E ISOLAMENTO PESANTE",
"""Il tetto nordico (a falde inclinate con isolamento pesante) e' la risposta ai climi freddi e nevosi:

1. STRATIGRAFIA TIPO: manto (tegole, scandole, lastre), controsoffitto ventilato, falda (orditura in legno), isolante pesante (lana di roccia o cellulosa 25-40 cm), parovento, camera d'aria ventilata, controsoffitto interno.

2. PRINCIPI: la camera d'aria ventilata elimina la condensa, l'isolamento pesante (posato sopra l'orditura o tra i listelli) riduce i ponti termici, il tetto ventilato elimina il carico nevico.

3. VARIANTI:
   - Tetto caldo (insulation on top of the roof deck) vs tetto freddo (insulation between rafters).
   - Tetto ventilato (con camera d'aria) vs tetto non ventilato (con barriera vapore esterna).
   - Tetto a falde singole vs falde multiple.

4. MATERIALI: tegole in laterizio, scandole in legno (cedar shakes), lastre in ardesia, metallo (rame, zinco, acciaio), membrane sottotegola traspiranti.

5. PROGETTAZIONE: pendenza minima (tegole 25-30%, lastre 15-20%), sbalzi per protezione solare e pioggia, grondaie dimensionate per il carico nevico, scarichi da neve se necessario."""))

C.append(("edilizia_giapponese",
"L'EDILIZIA TRADIZIONALE GIAPPONESE - LEGNO E SCIOGLIMENTO",
"""L'architettura tradizionale giapponese e' un sistema costruttivo in legno con principi unici:

1. MATERIALI: legno di cipresso (hinoki), pino e cedro, con giunti in legno senza chiodi (kigumi).

2. TECNICHE:
   - Telaio a travi e colonne con nodi incastrati (kigumi).
   - Fondazioni in pietra (ishi-date) che isolano il legno dall'umidita' e dal terreno.
   - Tatami (pavimenti in paglia), shoji (pannelli scorrevoli in carta), fusuma (pannelli scorrevoli in legno).
   - Ampie falde di copertura in tegole di argilla (kawara) o paglia (kaya).

3. PRINCIPI: flessibilita' sismica (il telaio in legno e' elastico e ammortizza), reversibilita' (gli elementi sono sostituibili), rispetto della natura (materiali naturali, integrazione col paesaggio).

4. PROBLEMATICHE: durabilita' del legno (richiede manutenzione e trattamenti), vulnerabilita' al fuoco, alla umidita' e ai parassiti.

5. INFLUENZA: l'architettura giapponese ha influenzato l'architettura moderna occidentale (Frank Lloyd Wright, minimalismo, interni flessibili)."""))

C.append(("costruzione_metallica",
"LE COSTRUZIONI METALLICHE - DAL FERRO ALL'ACCIAIO",
"""Le costruzioni metalliche hanno una storia che copre due secoli:

1. EVOLUZIONE: il ferro (ghisa e ferro battuto) per ponti e strutture industriali nel Settecento-Ottocento, l'acciaio (acciaio Bessemer, 1856) per grattacieli e ponti dal Novecento, l'acciaio ad alta resistenza e gli acciai inossidabili per le strutture contemporanee.

2. TIPI DI STRUTTURA:
   - Telaio a travi e colonne (beam and column).
   - Travi reticolari (trusses) per luci importanti.
   - Strutture a guscio (shells) e tensostrutture per coperture leggere.
   - Piattaforme industriali e torri.

3. CARATTERISTICHE: resistenza meccanica elevata (fyk 235-460 MPa), leggerezza, prefabbricazione, velocita' di montaggio, riciclabilita'. Svantaggi: vulnerabilita' al fuoco (richiede rivestimenti intumescenti), instabilita' delle aste snelle (raggio di rotazione, irrigidimenti), corrosione.

4. GIUNTI: saldati (pieni penetrazione), bullonati (attrito o appoggio), incernierati. La scelta influenza la velocita' di cantiere e la robustezza sismica.

5. APPLICAZIONI: ponti, grattacieli, hangar, palazzetti sportivi, strutture industriali, tetti di grandi luci."""))

C.append(("costruzione_modulare",
"LA COSTRUZIONE MODULARE E PREFABBRICATA",
"""La costruzione modulare e' la fabbricazione di edilizia in stabilimento con montaggio in cantiere:

1. TIPI:
   - Moduli completi (3D): box completi di struttura, tamponamento, impianti e finiture, trasportati e impilati.
   - Pannelli (2D): pareti e solai prefabbricati, assemblati in cantiere.
   - Componenti (1D): elementi strutturali, telaio, impianti preassemblati.

2. VANTAGGI: velocita' di cantiere (ridotta del 30-60%), qualita' controllata in stabilimento, riduzione sprechi, sicurezza (meno lavori in quota), minore impatto ambientale del cantiere.

3. PROBLEMATICHE: vincoli di trasporto (dimensioni moduli, 3,5x4x12 m massimo su strada), giunti tra moduli (tenuta, ponti termici, acustica), rigidita' progettuale (standardizzazione), accettazione normativa e assicurativa.

4. APPLICAZIONI: edilizia residenziale, ospedali, scuole, hotel, studentati, case temporanee di emergenza.

5. PROSPETTIVE: la costruzione modulare e' la direzione di sviluppo dell'edilizia industriale, con crescente integrazione di robotica, BIM e materiali avanzati."""))

os.makedirs('parsed', exist_ok=True)
meta = {
    "source": "sistemi_costruttivi_kimi",
    "license": "Sintesi didattica originale Kimi (pubblico dominio)",
    "commercial_ok": True,
    "attribution": "Corpus sistemi costruttivi internazionali a cura di Kimi",
    "url": "",
}
out = []
for i, (sistema, titolo, testo) in enumerate(C, 1):
    rec = dict(meta)
    rec.update({"id": f"COST-{i:02d}", "sistema": sistema, "title": titolo, "text": testo.strip()})
    out.append(rec)

path = 'parsed/sistemi_costruttivi.jsonl'
with open(path, 'w', encoding='utf-8') as f:
    for r in out:
        f.write(json.dumps(r, ensure_ascii=False) + '\n')
print(f"scritte {len(out)} schede sistemi costruttivi -> {os.path.abspath(path)}")
