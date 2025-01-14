import random

lista = [random.randint(-10, 10) for _ in range(20)]

print("Lista original:", lista)

maior_quantidade_negativos = 0
intervalo_com_mais_negativos = None


tamanho_intervalo = 5

for i in range(0, len(lista), tamanho_intervalo):
    intervalo = lista[i:i+tamanho_intervalo]
    negativos = [num for num in intervalo if num < 0]
    
    if len(negativos) > maior_quantidade_negativos:
        maior_quantidade_negativos = len(negativos)
        intervalo_com_mais_negativos = (i, i + tamanho_intervalo)

if intervalo_com_mais_negativos:
    del lista[intervalo_com_mais_negativos[0]:intervalo_com_mais_negativos[1]]

print("Lista depois da deleção:", lista)