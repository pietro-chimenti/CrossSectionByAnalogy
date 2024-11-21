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


# Algumas definições
diametro_bolinha = 20 # em milimetro, uma estimativa do diametro da bolinha de goode
tamanho_fenda = 500   # em milimetros, distancia entre os livros

def Probabilidade_Acerto(d_bolinha, t_fenda, n_tentativas = 1000000):
    """
    d_bolinhas: diametro das bolinhas
    t_fendas: distancias entre os livros

    Returns
    -------
    probabilidade (numero entre 0 e 1) de acertar a bolinha
    a probabilidade e´ estimada com metodo monte carlo usando n_tentativas
    """
    acerto = 0.
    for i in range(n_tentativas):
        posicao = rng.random()*t_fenda
        if abs(posicao - t_fenda/2.) < d_bolinha : acerto += 1
    return acerto/n_tentativas, np.sqrt(acerto)/n_tentativas


print("Probabilidade de acerto: ", Probabilidade_Acerto( diametro_bolinha , tamanho_fenda))

