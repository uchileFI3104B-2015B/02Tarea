#Tarea 2

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import brentq
from scipy.optimize import bisect
from scipy.optimize import newton


plt.figure(1)
plt.clf()
#definimos una funcion de posicion y velocidad del suelo
def y_suelo(A, w, t):
    return A*np.sin(w*t)
def v_suelo(A, w, t):
    return A*w*np.cos(w*t)
#definimos funciones de posicion y velocidad para la pelota
def y_pelota(y0, v0, t):
    return y0 + v0*t -(g*(t**2))/2
def v_pelota(v0, t):
    return v0 -g*t
# p menos s calcula la distancia entre la pelota y el suelo
def p_menos_s(y0, v0, t, A, w):
    return y_pelota(y0, v0, t) - y_suelo(A, w, t)
# v choque es la velocidad despues del choque
def v_choque(vs, vp):
    return (1+nu)*vs-nu*vp


def N(Yn,Vn,w,A,tn):
    '''
    Devuelve la posicion(Y_{n+1}) y la velocidad(V_{n+1})
    de la particula luego del choque n ademas del tiempo de choque
    en un vector de la forma [Yn+1,Vn+1,t]
    '''
    def p_s(t):
        d=p_menos_s(y0, v0, t, A, w)
        return d

    delta=0.001
    t1=tn+delta
    t2=tn+2*delta
    while (p_s(t1)*p_s(t2)>0.0):
            t1=t1+delta
            t2=t2+delta

    tn1 = brentq(p_s,t1,t2)
    Yn1 = y_pelota(tn1-delta,Yn,Vn)
    vs = v_suelo(tn1,w,A)
    vp = v_pelota(tn1-delta,Vn)
    Vn1 = v_choque(vs,vp)
    r=[Yn1,Vn1,tn1]
    return r
#definimos las variables de las cuales depende el problema
m=1
A=1
w=1
nu=1
y0=0
v0=2
g=1
def yp(t):
    return y0 + v0*t -(g*(t**2))/2
def ys(t):
    return A*np.sin(w*t)
Choque_n1=N(y0,v0,w,A,0)
print Choque_n1

xt = np.linspace(0, 4*np.pi, 100)
plt.plot(xt, ys(xt), label='suelo')
plt.plot(xt, yp(xt), label='pelota')

plt.xlabel('x [segundos]')
plt.legend()
plt.show()
