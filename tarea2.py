'''
Este es el codigo es el de la tarea 2.
Despues definire si voy a separar los codigos de cada pregunta
o hacerlos todos aqui
'''
import numpy as np
from scipy.optimize import brentq
import matplotlib.pyplot as plt

def y_suelo(w,t):
    '''
    Ecuacion de posicion de la pelota en funcion del tiempo
    '''
    A=1
    return A * np.sin (w*t)

def v_suelo(w,t):
    '''
    Ecuación de la velocidad del suelo en funcion del tiempo
    '''
    A=1
    return A * w * np.cos(w*t)

def v_pelota(v0,t):
    '''
    Ecuacion de la velocidad de la pelota en funcion del tiempo
    '''
    g=1
    return v0-gt

def y_pelota(y0,v0,t):
    '''
    Ecuacion de posicion de la pelota en funcion del tiempo
    '''
    g=1
    return y0 + v0 * t - 0.5 * g * t**2

def distancia(w,t,y0,v0):
    '''
    Retorna la distancia que hay entre la pelota y el suelo en un tiempo t
    '''
    A=1
    g=1
    return y_suelo(w,t) - y_pelota(y0,v0,t)

def v_despreb(n, w, t_reb, v0):
    ''''
    Retorna la velocidad justo despues del rebote
    '''
    A=1
    g=1
    return (1 + n)*v_suelo(w, t_reb) - n * v_pelota(v0,t_reb)

def nmasuno (w, n, t_reb_n, yn, vn):
    '''
    Retorna los valores de Yn+1 y Vn+1 dados Yn y Vn (la posicion y
    velocidad luego del n-esimo choque). Tambien retorna el valor t*,
    es decir, el tiempo en el que ocurre el choque.
    '''
    def d(t):
        #Necesito que quede solo en funcion de t para poder usar brentq
        return distancia (w,t,yn,vn)

    epsilon=0.001
    t_a = t_reb_n + epsilon #asi empiezo a recorrerde despues del tiempo del rebote n
    t_b = t_reb_n

    while d(t_a) >=0:
        t_a+=epsilon
        t_b+=epsilon

    t_reb_n1 = brentq (resta, t_a, t_b)  #tiempo del rebote n+1
    #las funciones de posicion estan definidas para un tiempo
    #que se reinicia tras cada rebote
    yn1 = y_pelota (yn, vn, t_reb_n1-t_reb_n)
    vn1 = v_despreb(n, w, t_reb_n1, vn)
    return [t_reb_n1, yn1, vn1]


n=0.15
w=1.66
y0=0
