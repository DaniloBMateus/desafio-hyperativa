# Documentação da API

## Visão Geral

Esta API foi desenvolvida utilizando Flask, Flask-SQLAlchemy, Flask-Marshmallow e Flask-JWT-Extended. Oferece funcionalidades de autenticação, inserção de cartões, processamento de arquivos e consulta de cartões.

## Configuração do Ambiente

Certifique-se de ter o Python instalado em seu ambiente. Execute o seguinte comando para instalar as dependências:

```bash
pip install -r requirements.txt

## Autenticação <a name="autenticacao"></a>

### Endpoint: `/api/auth` (POST)

Autentica um usuário e obtém um token de acesso.

#### Requisição
```json
{
  "username": "exemplo",
  "password": "senha123"
}

