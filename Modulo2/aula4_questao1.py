comprimento = int(input("digite o comprimeto"))
largura = int(input("digite a largura" ))
preco = float(input("valor do terreno"))

area = comprimento * largura 
valor = area * preco

print (f"O terreno possui {area}m2 e custa R${valor:,.2f}")