import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize as opti

'''
PARTE 1
definiremos una funcion choque, que reasigna una velocidad v_n1 para cada v_n, analogo para las posiciones y_inter y y_n.
Las funciones que devuelve están evaluada en "cero", que corresponde a las intersecciones de las posiciones de la superficie y la pelota.
Con esto, a partir de cada velocidad de la particula, podemos obtener la velocidad con la que rebota luego del impacto, junto con la
posicion en la cual ocurre.

def choques(y_n,v_n):
    A=1
    t_ini=0
    g= -1
    t_0=0
    n=0.15
    omega=1.66
    y_sup= lambda x: A*(np.sin(omega*x))   #posicion de la superficie
    y_pel= lambda x: y_n + v_n*x + ((x**2)*g)*(1/2.)    #posicion de la pelota, ecuacion de itinerario
    v_sup= lambda x: omega*A*(np.cos(omega*x))          #respectivas velocidades
    v_pel= lambda x: v_n + g*x
    inter= lambda x: y_pel(x) - y_sup(x)
    #Ahora definimos los limites para la biseccion
    a= (-1*v_n) * g
    b= ((-v_n - ((v_n)**2 - 2*(y_n+A)**(0.5)*g)))/g
    #encontramos las intersecciones
    cero=opti.bisect(inter,a,b)
    v_n1= (n+1)*v_sup(cero) - n*v_pel(cero)   #reformulamos la velocidad a partir de la ecuacion dada para v_p'(t)
    y_inter=y_pel(cero)

    return [y_inter,v_n1]



Iteraciones=input('ingrese numero de iteraciones')

#guardamos las velocidades de la pelota, justo despues del choque, en una lista
#v_0=input('ingrese velocidad inicial')
v_0=2
vel=[]
vel=np.append(vel,v_0)

#Guardaremos los "y" donde choca la pelota con la superficie en una lista
y_0=0
y_inter=[]
y_inter=np.append(y_inter,y_0)

#guardamos los intentos en una lista.
i=0
intento=[]
intento=np.append(intento,i)

#iteramos para obtener arreglos de las posiciones y las velocidades en las que chocan la pelota con la superficie.
while i <=Iteraciones:
    y_n = y_inter[i]
    v_n = vel[i]
    choque = choques(y_n,v_n)    #nos entrega la posicion y la velocidad de la pelota justo despues de impactar, Yn+1 y Vn+1
    v_choque = choque[1]
    y_choque = choque[0]
    y_inter = np.append(y_inter,y_choque)
    vel = np.append(vel,v_choque)
    i+=1
    intento=np.append(intento,i)


plt.plot(intento,vel)
plt.ylabel('Velocidad luego del impacto: Vn+1')
plt.xlabel('Numero de intento')
#plt.axis([0,(Iteraciones + 5),0,3])
plt.draw()
plt.show()
'''




'''
PARTE 2
Para esta parte basta repetir la iteracion para cada Velocidad inicial, luego implementeamos otra iteracion.




Iteraciones=input('ingrese el numero de iteraciones')


vel_iniciales= [2,3,4,5,6]


for k in vel_iniciales:

    v_0=k
    vel=[]
    vel=np.append(vel,v_0)
    #Guardaremos los "y" donde choca la pelota con la superficie en una lista
    y_0=0
    y_inter=[]
    y_inter=np.append(y_inter,y_0)
    #guardamos los intentos en una lista.
    i=0
    intento=[]
    intento=np.append(intento,i)
    #iteramos para obtener arreglos de las posiciones y las velocidades en las que chocan la pelota con el suelo.
    while i <=Iteraciones:
        y_n = y_inter[i]
        v_n = vel[i]
        choque = choques(y_n,v_n)
        v_choque = choque[1]
        y_choque = choque[0]
        y_inter = np.append(y_inter,y_choque)
        vel = np.append(vel,v_choque)
        i+=1
        intento=np.append(intento,i)

    plt.plot(intento,vel)
    plt.ylabel('Velocidad luego del impacto: Vn+1')
    plt.xlabel('Numero de intento')
    plt.axis([0,(Iteraciones + 5),0,3])
    plt.draw()
    plt.show()


    no supe como graficar todo en una foto, perdon. Aqui tocaria ticar un grafico para todos los Viniciales, para
    ver cuando empiezan a relajar, de todas formas puede verce en cada grafico por separado.
'''


'''
PARTE 4
Analogamente a la parte 2, haremos iterar la funcion para varios valores de la frecuencia, pero esta vez la funcion choques dependera
tambien de la frecuencia.
'''





def choques(y_n,v_n,omega):
    A=1
    t_ini=0
    g= -1
    t_0=0
    n=0.15
    y_sup= lambda x: A*(np.sin(omega*x))   #posicion de la superficie
    y_pel= lambda x: y_n + v_n*x + ((x**2)*g)*(1/2.)   #posicion de la pelota, ecuacion de itinerario
    v_sup= lambda x: omega*A*(np.cos(omega*x))
    v_pel= lambda x: v_n + g*x
    inter= lambda x: y_pel(x) - y_sup(x)
    #Ahora definimos los limites para la biseccion
    a= (*v_n) * (-1)*g
    b= ((-v_n - ((v_n)**2 - 2*(y_n+A)**(0.5)*g)))/g
    #encontramos las intersecciones
    cero=opti.bisect(inter,a,b)
    v_n1= (n+1)*v_sup(cero) - n*v_pel(cero)
    y_inter=y_pel(cero)

    return [y_inter,v_n1]







Iteraciones=input('ingrese el numero de iteraciones')

vel_iniciales= [2]
Q=input('ingrese el numero de frecuencias a considerar, se elijiran en un rango uniforme')
Salto=(1.79-1.66)/Q
Omegas= np.arange(1.66, 1.79, Salto)

for k in Omegas:

    v_0=2
    vel=[]
    vel=np.append(vel,v_0)
    #Guardaremos los "y" donde choca la pelota con la superficie en una lista
    y_0=0
    y_inter=[]
    y_inter=np.append(y_inter,y_0)
    #guardamos los intentos en una lista.
    i=0
    intento=[]
    intento=np.append(intento,i)
    #iteramos para obtener arreglos de las posiciones y las velocidades en las que chocan la pelota con el suelo.
    while i <=Iteraciones:
        y_n = y_inter[i]
        v_n = vel[i]
        choque = choques(y_n,v_n,k)
        v_choque = choque[1]
        y_choque = choque[0]
        y_inter = np.append(y_inter,y_choque)
        vel = np.append(vel,v_choque)
        i+=1
        intento=np.append(intento,i)

    plt.plot(intento,vel)
    plt.ylabel('Velocidad luego del impacto: Vn+1')
    plt.xlabel('Numero de intento')
    #plt.axis([0,(Iteraciones + 5),0,3])
    plt.draw()
    plt.show()
