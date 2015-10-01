'''
Este script...
'''
import numpy as np
import matplotlib.pyplot as plt
from bote import masa
from bote import outnchoque

#Parametros
w=np.linspace(1.66,1.79,100)
eta=0.15

#Condiciones iniciales
y=0
v=2
s=1
t=0

#Evolucion de particula
i=0 #contador de w
while i<100:
    n=0 #contador de botes
    while n<100:
        #print n
        out=outnchoque(y,v,w[i],s,eta)
        #if i==1:
            #localt=np.linspace(0,out[3],100)
            #plt.plot(localt+t,masa(localt,y,v),'g')
        y=out[0] #posicion del choque
        v=out[1] #v' despues del choque
        s=out[2] #signo de v_s despues del choque
        t+=out[3] #tiempo recorrido
        #if i==1:
            #plt.axvline(t, color='r')
        n+=1
        if n>50:
            plt.figure(1)
            plt.plot(w[i],v,'bo')
            #print v
        if i==3:
            plt.figure(2)
            plt.plot(n,v,'go')
            if n==99:
                plt.savefig('stabil.eps')
    i+=1

plt.savefig('bifurcacion.eps')


#time=np.linspace(0,t,1000)
#plt.plot(time,np.sin(time*w),'b')
#plt.savefig('botes.jpg')
#plt.savefig('botes.eps')
