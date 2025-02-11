import random # importar librería random para la generación de valores aleatorios
from fractions import Fraction # importar librería Fraction para el manejo de fracciones
import matplotlib.pyplot as plt # importar librería matplotlib para la generación de gráficas

num_experimentos = 50000 # número de experimentos a realizar, recomendable mayor a 1000
def calcular_saltos_promedio(n, num_experimentos): # función para calcular el promedio de saltos promedio
    total_saltos = 0
    for _ in range(num_experimentos):
        # Seleccionar dos nodos diferentes A y B
        (A, B)= random.sample(range(n), 2) # se seleccionan dos nodos aleatorios diferentes

        # Calcular la distancia (número de saltos) entre A y B
        saltos = abs(A - B) # se calcula como el valor absoluto de la diferencia entre A y B
        
        # Sumar al total de saltos
        total_saltos += saltos
    
    # Calcular el promedio de saltos
    promedio_saltos = total_saltos / num_experimentos # obtener el promedio como número real
    prom_frac=Fraction(total_saltos, num_experimentos) # obtener el promedio en forma de fracción
    return promedio_saltos, prom_frac

# Tamaños de red a simular
tamanos_red = [10, 100, 1000] # 10 pequeño - 100 mediano - 1000 grande

# Listas para almacenar los resultados
promedios = []
tamanos = []

# Realizar la simulación para cada tamaño de red
for n in tamanos_red:
    promedio = calcular_saltos_promedio(n, num_experimentos)
    print(f"\nPara una red de {n} nodos, el promedio de saltos es: {promedio[0]} o {promedio[1]}")
    promedios.append(promedio[0])
    tamanos.append(n)

    #print(F"Promedio teórico: {(n+1)/3}")

# Grafica
# Graficar los resultados
#De linea
plt.plot(tamanos, promedios, marker='o')
plt.xlabel('Tamaño de la red (n)')
plt.ylabel('Promedio de saltos')
plt.title('Promedio de saltos vs Tamaño de la red')
plt.grid(True)
plt.show()

# De barras
TALLER No. 2 
 
PROBLEMA: Determine la cantidad de saltos promedio que recorrerá un (1) paquete 
que es enviado desde un emisor A hacia un receptor B, sobre una red punto a punto 
de topología bus o lineal compuesta por n nodos. Este promedio debe estar 
determinado como una expresión de la cantidad de nodos en la red. 
 
PLANTEAMIENTO DE LA SOLUCIÓN: Haciendo uso de la simulación, como método 
científico para imitar escenarios reales, vamos a realizar experimentos que nos permitan 
determinar o inferir esa cantidad promedio de saltos. La simulación debe tener en cuenta 
las siguientes condiciones: 
 
1. Se define como salto, la cantidad de enlaces de interconexión por las cuales 
tendrá que atravesar el paquete para ir del nodo en donde se encuentra A al nodo 
donde está B 
2. Se deberá simular escenarios para tres tipos de tamaño de la red, es decir, el 
valor de n (10 tamaño pequeño, 100 mediano y 1000 gran tamaño). La 
cantidad de experimentos sugeridos seria 1000+ para que su inferencia esté 
soportada en una gran cantidad de escenarios. 
3. Consideren que A y B estarán en nodos diferentes, en caso contrario, este 
escenario no debe ser tenido en cuenta. 
4. La simulación la podrán implementar en cualquier lenguaje de programación. 
(Sugerencia: Python por su facilidad, pero no es mandatorio) 
 
ENTREGABLES:  
• Un informe bien presentado por los integrantes del grupo, en la que se destaque 
las conclusiones de la simulación y la respuesta al problema. Anexa screenshots 
o pantallazos de tu simulación con sus resultados. El nombre del informe taller2
UserId1-UserId2-UserId3.pdf, donde UserId corresponde a los de cada 
estudiante del grupo (3 estudiantes). 
• Programa fuente en el que implementó la simulación 