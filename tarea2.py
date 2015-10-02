#! /usr/bin/env python

#este es un script que modela el rebote de una pelota
#sobre una superficie que se mueve con una funcion sinusoidal


import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize
from scipy.optimize import brentq

def definiciones(): #crea las variables globales para todas la funciones
    global pos_init
    pos_init = 0
    global vel_init
    vel_init = 15
    global w
    w= 1.79
    global ajt
    ajt = 0


def resta(time):   #calcula la distancia relaiva entre el suelo y la pelota
    global pos_init
    global vel_init
    global w
    return pos_init + (vel_init*tiempoajustado(time)) - (tiempoajustado(time)*tiempoajustado(time)/2) - np.sin(w*time)

def tiempoajustado(t):  #ajuste de tiempo
    global ajt
    return t - ajt

def ajustartiempo(t):  #ajuste temporal
    global ajt
    ajt = t


def choque(coef,velp,vels):   #calcula la velocidad despues del rebote
    return ((1+coef)*vels) - (coef*velp)


def func_cinm(Ns,coef):  #funcion que describe la cinematica del problema
    global vel_init
    global pos_init


    epsilon = 0.01
    t=0;
    nchoques = 0
    dato = resta(t+epsilon)

    vp=0
    vs=0




    tiempo=[]
    vel=[]

    while nchoques<Ns:

        while dato>0  :
            t= t+epsilon
            dato = resta(t)



        tiempo.append(brentq(resta,t-epsilon,t))
        t=tiempo[nchoques]
        vp=(vel_init)-(tiempoajustado(t))
        vs=w*np.cos(w*t)
        vel.append(choque(coef,vp,vs))
        pos_init= np.sin(w*t)
        vel_init= vel[nchoques]
        ajustartiempo(t)
        print vel_init,nchoques
        nchoques+=1
        t=t+epsilon
        dato=resta(t)

    return tiempo , vel


definiciones()



a,b = func_cinm(80,0.15)



x_values = np.linspace(1, 80, 80)
print x_values
plt.figure(1)
plt.clf()
print "velocidades"
print b
plt.plot(x_values, b , label="w = 1,7 " )


plt.xlabel('numero de rebote')
plt.legend()


plt.draw()
plt.show()
