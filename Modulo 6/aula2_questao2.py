import random

num_elementos = random.randint(5, 20)
elementos = [random.randint(1, 10) for _ in range(num_elementos)]

print("Lista de elementos:", elementos)
soma = sum(elementos)
print("Soma dos valores da lista:", soma)

media = soma / num_elementos
print("Média dos valores da lista:", media)