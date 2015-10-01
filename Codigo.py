import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize as sc

plt.figure(1)
plt.clf()

global g
global m
global A
global w
global eta
A = 1.
m = 1.
g = 1.
w = 1.66
eta = 0.15

def y_suelo(t, phi):
    return A*np.sin(w*t + phi)

def v_suelo(t, phi):
    return A*w*np.cos(w*t + phi)

def get_y(t,yo,vo):
    y = -(0.5)*g*t**2 + vo*t + yo
    return y

def get_v(t,vo):
    return -g*t + vo

def h_abs(t,yo,vo,phi):
    return get_y(t,yo,vo) - y_suelo(t,phi)

def v_abs(t,yo,vo,phi):
    return get_v(t,vo) - v_suelo(t,phi)

def get_tcol(yo,vo,phi):
    '''
    Calcula el tiempo de colision de la pelota con la pared, dadas
    sus condiciones iniciales
    '''
    N = 1000
    tf = 10*w
    t_values = np.linspace(0, tf, N)
    i = 1
    while h_abs(t_values[i],yo,vo,phi)*h_abs(t_values[i+1],yo,vo,phi) >= 0:
        i += 1
        if i >= N-2:
            break
    t_col = t_values[i]
    t_col = sc.newton(h_abs, t_col ,args=(yo,vo,phi),maxiter = 100)
    return t_col

def col(yo,vo,phi):
    '''
    Funcion que retorna la posicion y velocidad de la pelota en la siguiente
    colision, tambien entrega la fase de la oscilacion del suelo en la colision.
    '''
    t_col = get_tcol(yo,vo,phi)
    y_col = get_y(t_col,yo,vo)
    v_col = get_v(t_col,vo)
    v_new = (1. + eta)*v_suelo(t_col,phi) - eta*v_col
    #if y_col <= y_suelo(t_col,phi) and v_new < v_suelo(t_col,phi):
        #y_col = y_suelo(t_col,phi)vu
        #v_new = v_suelo(t_col,phi)
    phi_col = w*t_col + phi
    return y_col, v_new, phi_col

tol = 1.0e-8 #Tolerancia de velocidad para decidir si la pelota se acopla al suelo
y = 0.
v = 4.
phi = 0.
t_col = 0
Ncol = 100
t_values = np.empty(0)
y_values = np.empty(0)
v_values = np.empty(0)
t_values = np.append(t_values, 0)
y_values = np.append(y_values, y)
v_values = np.append(v_values, v)

for i in range(1,Ncol,1):
    t_col = get_tcol(y,v,phi)
    y1 = col(y,v,phi)[0]
    v1 = col(y,v,phi)[1]
    phi = col(y,v,phi)[2]
    y = y1
    v = v1
    t_values = np.append(t_values, t_col + t_values[i-1])
    y_values = np.append(y_values, y)
    v_values = np.append(v_values, v)
    if v - v_suelo(t_col, phi) < tol:
        print("Pelota acoplada")
        break

ysuelo_values = y_suelo(t_values,0)
vsuelo_values = v_suelo(t_values,0)

tiempo = np.linspace(0,t_values[len(t_values)-1],1000)
y_sue = y_suelo(tiempo,0)
plt.plot(tiempo,y_sue)

plt.plot(t_values, y_values, marker='+', color='r')
plt.show()
