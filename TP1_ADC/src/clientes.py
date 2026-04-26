import json
import os

FICHEIRO = "data/clientes.json"

def carregar_clientes():
    if not os.path.exists(FICHEIRO):
        return []
    with open(FICHEIRO, "r") as f:
        return json.load(f)

def guardar_clientes(clientes):
    with open(FICHEIRO, "w") as f:
        json.dump(clientes, f, indent=4)

def cadastrar_cliente():
    clientes = carregar_clientes()
    print("\n=== CADASTRAR CLIENTE ===")
    nome = input("Nome: ")
    email = input("Email: ")
    telefone = input("Telefone: ")
    
    clientes.append({
        "id": len(clientes) + 1,
        "nome": nome,
        "email": email,
        "telefone": telefone
    })
    guardar_clientes(clientes)
    print("Cliente cadastrado com sucesso!")

def listar_clientes():
    clientes = carregar_clientes()
    print("\n=== LISTA DE CLIENTES ===")
    if not clientes:
        print("Nenhum cliente encontrado!")
        return
    for c in clientes:
        print(f"[{c['id']}] {c['nome']} | {c['email']} | {c['telefone']}")

def editar_cliente():
    clientes = carregar_clientes()
    listar_clientes()
    try:
        id = int(input("\nID do cliente a editar: "))
        for c in clientes:
            if c["id"] == id:
                c["nome"] = input(f"Nome ({c['nome']}): ") or c["nome"]
                c["email"] = input(f"Email ({c['email']}): ") or c["email"]
                c["telefone"] = input(f"Telefone ({c['telefone']}): ") or c["telefone"]
                guardar_clientes(clientes)
                print("Cliente atualizado com sucesso!")
                return
        print("Cliente não encontrado!")
    except:
        print("ID inválido!")

def remover_cliente():
    clientes = carregar_clientes()
    listar_clientes()
    try:
        id = int(input("\nID do cliente a remover: "))
        clientes = [c for c in clientes if c["id"] != id]
        guardar_clientes(clientes)
        print("Cliente removido com sucesso!")
    except:
        print("ID inválido!")

def listar_clientes_ordenados():
    clientes = carregar_clientes()

    print("\n=== CLIENTES ORDENADOS ===")

    if not clientes:
        print("Nenhum cliente encontrado!")
        return

    clientes.sort(key=lambda c: c["nome"].lower())

    for c in clientes:
        print(
            f"[{c['id']}] {c['nome']} | {c['email']} | {c['telefone']}"
        )

def total_clientes():
    clientes = carregar_clientes()

    print("\n=== TOTAL DE CLIENTES ===")
    print(f"Total de clientes cadastrados: {len(clientes)}")