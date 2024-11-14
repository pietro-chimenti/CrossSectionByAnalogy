# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 14:29:53 2024

@author: P.Chimenti, R.F.Marins
"""

import numpy as np
import matplotlib as mpl

print("Bem vindo à analise do experimento 'Seção de Choque por  Analogia' ")

# Vamos experimentar numeros aleatórios

seed = 12346
rng = np.random.default_rng(seed)
print("Um numero aleatório qualquer entre [0,1.0):",rng.random())
print("Um outro  numero aleatório qualquer entre [0,1.0):",rng.random())
