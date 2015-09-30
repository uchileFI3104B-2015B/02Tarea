'''
Este script...
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq
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

print ('Tiempo en el que chocan la particula con el suelo')
print raiz_brent                    #Mostramos el tiempo de interseccion
print ('Velocidad de la particula despues del choque')
print v_p_choque(raiz_brent,5)      #(arreglar v0) Mostramos el valor de la
                                    #velocidad despues del choque

plt.figure(1)
plt.clf()
plt.axvline(raiz_brent)
plt.plot(t_0,y_p(t_0,0,5))          #arreglar v0
plt.plot(t_0,y_s(t_0))
plt.show()
