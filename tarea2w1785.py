from math import *
from scipy import integrate as int
from scipy import optimize 
import pyfits #modulo para leer archivos fits
import matplotlib.pyplot as p #modulo para graficar
import numpy #este modulo es para trabajar con matrices como en matlab
import matplotlib as mp
#mp.rcParams['xtick.labelsize']=13
#mp.rcParams['ytick.labelsize']=13

N=70  #numero de choques considerados

y=numpy.zeros(N+1)    #vector que almacena la altura donde se produce el choque
v=numpy.zeros(N+1)    #vector que almacena la velocidad después de cada choque
t=numpy.zeros(N+1)    #vector que almacena el tiempo en que se produce cada choque

y0=0   #condición inicial posición
y[0]=y0
v[0]=2  #condición inicial velocidad
t[0]=0  #el movimiento comienza en t=0

g=1  #aceleración de gravedad
A=1  #amplitud movimiento del suelo
w=1.785  #frecuencia del suelo
eta=0.15   #coeficiente de restitución
 


h=numpy.linspace(0.0000001,50.0000001,501)
#h=[0.00000001, 0.501, 1.001, 1.501, 2.001, 2.501, 3.001, 3.501, 4.001, 4.501, 5.001, 5.501, 6.001, 6.501, 7.001, 7.501, 8.001, 8.501, 9.001, 9.501, 10.001, 10.501, 11.001, 11.501, 12, 13]

for i in range(N):
    def zy(x):    #función altura de la pelota
        return (y[i]+v[i]*x-(0.5*numpy.power(x,2)))

    def vy(x):    #función velocidad de la pelota
        return v[i]-g*x

    def zs(x):   #función altura del suelo
        return A*sin(w*(x+t[i]) + 0)

    def vs(x):   #función velocidad del suelo
        return A*w*cos(w*(x+t[i]) + 0)

    def f(x):  #diferencia entre ambas alturas
        return zy(x)-zs(x)

    for j in range(len(h)):   
        if f(h[j])<0:   
            tc=optimize.brentq(f, h[0], h[j])  #determinación del cero de f
            break


    y[i+1]=zy(tc)  #altura del choque
    v[i+1]=(1+eta)*vs(tc) - eta*vy(tc)  #velocidad del choque
    t[i+1]=t[i]+tc   #tiempo del choque
  
    
k=numpy.zeros(N+1)  #vector que contiene el número de cada choque

for i in range(N):
    k[i+1]=k[i]+1

#for i in range(len(t-1)):
 #   if (t[i+1]-t[i])<0.05:
  #      Nrel=k[i+1]
   #     break

#print Nrel

p.plot(k,v, label='Velocidad')
#p.plot(k,y, label='Altura')
p.xlabel('Numero de choque')
p.ylabel('Velocidad')
p.legend(loc='upper right')
p.title('Velocidad despues de cada choque')
p.show()



