import numpy as np

n = 3 #dimensão do sistema
A = np.array([[6,3,1],[4,9,-3],[1,-1,3]]) #matrix do sistema linear
b = np.array([10,16,14]) #vetor solução
x0 = np.array([-1.8,5.5,7.3]) # chute inicial
x = np.vstack((x0,np.zeros(3)))
epsilon = 0.1 #erro
limit = 100 #limite de iteracao

def gauss_jacobi(A,b,x,n):
    k = 1
    while (np.max(np.abs(x[1]-x[0])) > epsilon) and (k < limit):
        if (k!=1): x[0] = x[1]
        for i in range(n):
            sum = 0 
            for j in range(n):
                if j != i: 
                    sum = sum + (A[i][j] * x[0][j])
            x[1][i] = ((b[i] - sum) / A[i][i])
        k = k + 1
        print(np.max(np.abs(x[1]-x[0])))
    return x[1]

print("Resposta do método Gauss-Jacobi:", gauss_jacobi(A, b, x, n))