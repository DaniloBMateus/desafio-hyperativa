# Documentação da API

## Visão Geral

Esta API foi desenvolvida utilizando Flask, Flask-SQLAlchemy, Flask-Marshmallow e Flask-JWT-Extended. Oferece funcionalidades de autenticação, inserção de cartões, processamento de arquivos e consulta de cartões.

## Configuração
  * Certifique-se de ter o Python instalado em seu sistema.
  * Instale os pacotes necessários usando pip install -r requirements.txt.
  * Configure um ambiente virtual (recomendado).
  * Certifique-se de ter uma SECRET_KEY segura para autenticação JWT.
  * O banco de dados SQLite é utilizado.

## Autenticação
### Endpoint: /api/auth
  * Método: POST
  * Descrição: Autentica usuários.
  * Corpo da Requisição:

```json
{
  "username": "exemplo",
  "password": "senha123"
}

