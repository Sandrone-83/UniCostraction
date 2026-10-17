# -*- coding: utf-8 -*-
"""Giro di sicurezza — fix dei riferimenti stale certi in enciclopedia e indice."""
import io

def edit(path, old, new):
    t = io.open(path, encoding='utf-8').read()
    if new in t and old not in t:
        print('SKIP (già applicato) %s :: %s...' % (path.split('/')[-1], old[:45]))
        return
    assert old in t, 'NON TROVATO in %s: %s' % (path, old[:60])
    assert t.count(old) == 1, 'DUPLICATO in %s: %s' % (path, old[:60])
    io.open(path, 'w', encoding='utf-8').write(t.replace(old, new))
    print('OK %s :: %s...' % (path.split('/')[-1], old[:45]))

E = 'ENCICLOPEDIA/'

# 1-2. PRIERA (refuso noto dal Giro V, mai propagato alle voci)
edit(E + 'VOCI_FACOLTA_IMPIANTI_ENERGIA.md',
     'prenotare il termotecnico per la certificazione PRIERA della fine dei lavori',
     'prenotare il termotecnico per la certificazione PRIMA della fine dei lavori')
edit(E + 'VOCI_FACOLTA_GESTIONE_SISTEMA.md',
     'verificare il numero di millesimi presenti e il quorum PRIERA di firmare l\'appalto',
     'verificare il numero di millesimi presenti e il quorum PRIMA di firmare l\'appalto')

# 3. INDICE_ALFABETICO — voce diagnosi rinominata (Giro X)
edit(E + 'INDICE_ALFABETICO.md',
     '- **Diagnosi energetica e energy manager: gli obblighi D.Lgs 102/2014** — Obblighi · corso: *Energetica edilizia e incentivi* (`ENERGETICA_INCENTIVI_PACK`)\n  Il D.Lgs 102/2014 (attuazione della direttiva EED) impone: diagnosi energetica periodica alle grandi imprese e alle imprese energivore (scadenza dicembre degli anni dispari), con obbligo alternativo per piccole e medie (',
     '- **Diagnosi energetica e energy manager: gli obblighi D.Lgs 102/2024** — Obblighi · corso: *Energetica edilizia e incentivi* (`ENERGETICA_INCENTIVI_PACK`)\n  Il D.Lgs 102/2024 (recepimento della direttiva EED 2023/1791/UE, in vigore dal 10 ottobre 2025) ha riformato gli obblighi: diagnosi energetica ogni 4 anni per consumi ≥ 10 TJ/anno, ISO 50001 per consumi ≥ 85 TJ/anno; il vecchio sistema (grandi imprese ed energivore, scadenza dicembre anni dispari) resta storico fino al 2025. Energy manager per i soggetti con consumi rilevanti (soglie nei decreti attuativi): (')

# 4. (voce Transizione già aggiornata via script inline: riga 2164-2165 dell'indice)

# 5. Voce audit GEOMETRI — normativa su D.Lgs 102/2014 superata
edit(E + 'VOCI_FACOLTA_GEOMETRI_PERITI.md',
     '- **Caso tipico:** Due diligence tecniche negli acquisti di portafogli immobiliari; audit energetici obbligatori per grandi imprese e energivore.\n- **Normativa:** Art. 8 D.Lgs 102/2014 (audit energetici obbligatori per grandi imprese ed energivore ogni 4 anni); linee guida per le ispezioni degli edifici; norme UNI per la valutazione delle prestazioni degli edifici.',
     '- **Caso tipico:** Due diligence tecniche negli acquisti di portafogli immobiliari; audit energetici obbligatori per i soggetti con consumi ≥ 10 TJ/anno (D.Lgs 102/2024).\n- **Normativa:** D.Lgs 102/2024 (recepimento EED 2023/1791, in vigore dal 10/10/2025: diagnosi energetica UNI CEI EN 16247 ogni 4 anni per consumi ≥ 10 TJ/anno, ISO 50001 per ≥ 85 TJ/anno; ex D.Lgs 102/2014, storico); linee guida per le ispezioni degli edifici; norme UNI per la valutazione delle prestazioni degli edifici.')

# 6-8. Contabilizzazione calore / automazione — D.Lgs 102/2014 citato come vigente: aggiornato a 102/2024 (ex)
edit(E + 'VOCI_FACOLTA_GESTIONE_SISTEMA.md',
     'D.Lgs 102/2014 e normativa cam per la riqualificazione',
     'D.Lgs 102/2024 (ex 102/2014) e normativa CAM per la riqualificazione')
edit(E + 'VOCI_FACOLTA_TECNOLOGIA_E_COSTRUZIONE.md',
     'contabilizzazione calore (D.Lgs 102/2014)',
     'contabilizzazione calore (D.Lgs 102/2024, ex 102/2014)')
edit(E + 'VOCI_FACOLTA_IMPIANTI_ENERGIA.md',
     'illuminazione secondo D.Lgs 102/2014 come recepito',
     'illuminazione secondo D.Lgs 102/2024 (ex 102/2014) come recepito')
edit(E + 'VOCI_FACOLTA_IMPIANTI_ENERGIA.md',
     'D.Lgs 257/2016 (ricarica VE), D.Lgs 102/2014 (automazione), direttiva 2020/2184 (acque)',
     'D.Lgs 257/2016 (ricarica VE), D.Lgs 102/2024 (automazione, ex 102/2014), direttiva 2020/2184 (acque)')

print('Tutti i fix stale certi applicati.')
