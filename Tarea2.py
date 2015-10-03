import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq
#plt.rc('text',usetex=True)
#plt.rc('font', family='serif')

#### Parametros del problema

A = 1.
m = 1.
g = 1.




def SiguienteChoque(PosicionN, VelocidadN, SubiendoBajando,w,n,pegados):

    '''
    La funcion SiguienteChoque entrega, dados parametros para un choque n, datos del choque n+1.

    Los Parametros de entrada son : -PosicionN: Posicion inicial o Posicion inmediatamente despues de un choque (para la particula)
                                    -VelocidadN: Velocidad inicial o  Velocidad inmediatamente despues de un choque (para la particula)
                                    -:SubiendoBajando: Si el suelo iba subiendo o bajando inicialmente o en el ultimo choque
                                    -w: Frecuencia para el piso
                                    -n: Coef. de restitucion
                                    -pegados : True si estan pegados, False si no.
    Retorna:
        (Posicion del siguiente choque,
        velocidad para la particula luego del siquiente choque,
        Si la plataforma iba subiendo o bajando en el siguiente choque,
        Si la particula termino pegada al suelo o no)


    '''
    if pegados == False:
        phi = np.arcsin(PosicionN)
        if SubiendoBajando == "Subiendo":
            phi = phi
        elif SubiendoBajando == "Bajando":
            phi = np.pi-phi
        else:
            return 'Entrada invalida, entre "Subiendo" o "Bajando"'

        def PosicionRelativa(t):
            Yrelativa = PosicionN + VelocidadN*t - (1/2.)*g*t**2 - np.sin(w*t+phi)
            return Yrelativa

        #buscar el zero

        tmax = 2*VelocidadN/g +(-VelocidadN+np.sqrt(VelocidadN**2 + 2*g*(PosicionN+1)))/g
        if PosicionRelativa(0.0001)*PosicionRelativa(tmax)>0: #la particula se pego al piso
            return 0,0,"Subiendo", True

        elif PosicionRelativa(0.0001)*PosicionRelativa(tmax)<0:


            Raiz_brentq = brentq(PosicionRelativa,0.0001,tmax)

            YN1 = np.sin(w*(Raiz_brentq)+phi)
            VN1 = (1+n)*(w*np.cos(w*(Raiz_brentq)+phi)) - n*(VelocidadN-g*Raiz_brentq)
            SoB = ""
            if np.cos(w*Raiz_brentq+phi)>0:   #Estas condiciones permiten saber si el suelo termino subiendo o bajando
                SoB = "Subiendo"            # esto se encuentra a partir del signo de la velocidad del suelo en el instante del choque
            elif np.cos(w*Raiz_brentq+phi)<0:
                SoB = "Bajando"
            elif np.cos(w*Raiz_brentq+phi)==0 and YN1>0:
                SoB = "Subiendo"
            elif np.cos(w*Raiz_brentq+phi)==0 and YN1<0:
                SoB = "Bajando"
            if np.cos(w*Raiz_brentq+phi)== VN1:
                Pegados = True
            else:
                Pegados = False
            return YN1, VN1, SoB, Pegados
    elif pegados == True:
        return 0,0,"Subiendo", True


### Parametros del problema 2


w = 1.66
n = 0.15
VP0 = 30

Esto = SiguienteChoque(0,VP0,"Subiendo",w,n,False)
Nchoques = 100
Velocidades = np.zeros(Nchoques+1)
Velocidades[0] = VP0
Choques = np.linspace(0,Nchoques,Nchoques+1)
for i in range(1,np.shape(Choques)[0]):
    Esto = SiguienteChoque(Esto[0],Esto[1],Esto[2],w,n,Esto[3])
    Velocidades[i] = Esto[1]
plt.plot(Choques,Velocidades,"-o")
plt.grid()
plt.title('Velocidad luego del choque enesimo con w = 1.66')
plt.xlabel('Choque')
plt.ylabel('Velocidad [m/s]')
plt.show()
###########
w = 1.67
n = 0.15
VP0 = 30

Esto = SiguienteChoque(0,VP0,"Subiendo",w,n,False)
Nchoques = 100
Velocidades = np.zeros(Nchoques+1)
Velocidades[0] = VP0
Choques = np.linspace(0,Nchoques,Nchoques+1)
for i in range(1,np.shape(Choques)[0]):
    Esto = SiguienteChoque(Esto[0],Esto[1],Esto[2],w,n,Esto[3])
    Velocidades[i] = Esto[1]
plt.plot(Choques,Velocidades,"-o")
plt.grid()
plt.title('Velocidad luego del choque enesimo con w=1.67')
plt.xlabel('Choque')
plt.ylabel('Velocidad [m/s]')
plt.show()
###########
w = 1.68
n = 0.15
VP0 = 30

Esto = SiguienteChoque(0,VP0,"Subiendo",w,n,False)
Nchoques = 100
Velocidades = np.zeros(Nchoques+1)
Velocidades[0] = VP0
Choques = np.linspace(0,Nchoques,Nchoques+1)
for i in range(1,np.shape(Choques)[0]):
    Esto = SiguienteChoque(Esto[0],Esto[1],Esto[2],w,n,Esto[3])
    Velocidades[i] = Esto[1]

plt.plot(Choques,Velocidades,"-o")
plt.grid()
plt.title('Velocidad luego del choque enesimo con w = 1.68')
plt.xlabel('Choque')
plt.ylabel('Velocidad [m/s]')
plt.show()
###########
w = 1.69
n = 0.15
VP0 = 30

Esto = SiguienteChoque(0,VP0,"Subiendo",w,n,False)
Nchoques = 100
Velocidades = np.zeros(Nchoques+1)
Velocidades[0] = VP0
Choques = np.linspace(0,Nchoques,Nchoques+1)
for i in range(1,np.shape(Choques)[0]):
    Esto = SiguienteChoque(Esto[0],Esto[1],Esto[2],w,n,Esto[3])
    Velocidades[i] = Esto[1]
plt.plot(Choques,Velocidades,"-o")
plt.grid()
plt.title('Velocidad luego del choque enesimo con w = 1.69')
plt.xlabel('Choque')
plt.ylabel('Velocidad [m/s]')
plt.show()
###########
w = 1.7
n = 0.15
VP0 = 30

Esto = SiguienteChoque(0,VP0,"Subiendo",w,n,False)
Nchoques = 100
Velocidades = np.zeros(Nchoques+1)
Velocidades[0] = VP0
Choques = np.linspace(0,Nchoques,Nchoques+1)
for i in range(1,np.shape(Choques)[0]):
    Esto = SiguienteChoque(Esto[0],Esto[1],Esto[2],w,n,Esto[3])
    Velocidades[i] = Esto[1]
plt.plot(Choques,Velocidades,"-o")
plt.grid()
plt.title('Velocidad luego del choque enesimo con w = 1.7')
plt.xlabel('Choque')
plt.ylabel('Velocidad [m/s]')
plt.show()
#####
######### Parte 4

w=1.66
n=0.15
VP0 = 30

while w<=1.79:
    Esto = SiguienteChoque(0,VP0,"Subiendo",w,n,False)
    Nchoques = 100
    Velocidades = np.zeros(Nchoques+1)
    Velocidades[0] = VP0
    WGraficar = np.ones(Nchoques+1)*w
    for i in range(1,np.shape(Choques)[0]):
        Esto = SiguienteChoque(Esto[0],Esto[1],Esto[2],w,n,Esto[3])
        Velocidades[i] = Esto[1]
    plt.plot(WGraficar[40:90],Velocidades[40:90],"o")
    plt.grid()
    plt.title('Velocidad luego del choque enesimo vs w')
    plt.xlabel('Frecuencia [rad/s]')
    plt.ylabel('Velocidad[m/s]')


    w+=0.01
plt.xlim(1.65,1.8)
plt.ylim(0,4)
plt.show()
