#Tarea 2

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import brentq
from scipy.optimize import bisect
from scipy.optimize import newton


plt.figure(1)
plt.clf()
#definimos una funcion de posicion y velocidad del suelo
def y_suelo(w, t):
    return A*np.sin(w*t)
def v_suelo(w, t):
    return A*w*np.cos(w*t)
#definimos funciones de posicion y velocidad para la pelota
def y_pelota(y0, v0, t):
    return y0 + v0*t -(g*(t**2))/2
def v_pelota(v0, t):
    return v0 -g*t
# p menos s calcula la distancia entre la pelota y el suelo
def p_menos_s(y0, v0, t, tn, w):
    return y_pelota(y0, v0, t-tn) - y_suelo(w, t)
# v choque es la velocidad despues del choque
def v_choque(vs, vp):
    return (1+n)*vs-n*vp


def N(Yn,Vn,w,tn):
    '''
    Devuelve la posicion y velocidad del proximo choque
    dandole la velocidad, la posicion y tiempo del choque
    anterior
    '''
    def p_s(t):
        d=p_menos_s(Yn, Vn, t, tn, w)
        return d

    delta=0.01
    t1=tn
    p1=p_s(t1)
    p2=p_s(t1+delta)
    #print("Pos1: "+str(p1)+" Pos2: "+str(p2))
    while p2>0.0:
        t1=t1+delta
        p1=p2
        p2=p_s(t1+delta)
        #print("Pos1: "+str(p1)+" Pos2: "+str(p2))
    if p1>0.0:
        tn1 = brentq(p_s,t1,t1+delta)
    else:
        tn1 = t1
    Yn1 = y_pelota(Yn,Vn,tn1-tn-delta)
    vs = v_suelo(w, tn1-delta)
    vp = v_pelota(Vn, tn1-tn-delta)
    Vn1 = v_choque(vs,vp)
    r=[Yn1,Vn1,tn1]
    return r
#definimos las variables de las cuales depende el problema
m=1
A=1
w=1.7
n=0.15
y0=0
v0=2
g=1

def Nchoque(w, c):
    i=0
    Y=[0]
    V=[2]
    T=[0]
    while i<c:
        Ni=N(Y[i],V[i],w,T[i])
        T.append(Ni[2])
        V.append(Ni[1])
        Y.append(Ni[0])
        i+=1
    return V
Speed=Nchoque(1.66, 100)
Speed1=Nchoque(1.68, 100)
Speed2=Nchoque(1.7, 100)

choque= np.linspace(0,100,101)
plt.plot(choque, Speed, label='w=1.66')
plt.plot(choque, Speed1, label='w=1.68')
plt.plot(choque, Speed2, label='w=1.7')
plt.ylabel('Velocidades')
plt.xlabel('Numero de Choques')
plt.legend()

plt.show()
