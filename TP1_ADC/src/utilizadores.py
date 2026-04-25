import json
import os

FICHEIRO = "data/utilizadores.json"

def carregar_utilizadores():
    if not os.path.exists(FICHEIRO):
        return []
    with open(FICHEIRO, "r") as f:
        return json.load(f)

def guardar_utilizadores(utilizadores):
    with open(FICHEIRO, "w") as f:
        json.dump(utilizadores, f, indent=4)

def login():
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