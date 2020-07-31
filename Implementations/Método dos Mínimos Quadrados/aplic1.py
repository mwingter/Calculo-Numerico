#aplicação do método dos minimos quadrados
# Utilizando o método dos mínimos quadrados para encontrar a reta f(x) que melhor se ajusta 
# a tabela de dados referente à taxa bruta de natalidade no Brasil do ano 1950 à 2020.

import numpy as np
from minimosQuadrados import min_quadrados as mq

#import matplotlib.pyplot as plt

f = np.array([43.5,44.0,37.7,31.87,23.72,21.06]) #vetor de valores f
M = np.array([[0,1,2,3,4,5],[1,1,1,1,1,1,1,1,1]]) #matriz com os n vetores hk
n = 2 #dimensão da matriz simétrica A

#aplicando o método dos mínimos quadrados
print("Resp do metodo min quadrados: ", mq(f, M, n))
