# API REST para Gerenciamento de Lojas, Usuários e Itens

Este projeto é uma API RESTful desenvolvida com Python e Flask, destinada ao gerenciamento de dados de lojas, usuários e itens. Ele oferece funcionalidades como registro de usuários, autenticação segura com JWT, controle de acesso e operações CRUD completas para lojas e itens.
## Tecnologias

- **[Python](https://www.python.org/)**: Linguagem de programação. 
- **[Flask](https://flask.palletsprojects.com/)**: Microframework web em Python.
- **[Docker](https://www.docker.com/)**: Containerização da aplicação.
- **[JWT](https://jwt.io/)**: Padrão para compartilhamento de informações em segurança.
- **[PostgreSQL](https://www.docker.com/)**: Gerenciamento de banco de dados relacional.
- **[Render Web Service](https://render.com/docs/web-services)**: Hospedagem da aplicação web.

## Bibliotecas

- **[Flask-Smorest](https://render.com/docs/web-services)**: Extensão do Flask para criação de APIs REST.
- **[Python-dotenv](https://saurabh-kumar.com/python-dotenv/)**: Gerenciamento de variáveis de ambiente.
- **[SQLAlchemy](https://www.sqlalchemy.org/)**: Acesso e gerenciamento de banco de dados SQL.
- **[Flask-SQLAlchemy](https://flask-sqlalchemy.readthedocs.io/en/stable/)**: Integração do SQLAlchemy com o Flask.
- **[Flask-JWT-Extended](https://flask-sqlalchemy.readthedocs.io/en/stable/)**: Extensão para autenticação com JSON Web Tokens (JWT).
- **[Passlib](https://passlib.readthedocs.io/en/stable/)**: Hashing de senhas e autenticação segura.
- **[Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/)**: Gerenciamento de migrações de banco de dados.
- **[Gunicorn](https://docs.gunicorn.org/en/stable/)**: Servidor WSGI para aplicações em Python.
- **[Psycopg2](https://www.psycopg.org/docs/)**: Adaptador para conexão com bancos de dados PostgreSQL.
- **[Requests](https://requests.readthedocs.io/en/latest/)**: Requisições HTTP.

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

Disponível localmente em: http://localhost:5000.

Disponível remotamente em: URL_DO_SEU_WEB_SERVICE.

## Interagindo com a API

### Requisições para controle de usuário
#### 1. Registrar usuário

- **Endpoint**: `/register`
- **Descrição**: Permite a criação de um novo usuário no sistema.
- **Método**: `POST`
- **Exemplo de requisição**: 
```json
{ 
    "username": "nome do usuário",
    "email": "usuario@email.com",
    "password": "senha"
} 
``` 

#### 2. Login

- **Endpoint**: `/login`
- **Descrição**: Realiza a autenticação do usuário, retornando um token de acesso (JWT) para autenticação em outras requisições.
- **Método**: `POST`
- **Exemplo de requisição**: 
```json
{ 
    "username": "nome do usuário",
    "password": "senha"
} 
``` 

#### 3. Logout

- **Endpoint**: `/logout`
- **Descrição**: Finaliza a sessão atual.
- **Método**: `POST`
- **Exemplo de requisição**: 
```json
{ 
    "username": "nome do usuário",
    "password": "senha"
} 
``` 
#### 4. Refresh

- **Endpoint**: `/refresh`
- **Descrição**: Gera novo token de acesso sem a necessidade de novo login.
- **Método**: `POST`

#### 5. Ler informações de usuário

- **Endpoint**: `/user/<id>`
- **Descrição**: Retorna as informações visíveis do usuário selecionado.
- **Método**: `GET`

#### 6. Deletar usuário

- **Endpoint**: `/user/<id>`
- **Descrição**: Deleta o usuário selecionado.
- **Método**: `DELETE`

### Requisições para controle de lojas

#### 1. Registrar loja

- **Endpoint**: `/store`
- **Descrição**: Permite a criação de uma nova loja no sistema.
- **Método**: `POST`
- **Exemplo de requisição**: 
```json
{ 
    "name": "nome da loja"
} 
``` 
#### 2. Ver todas as lojas

- **Endpoint**: `/store`
- **Descrição**: Retorna as informações visíveis de todas as lojas.
- **Método**: `GET`

#### 3. Ver loja

- **Endpoint**: `/store/<id>`
- **Descrição**: Retorna as informações visíveis da loja selecionada.
- **Método**: `GET`

#### 4. Deletar loja

- **Endpoint**: `/store/<id>`
- **Authorization**: `Bearer {{access_token}}`
- **Descrição**: Deleta a loja selecionada.
- **Método**: `DELETE`

### Requisições para controle de itens

#### 1. Registrar item

- **Endpoint**: `/item`
- **Authorization**: `Bearer {{access_token}}`
- **Descrição**: Permite a criação de um novo item associado a uma loja no sistema.
- **Método**: `POST`
- **Exemplo de requisição**:
```json
{
  "name": "nome do item",
  "price": 5.55, 
  "store_id": 1
}
```

#### 2. Ver todos os itens

- **Endpoint**: `/item`
- **Authorization**: `Bearer {{access_token}}`
- **Descrição**: Retorna as informações visíveis de todos os itens.
- **Método**: `GET`

#### 3. Ver item

- **Endpoint**: `/item/<id>`
- **Authorization**: `Bearer {{access_token}}`
- **Descrição**: Retorna as informações visíveis do item selecionado.
- **Método**: `GET`

#### 4. Deletar item

- **Endpoint**: `/item/<id>`
- **Authorization**: `Bearer {{access_token}}`
- **Descrição**: Deleta o item selecionado.
- **Método**: `DELETE`

#### 5. Alterar item

- **Endpoint**: `/item/<id>`
- **Authorization**: `Bearer {{access_token}}`
- **Descrição**: Altera as informações do item selecionado.
- **Método**: `PUT`
- **Exemplo de requisição**:
```json
{
  "name": "novo nome do item",
  "price": 7, 
  "store_id": 1
}
```
### Requisições para controle de tags

#### 1. Registrar tag

- **Endpoint**: `/store/<id>/tag`
- **Descrição**: Cria uma tag para uma loja.
- **Método**: `POST`
- **Exemplo de requisição**:
```json
{
  "name": "nome da tag"
}
```

#### 2. Associar item a uma tag

- **Endpoint**: `/item/<id>/tag/<id>`
- **Descrição**: Associa item a uma tag existente na loja.
- **Método**: `POST`

#### 3. Ver tag

- **Endpoint**: `/tag/<id>`
- **Descrição**: Retorna as informações visíveis de uma tag, assim como todos os itens associados à mesma.
- **Método**: `GET`

#### 4. Ver tags de uma loja

- **Endpoint**: `/store/<id>/tag`
- **Descrição**: Retorna todas as tags registradas para a loja selecionada.
- **Método**: `GET`

#### 5. Retira tag do item

- **Endpoint**: `/item/<id>/tag/<id>`
- **Descrição**: Deleta associação do item com uma tag.
- **Método**: `DELETE`

#### 6. Deleta tag

- **Endpoint**: `/tag/<id>`
- **Descrição**: Deleta a tag selecionada, desde que não haja nenhuma relação entre ela e algum item.
- **Método**: `DELETE`

## Contribuindo

Sinta-se à vontade para abrir issues ou enviar pull requests.