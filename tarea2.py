import numpy as np
from scipy.optimize import bisect
import matplotlib.pyplot as plt

#parametros a utilzar
yo=0
vo=2
w=1.66
restitucion=0.15

#funciones de posicion y velocidad de la particula y el suelo
def pos_p(yo,vo,t):
    return yo + vo*t-0.5*(t**2)
def pos_s(w,yo,t):
    return np.sin(w*t+np.arcsin(yo))
def vel_p(vo,t):
    return vo-t
def vel_s(w,yo,t):
    return  np.cos(w*t+np.arcsin(yo))*w
def vel_prima_p(restitucion, w,yo,vo,t):
    return (1+restitucion) * vel_s(w,yo,t)- vel_p(vo,t)*restitucion

#funcion que resta la posicion de la particula con la del suelo
def particula_menos_suelo(yn,vn,w,t):
    return pos_p(yn,vn,t) - pos_s(w,yn,t)

#funcion choque para saltos relativamente grandes
def choque(w,yn,vn,restitucion):
    def dist_ps(t):
        return particula_menos_suelo(yn,vn,w,t)
    t_estimado=abs(vn*2) # tiempo estimado de choque de la particula con suelo.
    delta=0.5
    a=t_estimado-delta
    b=t_estimado+delta
    if a<0:
        a=0.1
    t_choque=bisect(dist_ps,a,b)
    y_n1=pos_p(yn,vn,t_choque)
    velocidad_s=vel_s(w,yn,t_choque)
    velocidad_p=vel_p(vn,t_choque)
    v_n1=vel_prima_p(restitucion, w, y_n1, velocidad_p, t_choque)
    return y_n1, v_n1, t_choque

#funcion choque1 para saltos chicos
def choque1(w,yn,vn,restitucion,a,b):
    def dist_ps(t):
        return particula_menos_suelo(yn,vn,w,t)
     # tiempo estimado de choque de la particula con suelo.
    if a<0:
        a=0.1
    t_choque=bisect(dist_ps,a,b)
    y_n1=pos_p(yn,vn,t_choque)
    velocidad_s=vel_s(w,yn,t_choque)
    velocidad_p=vel_p(vn,t_choque)
    v_n1=vel_prima_p(restitucion, w, y_n1, velocidad_p, t_choque)
    return y_n1, v_n1, t_choque


tiempo=np.linspace(0,20,10000)
reb=4 #4rebotes grandes
reb_peque=2 #2rebotes peque

s=(reb+reb_peque,3)
raices=np.zeros(s)
f=(reb+reb_peque,1000)
t_p=np.zeros(f)
vn=np.zeros(reb+reb_peque)
yn=np.zeros(reb+reb_peque)


plt.figure(1)
plt.clf()

q=0
posicion_s=pos_s(w,yo,tiempo)
plt.plot(tiempo,posicion_s, label='suelo',color='r')

for i in range(reb):
    raices[i]=choque(w,yo,vo,restitucion)
    t_p[i]=np.linspace(0,raices[i,2],1000)
    posicion_p=pos_p(yo,vo,t_p[i])
    if vel_s(w,yo,raices[i,2])<0:
        w=-abs(w)
    else:
        w=abs(w)
    plt.plot(t_p[i]+q,posicion_p,color='k')
    plt.axvline(raices[i,2]+q,color='y')
    yn[i]=yo
    vn[i]=vo

    q+=raices[i,2]
    #renovando valores
    yo= raices[i,0]
    vo= raices[i,1]

for i in range(reb,reb+reb_peque):
    raices[i]=choque1(w,yo,vo,restitucion,0.1,1.5)
    t_p[i]=np.linspace(0,raices[i,2],1000)
    posicion_p=pos_p(yo,vo,t_p[i])
    if vel_s(w,yo,raices[i,2])<0:
        w=-abs(w)
    else:
        w=abs(w)

    plt.plot(t_p[i]+q,posicion_p,color='k')
    plt.axvline(raices[i,2]+q,color='y')
    yn[i]=yo
    vn[i]=vo

    q+=raices[i,2]
    #renovando valores
    yo= raices[i,0]
    vo= raices[i,1]

plt.legend()
plt.draw()
plt.show()
