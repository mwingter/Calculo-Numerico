# -*- coding: utf-8 -*-
"""BissNewSec (1).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1B1Owz6bUHxAvzmwmig-2NGC8Jy3OABW3
"""

def matprint(mat, fmt="g"):
    col_maxes = [max([len(("{:"+fmt+"}").format(x)) for x in col]) for col in mat.T]
    for x in mat:
        for i, y in enumerate(x):
            print(("{:"+str(col_maxes[i])+fmt+"}").format(y), end="  ")
        print("")
    print("\n")

import numpy as np
from scipy import linalg as lin
import scipy as sci
import math as m
import matplotlib.pyplot as plt

"""# Métodos para encontrar zero de funções

Critérios de parada:
1.   Número máximo de iterações: $k < k_{max}$
2.   Erro absoluto: $\vert x_k - x_{k-1}\vert < \varepsilon_a$
3.   Erro relativo: $\dfrac{\vert x_k - x_{k-1}\vert}{\vert x_k \vert}< \varepsilon_r$
4.   Teste de resíduo: $\vert f(x_k)\vert < \tau$
"""

def bissecao(func,a,b,x0,tol,flag_parada):
    x = x0; erro = np.inf;
    k = 0; kmax = 1000;

    while(erro > tol and k < kmax):
        k = k + 1;
        if(func(a)*func(x) < 0):
            b = x;
        else:
            a = x;
        
        x0 = x;
        x = (a+b)/2;
        
        # cálculo do erro vai depender do critério de parada escolhido
        if(flag_parada == 0):
            erro = abs(x-x0);
        elif(flag_parada == 1):
            erro = abs(x-x0)/abs(x);
        else:
            erro = abs(func(x));
    
    return x, k

f = lambda x: x**3-30*x**2 + 2552
a = 0; b = 20; tol = 1e-6;
x0 = (a+b)/2;

print('Usando o critério de parada do erro absoluto:')
flag_parada = 0;
(x_0,k) = bissecao(f,a,b,x0,tol,flag_parada)
print('O zero da função é %.6f, foram usadas %d iterações\n' %(x_0,k))

print('Usando o critério de parada do erro relativo:')
flag_parada = 1;
(x_1,k) = bissecao(f,a,b,x0,tol,flag_parada)
print('O zero da função é %.6f, foram usadas %d iterações\n' %(x_1,k))

print('Usando o critério de parada do resíduo:')
flag_parada = 2;
(x_2,k) = bissecao(f,a,b,x0,tol,flag_parada)
print('O zero da função é %.6f, foram usadas %d iterações\n' %(x_2,k))

x_array = np.arange(a,b+0.5,0.5)
y_array = f(x_array)

plt.rc('font', size=12)
fig = plt.figure(1,figsize=(12,10),facecolor='white');
ax = fig.gca()
ax.set_xticks(np.arange(a, b+0.1, 1))
ax.set_yticks(np.arange(-1500, 2555, 250))
plt.grid()
plt.plot(x_array,y_array,linewidth='3',zorder=2)
plt.plot(x_array,0*x_array,ls='--',linewidth='3',zorder=1)
plt.scatter(x_1, f(x_1),linewidth='4',facecolor='red',zorder=3)
plt.xlabel('x',fontsize='large') 
plt.ylabel('y',fontsize='large') 
plt.title('Método Bisseção: x = %.6f'%(x_1)) 
plt.show()

def newton(func,dfunc,x0,tol,flag_parada):
    x = x0; erro = erro = np.inf;
    k = 0; kmax = 1000;

    while(erro > tol and k < kmax):
        k = k + 1;
        x0 = x;
        dx = func(x)/dfunc(x);
        x = x - dx;
        
        # cálculo do erro vai depender do critério de parada escolhido
        if(flag_parada == 0):
            erro = abs(x-x0);
        elif(flag_parada == 1):
            erro = abs(x-x0)/abs(x);
        else:
            erro = abs(func(x));
    
    return x, k

f = lambda x: x**3-30*x**2 + 2552
df = lambda x: 3*x**2-60*x
x0 = 3; tol = 1e-6; a = 0; b = 20;

print('Usando o critério de parada do erro relativo:')
flag_parada = 2;
(x_1,k) = newton(f,df,x0,tol,flag_parada)
print('O zero da função é %.6f, foram usadas %d iterações\n' %(x_1,k))

x_array = np.arange(a,b+0.5,0.5)
y_array = f(x_array)

plt.rc('font', size=12)
fig = plt.figure(1,figsize=(12,10),facecolor='white');
ax = fig.gca()
ax.set_xticks(np.arange(a, b+0.1, 1))
ax.set_yticks(np.arange(-1500, 2555, 250))
plt.grid()
plt.plot(x_array,y_array,linewidth='3',zorder=2)
plt.plot(x_array,0*x_array,ls='--',linewidth='3',zorder=1)
plt.scatter(x_1, f(x_1),linewidth='4',facecolor='red',zorder=3)
plt.xlabel('x',fontsize='large') 
plt.ylabel('y',fontsize='large') 
plt.title('Método de Newton: x = %.6f'%(x_1)) 
plt.show()

def secante(func,x0,x1,tol,flag_parada):
    erro = erro = np.inf;
    k = 0; kmax = 1000;
    x = x1;

    while(erro > tol and k < kmax):
        k = k + 1;
        f0 = func(x0)
        f1 = func(x);
        ds = f1*(x-x0)/(f1-f0);
        x0 = x;
        x = x - ds;
        
        # cálculo do erro vai depender do critério de parada escolhido
        if(flag_parada == 0):
            erro = abs(x-x0);
        elif(flag_parada == 1):
            erro = abs(x-x0)/abs(x);
        else:
            erro = abs(func(x));
    
    return x, k

f = lambda x: x**3-30*x**2 + 2552
x0 = 3; tol = 1e-6;
a = 0; b = 20;

# vamos fazer uma iteração da bisseção para achar x1
if(f(a)*f(x0) < 0):
    b = x0;
else:
    a = x0;       
x1 = (a+b)/2;

print('Usando o critério de parada do erro relativo:')
flag_parada = 1;
(x_1,k) = secante(f,x0,x1,tol,flag_parada)
print('O zero da função é %.6f, foram usadas %d iterações\n' %(x_1,k))

x_array = np.arange(a,b+0.5,0.5)
y_array = f(x_array)

plt.rc('font', size=12)
fig = plt.figure(1,figsize=(12,10),facecolor='white');
ax = fig.gca()
ax.set_xticks(np.arange(a, b+0.1, 1))
ax.set_yticks(np.arange(-1500, 2555, 250))
plt.grid()
plt.plot(x_array,y_array,linewidth='3',zorder=2)
plt.plot(x_array,0*x_array,ls='--',linewidth='3',zorder=1)
plt.scatter(x_1, f(x_1),linewidth='4',facecolor='red',zorder=3)
plt.xlabel('x',fontsize='large') 
plt.ylabel('y',fontsize='large') 
plt.title('Método da secante: x = %.6f'%(x_1)) 
plt.show()

"""Comparando os três métodos para função $f(x) = x^3-30x^2+2552$"""

f = lambda x: x**3-30*x**2 + 2552
df = lambda x: 3*x**2-60*x
x0 = 10; tol = 1e-6; a = 0; b = 20;
flag_parada = 1 # vamos manter o erro relativo em todos!
# vamos fazer uma iteração da bisseção para achar x1
a_new = a; b_new = b;
if(f(a_new)*f(x0) < 0):
    b_new = x0;
else:
    a_new = x0;       
x1 = (a_new+b_new)/2;

print('Bisseção:')
(x_biss,k_biss) = bissecao(f,a,b,x0,tol,flag_parada)
print('O zero da função é %.6f, foram usadas %d iterações\n' %(x_biss,k_biss))

print('Newton:')
(x_newt,k_newt) = newton(f,df,x0,tol,flag_parada)
print('O zero da função é %.6f, foram usadas %d iterações\n' %(x_newt,k_newt))

print('Secante:')
(x_sec,k_sec) = secante(f,x0,x1,tol,flag_parada)
print('O zero da função é %.6f, foram usadas %d iterações\n' %(x_sec,k_sec))

"""Agora vamos pegar a função $f(x) = x^3-5x$ e vamos testar com esses três métodos."""

f = lambda x: x**3-5*x;
a = -3; b = 3;

x_array = np.arange(a,b+0.5,0.1)
y_array = f(x_array)

plt.rc('font', size=12)
fig = plt.figure(1,figsize=(14,8),facecolor='white');
ax = fig.gca()
ax.set_xticks(np.arange(a, b+0.1, 0.5))
ax.set_yticks(np.arange(-20, 30, 5))
plt.grid()
plt.plot(x_array,y_array,linewidth='3',zorder=2)
plt.plot(x_array,0*x_array,ls='--',linewidth='3',zorder=1)
plt.scatter([0.5,3], [f(0.5),f(3)],linewidth='4',facecolor='red',label = 'Intervalo para bisseção',zorder=3)
plt.xlabel('x',fontsize='large') 
plt.ylabel('y',fontsize='large') 
plt.title('Função') 
plt.legend() 
plt.show()

f = lambda x: x**3-5*x;
df = lambda x: 3*x**2-5
x0 = 2.0; tol = 1e-6; a = 0.5; b = 3; # variar os chutes iniciais (1.0, 1.5, 2.0)
flag_parada = 1; # manter erro relativo para todos!
# vamos fazer uma iteração da bisseção para achar x1 do método da secante
a_new = a; b_new = b;
if(f(a_new)*f(x0) < 0):
    b_new = x0;
else:
    a_new = x0;       
x1 = (a_new+b_new)/2;

print('Bisseção:')
(x_biss,k_biss) = bissecao(f,a,b,x0,tol,flag_parada)
print('O zero da função é %.6f, foram usadas %d iterações\n' %(x_biss,k_biss))

print('Newton:')
(x_newt,k_newt) = newton(f,df,x0,tol,flag_parada)
print('O zero da função é %.6f, foram usadas %d iterações\n' %(x_newt,k_newt))

print('Secante:')
(x_sec,k_sec) = secante(f,x0,x1,tol,flag_parada)
print('O zero da função é %.6f, foram usadas %d iterações\n' %(x_sec,k_sec))

f = lambda x: x**3-5*x;
a = -3; b = 3;

x_array = np.arange(a,b+0.5,0.1)
y_array = f(x_array)

plt.rc('font', size=12)
fig = plt.figure(1,figsize=(14,8),facecolor='white');
ax = fig.gca()
ax.set_xticks(np.arange(a, b+0.1, 0.5))
ax.set_yticks(np.arange(-20, 30, 5))
plt.grid()
plt.plot(x_array,y_array,linewidth='3',zorder=2)
plt.plot(x_array,0*x_array,ls='--',linewidth='3',zorder=1)
plt.scatter([-2.0,0.5], [f(-2.0),f(0.5)],linewidth='4',facecolor='red',label = 'Intervalo para bisseção',zorder=3)
plt.xlabel('x',fontsize='large') 
plt.ylabel('y',fontsize='large') 
plt.title('Função') 
plt.legend() 
plt.show()

f = lambda x: x**3-5*x;
df = lambda x: 3*x**2-5
x0 = -0.5; tol = 1e-8; a = -2.0; b = 0.5; # variar os chutes iniciais (-1.5, -1.0, -0.5)
flag_parada = 0; # Usar erro absoluto pois está dando divisão por zero aqui
# vamos fazer uma iteração da bisseção para achar x1 do método da secante
a_new = a; b_new = b;
if(f(a_new)*f(x0) < 0):
    b_new = x0;
else:
    a_new = x0;       
x1 = (a_new+b_new)/2;

print('Bisseção:')
(x_biss,k_biss) = bissecao(f,a,b,(a+b)/2,tol,flag_parada)
print('O zero da função é %.6f, foram usadas %d iterações\n' %(x_biss,k_biss))

print('Newton:')
(x_newt,k_newt) = newton(f,df,x0,tol,flag_parada)
print('O zero da função é %.6f, foram usadas %d iterações\n' %(x_newt,k_newt))

print('Secante:')
(x_sec,k_sec) = secante(f,x0,x1,tol,flag_parada)
print('O zero da função é %.6f, foram usadas %d iterações\n' %(x_sec,k_sec))

"""1. Dada a função $f(x) = x\sin(x) - 1$ no intervalo $(0,2)$ resolva:
> 1.   Usando uma iteração do método da bisseção para achar o chute inicial, resolva essa equação com o método de Newton.
> 2.   Usando duas iterações do método da bisseção, encontre dois chutes iniciais e resolva a equação usando o método das Secantes.
> 3. Resolva também com o método da bisseção e compare as três soluções.
"""

f = lambda x: x*np.sin(x) - 1;
df = lambda x: np.sin(x) + x*np.cos(x);
a = 0; b = 2; tol = 1e-6;
# print(f(a));
# print(f(b));

print('Vamos visualizar a função:')
x_array = np.arange(a,b+0.0005,0.01)
y_array = f(x_array)

plt.rc('font', size=12)
fig = plt.figure(1,figsize=(12,8),facecolor='white');
ax = fig.gca()
ax.set_xticks(np.arange(a, b+0.0005, 0.1))
ax.set_yticks(np.arange(-1, 1, 0.1))
plt.grid()
plt.plot(x_array,y_array,linewidth='3',zorder=2)
plt.plot(x_array,0*x_array,ls='--',linewidth='3',zorder=1)
# plt.scatter([-2.0,0.5], [f(-2.0),f(0.5)],linewidth='4',facecolor='red',label = 'Intervalo para bisseção',zorder=3)
plt.xlabel('x',fontsize='large') 
plt.ylabel('y',fontsize='large') 
plt.title('Função') 
# plt.legend() 
plt.show()

print('\nCalculando dois passos do método da bisseção para chutes iniciais:')
a_new = a; b_new = b; x0_biss = (a_new+b_new)/2;
if(f(a_new)*f(x0_biss) < 0):
    b_new = x0_biss;
else:
    a_new = x0_biss;       
x0 = (a_new+b_new)/2;
x0_biss = x0;
if(f(a_new)*f(x0_biss) < 0):
    b_new = x0_biss;
else:
    a_new = x0_biss;       
x1 = (a_new+b_new)/2;
print('Primeiro chute inicial: %.4f' %(x0));
print('Segundo chute inicial: %.4f' %(x1));

print('\nCalculando com método de Newton:')
(x_newt,k_newt) = newton(f,df,x0,tol,1)
print('O zero da função é %.6f, foram usadas %d iterações' %(x_newt,k_newt))

print('\nCalculando com método da secante:')
(x_sec,k_sec) = secante(f,x0,x1,tol,1)
print('O zero da função é %.6f, foram usadas %d iterações' %(x_sec,k_sec))

print('\nCalculando com método da bisseção:')
(x_biss,k_biss) = bissecao(f,a,b,x0,tol,1)
print('O zero da função é %.6f, foram usadas %d iterações' %(x_biss,k_biss))