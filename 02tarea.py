import numpy as np
from pylab import *
import matplotlib.pyplot as plt
'''------------------------------------------------------------------'''
#datos del problema
w=1
eta=1 #entre 0 y 1
v0=2 #mayor que w
'''----------------------------------------------------------------'''
def avanzar_salto(yn,vn_prima):
    '''Funcion que recibe la posicion del choque n-esimo (yn),
    y la velcidad justo despues del choque n-esimo (vn_prima),
    y retorna la posicion del n+1 choque (yn+1) y la velocidad justo despues
    de este(vn+1_prima).'''
    #tn se define como el tiempo en que se produce el choque n-esimo
    tn = np.arcsin(yn)/w
    #definiremos funciones auxiliares a las cuales les buscaremos los ceros
    f_auxiliar = lambda t: yn-t^2/2+t*vn_prima-np.sin(w(t+tn))
    t1=encontrar_cero(f_auxiliar)
    yn1 = yn-t1^2/2+t1*vn_prima
    vn1_prima = (1+eta)*w*cos(w(t1+tn))-eta*(vn_prima-t1)
    return(yn1,vn1_prima)
'''----------------------------------------------------------------------'''
