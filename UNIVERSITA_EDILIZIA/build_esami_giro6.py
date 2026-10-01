# -*- coding: utf-8 -*-
"""Giro 6: esami per i 4 pack nuovi e 5 corsi che ancora non ne avevano."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_esami_giro5 import gen

JOBS = [
    ("SICUREZZA_CANTIERE_DLSGS81_PACK", "SICUREZZA_CANTIERE", 250),
    ("MURATURE_INTONACI_E_FINITURE_PACK", "MURATURE_INTONACI", 250),
    ("FACILITY_MANAGEMENT_E_MANUTENZIONE_PACK", "FACILITY_MANAGEMENT", 250),
    ("FISCO_TRIBUTI_IMPRESA_EDILE_PACK", "FISCO_IMPRESA_EDILE", 250),
    ("DISEGNO_TECNICO_MANUALE_PACK", "DISEGNO_TECNICO", 250),
    ("DOMOTICA_PACK", "DOMOTICA", 300),
    ("POSA_IN_OPERA_PACK", "POSA_IN_OPERA", 300),
    ("MATERIALI_COMPONENTI_IMPIANTISTICA_PACK", "MATERIALI_COMPONENTI", 250),
    ("INGEGNERIA_CIVILE_PACK", "INGEGNERIA_CIVILE", 250),
]
for pack, titolo, n in JOBS:
    gen(pack, titolo, n)
