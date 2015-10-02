import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import bisect


#Datos
w=1.66    #frecuencia suelo
eta=0.15  #coeficiente de restitucion
v0=2      #mayor que velocidad suelo
A=1       #Amplitud
g=1       #adimencionalizada la gravedad


def down(f,delta,a=0.001,max_=10000):
    #funcion que recorre la funcion de entrada con un delta dado hasta encontrar un punto donde sea negativa para asi detenerse
    m=a
    i=0
    while (f(m) > 0) and (i < max_) :
        m+=delta
        i+=1
    if(i >= max_):
        print("No se pudo hallar el punto negativo")
    return (m,m-delta)

def then(yn,vn_p):
# Recibe la posicion del choque n-esimo y la velocidad justo despues del choque n-esimo
# Devuelve el tiempo del choque que viene, la posicion y velocidad luego del choque n-esimo más 1

    tn = np.arcsin(yn)/w                                              #tn es el tiempo en que se produce el choque n-esimo
    fcero = lambda t: yn-(t**2)*g/2.+t*vn_p-A*np.sin(w*(t+tn))          #funcion a la que le calcularemos los ceros.
    (a,b)=down(fcero,0.001)
    t1=bisect(fcero,a,b)                                              #ocupamos el metodo de biseccion esta vez
    vn1_p = (1+eta)*A*w*np.cos(w*(t1+tn))-eta*(vn_p-g*t1)
    yn1 = yn-(t1**2)*g/2.+t1*vn_p

    return(t1,yn1,vn1_p)

def collision(tcero,ycero,vcero,numero):
    #Recibe el numero de choques mas condiciones iniciales para finalmente devolver los arreglos de tiempo,velocidad y posicion de cada choque
    (tn,yn,vn)=([],[],[])
    tn.append(tcero)
    yn.append(ycero)
    vn.append(vcero)
    for i in range (0,numero-1):
        (b1,b2,b3)=then(yn[i],vn[i])
        tn.append(b1+tn[i])
        yn.append(b2)
        vn.append(b3)
    return (tn,yn,vn)

# EXTRA,Grafico caso elastico para particula ( solucion analitica para y0=0, sin roce y con suelo fijo )
plt.figure(1)
plt.clf()

t_valuesp=np.linspace(0,2*v0/g,100)
y= lambda t: -(t**2)*g/2. +v0*t
y_valuesp=[y(i) for i in t_valuesp]

t_values2 = np.linspace(2*v0/g,4*v0/g,100)
y2= lambda t: -((t-2*v0/g)**2)*g/2. + v0*(t-2*v0/g)
y2_values= [y2(i) for i in t_values2]

t_values3=np.linspace(4*v0/g,6*v0/g,100)
y3= lambda t: -((t-4*v0/g)**2)*g/2. + v0*(t-4*v0/g)
y3_values= [y3(i) for i in t_values3]

t_values4=np.linspace(6*v0/g,8*v0/g,100)
y4= lambda t: -((t-6*v0/g)**2)*g/2. + v0*(t-6*v0/g)
y4_values= [y4(i) for i in t_values4]


plt.title('Posicion v/s Tiempo (Caso elastico + suelo fijo)')
plt.xlabel('Tiempo [s]')
plt.ylabel('Posicion [m]')
plt.ylim([-8,8])
plt.xlim([0,17])
plt.plot(t_valuesp, y_valuesp,color='red', label='Recorrido inicial',linewidth='3.5')
plt.plot(t_values2, y2_values,color='black', label='Recorrido post 1choque',linewidth='3.5')
plt.plot(t_values3, y3_values,color='yellow', label='Recorrido post 2choque',linewidth='3.5')
plt.plot(t_values4, y4_values,color='magenta', label='Recorrido post 3choque',linewidth='3.5')
plt.legend()
plt.savefig('Elastic collision.png')



# EXTRA,Grafico de 4 choques iniciales


plt.figure(2)
plt.clf()

(tn,yn,vn)=collision(0,0,v0,400)
t_values = np.linspace(0,50,100)
y= lambda t: -(t**2)*g/2. + v0*t
y_values= [y(i) for i in t_values]

y2= lambda t: yn[1]-((t-tn[1])**2)*g/2. + vn[1]*(t-tn[1])
y2_values= [y2(i) for i in t_values]

y3= lambda t: yn[2]-((t-tn[2])**2)*g/2. + vn[2]*(t-tn[2])
y3_values= [y3(i) for i in t_values]

y4= lambda t: yn[3]-((t-tn[3])**2)*g/2. + vn[3]*(t-tn[3])
y4_values= [y4(i) for i in t_values]


plt.title('Posicion v/s Tiempo')
plt.xlabel('Tiempo [s]')
plt.ylabel('Posicion [m]')
plt.ylim([-10,10])
plt.xlim([0,20])
plt.plot(t_values, np.sin(w*t_values),color='orange', label='Suelo',linewidth='3.5')
plt.plot(t_values, y_values,color='y', label='Recorrido inicial',linewidth='3.5')
plt.plot(t_values, y2_values,color='red', label='Recorrido post 1choque',linewidth='3.5')
plt.plot(t_values, y3_values,color='blue', label='Recorrido post 2choque',linewidth='3.5')
plt.plot(t_values, y4_values,color='black', label='Recorrido post 3choque',linewidth='3.5')
plt.axvline(tn[1],color='cyan',label='1choque')
plt.axvline(tn[2], color='g',label='2choque')
plt.axvline(tn[3], color='black',label='3choque')
plt.axvline(tn[4], color='y',label='4choque')
plt.legend()
plt.savefig('Collisions.png')

# Nrelaxed

#Lineas + circulos
plt.figure(3)
plt.clf()
plt.subplot(3, 1, 1)
plt.title ("$V_n'$ v/s n")
plt.xlabel('Cantidad de choques')
plt.ylabel('Velocidad [m/s]')
n=np.linspace(0,400,400)
#plt.plot(n,vn,color='g',label='Velocidad para w=1.660 [rad/s]')
plt.scatter(n,vn,color='g',label='Velocidad para w=1.660 [rad/s]')
plt.legend()

plt.subplot(3, 1, 2)
plt.xlabel('Cantidad de choques')
plt.ylabel('Velocidad [m/s]')
w=1.684
c=550
n=np.linspace(0,c,c)
(tn,yn,vn)=collision(0,0,v0,c)
#plt.plot(n,vn,color='black',label='Velocidad para w=1.674 [rad/s]')
plt.scatter(n,vn,color='black',label='Velocidad para w=1.674 [rad/s]')
plt.legend()

plt.subplot(3, 1, 3)
plt.xlabel('Cantidad de choques')
plt.ylabel('Velocidad [m/s]')
w=1.698
c=580
n=np.linspace(0,c,c)
(tn,yn,vn)=collision(0,0,v0,c)
#plt.plot(n,vn,color='orange',label='Velocidad para w=1.698 [rad/s]')
plt.scatter(n,vn,color='orange',label='Velocidad para w=1.698 [rad/s]')
plt.legend()

#plt.savefig('Nrelaxed.png')
plt.savefig('Nrelaxed2.png')





plt.figure(4)
plt.clf()
ycero_w=0
tcero_w=0
vcero_w=0
colors = np.random.rand(50) #pelotitas de todos los colores. Tambien puedo poner c=u'colorquequiera'


for w in np.linspace(1.660,1.675,20):
    n=150    #numero de choques
    (tn,yn,vn)=collision(tcero_w,ycero_w,vcero_w,n)
    vn_values=vn[100:]
    ycero_w=yn[n-1]
    tcero_w=tn[n-1]
    vcero_w=vn[n-1]
    w_values=np.ones(len(vn_values))*w
    plt.scatter(w_values,vn_values,c=colors)


for w in np.linspace(1.675,1.79,50):
    n=150
    (tn,yn,vn)=collision(tcero_w,ycero_w,vcero_w,n)
    vn_values=vn[100:]
    ycero_w=yn[n-1]
    tcero_w=tn[n-1]
    vcero_w=vn[n-1]
    w_values=np.ones(len(vn_values))*w
    plt.scatter(w_values,vn_values,c=colors)
plt.xlabel('w [rad/s]')
plt.ylabel("$V_n'$ estable [m/s]")
plt.title("$V_n'$ v/s w")
plt.legend()
plt.savefig('Dispersion graphic.png')
