import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq
#plt.rc('text',usetex=True)
#plt.rc('font', family='serif')

#### Parametros del problema

A = 1.
#w = np.pi/10
m = 1.
g = 1.
#VP0 = np.pi #w
#n = 0.4




def SiguienteChoque(PosicionN, VelocidadN, SubiendoBajando,w,n,pegados):

    '''
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
        print PosicionRelativa(0.1),"holas", PosicionRelativa(tmax)
        Raiz_brentq = brentq(PosicionRelativa,0.0001,tmax)

        YN1 = np.sin(w*(Raiz_brentq)+phi)
        VN1 = (1+n)*(w*np.cos(w*(Raiz_brentq)+phi)) - n*(VelocidadN-g*Raiz_brentq)
        SoB = ""
        if np.cos(w*Raiz_brentq+phi)>0:
            SoB = "Subiendo"
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


w = 1.7
n = 0.15
VP0 = 30

Esto = SiguienteChoque(0,VP0,"Subiendo",w,n,False)
print Esto
Nchoques = 100
Velocidades = np.zeros(Nchoques+1)
Velocidades[0] = VP0
Choques = np.linspace(0,Nchoques,Nchoques+1)
for i in range(1,np.shape(Choques)[0]):
    Esto = SiguienteChoque(Esto[0],Esto[1],Esto[2],w,n,Esto[3])
    Velocidades[i] = Esto[1]
print Velocidades, Choques
plt.plot(Choques,Velocidades,"-o")
plt.show()
