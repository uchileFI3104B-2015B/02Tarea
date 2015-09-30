'''
Este script...
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq
m=1
g=1
A=1
w=2
n=0.5
t_0=np.linspace( 0 , 5 ,100)

def y_p(t,y_0,v_0):
    return y_0+v_0*t-0.5*g*(t)**2
    return A*np.sin(w*t)
def resta(t,y_0,v_0):
    return y_p(t,y_0,v_0)-y_s(t)
def v_p(t,v_0):
    return v_0-g*t
def v_s(t):
    return A*w*np.cos(w*t)
raiz_brent=brentq(resta , 0.1, 5, args=(0,2.2) )
def v_p_choque(t,v_0):
    return (1+n)*v_s(t)-n*v_p(t,v_0)

print v_p_choque(raiz_brent,2.2)
print raiz_brent
plt.figure(1)
plt.clf()
plt.axvline(raiz_brent)
plt.plot(t_0,y_p(t_0,0,2.2))
plt.plot(t_0,y_s(t_0))
plt.show()

