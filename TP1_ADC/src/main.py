from src.utilizadores import login
from src.clientes import cadastrar_cliente, listar_clientes, editar_cliente, remover_cliente
from src.produtos import cadastrar_produto, listar_produtos, pesquisar_produto, editar_produto, remover_produto

def menu_admin():
    while True:
        print("\n=== MENU ADMIN ===")
        print("1. Clientes")
        print("2. Produtos")
        print("0. Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            menu_clientes()
        elif opcao == "2":
            menu_produtos()
        elif opcao == "0":
            break

def menu_clientes():
    while True:
        print("\n=== CLIENTES ===")
        print("1. Cadastrar cliente")
        print("2. Listar clientes")
        print("3. Editar cliente")
        print("4. Remover cliente")
        print("0. Voltar")
        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            listar_clientes()
        elif opcao == "3":
            editar_cliente()
        elif opcao == "4":
            remover_cliente()
        elif opcao == "0":
            break

def menu_produtos():
    while True:
        print("\n=== PRODUTOS ===")
        print("1. Cadastrar produto")
        print("2. Listar produtos")
        print("3. Pesquisar produto")
        print("4. Editar produto")
        print("5. Remover produto")
        print("0. Voltar")
        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            pesquisar_produto()
        elif opcao == "4":
            editar_produto()
        elif opcao == "5":
            remover_produto()
        elif opcao == "0":
            break

if __name__ == "__main__":
    utilizador = login()
    if utilizador:
        if utilizador["papel"] == "admin":
            menu_admin()