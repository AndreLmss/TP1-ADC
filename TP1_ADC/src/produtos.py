import json
import os

FICHEIRO = "data/produtos.json"

def carregar_produtos():
    if not os.path.exists(FICHEIRO):
        return []
    with open(FICHEIRO, "r") as f:
        return json.load(f)

def guardar_produtos(produtos):
    with open(FICHEIRO, "w") as f:
        json.dump(produtos, f, indent=4)

def cadastrar_produto():
    produtos = carregar_produtos()
    print("\n=== CADASTRAR PRODUTO ===")
    nome = input("Nome: ")
    categoria = input("Categoria (rato/teclado/headset/monitor): ")
    preco = float(input("Preço: "))
    stock = int(input("Stock: "))
    
    produtos.append({
        "id": len(produtos) + 1,
        "nome": nome,
        "categoria": categoria,
        "preco": preco,
        "stock": stock
    })
    guardar_produtos(produtos)
    print("Produto cadastrado com sucesso!")

def listar_produtos():
    produtos = carregar_produtos()
    print("\n=== LISTA DE PRODUTOS ===")
    if not produtos:
        print("Nenhum produto encontrado!")
        return
    for p in produtos:
        print(f"[{p['id']}] {p['nome']} | {p['categoria']} | {p['preco']}€ | Stock: {p['stock']}")

def pesquisar_produto():
    produtos = carregar_produtos()
    print("\n=== PESQUISAR PRODUTO ===")
    termo = input("Nome ou categoria: ").lower()
    resultados = [p for p in produtos if termo in p["nome"].lower() or termo in p["categoria"].lower()]
    if not resultados:
        print("Nenhum produto encontrado!")
        return
    for p in resultados:
        print(f"[{p['id']}] {p['nome']} | {p['categoria']} | {p['preco']}€ | Stock: {p['stock']}")

def editar_produto():
    produtos = carregar_produtos()
    listar_produtos()
    try:
        id = int(input("\nID do produto a editar: "))
        for p in produtos:
            if p["id"] == id:
                p["nome"] = input(f"Nome ({p['nome']}): ") or p["nome"]
                p["categoria"] = input(f"Categoria ({p['categoria']}): ") or p["categoria"]
                preco = input(f"Preço ({p['preco']}): ")
                p["preco"] = float(preco) if preco else p["preco"]
                stock = input(f"Stock ({p['stock']}): ")
                p["stock"] = int(stock) if stock else p["stock"]
                guardar_produtos(produtos)
                print("Produto atualizado com sucesso!")
                return
        print("Produto não encontrado!")
    except:
        print("ID inválido!")

def remover_produto():
    produtos = carregar_produtos()
    listar_produtos()
    try:
        id = int(input("\nID do produto a remover: "))
        produtos = [p for p in produtos if p["id"] != id]
        guardar_produtos(produtos)
        print("Produto removido com sucesso!")
    except:
        print("ID inválido!")

def produtos_stock_baixo():
    produtos = carregar_produtos()

    print("\n=== PRODUTOS COM STOCK BAIXO ===")

    encontrados = False

    for p in produtos:
        if p["stock"] <= 5:
            print(
                f"[{p['id']}] {p['nome']} | Stock: {p['stock']}"
            )
            encontrados = True

    if not encontrados:
        print("Nenhum produto com stock baixo.")