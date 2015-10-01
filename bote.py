'''
Este script contiene el metodo que calcula
y_n+1, v'_n+1 a partir de y_n, v'_n. Ademas
requiere el signo de la velocidad del suelo
al momento del choque
'''
import numpy as np
import matplotlib.pyplot as plt

def suelo(t,w,phi,A=1):
    return A*np.sin(w*t+phi)

def velsuelo(t,w,phi,A=1):
    return A*w*np.cos(w*t+phi)

def masa(t,y0,v0,g=1):
    return y0 + v0*t - (g/2.)*(np.power(t,2))

def velmasa(t,v0,g=1):
    return v0 - g*t

def outnchoque(yin,vin,w,signo,eta):
    if yin>=1:
        yin=1
    elif yin<=-1:
        yin=-1
    phi=np.arcsin(yin)
    if signo==-1:
        phi = np.pi -phi
    dt=0.1 #min(np.pi/(20.*w),np.fabs(2*vin/20.))
    t=0.0001
    while masa(t,yin,vin)>=suelo(t,w,phi):
        t+=dt

    #Caso de que la masa m no se despegue
    #Es decir, avanzar el tiempo haria que la masa
    #quede bajo el suelo
    if t==0:
        dt=0.01
        yout=suelo(dt,w,phi)
        vout=(1+eta)*velsuelo(dt,w,phi)-eta*velmasa(dt,vin)
        signo=velsuelo(dt,w,phi)/np.fabs(velsuelo(dt,w,phi))
        return yout,vout,signo,dt

    ##Biseccion
    a=t-dt
    b=t
    p=(a+b)/2.
    counter=1
    eps=0.0001
    max_iter=40
    while (np.fabs(masa(p,yin,vin)-suelo(p,w,phi))>=eps) and (counter<max_iter):
        if masa(p,yin,vin)-suelo(p,w,phi)==0:
            break
        if (masa(a,yin,vin)-suelo(a,w,phi))*(masa(p,yin,vin)-suelo(p,w,phi))<0:
            b = p
        else:
            a = p
        p = (a+b)/2.
        counter+=1

    #Salida de los datos
    yout=suelo(p,w,phi)
    vout=(1+eta)*velsuelo(p,w,phi) - eta*velmasa(p,vin)
    signo=velsuelo(p,w,phi)/np.fabs(velsuelo(p,w,phi))
    return yout, vout, signo, p


# w=1.66
# phiin=0
# y0=0
# v0=2
# eta=0.15
# raiz=outnchoque(y0,v0,w,1,eta)
# raiz2=outnchoque(raiz[0],raiz[1],w,raiz[2],eta)
#
# time1=np.linspace(0,raiz[3],100)
# time2=np.linspace(raiz[3],raiz2[3]+raiz[3],100)
# time=np.linspace(0,10,100)
#
#
# plt.figure(1)
# plt.plot(time,np.sin(time*w),'b')
# plt.plot(time1,masa(time1,y0,v0),'g')
# plt.plot(time2,masa(time2-raiz[3],raiz[0],raiz[1]),'g')
# plt.axvline(raiz[3], color='r')
# plt.axvline(raiz2[3]+raiz[3], color='r')
#
# plt.savefig('test.jpg')
