import numpy as np

n = 4 #dimensão do sistema
A = np.array([[1,1,0,3],[2,1,-1,1],[3,-1,-1,2],[-1,2,3,-1]]) #matrix do sistema linear
b = np.array([4,1,-3,4]) #vetor solução


# MÉTODO DIRETO - ELIMINAÇÃO DE GAUSS
def gauss_elimination(A, b, n): #Fase 1
    for i in range(n):
        pivot = A[i][i]
        for k in range(i+1,n):
            Mik = A[k][i] / pivot
            b[k] = b[k] - Mik * b[i]
            A[k] = A[k] - Mik * A[i] 

    return A, b


def retro_substitution(A, b, n): #Fase 2
    x = np.zeros(n)
    for i in range(n-1, -1,-1):
        x[i] = b[i]
        sum = 0 
        j = n-1
        while (j>i):
            sum = sum + A[i][j] * x[j]
            j = j-1  
        x[i] = (x[i] - sum)/A[i][i]

    return x


def gauss (A,b,n):
    C, blinha = gauss_elimination(A,b,n)
    x = retro_substitution(C,blinha,n)
    return x

print("Resposta do sistema linear:", gauss(A,b,n))

