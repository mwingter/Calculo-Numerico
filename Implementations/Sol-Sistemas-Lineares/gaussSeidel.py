import numpy as np

#teste1
"""
n = 3 #dimensão do sistema
A = np.array([[6.0,3.0,1.0],[4.0,9.0,-3.0],[1.0,-1.0,3.0]]) #matriz
b = np.array([10,16,14]) #vetor b
xi = np.array([-1.8,5.5,7.3]) #vetor aproximação inicial
x = np.array([1.0,1.0,1.0]) #vetor aproximação
e = 0.1 #erro
"""

#teste2 (ex da foto3) 
#resposta => x = (0.90863, 0.81781, 1.54497, 1.27248)
n = 4 #dimensão do sistema
A = np.array([[2.0,-1.0,0,0],[1.0,2.0,-1.0,0],[0,-1.0,2.0,-1.0],[0,0,-1.0,2.0]]) #matriz
b = np.array([1,1,1,1]) #vetor b
xi = np.array([1.0,1.0,1.0,1.0]) #vetor aproximação inicial
x = np.array([1.0,1.0,1.0,1.0]) #vetor aproximação
e = 0.001 #erro

"""
def gauss_seidel(A, b, xi, x, e, n):
    k = 1 #contador de iterações
    while(k < 20):
        print("---ITERAÇÃO ", k)
        for i in range(n):
            sum1 = 0 
            sum2 = 0
            for j in range(0, i):
                print("     sum1 = ", sum1, "+", A[i][j], "*", x[j])
                sum1 = sum1 + A[i][j] * x[j]
            for j in range (i+1, n):
                print("     sum2 = ", sum2, "+", A[i][j], "*", xi[j])
                sum2 = sum2 + A[i][j] * xi[j]
            print("sum 1 = ", sum1, "sum 2 =", sum2)
            x[i] = (1/A[i][i]) * (b[i] - sum1 - sum2)
            print("x[", i, "] = ( 1/", A[i][i], ") * (", b[i], "-", sum2, "-", sum1, ")")
            print("=> x[", i, "] = ", x[i])
            
        #Critério de parada
        max = -99999
        for i in range(n):
            tot = abs(x[i] - xi[i])
            print("x[", i, "] - xi[", i, "] =", x[i], "-", xi[i], "=", tot)
            if(max < tot):
                max = tot

        if(max < e):
            print("RESULTADO x = ", x)
            return x
        else:
            k = k + 1
            for i in range(n):
                xi[i] = x[i]

print("Resposta do método Gauss-Seidel:", gauss_seidel(A, b, xi, x, e, n))
"""
def iteration(A, b, xi, x, n): ##iteração k, em que se calcula os valores do array x
    for i in range(n):
        sum1 = 0 
        sum2 = 0
        for j in range(0, i):
            #print("     sum1 = ", sum1, "+", A[i][j], "*", x[j])
            sum1 = sum1 + A[i][j] * x[j]
        for j in range (i+1, n):
            #print("     sum2 = ", sum2, "+", A[i][j], "*", xi[j])
            sum2 = sum2 + A[i][j] * xi[j]
        #print("sum 1 = ", sum1, "sum 2 =", sum2)
        x[i] = (1/A[i][i]) * (b[i] - sum1 - sum2)
        #print("x[", i, "] = ( 1/", A[i][i], ") * (", b[i], "-", sum2, "-", sum1, ")")
        #print("x[", i, "] = ", x[i])

def stopCriteria(x, xi, n, e): #Critério de parada. Se retornar true, o critério foi satisfeito; se false, não foi.
    max = -99999
    for i in range(n):
        tot = abs(x[i] - xi[i])
        #print("tot = x[", i, "] - xi[", i, "] =", x[i], "-", xi[i], "=", tot)
        if(max < tot):
            max = tot
    
    if(max < e):
        return True
    else:
        return False

def gauss_seidel(A, b, xi, x, e, n):
    k = 1 #contador de iterações
    while(k < 25): # limite máximo de iterações
        #print("---ITERAÇÃO ", k)
        iteration(A, b, xi, x, n)

        if(stopCriteria(x, xi, n, e)):
            #print("RESULTADO x = ", x)
            return x
        else:
            k = k + 1
            for i in range(n):
                xi[i] = x[i]

print("Resposta do método Gauss-Seidel:", gauss_seidel(A, b, xi, x, e, n))