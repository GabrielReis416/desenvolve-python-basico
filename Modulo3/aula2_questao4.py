classe = input("Digite a classe do personagem (guerreiro, mago ou arqueiro): ").strip().lower()


forca = int(input("Digite os pontos de força: "))
magia = int(input("Digite os pontos de magia: "))


if classe == "guerreiro":

    if forca >= 15 and magia <= 10:
        print(True)
    else:
        print(False)

elif classe == "mago":

    if forca <= 10 and magia >= 15:
        print(True)
    else:
        print(False)

elif classe == "arqueiro":

    if 5 < forca <= 15 and 5 < magia <= 15:
        print(True)
    else:
        print(False)

else:
    
    print(False)