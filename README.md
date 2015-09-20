# Tarea nro. 1
## FI3104B - Metodos Numericos Para la Ciencia y la Ingenieria
#### Prof. Valentino González

Considere una partícula de masa _m_ que se mueve verticalmente sólo en
el eje _Y_ rebotando contra un suelo que oscila sinusoidalmente con
amplitud _A_ y frecuencia &omega;. El choque contra el suelo es inelástico
siguiendo la siguiente regla de choque.

<img src='eqs/rebote.png' alt='rebote inelastico' height='40'>

> Latex:
    v\_p'(t^\*) = (1+\eta)v\_s(t^\*) - \eta v\_p(t^\*)

donde t<sup>\*</sup> es el instante del bote, v<sub>p</sub> y
v<sub>p</sub><sup>'</sup> son las velocidades justo antes y justo
despues del bote, y v<sub>s</sub> es la velocidad del suelo en ese
instante y &eta; es un coeficiente de restitución (&eta; entre 0, y
1; &eta;=1 corresponde al caso elástico).

Inicialmente la partícula está en contacto con el suelo y con velocidad
hacia arriba mayor que la velocidad del éste.

El sistema descrito tiende a generar soluciones estables (periódicas)
luego de un período de relajación. A veces la solución es trivial, con
la partícula pegándose al suelo y a veces no hay solución periódica.  La
solución periódica más sencilla es cuando la partícula rebota contra el
suelo con el mismo período que tiene la oscilación de éste.

Los parámetros del problema son (_A_, &omega;, &eta;, _m_, _g_) y la
condición inicial (_y_(0), _v_(0)). Adimensinalice el problema con
_m_=1, _g_=1, y _A_=1. _y_(0) ya se escogió (pegado al suelo), asi que
solo queda por elegir _v_(0), &eta; y &omega;.

1. Escriba una rutina que le permita calcular (y<sub>n+1</sub>,
   v<sup>'</sup><sub>n+1</sub>) dados (y<sub>n</sub>,
   v<sup>'</sup><sub>n</sub>): la posición y velocidad luego del n-ésimo
   choque.

   > Su tarea involucra buscar t<sup>\*</sup> en el cual la partícula y el
   > suelo chocan, pero note que puede haber multiples soluciones. Asegúrese de
   > que su programa encuentra la solución correcta.
   >
   > Una estrategia posible a seguir es avanzar la partícula en intervalos de
   > tiempo _pequeños_ hasta que se detecte que ha pasado a estar debajo del
   > suelo y buscar un cero entre este instante y el anterior. ¿Cómo define
   > _pequeño_?
   > 
   > La sugerencia anterior puede resultar en un programa lento en algunos
   > casos. ¿Qué otra alternativa puede seguir para mejorar la eficiencia del
   > programa y asegurar que la solución encontrada es la correcta?

1. Usando &eta;=0.15 y para &omega; = 1.66, _estime_ _N_<sub>relax</sub>, el
   número de botes necesarios para relajar el sistema.

   > No se pide un cálculo preciso de N<sub>relax</sub>, sólo una estimación.
   > Hay varias formas de hacer esto pero una muy sencilla es simplemente
   > plotear v<sup>'</sup><sub>n</sub> vs. n y chequear para qué valor de n
   > v<sup>'</sup><sub>n</sub> se ha estabilizado.

1. Pruebe con un par de otros valores para &omega; entre 1.66 y 1.7. ¿Es
   _N_<sub>relax</sub> comparable?

1. Siga usando &eta;=0.15. Haga un gráfico de v<sup>'</sup><sub>n</sub> versus
   &omega; con &omega; entre 1.66 y 1.79 y n =2&times;_N_<sub>relax</sub>,...,
   2&times;_N_<sub>relax</sub> + 49, es decir, ploteará 50 valores de
   v<sup>'</sup><sub>n</sub> por cada valor de &omega;. Si algún valor de
   &omega; le parece interesante, haga la grilla más fina en ese sector.

   > Al final de un ciclo con un valor de &omega;, conviene usar el estado
   > final para el estado inicial del &omega; siguiente.

