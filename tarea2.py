import numpy
from pylab import *
import matplotlib
A=1
w=1.66
g=1
nn=1
Yo=-0.5
Vo=2
Fase=arcsin(Yo/A)

def Vs(t):
    return w*A*np.cos(w*t+Fase)

def Ys(t):
    return A*np.sin(w*t+Fase)

def Yp(t):
    return Yo+Vo*t-g*(t**2)/2

t=np.arange(0, 300, 0.001)
Vpiso=Vs(t)
Ypiso=Ys(t)
Ypart=Yp(t)
laF=Ypart-Ypiso

for n in range(len(laF)):
    if laF[n]*laF[n+1]<0.0:
        treb=n*0.001
        print (treb)   
        break
    else:
        a=1

t=np.arange(0, treb, 0.001)
Vpiso=Vs(t)
Ypiso=Ys(t)
Ypart=Yp(t)

plot(t,Ypiso, color='k', label='Ypiso')
plot(t,Ypart, color='g', label='Ypart')

t2=np.arange(treb, 300, 0.001)
Yo=Yp(treb)
Vo=(1+nn)*Vs(treb)-nn*(Vo-g*treb)
'''
##Segundo rebote

t20=np.arange(0, 300-treb, 0.001)
Vpiso2=Vs(t2)
Ypiso2=Ys(t2)
Ypart2=Yp(t20)
laF2=Ypart2-Ypiso2

for n in range(len(laF2)):
    if laF2[n]*laF2[n+1]<0.0:
        treb2=n*0.001+treb
        print (treb2)   
        break
    else:
        a=1

t2=np.arange(treb, treb2, 0.001)
t20=np.arange(0, treb2-treb, 0.001)
Vpiso2=Vs(t2)
Ypiso2=Ys(t2)
Ypart2=Yp(t20)

Vpiso=np.concatenate((Vpiso,Vpiso2))
Ypiso=np.concatenate((Ypiso,Ypiso2))
Ypart=np.concatenate((Ypart,Ypart2))
t=np.concatenate((t,t2))


plot(t,Ypiso, color='k')
plot(t,Ypart, color='g')
'''

legend()

show()
