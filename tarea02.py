
import fisica as fis
from numpy import *
import matplotlib.pyplot as plt

""" Inicio script """

""" Vector de tiempo de la simulacion """
t = arange(0, 10, 0.01)
g = -1
eta = 0.5  # Coeficiente inelasticidad

""" Calculo funcion de movimiento del suelo """
A = 1
w = 1
desfase = 0

pos_suelo = fis.posicion_sinusoidal( A*0 , w , desfase , t )
vel_suelo = fis.velocidad_sinusoidal( A*0 , w , desfase , t )

""" Calculo funcion inicial de movimiento de particula """

y_0 = 0
v_0 = vel_suelo[0]*2 + 1

pos_particula = fis.posicion_caida_libre( y_0 , v_0 , g ,  t )
vel_particula = fis.velocidad_caida_libre( v_0 , g , t )

""" Correccion de funcion de movimiento de particula """

pos_dif = pos_particula - pos_suelo

for i in range( len(t) - 1 ):

    # Toca el suelo entre i e i+1
    if pos_dif[i+1] < 0:

        y_0 = pos_suelo[i+1]

        v_0 = fis.choque_inelastico_pared( vel_particula[i+1] , vel_suelo[i+1] , eta )

        t_0 = t[i+1]

        t_calc = t[(i+1):len(t)] - t_0

        pos_particula[ (i+1):len(t) ] = fis.posicion_caida_libre( y_0 , v_0 , g , t_calc )
        vel_particula[ (i+1):len(t) ] = fis.velocidad_caida_libre( v_0 , g , t_calc)

        pos_dif = pos_particula - pos_suelo





plt.plot( t, pos_suelo )
plt.plot( t , pos_particula )
#plt.plot( t , pos_dif )
plt.grid()
plt.show()
plt.draw()
