# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 00:28:13 2015

@author: splatt
"""
import matplotlib.pyplot as plt
import math
import numpy as np
from scipy.optimize import brentq

A=1.
m=1.
g=1.

    
def YnVn(v0,eta,w,n,t0):
    def Y(t):
        return ((yn)+(vn*t)-((1./2.)*g*(t**2.)))
    def Z(t):
        return (A*math.sin(w*t))
    def H(t):
        return Y(t)-Z(tiempo+t)
    tiempo=t0
    vn=v0
    yn=Z(t0)
    print "v 0 =",vn
    print "y 0 =",yn
    while (Y(t0)-Z(t0))>=0:
        t0+=0.1
    raiz=brentq(H,t0-0.1,t0)
    print "raiz 1 =",raiz
    i=1
    tiempo=raiz
    while i<=n:
        yn=(A*math.sin(w*tiempo))
        vn=(1+eta)*(w*math.cos(w*tiempo))-eta*(vn-g*raiz)
        print "v",i,"=",vn
        print "y",i,"=",yn        
        ti=0
        while H(ti)>=0:
            ti+=0.1
        raiz=brentq(H,ti-0.1,ti)
        tiempo+=raiz
        i+=1
        print "raiz",i,"=",tiempo
        
    return np.array([vn,yn])
    
print YnVn(8.,0.5,1.5,3.,0.)

N1= np.linspace(0, 20, 21)
Vn=np.array([])
i=0
while i<=20:
    Vn=np.append(Vn,YnVn(4.,0.15,1.70,i,0.)[0])
    i+=1
print Vn
plt.figure(1)
plt.clf()
plt.plot(N1,Vn,'-')
plt.xlabel('Bote n')
plt.ylabel('Velocidad Vn')
plt.title('n-esimo bote v/s Velocidad luego de un bote')
plt.show()

Vn1=np.array([])
l=1.66
while l<=1.79:
    j=16
    while j<=65:
        Vn1=np.append(Vn1,YnVn(4.,0.15,l,j,0.)[0])
        j+=1
    l+=0.01
W1=np.linspace(0,49,50)
k=1.66
Wt=np.array([])
while k<=1.79:
    W1.fill(k)
    Wt=np.append(Wt,W1)
    k+=0.01
plt.figure(2)
plt.clf()
plt.plot(Wt,Vn1,'-')
plt.xlabel('frecuencia w')
plt.ylabel('Velocidad Vn')
plt.title('Frecuencia del suelo v/s Velocidad luego de un choque')
plt.show()

