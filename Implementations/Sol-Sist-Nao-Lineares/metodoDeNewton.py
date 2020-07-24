from sympy import *
import numpy as np

import sys
sys.path.insert(0, '../Sol-Sistemas-Lineares/')
import gaussElimination

n = 2 #numero de elementos em x
xi = np.array([-1, 6]) #vetor aproximação inicial
F = np.array([[1,1,-5],[1,1,-25]])
e = 0.1 #erro e


def toJacobian(f, x, dx=1e-8, n):
    func = f(x)
    jac = np.zeros((n, n))
    for j in range(n):  # through columns to allow for vector addition
        Dxj = (abs(x[j])*dx if x[j] != 0 else dx)
        x_plus = [(xi if k != j else xi + Dxj) for k, xi in enumerate(x)]
        jac[:, j] = (f(x_plus) - func)/Dxj
    return jac

def iteration_newton(n, xi):
    Jx = np.zeros((n,n)) #(A) matriz n x n cheia de zeros 
    Fx = np.zeros(n) #(b) vetor de tamanho n cheia de zeros 
    y = np.zeros(n) #(x)
    #encontrando o sistema Ax=b 
    for i in range(n): #Encontrando o 'b' (Fx)
        Fx[i] = F[i][n]
        for j in range(n):
            Fx[i] = Fx[i] + F[i][j] * (xi[j] ** (i+1))
    print(Fx)
    toJacobian() #encontrando o 'A' (Jx)

    x = gaussElimination.gauss(A, b, n) #resolvendo o sistema linear A.x=b ou Jx.x=Fx

    x = x + y
    return x


def newton(n, xi, e):
    k = 1 #contador de iterações
    while (k < 25):
        print("---ITERAÇÃO ", k)
        x = iteration_newton(n, xi)
        k = k + 1
        for i in range(n):
            xi = x


