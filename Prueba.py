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

    t1=Vn+np.sqrt(Vn**2+2*Yn)+tc
    t2=Vn+np.sqrt(Vn**2+2*Yn)+tc
    delta=0.001
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
v0=10.0

N1=ChoqueN(h0,v0,omega,A,nu,0)
N2=ChoqueN(N1[0],N1[1],omega,A,nu,N1[2])
N3=ChoqueN(N2[0],N2[1],omega,A,nu,N2[2])
N4=ChoqueN(N3[0],N3[1],omega,A,nu,N3[2])
N5=ChoqueN(N4[0],N4[1],omega,A,nu,N4[2])
N6=ChoqueN(N5[0],N5[1],omega,A,nu,N5[2])
N7=ChoqueN(N6[0],N6[1],omega,A,nu,N6[2])
N8=ChoqueN(N7[0],N7[1],omega,A,nu,N7[2])
N9=ChoqueN(N8[0],N1[1],omega,A,nu,N8[2])
N10=ChoqueN(N9[0],N2[1],omega,A,nu,N9[2])
N11=ChoqueN(N10[0],N3[1],omega,A,nu,N10[2])
N12=ChoqueN(N11[0],N4[1],omega,A,nu,N11[2])
N13=ChoqueN(N12[0],N5[1],omega,A,nu,N12[2])
N14=ChoqueN(N13[0],N6[1],omega,A,nu,N13[2])
N15=ChoqueN(N14[0],N7[1],omega,A,nu,N14[2])
