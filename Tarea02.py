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
R_p = lambda x : V_p*x     #Posicion de la particula
V_p = lambda x : x     #Velocidad de la particula antes del impacto
V_p1 = lambda x, h : (1+n)*V_s(x) - n*V_p(x-h) #Velocidad de la particula despues del impacto

y0 = 0 #pegado al suelo
v0 = 0 #velocidad inicial
h = 0.001 #paso dt
tf = 10 #tiempo final

a = np.arange(0, tf, h) #intervalo discreto

V1 = np.zeros(len(a))  #velocidad luego del choque
V1[0] = 2.
for i in range(len(a)):
    V1[i] = V_p1(a[i],h*i)



plt.plot(a,V1)
plt.show()
