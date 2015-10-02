"""
Parte 1
"""
import numpy as np
from scipy.optimize import bisect
"""
Script que contiene:
función f a la que se quiere encontrar la raiz (Yparticula-Ypiso)
función que calcula la velocidad v(n+1) que tendrá la partícula luego del choque 
con el piso y posición y(n+1) cuando sucede el choque , dado los valores 
anteriores y(n) y v(n)
"""

def f(t, y_n,v_n,w):
    """
    Función que recibe posición y velocidad inicial de la particula,
    frecuencia de oscilación del piso y tiempo.
    Entrega el valor de la función (Yparticula-Ypiso) en un tiempo dado.
    """
    return v_n*t-t**2/2+y_n-[np.sin(w*t+np.arcsin(y_n))]

def choque(y_n,v_n, w,eta):
    """
    Función que recibe (y_n) y (v_n), además de los parámetros
    coeficiente de restitución (eta) y frecuencia (w)
    Encuentra el cero de la función f y entrega y_(n+1) y v_(n+1)
    """
    t=0.001
    while f(t,y_n,v_n,w)>=0: # recorre la función en el tiempo hasta que se hace negativa
        t+=0.1
    t_choque = bisect(f, t-0.1,t, args=(y_n)) # encuentra el cero de la funcion entre t y el instante anterior
    vs=np.cos(w*t_choque+np.arcsin(y_n))*w #  velocidad del suelo en el tiempo de choque
    vp_antes=-(t_choque)+v_n   # velocidad de la partícula justo antes del rebote
    vp_despues=(1+eta)*vs-eta*vp_antes # velocidad de la partícula después del rebote
    y_n_siguiente=np.sin(w*t_choque+np.arcsin(y_n)) #posición de la partícula en el instante del choque
    return [y_n_siguiente,vp_despues]

"""
Parte 2
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import bisect
"""
Script que grafica la velocidad de la particula luego del rebote vs.
el numero del rebote
"""

def f(t, y_n,v_n,w):
    return v_n*t-t**2/2+y_n-(np.sin(w*t+np.arcsin(y_n)))

def choque(y_n,v_n, w,eta):
    t=0
    while f(t,y_n,v_n,w)>=0 or f(0,y_n,v_n,w)<0: # recorre la funcion en el tiempo hasta que se hace negativa
        t+=0.01
    t_choque = bisect(f, t-0.01, t, args=(y_n,v_n,w)) # encuentra el cero de la funcion entre t y el instante anterior
    vs=np.cos(w*t_choque+np.arcsin(y_n))*w #  velocidad del suelo en el tiempo de choque
    vp_antes=-(t_choque)+v_n   # velocidad de la particula justo antes del rebote
    vp_despues=(1+eta)*vs-eta*vp_antes # velocidad de la particula despues del rebote
    y_n_siguiente=np.sin(w*t_choque+np.arcsin(y_n)) #posicion de la particula en el instante del choque
    return [y_n_siguiente,vp_despues]

#condiciones iniciales y parametros
v_0=2
w=1.66
eta=0.15
y_0=0
n=100 #cantidad de rebotes

    
num=range(1,n+1) #lista con el numero del rebote
v=np.zeros(n)  #arreglo donde iran las velocidades v_n
y=np.zeros(n)
v[0]=v_0
y[0]*y_0
v_n=v_0
y_n=y_0
#Se itera para generar los rebotes, los y(n) y v(n) calculados se usan 
#como condiciones iniciales para la siguiente iteracion
i=1
while i<n:
    choque_yv=choque(y_n,v_n, w,eta)
    v_n=choque_yv[1]
    y_n=choque_yv[0]
    y[i]=y_n
    v[i]=v_n
    i+=1
    #Se plotea el grafico
plt.figure(1)
plt.plot(num,v)
plt.grid(True, which='both')
plt.title("Velocidad particula vp' vs. Numero de rebote")
plt.xlabel('Numero de rebote')
plt.ylabel("Velocidad particula")
plt.draw()
plt.show()

"""
Parte 3
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import bisect
"""
Script que grafica la velocidad de la particula luego del rebote vs.
el numero del rebote
"""

def f(t, y_n,v_n,w):
    return v_n*t-t**2/2+y_n-(np.sin(w*t+np.arcsin(y_n)))

def choque(y_n,v_n, w,eta):
    t=0.001
    while f(t,y_n,v_n,w)>=0 or f(0,y_n,v_n,w)<0: # recorre la funcion en el tiempo hasta que se hace negativa
        t+=0.1
    t_choque = bisect(f, t-0.1, t, args=(y_n,v_n,w)) # encuentra el cero de la funcion entre t y el instante anterior
    vs=np.cos(w*t_choque+np.arcsin(y_n))*w #  velocidad del suelo en el tiempo de choque
    vp_antes=-(t_choque)+v_n   # velocidad de la particula justo antes del rebote
    vp_despues=(1+eta)*vs-eta*vp_antes # velocidad de la particula despues del rebote
    y_n_siguiente=np.sin(w*t_choque+np.arcsin(y_n)) #posicion de la particula en el instante del choque
    return [y_n_siguiente,vp_despues]

#condiciones iniciales y parametros
v_0=2
eta=0.15
y_0=0
n=50 #cantidad de rebotes

    
num=range(1,n+1) #lista con el numero del rebote
v=np.zeros(n)  #arreglo donde iran las velocidades v_n
y=np.zeros(n)
v[0]=v_0
y[0]*y_0
v_n=v_0
y_n=y_0
#Se itera para generar los rebotes, los y(n) y v(n) calculados se usan 
#como condiciones iniciales para la siguiente iteracion
omegas=[1.68,1.7]
k=1
for w in omegas:
    i=1
    while i<n:
        [y_n,v_n]=choque(y_n,v_n, w,eta)
        y[i]=y_n
        v[i]=v_n
        i+=1
    #Se plotea el grafico
    plt.figure(k)
    plt.plot(num,v)
    plt.grid(True, which='both')
    plt.title("Velocidad particula vp' vs. Numero de rebote")
    plt.xlabel('Numero de rebote')
    plt.ylabel("Velocidad particula vp'")
    plt.draw()
    plt.show()
    k+=1
    
"""
Parte 4
"""
'''
Script que grafica 50 valores de las velocidades de la particula despues del 
rebote por cada frecuencia angular del piso entre 1.66 y 1.80. Las velocidades v_n' que
se utilizan corresponden a las obtenidas luego de que para todas las frecuencias
el sistema se ha estabilizado (es decir n suficientemente grande ). 
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import bisect

def f(t, y_n,v_n,w):
    return v_n*t-t**2/2+y_n-(np.sin(w*t+np.arcsin(y_n)))
    
def choque(y_n,v_n, w,eta):
    t=0.001
    while f(t,y_n,v_n,w)>=0 or f(0.001,y_n,v_n,w)<0: # recorre la funcion en el tiempo hasta que se hace negativa
        t+=0.1
    t_choque = bisect(f, t-0.1, t, args=(y_n,v_n,w)) # encuentra el cero de la funcion entre t y el instante anterior
    vs=np.cos(w*t_choque+np.arcsin(y_n))*w #  velocidad del suelo en el tiempo de choque
    vp_antes=-(t_choque)+v_n   # velocidad de la particula justo antes del rebote
    vp_despues=(1+eta)*vs-eta*vp_antes # velocidad de la particula despues del rebote
    y_n_siguiente=np.sin(w*t_choque+np.arcsin(y_n)) #posicion de la particula en el instante del choque
    return [y_n_siguiente,vp_despues]


plt.figure(1)
#Se utilizan frecuencias cercanas entre 1.66 y 1.669 y luego mas alejadas
#entre 1.67 y 1.79
frecuencia1=np.linspace(1.66,1.669,10)
frecuencia2=np.linspace(1.67,1.79,30)
frecuencia=np.concatenate((frecuencia1,frecuencia2))
#parametro eta y condiciones iniciales
eta=0.15
y_0=0
v_0=2
v_n=v_0
y_n=y_0
Nrelax=60 #numero en que se considera los sistemas estan estabilizados
#Se genera iteracion para graficar punto por punto
i=0 
for w in frecuencia:
    n=0 #numero del bote
    while n<2*Nrelax:
        [y_n,v_n]=choque(y_n,v_n, w,eta) #posicion en el choque y velocidad despues del choque
        n+=1
    while n>=2*Nrelax and n<170:
        [y_n,v_n]=choque(y_n,v_n, w,eta)
        n+=1
        plt.plot(w,v_n,'ro')
    i+=1
plt.xlabel('Frecuencia angular $\omega$')
plt.ylabel('Velocidad $v_n\'$ despues del rebote')
plt.title('velocidades $v_n\'$ vs. $\omega$ ')
plt.show()