# Documentação da API

## Visão Geral

Esta API foi desenvolvida utilizando Flask, Flask-SQLAlchemy, Flask-Marshmallow e Flask-JWT-Extended. Oferece funcionalidades de autenticação, inserção de cartões, processamento de arquivos e consulta de cartões.

## Configuração
  * Certifique-se de ter o Python instalado em seu sistema.
  * Instale os pacotes necessários usando pip install -r requirements.txt.
  * Configure um ambiente virtual (recomendado).
  * Certifique-se de ter uma SECRET_KEY segura para autenticação JWT.
  * O banco de dados SQLite é utilizado.

## Funcionalidades

### 1. Autenticação de Usuário

- **Endpoint:** `/api/auth` (método POST)
- Autenticação do usuário com base no nome de usuário e senha.
- Gera um token de acesso JWT para usuários autenticados.

### 2. Inserção de Cartão

- **Endpoint:** `/api/insert` (método POST)
- Requer autenticação com token JWT.
- Permite a inserção de novos cartões no sistema, evitando duplicatas.

### 3. Processamento de Arquivo de Texto

- **Endpoint:** `/api/processar-arquivo` (método POST)
- Requer autenticação com token JWT.
- Permite o envio de um arquivo de texto para processamento.
- O arquivo deve conter informações sobre cartões a serem inseridos no sistema.
- Extrai dados como nome do cliente, data de inserção, lote e quantidade de cartões.
- Inserção dos cartões no banco de dados.

### 4. Consulta de Cartão

- **Endpoint:** `/api/query/<card_number>` (método GET)
- Requer autenticação com token JWT.
- Permite a consulta de um cartão específico no sistema com base no número do cartão.

### 5. Banco de Dados

- Utiliza SQLAlchemy para interagir com o banco de dados SQLite.
- Possui duas tabelas no banco de dados: `User` e `Card`.
- A tabela `User` armazena informações de autenticação.
- A tabela `Card` armazena informações sobre os cartões.

### 6. Segurança

- Utiliza a extensão Flask-JWT-Extended para gerenciamento de tokens JWT.
- As senhas dos usuários são armazenadas de forma segura, utilizando o algoritmo de hash bcrypt.

