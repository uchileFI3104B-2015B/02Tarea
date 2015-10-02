
import matplotlib.pyplot as plt
import numpy as np
t=np.linspace(0,15*np.pi,200)
g=1
A=1
w=1.68
eta=0.15
fase=0 #luego iremos agregando para tener el comportamiento real del suelo
#al momento del bote

#posicion suelo
def y1(t):
    y1=A * np.sin(w*(t+fase))
    return y1

#velocidad suelo
def v1(t):
    v1= A*np.cos(w*(t+fase))*w
    return v1

y0= y1(t)[0]
v0=12

#posicion masa
def y2(t):
    y2= -(g*(t**2)/2.0)+ y0+ v0*t
    return y2
#velocidad masa
def v2(t):
    v2=v0-g*t
    return v2

plt.figure(1)
plt.clf()
plt.plot(t,y1(t),'r')
plt.plot(t,y2(t),'b')
plt.title('Primera interseccion')
plt.show()

from scipy.optimize import bisect
from scipy.optimize import newton
from scipy.optimize import brentq
#interseccion
def intersect (t):
    r= y2(t) - y1(t)
    return r

#Calculando el tiempo para maximo de la curva y para el momento en que
#esta mas bajo que la amplitu del suelo

def tmax(y0,v0):
    for i in range(2,len(t)-1):
        tmax=0
        if g*t[i] >= v0 :
            tmax=t[i]
            break
    return tmax

def tt(y0,v0):
    for i in range(2,len(t)-1):
        tt=0
        if y2(t[i]) <= (-A) :
            tt=t[i]
            break
    return tt

#definiendo una funcion que dadas unas condiciones iniciales entrega
#las siguientes
def enesimo(y0,v0):
    a= bisect(intersect,tmax(y0,v0),tt(y0,v0))
    yn=y2(a)
    vn=((1+eta)*v1(a))- (eta*v2(a)) #los valores nuevos para las c.i
    #vn(t^*) = (1+\eta)v_s(t^*) - \eta v_p(t^*)
    return (a,np.fabs(yn),vn)

d=enesimo(y0,v0)
print d
plt.axvline(d[0])
#def botes(y0,v0):
bot=[]
vel=[]
tiempos=[]
plt.figure(2)

bot=[]
vel=[]
tiempos=[]
fase=0


for i in range(len(t)-1):
    nuevo=enesimo(y0,v0)
    fase+=nuevo[0] #tiempo (desde 0) en que da el bote
    tiempos= tiempos + [fase] #tiempos reales
    y0=nuevo[1]
    bot=bot + [y0] #altura de la masa en que da los botes
    v0=nuevo[2]
    vel=vel + [v0] #velocidad con que sale en cada bote
    #tpart=np.linspace(fase,10*np.pi,200)
    #plt.plot(tpart,y2(t),'b')
    n=len(bot) #numero de botes
    nn=np.linspace(0,n-1,n)
    plt.plot(nn,vel)

plt.figure(3)
nr=70
ome=np.linspace(1.67,1.68,50)
V= vel[nr:nr+50]
plt.plot(ome,V)
"w=1.66 N=35"
"w=1.67 N=190"
"w=1.68 N=6"
"w=1.69 N=10"


#c=np.linspace(1.66,1.7,10)
#for i in c:
#    w=i
#    print w
#    n=len(vel) #numero de botes
#    nn=np.linspace(0,n-1,n)
#    plt.plot(nn,vel)



#La fase es el tiempo desde 0 cada vez, entonces vemos
#que deja de rebotar cuando la fase es n y n+1 son muy pequenas
#print tiempos
#print bot

#print vel
#n=len(bot) #numero de botes
#nn=np.linspace(0,n-1,n)



#plt.figure(2)
#plt.plot(nn,vel)

plt.draw()
plt.show()
