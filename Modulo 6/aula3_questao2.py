def receber_urls():

    urls = []
    while True:
        url = input("Digite uma URL que começa com 'www.' e termina com '.com' (ou 'fim' para parar): ")
        if url.lower() == 'fim':
            break
        elif url.startswith("www.") and url.endswith(".com"):
            urls.append(url)
        else:
            print("A URL deve começar com 'www.' e terminar com '.com'. Tente novamente.")
    return urls
urls = receber_urls()

dominios = [url[4:-4] for url in urls]
print("Lista de domínios:", dominios)