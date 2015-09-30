'''
Este script...
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq
from scipy.optimize import newton
from scipy.optimize import bisect
m=1
g=1
A=1
w=2
n=0.5
t_0=np.linspace( 0 , 12 ,200)

def y_p(t,y_0,v_0):                #Definimos la funcion itinerario de la
    return y_0+v_0*t-0.5*g*(t)**2  #particula en funcion de tiempo, posicion
                                   #inicial y velocidad inicial.
def y_s(t):                        #Definimos tambien la funcion de  oscilacion
    return A*np.sin(w*t)           #del suelo y la resta de ambas funciones.
def resta(t,y_0,v_0):
    return y_p(t,y_0,v_0)-y_s(t)
def v_p(t,v_0):                    #Definimos la funcion de velocidad de la
    return v_0-g*t                 #particula en funcion de la velocidad inicial
def v_s(t):                        #Tambien la del suelo
    return A*w*np.cos(w*t)
raiz_brent=brentq(resta , 0.1, 10.5, args=(0,5) ) #(arreglar v0)Encontramos la
                                                  #interseccion de las funciones
def v_p_choque(t,v_0):              #Definimos la funcion de velocidad de la
    return (1+n)*v_s(t)-n*v_p(t,v_0)#particula despues del choque.

def h_max(y_0,v_0):
    return y_0+(v_0**2)/(4*g)

def t_viaje(y_0,v_0):
    return v_0+(v_0**2+2*(1+y_0))**0.5

print ('Tiempo en el que chocan la particula con el suelo')
print raiz_brent                    #Mostramos el tiempo de interseccion
print ('Velocidad de la particula despues del choque')
print v_p_choque(raiz_brent,5)      #(arreglar v0) Mostramos el valor de la
                                    #velocidad despues del choque
vpchoque=v_p_choque(raiz_brent,5)   #(arreglar v0)
t_inter=raiz_brent
while (vpchoque > 0):
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
print raiz_brent+newton(resta,18,args=(0.73,4.41))
t_02=np.linspace(raiz_brent,20,200)
t_03=np.linspace(0,20,400)
plt.figure(1)
plt.clf()
#plt.axvline(raiz_brent)
plt.plot(t_0,y_p(t_0,0,5))          #(arreglar v0)
plt.plot(t_02,y_p(t_0,0.73,4.41))
plt.plot(t_03,y_s(t_03))
plt.show()
