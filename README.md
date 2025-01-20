# Projeto de Armazenamento de Dados de Lojas

Projeto de API REST, desenvolvido com Python e Flask, que armazena dados de usuários e lojas, incluindo seus itens e respectivas etiquetas. O projeto também oferece recursos de registro, login, controle de acesso e CRUD dos elementos.

## Tecnologias

- **Python**: Linguagem de programação. 
- **Flask**: Microframework web em Python.
- **Docker**: Conteinerização da aplicação.
- **JWT**: Padrão para compartilhamento de informações em segurança.
- **PostgreSQL**: Gerenciamento de banco de dados relacional.
- **Render Web Service**: Hospedagem da aplicação web.

## Bibliotecas

- **Flask-Smorest**: Extensão do Flask para criação de APIs REST.
- **Python-dotenv**: Gerenciamento de variáveis de ambiente.
- **SQLAlchemy**: Acesso e gerenciamento de banco de dados SQL.
- **Flask-SQLAlchemy**: Integração do SQLAlchemy com o Flask.
- **Flask-JWT-Extended**: Extensão para autenticação com JSON Web Tokens (JWT).
- **Passlib**: Hashing de senhas e autenticação segura.
- **Flask-Migrate**: Gerenciamento de migrações de banco de dados.
- **Gunicorn**: Servidor WSGI para aplicações em Python.
- **Psycopg2**: Adaptador para conexão com bancos de dados PostgreSQL.
- **Requests**: Requisições HTTP.

## Inicialização

Para iniciar o servidor remotamente:
```
docker-compose up --build -d
```

Para iniciar o servidor localmente:

``` 
flask run 
```

## Canais de acesso

Disponível localmente em: http://127.0.0.1:5000

Disponível remotamente em: URL do Serviço Web do Render