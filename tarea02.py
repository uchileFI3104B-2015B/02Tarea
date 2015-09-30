
import fisica as fis
from numpy import arange, zeros
import matplotlib.pyplot as plt


""" SETUP ---------------------------------------------------------------------"""

""" Constantes """

g = -1  # Aceleracion de gravedad
eta = 0.5  # Coeficiente inelasticidad
A = 1	# Amplitud movimiento sinusoidal suelo
w = 2	# Frecuencia de osciliacion suelo
desfase = 0	# Desfase osciliacion suelo
t_ini = 0   # Tiempo de inicio simulacion
delta_t = 0.01  # Resolucion temporal
t_fin = 100 # Tiempo final simulacion

""" Vectores de la simulacion """

t = arange(t_ini, t_fin, delta_t)

pos_suelo = zeros(len(t))
vel_suelo = zeros(len(t))

pos_particula = zeros(len(t))
vel_particula = zeros(len(t))

def calcular_suelo( A , w , desfase , t ):

    global pos_suelo, vel_suelo

    pos_suelo = fis.posicion_sinusoidal( A , w , desfase , t )
    vel_suelo = fis.velocidad_sinusoidal( A , w , desfase , t )
# END calcular_suelo

def calcular_particula( t_0 , y_0 , v_0 , g , index ):

    """ Recalcula posicion y velocidad de la particula a partir de
    un indice index de t """

    global pos_particula, vel_particula, t

    new_t = t[ index:len(t) ] - t_0

    pos_particula [ index:len(pos_particula) ] = fis.posicion_caida_libre( y_0 , v_0 , g , new_t )
    vel_particula [ index:len(pos_particula) ] = fis.velocidad_caida_libre( v_0 , g , new_t )
# END calcular_particula

def calcular_choque( index ):
    """ Calcula los pasos a tomar para un choque ocurrido en index+1
    index es el valor del indice de t donde la particula cruza bajo el suelo """

    global t, eta

    y_0 = pos_suelo[index]
    v_0 = fis.choque_inelastico_pared( vel_particula[index] , vel_suelo[index] , eta )
    t_0 = t[index]
    calcular_particula(t_0 , y_0, v_0 , g, index)
# END calcular_choque

""" END SETUP -----------------------------------------------------------------"""

#################################################################################
""" Inicio script """

# Calculo funcion de movimiento del suelo
calcular_suelo( A , w , desfase , t )


# Calculo funcion inicial de movimiento de particula
y_0 = pos_suelo[0]
v_0 = vel_suelo[0]*2 + 1

calcular_particula( t[0] ,y_0 , v_0 , g , 0 )


# Correccion de funcion de movimiento de particula
pos_dif = pos_particula - pos_suelo

for i in range( len(t) - 1 ):

    # en i+1 aparece bajo el suelo
    if pos_dif[i+1] < 0:

        """ IMPLEMENTAR BUSQUEDA DE INDICE DE CHOQUE MAS VELOZ """
        calcular_choque( i + 1 )
        pos_dif = pos_particula - pos_suelo





plt.plot( t, pos_suelo )
plt.plot( t , pos_particula )
#plt.plot( t , pos_dif )
plt.grid()
plt.show()
plt.draw()
