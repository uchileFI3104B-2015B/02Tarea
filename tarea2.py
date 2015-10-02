#! /usr/bin/env python




import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize
from scipy.optimize import brentq

def definiciones():
    global pos_init
    pos_init = 0
    global vel_init
    vel_init = 15
    global w
    w= 1.79
    global ajt
    ajt = 0


def resta(time):
    global pos_init
    global vel_init
    global w
    return pos_init + (vel_init*tiempoajustado(time)) - (tiempoajustado(time)*tiempoajustado(time)/2) - np.sin(w*time)

def tiempoajustado(t):
    global ajt
    return t - ajt

def ajustartiempo(t):
    global ajt
    ajt = t


def choque(coef,velp,vels):
    return ((1+coef)*vels) - (coef*velp)


def func_cinm(Ns,coef):
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

# func_cinm(500,0.15)

a,b = func_cinm(80,0.15)
#print a
#print b


x_values = np.linspace(1, 80, 80)
print x_values
plt.figure(1)
plt.clf()
print "velocidades"
print b
#plt.plot(x_values, b , label="w = 1,7 " )
#plt.plot(x_values, np.cos(x_values), label='cos(x)')

#plt.xlabel('numero de rebote')
#plt.legend()


#plt.draw()
#plt.show()
