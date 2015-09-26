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
def Ps(t,omega):
    '''
    Entrega la posicion de la membrana en un instante t
    '''
    ps=np.sin(omega*t)
    return ps

def Vs(t,omega):
    '''
    Entrega la velocidad de la membrana en un instante t
    '''
    vs=omega*np.cos(omega*t)
    return omega
def Yp(t,ho,vo):
    g=1
    yp=ho+v0*t+0.5*g*t**2
    return yp
def Vp(t,vo):
    g=1
    vp=v0-gt

def distancia(t):
    '''
    determina la distancia entre la particula y la membrana en un tiempo t
    '''
    d=Ps(t)-Yp(t)
    return d
