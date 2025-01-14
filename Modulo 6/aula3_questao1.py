def receber_lista():
    lista = []
    while True:
        try:
            entrada = input("Digite um número inteiro (ou 'fim' para parar): ")
            if entrada.lower() == 'fim':
                
                if len(lista) >= 4:
                    break
                else:
                    print("Por favor, insira pelo menos 4 números.")
            else:
                lista.append(int(entrada))
        except ValueError:
            print("Por favor, insira apenas números inteiros ou 'fim' para parar.")
    return lista

lista = receber_lista()
print("Lista original:", lista)
print("Os 3 primeiros elementos:", lista[:3])
print("Os 2 últimos elementos:", lista[-2:])
print("Lista invertida:", lista[::-1])
print("Elementos de índice par:", lista[::2])
print("Elementos de índice ímpar:", lista[1::2])