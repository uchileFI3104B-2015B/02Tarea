import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize as opt

'''
La funcion choque entrega la posicion yn+1 y vn+1 en base a y y v.
Ademas, grafica la interseccion de las funciones. Esto permite comprobar que
para cualquier vn e yn entrega los valores siguientes siempre que vn sea mayor
que la velocidad del plano (mayor que 1).
'''


def choque(vn,yn,tn):
    A=1
    g=-1
    n=1
    t_0=0
    n=0.15
    w=1.66
    ys= lambda x: A*np.sin(w*x)
    yp= lambda x: (((1/2.)*g*x**2)+vn*x+tn)
    y= lambda x: yp(x)-ys(x)
    vs= lambda x: A*w*np.cos(w*x)
    vp= lambda x: (g*x+vn)
    a=-vn/g
    b=(-vn-(vn**2-2*g*(yn+A))**(0.5))/g
    s = opt.bisect(y,a,b)
    v=(1+n)*vs(s)-n*vp(s)
    p=yp(s)
    return v,p,s

A=1
g=-1
n=1
t_0=0
n=0.15
w=1.66

vn=2
tn=0
ys= lambda x: A*np.sin(w*x)
yp= lambda x: (((1/2.)*g*x**2)+vn*x+tn)
y= lambda x: yp(x)-ys(x)
yn=yp(tn)


a=-vn/g
b=(-vn-(vn**2-2*g*(yn+A))**(0.5))/g
t=np.linspace(0, b, 500)
zn=choque(vn,yn,tn)
z=zn[1]
zz=zn[0]
zzz=zn[2]


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
print zzz
