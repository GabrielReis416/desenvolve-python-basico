emoji_dict = {
    "😀": "feliz",
    "😢": "triste",
    "😍": "apaixonado",
    "😎": "legal",
    "😂": "rindo",
    "🤔": "pensando",
    "👍": "positivo",
    "👎": "negativo",
    "❤️": "amor",
    "🔥": "fogo",
    "💡": "ideia",
}


def exibir_emojis():
    print("Lista de emojis disponíveis e seus textos correspondentes:")
    for emoji, texto in emoji_dict.items():
        print(f"{emoji} -> {texto}")

def emojizar_frase(frase):
    palavras = frase.split()
    frase_emojis = []
    for palavra in palavras:
        emoji = next((emoji for emoji, texto in emoji_dict.items() if texto == palavra), None)
        if emoji:
            frase_emojis.append(emoji)
        else:
            frase_emojis.append(palavra)  
    return " ".join(frase_emojis)

def decodificar_frase(frase_emojis):
    emojis = frase_emojis.split()
    frase_texto = []
    for emoji in emojis:
        texto = emoji_dict.get(emoji, emoji)  
        frase_texto.append(texto)
    return " ".join(frase_texto)


exibir_emojis()

frase = input("\nDigite uma frase para ser convertida em emojis: ")
frase_emojizada = emojizar_frase(frase)
print("\nFrase em emojis: ", frase_emojizada)

frase_com_emojis = input("\nAgora, digite uma frase codificada em emojis: ")
frase_decodificada = decodificar_frase(frase_com_emojis)
print("\nFrase decodificada: ", frase_decodificada)