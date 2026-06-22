import json
import os

FICHEIRO = "data/clientes.json"

def carregar_clientes():
    """
    Carrega os clientes a partir do ficheiro JSON correspondente.
    Retorna uma lista vazia se o ficheiro não existir.
    """
    if not os.path.exists(FICHEIRO):
        return []
    with open(FICHEIRO, "r") as f:
        return json.load(f)

def guardar_clientes(clientes):
    """
    Guarda a lista de clientes no ficheiro JSON de dados.
    """
    with open(FICHEIRO, "w") as f:
        json.dump(clientes, f, indent=4)

def cadastrar_cliente():
    """
    Regista um novo cliente no sistema.
    Pede ao utilizador os dados do cliente e guarda-os.
    """
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
    """
    Imprime no ecrã a lista de todos os clientes registados no sistema.
    """
    clientes = carregar_clientes()
    print("\n=== LISTA DE CLIENTES ===")
    if not clientes:
        print("Nenhum cliente encontrado!")
        return
    for c in clientes:
        print(f"[{c['id']}] {c['nome']} | {c['email']} | {c['telefone']}")

def editar_cliente():
    """
    Permite editar os dados de um cliente existente com base no seu ID.
    O utilizador pode deixar em branco para manter o valor atual.
    """
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
    """
    Remove um cliente do sistema com base no ID fornecido pelo utilizador.
    """
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
    """
    Apresenta a lista de clientes ordenada alfabeticamente pelo nome.
    """
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
    """
    Calcula e exibe o número total de clientes atualmente registados no sistema.
    """
    clientes = carregar_clientes()

    print("\n=== TOTAL DE CLIENTES ===")
    print(f"Total de clientes cadastrados: {len(clientes)}")