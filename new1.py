import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize as opt

'''
La funcion choque entrega la posicion yn+1 y vn+1 en base a y y v.
Ademas, grafica la interseccion de las funciones. Esto permite comprobar que
para cualquier 
'''


def choque(vn,yn):
    A=1
    g=-1
    n=1
    t_0=0
    n=0.5
    w=1
    ys= lambda x: A*np.sin(w*x)
    yp= lambda x: (((1/2.)*g*x**2)+vn*x+yn)
    y= lambda x: yp(x)-ys(x)
    vs= lambda x: A*np.cos(w*x)
    vp= lambda x: (g*x+vn)
    a=-vn/g
    b=(-vn-(vn**2-2*g*(yn+A))**(0.5))/g
    s = opt.bisect(y,a,b)
    v=(1+n)*vs(s)-n*vp(s)
    return s,v

A=1
g=-1
n=1
t_0=0
n=0.5
w=1
yn=1
vn=4
a=-vn/g
b=(-vn-(vn**2-2*g*(yn+A))**(0.5))/g
t=np.linspace(yn, b, 100)
zn=choque(vn,yn)
z=zn[0]
zz=zn[1]
ys= lambda x: A*np.sin(w*x)
yp= lambda x: (((1/2.)*g*x**2)+vn*x+yn)
y= lambda x: yp(x)-ys(x)
plt.figure(1)
plt.clf()
plt.plot(t,ys(t),'g')
plt.plot(t,yp(t),'r')
plt.axvline(z)
plt.axvline(a)
plt.axvline(b)


plt.draw()
plt.show()

print z
print zz
