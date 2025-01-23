~~# Projeto de API para Armazenamento de Dados de Lojas

Projeto de API REST, desenvolvido com Python e Flask, que armazena dados de usuários e lojas, incluindo seus itens e respectivas etiquetas. O projeto também oferece recursos de registro, login, controle de acesso e gerenciamento dos elementos.

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

1. Clone o repositório:
```
git clone https://github.com/GiovanniMiro/rest-apis-project.git
```

2. Acesse a pasta do projeto:

```
cd rest-apis-project
```

3. Crie e ative o ambiente virtual:

```commandline
python -m venv .venv
.venv\Scripts\activate
```

4. Crie um banco de dados PostgreSQL e salve seu URL.
5. Crie um Web Service no [Render](https://render.com/).
6. No Web Service, vá para Environment.
7. No campo de Environment Variables, crie a Key ```DATABASE_URL``` e preencha o seu Value com a URL do seu banco de dados.
8. Construa as imagens e inicie os contêineres:
```
docker-compose up --build -d
```
9. Para iniciar o servidor localmente:
``` 
flask run 
```

## Canais de acesso

Disponível localmente em: http://127.0.0.1:5000

Disponível remotamente em: URL do Web Service do Render.

## Interagindo com a API

### Registrar usuário

- **Endpoint**: `/`
- **Descrição**: Cria um novo usuário e retorna um token de acesso.
- **Método**: `POST`
- **Exemplo de requisição**: 
```commandline
{ 


}
```



