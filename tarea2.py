'''
Este es el codigo es el de la tarea 2.
Despues definire si voy a separar los codigos de cada pregunta
o hacerlos todos aqui
'''
import numpy as np
from scipy.optimize import brentq
import matplotlib.pyplot as plt

def y_suelo(A,w,t):
    '''
    Ecuacion de posicion de la pelota en funcion del tiempo
    '''
    return A * np.sin (w*t)

def v_suelo(A,w,t):
    return A * w * np.cos(w*t)

def v_pelota(v0,g,t):
    return v0-gt

def y_pelota(y0,v0,t,g):
    '''
    Ecuacion de posicion de la pelota en funcion del tiempo
    '''
    return y0 + v0 * t - 0.5 * g * t**2

def resta(A,w,t,y0,v0,g):
    return y_suelo(A,w,t) - y_pelota(y0,v0,t,g)

A=1
g=1
n=1
y0=0
N=100
t=np.linspace(0,np.pi/4, N)
v0=10
w=1.66

def v_despreb(n, A, w, t_reb, v0, g):
    return (1 + n)*v_suelo(A, w, t_reb) - n * v_pelota(v0,g,t_reb)

#para usar el metodo de brentq necesito entregarle una funcion,
#un tiempo anterior al cero y un tiempo posterior al cero.
#por eso debo definirlos (t_a y t_b)

#t_a=0
#t_b=10

#t_reb = brentq(resta, t_a, t_b)

arreglo_posc_pel=np.zeros(N-1)
REB=0 #numero rebotes

'''for i in range(N):
    if resta(A,w,t[i],y0,v0,g)*resta(A,w,t[i+1],y0,v0,g) <=0:
        t_reb = brentq (resta, t[i], t[i+1])
        y0 = y_pelota (y0,v0,t_reb,g)
        v0 = v_despreb(n,A,w,r_reb,v0,g)
        REB+=1
        arreglo_posc_pel[i]= y0

    else:
        arreglo_posc_pel[i] = y_pelota(y0,v0,t_reb,g)

plt.figure(1)
plt.clf()
plt.plot(t, y_suelo, label='Suelo')
plt.plot(t, arreglo_posc_pel, label='Pelota')

plt.xlabel('tiempo')
plt.ylabel('posicion')
plt.legend()

show()
'''

for i in range(N-1):
    if resta(A,w,t[i],y0,v0,g)*resta(A,w,t[i+1],y0,v0,g) <=0:
        t_reb = brentq (resta, t[i], t[i+1])

plt.figure(1)
plt.clf()
plt.plot(t, y_suelo, label='Suelo')
plt.plot(t, arreglo_posc_pel, label='Pelota')
plt.axvline(t_reb,color='g')

plt.xlabel('tiempo')
plt.ylabel('posicion')
plt.legend()
