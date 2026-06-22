import json
import os
from src.clientes import carregar_clientes
from src.produtos import carregar_produtos, guardar_produtos

FICHEIRO = "data/vendas.json"

def carregar_vendas():
    """
    Carrega as vendas a partir do ficheiro JSON.
    Retorna uma lista vazia se o ficheiro não existir.
    """
    if not os.path.exists(FICHEIRO):
        return []
    with open(FICHEIRO, "r") as f:
        return json.load(f)

def guardar_vendas(vendas):
    """
    Guarda a lista de vendas no ficheiro JSON.
    """
    with open(FICHEIRO, "w") as f:
        json.dump(vendas, f, indent=4)

def registar_venda():
    """
    Permite registar uma nova venda no sistema.
    O utilizador escolhe o cliente, o produto e a quantidade.
    O stock do produto é atualizado automaticamente.
    """
    vendas = carregar_vendas()
    clientes = carregar_clientes()
    produtos = carregar_produtos()
    
    print("\n=== REGISTAR VENDA ===")
    if not clientes:
        print("Erro: Não há clientes registados.")
        return
    if not produtos:
        print("Erro: Não há produtos registados.")
        return
        
    try:
        # Selecionar Cliente
        id_cliente = int(input("ID do Cliente: "))
        cliente_encontrado = next((c for c in clientes if c["id"] == id_cliente), None)
        if not cliente_encontrado:
            print("Cliente não encontrado!")
            return
            
        # Selecionar Produto
        id_produto = int(input("ID do Produto: "))
        produto_encontrado = next((p for p in produtos if p["id"] == id_produto), None)
        if not produto_encontrado:
            print("Produto não encontrado!")
            return
            
        quantidade = int(input(f"Quantidade (Stock: {produto_encontrado['stock']}): "))
        if quantidade <= 0 or quantidade > produto_encontrado['stock']:
            print("Quantidade inválida ou stock insuficiente!")
            return
            
        # Calcular total
        total = quantidade * produto_encontrado['preco']
        
        # Atualizar Stock
        produto_encontrado['stock'] -= quantidade
        guardar_produtos(produtos)
        
        # Registar Venda
        nova_venda = {
            "id": len(vendas) + 1,
            "id_cliente": id_cliente,
            "nome_cliente": cliente_encontrado["nome"],
            "id_produto": id_produto,
            "nome_produto": produto_encontrado["nome"],
            "quantidade": quantidade,
            "total": total
        }
        vendas.append(nova_venda)
        guardar_vendas(vendas)
        
        print(f"Venda registada com sucesso! Total a pagar: {total:.2f}€")
        
    except ValueError:
        print("Valor inválido inserido!")

def listar_vendas():
    """
    Lista todas as vendas registadas no sistema.
    """
    vendas = carregar_vendas()
    print("\n=== LISTA DE VENDAS ===")
    if not vendas:
        print("Nenhuma venda registada!")
        return
    for v in vendas:
        print(f"[{v['id']}] Cliente: {v['nome_cliente']} | Produto: {v['nome_produto']} | Qtd: {v['quantidade']} | Total: {v['total']:.2f}€")
