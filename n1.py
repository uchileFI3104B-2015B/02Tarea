import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize as opt

'''
programa que permite obtener posicion, velocidad y tiempo de un instante dadas
las mismas del instante anterior. tambien grafica para comprobar que el programa
funcione. se puede usar como prueba para ver que sucede durante choques
puntuales dadas ciertas condiciones de base.
'''

def choque(vn,yn,tn):
    #parametros
    A=1
    g=-1
    n=1
    t_0=0
    n=0.15
    w=1.66
    e=0.0001
    #difinicion de funciones
    ys= lambda x: A*np.sin(w*(x))
    yp= lambda x: (((1/2.)*g*(x-tn)**2)+vn*(x-tn)+yn)
    y= lambda x: yp(x)-ys(x)
    vs= lambda x: A*w*np.cos(w*(x))
    vp= lambda x: (g*(x-tn)+vn)
    das= lambda x: -a*w**3*np.cos(w*(x)) # se pretencia usar para cuando se
    #pegada al suelo
    a=-vn/g+tn
    b=(-vn-(vn**2-2*g*(yn+A))**(0.5))/g+tn
    #busca el caso en que la velocidad de la particula sea menor que la del piso
    #se plantea la posibilidad de mejorar este programa considerando los casos en
    #que las velocidades sean muy pequeñas. pendiende por implementar de forma funcional
    if vs(tn)<=vn:
        s=y(tn+e)*y(a)
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

#metodo de verificacion de que funcione la funcion choque
A=1
g=-1
n=1
t_0=0
n=0.15
w=1.66
'''

algunos valores de prueba
yn=0.1921
vn=2.1586
tn=3.9015

yn=0.53700736
vn=1.89096881
tn=185.80901541
'''
yn=0
vn=2
tn=0


ys= lambda x: A*np.sin(w*(x))
yp= lambda x: (((1/2.)*g*(x-tn)**2)+vn*(x-tn)+yn)
y= lambda x: yp(x)-ys(x)


a=-vn/g
b=(-vn-(vn**2-2*g*(yn+A))**(0.5))/g+tn
t=np.linspace(0, b, 500)
zn=choque(vn,yn,tn)
z=zn[1]
zz=zn[0]
zzz=zn[2]


plt.figure(1)
plt.clf()
plt.plot(t,ys(t),'g')
plt.plot(t,yp(t),'r')
plt.axvline(zzz)
plt.axvline(a)
plt.axvline(tn)

print z
print zz
print zzz

plt.draw()
plt.show()
