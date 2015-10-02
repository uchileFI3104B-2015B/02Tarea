import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import brentq
from scipy.optimize import bisect
from scipy.optimize import newton
from scipy import optimize as opt

#Definimos las constantes a usar
m=1
g=1
A=1
w=1.66
n=0.15

#Definimos los parametros iniciales
y0= 0
ysuelo=0
tcero=0
v0=5   #Velocidad inicial, modificable para ver como varia el problema


#Intervalos
a=0.1
b= (v0 + (((v0**2)+2*(1+y0))**0.5) ) #b corresponde al valor aproximado de la
                                     #interseccion. Se usara para ver los pará-
                                     #metros de la funcion para encontrar los
                                     #ceros.
#Ecuaciones de movimiento:

#Ecuación itinerario de la partícula
def y_p(t,y, v):
    return y + v * t - 0.5*g*(t**2)
#Posicion del suelo
def y_s(t,dt):
    return A * np.sin(w*(t+dt))
#Velocidad del suelo
def v_s(t,dt):
    return A * w * np.cos(w*(t+dt))
#Velocidad de la particula antes del choque
def v_p(t,v):
    return v-g*t
#Velocidad de la particula despues del choque
def v_pd(t,v,dt):
    return (1+n)*v_s(t,dt) - n *v_p(t,v)

#Diferencia entre posicion del suelo y posicion de la particula
def ys_menos_yp(t,y,v,dt):
    return  y_s(t,dt) - y_p(t,y,v)

#Contadores:
i=0                    #Contador de rebotes
rebotes=10             #Rebotes que queremos observar
raices=0               #t en el cual ocurre la intersección
tiempos=[]             #vector que ira guardando los valores de las raices
yparticula=[]          #vector posicion de la particula
vparticulachoque=[]    #vector velocidad de la particula despues del choque

for i in range(rebotes):
    resta=ys_menos_yp(0,y0,v0,tcero)
    print ('Resta')
    print resta
    raiz= brentq(ys_menos_yp, a, b, args=(y0,v0,tcero), xtol= 10**(-12))
    raices+=raiz
    print ('Raiz, tiempo de interseccion')
    print raiz
    y0=y_p(raiz,y0,v0)
    print ('Nuevo y0, posicion de la particula justo despues del choque')
    print y0
    #Actualizar valores
    vs=v_s(raiz,tcero)
    print ('Velocidad del suelo en la interseccion')
    print vs
    vp=v_p(raiz,v0)
    print ('Velocidad de la particula justo en la interseccion')
    print vp
    v0=(1+n)*vs - n *vp
    print ('Velocidad particula despues del choque, nueva v0')
    print v0


    #Actualizar valores del intervalo

    a=0.1
    b= (v0 + (((v0**2)+2*(1+y0))**0.5) )

    tcero=raiz
    print ('Valores de b, intervalos')
    print b
    print tcero

    #Agregar valores a vectores
    tiempos=np.append(tiempos,raices)
    yparticula=np.append(yparticula,y0)
    vparticulachoque=np.append(vparticulachoque,v0)
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
