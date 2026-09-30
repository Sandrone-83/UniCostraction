# -*- coding: utf-8 -*-
"""Corpus Infrastrutture: ponti, strade, ferrovie, dighe, tunnel."""
import json, os

S = []

S.append(("ponti_tipologie",
"I PONTI: TIPOLOGIE E ELEMENTI COSTRUTTIVI",
"""Il ponte e' l'opera d'ingegneria piu' emblematica: attraversa un ostacolo sostenendo la circolazione:

1. ELEMENTI: impalcato (la struttura portante), spalle (appoggi di estremita'), pile (appoggi intermedi), fondazioni, apparecchi di appoggio (scaricano gli spostamenti), giunti (assorbono dilatazioni), impalcato stradale o ferroviario, parapetti e sistemi di sicurezza.

2. TIPOLOGIE STRUTTURALI:
   - Travi: reticolari, piene (prefabbricate o gettate in opera), continue (piu' campate).
   - Arco: spinge orizzontalmente (richiede spalle resistenti o tiranti).
   - Sospesi: cavi principali + impalcato (luci oltre 500-1.000 m).
   - Strallati: torre + stralli (luci 200-1.100 m, tipo Millau, Morandi originale).
   - Travi a cassone (box girder) in acciaio o c.a. per grandi luci.

3. MATERIALI: calcestruzzo precompresso (il piu' diffuso), acciaio, compositi acciaio-calcestruzzo, strutture in legno per ponti minori.

4. PROGETTAZIONE: verifiche agli SLU (flessione, taglio, torsione, instabilita' locale) e SLE (frecce, vibrazioni, fessurazione), azioni traffico, vento, sisma, urto."""))

S.append(("ponti_carichi",
"LE AZIONI SUI PONTI",
"""Il dimensionamento dei ponti si basa sulle azioni previste in esercizio e in costruzione:

1. CARICO PERMANENTE: peso proprio della struttura, dei ballatoi, degli impianti, del manto stradale, delle barriere di sicurezza.

2. CARICO DI TRAFFICO (NTC 2018, LM1 e LM2):
   - LM1: carichi uniformi sulle corsie (10 kN/m²) e assi di veicoli (300 kN) per le verifiche globali.
   - LM2: asso singolo (400 kN) per le verifiche locali (impalcato, pavimentazione).
   - LM3/4: veicoli speciali e carichi eccezionali per ponti specifici.

3. AZIONI AMBIENTALI: vento (pressione sulla superficie esposta, raffica), neve (sull'impalcato), sisma (con comportamento dissipativo o isolato), temperatura (gradienti termici, dilatazioni).

4. AZIONI ECCEZIONALI: urto dei veicoli (parapeti e pile), incendio, alluvione (per le pile nel fiume), cedimento di una campata (robustezza progressiva).

5. COMBINAZIONI: fondamentali (permanente + traffico + variabili), frequenti, quasi permanenti, sismiche, di costruzione (fasi provvisorie)."""))

S.append(("calcestruzzo_precompresso",
"IL CALCESTRUZZO PRECOMPRESSO",
"""La precompressione ha rivoluzionato le strutture in c.a. permettendo luci e sezioni maggiori:

1. PRINCIPIO: si tendono armature ad alto limite elastico (armature pre-tese o post-tese) prima o dopo il getto, comprimendo il calcestruzzo. La compressione previene la fessurazione da carichi di esercizio.

2. TECNICHE:
   - Pre-tensione: cavi tesi prima del getto, ancorati ai puntoni della cassaforma; usato per elementi prefabbricati (travi, travetti, pannelli).
   - Post-tensione: cavi tesi dopo il getto e l'hardizimento, inseriti in guaine ondulate e ancorati con testate attive o fisse; usato per ponti, solai di grandi luci, serbatoi.

3. VANTAGGI: minori frecce e fessure, materiali piu' snelli, maggiori luci, durabilita' superiore, minori costi di manutenzione.

4. PROBLEMATICHE: perdite di tensione (viscosita', ritiro, rilassamento), corrosione dei cavi (richiedono iniezione di cemento o cere), rischio fragilita' in caso di degrado, costi iniziali piu' elevati.

5. APPLICAZIONI: ponti, viadotti, solai, coperture, serbatoi, strutture marine, elementi prefabbricati."""))

S.append(("strade",
"LE STRADE: CLASSIFICAZIONE E SEZIONI TIPO",
"""La strada e' l'infrastruttura lineare piu' diffusa:

1. CLASSIFICAZIONE FUNZIONALE: autostrade, strade extraurbane principali, secondarie, locali; urbane (arteriali, secondarie, locali).

2. ELEMENTI DELLA SEZIONE: carreggiata (corsie e banchine), spartitraffico, banchina, fosso, ciglio, cunetta, paratoie, segnaletica, barriere di sicurezza (guard-rail o New Jersey), drenaggi (laterali, sottoservizi).

3. PAVIMENTAZIONE: struttura a strati (fondo, sottofondo, base, legante, usura); materiali: asfalti (bitume + inerti), calcestruzzo, pavimentazioni semplici (stenopatie). Lo spessore dipende dal traffico (ESA: equivalenti standard assi).

4. PROGETTAZIONE: geometrica (raggio minimo, pendenza massima, visibilita'), pavimentale (metodo analitico AASHTO o cataloghi), drenaggio (scarichi, tombini, canalette).

5. MANUTENZIONE: rinfreschi bituminosi, ripristini parziali, rifacimento del manto ogni 15-25 anni."""))

S.append(("ferrovie",
"LE FERROVIE: BINARI, MASSICCIATA E OPERE D'ARTE",
"""La ferrovia e' il sistema di trasporto con la struttura piu' complessa:

1. BINARIO: rotaie (acciaio, 50-60 kg/m), traverse (legno, cemento, acciaio), pattini, bulloni, massicciata (ghiaia frantumata 30-40 cm), sottostructura (stabilizzato, migliorato terreno).

2. GEOMETRIA DEL TRACCIATO: pendenza massima (12-35 per mille secondo il tipo di linea), raggio minimo delle curve (300-4.000 m), soprelevazione e lunghezza di raccordo, scartamento standard 1.435 mm.

3. OPERE D'ARTE: ponti ferroviari (carichi piu' pesanti e dinamici di quelli stradali), gallerie (sezione maggiorata per l'aerodinamica), sottovia, soppressioni, stazioni.

4. SISTEMI: alimentazione elettrica (3 kV cc, 25 kV ca), segnalamento (blocco, ATP, ERTMS per l'alta velocita'), sicurezza (barriere, passaggi a livello).

5. COSTRUZIONE: posa del binario con cantieri di armamento (tradizionale o con macchine automatiche), compattazione della massicciata, collaudo con prove di carico dinamico."""))

S.append(("dighe",
"DIGHE E OPERE IDRAULICHE",
"""Le dighe sfruttano l'acqua per l'irrigazione, l'approvvigionamento e la produzione idroelettrica:

1. TIPOLOGIE:
   - A gravità: resiste con il proprio peso (muratura, calcestruzzo).
   - Ad arco: scarica le spinte sugli speroni (calcestruzzo).
   - A contrafforti: con contrafforti verticali che irrigidiscono (calcestruzzo o materiali locali).

2. ELEMENTI: corpo diga, scarichi (di superficie, di fondo, evacuatori), presa d'acqua, centrali idroelettriche (condotte forzate, turbine), bacino di accumulo.

3. PROGETTAZIONE: stabilità (ribaltamento, scorrimento, portanza), azioni idrodinamiche, filtrazione (gradienti idraulici, opere di drenaggio), sisma, vuoto (ondulazioni del lago).

4. COSTRUZIONE: getti successivi con giunti, raffreddamento del calcestruzzo (il calore di idratazione puo' fessurare), grouting delle fondazioni, riempimento graduale.

5. SICUREZZA: collaudo, monitoraggio (pendoli, estensimetri, piezometri), procedure di gestione delle piene."""))

S.append(("opere_marittime",
"OPERE MARITTIME E COSTRUZIONI IN AMBIENTE MARINO",
"""Le costruzioni marine affrontano l'ambiente piu' aggressivo per i materiali:

1. OPERE: dighe foranee (a scogli o a calcestruzzo), moli e banchine, pontili, strutture offshore (fondazioni eoliche), condotte sottomarine, dragaggi.

2. AZIONI: onde (spinte, rissalita, impatto), correnti, maree, sisma maremoto (tsunami), sprofondamento del fondale, usura ambientale.

3. MATERIALI: calcestruzzo con inerti resistenti e basso contenuto di cloruri, acciaio con protezione catodica (anodi sacrificali o corrente imposta), rocce di grande pezzatura per le dighe a scogli.

4. FONDAMENTAZIONI: pali infissi, cassoni a depressione (svasati e riempiti), fondazioni a gravità, fondazioni su micropali.

5. NORME: Eurocodici con documenti di applicazione per l'ambiente marino, classi di esposizione XA (cloruri) e XS per il calcestruzzo."""))

S.append(("tunnel",
"I TUNNEL: COSTRUZIONE E SICUREZZA",
"""I tunnel attraversano le montagne e i centri urbani con l'ingegneria piu' avanzata:

1. METODI COSTRUTTIVI:
   - Tradizionale (NATM - New Austrian Tunnelling Method): scavo progressivo con sostegno in calcestruzzo spruzzato (shotcrete), boulons e armature.
   - Meccanizzato (TBM - Tunnel Boring Machine): scavatrice a testa rotante per lunghe gallerie.
   - Cut-and-cover per tratti superficiali.
   - Immersione (elementi prefabbricati posati sul fondo) per tunnel sottomarini.

2. PROBLEMI GEOTECNICI: pressioni laterali, carichi di spinta, instabilita' del fronte, acqua in pressione, gas, terreni deformabili (in urbano: cedimenti controllati).

3. SICUREZZA IN CANTIERE: il D.Lgs 81/2008 e la norma UNI 11224 per le attivita' in sotterraneo; rischi: crolli, incendi, inondazioni, mancanza d'aria; sistemi di ventilazione, illuminazione di emergenza, comunicazioni, vie di fuga.

4. SISTEMI COMPLEMENTARI: ventilazione (longitudinale o trasversale), illuminazione, segnaletica, sistemi di gestione traffico e incendio."""))

os.makedirs('parsed', exist_ok=True)
meta = {
    "source": "infrastrutture_kimi",
    "license": "Sintesi didattica originale Kimi (pubblico dominio)",
    "commercial_ok": True,
    "attribution": "Corpus infrastrutture a cura di Kimi",
    "url": "",
}
out = []
for i, (tema, titolo, testo) in enumerate(S, 1):
    rec = dict(meta)
    rec.update({"id": f"INF-{i:02d}", "tema": tema, "title": titolo, "text": testo.strip()})
    out.append(rec)

path = os.path.join('Edilizia_Pack', 'parsed', 'infrastrutture.jsonl')
os.makedirs(os.path.dirname(path), exist_ok=True)
with open(path, 'w', encoding='utf-8') as f:
    for r in out:
        f.write(json.dumps(r, ensure_ascii=False) + '\n')
print(f"scritte {len(out)} schede infrastrutture -> {os.path.abspath(path)}")
