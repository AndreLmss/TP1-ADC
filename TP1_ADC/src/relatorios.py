from src.vendas import carregar_vendas
from src.produtos import carregar_produtos
from src.clientes import carregar_clientes

def relatorio_vendas_totais():
    """
    Calcula e apresenta o total faturado com todas as vendas registadas.
    """
    vendas = carregar_vendas()
    print("\n=== RELATÓRIO: VENDAS TOTAIS ===")
    if not vendas:
        print("Nenhuma venda registada ainda.")
        return
        
    total_faturado = sum(v["total"] for v in vendas)
    quantidade_produtos = sum(v["quantidade"] for v in vendas)
    
    print(f"Total de vendas realizadas: {len(vendas)}")
    print(f"Quantidade de produtos vendidos: {quantidade_produtos}")
    print(f"Faturação Total: {total_faturado:.2f}€")

def relatorio_produtos_mais_vendidos():
    """
    Apresenta um relatório dos produtos mais vendidos ordenados por quantidade.
    """
    vendas = carregar_vendas()
    print("\n=== RELATÓRIO: PRODUTOS MAIS VENDIDOS ===")
    if not vendas:
        print("Nenhuma venda registada ainda.")
        return
        
    produtos_vendidos = {}
    for v in vendas:
        id_produto = v["id_produto"]
        if id_produto not in produtos_vendidos:
            produtos_vendidos[id_produto] = {"nome": v["nome_produto"], "quantidade": 0}
        produtos_vendidos[id_produto]["quantidade"] += v["quantidade"]
        
    lista_produtos = list(produtos_vendidos.values())
    lista_produtos.sort(key=lambda x: x["quantidade"], reverse=True)
    
    for idx, p in enumerate(lista_produtos, 1):
        print(f"{idx}º lugar - {p['nome']} (Vendidos: {p['quantidade']})")
