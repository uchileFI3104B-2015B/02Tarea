#!/usr/bin/env python
###################################
#Se importan librerías importantes#
###################################
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq

#Algunos Parámetros
A=1.0
m=1.0
g=1.0
w=1.66
eta=0.75
T=-0.01

#Se busca definir las posiciones y velocidades tanto del
#suelo como de la partícula

def groundposition(t):
    '''
    Help on function groundposition:
    groundposition(time, angle, amplitude)
        Find the grounds position (having in consideration an unidimensional ground).
        Return float, the position of the ground in the Y axis.

        Description:
        Uses the classic formula for sinusoidal wave behavior, y=A*sin(w*t) to return
        the value of y.
        '''
        #es y(t)=A*sin(wt+b)
    return A*np.sin(w*t)
def groundvelocity(t):
    '''
    Help on function groundvelocity:
    groundvelocity(time, angle, amplitude)
        Find the grounds relative velocity.
        Returns float, the velocity of the ground in the Y axis.

        Description:
        Uses the classic formula for sinusoidal wave behavior, y=w*A*cos(w*t)
        to return
        the value of y.
        '''
        #es y(t)=w*A*cos(wt+b)
    return w*A*np.cos(w*t)
def particleposition(t,y_0,v_0):
    '''
    Help on function particleposition:
    particleposition(time, initial altitude, initial velocity)
        Find the particle position relative to a fixed coordinates
        sistem.
        Returns float, the position of the particle in the Y axis.

        Description:
        Uses the classic formula for a vertical launch in the Earth's
        surface
        y= h_0 - 0.5*g*t^2 + v_0*t
        '''
    return y_0 + v_0*t - 0.5*g*t**2
def particlevelocity(t,v_0):
    '''
    Help on function particlevelocity:
    particlevelocity(time, initial velocity)
        Find the particle position relative to a fixed coordinates
        sistem.
        Return float, the velocity of the particle in the Y axis.

        Description:
        Uses the classic formula for a vertical launch in the Earth's
        surface.
        y= -g*t + v_0
    '''
    return v_0 - g*t
def choque(groundvel,partvel):
    '''
    Help on function choque:
    choque(time, angle, restitution coefficient)
        Find the particle speed after collition, considering the absorption
        (the loss of velocity due to collition).
        Returns float, the speed of the particle.

        Description:
        Uses the not-so-classic formulae for restitution coefficient (eta),
        vp'(t*)=vs+ eta(vs-vp)
        with vp and vp'= particle's velocity just before and after the
        collition.
    '''
    return groundvel + eta*(groundvel-partvel)


############################
#INICIO PROGRAMA
############################
t=-0.01
rp=[]
rs=[]
hachocado= False
t_values=[]
while T<34:
    t+=0.01
    T+=0.01
    a=0
    if hachocado==False:
        y0=0.0
        v0=10.0
    def distax(tiempo):
        '''
        print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
        print 'Tiempo= ', T, '      ', t
        print 'Particula       Suelo'
        print particleposition(tiempo,y0,v0),'           ', groundposition(T)
        '''
        return particleposition(tiempo,y0,v0)-groundposition(T)
    d=distax(t)
    #print 'DISTANCIA= ', d
    print 'TIEMPO= ', T
    if d>0:
        rp=np.append(rp,particleposition(t,y0,v0))
        rs=np.append(rs,groundposition(T))
        t_values=np.append(t_values, T)


    if d<0:
        print 'distax= ', distax(t)
        print 'distax= ', distax(t-0.1)

        t_choque=brentq(distax,t,t-0.01)

        #print t_choque
        T=t_choque

        rp=np.append(rp,particleposition(t_choque,y0,v0))
        rs=np.append(rs,groundposition(T))
        t_values=np.append(t_values, T)

        hachocado=True
        y0=particleposition(t_choque,y0,v0)
        v0=choque(groundvelocity(T),particlevelocity(t_choque,v0))
        x=t
        t=0
        a=1
    if a==1:
        print 'xd'









plt.clf()
plt.plot(t_values,rp, 'b', label= 'Particula')
plt.plot(t_values,rs,'r',label='Suelo')
plt.xlabel('Tiempo [$s$]',fontsize=18)
#plt.xlim(0,8) #se agrega límite
plt.ylabel('Posicion [$cm$]',fontsize=18)
plt.title('Posicion vs Tiempo',fontsize=22)
plt.legend(loc=3)

plt.savefig('Posicion_pelota.png')
plt.draw()
plt.show()





























    #
