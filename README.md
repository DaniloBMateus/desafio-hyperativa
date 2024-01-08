# Documentação da API

## Visão Geral

Esta API foi desenvolvida utilizando Flask, Flask-SQLAlchemy, Flask-Marshmallow e Flask-JWT-Extended. Oferece funcionalidades de autenticação, inserção de cartões, processamento de arquivos e consulta de cartões.

## Configuração
  * Certifique-se de ter o Python instalado em seu sistema.
  * Instale os pacotes necessários usando pip install -r requirements.txt.
  * Configure um ambiente virtual (recomendado).

## Autenticação <a name="autenticacao"></a>

### Endpoint: `/api/auth` (POST)

Autentica um usuário e obtém um token de acesso.

#### Requisição
```json
{
  "username": "exemplo",
  "password": "senha123"
}

