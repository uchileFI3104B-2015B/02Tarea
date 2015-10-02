import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize as opt

def choque(vn,yn,tn,wi):
    A=1
    g=-1
    n=1
    t_0=0
    n=0.15
    w=wi
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


plt.figure(1)
plt.clf()

for wi in np.linspace(1.66,1.79,20):
    (wf,vf)=([],[])
    N=170
    Nrel=60
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
    vi=[]
    while i <= N:
        yn=y[i]
        vn=v[i]
        tn=t[i]
        z=choque(vn,yn,tn,wi)
        v_m=z[0]
        y_m=z[1]
        t_m=z[2]
        if i>=120:
            vi=np.append(vi,v_m)
            wf=np.append(wf,wi)
        v=np.append(v,v_m)
        y=np.append(y,y_m)
        t=np.append(t,t_m)
        i=i+1
        n=np.append(n,i)

#    vf=np.append(vn)
    plt.plot(wf,vi,'.')
plt.xlabel('Frecuencia de oscilacion del suelo')
plt.ylabel('Velocidad del regimen estable')
plt.draw()
plt.show()
