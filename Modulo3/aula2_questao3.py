idade = int (input("Digite sua idade: "))

partidas = input ("Já jogou pelo menos 3 partidas ? (True ou False)")

partidas = partidas == 'True'

venceu = int(input("Quantas vezes você venceu um jogo ? "))

if 16 <= idade <= 18 and partidas and venceu >= 1:
    print (True)
else:
    print (False)