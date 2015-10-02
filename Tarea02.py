#######################################################
'''
Metodos Numericos para la Ciencia e Ingenieria FI3104
Tarea 2
Maximiliano Dirk Vega Aguilera
18.451.231-9
'''
#######################################################

import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize as op

#######################################################

A = 1.     #Amplitud
w = 1.68   #Frecuencia del suelo
n = 0.15   #Coeficiente de restitucion
m = 1.     #Masa
g = 9.     #Aceleracion de gravedad
R = 0.     #Posicion inicial
V = 50.    #Velocidad inicial

def Pos_Vel(R,V):
    '''
    Funcion que entrega la posicion y velocidad de la particula despues del
    choque dados el choque anterior.
    Se definen las funciones a usar y se calcula el punto en el que el suelo
    esta en contacto con la particula utilizando el metodo de la biseccion
    para una funcion auxiliar.
    Al final, R = -R_p(t), el menos es para solucionar un error.
    '''
    R_s = lambda x : A*np.sin(w*x+np.arcsin(R))     #Posicion del suelo
    V_s = lambda x : A*w*np.cos(w*x+np.arcsin(R))   #Velocidad del suelo
    R_p = lambda x : R + V*x -(1./2.)*g*(x**2)      #Posicion de la particula
    V_p = lambda x : V - g*x                        #Velocidad de la particula
    V_pa = lambda x : (1+n)*V_s(x) - n*V            #Vel antes del choque
    V_pd = lambda x : (1+n)*V_s(x) - n*V_pa(x)      #Vel despues del choque
    f = lambda x : A*np.sin(w*x+np.arcsin(R)) + R + V*x -(1./2.)*g*(x**2)
    dt = 0.00
    while True:          #Busca el cero de f
        a = f(0.+dt)
        b = f(2.*dt)
        if a*b < 0:      #Moviendose en dt busca cuando pasa el 0
            t = op.bisect(f,0.+dt,2.*dt)
            break
        else:
            dt += 0.005  #Intervalo que me muevo para buscar cero
    R = -R_p(t)          #Entrega posicion de la particula despues del choque
    V = V_pd(t)          #Entrega velocidad de la particula despues del choque
    return [R,V]

N = 100                  #Numero de choques a encontrar
aN = np.arange(1,N+1,1)  #Arreglo del numero de choques
aV= np.zeros(N)          #Arreglo de velocidad despues del choque
for i in range(N):       #Asigna los valores a los arreglos
    print i,Pos_Vel(R , V) #Muestra los datos obtenidos para verificar en el proceso
    aV[i] = Pos_Vel(R,V)[1]
    R = Pos_Vel(R,V)[0]
    V = Pos_Vel(R,V)[1]


plt.plot(aN,aV,'o-',label=('$w$ =',w))
plt.title('Velocidad de la particula despues del n-esimo choque')
plt.xlabel('$N^o$ de choques')
plt.ylabel('Velocidad de la particula')
plt.legend()
plt.show()
