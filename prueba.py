import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import brentq
from scipy.optimize import bisect
from scipy.optimize import newton


t_values= np.linspace(0,20,100)
m=1
g=1
A=1
y0=0
v0=5
w=2
n=0.5
a=0.1
b=11

y1=0.74
v1=4.41



def y_p(t,y0, v0):
    return y0 + v0 * t - 0.5*g*(t**2)
#Posicion del suelo
def y_s(t):
    return A * np.sin(-w*t)
#Velocidad del suelo
def vs(t):
    return A*-w*np.cos(w*t)
#Velocidad de la particula antes del choque
def vp(t,v0):
    return v0-g*t
#Velocidad de la particula despues del choque
def v_pd(t,v0):
    return (1+n)*vs(t) - n *vp(t,v0)

def ys_menos_yp(t,y0,v0):
    return y_p(t,y0,v0) - y_s(t)

raiz=brentq(ys_menos_yp, a, b, args=(y0,v0))
t_values2=np.linspace(raiz, 20, 100)
print t_values2

plt.plot(t_values, y_p(t_values,y0,v0), label= 'Posicion pelota')
plt.plot(t_values, y_s(t_values), label= 'Posicion suelo')
plt.plot(t_values2, y_p(t_values,y1,v1), label= 'Posicion pelota 2')



plt.draw()
plt.show()
