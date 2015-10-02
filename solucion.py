import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize as opt

A=1 #fijo
g=1 #fijo
m=1 #fijo
w=1.67
rest=0.15 #va de 0 a 1
n=60 #número de rebotes
eps=0.1

y=[]; #vector que contendrá las alturas de los choques
v=[]; #vector que contendrá las velocidades después de los choques
fase=[]; #vector que contendrá la fase del piso en cada choque

y=np.append(y,0) #cero corresponde a la posición inicial
v=np.append(v,60) #velocidad inicial, se puede cambiar
fase=np.append(fase,0) #cero es la fase inicial

def particle(t,y0,v0):
    yp=y0+v0*t-(1/2.)*g*t**2
    return yp
def velpart(t,v0):
    vp=v0-g*t
    return vp
def floor(t,phi):
    ys=A*np.sin(w*t+phi)
    return ys
def velfloor(t,phi):
    vs=A*w*np.cos(w*t+phi)
    return vs
def collision(t,v0,phi):
    vp_new=(1+rest)*velfloor(t,phi)-rest*velpart(t,v0)
    return vp_new

for i in range(1,n):
    def resta(t):
        r=particle(t,y[i-1],v[i-1])-floor(t,fase[i-1])
        return r
    inf=v[i-1]/g
    sup=(v[i-1]+np.sqrt(v[i-1]**2+2*g*(A+y[i-1])))/g
    while resta(inf)*resta(sup)>0: #cuando los puntos no están a lados contrarios del cero
        inf=inf-eps
        sup=sup+eps
    zero=opt.bisect(resta,inf,sup)
    y_new=particle(zero,y[i-1],v[i-1])
    v_new=collision(zero,v[i-1],fase[i-1])
    fase_new=np.arcsin((y[i-1]/A)+(v[i-1]*zero/A)-(g*zero**2/(2*A)))
    y=np.append(y,y_new)
    v=np.append(v,v_new)
    fase=np.append(fase,fase_new)

print(y)
print(v)

t=np.arange(10,n,1)
vplot=v[10:]
plt.figure()
plt.clf()
plt.plot(t,vplot,'bs')
plt.xlabel('Numero de rebotes')
plt.ylabel('Velocidad')
plt.savefig('grafico.png')
plt.show()
