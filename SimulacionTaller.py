import random
num_experimentos=1000
def calcular_saltos_promedio(n, num_experimentos):
    total_saltos = 0
    for _ in range(num_experimentos):
        # Seleccionar dos nodos diferentes A y B
        A, B = random.sample(range(n), 2)
        
        # Calcular la distancia (número de saltos) entre A y B
        saltos = abs(A - B)
        
        # Sumar al total de saltos
        total_saltos += saltos
    
    # Calcular el promedio de saltos
    promedio_saltos = total_saltos / num_experimentos
    return promedio_saltos

# Tamaños de red a simular
tamanos_red = [10, 100, 1000]

# Realizar la simulación para cada tamaño de red
for n in tamanos_red:
    promedio = calcular_saltos_promedio(n, num_experimentos)
    print(f"Para una red de {n} nodos, el promedio de saltos es: {promedio}")