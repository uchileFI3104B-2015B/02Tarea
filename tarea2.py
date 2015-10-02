import numpy
from pylab import *
import matplotlib
#PARTE 1
#Definicion de funciones
def Vs(t):
    return w*A*np.cos(w*t+Fase)

def Ys(t):
    return A*np.sin(w*t+Fase)

def Yp(t):
    return Yo+Vo*t-g*(t**2)/2
#Ajuste de condiciones iniciales
A=1
w=float(input('w? : '))
g=1
nn=0.15
L=0       #Inicializacion de variables auxiliares que se modifican con cada iteración
t0=0      #
VN=[]    #Guarda los Vn
LL=[]     #Va sumando los N
#Condiciones iniciales ingresadas por el usuario
Yo=float(input('¿Posición en Y? (Para A='+str(A)+', Y debe estar entre [-'+str(A)+' y '+str(A)+']) : '))
if A!=0:                         #Revisa si el piso se mueve o no para agregar el desfase
    Fase=arcsin(Yo/A)    #     
else:                            #
    Fase=0                    #

S=float(input('¿El piso sube o baja en ese momento? [ 0 : Sube, 1 : Baja. ] : '))   #Metodo para arreglar el problema de desfase si el piso esta bajando
if S==0:                                                                                                         #(Por defecto el piso sube)
    t0=0                                                                                                          #
else:                                                                                                             #
    t=np.arange(0, 200, 0.0001)                                                                        #Use 200 como caso borde, para no alargar el programa mucho
    for a in Ys(t):                                                                                             #
        if a<Ys(0):                                                                                             #
            B=Ys(t).tolist()                                                                                   #
            K=B.index(a)                                                                                     # 
            break                                                                                                #
    t0=K/10000                                                                                               #

Vo=float(input('¿Velocidad? (Dada la posición, debe ser mayor que '+str(Vs(t0))+') : '))

N=float(input('¿Numero de botes? : '))
#Guardando Condiciones iniciales para la Parte 4
YoN=Yo
VoN=Vo
SN=S
FaseN=Fase
t0N=t0
#Comienzo
while L!=N:    
    if Vo<Vs(t0): #Excepcion
        print ('La partícula en el ultimo choque queda con velocidad menor a la del piso en ese momento ('+str(Vs(t0))+' , por lo tanto ya no rebotará otra vez (se pega).')
        break
    #Arreglos numericos
    t=np.arange(0, 200, 0.0001)
    Vpiso=Vs(t+t0)
    Ypiso=Ys(t+t0)
    Ypart=Yp(t)
    laF=Ypart-Ypiso #Funcion distancia de la particula al piso
    for n in range(len(laF)-1): #Buscando el cero de la Funcion
        if laF[n]*laF[n+1]<0.0: #
            treb=n*0.0001        #Tiempo de rebote
            break                    #
    #Arreglos numericos con el tiempo del rebote
    t=np.arange(0, treb, 0.0001)
    Vpiso=Vs(t+t0)
    Ypiso=Ys(t+t0)
    Ypart=Yp(t)
    
    #Entrega de datos
    print ('Tiempo transcurrido desde el último rebote '+str(treb))
    #Preparando condiciones iniciales y auxiliares para el siguiente rebote
    VN.append(Vo)
    LL.append(L)
    Yo=Yp(treb)
    Vo=(1+nn)*Vs(treb)-nn*(Vo-g*treb) #Ecuacion principal
    #Grafico
    plot(t,Ypiso, color='k', label='Ypiso')
    plot(t,Ypart, color='g', label='Ypart')
    legend()
    show()
    
    L+=1 #Contador de iteracion
    
    if Vo<Vs(treb): #Excepcion
        print ('Y'+str(L)+' = ' +str(Yo)+', V'+str(L)+' = ' +str(Vo))
        print ('La partícula en este choque queda con velocidad menor a la del piso en ese momento ('+str(Vs(treb))+' , por lo tanto ya no rebotará otra vez (se pega).')
        break
    #Entrega de datos
    print ('Y'+str(L)+' = ' +str(Yo)+', V'+str(L)+' = ' +str(Vo))
    #Ajustando el tiempo inicial para el proximo bote
    t0=treb+t0
    

print ('Tiempo total transcurrido desde el primer al ultimo rebote: '+str(t0)+'.')

#PARTE 2 Y 3 (Ajustando valores distintos de w y ejecutando el programa)
#Grafico Vn vs n
print ('A los '+str(L)+' rebotes el sistema se relaja, con w = '+str(w)+'.')
plot(LL,VN) 
title('Velocidad luego de N choques')
xlabel('n')
ylabel('Vn')
show()

print ('COMIENZO DE PARTE 4, Para volver a probar con otro w reinicie programa.')
#PARTE 4
#Copia del programa principal quitando partes innecesarias
W=[1.66,1.665,1.67,1.675,1.68,1.685,1.69,1.695,1.7, 1.705, 1.71, 1.715, 1.72, 1.725, 1.73, 1.735, 1.74, 1.745, 1.75, 1.755, 1.76, 1.765, 1.77, 1.775, 1.78, 1.785, 1.79]
#Iteracion para cada w
for w in W:
    #Condiciones iniciales auxiliares y guardadas
    L=0
    t0=0
    VN=[]
    LL=[]
    Yo=YoN
    Vo=VoN
    S=SN
    Fase=FaseN
    t0=t0N
    N=80 #Ajuste n a 80 para asegurar superar el 2*Nrelax por al menos 50

    #Base del programa principal
    while L!=N:
        t=np.arange(0, 200, 0.001)
        Vpiso=Vs(t+t0)
        Ypiso=Ys(t+t0)
        Ypart=Yp(t)
        laF=Ypart-Ypiso
        for n in range(len(laF)-1):
            if laF[n]*laF[n+1]<0.0:
                treb=n*0.001
                break
            else:
                a=1
    
        t=np.arange(0, treb, 0.001)
        Vpiso=Vs(t+t0)
        Ypiso=Ys(t+t0)
        Ypart=Yp(t)
        VN.append(Vo)
        LL.append(L)
        Yo=Yp(treb)
        Vo=(1+nn)*Vs(treb)-nn*(Vo-g*treb)
      
        L+=1
        t0=treb+t0
    #Expone graficos para cada w
    plot(LL,VN)
    xlabel('n')
    ylabel('Vn')
    title('w= '+str(w)+'.')
    show() 
print ('Fin')
