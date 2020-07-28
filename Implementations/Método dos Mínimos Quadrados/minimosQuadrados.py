import numpy as np

import sys
sys.path.insert(0, '../Sol-Sistemas-Lineares/')
import gaussElimination

f = np.array([0.459,0.828,1.006,1.150,1.354,1.261,1.157,0.834,0.511]) #vetor de valores f
M = np.array([[0.01,0.04,0.09,0.16,0.25,0.36,0.49,0.64,0.81],[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9],[1,1,1,1,1,1,1,1,1]]) #matriz com os n vetores hk
n = 3 #dimensão da matriz simétrica A


def min_quadrados(f, M, n):
    A = np.zeros((n,n)) # matriz n x n cheia de zeros
    b = np.zeros(n) #vetor b de tamanho n cheia de zeros
    for i in range(n):
        for j in range(i+1):
            A[i][j] = round(np.dot(M[i],M[j]), 3) # np.dot calcula o produto escalar entre dois vetores
            A[j][i] = round(np.dot(M[i],M[j]), 3)
    
    for i in range(n):
        b[i] = round(np.dot(f,M[i]), 3)

    print(A)
    print("\n", b)

    # utilizando o método de resolução de sistemas lineares  
    # para encontrar os coeficientes da solução
    return gaussElimination.gauss(A, b, n)

print("Resposta dos mínimos quadrados:", min_quadrados(f, M, n))

