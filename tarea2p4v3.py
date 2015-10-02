from math import *
from scipy import integrate as int
from scipy import optimize 
import pyfits #modulo para leer archivos fits
import matplotlib.pyplot as p #modulo para graficar
import numpy #este modulo es para trabajar con matrices como en matlab
import matplotlib as mp
#mp.rcParams['xtick.labelsize']=13
#mp.rcParams['ytick.labelsize']=13

N=70

y=numpy.zeros(N+1)
v=numpy.zeros(N+1)
t=numpy.zeros(N+1)
altmax=numpy.zeros(N+1)

altmax[N]=0

y0=0
y[0]=y0
v[0]=2
t[0]=0

g=1
A=1
w=numpy.linspace(1.64,1.79,51)

eta=0.15


vf=numpy.zeros((50,len(w)))



h=[0.00000001, 0.501, 1.001, 1.501, 2.001, 2.501, 3.001, 3.501, 4.001, 4.501, 5.001, 5.501, 6.001, 6.501, 7.001, 7.501, 8.001, 8.501, 9.001, 9.501, 10.001, 10.501, 11.001, 11.501, 12, 13]

#h=numpy.linspace(0.0001,20.0001,101)

for m in range(len(w)):
    
    for i in range(N):
        def zy(x):
            return (y[i]+v[i]*x -(0.5*numpy.power(x,2)))

        def vy(x):
            return v[i]-g*x

        def zs(x):
            return A*sin(w[m]*(x+t[i]) + c)

        def vs(x):
            return A*w[m]*cos(w[m]*(x+t[i]) + c)

        def f(x):
            return zy(x)-zs(x)

        for j in range(len(h)):
            if f(h[j])<0:
                tc=optimize.brentq(f, h[0], h[j])
                break

     

        y[i+1]=zy(tc)
        v[i+1]=(1+eta)*vs(tc) - eta*vy(tc)
        t[i+1]=t[i]+tc

    for i in range(50):
        vf[i,m]=v[N-49+i]
    
    
        
    v[0]=v[N]    #La condición final de un caso es la inicial del siguiente
    y[0]=y[N]
    if vs(0)>0:
        c=asin(y[0]/A)
    else:
        c=pi-asin(y[0]/A)

    
      
k=numpy.zeros(N+1)

for i in range(N):
    k[i+1]=k[i]+1



for i in range(50):
    p.plot(w, vf[i,:], 'o')



p.xlabel('Frecuencia angular [rad/s]')
p.ylabel('Velocidad')
p.title('Velocidades de relajacion para cada frecuencia')
p.show()








    


