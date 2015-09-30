import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize as opt



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
    a=-vn/g
    b=(-vn-(vn**2-2*g*(yn+A))**(0.5))/g
    s = opt.brentq(y,a,b)
    return s


A=1
g=-1
n=1
t_0=0
n=0.5
w=1
yn=17
vn=1
a=-vn/g
b=(-vn-(vn**2-2*g*(yn+A))**(0.5))/g
t=np.linspace(yn, b, 100)
z=choque(vn,yn)
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
