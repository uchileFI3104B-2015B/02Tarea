'''

Este es un script que busca la interseccion entre un suelo que oscila y una
pelota que describe una trayectoria gracias a la gravedad, es decir, busca los
choques o rebotes de la particula en este suelo. Para esto se define una funcion
que resta ambas ecuaciones de movimiento y se buscan los ceros de esta funcion
con el comando "brentq". Todo este procedimiento se repite tantas veces como
choques permitan esta particula y el suelo. El numero de iteraciones queda
determinado por la velocidad con que sale la particula despues del n-esimo
choque, ya que si esta es negativa es porque la particula quedo por debajo del
suelo, lo cual no es posible.

'''

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import brentq
from scipy.optimize import bisect
from scipy.optimize import newton
from scipy import optimize as opt

#Parametros del problema
m=1
g=1
A=1
w=1.66
n=0.15

#Condiciones iniciales
y0= 0
ysuelo=0
tcero=0
v0=5 #Este valor se puede ir cambiando para probar cuantos choques hay,
        #que pasa con ciertas velocidades, etc.

#Contadores. i es para contar el numero de choques y raices es para contar el
#tiempo en el que ocurren estos choques
i=0
raices=0
tiempos=[]
ypelota=[]
vpelotachoque=[]

#Intervalos
a=0.1
b= (v0 + (((v0**2)+2*(1+y0))**0.5) )

#Ecuaciones de movimiento

#Posicion de la particula
def y_p(t,y, v):
    return y + v * t - 0.5*g*(t**2)
#Posicion del suelo
def y_s(t,td):
    return A * np.sin(w*(t+td))
#Velocidad del suelo
def v_s(t,td):
    return A * w * np.cos(w*(t+td))
#Velocidad de la particula antes del choque
def v_p(t,v):
    return v-g*t
#Velocidad de la particula despues del choque
def v_pd(t,v,td):
    return (1+n)*v_s(t,td) - n *v_p(t,v)

#Diferencia entre posicion del suelo y posicion de la particula
def ys_menos_yp(t,y,v,td):
    return  y_s(t,td) - y_p(t,y,v)


plt.clf()

tiempo=np.linspace(0,20,100)
choques=3

plt.plot(tiempo, y_s(tiempo,tcero), label='suelo',color='r')
plt.plot(tiempo, y_p(tiempo, y0, v0))

for i in range(choques):
    resta=ys_menos_yp(0,y0,v0,tcero)
    print ('Resta')
    print resta
    raiz= brentq(ys_menos_yp, a, b, args=(y0,v0,tcero), xtol= 10**(-12))
    raices+=raiz
    print ('Raiz, tiempo de interseccion')
    print raiz

    t_values=np.linspace(0, raices,100)


    plt.plot(t_values+raices, y_p(tiempo,y0,v0) , color='b')
    plt.axvline(raices,color='y')

    y0=y_p(raiz,y0,v0)
    print ('Nuevo y0, posicion de la pelota justo despues del choque')
    print y0
    #Actualizar valores
    vs=v_s(raiz,tcero)
    print ('Velocidad del suelo en la interseccion')
    print vs
    vp=v_p(raiz,v0)
    print ('Velocidad de la pelota justo en la interseccion')
    print vp
    v0=(1+n)*vs - n *vp
    print ('Velocidad pelota despues del choque, nueva v0')
    print v0

    #Actualizar valores del intervalo
    a=0.1
    b= (v0 + (((v0**2)+2*(1+y0))**0.5) )
    tcero=raiz

    #Agregar valores a vectores
    tiempos=np.append(tiempos,raices)
    ypelota=np.append(ypelota,y0)
    vpelotachoque=np.append(vpelotachoque,v0)
    print ('Numero de choque (primer choque = 0 y asi en adelante)')
    print i
    i+=1


plt.legend()
plt.draw()
plt.show()


print ('Vector que presenta tiempos en el que sucede cada choque')
print tiempos
print ('Vector que presenta la posicion inicial de la pelota luego de cada choque')
print ypelota
print ('Vector que presenta la velocidad de la pelota despues de cada choque')
print vpelotachoque
