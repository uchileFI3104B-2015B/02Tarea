'''
Este script contiene el metodo que calcula
y_n+1, v'_n+1 a partir de y_n, v'_n
'''
import numpy as np
import matplotlib.pyplot as plt

def suelo(t,w,phi,A=1):
    return A*np.sin(w*t+phi)

def masa(t,y0,v0,g=1):
    return y0 + v0*t - (g/2.)*(np.power(t,2))

def outnchoque(yin,vin,w,signo):
    phi=np.arcsin(yin)
    if signo==-1:
        phi = -phi
    dtbrowse=min(np.pi/(20.*w),2*vin/20.)
    t=0
    while masa(t,yin,vin)>=suelo(t,w,phi):
        t+=dtbrowse
        print t

    ##Biseccion
    a=t-dtbrowse
    b=t
    p=(a+b)/2.
    counter=1
    eps=0.01
    max_iter=200
    while (np.fabs(masa(p,y0,v0)-suelo(p,w,phi))>=eps) and (counter<max_iter):
        if masa(p,y0,v0)-suelo(p,w,phi)==0:
            break
        if (masa(a,y0,v0)-suelo(a,w,phi))*(masa(p,y0,v0)-suelo(p,w,phi))<0:
            b = p
        else:
            a = p
        p = (a+b)/2.
        counter+=1
    #return yout, vout, signo
    return p

w=1
phiin=0
y0=0
v0=4
time=np.linspace(0,10,1000)
raiz=outnchoque(y0,v0,w,1)
plt.figure(1)
plt.plot(time,suelo(time,w,phiin),'b')
plt.plot(time,masa(time,y0,v0),'g')
plt.axvline(raiz, color='r')

plt.savefig('test.jpg')
