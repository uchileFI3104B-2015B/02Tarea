import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import brentq
from scipy.optimize import bisect
from scipy.optimize import newton


t_values= np.linspace(0,20,50)
m=1
g=1
A=1
y0=0
v0=10
w=2
n=0.5
a=0.1
b=(v0 + (((v0**2)+2*(1+y0))**0.5) )
t0=0


def y_p(t,y,v):
    return y + v * t - 0.5*g*(t**2)
#Posicion del suelo
def y_s(t,td):
    return A * np.sin(w*(t+td))
#Velocidad del suelo
def v_s(t,td):
    return A*w*np.cos(w*(t+td))
#Velocidad de la particula antes del choque
def v_p(t,v):
    return v-g*t
#Velocidad de la particula despues del choque
def v_pd(t,v,td):
    return (1+n)*v_s(t,td) - n *v_p(t,v)

def ys_menos_yp(t,y,v,td):
    return y_s(t,td) - y_p(t,y,v)

raiz1= brentq(ys_menos_yp, a, b , args=(y0,v0,t0))
#print raiz1
plt.axvline(raiz1, color='r')

vs=v_s(raiz1,t0)
print vs

a2= 0.1
b2= (v0 + (((v0**2)+2*(1+y0))**0.5) )

#print a2
#print b2
#print ys_menos_yp(a2,y1,v1)
#print ys_menos_yp(,y1,v1)

#plt.axhline(sha, color='r')
#plt.axhline(shi, color='b')
#plt.axhline(shu, color='g')
#plt.axhline(a2, color='b')
'''
y1=y_p(raiz1,y0,v0)
vs=v_s(raiz1)
vp=v_p(raiz1,v0)
v1=(1+n)*vs - n *vp
t1=raiz1

raiz2=brentq(ys_menos_yp, a2, b2, args=(y1,v1,t1))
print raiz2
#plt.axvline(raiz2, color='b')

y2=y_p(raiz2,y1,v1)
vs1=v_s(raiz2)
vp1=v_p(raiz2,v1)
v2=(1+n)*vs1 - n *vp1
t2=raiz2

b3= (v1 + (((v1**2)+2*(1+y1))**0.5) )


raiz3=brentq(ys_menos_yp, a2, b3, args=(y2,v2,t2))
print raiz3
#plt.axvline(raiz3, color='g')

'''

plt.plot(t_values, y_p(t_values,y0,v0), label= 'Posicion pelota')
plt.plot(t_values, y_s(t_values,0), label= 'Posicion suelo')
#plt.plot(t_values, y_p(t_values,y1,v1), label= 'Posicion pelota 2')
#plt.plot(t_values, y_p(t_values,y2,v2), label= 'Posicion pelota 3')
#plt.plot(t_values, y_s(t_values,raiz1))
#plt.plot(t_values,y_s(t_values,raiz2))



plt.draw()
plt.show()
