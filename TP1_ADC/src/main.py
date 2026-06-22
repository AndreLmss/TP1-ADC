from src.utilizadores import login
from src.clientes import cadastrar_cliente, listar_clientes, editar_cliente, remover_cliente, listar_clientes_ordenados, total_clientes
from src.produtos import cadastrar_produto, listar_produtos, pesquisar_produto, editar_produto, remover_produto, produtos_stock_baixo, pesquisar_por_preco
from src.vendas import registar_venda, listar_vendas
from src.relatorios import relatorio_vendas_totais, relatorio_produtos_mais_vendidos

def menu_admin():
    """
    Exibe o menu principal para o utilizador com papel de administrador.
    Permite navegar para a gestão de clientes, produtos, vendas e relatórios.
    """
    while True:
        print("\n=== MENU ADMIN ===")
        print("1. Clientes")
        print("2. Produtos")
        print("3. Vendas")
        print("4. Relatórios")
        print("0. Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            menu_clientes()
        elif opcao == "2":
            menu_produtos()
        elif opcao == "3":
            menu_vendas()
        elif opcao == "4":
            menu_relatorios()
        elif opcao == "0":
            break

def menu_clientes():
    """
    Exibe o menu de gestão de clientes.
    """
    while True:
        print("\n=== CLIENTES ===")
        print("1. Cadastrar cliente")
        print("2. Listar clientes")
        print("3. Listar clientes (Ordenados)")
        print("4. Total de clientes")
        print("5. Editar cliente")
        print("6. Remover cliente")
        print("0. Voltar")
        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            listar_clientes()
        elif opcao == "3":
            listar_clientes_ordenados()
        elif opcao == "4":
            total_clientes()
        elif opcao == "5":
            editar_cliente()
        elif opcao == "6":
            remover_cliente()
        elif opcao == "0":
            break

def menu_produtos():
    """
    Exibe o menu de gestão de produtos.
    """
    while True:
        print("\n=== PRODUTOS ===")
        print("1. Cadastrar produto")
        print("2. Listar produtos")
        print("3. Pesquisar produto")
        print("4. Pesquisar por preço")
        print("5. Produtos com stock baixo")
        print("6. Editar produto")
        print("7. Remover produto")
        print("0. Voltar")
        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            pesquisar_produto()
        elif opcao == "4":
            pesquisar_por_preco()
        elif opcao == "5":
            produtos_stock_baixo()
        elif opcao == "6":
            editar_produto()
        elif opcao == "7":
            remover_produto()
        elif opcao == "0":
            break

def menu_vendas():
    """
    Exibe o menu de gestão de vendas.
    """
    while True:
        print("\n=== VENDAS ===")
        print("1. Registar venda")
        print("2. Listar vendas")
        print("0. Voltar")
        opcao = input("Escolha: ")

        if opcao == "1":
            registar_venda()
        elif opcao == "2":
            listar_vendas()
        elif opcao == "0":
            break

def menu_relatorios():
    """
    Exibe o menu de relatórios do sistema.
    """
    while True:
        print("\n=== RELATÓRIOS ===")
        print("1. Vendas Totais")
        print("2. Produtos Mais Vendidos")
        print("0. Voltar")
        opcao = input("Escolha: ")

        if opcao == "1":
            relatorio_vendas_totais()
        elif opcao == "2":
            relatorio_produtos_mais_vendidos()
        elif opcao == "0":
            break

if __name__ == "__main__":
    utilizador = login()
    if utilizador:
        if utilizador["papel"] == "admin":
            menu_admin()