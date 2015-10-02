import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize as sc

plt.figure(1)
plt.clf()

global g
global m
global A
global eta
A = 1.
m = 1.
g = 1.
eta = 0.15

def y_suelo(t, phi, w):
    return A*np.sin(w*t + phi)

def v_suelo(t, phi, w):
    return A*w*np.cos(w*t + phi)

def get_y(t,yo,vo):
    y = -(0.5)*g*t**2 + vo*t + yo
    return y

def get_v(t,vo):
    return -g*t + vo

def h_abs(t,yo,vo,phi,w):
    return get_y(t,yo,vo) - y_suelo(t,phi, w)

def v_abs(t,yo,vo,phi,w):
    return get_v(t,vo) - v_suelo(t,phi, w)

def get_tcol(yo,vo,phi, w):
    '''
    Calcula el tiempo de colision de la pelota con la pared, dadas
    sus condiciones iniciales
    '''
    N = 1000
    tf = 10*w
    t_values = np.linspace(0, tf, N)
    i = 1
    while h_abs(t_values[i],yo,vo,phi,w)*h_abs(t_values[i+1],yo,vo,phi,w) >= 0:
        i += 1
        if i >= N-2:
            break
    t_col = t_values[i]
    t_col = sc.newton(h_abs, t_col ,args=(yo,vo,phi, w),maxiter = 100)
    return t_col

def col(yo,vo,phi,w):
    '''
    Funcion que retorna la posicion y velocidad de la pelota en la siguiente
    colision, tambien entrega la fase de la oscilacion del suelo en la colision.
    '''
    t_col = get_tcol(yo,vo,phi,w)
    y_col = get_y(t_col,yo,vo)
    v_col = get_v(t_col,vo)
    v_new = (1. + eta)*v_suelo(t_col,phi,w) - eta*v_col
    #if y_col <= y_suelo(t_col,phi) and v_new < v_suelo(t_col,phi):
        #y_col = y_suelo(t_col,phi)vu
        #v_new = v_suelo(t_col,phi)
    phi_col = w*t_col + phi
    return y_col, v_new, phi_col

tol = 1.0e-8 #Tolerancia de velocidad para decidir si la pelota se acopla al suelo
y = 0.
v = 4.
phi = 0.
Ncol = 200
v_values = np.empty(0)
w_plot = np.empty(0)
v_values = np.append(v_values, v)
w_plot = np.append(w_plot, 1.66)
Nw = 50
w_values = np.linspace(1.66, 1.79, Nw)
for j in range(0, Nw, 1):
    w = w_values[j]
    for i in range(150,Ncol,1):
        t_col = get_tcol(y,v,phi,w)
        y1 = col(y,v,phi,w)[0]
        v1 = col(y,v,phi,w)[1]
        phi = col(y,v,phi,w)[2]
        y = y1
        v = v1
        v_values = np.append(v_values, v)
        w_plot = np.append(w_plot, w)
        if v - v_suelo(t_col, phi,w) < tol:
            print("Pelota acoplada")
            break

plt.plot(w_plot, v_values, marker='o', linestyle="none",color='g')
plt.show()

fig = plt.figure(1, figsize=(6, 4))
ax = fig.add_subplot(111)
ax.set_title('Velocidades en funcion de la frecuencia')

ax.set_xlabel('Frecuencia Angular')
ax.set_ylabel('Velocidad')
