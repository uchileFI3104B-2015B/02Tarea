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
from scipy import optimize as op

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
R = 0. #posicion inicial
V = 7. #Velocidad inicial
ti = 0  #tiempo inicial
tf = 10 #tiempo final
h = 0.001 #paso

idt = np.arange(ti, tf, h) #intervalo de tiempo discreto

'''
V_pa= np.zeros(len(dt))  #velocidad antes del choque
V_pd= np.zeros(len(dt))  #velocidad luego del choque
R_p= np.zeros(len(dt))  #posicion de la particula
V_p= np.zeros(len(dt))  #velocidad de la particula

fR_s = lambda x : A*np.sin(w*x) #Posicion del suelo, x variable tiempo
fV_s = lambda x : A*w*np.cos(w*x) #Velocidad del suelo, x variable tiempo
fR_p = lambda x: V*x -(1/2)*g*(x**2) #posion de la particula,x tiempo, Vel despues del impacto
fV_p1 = lambda x, h : (1+n)*V_s(x) - n*V_p(x-h) #Velocidad de la particula despues del impacto

V_pa[0] = V #velocidad inicial antes del primer impacto (inicial)
V_pd[0] = (1+n)*fV_s(0) - n*V_pa[0] #velocidad despues del primer impacto (inicial)
V = V_pd[0] #Velocidad inicial despues del choque
R_p = lambda x : V*x -(1./2.)*g*(x**2.)

V_pa = V #velocidad inicial antes del primer impacto (inicial)
V_pd = (1+n)*fV_s(0) - n*V_pa[0] #velocidad despues del primer impacto (inicial)
'''
def Pos_Vel(R,V):
    R_s = lambda x : A*np.sin(w*x)
    V_s = lambda x : A*w*np.cos(w*x)
    R_p = lambda x : R + V*x -(1./2.)*g*(x**2)
    V_p = lambda x : V - g*x
    V_pa = lambda x : (1+n)*V_s(x) - n*V
    V_pd = lambda x : (1+n)*V_s(x) - n*V_pa(x)
    f = lambda x : R_s(x) - R_p(x)
    dt = 0.0
    while True:
        a = f(dt)
        b = f(2*dt)
        if a*b < 0:
            t = op.brentq(f,dt,2*dt)
            break
        else:
            dt += 0.05   #intervalo que me muevo para buscar (que tan pequenho (?))
    V = V_p(t)
    R = R_p(t)
    V = V_pd(t)
    return [R,V,f(t)]

#plt.plot(idt,)
for i in range(5):
    print Pos_Vel(R , V)
    R = Pos_Vel(R,V)[0]
    V = Pos_Vel(R,V)[1]




#plt.plot(dt,R_p(dt))
#plt.show()
