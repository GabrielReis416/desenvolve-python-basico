import csv
import os

def carregar_usuarios():
    if not os.path.exists('usuarios.csv'):
        criar_usuario_inicial()
    with open('usuarios.csv', mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        usuarios = [linha for linha in reader]
    return usuarios

def salvar_usuarios(usuarios):
    with open('usuarios.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(usuarios)

def carregar_produtos():
    if not os.path.exists('produtos.csv'):
        return []
    with open('produtos.csv', mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        produtos = [linha for linha in reader]
    return produtos

def salvar_produtos(produtos):
    with open('produtos.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(produtos)

def criar_usuario_inicial():
    usuarios_iniciais = [['admin', 'admin123', 'gerente']]
    salvar_usuarios(usuarios_iniciais)
    print("Usuário inicial padrão 'admin' criado com sucesso.")

def autenticar_usuario():
    usuarios = carregar_usuarios()
    nome = input("Nome de usuário: ")
    senha = input("Senha: ")
    for usuario in usuarios:
        if usuario[0] == nome and usuario[1] == senha:
            return usuario
    print("Usuário ou senha incorretos!")
    return None

def exibir_menu(usuario):
    if usuario[2] == "gerente":
        print("\nMenu Gerente:")
        print("1. Criar usuário")
        print("2. Listar usuários")
        print("3. Atualizar usuário")
        print("4. Excluir usuário")
        print("5. Criar produto")
        print("6. Listar produtos")
        print("7. Sair")
    elif usuario[2] == "funcionario":
        print("\nMenu Funcionário:")
        print("1. Listar usuários")
        print("2. Atualizar usuário")
        print("3. Listar produtos")
        print("4. Sair")
    elif usuario[2] == "estagiario":
        print("\nMenu Estagiário:")
        print("1. Listar usuários")
        print("2. Listar produtos")
        print("3. Sair")

def criar_usuario():
    nome = input("Nome do novo usuário: ")
    senha = input("Senha do novo usuário: ")
    tipo = input("Tipo de usuário (gerente, funcionario, estagiario): ")
    usuarios = carregar_usuarios()
    usuarios.append([nome, senha, tipo])
    salvar_usuarios(usuarios)
    print("Usuário criado com sucesso!")

def listar_usuarios():
    usuarios = carregar_usuarios()
    print("\nUsuários cadastrados:")
    for usuario in usuarios:
        print(f"Nome: {usuario[0]}, Tipo: {usuario[2]}")

def atualizar_usuario():
    nome = input("Digite o nome do usuário que deseja atualizar: ")
    usuarios = carregar_usuarios()
    for usuario in usuarios:
        if usuario[0] == nome:
            senha = input("Nova senha: ")
            tipo = input("Novo tipo de usuário (gerente, funcionario, estagiario): ")
            usuario[1] = senha
            usuario[2] = tipo
            salvar_usuarios(usuarios)
            print("Usuário atualizado com sucesso!")
            return
    print("Usuário não encontrado!")

def excluir_usuario():
    nome = input("Digite o nome do usuário que deseja excluir: ")
    usuarios = carregar_usuarios()
    for usuario in usuarios:
        if usuario[0] == nome:
            usuarios.remove(usuario)
            salvar_usuarios(usuarios)
            print("Usuário excluído com sucesso!")
            return
    print("Usuário não encontrado!")

def criar_produto():
    nome_produto = input("Nome do produto: ")
    try:
        preco_produto = float(input("Preço do produto: "))
        quantidade_produto = int(input("Quantidade do produto: "))
    except ValueError:
        print("Preço ou quantidade inválidos. Por favor, insira valores numéricos válidos.")
        return
    produtos = carregar_produtos()
    produtos.append([nome_produto, preco_produto, quantidade_produto])
    salvar_produtos(produtos)
    print("Produto criado com sucesso!")

def listar_produtos():
    produtos = carregar_produtos()
    print("\nProdutos cadastrados:")
    for produto in produtos:
        print(f"Nome: {produto[0]}, Preço: {produto[1]}, Quantidade: {produto[2]}")

def main():
    while True:
        usuario_logado = autenticar_usuario()
        if usuario_logado:
            while True:
                exibir_menu(usuario_logado)
                opcao = input("Escolha uma opção: ")

                if usuario_logado[2] == "gerente":
                    if opcao == "1":
                        criar_usuario()
                    elif opcao == "2":
                        listar_usuarios()
                    elif opcao == "3":
                        atualizar_usuario()
                    elif opcao == "4":
                        excluir_usuario()
                    elif opcao == "5":
                        criar_produto()
                    elif opcao == "6":
                        listar_produtos()
                    elif opcao == "7":
                        print("Saindo...")
                        return
                    else:
                        print("Opção inválida!")

                elif usuario_logado[2] == "funcionario":
                    if opcao == "1":
                        listar_usuarios()
                    elif opcao == "2":
                        atualizar_usuario()
                    elif opcao == "3":
                        listar_produtos()
                    elif opcao == "4":
                        print("Saindo...")
                        return
                    else:
                        print("Opção inválida!")

                elif usuario_logado[2] == "estagiario":
                    if opcao == "1":
                        listar_usuarios()
                    elif opcao == "2":
                        listar_produtos()
                    elif opcao == "3":
                        print("Saindo...")
                        return
                    else:
                        print("Opção inválida!")

if __name__ == "__main__":
    main()