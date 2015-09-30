'''
Este es el codigo es de la tarea 2. Se busca modelar el movimiento de
una pelota que se mueve verticalmente rebotando contra un suelo que
oscila sinusoidalmente con amplitud A y frecuencia omega
'''
import numpy as np
from scipy.optimize import brentq
from scipy.optimize import bisect
import matplotlib.pyplot as plt

def y_suelo(w,t):
    ''' Ecuacion de posicion de la pelota en funcion del tiempo  '''
    A = 1
    return A * np.sin (w*t)

def v_suelo(w,t):
    ''' Ecuacion de la velocidad del suelo en funcion del tiempo '''
    A = 1
    return A * w * np.cos(w*t)

def v_pelota(v0,t):
    ''' Ecuacion de la velocidad de la pelota en funcion del tiempo '''
    g = 1
    return v0 - g * t

def y_pelota(y0,v0,t):
    ''' Ecuacion de posicion de la pelota en funcion del tiempo '''
    g = 1
    return y0 + v0 * t - 0.5 * g * t**2

def resta(w,t,y0,v0,t_reb):
    ''' Retorna la distancia que hay entre la pelota y el suelo en un tiempo t '''
    #t = tiempo en el que se desea calcular la distancia
    #t_reb = tiempo rebote anterior
    A = 1
    g = 1
    return y_pelota(y0, v0, t-t_reb) - y_suelo(w, t)

def v_despreb(eta, vs_reb, vp_reb):
    '''' Retorna la velocidad justo despues del rebote'''
    #vs_reb = velocidad del suelo justo antes del rebote
    #vp_reb = velocidad de la pelota justo antes del rebote
    A=1
    g=1
    return (1 + eta)*vs_reb - eta * vp_reb

def nmasuno (w, eta, t_reb_n, yn, vn):
    '''
    Retorna los valores de Yn+1 y Vn+1 dados Yn y Vn (la posicion y
    velocidad luego del n-esimo choque). Tambien retorna el valor t*,
    es decir, el tiempo en el que ocurre el choque.
    '''
    def d(t):
        #Necesito que quede solo en funcion de t para poder usar brentq
        return resta (w,t,yn,vn,t_reb_n)

    #------Para encontrar dos tiempos usables en brenq-----#
    epsilon=0.01
    t_a = t_reb_n + epsilon
    while d(t_a) >0:
        t_a+=epsilon
    t_b=t_a-epsilon
    if d(t_a)*d(t_b)>0:
        return [t_a,0,yn]
        #condicion geometrica

    #---------------Calculo de valores-----------------#
    t_reb_n1 = bisect (d, t_a, t_b)  #tiempo del rebote n+1
    yn1 = y_pelota (yn, vn, t_reb_n1 - t_reb_n)
    vs_reb = v_suelo(w, t_reb_n1)
    vp_reb = v_pelota(vn, t_reb_n1 - t_reb_n)
    vn1 = v_despreb(eta, vs_reb, vp_reb)
    return [t_reb_n1, yn1, vn1]


eta = 0.15
y0 = 0
v0 = input('Valor v0?: ')

def Nrelax(w, eta, y0, v0):
    '''Retorna una matriz con los numeros de botes, y la velocidad
    asociada a dicho bote, para un valor especifico de omega.
    [Esto sirve para graficar] '''
    maxim= 152 #input('Maximo de iteraciones? ')
    N = np.zeros(maxim)
    v_n = np.zeros(maxim)
    y_n = np.zeros(maxim)
    t = np.zeros(maxim)

    i = 1
    v_n[0] = v0
    y_n[0] = y0
    while i<maxim:
        vector = nmasuno(w, eta, t[i-1], y_n[i-1], v_n[i-1])
        t[i] = vector[0]
        y_n[i] = vector[1]
        v_n[i] = vector[2]
        N[i] = i
        i+=1

    return [N, v_n]

Nrelax166=Nrelax(1.66,eta,y0,v0)
Nrelax168=Nrelax(1.68,eta,y0,v0)
Nrelax170=Nrelax(1.70,eta,y0,v0)


#------------------------PLOTS---------------------------
plt.figure(1)
plt.clf()
plt.plot(Nrelax166[0][0:80], Nrelax166[1][0:80], label='$\omega=1.66$')
plt.plot(Nrelax168[0][0:80], Nrelax168[1][0:80], label='$\omega=1.68$', color='green')
plt.plot(Nrelax170[0][0:80], Nrelax170[1][0:80], label='$\omega=1.70$', color='red')
plt.xlabel('Numero de rebotes')
plt.ylabel('Velocidad particula justo despues del rebote')
plt.legend()
plt.grid(True)
plt.savefig('Grafico_v0_70.eps')

#-------------------------------------

plt.figure(2)
plt.subplot(3,1,1)
plt.plot(Nrelax166[0], Nrelax166[1], label='$\omega=1.66$')
plt.legend()
plt.grid(True)

plt.subplot(3,1,2)
plt.plot(Nrelax168[0], Nrelax168[1], label='$\omega=1.68$', color='green')
plt.legend()
plt.grid(True)

plt.subplot(3,1,3)
plt.plot(Nrelax170[0], Nrelax170[1], label='$\omega=1.70$', color='red')
plt.legend()
plt.grid(True)

plt.savefig("Grafico_subplots_v0_70.eps")

#---------------------------------------

plt.figure(3)

n = 100 #N_relax es como 80

for omega in np.linspace(1.66, 1.7, 5):
    variable = Nrelax (omega, eta, y0, v0)
    Num_reb = variable[0]
    velocidades = variable[1]
    valores_veloc = velocidades[n:(n+50)]
    valores_omega = np.ones(len(valores_veloc)) * omega
    plt.scatter(valores_omega,valores_veloc)

plt.xlabel('$\omega$')
plt.ylabel('Velocidad particula justo despues del rebote')
plt.grid(True)
plt.savefig("Grafico_p4_v0_70.eps")


plt.show()
