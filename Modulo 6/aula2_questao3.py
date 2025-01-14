import random


lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]
inter = list(set(lista1) & set(lista2))

print("Lista 1:", lista1)
print("Lista 2:", lista2)

print("Lista interseção ordenada:", sorted(inter))
for elemento in set(lista1):
    print(f"Elemento {elemento} aparece {lista1.count(elemento)} vezes na lista 1")
    
for elemento in set(lista2):
    print(f"Elemento {elemento} aparece {lista2.count(elemento)} vezes na lista 2")