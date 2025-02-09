import random, itertools
n=int(input('Valor para n: '))
'''
creo que hay que usar un itertool para todas las combinaciones posibles de A y B
de distancia entre 0 y n
'''
prom=0
for i in range(0,n): 
    A=random.randint(0,n) # 0 n
    B=random.randint(0,n) # 0 a n
    distancia=abs(A-B)
    prom=prom+distancia
prom=prom/n

print('Promedio de distancia: ',prom)
'''
Probar con 10, 100, 1000 y mas de 1000 so digo que 2000?
'''