import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from scipy.optimize import brentq

def Vprima(t,nu,vs,vp):
    '''
    Recive el valor de la velocidad del suelo y de la particula
    justo antes del choque y devuelve el valor de la velocidad
    de la particual un instante despues
    '''
    vpp=(1+nu)*vs-nu*vp
    return vpp
def Ps(t,omega,A):
    '''
    Entrega la posicion de la membrana en un instante t
    '''
    ps=np.sin(omega*t)
    return ps

def Vs(t,omega,A):
    '''
    Entrega la velocidad de la membrana en un instante t
    '''
    vs=omega*np.cos(omega*t)
    return omega
def Yp(t,h0,v0):
    g=1
    yp=h0+v0*t-0.5*g*t**2
    return yp
def Vp(t,v0):
    g=1
    vp=v0-g*t
    return vp

def distancia(t,omega,A,h0,v0):
    '''
    determina la distancia entre la particula y la membrana en un tiempo t
    '''
    d=Ps(t,omega,A)-Yp(t,h0,v0)
    return d



def ChoqueN(Yn,Vn,omega,A,nu):
    '''
    Devuelve la posicion(Y_{n+1}) y la velocidad(V_{n+1})
    de la particula luego del choque n ademas del tiempo de choque
    en un vector de la forma [Yn+1,Vn+1,t]
    '''
    def distanciat(t):
        d=distancia(t,omega,A,h0,v0)
        return d

    tm=2*Vn # tiempo estimado de choque de la particula con la menbrana
    delta=0.5
    t_eff=brentq(distanciat,tm-delta,tm+delta)
    Yn1=Yp(t_eff,Yn,Vn)
    vs=Vs(t_eff,omega,A)
    vp=Vp(t_eff,Vn)
    Vn1=Vprima(t_eff,nu,vs,vp)
    r=[Yn1,Vn1,t_eff]
    return r


t_values= np.linspace(0,100,1000)
omega=1.66
A=1
nu=0.15
h0=0
v0=10

plt.figure(1)
plt.clf()



plt.plot(t_values, Yp(t_values,h0,v0), label='particula')
plt.plot(t_values, Ps(t_values,omega,A), label='membrana')


plt.legend()

cero=ChoqueN(h0,v0,omega,A,nu)
plt.axvline(cero[2], color='b')

plt.draw()
plt.show()
