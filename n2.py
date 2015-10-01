import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize as opt

def choque(vn,yn,tn):
    A=1
    g=-1
    n=1
    t_0=0
    n=0.15
    w=1.66
    e=0.0001
    ys= lambda x: A*np.sin(w*(x))
    yp= lambda x: (((1/2.)*g*(x-tn)**2)+vn*(x-tn)+yn)
    y= lambda x: yp(x)-ys(x)
    vs= lambda x: A*w*np.cos(w*(x))
    vp= lambda x: (g*(x-tn)+vn)
    das= lambda x: -a*w**3*np.cos(w*(x))
    a=-vn/g+tn
    b=(-vn-(vn**2-2*g*(yn+A))**(0.5))/g+tn
    if vs(tn)<=vn:
        s=y(tn)*y(a)
        if s<0:
            t=opt.bisect(y,yn+e,a)
        else:
            t=opt.bisect(y,a,b)
        v=(1+n)*vs(t)-n*vp(t)
#        yd=ys(t)
    else:
        c=tn
        d=tn+np.pi/w
        t=opt.bisect(das,c,d)
        v=vs(t)

    p=ys(t)
    return v,p,t

'''
def choque(vn,yn,tn):
    A=1
    g=-1
    n=1
    t_0=0
    n=0.15
    w=1.66
    e=0.000001
    ys= lambda x: A*np.sin(w*(x-tn))
    yp= lambda x: (((1/2.)*g*(x-tn)**2)+vn*(x-tn)+yn)
    y= lambda x: yp(x)-ys(x)
    vs= lambda x: A*w*np.cos(w*(x-tn))
    vp= lambda x: (g*(x-tn)+vn)
    das= lambda x: -a*w**3*np.cos(w*(x-tn))
    a=-vn/g+tn
    b=(-vn-(vn**2-2*g*(yn+A))**(0.5))/g+tn
    if vs(tn)<=vn:
        s=yn*a
        if s<0:
            t=opt.bisect(y,yn+e,a)
        else:
            t=opt.bisect(y,a,b)
        v=(1+n)*vs(t)-n*vp(t)
#        yd=ys(t)
    else:
        c=tn
        d=tn+np.pi/w
        t=opt.bisect(das,c,d)
        v=vs(t)

    p=ys(t)
    return v,p,t
'''


plt.figure(1)
plt.clf()

N=50
v=[]
y=[]
t=[]
v0=2
y0=0
t0=0
v=np.append(v,v0)
y=np.append(y,y0)
t=np.append(t,t0)
i=0
n=[]
n=np.append(n,i)
while i <= N:
    yn=y[i]
    vn=v[i]
    tn=t[i]
    z=choque(vn,yn,tn)
    v_m=z[0]
    y_m=z[1]
    t_m=z[2]
    v=np.append(v,v_m)
    y=np.append(y,y_m)
    t=np.append(t,t_m)
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
print y
print t
