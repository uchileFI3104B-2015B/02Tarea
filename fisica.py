
from math import *
from numpy import *

def posicion_sinusoidal( A , w , desfase , t ):

    return  A*sin(w*t + desfase)
# END posicion_sinusoidal


def velocidad_sinusoidal( A , w , desfase , t ):

    return A*w*cos(w*t + desfase)
# END velocidad_sinusoidal


def posicion_caida_libre( y_0 , v_0 , a , t):

    return a*t**2/2 + v_0*t + y_0
# END posicion_caida_libre


def velocidad_caida_libre( v_0 , a , t ):

    return a*t + v_0
# END velocidad_caida_libre


def choque_inelastico_pared( v_particula , v_pared , nu):

    new_v_particula = ( 1 + nu ) * v_pared - nu * v_particula

    return new_v_particula
# END choque_inelastico_pared
