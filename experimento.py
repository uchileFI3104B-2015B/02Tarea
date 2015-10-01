'''
Este script desarrolla el experimento de dejar
la partícula de masa m rebotar sobre el suelo
oscilante, y registra los valores de las
velocidades de salida de la particula luego de
cada choque. Se imprime un grafico de las
velocidades de salida para los n suficientemente
grandes tal que el sistema ya se haya
estabilizado, para asi estudiar las diferentes
tipos de movimiento que tiene la particula
al rebotar sobre el suelo
'''
import numpy as np
import matplotlib.pyplot as plt
from bote import outnchoque

#Parametros
w1=np.linspace(1.66,1.669,10)
w2=np.linspace(1.67,1.6798,50)
w3=np.linspace(1.68,1.724,45)
w4=np.linspace(1.725,1.7398,50)
w5=np.linspace(1.735,1.79,45)
w=np.concatenate((w1,w2,w3,w4,w5))
eta=0.15

#Condiciones iniciales
y=0
v=2
s=1
t=0

#Evolucion de particula
i=0 #contador de w
plt.figure(1)
while i<len(w):
    n=0 #contador de botes
    while n<150:
        out=outnchoque(y,v,w[i],s,eta)
        y=out[0] #posicion del choque
        v=out[1] #v' despues del choque
        s=out[2] #signo de v_s despues del choque
        n+=1
        if n>100:
            plt.plot(w[i],v,'bo')
    i+=1
plt.xlabel('Frecuencia angular $\omega$')
plt.ylabel('Velocidad despues del bote $v\'_n$')
plt.title('Valores estacionarios de $v\'_n$ versus $\omega$ ')
plt.savefig('bifurcacion.eps')
