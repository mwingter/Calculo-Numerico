import numpy as np

n = 4 #dimensão do sistema
A = np.array([[1,2,-1,0],[2,-1,0,0],[0,-1,2, -1],[0,0,-1,2]]) #matriz
b = np.array([1,1,1,1]) #vetor b
xi = np.array([1,1,1,1]) #vetor aproximação inicial
x = np.array([1,1,1,1]) #vetor aproximação
e = 0.001 #erro 

def gauss_seidel(A, b, xi, x, e, n):
    k = 1 #contador de iterações
    while(1):
        print("---ITERAÇÃO ", k)
        for i in range(n):
            sum1 = 0 
            sum2 = 0
            for j in range(0, i-1):
                sum1 = sum1 + A[i][j] * x[j]
            for j in range (i+1, n):
                sum2 = sum2 + A[i][j] * xi[j]
            print("sum 1 = ", sum1, "sum 2 =", sum2)
            x[i] = (1/A[i][i]) * (b[i] - sum1 - sum2)
            print("x[", i, "] = ( 1/", A[i][i], ") * (", b[i], "-", sum2, "-", sum1, ")")
            print("x[", i, "] = ", x[i])
            
        #Critério de parada
        max = -99999
        for i in range(n):
            tot = abs(x[i] - xi[i])
            print("x[", i, "] - xi[", i, "] =", x[i], "-", xi[i], "=", tot)
            if(max < tot):
                max = tot

        if(max < e):
            #print("RESULTADO x = ", x)
            return x
        else:
            k = k + 1
            for i in range(n):
                xi[i] = x[i]

print("Resposta do método Gauss-Seidel:", gauss_seidel(A, b, xi, x, e, n))