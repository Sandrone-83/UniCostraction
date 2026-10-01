# -*- coding: utf-8 -*-
"""LEGISLAZIONE_PRIVATA_EDILIZIA_PACK: contratti privati, condominio, responsabilità, garanzie in edilizia."""
import json, os

ROOT = os.path.dirname(os.path.abspath(__file__))

def s(cat, nome, desc, tec, app, van, lim, cos, casi, norm, note):
    return dict(categoria=cat, nome=nome, descrizione=desc, tecnologia=tec,
                applicazioni=app, vantaggi=van, limiti=lim, costi_e_economia=cos,
                casi_real_world=casi, normative=norm, note_cantiere=note)

DATA = [
s("Compravendita", "La compravendita immobiliare: atto, passaggi, imposte",
 "Comprare e vendere un immobile (o una costruzione futura: vendita su carta) richiede la verifica completa della situazione legale e fiscale PRIORA del rogito: visura catastale e ipotecaria, conformità urbanistica, stato di occupazione, ipoteche e gravami.",
 "Passaggi: proposta con acconto (caparra confirmatoria 10-15%) → atto preliminare (compromesso, trascrivibile con clausole) → verifiche preliminari (visura, catastale, planimetrie, abusi) → rogito notarile con passaggio di proprietà e pagamento (saldo, imposte di registro o IVA se da costruttore entro 4 anni, ipotecaria, catastale, notaio); la vendita di immobile abusivo è nulla o annullabile: verifica dei titoli edilizi essenziale.",
 "Trattative immobiliari, vendita di costruzioni, ristrutturazioni a scopo di valorizzazione.",
 "La due diligence immobiliare protegge compratore e venditore: niente sorprese dopo il rogito (abusivi scoperti, abitanti non sfrattabili, ipoteche non visibili).",
 "Le verifiche hanno un costo (visure, tecnico) e richiedono settimane: chi corre sul rogito raccoglie i problemi.",
 "Costi compratore: imposte 2-9% del valore (secondo caso: prima casa, seconda, da costruttore), notaio 1.500-4.000 €, tecnico per verifiche 500-2.000 €.",
 "Compravendita con abuso (mansardo non accatastata): scoperto dopo il rogito, il compratore ha dovuto sanare a proprie spese (40.000 €); il perito pre-acquisto avrebbe intercettato tutto.",
 "Codice civile artt. 1470-1547 (compravendita); DPR 131/1986 (catasto); normativa fiscale (TUIR, aggiornata annualmente).",
 "Domande da insegnare: il venditore è costruttore (IVA) o privato (registro)? ci sono abusi? il catasto è conforme al reale? l'immobile è libero?"),
s("Locazione", "La locazione abitativa: legge 431/1998, canone concordato",
 "La locazione abitativa è regolata dalla L. 431/1998: durata minima 4 anni + rinnovo 4 (contratto transitorio solo per esigenze specifiche), requisiti abitabilità e agibilità, deposito cauzionale max 3 mensilità; il canone concordato (presso le organizzazioni di categoria) prevede tassazione ridotta (cedolare secca 21% o 26% seconda casa) e canoni calmierati.",
 "Strumenti: contratto registrato (obbligo), inventario con foto, stato manutentivo (chi cura cosa), clausole di recesso, aggiornamento ISTAT annuo per canone libero; locazione breve turistica (CIN, regole regionali e comunali sempre più stringenti).",
 "Proprietari, inquilini, imprese che gestiscono patrimoni locativi.",
 "Il contratto scritto e registrato protegge entrambi: il proprietario può sfrattare e aggiornare, l'inquilino ha diritti certi.",
 "La locazione informale è illegale e pericolosa per entrambi: sfratto difficile per il proprietario, nessun diritto per l'inquilino.",
 "Costi: registrazione proporzionale o fisso (cedolare secca: 21/26% sul canone); agenzia: una mensilità + IVA circa.",
 "Locazione con canone concordato + cedolare secca: tassazione effettiva dimezzata rispetto al regime ordinario su un appartamento da 700 €/mese: differenza di oltre 1.200 €/anno.",
 "L. 431/1998; D.Lgs 23/2011 (cedolare secca); leggi regionali su locazioni brevi.",
 "Il contratto tipo del territorio (canone concordato) conviene quasi sempre: meno tasse, canone leggermente calmierato ma stabilità maggiore."),
s("Condominio", "Il condominio: riforma 2012, assemblea, ripartizioni",
 "Il condominio negli edifici è regolato dalla riforma del 2012 (L. 220/2012): assemblea con maggioranze (500 millesimi per la maggioranza semplice, 2/3 del valore per le opere straordinarie), lavori straordinari obbligatori (art. 1117-bis c.c.), amministratore con doveri di cura, tabella millesimale come chiave di tutte le ripartizioni.",
 "Meccanismi: assemblea ordinaria e straordinaria (secondo l'oggetto), le maggioranze: 500 millesimi presenza + maggioranza dei presenti per gestione ordinaria; 500 millesimi presenza + 2/3 dei presenti per innovazioni straordinarie e installazioni; l'impresa che lavora in condominio interagisce con l'amministratore: ordini, autorizzazioni assembleari per parti comuni.",
 "Cantieri condominiali (facciate, coperture, impianti centralizzati), consulenza a proprietari e amministratori.",
 "Le regole del condominio sono oggettive: chi conosce le maggioranze e le ripartizioni evita contestazioni e lavori bloccati.",
 "La tabella millesimale è spesso vecchia o controversa: le opere su parti comuni si ripartiscono per millesimi salvo diversa destinazione d'uso.",
 "Costi: amministratore 200-600 €/anno per unità; perizie e tabelle: a parte.",
 "Cantiere di rifacimento copertura condominiale: l'impresa aveva il solo ordine del presidente; l'assemblea non aveva autorizzato: lavori bloccati a metà e contenzioso; la verifica dell'autorizzazione assembleare prima di iniziare era il passaggio mancante.",
 "Artt. 1117-1139 c.c.; L. 220/2012 (riforma condominio); regolamento condominiale.",
 "Regola per l'impresa: in condominio si inizia SOLO con autorizzazione scritta dell'amministratore o dell'assemblea documentata."),
s("Responsabilità", "La responsabilità dell'impresa costruttrice: art. 1669 e decennale",
 "L'art. 1669 c.c. (responsabilità del costruttore e dell'impresa) prescrive: se entro 10 anni (decennale) l'immobile mostra vizi o crolli per difetto della costruzione o del terreno, il costruttore è tenuto al risarcimento; per il venditore di immobili su aree proprie vale lo stesso termine; la garanzia è assicurata (obbligo polizza decennale per le costruzioni).",
 "Catena della responsabilità: costruttore (10 anni), installatori di opere importanti (appalto e subentro, 10 anni), professionisti (3 o 10 anni secondo la natura del vizio, giurisprudenza consolidata); prescrizione decennale; azione diretta del compratore contro chi ha costruito anche senza contratto diretto (art. 1670 c.c.).",
 "Ogni impresa costruttrice, ogni professionista, ogni compratore di nuovo.",
 "La regola chiara dei termini permette di prevedere il rischio: l'impresa sa cosa rischia e per quanto; il cliente sa a chi rivolgersi.",
 "I vizi latenti emergono a cantiere chiuso da anni: l'impresa che non tiene l'archivio dei cantieri (materiali, collaudi, foto) non può difendersi.",
 "Polizza decennale: 0,5-1,5% del valore dell'opera; la difesa in un contenzioso decennale: 15.000-100.000 €.",
 "Infiltrazione in una cantina di condominio costruito 8 anni prima: l'impermeabilizzazione era difettosa; la polizza decennale ha coperto la riparazione (60.000 €) — senza polizza, l'impresa (ancora esistente) avrebbe pagato di tasca propria.",
 "Art. 1669-1670 c.c.; normativa sulla polizza assicurativa obbligatoria (legge 210/2004).",
 "Per il LLM: il decennale non è uno scudo assicurativo ma un regime di responsabilità: la polizza copre, ma la reputazione si difende con l'archivio del cantiere."),
s("Garanzie", "Le garanzie in edilizia: fideiussioni, certificazioni e attestazioni",
 "Le garanzie muovono denaro: il cliente chiede fideiussione (garanzia bancaria o assicurativa) a garanzia di caparra, acconti, esecuzione; l'impresa offre attestazioni di conformità, certificazioni energetiche, attestati di collaudo; ogni garanzia ha un costo che va nel prezzo.",
 "Tipi: fideiussione a garanzia dell'acconto (5-20% del contratto), fideiussione per ultimazione lavori, polizza decennale postuma, certificazione energetica APE obbligatoria in compravendita e locazione, attestato di conformità impianti (obbligo), attestazione di regolare esecuzione a fine lavori; la fideiussione bancaria costa commissioni annuali (1-3%); quella assicurativa è spesso più economica.",
 "Contratti di ristrutturazione e nuova costruzione, compravendite, pratiche di fine lavori.",
 "Le garanzie corrette danno sicurezza a entrambe le parti: il cliente protegge i soldi, l'impresa documenta la qualità.",
 "Il circolo vizioso del 'faccio la fideiussione dopo': chi consegna acconti senza garanzia scopre poi che recuperare è costoso e lento.",
 "Costo fideiussione: 1-3%/anno dell'importo garantito (banca), 0,5-1,5% (assicurativa); emissione: 100-300 € fisse.",
 "Cliente che ha versato 30.000 € di acconto con fideiussione assicurativa: l'impresa è fallita a metà lavori; l'assicurazione ha rimborsato l'acconto in 3 mesi; il vicino di casa, senza fideiussione, è in attesa di recupero dal fallimento da 2 anni.",
 "Codice civile (garanzie, assicurazioni); legge 210/2004 (polizze); normativa APE (D.Lgs 192/2005 s.m.i.).",
 "Regole per l'LLM consulente: mai acconti senza garanzia, mai garanzie senza costo nel preventivo, mai fine lavori senza attestazioni."),
s("Consumatore", "Il cliente consumatore in edilizia: diritti e doveri",
 "Quando il committente è un consumatore (famiglia, persona fisica per uso personale) si applica il codice del consumo (D.Lgs 206/2005): divieto di clausole vessatorie, obbligo di chiarezza contrattuale, responsabilità per difetti di conformità (2 anni di garanzia sulle cose vendute, applicabile per le opere), diritto di recesso nei contratti negoziati fuori sede (anche il preventivo firmato in casa del cliente).",
 "Implicazioni pratiche: il contratto con il privato deve essere chiaro (voci, esclusioni, tempi, penali), i preventivi dettagliati (voce per voce), la documentazione consegnata (manuali, certificazioni), la gestione dei reclami documentata; il recesso fuori sede: 14 giorni con restituzione di quanto pagato.",
 "Impresa che lavora per privati: la quasi totalità delle ristrutturazioni residenziali.",
 "Il rispetto delle regole consumatore elimina la maggior parte dei contenziosi: i clienti litigano quando si sentono aggrediti, non quando sono informati.",
 "Le sanzioni amministrative per pratiche scorrette (es. preventivi gonfiati, subentri occulti) sono pesanti e pubbliche (comunicazione AGCM).",
 "Costo della conformità: tempo di scrittura contratti (o modello legale: 500-2.000 € da professionista).",
 "Ristrutturazione con contratto 'tutto incluso' senza dettaglio voci: il cliente ha chiesto il dettaglio a fine lavori, i prezzi erano 'a sensazione': il giudice ha ridotto il corrispettivo del 22% per mancanza di trasparenza.",
 "D.Lgs 206/2005 (codice consumo); D.Lgs 21/2014; prassi AGCM.",
 "La trasparenza preventiva è la polizza assicurativa più economica dell'impresa edile."),
s("Tutela operatore", "La tutela dell'operatore: riserve, verbali, perizie",
 "L'impresa e il professionista devono proteggersi DURANTE il rapporto: le riserve scritte (entro 24-48 ore dall'evento), i verbali di sopralluogo firmati, le perizie asseverate nei casi controversi, la documentazione fotografica continua; il silenzio prolungato vale come accettazione nella prassi giudiziaria.",
 "Strumenti: riserva formale (lettera/email all'amministrazione o al committente: 'si riserva di comunicare costi e tempi delle sconnessioni emerse in data...'), verbale di sopralluogo congiunto firmato da entrambe le parti, perizia giurata di parte quando il conflitto è serio; registro di tutte le comunicazioni (email valgono).",
 "Ogni cantiere con sconnessioni, varianti, contestazioni.",
 "La riserva tempestiva cambia l'esito dei giudizi: chi riserva subito, poi può chiedere; chi tace per mesi, quasi mai.",
 "La cultura della riserva è bassissima nelle imprese piccole: 'non voglio litigare col cliente' si trasforma in 'ho pagato io le sconnessioni'.",
 "Costo: tempo (mezz'ora a evento); perizia asseverata: 1.000-3.000 €.",
 "Cantiere con umidità emersa a parete smontata: riserva scritta in 24 ore con foto; il committente ha riconosciuto il costo extra (4.800 €) senza alcuna vertenza; la stessa impresa, altro cantiere, senza riserva: ha pagato lei.",
 "Codice civile (appalto, atti di procedura); prassi giudiziaria consolidata.",
 "Frase chiave: 'riservarsi di comunicare' è la formula professionale che trasforma un problema in una voce di conto."),
s("Crisi impresa", "La crisi d'impresa: segnali, strumenti, continuità",
 "Le imprese edili falliscono per crisi di liquidità più che di mercato: segnali precoce (fornitori che chiedono ridotte tempistiche, banca che riduce i fidi, cantieri che non chiudono i SAL, margine che scivola sotto il 10%); la legge sulla crisi d'impresa (Codice della crisi 2022) ha introdotto l'allerta con obblighi di monitoraggio.",
 "Strumenti: il piano dei flussi di cassa mensile (previsione entrate/uscite), la negoziazione con banche e fornitori PRIORA del dissesto, la composizione negoziata per la crisi (strumento che protegge mentre si rinegozia), la cessione del ramo d'azienda, la continuazione come subentrante; l'obbligo di allerta per società e ditte sopra certe soglie.",
 "Imprese in difficoltà, subentri in cantiere, gestione delle commesse di imprese fallite.",
 "La crisi gestita precocemente salva l'impresa: i segnali di 6 mesi prima sono leggibili da chi controlla.",
 "Il tabù del fallimento ritarda l'azione: quando si parla di crisi è spesso tardi per i rimedi morbidi.",
 "Costo consulenza crisi: da quotazione singola a gestione continuativa; il piano flussi fatto internamente: zero.",
 "Impresa con flussi mensili che ha visto il buco di cassa a 5 mesi di distanza: ha ridotto i nuovi cantieri, ceduto un mezzo inutilizzato e negoziato un mini-fido ponte: attraversato la crisi dell'ordine pubblico senza scossoni.",
 "Codice della crisi d'impresa e dell'insolvenza (D.Lgs 14/2019, in vigore 2022); normativa fallimentare precedente.",
 "Domanda mensile del titolare: 'se incassassi la metà dei crediti previsti per 3 mesi, cosa succede?' — chi sa rispondere non muore di sorpresa."),
s("Notaio", "Il notaio in edilizia: rogiti, ipoteche, trascrizioni",
 "Il notaio pubblico è l'ufficiale che dà certezza ai passaggi immobiliari: atto di compravendita, atto di divisione, ipoteca, trascrizione preliminare (salvaguardia chi compra su carta), servitù, diritti reali; la trascrizione nei registri immobiliari è ciò che rende il diritto opponibile.",
 "Operazioni tipiche in edilizia: atto di vendita con clausole a garanzia (vincoli di destinazione, garanzie per vizi), trascrizione del preliminare (protegge l'acquirente da vendite successive), ipoteca per mutui (garanzia della banca), atti di lottizzazione e costituzione di vincoli, successioni e divisioni che riorganizzano i proprietari.",
 "Acquisti immobiliari, vendite, operazioni societarie con immobili.",
 "La certezza notarile evita doppie vendite e passaggi illegittimi: il registro immobiliare è il cuore della sicurezza del mercato.",
 "L'onorario notarile è proporzionale al valore: sulle operazioni piccole pesa in percentuale; i tempi di appuntamento possono rallentare le trattative rapide.",
 "Onorario: tariffario notarile proporzionale (indicativamente 0,5-2,5% secondo valore e complessità) + diritti.",
 "Acquisto con trascrizione preliminare: il venditore ha tentato di vendere a terzi durante la costruzione; la trascrizione ha reso inefficace la seconda vendita e protetto l'acquirente.",
 "Legge notarile (L. 89/1913); disposizioni sul registro immobiliare (DPR 222/1983).",
 "La lezione per l'LLM: nei passaggi immobiliari vale la regola del 'chi trascrive per primo' — la burocrazia tempestiva è difesa dei diritti."),
s("Contratto privato", "Il contratto di appalto privato domestico: equilibrio e chiarezza",
 "L'appalto domestico (art. 1655 c.c.) tra privato e impresa è il contratto tipo della ristrutturazione: l'impresa si obbliga a compiere un'opera o un servizio verso corrispettivo; la chiarezza delle parti (prestazioni, tempi, prezzo, varianti) decide la serenità del cantiere.",
 "Clausole fondamentali: oggetto dettagliato (con richiami a capitolato e computo allegati), prezzo (corrispettivo determinato o a misura), tempi con penale, modalità pagamento (acconto protetto, SAL, saldo a collaudo), varianti (procedura scritta e prezzi prestabiliti), collaudo tacito (l'opera si intende accettata se il committente la utilizza senza riserve), garanzie (decennale), esclusioni esplicite (cosa NON è compreso).",
 "Ristrutturazioni residenziali, contratti tra imprese e famiglie.",
 "Il contratto chiaro è il progetto legale del cantiere: se le regole del gioco sono scritte, il gioco è pulito.",
 "I contratti copia-incolla dal web senza adattamento nascondono clausole vessatorie o inapplicabili (es. penali assurde, riferimenti a norme sbagliate).",
 "Costo modello contrattuale da professionista: 500-2.000 €; negoziazione: tempo.",
 "Contratto con penale di 500 €/giorno di ritardo e bonus di 200 €/giorno di anticipo: il cantiere è finito 3 settimane prima del previsto; entrambe le parti hanno guadagnato dalla chiarezza.",
 "Art. 1655-1677 c.c.; giurisprudenza su clausole vessatorie (art. 1469-bis e ss.).",
 "La checklist del contratto privato (10 clausole) vale più di qualsiasi negoziazione verbale: chi la insegna al LLM offre consulenza di alto livello."),
]

README = """# LEGISLAZIONE_PRIVATA_EDILIZIA_PACK — Diritto privato dell'edilizia

**Facoltà:** FACOLTA_GESTIONE_SISTEMA · **Livello:** L2 · **Schede:** {n}

## Contenuto
Il diritto privato che muove il mercato delle costruzioni: compravendita e due
diligence, locazione abitativa e cedolare secca, condominio e maggioranze,
responsabilità decennale del costruttore, garanzie e fideiussioni, cliente
consumatore (codice del consumo), tutela dell'operatore (riserve e perizie),
crisi d'impresa, notaio e trascrizioni, contratto di appalto privato domestico.

## Formato
- `schede/schede.jsonl` — una scheda per riga, 11 campi standard.
- `COURSE.yaml` — metadati del corso.

## Uso per l'addestramento
Adatto a: consulenza contrattuale di base, conversazioni su diritti e doveri,
prevenzione del contenzioso. NON sostituisce il parere legale: insegna a
riconoscere QUANDO serve il professionista legale e cosa chiedergli.
""".format(n=len(DATA))

COURSE = """corso: "Diritto privato dell'edilizia"
facolta: "FACOLTA_GESTIONE_SISTEMA"
livello: "L2"
schede: {n}
formato: "JSONL"
lingua: "it"
schema_campi: [categoria, nome, descrizione, tecnologia, applicazioni, vantaggi, limiti, costi_e_economia, casi_real_world, normative, note_cantiere]
""".format(n=len(DATA))

os.makedirs(os.path.join(ROOT, "schede"), exist_ok=True)
with open(os.path.join(ROOT, "schede", "schede.jsonl"), "w", encoding="utf-8") as f:
    for d in DATA:
        f.write(json.dumps(d, ensure_ascii=False) + "\n")
with open(os.path.join(ROOT, "README.md"), "w", encoding="utf-8") as f:
    f.write(README)
with open(os.path.join(ROOT, "COURSE.yaml"), "w", encoding="utf-8") as f:
    f.write(COURSE)
print("OK", len(DATA), "schede")
