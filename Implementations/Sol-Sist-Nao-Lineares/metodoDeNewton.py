import numpy as np

#import numdifftools as nd

#importando o arquivo python de resolução de sistemas lineares
import sys
sys.path.insert(0, '../Sol-Sistemas-Lineares/')
import gaussElimination

n = 2 #numero de elementos em x
xi = np.array([-1, 6]) #vetor aproximação inicial
F = np.array([[1,1,-5],[1,1,-25]])
e = 0.1 #erro e


"""
def toJacobian(f, x, dx=1e-8, n):
    func = f(x)
    jac = np.zeros((n, n))
    for j in range(n):  # through columns to allow for vector addition
        Dxj = (abs(x[j])*dx if x[j] != 0 else dx)
        x_plus = [(xi if k != j else xi + Dxj) for k, xi in enumerate(x)]
        jac[:, j] = (f(x_plus) - func)/Dxj
    return jac
"""

def toJacobian(f, x, n):
    J = np.zeros((n, n))

    for i in range(n): #para cada linha
        for j in range(n): #para cada coluna
            for k in range(n): #para cada x (x1, x2, x3, etc) -> por ex se n=2, temos x1 e x2
                if(i == k): 
                    J[i][j] = f[i][j] * (i+1) * (x[j] ** i) ##derivando e ja substituindo x
                    print("J[", i, "][", j, "] =", f[i][j], "*", (i+1), "*", x[j],  "^", i, "=", J[i][j])

    print("J = ", J)
    return J

def stopCriteria(x, xi, n, e): #Critério de parada. Se retornar true, o critério foi satisfeito; se false, não foi.
    max = -99999
    for i in range(n):
        tot = abs(x[i] - xi[i])
        if(max < tot):
            max = tot  
    if(max < e):
        return True
    else:
        return False

def iteration_newton(n, xi, F, e):
    Jx = np.zeros((n,n)) #(A) matriz n x n cheia de zeros 
    Fx = np.zeros(n) #(b) vetor de tamanho n cheia de zeros 

    #encontrando o sistema Ax=b 
    for i in range(n): #Encontrando o 'b' (Fx)
        Fx[i] = F[i][n]
        for j in range(n):
            Fx[i] = Fx[i] + F[i][j] * (xi[j] ** (i+1))
    print("Achei o Fx = ", Fx)
    Jx = toJacobian(F, xi, n) #encontrando o 'A' (Jx)

    y = gaussElimination.gauss(Jx, -Fx, n) #gauss(A,b,n) resolvendo o sistema linear A.x=b (ou Jx.x=-Fx) usando o metodo da eliminação de gauss
    print("y = ", y)
    print("xi = ", xi)

    x = xi + y
    print("x = xi + y = ", x)

    return x

def newton(n, xi, F, e):
    k = 1 #contador de iterações
    while (k < 25):
        print("---ITERAÇÃO ", k)
        x = iteration_newton(n, xi, F, e)
        if(stopCriteria(x, xi, n, e)):
            return x
        else:
            k = k + 1
            for i in range(n):
                xi[i] = x[i]

print("Resultado do Método de Newton:", newton(n,xi,F,e))