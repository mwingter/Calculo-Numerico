import numpy as np

import sys
sys.path.insert(0, '../Sol-Sistemas-Lineares/')
import gaussElimination

import matplotlib.pyplot as plt

#exemplo
'''
f = np.array([0.459,0.828,1.006,1.150,1.354,1.261,1.157,0.834,0.511]) #vetor de valores f
M = np.array([[0.01,0.04,0.09,0.16,0.25,0.36,0.49,0.64,0.81],[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9],[1,1,1,1,1,1,1,1,1]]) #matriz com os n vetores hk
n = 3 #dimensão da matriz simétrica A
'''

#ex1
'''
f = np.array([1,1.01,1.02,1.04,1.05,1.06,1.065,1.08]) #vetor de valores f
M = np.array([[1,1.05,1.1,1.15,1.2,1.25,1.3,1.35],[1,1,1,1,1,1,1,1]]) #matriz com os n vetores hk
n = 2 #dimensão da matriz simétrica A
'''

#ex2
'''
f = np.array([1.105,1.221,1.348,1.491,1.64,1.822,2.013,2.22,2.459]) #vetor de valores f
M = np.array([[0.01,0.04,0.09,0.16,0.25,0.36,0.49,0.64,0.81],[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9],[1,1,1,1,1,1,1,1,1]]) #matriz com os n vetores hk
n = 3 #dimensão da matriz simétrica A
'''

#ex3 - natalidade brasil
f = np.array([43.5,44.0,37.7,31.87,23.72,21.06]) #vetor de valores f
M = np.array([[0,1,2,3,4,5],[1,1,1,1,1,1]]) #matriz com os n vetores hk
n = 2 #dimensão da matriz simétrica A


def min_quadrados(f, M, n):
    A = np.zeros((n,n)) # matriz n x n cheia de zeros
    b = np.zeros(n) #vetor b de tamanho n cheia de zeros
    for i in range(n):
        for j in range(i+1):
            A[i][j] = round(np.dot(M[i],M[j]), 3) # np.dot calcula o produto escalar entre dois vetores
            A[j][i] = round(np.dot(M[i],M[j]), 3)
    
    for i in range(n):
        b[i] = round(np.dot(f,M[i]), 3)

    #print(A)
    #print("\n", b)

    # utilizando o método de resolução de sistemas lineares  
    # para encontrar os coeficientes da solução
    return gaussElimination.gauss(A, b, n)


print("Resposta dos mínimos quadrados:", min_quadrados(f, M, n))

#função que printa o polinomio, dados os coeficientes, em ordem decrescente por grau, ex: c = [1,2,3] => p(x) = 1x^2 + 2x^1 + 3
def aproxFunction(c, n): # c são os coeficientes do polinômio
    p = "p(t) = "
    for i in range(n-1):
        p = p + str(round(c[i], 3)) + "t^(" + str(n-i-1) + ")"
        p = p + " + "

    p = p + str(round(c[n-1], 3))
    print("\nA aproximação por mínimos quadrados é:", p)

aproxFunction(min_quadrados(f,M,n), n)

#outra forma de achar o polinomio é usando função do numpy - ex: poly1d(3, 2, 6) = 3x2 + 2x + 6
polinomio = np.poly1d(min_quadrados(f,M,n))
print("Polinomio: \n", polinomio)

coef = min_quadrados(f,M,n)

#p = lambda x: coef[2] + coef[1]*x + coef[0]*x**2
p = lambda x: coef[1] + coef[0]*x

x = np.linspace(0, 10, num=6, endpoint=True)
# Vamos plotar os resultados
plt.figure(figsize=(10,6),facecolor='white')
#plt.plot(x,np.exp(x),label = 'f(x)',linewidth = 3)
plt.plot(x,p(x),label = 'p(x)',linewidth = 2,marker='>')
plt.xlabel('x',fontsize='large') 
plt.ylabel('y',fontsize='large') 
plt.title('Comparação da função aproximada') 
plt.legend(fontsize='large') 
plt.show()
