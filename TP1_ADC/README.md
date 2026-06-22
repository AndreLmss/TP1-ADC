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

## Como Executar a Aplicação (Python)

1. Certifique-se de que tem o Python instalado no seu sistema.
2. Na raiz do projeto, instale as dependências (caso existam) com `pip install -r requirements.txt` (por predefinição, a aplicação usa bibliotecas nativas como `json` e `os`).
3. Execute a aplicação usando o terminal:
   ```bash
   python src/main.py
   ```
4. As credenciais por defeito (Administrador) são:
   - **Username:** `admin`
   - **Password:** `admin`

## Como Executar o Site (Docusaurus)

O projeto inclui um site desenvolvido em Docusaurus para publicitar a aplicação e/ou empresa. Para testar o site localmente:

1. Certifique-se de que tem o [Node.js](https://nodejs.org/) instalado.
2. No terminal, navegue até à pasta do website:
   ```bash
   cd website
   ```
3. Instale as dependências (apenas na primeira vez):
   ```bash
   npm install
   ```
4. Inicie o servidor de desenvolvimento:
   ```bash
   npm start
   ```
O seu navegador deverá abrir automaticamente o site no endereço `http://localhost:3000`.

## Documentação do Código (Docstrings)
Todas as funções do código fonte estão devidamente comentadas (docstrings) para facilitar a leitura e manutenção futuras.
