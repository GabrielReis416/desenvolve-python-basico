n1 = int(input("Digite um numero: "))
n2 = int(input("Digite um numero: "))
n3 = int(input("Digite um numero: "))

m = (n1 + n2 + n3)/3

if m >= 60 :
    print(" Aprovado ")
    print("Fim")
elif m >= 40:
    print( " Recuperação ")
    print("Fim")
else: 
    print(" Reprovado")
    print("Fim")