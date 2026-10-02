# -*- coding: utf-8 -*-
"""Giro O: esame content-locked (criterio v2) per SERRAMENTI_E_VETRATE_PACK.

Primo esame generato interamente col criterio corretto post-audit: cloze
numeriche e su nomi propri + casi/costi/note/norme. Nessuna domanda
'appartiene alla tecnologia' risolvibile per tematica.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_esami_design_v2 import gen

if __name__ == "__main__":
    gen("SERRAMENTI_E_VETRATE_PACK", "SERRAMENTI", 250)
