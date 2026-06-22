import json
import os

FICHEIRO = "data/utilizadores.json"

def carregar_utilizadores():
    """
    Lê os dados dos utilizadores do ficheiro JSON de sistema.
    """
    if not os.path.exists(FICHEIRO):
        return []
    with open(FICHEIRO, "r") as f:
        return json.load(f)

def guardar_utilizadores(utilizadores):
    """
    Escreve a lista de utilizadores no ficheiro de dados JSON.
    """
    with open(FICHEIRO, "w") as f:
        json.dump(utilizadores, f, indent=4)

def login():
    """
    Solicita as credenciais ao utilizador e verifica se são válidas.
    Retorna o dicionário do utilizador autenticado ou None em caso de erro.
    """
    utilizadores = carregar_utilizadores()
    if not utilizadores:
        print("Nenhum utilizador encontrado!")
        return None
    
    print("\n=== LOGIN ===")
    username = input("Username: ")
    password = input("Password: ")
    
    for u in utilizadores:
        if u["username"] == username and u["password"] == password:
            print(f"\nBem-vindo, {u['nome']}! ({u['papel']})")
            return u
    
    print("Username ou password incorretos!")
    return None

def criar_utilizador(nome, username, password, papel):
    """
    Regista um novo utilizador no sistema com o seu papel (admin/outro).
    Utilizado internamente ou por um administrador (não tem interface no menu default).
    """
    utilizadores = carregar_utilizadores()
    utilizadores.append({
        "id": len(utilizadores) + 1,
        "nome": nome,
        "username": username,
        "password": password,
        "papel": papel
    })
    guardar_utilizadores(utilizadores)
    print(f"Utilizador {username} criado com sucesso!")