# Projeto TP1_ADC: Aplicação de Gestão

Esta aplicação em Python foi desenvolvida no âmbito da disciplina TP1_ADC para permitir a gestão de clientes, produtos, vendas e relatórios de faturação. O sistema utiliza ficheiros JSON para a persistência dos dados e oferece um interface de texto na consola.

## Funcionalidades

- **Autenticação**: Login como administrador.
- **Gestão de Clientes**: Cadastrar, listar, ordenar, editar e remover.
- **Gestão de Produtos**: Cadastrar, listar, pesquisar, editar, remover e alertas de stock.
- **Gestão de Vendas**: Registar novas vendas (com cálculo de total e atualização automática de stock) e listar o histórico.
- **Relatórios**: Visualizar vendas totais e produtos mais vendidos.

## Estrutura do Projeto

- `src/`: Contém os ficheiros de código fonte Python (`main.py`, `clientes.py`, `produtos.py`, `vendas.py`, `relatorios.py`, `utilizadores.py`).
- `data/`: Contém os ficheiros JSON com os dados persistentes (`clientes.json`, `produtos.json`, `vendas.json`, `utilizadores.json`).
- `website/`: Contém a documentação construída com o Docusaurus.

## Como Executar

1. Certifique-se de que tem o Python instalado no seu sistema.
2. Na raiz do projeto, instale as dependências (caso existam) com `pip install -r requirements.txt` (por predefinição, a aplicação usa bibliotecas nativas como `json` e `os`).
3. Execute a aplicação usando:
   ```bash
   python src/main.py
   ```
4. As credenciais por defeito estão em `data/utilizadores.json` (ex: `admin` / `admin`).

## Documentação do Código (Docstrings)
Todas as funções do código fonte estão devidamente comentadas (docstrings) para facilitar a leitura e manutenção futuras.
