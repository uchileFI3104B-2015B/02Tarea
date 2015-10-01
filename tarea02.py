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

'''
Código para el movimiento del suelo
'''
pos_suelo = np.zeros(len(t))
vel_suelo = np.zeros(len(t))
for i in range(0,len(t)-1):
    pos_suelo[i] = A*sin(w*t[i])
    vel_suelo[i] = A*w*cos(w*t[i])
    
    
def particula(t):
    pass

def choque(A,w,t):
    pass


