# -*- coding: utf-8 -*-
from math import *
import numpy as np
import matplotlib.pyplot as plt
'''
Definición de valores y vectores.
'''
g = -1 ; eta = 0.5 ; A = 1 ; w = 2	
desfase = 0	 ; t_inicio = 0  ; delta_t = 0.1  
t_final = 100 
t = np.arange(t_ini, t_fin, delta_t)
pos_particula = np.zeros(len(t))
velP_particula = np.zeros(len(t))
velP*_particula = np.zeros(len(t))
pos_suelo = np.zeros(len(t))
vel_suelo = np.zeros(len(t))
'''
Código para calcular el movimiento del suelo y la particula
'''

for i in range(0,len(t)-1):
    pos_suelo[i] = A*sin(w*t[i])
    vel_suelo[i] = A*w*cos(w*t[i])
    pos_particula[i] = 
    velP_particula[i] =(g*t[i]**2)/2
    if pos_particula[i]==pos_suelo[i]:
        velP*_particula[i] = (1+eta)*vel_suelo[i]-eta*velP_particula[i]
'''

'''

