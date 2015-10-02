import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq
plt.rc('text',usetex=True)
plt.rc('font', family='serif')

#### Parametros del problema

A = 1.
w = np.pi
m = 1.
g = 1.
VPF = 0
VP0 = 4
n = 0.4
VS = 0
Y0 = 0
t = np.linspace(0,10,10000)
###
Y = Y0 + VP0*t - (1/2.)*g*t**2
#VF = (1+n)VS -nVP0
YP = A*np.sin(w*t)
VP = A*w*np.sin(w*t)

def PosicionRelativa(t, PosicionN, VelocidadN,phi):
    Yrelativa = PosicionN + VelocidadN*t - (1/2.)*g*t**2 -



def SiguienteChoque(PosicionN, VelocidadN, N, SubiendoBajando):
    '''
    '''
    phi = np.arcsin(PosicionN)
    if SubiendoBajando == "Subiendo":
        phi = phi
    elif SubiendoBajando == "Bajando":
        phi = np.pi-phi
    else:
        return print 'Entrada invalida, entre "Subiendo" o "Bajando"'



    phi = np.arcsin(PosicionN)
    VS=-1*w*np.cos(wt)

    VPF = (1+n)*VS - n*VelocidadN
    #buscar el zero
    Raiz_brentq = brentq()
    YParticula = PosicionN + VelocidadN*t -(1/2.)*g*t**2
    Yaux = YParticula-Ysuelo
    #buscar cero de Yaux con intervalo PosicionN y y=-1 para la particula
    return YPF,VPF #tercer parametro que dice si el suelo termino subiendo o Bajando
