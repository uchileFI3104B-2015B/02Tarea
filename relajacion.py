'''
Este script define una funcion que permite
estudiar la convergencia de v'_n a medida que
el sistema va relajando.
'''
import numpy as np
import matplotlib.pyplot as plt
from bote import outnchoque

def Nrelax(w,eta):
    '''
    Esta funcion recibe como parametros la
    frecuencia de oscilacion del suelo y el
    coeficiente de restitucion. Como resultado
    crea una figura que permite evaluar
    visualmente si v'_n converge y de que forma
    lo hace.
    '''
    #Condiciones iniciales
    y=0 #posicion
    v=2 #velocidad
    s=1 #signo de la velocidad
    n=0 #numero de botes
    while n<100:
        out=outnchoque(y,v,w,s,eta)
        y=out[0] #posicion del choque
        v=out[1] #v' despues del choque
        s=out[2] #signo de v_s despues del choque
        n+=1
        plt.figure(1)
        plt.plot(n,v,'go')
    plt.xlabel('Numero de colisones $n$')
    plt.ylabel('Velocidad despues del bote $v\'_n$')
    plt.title('Comportamiento de $v\'_n$ versus la cantidad de botes $n$, $\omega =$ '+str(w))
    num=str(w)
    num=num.replace('.','')
    plt.savefig('estabilidad'+num+'.eps')
    return

if __name__ == '__main__':
    Nrelax(1.7,0.15)
