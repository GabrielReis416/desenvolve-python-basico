def receber_lista(nome_lista):
    
    lista = []
    while True:
        try:
            entrada = input(f"Digite os números para {nome_lista}, separados por espaço: ")
            lista = list(map(int, entrada.split()))
            break
        except ValueError:
            print("Por favor, insira apenas números inteiros, separados por espaço.")
    return lista

lista1 = receber_lista("lista 1")
lista2 = receber_lista("lista 2")

lista_resultante = []
tamanho_minimo = min(len(lista1), len(lista2))
for i in range(tamanho_minimo):
    lista_resultante.append(lista1[i])
    lista_resultante.append(lista2[i])

lista_resultante.extend(lista1[tamanho_minimo:])
lista_resultante.extend(lista2[tamanho_minimo:])
print("Lista resultante:", lista_resultante)