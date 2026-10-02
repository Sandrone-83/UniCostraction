# -*- coding: utf-8 -*-
"""Aggiunge 3 schede Conto Termico 3.0 (errori di rigetto, calcolo incentivo,
multi-intervento/cumuli) da ENERGETICA_INCENTIVI e sincronizza la scheda 'accesso'
con la soglia 15.000 € già verificata sulle Regole Applicative GSE (Giro U)."""
import json, os, io, re

ROOT = os.path.dirname(os.path.abspath(__file__))

def s(cat, nome, desc, tec, app, van, lim, cos, casi, norm, note):
    return dict(categoria=cat, nome=nome, descrizione=desc, tecnologia=tec,
                applicazioni=app, vantaggi=van, limiti=lim, costi_e_economia=cos,
                casi_real_world=casi, normative=norm, note_cantiere=note)

NEW = [
s("Incentivi", "Conto Termico 3.0: gli errori che fanno rigettare o sospendere la pratica",
 "L'istruttoria GSE è severa sulle formalità: le istanze carenti dei requisiti di ammissione sono improcedibili, le integrazioni richieste sospendono i termini del procedimento (secondo la legge 241/1990) e il sopralluogo sospende il termine. Il rigetto più frequente non nasce da un vizio tecnico ma da documentazione assente, scaduta o difforme rispetto a quanto dichiarato.",
 "Errori tipici documentati: 1) istanza nel portale ma non inviata (stato 'Non inviata': il GSE non valuta); 2) APE post-intervento assente o che non dimostra il miglioramento richiesto; 3) fatture prive di riferimento all'intervento o di split tra opera e oneri non ammissibili; 4) prodotto non iscritto al catalogo GSE (o iscritto con classe diversa da quella dichiarata); 5) DURC irregolare o scaduto; 6) incongruenze tra prenotazione e contratto definitivo (l'acconto si calcola sul minore tra massimale prenotato e importo contrattualizzato: dichiarare un eccesso non porta più soldi, un difetto sì); 7) termine di conclusione lavori scaduto (12 mesi dall'avvio, 36 per nZEB); 8) documentazione difforme integrata in ritardo o mai.",
 "Professionisti e imprese che preparano pratiche Portaltermico, direzioni lavori di ristrutturazioni incentivabili, uffici tecnici comunali e PA.",
 "Conoscere l'elenco degli errori evita il 90% dei rigetti: la checklist pre-invio (stato pratica, APE, fatture, catalogo, DURC, termini) richiede mezz'ora e vale l'intero incentivo; le integrazioni tempestive dentro i termini salvano la pratica senza penali.",
 "L'istruttoria può chiedere integrazioni anche ad amministrazioni ed enti terzi (sospensione termini): i tempi si allungano oltre il previsibile; un rigetto in fase di saldo recupera solo la parte residua documentabile; la rinuncia va comunicata formalmente (funzione Portaltermico o PEC/raccomandata A/R con oggetto 'Conto Termico - nome SR - codice intervento - rinuncia agli incentivi').",
 "Costo degli errori: una pratica rigetta e ripresentata perde mesi di coda e rischio fondi a esaurimento; assistenza professionale per pratica completa: 500-2.000 € tipici (1-3% dell'incentivo per gli importi più alti).",
 "Impresa con pratica rigettata due volte: la prima per DURC scaduto, la seconda per fattura 'opere edili' generica senza riferimento ai componenti incentivati. La terza presentazione con fatture ricostruite e storni documentati passò dopo 5 mesi: lavori identici, esito opposto — la differenza era solo la documentazione.",
 "Regole Applicative D.M. 7/8/2025 (GSE): improcedibilità, integrazioni, sospensioni, sopralluogo, rinuncia; legge 241/1990 (procedimento amministrativo); D.M. 7/8/2025 (requisiti di ammissione).",
 "Regola d'oro: la pratica si prepara AL CONTRATTO, non alla fine dei lavori. Ogni fattura deve già nascere 'incentivabile': riferimento all'intervento, componenti iscritti al catalogo, importi separati tra ammissibile e non. Il GSE non corregge le fatture: rifiuta la pratica."),
s("Incentivi", "Conto Termico 3.0: massimali, costi ammissibili e calcolo dell'incentivo",
 "L'incentivo non è 'una percentuale della spesa': è una formula. Per le strutture opache: I_tot = %spesa × C × S_int, con I_tot ≤ I_max; se il costo specifico sostenuto C (€/m²) supera il valore massimo C_max di tabella 7 (Allegato 2 del Decreto), il calcolo avviene con C_max — spese oltre il massimale restano a carico del cliente. Per i generatori l'incentivo si calcola su tariffe di riferimento per kW (o m² per solare termico) con massimali per taglia.",
 "Elementi della formula: %spesa da tabella 7 (es. superfici opache 40% base, 50% zone E e F, 55% se combinata con altri interventi del Titolo III); C = spesa sostenuta / superficie intervento; C_max da tabella 7; S_int = superficie oggetto di intervento; I_max massimale per intervento. Acconto (via prenotazione): 2/5 di I_tot se durata 5 anni, 50% se 2 anni, calcolato sul minore tra massimale prenotato e importo contrattualizzato. Corrispettivo GSE: 1% di I_tot, massimale 250 € imponibile (+IVA), trattenuto sulla prima rata.",
 "Preventivazione di interventi incentivabili, verifica dell'congruità delle offerte rispetto ai massimali, simulazioni incentivo per il cliente prima della firma del contratto.",
 "La formula rende la trattativa professionale: si dimostra al cliente che spingere il prezzo oltre C_max non aumenta l'incentivo (riduce solo il proprio contributo); si dimensiona l'acconto per la cassa d'impresa; il corrispettivo GSE è noto a priori (1% con tetto 250 €).",
 "I valori C_max e I_max cambiano per tipologia e possono aggiornarsi: vanno verificati sulla tabella 7 vigente al momento della pratica; la spesa ammissibile esclude oneri non documentabili (chiarire in fattura); il calcolo con componenti UE (+10%) va attestato già in fase di richiesta e rendicontato a saldo.",
 "Ordini di grandezza indicativi: simulazione incentivo professionale 150-400 €; per un cappotto da 100 m² con C = 90 €/m² e %spesa 40%: I_tot = 3.600 € (unica rata, sotto i 15.000 €).",
 "Condominio con preventivo cappotto a 110 €/m² contro C_max di riferimento inferiore: la simulazione mostrò che l'incentivo si calcolava sul C_max, non su 110 €/m²: il ribasso del contratto a 98 €/m² lasciava l'incentivo identico e risparmiava 1.200 € ai condomini senza togliere un euro di contributo.",
 "Regole Applicative D.M. 7/8/2025 (GSE): formula incentivo, C_max, I_max, acconto 2/5 o 50%, corrispettivo 1% max 250 €; D.M. 7/8/2025 Allegato 2 tabella 7 (costi massimi unitari); tabella 1 art. 11 co. 3 (durate e rate).",
 "Per il LLM: mai dire al cliente 'incentivo del 40% sulla spesa' senza aver verificato C_max: la frase professionale è '40% della spesa entro il costo massimo ammissibile'. Il calcolo va fatto sui NUMERI del contratto, non sui numeri del preventivo."),
s("Incentivi", "Conto Termico 3.0: multi-intervento, cumuli e maggiorazioni",
 "Il Conto Termico 3.0 premia le riqualificazioni organiche: il multi-intervento somma gli incentivi dei singoli lavori, il numero delle rate è il massimo tra le durate dei singoli interventi (con distribuzione equa dell'incentivo totale), e sono previste maggiorazioni: +10% con componenti prodotti nell'Unione Europea (interventi art. 5 lett. a-f), con attestazione in fase di richiesta e rendicontazione a saldo per le pratiche a prenotazione; per il fotovoltaico esistono massimali dedicati con riferimento al registro delle tecnologie FV.",
 "Regole del multi-intervento: incentivo = somma degli incentivi dei singoli interventi; rate = valore massimo delle durate tabellari, equamente distribuite; per gli ETS economici con combinazione Titolo II (terziario) + Titolo III, l'erogazione oltre 15.000 € è multi-rata uniformata alla durata massima del Titolo II; PA e ETS non economici in accesso diretto possono avere unica rata anche oltre 15.000 €. Non cumulabilità: con le detrazioni fiscali statali sulle stesse spese; la scelta è definitiva per l'intervento.",
 "Impianti chiavi in mano su edifici interi (involucro + generatore + FV), ESCo che strutturano contratti di servizio energetico, PA con piani pluriennali di riqualificazione.",
 "Il multi-intervento semplice massimizza l'incentivo complessivo con una sola pratica; la maggiorazione UE vale fino al rispetto dei tetti di incentivazione; la pianificazione organica (tutto insieme) dà rate uniche più lunghe e flussi di cassa migliori per l'impresa.",
 "Ogni intervento del multi-intervento deve comunque rispettare requisiti e massimali propri (il più debole non trascina gli altri, ma una parte rigettata si perde); la scelta detrazione vs Conto Termico è irreversibile: valutarla con la capienza fiscale reale del cliente; la rendicontazione a saldo della maggiorazione UE richiede documentazione dei componenti conservata.",
 "Ordini di grandezza: pratica multi-intervento (3 interventi) simulata e gestita: 800-2.500 € di assistenza tecnica; incentivo complessivo esempio: involucro 3.600 € + PdC 6.500 € + FV 3.000 € = 13.100 € (unica rata se ≤ 15.000 €, altrimenti rate annuali).",
 "Villetta con involucro + pompa di calore + fotovoltaico presentati come unica pratica multi-intervento: incentivo totale sotto i 15.000 €, erogato in unica rata a saldo; il preventivo del cliente separava già le voci ammissibili: la rendicontazione è durata 40 giorni senza integrazioni.",
 "Regole Applicative D.M. 7/8/2025 (GSE): multi-intervento, maggiorazione 10% componenti UE, unica rata PA/ETS, non cumulabilità; D.M. 7/8/2025 art. 11 (rate e soglie); D.Lgs 28/2011 (quadro incentivi energetici).",
 "Per il LLM: la prima domanda professionale è 'facciamo un unico intervento o più interventi?' — la risposta cambia incentivo, rate e pratica. E prima di consigliare 'meglio il Conto Termico' o 'meglio la detrazione' servono capienza fiscale, tempi di cassa e natura del cliente (privato, impresa, PA)."),
]

path = os.path.join(ROOT, "schede", "schede.jsonl")
schede = [json.loads(l) for l in io.open(path, encoding="utf-8") if l.strip()]
nomi = {x["nome"] for x in schede}
out = []
for d in schede:
    if d["nome"] == "Conto Termico 3.0: accesso diretto, prenotazione, pratica":
        d["tecnologia"] = d["tecnologia"].replace(
            "soglia 5.000-15.000 € da verificare sulle Regole Applicative GSE vigenti",
            "unica rata per incentivi ≤ 15.000 € (Regole Applicative GSE D.M. 7/8/2025 art. 11 co. 4: i 5.000 € citati da alcune fonti appartengono al Conto Termico 2.0)")
        d["note_cantiere"] = d["note_cantiere"].replace("PRIERA", "PRIMA")
    out.append(json.dumps(d, ensure_ascii=False))
add = [d for d in NEW if d["nome"] not in nomi]
for d in add:
    out.append(json.dumps(d, ensure_ascii=False))
io.open(path, "w", encoding="utf-8").write("\n".join(out) + "\n")
n = len(schede) + len(add)
y = io.open(os.path.join(ROOT, "COURSE.yaml"), encoding="utf-8").read()
io.open(os.path.join(ROOT, "COURSE.yaml"), "w", encoding="utf-8").write(
    re.sub(r"schede: \d+", f"schede: {n}", y))
print("aggiunte:", len(add), "| totale:", n)
