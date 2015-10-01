import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from scipy.optimize import brentq


#------------Se definen la funciones a usar en el programa------------#
def Vprima(eta,vs,vp):
    '''
    Recive el valor de la velocidad del suelo y de la particula
    justo antes del choque y devuelve el valor de la velocidad
    de la particula un instante despues
    '''
    return (1+eta)*vs-eta*vp


def Ps(t,omega,A):
    '''
    Entrega la posicion de la membrana en un instante t
    '''
    return A*np.sin(omega*t)+1

def Vs(t,omega,A):
    '''
    Entrega la velocidad de la membrana en un instante t
    '''
    return A*omega*np.cos(omega*t)


def Yp(t,h0,v0):
    '''
    Entrega la posicion de la particula para el tiempo t
    '''
    g=1
    return h0+v0*t-0.5*g*t**2

def Vp(t,v0):
    '''
    Entrega la velocidad de la particula para el tiempo t
    '''
    g=1
    return v0-g*t

def distancia(t,omega,A,h0,v0,tc):
    '''
    determina la distancia entre la particula y la membrana
    en un tiempo t
    '''
    return Ps(t,omega,A)-Yp(t-tc,h0,v0)



def ChoqueN(Yn,Vn,omega,A,eta,tc):
    '''
    Devuelve la posicion(Y_{n+1}) y la velocidad(V_{n+1})
    de la particula luego del choque n ademas del tiempo de choque
    en un vector de la forma [Yn+1,Vn+1,t]
    '''
    def distanciat(t):
        '''
        Crea una funcion de distancia que solo depende del tiempo
        '''
        d=distancia(t,omega,A,Yn,Vn,tc)
        return d

    if Vn<Vs(tc,omega,A):
        delta=0.001
        t1=tc
        t2=t1+delta
        while (distanciat(t1)*distanciat(t2) > 0.0):
                t2=t2+delta
    else:
        delta=0.01
        t1=Vn+np.sqrt((Vn**2)+2*Yn-4)+tc
        t2=t1+delta
        while (distanciat(t1)*distanciat(t2) > 0.0) and (t2<Vn+np.sqrt((Vn**2)+2*Yn)+tc):
                t2=t2+delta

    t_eff=brentq(distanciat,t1,t2)
    Yn1=Yp(t_eff-tc,Yn,Vn)
    vs=Vs(t_eff,omega,A)
    vp=Vp(t_eff-tc,Vn)
    Vn1=Vprima(eta,vs,vp)
    return Yn1,Vn1,t_eff

def Nrelax(fin,omega,ho,vo):
    '''
    Calcula el tiempo de choque 'n' veces y devuelve tres de tamano
    n+1, los vectores entregados son:
    *La posicion de la particula al efectuarse cada choque
    *Las velocidades con la que sale luego de cada choque
    *Los tiempos en que ocurre cada choque
    '''
    A=1
    eta=0.15
    i=0
    P=[ho]
    V=[vo]
    tc=[0]
    while i<fin:
        vec=ChoqueN(P[i],V[i],omega,A,eta,tc[i])
        P+=[vec[0]]
        V+=[vec[1]]
        tc+=[vec[2]]
        i+=1
        print V[i]
    return P,V,tc
#---------------------------------------------------------------------#
omega=1.66
hp=1.0
vp=2.0

cero=ChoqueN(hp,vp,omega,1,0.15,0)
t_values= np.linspace(0,2*cero[2],100)
plt.figure(1)
plt.clf()



plt.plot(t_values, Yp(t_values,hp,vp), label='particula')
plt.plot(t_values, Ps(t_values,omega,1), label='membrana')


plt.legend()


plt.axvline(cero[2], color='r')

plt.draw()
plt.show()

#---------------------------------Parte 2-3 -------------------------------------#
n=3

Velocidades1=Nrelax(n,1.66,hp,vp)
Velocidades2=Nrelax(n,1.67,hp,vp)
Velocidades3=Nrelax(n,1.68,hp,vp)
Velocidades4=Nrelax(n,1.69,hp,vp)
Velocidades5=Nrelax(n,1.70,hp,vp)

plt.figure(2)
plt.clf()

N=np.linspace(0,10,11)

plt.plot(N,Velocidades1[1], label='$N_{relax}\;\omega=1.66$')
plt.plot(N,Velocidades2[1], label='$N_{relax}\;\omega=1.67$')
plt.plot(N,Velocidades3[1], label='$N_{relax}\;\omega=1.68$')
plt.plot(N,Velocidades4[1], label='$N_{relax}\;\omega=1.69$')
plt.plot(N,Velocidades5[1], label='$N_{relax}\;\omega=1.70$')

plt.legend()

plt.draw()
plt.show()
#---------------------------parte 4------------------------------------#
'''
w=input('Frecuencia=')
vo=input('Velocidad=')
h0=input('Posicion inicial de la particula=')
n=input('Numero de iteraciones(o choques)=')
img=raw_input('desea guardar las imagenes? (Y o N):')
VN=Nrelax(n,w,h0,vo)

tiempos=VN[2]
posiciones=VN[0]
velocidades=VN[1]
P=[]

plt.figure(1)
plt.clf()

for i in range(len(tiempos)-2):
    t_values= np.linspace(tiempos[i],tiempos[i+1],100)
    P+=[Yp(t_values,posiciones[i],velocidades[i])]
    plt.axvline(tiempos[i], color='b')


plt.plot(tiempos, P, label='particula')
plt.plot(tiempos, Ps(tiempos,omega,A), label='membrana')

plt.legend()



plt.draw()
plt.show()
'''
