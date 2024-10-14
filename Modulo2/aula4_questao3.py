produto1 = input ("Digite o nome do produto: ")
valor1 = float (input (" Digite Valor do Produto : "))
quantidade1 = int(input ("Digite a quantidade do produto "))


produto2 = input ("Digite o nome do produto: ")
valor2 = float(input (" Digite Valor do Produto : "))
quantidade2 = int(input ("Digite a quantidade do produto "))


produto3 = input ("Digite o nome do produto: ")
valor3 = float (input (" Digite Valor do Produto : "))
quantidade3 = int (input ("Digite a quantidade do produto "))

total1 =  valor1 * quantidade1
total2 =  valor2 * quantidade2
total3 =  valor3 * quantidade3

totalCompra = total1 + total2 + total3

print ("Total: R$", totalCompra)