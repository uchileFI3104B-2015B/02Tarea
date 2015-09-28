import numpy as np
from pylab import *
import matplotlib.pyplot as plt
'''------------------------------------------------------------------'''
#datos del problema
w=1
eta=1 #entre 0 y 1
v0=2 #mayor que w
'''----------------------------------------------------------------'''
def encontrar_cero(f,a,b,err=0.01,itera=40):
    '''Funcion que recibe una funcion y encuentra un cero mediante el metodo de biseccion '''
    p = (a+b)/2.
    i = 1
    while(np.fabs(f(p))>err)and(i<itera):
        if f(p) == 0:
            return p
        if f(a) * f(p) > 0:
            a = p
        else:
            b = p
        p = (a + b)/2.
        i += 1
    return p

def busca_bajo_piso(f,dx,a=0.01,max_=10000):
    '''recorre la funcion con un paso dado hasta encontrar un punto donde sea negativa'''
    u=a
    i=0
    while (f(u) > 0) and (i < max_) :
        u+=dx
        i+=1
    if(i >= max_):
        print("No se encontró punto negativo")
    return (u,u-dx)

def avanzar_salto(yn,vn_prima):
    '''Funcion que recibe la posicion del choque n-esimo (yn),
    y la velcidad justo despues del choque n-esimo (vn_prima),
    y retorna la posicion del n+1 choque (yn+1) y la velocidad justo despues
    de este(vn+1_prima).'''
    #tn se define como el tiempo en que se produce el choque n-esimo
    tn = np.arcsin(yn)/w
    #definiremos funciones auxiliares a las cuales les buscaremos los ceros
    f_auxiliar = lambda t: yn-t^2/2.+t*vn_prima-np.sin(w(t+tn))
    (a,b)=busca_bajo_piso(f_auxiliar)
    t1=encontrar_cero(f_auxiliar,a,b)
    yn1 = yn-t1**2/2.+t1*vn_prima
    vn1_prima = (1+eta)*w*cos(w(t1+tn))-eta*(vn_prima-t1)
    return(yn1,vn1_prima)
'''----------------------------------------------------------------------'''
plt.figure(1)
plt.clf()

t_values = np.linspace(0,6, 40)
y= lambda t: -t**2/2. + v0*t
y_values= [y(i) for i in t_values]
plt.plot(t_values, np.sin(w * t_values), label='piso')
plt.plot(t_values, y_values,color='red', label='pelota')
show()
