import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize as opt


#parametros
t=np.linspace(0, 2*np.pi, 100)
A=1
g=1
n=1
t_0=0
n=0.5
w=1
y0=0
v0=2

def ys(t):
    return A*np.sin(w*t)
def vs(t):
    return A*np.cos(w*t)
def yp(t,yn,vn):
    y=yn+(vn*t)-((1/2.)*g*t**2)
    return y
def vp(t,yn,vn):
    return vn-g*t
def rest(t,yv,vn):
    y=yp(t,yv,vn)-ys(t)
def choque(yn,vn):
    g=-1
    A=1
    ys=sen(t,A,w)
    yp=((1/2)*g*t**2)+vn*t+yn
    maxp=-vn/(g)
    minp=(-vn+(vn**2-4*g*(yn-A))**(0.5))/(2*g)
    y=yp-ys
    s = opt.bisect(y,maxp,minp)
    return s

yr=rest(t,y0,v0)
zero1=opt.newton(yr,4)
ys=ys(t)
yp=yp(t,y0,v0)



#plt.axvline(s,color='b')

plt.figure(1)
plt.clf()
plt.plot(t,ys,'g')
plt.plot(t,yp,'r')
plt.axvline()

plt.show()
