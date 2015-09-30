import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize as opt

t=np.linspace(0,10,1000);
A=1 #fijo
g=1 #fijo
m=1 #fijo
w=1
rest=0.5 #va de 0 a 1
y_0=0
v_0=2 #debe ser mayor que A*w
n=10 #número de rebotes
times=[]; #vector que contendrá los tiempos en que se producen los rebotes

def floor(t):
    y_s=A*np.sin(w*t); #posición del suelo
    return y_s
def particle(t):
    y_p=y_0+(v_0*t)-((1/2.)*g*t**2); #posición de la partícula
    return y_p
def floorv(t):
    v_s=A*w*np.cos(w*t); #velocidad del suelo
    return v_s
def particlev(t):
    v_p=v_0-g*t #velocidad de la partícula
    return v_p
def collision(t):
    v_p_new=(1+rest)*floorv(t)-rest*particlev(t) #cambio de velocidad de la partícula al chocar
    return v_p_new
def resta(x):
    y=floor(x)-particle(x)
    return y

plt.figure(1)
plt.clf()

for i in range(0,n):
    zero_i=opt.bisect(resta,4+i,6+i); #falta determinar los instantes entre los cuales la wea choca
    times.insert(i,zero_i) #inserta el tiempo en que ocurre el choque i
    v_p_new=(1+rest)*floorv(zero_i)-rest*particlev(zero_i) #velocidad de la particula despues de chocar por 1ra vez
    y_0_new=particle(zero_i)
    def particle(t):
        y_p=(y_0_new)+(v_p_new*(t-zero_i))-((1/2.)*g*(t-zero_i)**2); #redefino la ecuación de movimiento de la partícula
        return y_p
    plt.plot(t,floor(t),'r',t,particle(t),'b')
    plt.axvline(zero_i,color='g')

plt.xlabel('Tiempo [s]')
plt.ylabel('Altura [m]')
plt.show()
