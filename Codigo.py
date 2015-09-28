#Tarea 2

import matplotlib.pyplot as plt
import numpy as np

#definimos las variables de las cuales depende el problema
m=1
A=1
w=1
n=1
y0=0
v0=1
g=1
t=np.linspace(0, 2*np.pi, 1000)
#definimos una funcion de posicion y velocidad del suelo
def y_suelo(t):
    return A*np.sin(w*t)
def v_suelo(t):
    return A*w*np.cos(w*t)
#definimos funciones de posicion y velocidad para la pelota
def y_pelota(t):
    return y0 + v0t -(g*(t**2))/2
def v_pelota(t):
    return v0 -gt
def sp(t):
    return y_suelo(t) - y_pelota(t)

def biseccion(func, a, b, eps=0.01, max_iter=40):
	'''
	Recibe una funcion y dos puntos en lados
	opuestos a una raiz, y encuentra la raiz
	usando el metodo de la biseccion.
	'''
	p = (a + b) / 2.
	counter = 1
	while (np.fabs(func(p)) >= eps) and (counter < max_iter):
		if func(p) == 0:
			return p
		if func(a) * func(p) > 0:
			a = p
		else:
			b = p
		p = (a + b) / 2.
		counter += 1
	return p
n=
yt=[]
i=1
while i<n:
