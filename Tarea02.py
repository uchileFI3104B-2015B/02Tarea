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
w = 1.  #Frecuencia
n = 0. #coeficiente de restitucion
m = 1.  #masa
g = 1.
y0 =  0 #pegado al suelo
v0 =  0 #velocidad inicial

R_s = lambda x : A*np.sin(w*x) #Posicion del suelo
V_s = lambda x : A*w*np.cos(w*x) #Velocidad del suelo

a = np.arange(0,4*np.pi,0.01)

plt.plot(a,R_s(a))
plt.show()
