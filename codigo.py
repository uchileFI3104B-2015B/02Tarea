'''
Este es un script que


Para encontrar el tiempo t* tenemos que intersectar la funcion itinerario de
la pelota, con la oscilación del suelo
No se me ocurre como escribirlas, pero los pasos a seguir son:
-Definir la ecuacion itinerario
-Definir la funcion de oscilacion del suelo
-Restarlas e igualarlas a cero para obtener la intersección y el tiempo "t"
donde se intersectan
-Va a tener muchas soluciones
-Ahi hay que aplicar la recurrencia de alguna forma
-Te necesito a ti para ver como escribir los codigos jajajaja
Ecuacion itinerario: y_pelota=y0 + v0*t - 0.5*g*(t^2)
Oscilacion del suelo: y_suelo=A*sin(w*t)

'''

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import brentq
from scipy.optimize import bisect
from scipy.optimize import newton
from scipy import optimize as opt


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
    return y_s(t,td) - y_p(t,y,v)


#Parametros del problema
m=1
g=1
A=1
y0= 0
t0=0
v0=5
w=2
n=0.5
i=0
a=0.1
b= (v0 + (((v0**2)+2*(1+y0))**0.5) )
tiempos=[0]*20
ypelota=[0]*20
vpelotachoque=[0]*20
raices=0

#iteracion
while True:
    if v0>1.5:
        raiz= brentq(ys_menos_yp, a, b, args=(y0,v0,t0))
        raices+=raiz
        print ('Raiz, tiempo de interseccion')
        print raiz
        y0=y_p(raiz,y0,v0)
        print ('Nuevo y0, posicion de la pelota justo despues del choque')
        print y0
    #Actualizar valores
        vs=v_s(raiz,t0)
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
        t0=raiz
        print ('Valores de b, intervalos')
        print b

        #Agregar valores a vectores
        tiempos[i]=raiz
        ypelota[i]=y0
        vpelotachoque[i]=v0

        i+=1
    else:
        break


print tiempos
print ypelota
print vpelotachoque



#raiz_bisect = bisect(ys_menos_yp, 0.1, 2.5)
#print raiz_bisect
#plt.axvline(raiz_bisect, color='g')

#raiz_newton = newton(ys_menos_yp, 2.5)
#print raiz_newton
#plt.axvline(raiz_newton, color='b')
