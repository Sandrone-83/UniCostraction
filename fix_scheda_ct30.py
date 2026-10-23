import json, io

p = r'UNIVERSITA_EDILIZIA/ENERGETICA_INCENTIVI_PACK/schede/schede.jsonl'
rows = [json.loads(l) for l in open(p, encoding='utf-8').read().splitlines() if l.strip()]
r = rows[0]
assert r['nome'].startswith('Il Conto Termico 3.0'), r['nome']

OLD = ("Nota ottobre 2026: un decreto correttivo del D.M. 7/8/2025 e' in itinere: lo schema di modifica e' "
       "all'ordine del giorno della Conferenza Unificata del 22 ottobre 2026 (convocazione protocollata il "
       "14/10/2026, intesa ai sensi dell'art. 10 co. 2 D.Lgs 199/2021; temi attesi: gestione delle risorse, "
       "accessi, piccoli Comuni, controlli). L'iscrizione all'ordine del giorno NON equivale a regole gia' "
       "operative: contenuti, esito e data di entrata in vigore da verificare sul testo pubblicato in Gazzetta "
       "Ufficiale e sulle Regole Applicative GSE aggiornate.")

NEW = ("Nota ottobre 2026 (aggiornata al 23/10): la Conferenza Unificata del 22/10/2026 ha espresso INTESA "
       "CON OSSERVAZIONI sullo schema di decreto correttivo del D.M. 7/8/2025; il MASE adottera' il testo "
       "definitivo e la pubblicazione in Gazzetta Ufficiale e' ancora attesa: le nuove regole NON sono "
       "operative finche' il decreto non e' pubblicato in GU e fino all'aggiornamento delle Regole Applicative "
       "GSE. Contenuti dello schema (da bozza, da confermare sul testo definitivo): per i Comuni fino a 15.000 "
       "abitanti copertura al 100% solo per il primo intervento e 80% per quelli successivi, con tutela delle "
       "domande presentate prima dell'entrata in vigore; gestione dei 900 M€/anno con riserva minima di 300 M€ "
       "per le PA e 300 M€ per privati/imprese e limitazioni dell'accesso a prenotazione al raggiungimento delle "
       "soglie di impegno (600 M€ per categoria: solo accesso diretto per 60 giorni; 900 M€ complessivi: stop "
       "prenotazioni per 60 giorni; prenotazioni entro il 50% delle risorse PA); calcolo dell'impegno di spesa "
       "cumulata su media triennale con contatore pubblico GSE; per le PA pagamento in unica soluzione se "
       "l'incentivo non supera 50.000 euro; rafforzamento di rigetto, decadenza e recupero (anche verso il "
       "mandatario all'incasso); estensione dell'obbligo di APE post-intervento e diagnosi anche a sostituzione "
       "serramenti e schermature solari; aggiornamento dei requisiti tecnici per schermature, illuminazione LED "
       "e generatori a biomassa (parametri di particolato).")

assert OLD in r['normative'], 'pattern non trovato'
r['normative'] = r['normative'].replace(OLD, NEW)

out = io.open(p, 'w', encoding='utf-8', newline='\n')
for row in rows:
    out.write(json.dumps(row, ensure_ascii=False) + '\n')
out.close()

rows2 = [json.loads(l) for l in open(p, encoding='utf-8') if l.strip()]
assert len(rows2) == 18
print('OK: scheda 0 aggiornata, JSON valido, 18 righe')
i = rows2[0]['normative'].find('Nota ottobre 2026')
print()
print(rows2[0]['normative'][i:i+520])
