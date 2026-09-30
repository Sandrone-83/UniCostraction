# -*- coding: utf-8 -*-
"""Corpus Antincendio: normativa, prevenzione, strutture e impianti."""
import json, os

S = []

S.append(("quadro_normativo",
"IL QUADRO NORMATIVO ANTINCENDIO ITALIANO",
"""La prevenzione incendi in Italia e' regolata da un corpus normativo complesso:

1. D.M. 3 AGOSTO 2015: regola la prevenzione incendi per le attivita' soggette (industrie, centri commerciali, uffici sopra certe superfici, scuole, ospedali, alberghi, discoteche). Stabilisce i requisiti di progetto (conformita' tecnica) o la possibilita' di usare codici di prevenzione o prove sperimentali.

2. VIGILI DEL FUOCO: il comando provinciale VVF rilascia il certificato di prevenzione incendi (CPI) a seguito di istruttoria della pratica di prevenzione incendi presentata dal progettista (moduli SCU).

3. DIRETTIVA 2019/856: recepita in Italia, ha riorganizzato la prevenzione incendi introducendo l'approccio basato sul rischio (risk-based approach) e il ruolo dei professionisti certificatori.

4. ALTRE NORME: D.M. 24 luglio 2021 (sicurezza antincendio nei cantieri temporanei), UNI EN 13501 (classificazione resistenza al fuoco), UNI EN 1363 (curve di riscaldamento), UNI 9174/UNI 9177 (classificazione reazione al fuoco dei materiali).

5. RESPONSABILITA': il committente e' responsabile della manutenzione degli impianti; il progettista risponde della conformita' del progetto; i controlli VVF sono a campione o sistematici a seconda della soglia di rischio.

Per il tecnico che progetta attivita' soggette, la conoscenza del D.M. 3/8/2015 e dei codici di prevenzione e' indispensabile prima di avviare il progetto."""))

S.append(("resistenza_fuoco",
"RESISTENZA AL FUOCO E COMPARTIMENTAZIONE",
"""La resistenza al fuoco e' la capacita' di un elemento o struttura di mantenere le proprie funzioni durante l'incendio:

1. CRITERI REI: R (resistenza meccanica: portare i carichi), E (tenuta: non lasciare passare fiamme e gas), I (isolamento termico: limitare la temperatura sul lato non esposto a 140 °C medio / 180 °C max). Un muro REI 120 mantiene queste caratteristiche per 120 minuti.

2. CLASSIFICAZIONE: elementi portanti (R), pareti divisorie (EI), coperture (RE), porte (EI1 o EI2 per il senso di chiusura), canalizzazioni (EI).

3. COMPARTIMENTAZIONE: l'edificio e' diviso in compartimenti antincendio (di solito 1.500-3.000 m²) con pareti e solai REI; i passaggi (porte, varchi, canalizzazioni) devono mantenere la resistenza (serrande tagliafuoco, porte REI, materie plasticiche intumescenti).

4. METODI DI PROGETTO: analisi sperimentale (curve ISO 834), calcolo con modelli termici e meccanici ( Eurocodici EN 1991-1-2, 1992-1-2, 1993-1-2, 1994-1-2, 1995-1-2, 1996-1-2), tabelle di abachi (per le strutture piu' comuni).

5. MATERIALI: acciaio (sgradevole sopra 500-600 °C: richiede intonaci, vernici intumescenti o cladding), calcestruzzo (buona resistenza ma esplosione per riscaldo idrico), legno (carbonizza prevedibilmente: sezioni maggiori), muratura (ottima resistenza)."""))

S.append(("vie_fuga",
"VIE DI FUGA ED EVACUAZIONE",
"""Le vie di fuga sono il percorso che gli occupanti devono compiere per mettersi in salvo:

1. PRINCIPI: ogni ambiente deve avere almeno due vie di fuga alternative quando possibile; le vie di fuga devono condurre all'esterno o a luogo sicuro in modo autonomo (senza dipendere da impianti).

2. PARAMETRI GEOMETRICI: larghezza minima delle uscite (tipicamente 1,00-1,20 m per luoghi di lavoro, 0,90 m per abitazioni), numero minimo di uscite in funzione della superficie e del numero di occupanti, percorso massimo in funzione del rischio e della resistenza al fuoco (tipicamente 25-45 m).

3. ELEMENTI: porte REI con apertura verso l'esterno o verso il percorso di fuga, scale con pareti REI e porte REI, corridoi con reazione al fuoco limitata, uscite con larghezza totale adeguata al numero di occupanti.

4. LUNGHEZZA DI FUGA: distanza massima da coprire in funzione del pericolo d'incendio (basso, medio, alto, molto alto) e della resistenza al fuoco della struttura; e' misurata lungo il percorso piu' sfavorevole.

5. EVACUAZIONE: per luoghi di lavoro serve un piano di evacuazione con percorso segnalato, addetti antincendio e di piano, prove di evacuazione periodiche."""))

S.append(("scenario_incendio",
"SCENARI DI INCENDIO E PROGETTAZIONE PREVISIONALE",
"""Il progetto antincendio si basa sulla previsione dell'evoluzione dell'incendio:

1. CURVA TEMPO-TEMPERATURA ISO 834: rappresenta l'incendio standard (celluloosico): temperatura che cresce rapidamente fino a oltre 1.000 °C in 2 ore. Altri incendi: idrocarburi (curva rapida), incendio esterno.

2. CARICO D'INCENDIO: energia potenzialmente sviluppabile da tutti i materiali combustibili presenti (MJ/m² di superficie di pavimento). Valori tipici: uffici 400-800 MJ/m², biblioteche 1.000-2.000 MJ/m², depositi 2.000-4.000 MJ/m².

3. MODELLI DI EVOLUZIONE: crescita del fuoco (curva potenziale), fase di sviluppo, fase di regime (ventilation-controlled o fuel-controlled), fase di estinuzione.

4. SCENARI DI PROGETTO: incendio nel compartimento piu' sfavorevole, propagazione verticale (camini di fumo), propagazione orizzontale, incendio esterno con irraggiamento.

5. STRATEGIE: compartimentazione, spegnimento automatico (sprinkler), controllo fumi (sfogo o ventilazione), evacuazione controllata."""))

S.append(("rivelazione_allarme",
"IMPIANTI DI RIVELAZIONE E ALLARME",
"""La rivelazione precoce e l'allarme permettono l'evacuazione tempestiva:

1. RIVELATORI: fumo (ottici, ionici, lineari), calore (termici, a temperatura fissa o a velocita' di aumento), fiamma (UV/IR), gas. La scelta dipende dal tipo di ambiente (fumoso, polveroso, con alti soffitti).

2. SISTEMI: centrali di rivelazione indirizzate (identificano il punto esatto) o convenzionali (zone), con segnalazione visiva e acustica interna ed esterna.

3. ALLARME: sistemi di altoparlanti (evacuazione guidata), pulsantiere manuali, connessione al sistema di gestione dell'edificio (BMS).

4. COLLEGAMENTI: interblocchi con porte REI (chiusura automatica), serrande tagliafuoco, impianti di spegnimento, ascensori (richiamo al piano, esclusi in caso di incendio), Ventilazione controlata.

5. NORME: UNI EN 54 (sistemi di rivelazione e allarme), UNI 11224 (verifica e manutenzione)."""))

S.append(("spegnimento",
"IMPIANTI DI SPEGNIMENTO",
"""Gli impianti di spegnimento sono la seconda barriera dopo la compartimentazione:

1. IDRANTI E MANICHETTE: rete di idranti a muro con lance e manichetta, alimentata da idrico pubblico o serbatoio; portata e pressione minime secondo rischio.

2. ESTINTORI: portatili (polvere, CO2, idrico) e carrellati; capacita' di estinzione minima in funzione del rischio; posizionamento visibile e accessibile.

3. SPRINKLER: impianto a pioggia con testine termosensibili attivate a 57-74 °C o a rivelazione elettronica; progettati per controllare l'incendio in un compartimento; richiedono riserva idrica dedicata e pompe.

4. A GAS: impianti a CO2, FM-200, Novec 1230 per ambienti elettrici e di pregio; richiedono compartimentazione a tenuta e procedure di evacuazione prima dello scarico.

5. PROGETTAZIONE: UNI EN 12845 (sprinkler), NFPA 13 (metodo alternativo), UNI 10779 (idranti). La scelta dipende dal rischio, dal valore dei beni, dalla disponibilita' idrica."""))

S.append(("gestione_emergenza",
"GESTIONE DELL'EMERGENZA E ADDETTI ANTINCENDIO",
"""L'organizzazione dell'emergenza e' l'elemento umano del sistema antincendio:

1. ADDETTI: per i luoghi di lavoro, il datore designa addetti antincendio e di primo soccorso in numero adeguato (tipicamente 1 ogni 50 lavoratori per rischio medio, piu' 1 ogni piano per rischio alto).

2. FORMAZIONE: corso antincendio (4 ore per rischio basso, 8 medio, 16 alto) con aggiornamento quinquennale; primo soccorso analogo.

3. PIANO DI EMERGENZA: documento che definisce le procedure (rilevazione, allarme, evacuazione, soccorso, comunicazione), i ruoli degli addetti, le vie di fuga, i punti di raccolta, i numeri utili.

4. PROVE DI EVACUAZIONE: obbligatorie almeno annuali (o semestrali per i rischi alti), con cronometraggio e analisi dei risultati.

5. CONTROLLI: la manutenzione degli impianti (rivelazione, spegnimento, porte REI) e' obbligatoria e documentata; i controlli VVF verificano la tenuta dei sistemi."""))

S.append(("materiali_fuoco",
"MATERIALI E FINITURE: REAZIONE E RESISTENZA AL FUOCO",
"""La scelta dei materiali influenza la sicurezza antincendio dell'edificio:

1. REAZIONE AL FUOCO: la capacita' del materiale di contribuire all'incendio (classi A1, A2, B, C, D, E, F con fumo s1-s3 e gocciolamento d0-d2). Materiale A1 (calcestruzzo, laterizio, acciaio) non contribuisce; legno massiccio trattato puo' essere B-s2,d0.

2. RESISTENZA AL FUOCO: la capacita' di mantenere le funzioni (REI) come descritto nella scheda dedicata. E' una proprieta' dell'elemento costruttivo (parete, solaio, porta), non del solo materiale.

3. FINITURE INTERNe: rivestimenti, pavimenti, tendaggi devono rispettare la classe di reazione al fuoco richiesta per la destinazione d'uso; le vernici intumescenti proteggono l'acciaio.

4. FACCIATE E COPERTURE: sistemi di facciata ventilata con barriere antincendio (cavity barriers) tra i piani; coperture con manti classificati; camini di fumo da evitare.

5. DOCUMENTAZIONE: certificati di classificazione dei materiali (rapporti di prova, ETA, DoP) vanno conservati nel fascicolo tecnico dell'edificio."""))

os.makedirs('parsed', exist_ok=True)
meta = {
    "source": "antincendio_kimi",
    "license": "Sintesi didattica originale Kimi (pubblico dominio)",
    "commercial_ok": True,
    "attribution": "Corpus antincendio a cura di Kimi",
    "url": "",
}
out = []
for i, (tema, titolo, testo) in enumerate(S, 1):
    rec = dict(meta)
    rec.update({"id": f"INC-{i:02d}", "tema": tema, "title": titolo, "text": testo.strip()})
    out.append(rec)

path = os.path.join('Edilizia_Pack', 'parsed', 'antincendio.jsonl')
os.makedirs(os.path.dirname(path), exist_ok=True)
with open(path, 'w', encoding='utf-8') as f:
    for r in out:
        f.write(json.dumps(r, ensure_ascii=False) + '\n')
print(f"scritte {len(out)} schede antincendio -> {os.path.abspath(path)}")
