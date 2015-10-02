'''
Este es un script que busca el punto de interseccion entre la
funcion piso_oscilante y arco_pelota, para después calcular 
la posición y velocidad del siguente bote de una pelota.
'''

import numpy as np
import matplotlib.pyplot as plt

def Ppiso_oscilante (A,w,t):
    '''
    Esta funcion recibe una amplitud, una frecuencia,
    y un tiempo, y retorna una funcion sinusoidal que
    describe la posicion del piso en el tiempo t.
    '''
    ft=A*np.sin((w*t))
    return ft

def arco_pelota (Xi,Vi,g,t):
    '''
    Esta función recibe la posicion inicial, velocidad inicial, 
    aceleracion de gravedad, la masa de la pelota y un tiempo t
    y retorna la posición de la pelota en el tiempo t.
    '''
    yt=Xi+Vi*t-g*(t**2)/2
    return yt

def Vpiso_oscilante (A,w,t):
    '''
    Esta funcion recibe una amplitud, una frecuencia,
    y un tiempo, y retorna una funcion sinusoidal que
    describe la velocidad del piso en el tiempo t.
    '''
    ft=A*w*np.cos((w*t))
    return ft
    
def rebote_pelota (eta,vs,vp):
    '''
    Esta funcion recibe un coeficiente de restitucion eta,
    la velocidad del piso, y la velocidad de la pelota
    antes de rebotar, y retorna la velocidad de la pelota
    despues de rebotar contea el piso.
    '''
    Vpf=(1+eta)*vs-(eta*vp)
    return Vpf

def velocidad_pelota (Vi,g,t):
    '''
    Esta función recibe la posicion inicial, velocidad inicial, 
    aceleracion de gravedad, la masa de la pelota y un tiempo t
    y retorna la velocidad de la pelota en el tiempo t.
    '''
    yt=Vi-g*t
    return yt
    
Vn=float(input('Velocidad inicial pelota?'))
Yn=float(input('Posicion inicial pelota? (Debe ser entre -1 y 1)'))
while (Yn<-1) or (Yn>1):
    print "Comando inválido"
    Yn=float(input('Posicion inicial pelota? (Debe ser entre -1 y 1)'))
Etan=float(input('Coeficiente de restitucion (eta)? (debe ser entre 0 y 1)'))
while (Etan<0) or (Etan>1):
    print "Comando inválido"
    Etan=float(input('Coeficiente de restitucion (eta)? (debe ser entre 0 y 1)'))
wn=float(input('Frecuencia oscilacion piso?'))
sb=int(input("Piso sube o baja? (-1 si baja, 1 si sube)"))

while (sb!=1) and (sb!=-1):
    print "Comando inválido"
    sb=input("Piso sube o baja? (-1 si baja, 1 si sube)")
    
A=1
g=1

if sb==1:
    tn=np.arcsin(Yn/A)/wn #El piso sube
else:
    tn=(-np.arcsin(Yn/A)+np.pi)/wn #El piso baja
    

from scipy.optimize import brentq

def siguiente_rebote(Yn,Vn,g,A,wn,t):
    arco_pelota(Yn,Vn,g,t)-Ppiso_oscilante(A,wn,t)

tf = brentq(siguiente_rebote, -np.pi/2, 15)
print (tf)
Yf=Ppiso_oscilante(A,wn,(tf+tn))
vs=Vpiso_oscilante(A,wn,(tf+tn))
vp=velocidad_pelota(Vn,g,tf)
Vf=rebote_pelota(Etan,vs,vp)
print (Yf)
print (Vf)