import random

numero_aleatorio = random.randint(1, 10)

while True:
    
    palpite = int(input("Adivinhe o número entre 1 e 10: "))
    
    if palpite < numero_aleatorio:
        print("Seu palpite é muito baixo. Tente novamente!")
    elif palpite > numero_aleatorio:
        print("Seu palpite é muito alto. Tente novamente!")
    else:
        print("Parabéns! Você acertou o número!")
        break 