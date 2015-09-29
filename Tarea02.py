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

#######################################################

#R = lambda x : A*sin(w*x) + A*cos(w*x)




vprima_p = 0. #velocidad justo despues del choque
v_p = 0. #velocidad justo antes del choque
v_s = 0. #velocidad del suelo

A = 1.  #Amplitud
w = 1.5  #Frecuencia del suelo
n = 0.5  #coeficiente de restitucion
m = 1.  #masa
g = 1.


R_s = lambda x : A*np.sin(w*x) #Posicion del suelo
V_s = lambda x : A*w*np.cos(w*x) #Velocidad del suelo
R_p = lambda x,y : y*x     #Posicion de la particula x Velocidad, y tiempo
V_p = lambda x : x     #Velocidad de la particula antes del impacto
V_p1 = lambda x, h : (1+n)*V_s(x) - n*V_p(x-h) #Velocidad de la particula despues del impacto

y0 = 0 #pegado al suelo
v0 = 0 #velocidad inicial
h = 0.001 #paso dt
tf = 10 #tiempo final

dt = np.arange(0, tf, h) #intervalo de tiempo discreto


V1 = np.zeros(len(dt))  #velocidad luego del choque
V1[0] = 2.
for i in range(len(dt)):
    V1[i] = V_p1(dt[i],h*i)

plt.plot(dt,R_p(V1,dt))
plt.show()

''''
ver que como implementar correctamente:
tengo la posicion y la velocidad del suelo
la posicion inicial de la particula
debo darme una velocidad inicial
calcular la velocidad' de la relacion con el suelo y eta
ver como calcular la posicion de la particula (integrar?)
intersectar la posicion de la particula con la del suelo
usar ese tiempo y repetir n veces
buena suerte D:
'''
