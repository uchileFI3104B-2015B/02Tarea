import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from scipy.optimize import brentq


#---------------------------------Parte 1 -------------------------------------#
def Vprima(nu,vs,vp):
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
    ps=A*np.sin(omega*t)
    return ps

def Vs(t,omega,A):
    '''
    Entrega la velocidad de la membrana en un instante t
    '''
    vs=A*omega*np.cos(omega*t)
    return omega


def Yp(t,h0,v0):
    g=1
    yp=h0+v0*t-0.5*g*t**2
    return yp
def Vp(t,v0):
    g=1
    vp=v0-g*t
    return vp

def distancia(t,omega,A,h0,v0,tc):
    '''
    determina la distancia entre la particula y la membrana en un tiempo t
    '''
    d=Ps(t,omega,A)-Yp(t-tc,h0,v0)
    return d



def ChoqueN(Yn,Vn,omega,A,nu,tc):
    '''
    Devuelve la posicion(Y_{n+1}) y la velocidad(V_{n+1})
    de la particula luego del choque n ademas del tiempo de choque
    en un vector de la forma [Yn+1,Vn+1,t]
    '''
    def distanciat(t):
        d=distancia(t,omega,A,h0,v0,tc)
        return d

    tm=Vn+np.sqrt(Vn**2+2*np.fabs(Yn))+tc
    delta=0.001
    t1=tm-delta
    t2=tm+delta
    while (distanciat(t1)*distanciat(t2)>0.0):
            t1=t1-delta
            t2=t2+delta


    t_eff=brentq(distanciat,t1,t2)
    Yn1=Yp(t_eff-tc,Yn,Vn)
    vs=Vs(t_eff,omega,A)
    vp=Vp(t_eff-tc,Vn)
    Vn1=Vprima(nu,vs,vp)
    r=[Yn1,Vn1,t_eff]
    return r



omega=1.7
A=1.0
nu=0.15
h0=0.0
v0=100

cero=ChoqueN(h0,v0,omega,A,nu,0)
t_values= np.linspace(0,2*cero[2],100)
plt.figure(1)
plt.clf()



plt.plot(t_values, Yp(t_values,h0,v0), label='particula')
plt.plot(t_values, Ps(t_values,omega,A), label='membrana')


plt.legend()


plt.axvline(cero[2], color='b')

plt.draw()
plt.show()
#---------------------------------Parte 2-3 -------------------------------------#
def Nrelax(fin,omega):
    i=0
    P=[h0]
    V=[v0]
    tc=[0]
    while i<fin:
        vec=ChoqueN(P[i],V[i],omega,A,nu,tc[i])
        P+=[vec[0]]
        V+=[vec[1]]
        tc+=[vec[2]]
        i+=1
        print V[i]
    return V

Velocidades1=Nrelax(10,1.66)
Velocidades2=Nrelax(10,1.67)
Velocidades3=Nrelax(10,1.68)
Velocidades4=Nrelax(10,1.69)
Velocidades5=Nrelax(10,1.70)

plt.figure(2)
plt.clf()

N=np.linspace(0,10,11)

plt.plot(N,Velocidades1, label='$N_{relax}\;\omega=1.66$')
plt.plot(N,Velocidades2, label='$N_{relax}\;\omega=1.67$')
plt.plot(N,Velocidades3, label='$N_{relax}\;\omega=1.68$')
plt.plot(N,Velocidades4, label='$N_{relax}\;\omega=1.69$')
plt.plot(N,Velocidades5, label='$N_{relax}\;\omega=1.70$')

plt.legend()

plt.draw()
plt.show()
