
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import brentq


plt.figure(1)
plt.clf()


a=1
A=1
phi=0
w=1.66
vo=2
yo=0
n=0.01
def y_p(t):
    '''funcion que me da la posicion de la masa'''
    yp=yo + vo*t -(0.5)*a*t**2
    return yp

def v_p(t):
    ''' funcion velocidad de la particula'''
    vp=vo - a*t**2
    return vp

def y_s(t):
    '''funcion que me da el movimiento del suelo (sinusoidal)'''
    ys=A*np.sin(w*t+phi)
    return ys
def v_s(t):
    '''velocidad del suelo'''
    vs=A*w*np.cos(w*t+phi)
    return vs

t=np.linspace(0,4*np.pi,100)

plt.plot(t,y_s(t),color='r')
plt.plot(t,y_p(t),color='b')
#plt.show()


def v_dr(t):
    ''' funcion de rebote'''
    vdr= (1+n)*v_s(t)-n*v_p(t)
    return vdr

def choque(t):
    ''' cuando chocan la diferencia de la resta debe ser cero'''
    choque=y_p(t)-y_s(t)
    return choque


'''for i in range(len(t-1)):
    if choque(t[i])<0:
        print i
        raiz_brentq=brentq(choque,t[i-1],t[i])
        break
'''
#plt.axvline(raiz_brentq, color='g')
plt.plot(t,y_s(t),color='r')
#plt.plot(t,y_p(t),color='b')
plt.show()
print 'oli'
