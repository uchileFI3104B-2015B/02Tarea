# -*- coding: utf-8 -*-

from math import *
import numpy as np
import matplotlib.pyplot as plt
'''
Definición de valores y vectores.
'''
g = -1 ; eta = 0.5 ; A = 1 ; w = 5	

'''
Condiciones iniciales
'''
t_inicio = 0.0  ; delta_t = 1.0 ; t_final = 30 
vel_inicialsuelo = 5.0 ; vel_inicialparticula = 10.0 ; pos_inicialparticula = 0.0
t = np.arange(t_inicio, t_final, delta_t)
pos_particula = np.zeros(len(t))
velP_particula = np.zeros(len(t))
pos_suelo = np.zeros(len(t))
vel_suelo = np.zeros(len(t))
vel_suelo[0] = vel_inicialsuelo
velP_particula[0] = vel_inicialparticula
pos_particula[0] = pos_inicialparticula
vel_ini=velP_particula[0] 
print velP_particula[0]

'''
Código para calcular el movimiento del suelo y la particula
'''

for i in range(1,len(t)-1):   
    pos_suelo[i] = A*sin(w*t[i])
    vel_suelo[i] = A*w*cos(w*t[i])              
    
    if pos_particula[i]<pos_suelo[i] and i>1:
        pos_particula[i] = pos_suelo[i]
        velP_particula[i] = (1+eta)*vel_suelo[i-1]-eta*velP_particula[i]
        vel_ini=velP_particula[i]  
        
    else:
        if velP_particula[i]>=0: 
            velP_particula[i]= vel_ini+g*t[i]
            pos_particula[i] = vel_ini*t[i]+(g*t[i]**2)/2
            
        else:      
            velP_particula[i]= g*t[i]
            pos_particula[i] = pos_particula[i-1] + (g*t[i]**2)/2
print velP_particula[0]
          
plt.plot(t,pos_particula,'r' )
plt.plot(t,pos_suelo,'b' )
plt.xlabel('Tiempo[s]')
plt.ylabel('Posiciones')
plt.grid(True)
plt.show()
        
     
'''
'''
