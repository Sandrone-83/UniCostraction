# -*- coding: utf-8 -*-
"""Tecnica specialistica d'elite per l'Edilizia_Pack."""
import json, os

S = []

S.append(("facciate","facciate_ventilate_bipv",
"FACCIATE VENTILATE, CONTINUE E BIPV",
"""Le facciate moderne sono sistemi tecnologici complessi:

1. FACCIATA VENTILATA: strato esterno (lastre in gres, metallo, pietra, HPL) ancorato a sottostruttura metallica, con camera d'aria ventilata (minimo 2 cm, tipicamente 8-20 cm), strato isolante sul massetto (o esterno), parete di fondo. Funzione: drenaggio e deflusso dell'acqua, ventilazione che asciuga l'umidita', riduzione ponti termici, manutenibilita'.

2. ANCORAGGI: sistemi a vista (fissaggi meccanici a tassello o gancio) o a fissaggi nascosti (profili orizzontali/verticali); verifiche sismiche, resistenza al vento (curve di pressione), dilatazioni termiche dei pannelli.

3. FACCIATA CONTINUA (curtain wall): montanti e traversi metallici con vetro strutturale o infissi; tipologie: stick system (montato in opera), unitized (moduli prefabbricati), semi-unitized, structural glazing (vetro adesivo), point fixed (fissaggi puntiformi a ragno).

4. BIPV (Building Integrated Photovoltaics): moduli fotovoltaici che sostituiscono il rivestimento (lastre, vetri fumè con celle, tegole solari); resa 100-180 W/m², integrazione estetica, vantaggi per permessi in centri storici.

5. REQUISITI: reazione al fuoco (classe dei pannelli e del sistema), resistenza al vento (prova in galleria), permeabilita' all'aria, tenuta all'acqua, impatto (per vetri), isolamento acustico, manutenzione." """))
S.append(("fisica_edilizia","condensa_glaser",
"CONDENSA INTERSTIZIALE E METODO DI GLASER",
"""Il metodo di Glaser valuta il rischio di condensa nei componenti opachi:

1. PRINCIPIO: per ogni strato si calcola la temperatura e la pressione di vapore saturo; se la pressione di vapore reale supera quella di saturazione in un punto, si forma condensa. La verifica si fa per il periodo invernale (esterno freddo-umido, interno caldo-umido).

2. PROCEDIMENTO: calcolo delle temperature di interfaccia (con flusso stazionario), calcolo delle pressioni di vapore (con permeabilita' ai vapori dei materiali), confronto con saturazione; eventuale calcolo dello spessore di condensa e del tempo di evaporazione estiva.

3. CRITICITA' TIPICHE: strati impermeabili al vapore sul lato caldo (es. membrane posate male), isolamento interno senza barriera adeguata, ponti di vapore (giunti, fissaggi), murature spesse con intonaco impermeabile.

4. SOLUZIONI: barriera al vapore sul lato caldo (posizione corretta, giunzioni sigillate), materiali traspiranti verso l'esterno, stratigrafie con resistenza al vapore decrescente da interno verso esterno, ventilazione della camera d'aria.

5. NORME: UNI EN ISO 13788 (metodo di Glaser), EN 15026 (simulazione dinamica), software WUFI per l'igrotermia dinamica (considera la capacita' di accumulo dell'umidita')."""))
S.append(("fisica_edilizia","simulazione_energetica",
"SIMULAZIONE ENERGETICA DINAMICA E COMFORT ESTIVO",
"""La simulazione dinamica supera il calcolo statico per il progetto energetico:

1. MOTIVAZIONE: il bilancio statico (gradi giorno) non coglie l'inerzia termica, i guadagni solari variabili, le condizioni estive; la simulazione oraria (8760 ore) riproduce il comportamento reale.

2. STRUMENTI: EnergyPlus, DesignBuilder, IES VE, TRNSYS, IDA ICE; input: geometria, stratigrafie, impianti, occupazione, meteo (file EPW per la localita').

3. OUTPUT: fabbisogni mensili e orari di riscaldamento/raffrescamento/ACS/luce, temperature operative, gradi di ore di discomfort (PMV, PPD), consumi elettrici, produzione FER, autoconsumo.

4. COMFORT ESTIVO: valutazione con PMV (Predicted Mean Vote) e PPD (Predicted Percentage of Dissatisfied) secondo UNI EN ISO 7730; strategie passive: schermature, ventilazione notturna, inerzia termica, deumidificazione.

5. CERTIFICAZIONE: simulazione dinamica richiesta per le certificazioni avanzate (LEED, BREEAM) e per il progetto NZEB complesso; calibrazione su consumi reali (retrofitting)."""))
S.append(("geotecnica","consolidamenti",
"CONSOLIDAMENTO DEI TERRENI: MICROPALI, JET GROUTING, INIEZIONI",
"""Il miglioramento del terreno permette fondazioni e scavi impossibili altrimenti:

1. MICROPALI: pali di piccolo diametro (76-300 mm) in acciaio con iniezione di calcestruzzo, capacita' di carico 300-1.500 kN, usati per rinforzo di fondazioni esistenti, sotto soletta, in spazi ridotti, per contrastare cedimenti.

2. JET GROUTING: iniezione di cemento ad altissima pressione (200-600 bar) che frantuma e mescola il terreno creando colonne (diametro 0,6-2,5 m) o pali di terreno migliorato; usato per sotto-soli, impermeabilizzazioni, rinforzi.

3. INIEZIONI: riempimento di fessure e cavita' con calcestruzzo, resine, sospensioni; classificazione per pressione e viscosita' (compensation grouting per sollevare strutture).

4. MURI DI SOSTEGNO: muri in cemento armato (gravity, cantilever, a contrafforti), paratie (palancole in acciaio o cemento, diaframmi in c.a.), ancoraggi attivi o passivi, tiranti; verifiche di stabilita' (ribaltamento, scorrimento, portanza, spinta).

5. SCAVI PROFONDI: tecnica del top-down (soletta di copertura prima dello scavo), auto-sollevamento (strutture di fondazione che usano l'attrito del terreno), monitoring (inclinometri, estensimetri, piezometri) per edifici vicini."""))
S.append(("materiali","calcestruzzi_speciali",
"CALCESTRUZZI SPECIALI: AUTO-COMPATTANTE, UHPC, FIBRE, BIO-BASED",
"""I calcestruzzi moderni coprono prestazioni specifiche:

1. SCC (Self-Compacting Concrete): autolivellante grazie ad additivi superfluidificanti e granulometria controllata; riempie casseforme complesse senza vibrazione; usato per elementi armati densi, getti difficili, finiture lisce.

2. UHPC (Ultra High Performance Concrete): resistenza >150 MPa con aggregati fini, silice fumante, fibre metalliche (2-5%); duttile, resistente agli agenti aggressivi; usato per ponti, elementi sottili, riparazioni strutturali; costo elevato (500-1.000 €/m³).

3. FRC (Fibre Reinforced Concrete): fibre in acciaio, vetro, polipropilene, basaltiche (0,5-2% in volume) che controllano fessurazione e ritiro; calcestruzzo da getto con fibre per solai, pavimentazioni, tunnel.

4. CALCESTRUZZI SPECIALI FUNZIONALI: alleggeriti strutturali, massicci (barite per radiazioni), colorati, stampati, permeabili (drainage), termoisolanti (argilla espansa), fotocatalitici (NOx), conduttivi.

5. BIO-BASED: legno-cemento, canapa-calce, paglia, sughero; isolanti naturali, basso carbonio embodied, regolazione igrometrica; verifiche tecniche (reazione fuoco, durabilita')."""))
S.append(("sostenibilita","certificazioni_green",
"LEED, BREEAM, ITACA E LCA: LE CERTIFICAZIONI DI SOSTENIBILITA'",
"""Le certificazioni misurano la sostenibilita' dell'edilizia:

1. LEED (USGBC, USA): crediti in categorie (siti, acqua, energia, materiali, qualita' ambientale interna, innovazione); livelli Certified/Silver/Gold/Platinum (40-80+ punti); adattato per l'Italia con crediti regionali.

2. BREEAM (BRE, UK): manuale New Construction, In-Use, Refurbishment; rating da Pass a Outstanding; molto diffuso in Europa, adattato con schemi nazionali.

3. ITACA (Protocollo Nazionale CasaClima in Italia, aderente a SBTool): indicatori di sostenibilita' ambientale, sociale, economica, istituzionale; fasi di progettazione, costruzione, gestione; richiesto da bandi pubblici.

4. LCA (Life Cycle Assessment): analisi del ciclo di vita secondo UNI EN ISO 14040/44; quantifica l'impatto ambientale (GWP, acidificazione, eutrofizzazione, consumo risorse) dalla produzione dei materiali alla demolizione; EPD (Environmental Product Declaration) per i prodotti; carbon footprint embodied vs operational.

5. NZEB E GREEN BUILDING: integrazione con la direttiva EPBD, Nearly Zero Energy Building, e crescente attenzione al carbonio incorporato (embodied carbon), alla circolarita' (DPP - Digital Product Passport), al benessere occupanti (WELL Building Standard)."""))
S.append(("antisismica","microzonazione_sito",
"MICROZIONAZIONE SISMICA E CONDIZIONI DI SITO",
"""La risposta sismica dipende dal terreno oltre che dalla sorgente:

1. PERICOLOSITA' SISMICA (PSHA): probabilita' di superamento di un livello di scuotimento in un tempo di riferimento; parametri ag, F0, Tc* per le quattro zone sismiche italiane (ag da 0,05 a 0,35+ g); ritorno 475 anni (10% in 50 anni) per lo stato limite di salvaguardia della vita.

2. MICROZIONAZIONE (LC e MS): livello 1 (identificazione zone omogenee per amplificazione e instabilita'), livello 2 (studio locale di amplificazione, instabilita' di pendio, liquefazione, faglie attive); obbligo di considerazione in provincia (DGR e ordinanze) e nei comuni.

3. AMPLIFICAZIONE DI SITO: depositi di terreno soffici amplificano le onde sismiche (effetto di sito, Vs30, categorie A-E); pendii con instabilita' (frane) e basin effects.

4. RISPOSTA LOCALE: analisi 1D/2D della colonna di terreno (EERA, DEEPSOIL), analisi non lineare per terreni deboli.

5. CONSEGUENZE PROGETTUALI: spettro di risposta di sito (SS) se amplificazione significativa; condizioni topografiche (categorie T1-T4 per pendii); vincoli di fondazione in presenza di liquefazione (D.M. 17/01/2018, allegato); rinforzo del terreno (stone columns, drainage, solidificazione)."""))
S.append(("antisismica","dissipatori",
"DISPOSITIVI DI DISSIPAZIONE E PROGETTAZIONE DISSIPATIVA",
"""La progettazione dissipativa concentra il danno in elementi sostituibili:

1. CRITERIO DI PROGETTAZIONE: struttura a comportamento fattore-q ( dissipativa: dissipazione nel SLD); gli elementi dissipativi sono progettati per snervarsi (duttilita'), gli altri restano elastici (capacita' progettuale).

2. DISPOSITIVI DISSIPATIVI: dissipatori a taglio (ADAS, TADAS), a flessione (added damping and stiffness devices), viscosi (fluidi ad alta viscosita'), a frizione (pall friction dampers), viscoelastici; posizionati in diagonali, tra piani, su isolatori.

3. SMORZAMENTO EQUIVALENTE: i dissipatori aumentano lo smorzamento (5% elastico -> 15-30% dissipativo), riducendo le forze sismiche sulla struttura; verifica con spettro ridotto per smorzamento.

4. ANALISI: modellazione non lineare degli elementi dissipativi (link elements, hysteretic rules), time-history per verifiche, prove sperimentali sui dispositivi (qualifica).

5. APPLICAZIONI: edifici nuovi in zone sismiche (edifici base-isolated + dissipatori), retrofit di edifici esistenti, ponti (cuscinetti con dissipatori)."""))
S.append(("incendio","ingegneria_fse",
"INGEGNERIA ANTINCENDIO AVANZATA: FSE, CFD ED EVACUAZIONE",
"""L'ingegneria della sicurezza incendio usa strumenti avanzati:

1. FSE (Fire Safety Engineering): progettazione basata su analisi prestazionale invece che su prescrizioni; analisi del rischio (scenario, probabilita', conseguenza), obiettivi di sicurezza, strategie (prevenzione, protezione, gestione emergenza); conformita' tramite codici (approccio prescrizionale), prove sperimentali, o valutazione ingegneristica.

2. SIMULAZIONE CFD: modellazione della propagazione di fumo e calore (FDS - Fire Dynamics Simulator, PyroSim); input: scenario di incendio (curva di rilascio termico HRR), geometria, ventilazione; output: temperature, visibilita', concentrazione CO, tempo disponibile per l'evacuazione (ASET).

3. EVACUAZIONE: simulazione del movimento degli occupanti (Pathfinder, STEPS, Exodus, FDS+Evac); modelli: veloci (flusso attraverso uscite), agent-based (comportamento individuale); output: RSET (Required Safe Egress Time) confrontato con ASET (margin of safety).

4. STRUTTURE: analisi termo-meccanica degli elementi esposti al fuoco (ANSYS, SAFIR), verifica della resistenza R in condizioni d'incendio (carichi accidentali, temperatura).

5. APPLICAZIONI: centri commerciali complessi, stadi, tunnel, grattacieli, opere con geometrie non standard; validazione del progetto con il VVF (D.M. 3/8/2015, art. 15 - codici di prevenzione, alternative)."""))
S.append(("idraulica","suids_green",
"IDRAULICA URBANA SOSTENIBILE: LID, SUDS E INFRASTRUTTURE VERDI",
"""La gestione delle acque piovane urban e' diventata strategica:

1. PROBLEMATICA: urbanizzazione -> incremento del deflusso superficiale (2-10 volte), allagamenti, inquinamento delle acque riceventi (prima pioggia), impoverimento falda.

2. LID (Low Impact Development, USA) / SUDS (Sustainable Drainage Systems, UK) / Sponge City (Cina): principi: infiltrare, trattenere, filtrare, riutilizzare l'acqua piovana il piu' vicino possibile al punto di caduta; fonte -> bacino di trattenimento -> filtrazione -> infiltrazione -> ricarica falda.

3. TECNICHE: tetti verdi (estensivi 5-15 cm, intensivi 20-60 cm), pavimentazioni permeabili (sabbia stabilizzata, blocchi forati), bioretention (vasche con substrati filtranti), rain garden, bacini di trattenimento (dry/wet ponds), trench d'infiltrazione, cisterne di accumulo per irrigazione.

4. DIMENSIONAMENTO: evento di progetto (pioggia di riferimento, durata/intensita'), volume di prima pioggia da trattare, portata di sfioro; modelli idrologici (SWMM, MUSIC).

5. BENEFICI: riduzione picchi di piena, depurazione naturale, ricarica falda, mitigazione isola di calore, biodiversita'; integrazione con il verde urbano (nature-based solutions)."""))
S.append(("impianti_avanzati","hp_vrf_geotermia",
"POMPE DI CALORE VRF, GEOTERMIA E DISTRETTERMICI",
"""Gli impianti termici avanzati per edilizia complessa:

1. VRF/VRV (Variable Refrigerant Flow): pompe di calore multizona con refrigerante variabile; un'unita' esterna alimenta piu' unita' interne (fino 64); portate parziali elevate (EER 4-5, SEER > 8); recupero di calore tra zone contemporanee; controlli individuali.

2. GEOTERMIA A BASSA ENTALPIA: pompe di calore con sonde di scambio verticale (50-150 m) o orizzontali (1-2 m di profondita'), captazione falda (pozzi di immissione); COP 4-5 stabili tutto l'anno; campo sonde dimensionato su fabbisogno (W/m di sonda); vincoli autorizzativi (regioni richiedono autorizzazione).

3. DISTRETTERMICI: teleriscaldamento/teleraffrescamento da rete di calore (centrali a biomassa, CCGT, cogenerazione); sottostazioni di scambio; vantaggi: rendimenti centralizzati, integrazione FER, eliminazione caldaie locali.

4. ACCUMULO TERMICO: bollitori stratificati, accumuli inerziali di rete, serbatoi di ghiaccio per raffrescamento diurno (ice storage), termocisterne per isteresi stagionale (sistemi di accumulo di caldo per inverno).

5. IDROGENO E VETTORI: prototipi di reti a idrogeno per edilizia, pompe di calore a idrogeno, ibridi gas-idrogeno; monitoraggio tecnico e normativo in evoluzione."""))
S.append(("emergenza","ricostruzione_post_sisma",
"RICOSTRUZIONE POST-DISASTRO: C.A.S.E., MAP E EDILIZIA DI EMERGENZA",
"""Dopo un sisma o alluvione la ricostruzione e' un processo organizzato:

1. EMERGENZA: valutazione agibilita' (A - agibile, B - agibile con lavori, C - parzialmente agibile, D - inagibile, E - inagibile per pericolo esterno), evacuazione, alloggi di emergenza (tende, container, strutture temporanee), ricerca persone (USAR - Urban Search and Rescue), valutazione rapida con metodi semplificati.

2. C.A.S.E. (Calatestio Anti-Sismico Edilizio, L'Aquila 2009): progetto per edilizia temporanea antisismica in acciaio con isolatori alla base, installata in 4 mesi, standard per le nuove ricostruzioni temporanee.

3. MAP (Moduli Abitativi Provvisori): sistema modulare in acciaio con tamponamenti variabili, connettori rapidi, servizi integrati; progettato per durata 3-8 anni.

4. PERMANENTE: ricostruzione con criteri antisismici attuali (miglioramento, non solo ripristino), con incentivi specifici (Sismabonus), ricostruzione pesante (demolizione) o leggera (consolidamento), ricostruzione privata vs pubblica, gare per assegnazione.

5. LESSON LEARNED: dalla gestione L'Aquila (2009) ed Emilia (2012): importanza della velocita' di valutazione, comunicazione pubblica, coinvolgimento dei privati, qualita' degli interventi, memoria sismica."""))

os.makedirs('parsed', exist_ok=True)
meta = {
    "source": "tecnica_specialistica_kimi",
    "license": "Sintesi didattica originale Kimi (pubblico dominio)",
    "commercial_ok": True,
    "attribution": "Corpus tecnica specialistica a cura di Kimi",
    "url": "",
}
out = []
for i, (cat, tema, titolo, testo) in enumerate(S, 1):
    rec = dict(meta)
    rec.update({"id": f"SPE-{i:03d}", "categoria": cat, "tema": tema, "title": titolo, "text": testo.strip()})
    out.append(rec)

path = os.path.join('Edilizia_Pack', 'parsed', 'tecnica_specialistica.jsonl')
os.makedirs(os.path.dirname(path), exist_ok=True)
with open(path, 'w', encoding='utf-8') as f:
    for r in out:
        f.write(json.dumps(r, ensure_ascii=False) + '\n')
print(f"scritte {len(out)} schede tecnica specialistica -> {os.path.abspath(path)}")
