import matplotlib.pyplot as plt
import numpy as np
from pylab import *
from scipy.optimize import brentq

#Parámetros fijos
m=1
g=1
A=1
H0=[0]
tc=[0]

#Parámetros a elegir
V0=[5]
eta=0.8
omega=1.66
n=10
t=np.linspace(0,50,100)

##Pregunta 1

#Caracterización del suelo
def ys(A,omega,t):
    '''
    Función para describir el movimiento sinusoidal del suelo.
    -A corresponde a la amplitud máxima del movimiento sinusoidal del suelo
    -omega corresponde a la frecuencia angular del movimiento sinusoidal del suelo
    '''
    Ys=A*np.sin(omega*t)
    return Ys

def vs(A,omega,t):
    '''
    Derivada de 'xs', i.e, velocidad de un punto específico del suelo suelo.
    -A corresponde a la amplitud máxima del movimiento sinusoidal del suelo
    -omega corresponde a la frecuencia angular del movimiento sinusoidal del suelo
    '''
    vs=A*omega*np.cos(omega*t)
    return vs

#Caracterización de la partícula de masa m=1
def yp(h0,v0,g,t):
    '''
    Posición de la particula en función del tiempo
    (Eje y, movimiento vertical con gravedad g=1)
    -h0 corresponde a la altura inicial de la partícula
    -v0 corresponde a la velocidad inicial de la partícula
    '''
    Yp=h0+v0*t-0.5*g*t**2
    return Yp

def vp(v0,g,t):
    '''
    Velocidad de la partícula en función del tiempo
    -v0 corresponde a la velocidad inicial de la partícula
    '''
    Vp=v0-g*t
    return Vp

def vpp(Vs,Vp,eta):
    '''
    Función que entrega el valor de la velocidad de la partícula justo después del bote.
    -eta corresponde al coeficiente de restitución (Entre 0 y 1, eta=1 caso elástico).
    -vs corresponde a la velocidad del suelo en el instante del choque.
    -vp corresponde a la velocidad de la partícula justo antes del choque.
    '''
    Vpp=(1+eta)*Vs-eta*Vp
    return Vpp

#Método para buscar los 0's entre el movimiento del suelo y de la partícula
def funcion(Yn,Vn,A,omega,eta,g,ta):
    '''
    Función que permite calcular (Yn+1, Vn+1) dados (Yn, Vn):
    -Yn corresponde a la posición de la partícula luego del N-ésimo choque
    -Vn corresponde a la posición de la particula luego del N-ésimo choque
    -A corresponde a la amplitud máxima del movimiento sinusoidal del suelo
    -omega corresponde a la frecuencia angular del movimiento sinusoidal del suelo
    -eta corresponde al coeficiente de restitución
    -ta corresponde al tiempo en que se produce el choque anterior
    '''
    def dist(Yn,Vn,A,omega,g,t,ta):
        '''
        Función que permite calcular la altura entre la partícula y el suelo
        '''
        r=-ys(A,omega,t)+yp(Yn,Vn,g,t-ta)
        return r

    def f(t):
        F=dist(H0[j],V0[j],A,omega,g,t,tc[j])
        return F

    tiempitos=ta
    d=0.0005
    while f(tiempitos)>0.0:
        tiempitos+=d

    t1=tiempitos-d
    t2=tiempitos

    #Usamos el método 'Brentq' para encontrar la raíz exacta de la función 'yc'
    #dados los tiempos encontrados por el método de buscar ceros

    tf=brentq(f,t1,t2)  #Tiempo que buscamos (Raíz)

    Vs=vs(A,omega,tf)
    Vp=vp(Vn,g,tf)

    Y=yp(Yn,Vn,g,tf-ta)
    V=vpp(Vs,Vp,eta)

    arreglo=[tf,Y,V]

    return arreglo

j=0
choque=[funcion(H0[j],V0[j],A,omega,eta,g,tc[j])]
print choque

tc+=[choque[0][0]]
H0+=[choque[0][1]]
V0+=[choque[0][2]]

j=1
while j<n:
    choque+=[funcion(H0[j],V0[j],A,omega,eta,g,tc[j])]
    tc+=[choque[j][0]]
    H0+=[choque[j][1]]
    V0+=[choque[j][2]]
    j+=1

print tc
print H0
print V0
