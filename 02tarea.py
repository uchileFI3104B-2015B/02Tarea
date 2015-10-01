import numpy as np
from pylab import *
from scipy import optimize
import matplotlib.pyplot as plt
'''------------------------------------------------------------------'''
#datos del problema
w=1.66
eta=0.15 #entre 0 y 1
v0=2 #mayor que w
'''----------------------------------------------------------------'''
def encontrar_cero(f,a,b,err=0.0001,itera=40):
    '''Funcion que recibe una funcion y encuentra un cero mediante el metodo de biseccion '''
    p = (a+b)/2.
    i = 1
    while(np.fabs(f(p))>err)and(i<itera):
        if f(p) == 0:
            return p
        if f(a) * f(p) > 0:
            a = p
        else:
            b = p
        p = (a + b)/2.
        i += 1
    return p

def busca_bajo_piso(f,dx,a=0.001,max_=10000):
    '''recorre la funcion con un paso dado hasta encontrar un punto donde sea negativa'''
    u=a
    i=0
    while (f(u) > 0) and (i < max_) :
        u+=dx
        i+=1
    if(i >= max_):
        print("No se encontró punto negativo")
    return (u,u-dx)

def avanzar_salto(yn,vn_prima):
    '''Funcion que recibe la posicion del choque n-esimo (yn),
    y la velcidad justo despues del choque n-esimo (vn_prima),
    y retorna la posicion del n+1 choque (yn+1) y la velocidad justo despues
    de este(vn+1_prima).'''
    #tn se define como el tiempo en que se produce el choque n-esimo
    tn = np.arcsin(yn)/w
    #definiremos funciones auxiliares a las cuales les buscaremos los ceros
    f_auxiliar = lambda t: yn-t**2/2.+t*vn_prima-np.sin(w*(t+tn))
    (a,b)=busca_bajo_piso(f_auxiliar,0.1)
    t1=encontrar_cero(f_auxiliar,a,b)
    #t1=scipy.optimize.brentq(f_auxiliar,a,b)
    yn1 = yn-t1**2/2.+t1*vn_prima
    vn1_prima = (1+eta)*w*cos(w*(t1+tn))-eta*(vn_prima-t1)
    return(t1,yn1,vn1_prima)

def llenar_choques(t0,y0,v0,cantidad):
    '''Recibe la cantidad de choques a computar, devuelve el tiempo y la posición en ue ocurren, además de la velocidad justo después de cada choque'''
    #intentaremos encontrar choques para luego graficarlos
    (tn,yn,vn)=([],[],[])
    tn.append(t0)
    yn.append(y0)
    vn.append(v0)
    for i in range (0,cantidad-1):
        (a,b,c)=avanzar_salto(yn[i],vn[i])
        tn.append(a+tn[i])
        yn.append(b)
        vn.append(c)
    return (tn,yn,vn)
'''---------------------------------------------------------------'''
#gráfico de los 2 primeros choques
plt.figure(1)
plt.clf()

(tn,yn,vn)=llenar_choques(0,0,v0,200)
t_values = np.linspace(0,18, 100)
y= lambda t: -t**2/2. + v0*t
y_values= [y(i) for i in t_values]

y2= lambda t: yn[1]-(t-tn[1])**2/2. + vn[1]*(t-tn[1])
y2_values= [y2(i) for i in t_values]
plt.title('Posiciones vs tiempo')
plt.xlabel('tiempo (s)')
plt.ylabel('Posicion (m)')
plt.ylim([-10,10])
plt.plot(t_values, np.sin(w * t_values), label='piso')
plt.plot(t_values, y_values,color='red', label='trayectoria inicial')
plt.plot(t_values, y2_values,color='y', label='trayectoria luego del choque')
plt.axvline(tn[1], color='g',label='Primer choque')
plt.axvline(tn[2], color='cyan',label='Segundo choque')
plt.legend()
plt.savefig('choques.png')
'''----------------------------------------------------------'''
#estimación Nrelax
plt.figure(2)
plt.clf()
plt.subplot(3, 1, 1)
plt.title ("$V_n'$ vs n")
plt.xlabel('numero de choques')
plt.ylabel('velocidad [m/s]')
n=np.linspace(0,200,200)
plt.plot(n,vn, label='velocidad para $\omega$=1.66')
plt.legend()

plt.subplot(3, 1, 2)
plt.xlabel('numero de choques')
plt.ylabel('velocidad [m/s]')
w=1.67
Nr=600
n=np.linspace(0,Nr,Nr)
(tn,yn,vn)=llenar_choques(0,0,v0,Nr)
plt.plot(n,vn,color='red',label='velocidad para $\omega$=1.67')
plt.legend()

plt.subplot(3, 1, 3)
plt.xlabel('numero de choques')
plt.ylabel('velocidad [m/s]')
w=1.672
Nr=600
n=np.linspace(0,Nr,Nr)
(tn,yn,vn)=llenar_choques(0,0,v0,Nr)
plt.plot(n,vn,color='g',label='velocidad para $\omega$=1.672')
plt.legend()
plt.savefig('Nrelax.png')
'''--------------------------------------------------------------------------'''
'''Siga usando η=0.15. Haga un gráfico de v'n
versus ω con ω entre 1.66 y 1.79 y n =2×Nrelax,..., 2×Nrelax + 49,
 es decir, ploteará 50 valores de v'n por cada valor de ω.
 Si algún valor de ω le parece interesante, haga la grilla más fina en ese sector.
'''
plt.figure(3)
plt.clf()
t0_w=0
y0_w=0
v0_w=0

for w in linspace(1.66,1.67,5):
    n=250
    (tn,yn,vn)=llenar_choques(t0_w,y0_w,v0_w,n)
    vn_values=vn[200:]
    t0_w=tn[n-1]
    y0_w=yn[n-1]
    v0_w=vn[n-1]
    w_values=np.ones(len(vn_values))*w
    plt.scatter(w_values,vn_values)

#valores interesantes
for w in linspace(1.67,1.675,10):
    n=250
    (tn,yn,vn)=llenar_choques(t0_w,y0_w,v0_w,n)
    vn_values=vn[200:]
    t0_w=tn[n-1]
    y0_w=yn[n-1]
    v0_w=vn[n-1]
    w_values=np.ones(len(vn_values))*w
    plt.scatter(w_values,vn_values)
#fin valores interesantes
for w in linspace(1.675,1.79,50):
    n=250
    (tn,yn,vn)=llenar_choques(t0_w,y0_w,v0_w,n)
    vn_values=vn[200:]
    t0_w=tn[n-1]
    y0_w=yn[n-1]
    v0_w=vn[n-1]
    w_values=np.ones(len(vn_values))*w
    plt.scatter(w_values,vn_values)
plt.xlabel('$\omega$ [rad/s]')
plt.ylabel("$V_n'$ estable [m/s]")
plt.title("$V_n'$ vs $\omega$")
plt.legend()
plt.savefig('bifurcacion.png')
show()
