import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq
plt.rc('text',usetex=True)
plt.rc('font', family='serif')

#### Parametros del problema

A = 1.
w = np.pi/10
m = 1.
g = 1.
VP0 = np.pi #w
n = 0.4




def SiguienteChoque(PosicionN, VelocidadN, SubiendoBajando):
    '''
    '''
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
    Raiz_brentq = brentq(PosicionRelativa,0.1,tmax)

    YN1 = np.sin(w*(Raiz_brentq)+phi)
    VN1 = (1+n)*(w*np.cos(w*(Raiz_brentq)+phi)) - n*(VelocidadN-g*Raiz_brentq)
    print "piso ", (w*np.cos(w*(Raiz_brentq)+phi)), "Pelota", VelocidadN-g*Raiz_brentq, "tiempo", Raiz_brentq
    SoB = ""
    if np.cos(w*Raiz_brentq+phi)>0:
        SoB = "Subiendo"
    elif np.cos(w*Raiz_brentq+phi)<0:
        SoB = "Bajando"
    elif np.cos(w*Raiz_brentq+phi)==0 and YN1>0:
        SoB = "Subiendo"
    elif np.cos(w*Raiz_brentq+phi)==0 and YN1<0:
        SoB = "Bajando"
    return YN1, VN1, SoB

Esto = SiguienteChoque(0,VP0,"Subiendo")
print Esto
