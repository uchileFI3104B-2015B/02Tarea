'''
Este script...
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq
from scipy.optimize import newton
from scipy.optimize import bisect
#Parámetros del problema
m=1
g=1
A=1
w=2
n=0.5
#Condiciones Iniciales
v0=5.2
y0=0
ysuelo=0
tcero=0
t_0=np.linspace( 0 , 12 ,200)
#Posicion de la prticula
def y_p(t,y,v):
    return y+v*t-0.5*g*(t)**2
#Posicion del suelo
def y_s(t):
    return A*np.sin(w*t)
#Diferencia de las funciones
def resta(t,y,v):
    return y_p(t,y,v)-y_s(t)
#Velocidad de la particula
def v_p(t,v):
    return v-g*t
#Velocidad del suelo
def v_s(t):
    return A*w*np.cos(w*t)
#Velocidad de la particula despues del choque
def v_p_choque(t,v):
    return (1+n)*v_s(t)-n*v_p(t,v)
#Altura maxima
def h_max(y,v):
    return y+(v**2)/(4*g)
#Tiempo (aproximado) de vuelo de la particula
def t_viaje(y,v):
    return v+(v**2+2*(1+y))**0.5
#Encontramos el tiempo de interseccion de ambas funciones para el primer choque
t_choque_1=brentq(resta , 0.1, 10.5, args=(y0,v0) )
#Los mostramos
print ('Tiempo en el que chocan la particula con el suelo')
print t_choque_1
print ('Velocidad de la particula despues del choque')
print v_p_choque(t_choque_1,v0)

vpchoque=v_p_choque(t_choque_1,v0)

t_inter=t_choque_1

while (vpchoque > v_s(t_inter)):
    yp=y_p(t_inter , y_s(t_inter) ,vpchoque )
    ys=y_s(t_inter)
    vp=v_p(t_inter,vpchoque)
    vs=v_s(t_inter)
    #t_inter+=brentq(resta , t_inter+0.1 , t_viaje(yp,vp)+0.1 , args=(yp,vp))
    t_inter=newton(resta , t_viaje(yp,vp) , args=(yp,vp) )
    vpchoque=v_p_choque(t_inter,vp)
    print ('velocidades de choque')
    print vpchoque
    print ('tiempos')
    print t_inter

print ('interseccion del segundo rebote')
print t_choque_1+newton(resta,18,args=(0.73,4.41))
t_02=np.linspace(t_choque_1,20,200)
t_03=np.linspace(0,20,400)
plt.figure(1)
plt.clf()
#plt.axvline(raiz_brent)
plt.plot(t_0,y_p(t_0,y0,v0))          #(arreglar v0)
plt.plot(t_02,y_p(t_0,0.73,4.41))
plt.plot(t_03,y_s(t_03))
plt.show()
