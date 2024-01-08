# Documentação da API

## Visão Geral

Esta API foi desenvolvida utilizando Flask, Flask-SQLAlchemy, Flask-Marshmallow e Flask-JWT-Extended. Oferece funcionalidades de autenticação, inserção de cartões, processamento de arquivos e consulta de cartões.

## Autenticação <a name="autenticacao"></a>

### Endpoint: `/api/auth` (POST)

Autentica um usuário e obtém um token de acesso.

#### Requisição
```json
{
  "username": "exemplo",
  "password": "senha123"
}

