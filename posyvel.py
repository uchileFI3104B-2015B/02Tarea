import matplotlib.pyplot as plt
import numpy as np
#from astropy import units as u
#from astropy import constants as v
#from scipy import integrate as s
#import time
from scipy.optimize import brentq
import matplotlib.pyplot as plt



#parametros
A=1
g=-1
n=1
t_0=0
n=0.3
w=1

def parab(x,a,b,c):
    y=((1/2)*a*x**2)+b*x+c
    return y

def sen(x,A,w):
    y=A*np.sin(w*x)
    return y



#def ys(t):
#    return sen(t,A,w)


y0=0
v0=4


def choque(y_n,v_n):
    g=-1
    A=1
    ys=A*np.sin(w*t)
    yp=((1/2)*g*t**2)+v_n*t+y_n
    maxp=-v_n/(g)
    minp=(-v_n+(v_n**2-4*g*(y_n-A))**(0.5))/(2*g)
    y=yp-ys
    s = brentq(y,maxp,minp)
    return s


    '''

ys=sen(t,A,w)
yp=parab(t,g,vn,yn)
maxp=-vn/(g)
minp=(-vn+(vn**2-4*g*(yn-A))**(1/2))/(2*g)
y=ys-yp
s = opt.bisect(y,maxp,minp)

'''

t=np.linspace(0, np.pi, 100)
ys=sen(t,A,w)
yp=(g/2)*t**2+v0*t+y0
b=choque(y0,v0)


plt.axvline(s,color='b')

plt.figure(1)
plt.clf()
plt.plot(t,ys,'g')
plt.plot(t,yp,'r')
plt.axvline()


plt.draw()
plt.show()
