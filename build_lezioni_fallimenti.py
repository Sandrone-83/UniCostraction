# -*- coding: utf-8 -*-
"""Corpus Lezioni dai Fallimenti: cause tecniche dei grandi disastri edilizi."""
import json, os

S = []

S.append(("morandi",
"IL COLLO DEL PONTE MORANDI (2014) - LEZIONI PER L'INGEGNERIA",
"""Il crollo del viadotto Polcevera (Genova, 14 agosto 2018, 43 vittime) e' una delle tragedie piu' studiate della storia dell'ingegneria moderna:

1. LE CAUSE: la commissione d'inchiesta ha individuato una combinazione di fattori: degrado da decenni della struttura in calcestruzzo armato precompresso, corrosione delle armature da infiltrazioni d'acqua, manutenzione inadeguata, aumento progressivo del carico di traffico, errori di progetto originale (prevedibilita' del degrado sottostimata).

2. LEZIONI STRUTTURALI: la robustezza progressiva (la capacita' di una struttura di non collassare per la perdita di un elemento) era insufficiente; il concetto di 'elemento vitale' non era stato adeguatamente applicato alle strutture in c.a. precompresso.

3. LEZIONI DI GESTIONE: il monitoraggio e la manutenzione programmata sono parte della sicurezza strutturale; i controlli periodici (visivi e strumentali) non erano stati eseguiti con la frequenza necessaria; le segnalazioni di degrado non erano state seguite da interventi tempestivi.

4. IL NUOVO VIADOTTO: il Genova San Giorgio (progettato da Renzo Piano) ha introdotto il concetto di 'barca' autoportante e di manutenibilita' come requisito di progetto: ogni elemento deve essere ispezionabile e sostituibile.

5. REGOLE PER IL TECNICO: mai sottovalutare le fessure e le infiltrazioni; progettare per la manutenzione; applicare la robustezza progressiva; documentare le valutazioni di degrado."""))

S.append(("sisma_aquila",
"L'AQUILA 2009 E IL CONFRONTO CON NORCIA 2016 - LE NORME ANTISISMICHE FUNZIONANO",
"""Il confronto tra i due terremoti dimostra l'efficacia delle norme antisismiche moderne:

1. L'AQUILA (6 aprile 2009, Mw 6,3, 309 vittime): edifici storici in muratura non rinforzata crollarono diffusamente; il centro storico fu devastato. Le cause: murature senza catene, solai non ammorsati, tamponature spingenti, manutenzione assente.

2. NORCIA (30 ottobre 2016, Mw 6,6): nonostanta magnitudo maggiore, i danni furono molto piu' contenuti. Le ragioni: gli edifici ricostruiti dopo il 1997 (normativa post-Umbria-Marche) con catene, cordoli e rinforzi si sono comportati bene; la tipologia costruttiva rinforzata (muratura armata o rinforzata con FRP) ha dimostrato la sua efficacia.

3. LE LEZIONI: le norme antisismiche funzionano se applicate; la ricostruzione con le regole moderne ha salvato vite; gli edifici antichi non rinforzati restano il punto debole.

4. IL RUOLO DEL TECNICO: la valutazione sismica di vulnerabilita' (VUL) degli edifici esistenti e' lo strumento per individuare gli edifici a rischio prima del terremoto; la ricostruzione post-sisma deve applicare i criteri di riduzione del rischio, non solo il ripristino formale."""))

S.append(("balconi",
"IL CROLLO DEI BALCONI - MANUTENZIONE E CONTROLLI",
"""I crolli di balconi e terrazze sono tra gli incidenti edilizi piu' frequenti e prevenibili:

1. LE CAUSE: corrosione delle armature da infiltrazioni (fessure nella guaina, guarnizioni dei parapetti, stagneita' delle soglie), sovraccarico (depositi, piante, arredi pesanti), degrado del calcestruzzo (carbonatazione), mancato controllo delle fessure e delle lesioni.

2. I SEGNALI: fessure sulla soletta o sul cordolo, armature affioranti, distacco dell'intonaco sotto la soletta, gocciolamenti persistenti, rigonfiamenti del manto di copertura del balcone.

3. I CONTROLLI: ispezione periodica (almeno ogni 2-3 anni), verifica della tenuta delle guaine, controllo dei cordoli, misura del copriferro con cover meter, valutazione del degrado del calcestruzzo.

4. LE RESPONSABILITA': il proprietario risponde per i danni a terzi (art. 2051 c.c.); in condominio, la manutenzione dei balconi e' di competenza del proprietario, ma le parti comuni (struttura, facciata) possono essere condominiali; l'amministratore deve promuovere i controlli.

5. LE PRESCRIZIONI: il D.M. 17/01/2018 richiede la valutazione della sicurezza degli edifici esistenti con piani di manutenzione; le assicurazioni RC chiedono sempre piu' spesso l'ispezione documentata."""))

S.append(("alluvioni",
"ALLUVIONI E SOTTOSUOLO - LEZIONI SUL DRENAGGIO E SULLA TENUTA",
"""Le alluvioni urbani dei recenti anni (Marche 2022, Romagna 2023, Toscana 2023) hanno evidenziato i limiti della gestione del territorio e delle costruzioni:

1. LE CAUSE: urbanizzazione diffusa su aree naturalmente di deflusso (fondovalle, conoidi di deiezione), impermeabilizzazione eccessiva del suolo, manutenzione assente di fossi e corsi d'acqua, edilizia nel greto o nelle aree golenali, sottovalutazione delle portate di progetto.

2. LE LEZIONI COSTRUTTIVE: fondazioni e spazi interrati in zone alluvionabili richiedono: barriere stagne, sistemi di drenaggio attivo (pompe di sollevamento con alimentazione di emergenza), paratie anti-risorsa, solette di ripartizione impermeabili, materiali resistenti all'immersione.

3. LA MANUTENZIONE DEL TERRITORIO: la sicurezza idraulica dipende dai manufatti esistenti: pulizia di fossi e caditoie, manutenzione degli argini, controllo degli scarichi, rimozione delle ostruzioni.

4. IL RUOLO DEL TECNICO: verificare la classificazione del rischio idraulico del sito prima del progetto; adottare soluzioni costruttive resilienti; informare il committente dei rischi."""))

S.append(("cantiere_crollo",
"COLLOPSI IN CANTIERE - PONTEGGI, GETTI E SICUREZZA",
"""I crolli in fase di costruzione sono tra gli infortuni piu' gravi dell'edilizia:

1. LE CAUSE: ponteggi non dimensionati o non ancorati correttamente, getti eseguiti troppo presto (casseforme rimosse prima della resistenza richiesta), sovraccarico dei solai in costruzione (depositi di materiali), mancato rispetto delle sequenze costruttive, vento forte su strutture provvisorie.

2. I PRESIDI: progetto dei ponteggi (ponteaggio a carico di lavoro e vento), verifiche di stabilita' delle casseforme, programma dei getti (resistenza minima richiesta prima del disarmo: tipicamente 70-75% Rck per solai), controllo delle condizioni meteo, formazione dei lavoratori.

3. LE NORME: UNI EN 12811 (ponteggi), UNI 7129 (casseforme), DM 14/01/2008 (aggiornato) per le condizioni di sicurezza in fase di costruzione, D.Lgs 81/2008.

4. LE RESPONSABILITA': il datore di lavoro, il DL, il progettista e il costruttore rispondono secondo la catena delle responsabilita'; l'art. 434 c.p. (disastro colposo) colpisce chi, violando le norme tecniche, cagiona il crollo."""))

S.append(("errori_progettazione",
"GLI ERRORI PIU' COSTOSI DI PROGETTAZIONE E CANTIERE",
"""L'esperienza dei disastri edilizi insegna a riconoscere gli errori ricorrenti:

1. FONDAZIONI SOTTODIMENSIONATE: fidarsi di indagini geognostiche insufficienti o sovrastimare la portanza del terreno; errore tipico: non verificare i cedimenti differenziali.

2. SOTTOVALUTAZIONE DEI CARICHI: dimenticare carichi permanenti (tamponature, impianti, arredi) o i sovraccarichi di esercizio reali; usare sovraccarichi normativi quando il carico reale e' maggiore (depositi, attivita' commerciali).

3. PONTI TERMICI E CONDENSA: dettagli costruttivi sbagliati (pilastri non isolati, travi che attraversano il cappotto, ponti termici ai balconi) che generano muffa e degrado.

4. DETTAGLI ESECUTIVI ASSENTI: progettare senza dettagli costruttivi (giunti, ancoraggi, allacci) che poi in cantiere vengono improvvisati con risultati imprevedibili.

5. MATERIALI NON VERIFICATI: usare materiali senza certificazione o senza prove in sito (calcestruzzo senza cubi, acciaio senza certificati di collaudo).

6. MANUTENZIONE IGNORATA: progettare senza considerare l'accessibilita' e la manutenibilita' degli elementi (coperture, facciate, impianti) che poi si degradano invisibilmente.

7. LA REGOLA D'ORO: ogni progetto deve prevedere le fasi di costruzione, l'ispezionabilita' e la manutenzione programmata."""))

os.makedirs('parsed', exist_ok=True)
meta = {
    "source": "lezioni_fallimenti_kimi",
    "license": "Sintesi didattica originale Kimi (pubblico dominio)",
    "commercial_ok": True,
    "attribution": "Corpus lezioni dai fallimenti a cura di Kimi",
    "url": "",
}
out = []
for i, (tema, titolo, testo) in enumerate(S, 1):
    rec = dict(meta)
    rec.update({"id": f"FAL-{i:02d}", "tema": tema, "title": titolo, "text": testo.strip()})
    out.append(rec)

path = os.path.join('Edilizia_Pack', 'parsed', 'lezioni_fallimenti.jsonl')
os.makedirs(os.path.dirname(path), exist_ok=True)
with open(path, 'w', encoding='utf-8') as f:
    for r in out:
        f.write(json.dumps(r, ensure_ascii=False) + '\n')
print(f"scritte {len(out)} schede lezioni dai fallimenti -> {os.path.abspath(path)}")
