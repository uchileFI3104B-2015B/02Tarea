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
from scipy import integrate as Int

#######################################################
'''
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

'''
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

A = 1.  #Amplitud
w = 1.5  #Frecuencia del suelo
n = 0.3  #coeficiente de restitucion
m = 1.  #masa
g = 1.  #aceleracion de gravedad

ti = 0  #tiempo inicial
tf = 10 #tiempo final
h = 0.001 #paso

dt = np.arange(ti, tf, h) #intervalo de tiempo discreto

V_pa= np.zeros(len(dt))  #velocidad antes del choque
V_pd= np.zeros(len(dt))  #velocidad luego del choque
R_p= np.zeros(len(dt))  #posicion de la particula
V_p= np.zeros(len(dt))  #velocidad de la particula

fR_s = lambda x : A*np.sin(w*x) #Posicion del suelo, x variable tiempo
fV_s = lambda x : A*w*np.cos(w*x) #Velocidad del suelo, x variable tiempo
fR_p = lambda V: V*dt -(1/2)*g*(dt**2) #posion de la particula,x tiempo, Vel despues del impacto
fV_p1 = lambda x, h : (1+n)*V_s(x) - n*V_p(x-h) #Velocidad de la particula despues del impacto

V_pa[0] = 5 #velocidad inicial antes del primer impacto (inicial)
V_pd[0] = (1+n)*fV_s(0) - n*V_pa[0] #velocidad despues del primer impacto (inicial)
R_p[0] = lambda x,i : V_pd[i]*x -(1/2)*g*(x**2)
#R_p = Int.quad(V_pd[0],ti,tf)
print V_pd[0]

plt.plot(dt,R_p[0](dt,0))
plt.show()
