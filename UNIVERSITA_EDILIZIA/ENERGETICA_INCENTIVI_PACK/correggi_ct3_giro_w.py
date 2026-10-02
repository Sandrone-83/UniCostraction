# Giro W — Correzioni Conto Termico 3.0 su fonte primaria GSE (Regole Applicative D.M. 7/8/2025,
# PDF gse.it Regole_Applicative_CT_3_0.pdf, riletto integralmente il 02/10/2026) + D.D. MASE 72/2026.
# Ogni modifica rispetta la regola prima->dopo->fonte del changelog.
import json, io, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(ROOT, "ENERGETICA_INCENTIVI_PACK", "schede", "schede.jsonl")

schede = []
with io.open(PATH, encoding="utf-8") as f:
    for line in f:
        if line.strip():
            schede.append(json.loads(line))

def get(nome):
    for s in schede:
        if s["nome"] == nome:
            return s
    raise KeyError(nome)

# ---------------------------------------------------------------- W1: scheda 1 «la misura e i numeri»
s1 = get("Il Conto Termico 3.0: la misura e i numeri (verificati ottobre 2026)")

# PRIMA: dotazione «900 mln €/anno (500 mln privati di cui 150 mln imprese con tetto di 30 mln a impresa; 400 mln PA)»
# DOPO: + rimodulazione 2026 D.D. 72 (verificata su 5 fonti di settore indipendenti) + 20 mln diagnosi PA
s1["tecnologia"] = (
    "Dati verificati (ottobre 2026): 1) norma: D.M. 7 agosto 2025 (G.U. n. 224 del 26/9/2025), gestione GSE; "
    "2) beneficiari: pubbliche amministrazioni, privati, imprese, enti del terzo settore, CER, ESCo certificate; "
    "3) dotazione: 900 mln €/anno — per legge 400 mln per PA e ETS non economici (di cui 20 mln per diagnosi energetiche) "
    "e 500 mln per privati, imprese e ETS economici (con limite 150 mln €/anno per le imprese e tetto di 30 mln € per "
    "singola impresa e intervento, art. 28); con Decreto direttoriale MASE n. 72 del 10 aprile 2026 la ripartizione 2026 è "
    "stata rimodulata a 450 mln PA / 450 mln privati (rimodulazione annua possibile: verificare sempre i limiti vigenti sul sito GSE); "
    "4) coperture: fino al 65% del costo ammissibile per privati, ETS e imprese (per le imprese l'intensità segue le regole "
    "degli aiuti di Stato del Titolo V: interventi Titolo III con intensità base 45% fino a 65/55/45% per piccola/media/grande "
    "impresa; interventi Titolo II 25% singolo o 30% multi-intervento fino a 65/65/60%); fino al 100% per scuole, strutture "
    "sanitarie e immobili dei comuni sotto i 15.000 abitanti; 5) erogazione: unica rata se l'incentivo totale è ≤ 15.000 € "
    "(Regole Applicative GSE, art. 11 co. 4: la soglia di 5.000 € citata da alcune fonti si riferisce al precedente "
    "Conto Termico 2.0, D.M. 16/2/2016), altrimenti rate annuali costanti (2 o 5 anni secondo tabella 1 del decreto); "
    "rata di acconto alla comunicazione di avvio lavori pari a 2/5 dell'incentivo se durata 5 anni, 50% se durata 2 anni; "
    "conclusione lavori entro 12 mesi dall'avvio per le fattispecie i-iv (36 mesi per gli interventi nZEB; fattispecie a: "
    "avvio entro 18 mesi dall'accettazione della prenotazione e conclusione entro i successivi 48 mesi); corrispettivo GSE "
    "per le attività istruttorie pari all'1% dell'incentivo, massimale 250 € imponibile; maggiorazione +10% con componenti "
    "prodotti nell'Unione Europea (art. 5, lett. a-f); 6) impegni: impianti in esercizio almeno 5 anni; 7) storia operativa: "
    "portale aperto il 2 febbraio 2026, sospeso il 3 marzo 2026 (oltre 2.200 domande per ~1,3 mld € contro 900 mln disponibili), "
    "riaperto il 13 aprile 2026 con sola modalità accesso diretto (prenotazioni PA sospese) e proroga di 40 giorni per le "
    "istanze bloccate; le risorse sono annuali e a esaurimento: verificare sempre la disponibilità sul sito GSE prima di "
    "promettere il contributo al cliente."
)

# PRIMA: «incentivo stimato 65% sul termico e 20% sul FV (maximale ~1.500 €/kW decrescente con la taglia); pratica in accesso
# diretto entro 90 giorni dalla fine lavori, prima rata dopo istruttoria GSE (60 giorni di valutazione)»
# DOPO: termico su producibilità (NON 65% di spesa); erogazione per bimestre; 90 giorni confermato
s1["casi_real_world"] = (
    "Impresa metalmeccanica: pompa di calore da 40 kW + fotovoltaico trainato da 30 kWp: l'incentivo termico si calcola "
    "sulla producibilità (energia termica prodotta × coefficiente €/kWh, con premialità di efficienza), NON come percentuale "
    "della spesa; il fotovoltaico trainato è al 20% con costo massimo 1.500 €/kW (fino a 20 kW) e tetto pari all'incentivo "
    "della pompa di calore; pratica in accesso diretto entro 90 giorni dalla fine lavori, poi erogazione entro l'ultimo "
    "giorno del mese successivo al bimestre di perfezionamento della scheda-contratto."
)

# PRIMA: «D.Lgs 28/2011 (esenzione IRPEF del contributo per le persone fisiche, art. 11)» — NORMA VERA FUORI POSTO:
# l'art. 11 D.Lgs 28/2011 disciplina la certificazione energetica. Il documento GSE supporta direttamente: fuori campo IVA,
# niente ritenuta art. 28 D.P.R. 600/73.
s1["normative"] = (
    "D.M. 7 agosto 2025 (Conto Termico 3.0); GSE — Regole Applicative del D.M. 7/8/2025 (erogazione, soglia 15.000 €, "
    "acconto 2/5, corrispettivo 1% max 250 €, tassazione: contributo fuori campo IVA e fuori dall'art. 28 D.P.R. 600/1973, "
    "cioè senza ritenuta del 4%); GSE — regole tecniche e catalogo apparecchi (aggiornato dal 15 aprile 2026); D.D. MASE "
    "n. 72 del 10/4/2026 (rimodulazione limiti di spesa 2026: 450 mln PA / 450 mln privati). Per la tassazione IRPEF/IRES "
    "completa (privati esclusi da imposizione; imprese in conto impianti) rimandare alla prassi Agenzia delle Entrate e al "
    "commercialista — NON citare D.Lgs 28/2011 che non tratta la materia."
)

# ---------------------------------------------------------------- W2: scheda 2 «interventi ammessi e percentuali» (RISCrittURA)
s2 = get("Conto Termico 3.0: interventi ammessi e percentuali")

s2["descrizione"] = (
    "Il Conto Termico 3.0 incentiva interventi su inviluppo e impianti con DUE famiglie di algoritmi: l'involucro (Titolo II) "
    "è a percentuale della spesa entro costi massimi unitari (Itot = %spesa × C × S ≤ Imax); i generatori a rinnovabili "
    "termiche (Titolo III: pompe di calore, solare termico, biomassa, ibridi, scaldaacqua a PdC) sono incentivati sulla "
    "producibilità, cioè sull'energia termica prodotta (€/kWh), non sulla spesa. Fotovoltaico e accumulo (intervento II.H) "
    "rientrano solo 'trainati' dalla pompa di calore elettrica, al 20% della spesa entro costi massimi per taglia."
)
s2["tecnologia"] = (
    "DUE ALGORITMI VERIFICATI sulle Regole Applicative GSE (ottobre 2026). A) INVOLUCRO — percentuale della spesa: "
    "1) isolamento superfici opache (II.A): 40% base, 50% nelle zone climatiche E e F, 55% se combinato con almeno un "
    "intervento III.A/III.B/III.C/III.E, 100% sugli edifici pubblici di cui all'art. 11 co. 2; costi massimi Cmax: copertura "
    "esterno 300 €/m² (interno 150, ventilata 350), pavimenti 170/150, pareti esterno 200 (interno 100, ventilata 250); "
    "massimale complessivo (coperture+pavimenti+pareti) 1.000.000 €; 2) sostituzione serramenti (II.B): 40%, Cmax 700 €/m² "
    "zone A-B-C e 800 €/m² zone D-E-F, Imax 500.000 €; 3) schermature solari (II.C): 40%; 4) trasformazione in nZEB (II.D): "
    "65% con formula Itot = %spesa × C × Sed; 5) illuminazione efficiente (II.E) e building automation (II.F) ammesse; "
    "6) colonnine ricarica (II.G) e fotovoltaico (II.H): solo congiuntamente alla sostituzione del generatore con pompa di "
    "calore elettrica. B) GENERATORI — producibilità (incentivo annuo = energia termica prodotta × coefficiente €/kWh): "
    "1) pompe di calore elettriche (III.A): Ia = Ei × Ci, con Ei = Qu × [1 - 1/SCOP] × kp; Qu = potenza nominale × coefficiente "
    "di utilizzo della zona climatica; kp = premialità efficienza (ηs/ηs minimo ecodesign); requisito di accesso: SCOP almeno "
    "pari al minimo ecodesign della tipologia (UNI EN 14825, tabelle 3-4 Allegato 1); 2 annualità se ≤ 35 kW, 5 oltre; "
    "impianti ammessi fino a 2.000 kWt; oltre 200 kW contabilizzazione del calore obbligatoria; 2) sistemi ibridi (III.B): "
    "ibrido factory made o bivalente (pompa di calore + caldaia a condensazione a gas oppure a biomassa), oppure pompa di "
    "calore add-on su caldaia a condensazione a gas preesistente, sempre con regolazione intelligente; 3) biomassa (III.C): "
    "caldaie fino a 500 kWt e 500-2.000 kWt, stufe e termocamini a pellet, termocamini e stufe a legna; classe ambientale "
    "5 stelle o superiore (nella sostituzione di generatori a GPL/gas: anche emissioni di particolato ≤ 1 mg/Nm³); impianti "
    "di teleriscaldamento con incentivo ridotto del 20%; 4) solare termico (III.D): Ia = Ci × Qu × Sl (superficie lorda), "
    "coefficienti Ci da 0,35 €/kWh per a.c.s. sotto i 12 m² a 0,11 €/kWh oltre 500 m² (solar cooling fino a 0,43); "
    "certificazione Solar Keymark obbligatoria; 2 annualità se ≤ 50 m², 5 oltre; 5) scaldaacqua a pompa di calore (III.E) "
    "in sostituzione di scaldacqua elettrici e a gas. C) FOTOVOLTAICO TRAINATO (II.H): 20% della spesa, in autoconsumo "
    "(cessione del surplus), potenza 2 kW - 1 MW, produzione non superiore al fabbisogno energetico dell'edificio +5%; "
    "costi massimi: 1.500 €/kW fino a 20 kW, 1.200 €/kW fino a 200 kW, 1.100 €/kW fino a 600 kW, 1.050 €/kW fino a 1.000 kW; "
    "accumulo con costo massimo 1.000 €/kWh; incentivo FV+accumulo mai superiore all'incentivo della pompa di calore. "
    "D) REGOLE PER IMPRESE E ETS ECONOMICI (Titolo V, aiuti di Stato): esclusi gli apparecchi alimentati a combustibili "
    "fossili — niente pompe di calore a gas né ibridi con caldaia a gas (art. 25 co. 2); intensità massime: Titolo III "
    "base 45% (+20% piccole, +10% medie) → 65/55/45%; Titolo II 25% singolo / 30% multi-intervento (+20/10 dimensione, "
    "+15/+5 zone assistite TFEU 107.3.a/c, +15 se miglioramento prestazione energetica ≥ 40%) → 65/65/60%; tetto 150 mln "
    "€/anno per le imprese. E) MAGGIORAZIONI: +10% con componenti prodotti nell'Unione Europea per gli interventi "
    "art. 5 lett. a-f (attestazione già nella richiesta; rendicontata a saldo per le pratiche a prenotazione); +5, +10 o "
    "+15 punti percentuali con moduli fotovoltaici iscritti al Registro delle tecnologie per il fotovoltaico (art. 12 "
    "D.L. 181/2023, sezioni a/b/c per requisiti territoriali e tecnici — DEVONO appartenere tutti alla stessa sezione)."
)
s2["applicazioni"] = (
    "Riqualificazione termica di edifici residenziali (generatori Titolo III), aziende (terziario: involucro + generatori + "
    "FV trainato, con intensità aiuti di Stato per dimensione d'impresa), scuole e comuni (fino al 100%)."
)
s2["vantaggi"] = (
    "La logica 'trainata' del fotovoltaico allinea l'incentivo alla decarbonizzazione del calore: il progetto integrato "
    "PdC+FV+accumulo è il target della misura; per i generatori la premialità kp premia chi sceglie macchine più efficenti "
    "del minimo ecodesign."
)
s2["limiti"] = (
    "Il fotovoltaico da solo NON entra: serve sempre la sostituzione del generatore termico con pompa di calore elettrica; "
    "per imprese ed ETS economici sono escluse le apparecchiature a combustibili fossili; i generatori non sono a "
    "percentuale di spesa: sotto-i-centivare o sovrastimare l'incentivo 'a occhio' è l'errore classico — va simulato "
    "l'algoritmo di producibilità; la Solar Keymark e l'iscrizione al catalogo GSE sono requisiti d'accesso, non formalità."
)
s2["costi_e_economia"] = (
    "Esempio verificato sui valori di tabella 7 (Allegato 2): serramenti 20 m² in zona C a 350 €/m² di spesa sostenuta "
    "(sotto il Cmax di 700 €/m²): incentivo = 40% × 350 × 20 = 2.800 €, erogato in unica rata (sotto i 15.000 €). "
    "Esempio involucro: cappotto 100 m² a 90 €/m² (Cmax pareti esterno 200 €/m² non raggiunto): 40% × 90 × 100 = 3.600 €. "
    "Per pompe di calore, solare termico e biomassa non esiste una percentuale di spesa: l'incentivo va simulato sul "
    "Portaltermico con i coefficienti ufficiali (tabelle 9, 10, 16 dell'Allegato 2) — diffidare delle 'percentuali tipo' "
    "di fonti non ufficiali."
)
s2["casi_real_world"] = (
    "Azienda alberghiera: sostituzione caldaia a gas con PdC elettrica 50 kW (incentivo su producibilità, 5 annualità, "
    "premialità kp per lo SCOP sopra il minimo ecodesign) + FV trainato 20 kW (20% con Cmax 1.500 €/kW → al massimo 6.000 €) "
    "+ accumulo 10 kWh (20% con Cmax 1.000 €/kWh → 2.000 €): il tetto FV+accumulo è l'incentivo PdC. La stessa azienda con "
    "solo fotovoltaico, senza pompa di calore, avrebbe avuto zero."
)
s2["normative"] = (
    "D.M. 7/8/2025 e Allegato 1 (requisiti tecnici, tabelle 2-4: trasmittanze, SCOP ecodesign) e Allegato 2 (algoritmi: "
    "tabella 7 costi massimi involucro, tabelle 9/10/16 coefficienti €/kWh generatori); Regole Applicative GSE "
    "(paragrafi 4.2.1 intensità imprese, 9.x algoritmi per intervento, Allegato 4 maggiorazione componenti UE); catalogo "
    "apparecchi GSE (iscritti = requisito); D.L. 181/2023 art. 12 (Registro delle tecnologie per il fotovoltaico); DM 37/08 "
    "per la conformità impiantistica."
)
s2["note_cantiere"] = (
    "Il catalogo GSE e la certificazione del prodotto decidono: prima di quotare, verificare che il modello specifico sia "
    "iscritto al catalogo (generatori) e che il collettore abbia la Solar Keymark (solare termico). Il modello non iscritto "
    "o senza certificazione = incentivo azzerato. Per le pompe di calore chiedere al fornitore lo SCOP in zona 'average' "
    "e confrontarlo con il minimo ecodesign: kp = ηs/ηs,min determina la premialità."
)

# ---------------------------------------------------------------- W3: scheda «errori» — termini conclusione + regola 120 giorni
s3 = get("Conto Termico 3.0: gli errori che fanno rigettare o sospendere la pratica")
s3["tecnologia"] = (
    "Errori tipici documentati: 1) istanza nel portale ma non inviata (stato 'Non inviata': il GSE non valuta); 2) APE "
    "post-intervento assente o che non dimostra il miglioramento richiesto; 3) fatture prive di riferimento all'intervento "
    "o di split tra opera e oneri non ammissibili; 4) prodotto non iscritto al catalogo GSE (o iscritto con classe diversa "
    "da quella dichiarata); 5) DURC irregolare o scaduto; 6) incongruenze tra prenotazione e contratto definitivo (l'acconto "
    "si calcola sul minore tra massimale prenotato e importo contrattualizzato: dichiarare un eccesso non porta più soldi, "
    "un difetto sì); 7) termine di conclusione lavori scaduto — fattispecie i-iv: conclusione entro 12 mesi dalla "
    "documentazione di avvio (36 mesi per nZEB); fattispecie a: avvio lavori entro 18 mesi dall'accettazione della "
    "prenotazione e conclusione entro i successivi 48 mesi; 8) 'data di effettuazione dell'ultimo pagamento' oltre 120 "
    "giorni prima della data di conclusione dichiarata (la conclusione non può superare i 120 giorni dall'ultimo "
    "pagamento); 9) documentazione difforme integrata in ritardo o mai."
)
s3["normative"] = (
    "Regole Applicative D.M. 7/8/2025 (GSE): improcedibilità, integrazioni, sospensioni, sopralluogo, rinuncia, data "
    "conclusione e regola dei 120 giorni (paragrafi 12.1 e 7.x); legge 241/1990 (procedimento amministrativo); D.M. 7/8/2025 "
    "(requisiti di ammissione)."
)

# ---------------------------------------------------------------- W4: scheda «massimali» — formula generatori
s4 = get("Conto Termico 3.0: massimali, costi ammissibili e calcolo dell'incentivo")
s4["descrizione"] = (
    "L'incentivo non è 'una percentuale della spesa': sono due famiglie di formule. Per l'involucro (Titolo II): "
    "I_tot = %spesa × C × S_int, con I_tot ≤ I_max; se il costo specifico sostenuto C (€/m²) supera il valore massimo C_max "
    "di tabella 7 (Allegato 2 del Decreto), il calcolo avviene con C_max — spese oltre il massimale restano a carico del "
    "cliente. Per i generatori a rinnovabili termiche (Titolo III: pompe di calore, solare termico, biomassa, ibridi, "
    "scaldaacqua a PdC) l'incentivo annuo si calcola invece sulla producibilità: energia termica prodotta stimata "
    "× coefficiente in €/kWh (tabelle 9, 10 e 16 dell'Allegato 2), con premialità per l'efficienza — non esiste una "
    "tariffa per kW installato né per m² di collettore."
)
s4["normative"] = (
    "Regole Applicative D.M. 7/8/2025 (GSE): formula incentivo involucro, C_max, I_max, acconto 2/5 o 50%, corrispettivo "
    "1% max 250 €, algoritmi di producibilità Titolo III (paragrafi 9.9, 9.12 e seguenti); D.M. 7/8/2025 Allegato 2 "
    "(tabella 7 costi massimi unitari; tabelle 9, 10, 16 coefficienti €/kWh); tabella 1 art. 11 co. 3 (durate e rate)."
)

# ---------------------------------------------------------------- W5: scheda «multi-intervento» — registro FV corretto
s5 = get("Conto Termico 3.0: multi-intervento, cumuli e maggiorazioni")
s5["descrizione"] = (
    "Il Conto Termico 3.0 premia le riqualificazioni organiche: il multi-intervento somma gli incentivi dei singoli lavori, "
    "il numero delle rate è il massimo tra le durate dei singoli interventi (con distribuzione equa dell'incentivo totale), "
    "e sono previste maggiorazioni: +10% con componenti prodotti nell'Unione Europea (interventi art. 5 lett. a-f), con "
    "attestazione in fase di richiesta e rendicontazione a saldo per le pratiche a prenotazione; per il fotovoltaico "
    "+5/10/15 punti percentuali con moduli iscritti al Registro delle tecnologie per il fotovoltaico (art. 12 D.L. 181/2023, "
    "sezioni a/b/c: requisiti territoriali e tecnici — tutti i moduli della stessa sezione)."
)

# ---------------------------------------------------------------- salvataggio
with io.open(PATH, "w", encoding="utf-8") as f:
    for s in schede:
        f.write(json.dumps(s, ensure_ascii=False) + "\n")
print("schede aggiornate: 5 | totale:", len(schede))
