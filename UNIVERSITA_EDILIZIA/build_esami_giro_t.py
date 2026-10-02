# -*- coding: utf-8 -*-
"""Giro T: rigenerazione content-locked (criterio v2) dei settori sotto il 10% di LOCK
che AuraTrix studia per primo: DIMENSIONAMENTO_TERMOTECNICO (2%), ENERGETICA_INCENTIVI (2%),
FOTOVOLTAICO_CER (5%). Bozza verso v1.4, nessun tag."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_esami_design_v2 import gen

JOBS = [
    ("DIMENSIONAMENTO_TERMOTECNICO_PACK", "DIMENSIONAMENTO_TERMOTECNICO", 250),
    ("ENERGETICA_INCENTIVI_PACK", "ENERGETICA_INCENTIVI", 250),
    ("FOTOVOLTAICO_CAMPI_AGRIVOLTAICO_CER_PACK", "FOTOVOLTAICO_CER", 400),
]
if __name__ == "__main__":
    for pack, titolo, n in JOBS:
        gen(pack, titolo, n)
