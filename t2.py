
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import brentq
from scipy.optimize import newton


plt.figure(1)


'''-----parte 1 -----------'''

def y_p(t,vo,yo):
    '''funcion que me da la posicion de la masa'''
    yp=yo + vo*t -(0.5)*g*t**2
    return yp

def v_p(t,vo):
    ''' funcion velocidad de la particula g=1 asi que omitimos'''

    vp=vo -t**2
    return vp

def y_s(t,w,phi):
    '''funcion que me da el movimiento del suelo (sinusoidal)'''
    ys=np.sin(w*t+phi)
    return ys
def v_s(t,w,phi):
    '''velocidad del suelo'''
    vs=w*np.cos(w*t+phi)
    return vs

def v_dr(t,w,vo,n,phi):
    ''' funcion velocidad despues del de rebote'''
    vdr= (1+n)*v_s(t,w,phi)-n*v_p(t,vo)
    return vdr

def resta_posicion(t,vn,yn,w,phi):
    ''' cuando chocan la diferencia de la resta debe ser cero'''
    choque=y_p(t,vo,yo)-y_s(t,w,phi)
    return choque

def valorenesimo(yn,vn,w):
    def restat(t):
        return resta_posicion(t,vn,yn,w,phi)

    taprox=np.fabs(2*vo/g)

    ''' esto viene de t= 2*vo*sen(a)/g
    en un lanzamiento de proyectil'''

    delta= 0.1
    t1=taprox -delta
    t2=taprox + delta
    while restat(t2)>0 and y_p(t2,vn,yn)<y_s(t2,vn,yn):
        t2+=delta

    tn1=brentq(restat,t1-delta,t2)
    yn1=y_p(tn1,yo,vo)
    vs=v_s(tn1,w,yn1)
    vp=v_p(tn1,vo)
    vn1=v_dr(tn1,w,vp,n,phi)
    a=(tn1,yn1,vn1)
    #print a
    return a

g=1
phi=0
yo=0
w=1.66
vo=2
yo=0
n=0.15
p=valorenesimo(yo,vo,w)
print "valores de tiempo rebote,posicion y velocidad de la pelota",
print p
tn1=p[0]


t=np.linspace(0,4*np.pi,100)
plt.xlabel('$tiempo [s]$')
plt.ylabel('$posicion [m]$ ')
plt.title('$puntos \ de \ choque \ de \ la \ pelota \ con \ el \ suelo$')
plt.savefig("figura1.png")
plt.axvline(tn1, color='g')
plt.plot(t,y_s(t,w,phi),color='r')
plt.plot(t,y_p(t,vo,yo),color='b')
plt.show()
