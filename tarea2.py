import numpy as np
from scipy.optimize import bisect
import matplotlib.pyplot as plt

'''Este script modela el rebote de una particula de masa m
en presencia de gravedad sobre una superficie que oscila
sinusoidalmente. Grafica n(rebotes) vs vn'(velocidad luego
del n-esimo rebote) para 2 frecuencias distintas para poder
estimar el n en que el sistema se estabiliza. Finalmente
se grafica n(rebotes) vs vn(velocidad luego
del n-esimo rebote) para frecuencias entre 1.66 y 1.776 para
n's en que se asegura que la situacion ya es estable.
'''
#condiciones iniciales
yo=0
vo=2
#coeficiente de restitucion entre 0 y 1
restitucion=0.15

#funciones de posicion de la particula y del suelo
def pos_p(yn,vn,t):
    return yn + vn*t-0.5*(t**2)
def pos_s(w,t,tn):
    return np.sin(w*(t+tn))

#funcion que resta la posicion de la particula con la posicion del suelo
def particula_menos_suelo(yn,vn,w,t,tn):
    return pos_p(yn,vn,t) - pos_s(w,t,tn)

#funcion choque, dado los parametros w, yn, vn, restitucion nos entrega t_choque,
#y_n1, v_n1.
def choque(w,yn,vn,restitucion):
    tn = np.arcsin(yn)/w
    def dist_ps(t):
        return particula_menos_suelo(yn,vn,w,t,tn)
    t_e=abs(2*vn)
    delta=1
    t_choque=bisect(dist_ps,t_e-delta,t_e+delta)
    y_n1=pos_p(yn,vn,t_choque)
    v_n1 = (1+restitucion)*w*np.cos(w*(t_choque+tn))-restitucion*(vn-t_choque)
    return t_choque, y_n1, v_n1

#funcion que da los vectores tn,yn,vn para la cantidad de choques que
#se escojan.
def n_choques(to,yo,vo,choques):
    (tn,yn,vn)=([],[],[])
    tn.append(to)
    yn.append(yo)
    vn.append(vo)
    for i in range (0,choques-1):
        (t,y,v)=choque(w,yn[i],vn[i],restitucion)
        tn.append(t+tn[i])
        yn.append(y)
        vn.append(v)
    return (tn,yn,vn)

#primera figura que contiene la grafica n vs vn para estimar N_relax
plt.figure(1)
plt.clf()

w=1.66
(tn,yn,vn)=n_choques(0,yo,vo,70)
n=np.arange(70)
plt.subplot(3,1,1)
plt.ylabel('$v_n$', fontsize=25)
plt.xlabel('cantidad de rebotes')
plt.plot(n,vn,label='$\omega_1=1.66$',color='g')
plt.legend()
plt.title('$N_{relax}$ para $\omega_1=1.66, \omega_2=1.685, \omega_3=1.7$', fontsize=18)

w=1.685
(tn,yn,vn)=n_choques(0,yo,vo,10)
n=np.arange(10)
plt.subplot(3,1,2)
plt.ylabel('$v_n$', fontsize=25)
plt.xlabel('cantidad de rebotes')
plt.plot(n,vn,label='$\omega_2=1.685$', color='r')
plt.legend()

w=1.7
(tn,yn,vn)=n_choques(0,yo,vo,10)
n=np.arange(10)
plt.subplot(3,1,3)
plt.ylabel('$v_n$', fontsize=25)
plt.xlabel('cantidad de rebotes')
plt.plot(n,vn,label='$\omega_3=1.7$')
plt.legend()

plt.draw()
plt.show()
plt.savefig('figura1.png')


#segunda figura

plt.figure(2)
plt.clf()
plt.xlim(1,2)

for w in np.linspace(1.66,1.776,30):
    (tn,yn,vn)=n_choques(0,yo,vo,150)
    vni=vn[100:]
    omega=w*np.ones(50)
    plt.plot(omega,vni,'o')


plt.xlim(1.65,1.8)
plt.xlabel('Frecuencia $\omega$ del suelo')
plt.ylabel('Velocidad de la particula en regimen estable')
plt.draw()
plt.show()
plt.savefig('figura2.png')
