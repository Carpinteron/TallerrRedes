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

#