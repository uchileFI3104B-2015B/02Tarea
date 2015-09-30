'''
Este es el codigo es el de la tarea 2.
Despues definire si voy a separar los codigos de cada pregunta
o hacerlos todos aqui
'''
import numpy as np
from scipy.optimize import brentq
from scipy.optimize import bisect
import matplotlib.pyplot as plt

def y_suelo(w,t):
    '''
    Ecuacion de posicion de la pelota en funcion del tiempo
    '''
    A=1
    return A * np.sin (w*t)

def v_suelo(w,t):
    '''
    Ecuacion de la velocidad del suelo en funcion del tiempo
    '''
    A=1
    return A * w * np.cos(w*t)

def v_pelota(v0,t):
    '''
    Ecuacion de la velocidad de la pelota en funcion del tiempo
    '''
    g=1
    return v0 - g * t

def y_pelota(y0,v0,t):
    '''
    Ecuacion de posicion de la pelota en funcion del tiempo
    '''
    g=1
    return y0 + v0 * t - 0.5 * g * t**2

def resta(w,t,y0,v0,t_reb):
    '''
    Retorna la distancia que hay entre la pelota y el suelo en un tiempo t
    '''
    A=1
    g=1
    return y_pelota(y0,v0,t-t_reb) - y_suelo(w,t)

def v_despreb(n, vs_reb, vp_reb):
    ''''
    Retorna la velocidad justo despues del rebote
    Recibe la velocidad del suelo y la velocidad de la pelota
    justo antes del rebote
    '''
    A=1
    g=1
    return (1 + n)*vs_reb - n * vp_reb

def nmasuno (w, n, t_reb_n, yn, vn):
    '''
    Retorna los valores de Yn+1 y Vn+1 dados Yn y Vn (la posicion y
    velocidad luego del n-esimo choque). Tambien retorna el valor t*,
    es decir, el tiempo en el que ocurre el choque.
    '''
    def d(t):
        #Necesito que quede solo en funcion de t para poder usar brentq
        return resta (w,t,yn,vn,t_reb_n)

    epsilon=0.01
    t_a = t_reb_n + epsilon #asi empiezo a recorrerde despues del tiempo del rebote n

    while d(t_a) >0:
        t_a+=epsilon

    t_b=t_a-epsilon

    if d(t_a)*d(t_b)>0:
        return [t_a,0,0]
    #while d(t_a)*d(t_b) >0:
    #    if t_b<0:
    #        t_b=t_b+epsilon
    #        break
    #    else:
    #        t_b-=epsilon
    #        print 'b',t_b


    t_reb_n1 = bisect (d, t_a, t_b)  #tiempo del rebote n+1
    #las funciones de posicion estan definidas para un tiempo
    #que se reinicia tras cada rebote
    yn1 = y_pelota (yn, vn, t_reb_n1-t_reb_n)
    vs_reb=v_suelo(w,t_reb_n1)
    vp_reb=v_pelota(vn,t_reb_n1-t_reb_n)
    vn1 = v_despreb(n, vs_reb, vp_reb)
    return [t_reb_n1, yn1, vn1]


n=0.15
y0=0
v0=input('Valor v0? ')

def Nrelax(w,n,y0,v0):
    maxim= 100 #input('Maximo de iteraciones? ')
    N=np.zeros(maxim)
    v_n=np.zeros(maxim)
    y_n=np.zeros(maxim)
    t=np.zeros(maxim)

    i=1
    v_n[0]=v0
    y_n[0]=y0
    while i<maxim:
        vector=nmasuno(w, n, t[i-1], y_n[i-1], v_n[i-1])
        t[i]=vector[0]
        y_n[i]=vector[1]
        v_n[i]=vector[2]
        N[i]=i
        i+=1

    return [N,v_n]

Nrelax166=Nrelax(1.66,n,y0,v0)
Nrelax168=Nrelax(1.68,n,y0,v0)
Nrelax170=Nrelax(1.70,n,y0,v0)

plt.figure(1)
plt.clf()
plt.plot(Nrelax166[0], Nrelax166[1], label='$N_{relax}=1.66$')
plt.plot(Nrelax168[0], Nrelax168[1], label='$N_{relax}=1.68$', color='green')
plt.plot(Nrelax170[0], Nrelax170[1], label='$N_{relax}=1.70$', color='red')


plt.xlabel('Numero de rebotes')
plt.ylabel('Velocidad particula justo despues del rebote')
plt.legend()
plt.grid(True)
plt.savefig("Grafico_")

plt.show()
