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


#Parametros del problema
m=1
g=1
A=1
y0= 0
v0=5
w=2
n=0.5
t_values= np.linspace(0,12,50)

#Ecuaciones de movimiento

#Posicion de la particula
def y_p(t,y0, v0):
    return y0 + v0 * t - 0.5*g*(t**2)
#Posicion del suelo
def y_s(t):
    return A * np.sin(w*t)
#Velocidad del suelo
def vs(t):
    return A*w*np.cos(w*t)
#Velocidad de la particula antes del choque
def vp(t,v0):
    return v0-g*t
#Velocidad de la particula despues del choque
def v_pd(t,v0):
    return (1+n)*vs(t) - n *vp(t,v0)

plt.plot(t_values, y_p(t_values,y0,v0), label= 'Posicion pelota')
plt.plot(t_values, y_s(t_values), label= 'Posicion suelo')

#Diferencia entre posicion del suelo y posicion de la particula
def ys_menos_yp(t,y0,v0):
    return y_p(t,y0,v0) - y_s(t)

#Calculo de la Raiz
raiz_brent = brentq(ys_menos_yp, 0.1, 11, args=(y0,v0))
print raiz_brent
plt.axvline(raiz_brent, color='r')



plt.draw()
plt.show()


#raiz_bisect = bisect(ys_menos_yp, 0.1, 2.5)
#print raiz_bisect
#plt.axvline(raiz_bisect, color='g')

#raiz_newton = newton(ys_menos_yp, 2.5)
#print raiz_newton
#plt.axvline(raiz_newton, color='b')
