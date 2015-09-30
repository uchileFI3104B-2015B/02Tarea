import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize as opt



def choque(vn,yn):
    A=1
    g=-1
    n=1
    t_0=0
    n=0.15
    w=1.66
    ys= lambda x: A*np.sin(w*x)
    yp= lambda x: (((1/2.)*g*x**2)+vn*x+yn)
    y= lambda x: yp(x)-ys(x)
    vs= lambda x: A*np.cos(w*x)
    vp= lambda x: (g*x+vn)
    a=-vn/g
    b=(-vn-(vn**2-2*g*(yn+A))**(0.5))/g
    s = opt.bisect(y,a,b)
    v=(1+n)*vs(s)-n*vp(s)
    return v,s



plt.figure(1)
plt.clf()

N=50
v=[]
y=[]
v0=2
y0=0
v=np.append(v,v0)
y=np.append(y,y0)
i=0
n=[]
n=np.append(n,i)
while i <= N:
    yn=y[i]
    vn=v[i]
    z=choque(vn,yn)
    v_m=z[0]
    y_m=z[1]
    v=np.append(v,v_m)
    y=np.append(y,y_m)
    i=i+1
    n=np.append(n,i)

'''
para graficar el n de relajo para varios valores de v0
v0_n=(2, 5, 10, 20, 30, 40)
k=1
for v0 in v0_n:
    N=50
    v=[]
    y=[]
    y0=0
    v=np.append(v,v0)
    y=np.append(y,y0)
    i=0
    n=[]
    n=np.append(n,i)
    while i <= N:
        yn=y[i]
        vn=v[i]
        z=choque(vn,yn)
        v_m=z[0]
        y_m=z[1]
        v=np.append(v,v_m)
        y=np.append(y,y_m)
        i=i+1
        n=np.append(n,i)
    plt.subplot(611)
    plt.plot(n,v,'g')
    k=k+1

'''


plt.plot(n,v,'g')
plt.draw()
plt.show()
print v
print n
