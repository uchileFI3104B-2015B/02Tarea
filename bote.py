'''
Este script contiene el metodo que calcula
y_n+1, v'_n+1 a partir de y_n, v'_n. Ademas
contiene otras funciones auxiliares necesarias
para la ejecucion de ella.
'''
import numpy as np
import matplotlib.pyplot as plt

def suelo(t,w,phi,A=1):
    '''
    Esta funcion calcula la posicion del suelo,
    dado el instante de tiempo, la frecuencia
    angular, la fase asociada, y opcionalmente,
    la amplitud.
    '''
    return A*np.sin(w*t+phi)

def velsuelo(t,w,phi,A=1):
    '''
    Esta funcion calcula la velocidad del suelo,
    dado el instante de tiempo, la frecuencia
    angular, la fase asociada, y opcionalmente,
    la amplitud.
    '''
    return A*w*np.cos(w*t+phi)

def masa(t,y0,v0,g=1):
    '''
    Esta funcion calcula la posicion de la masa,
    dado el instante de tiempo, y las condiciones
    iniciales asociadas al movimiento.
    '''
    return y0 + v0*t - (g/2.)*(np.power(t,2))

def velmasa(t,v0,g=1):
    '''
    Esta funcion calcula la velocidad de la masa,
    dado el instante de tiempo, y las velocidad
    inicial.
    '''
    return v0 - g*t

def outnchoque(yin,vin,w,signo,eta):
    '''
    Esta es la funcion que calcula los valores
    de y_(n+1) y v'_(n+1) a partir de y_n, v'_n.
    Ademas recibe como parametros el signo de la
    velocidad del suelo (requerido para despejar
    de forma unica la trayectoria anterior del
    suelo en cada paso), la frecuencia de
    oscilacion del suelo y el coeficiente de
    restitucion.
    '''
    #Manejo de excepciones e inversion de la
    #fase, en caso de que la velocidad del suelo
    #sea negativa
    if yin>=1:
        yin=1
    elif yin<=-1:
        yin=-1
    phi=np.arcsin(yin)
    if signo==-1:
        phi = np.pi -phi

    #Experimentalmente se encontro que dt=0.1
    #era suficientemente pequeno para el rango
    #de w estudiado
    dt=0.1

    #Encontrar momento en que la diferencia entre
    #la posicion de la masa y la del suelo cambia
    #de signo
    t=0.0001
    while masa(t,yin,vin)>=suelo(t,w,phi):
        t+=dt

    #Caso de que la masa m no se despegue
    #Esto se hace para evitar que al avanzar el
    #tiempo la masa quede bajo el suelo
    if t==0.0001:
        yout=suelo(t,w,phi)
        vout=(1+eta)*velsuelo(t,w,phi)-eta*velmasa(t,vin)
        signo=velsuelo(t,w,phi)/np.fabs(velsuelo(t,w,phi))
        return yout,vout,signo,t

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

#Lo siguiente es para verificar el correcto
#funcionamiento del metodo antes definido
if __name__ == '__main__':
    #Condiciones iniciales
    y=0
    v=2
    s=1
    t=0

    #parametros
    w=1.66
    eta=0.15

    plt.figure(1)
    time=np.linspace(0,60,600)
    plt.plot(time,np.sin(time*w),'b')
    while t<60:
        out=outnchoque(y,v,w,s,eta)
        localt=np.linspace(0,out[3],100)
        plt.plot(localt+t,masa(localt,y,v),'g')
        y=out[0] #posicion del choque
        v=out[1] #v' despues del choque
        s=out[2] #signo de v_s despues del choque
        t+=out[3] #tiempo recorrido
        plt.plot(t,y,'ro')
    plt.xlabel('Tiempo')
    plt.ylabel('Posiciones del sistema')
    plt.title('Comportamiento del sistema en el tiempo, $\omega=1.66$ ')
    plt.xlim(0,60)
    plt.savefig('verificacion.eps')
