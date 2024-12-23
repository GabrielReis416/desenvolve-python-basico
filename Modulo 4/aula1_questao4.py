n = int(input("Digite um numero: "))

maior = 0 
while n > 0 :
    x = int (input("Digite um novo numero"))
    if x > maior:
        maior = x
    else:
        n = n - 1
else:
    print("maior")