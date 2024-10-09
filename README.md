# API FastAPI com Autenticação JWT

Este projeto é uma API FastAPI que implementa autenticação JWT com níveis de acesso para usuários e administradores. Ele
utiliza SQLAlchemy para o banco de dados, Alembic para migrações e Pydantic para validação de dados.

## Características

- Autenticação JWT
- Rotas protegidas com diferentes níveis de acesso (usuário e administrador)
- Banco de dados SQLite com SQLAlchemy
- Migrações de banco de dados com Alembic
- Validação de dados com Pydantic
- Formatação de código com Black (apenas para desenvolvimento)
- Cobertura de testes com Coverage (apenas para desenvolvimento)

## Requisitos

### Produção

- Python 3.11
- FastAPI
- SQLAlchemy
- Alembic
- Pydantic
- Python-jose
- Passlib
- Python-multipart
- Python-dotenv

### Desenvolvimento

- Pytest
- Httpx
- Black
- Coverage

## Instalação

1. Clone o repositório:
   ```bash
   git https://github.com/kalebeasilvadev/fastapi-minimal.git
   cd fastapi-minimal
   ```

2. Crie um ambiente virtual e ative-o:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use `venv\Scripts\activate`
   ```

3. Instale as dependências:
   Para produção:
   ```bash
   pip install -r requirements.txt
   ```
   Para desenvolvimento:
   ```bash
   pip install -r requirements-dev.txt
   ```

4. Configure as variáveis de ambiente:
   Crie um arquivo `.env` na raiz do projeto e adicione as seguintes variáveis:
   ```bash
   SECRET_KEY=sua_chave_secreta_muito_segura
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   DATABASE_URL=sqlite:///./sql_app.db
   ```

5. Execute as migrações do banco de dados:
   ```bash
   alembic upgrade head
   ```

## Executando a aplicação

Para iniciar o servidor de desenvolvimento:

```bash
uvicorn app:app --reload
```

Acesse a documentação da API em [http://localhost:8000/docs](http://localhost:8000/docs)

## Testes

Para executar os testes:

```bash
pytest
```

Para verificar a cobertura de testes:

```bash
coverage run -m pytest
coverage report
```

## Endpoints Disponíveis

### Autenticação

- **POST /token**: Login para obter um token de acesso.
    - Corpo da requisição: `username`, `password`
    - Resposta: Token de acesso

### Administração

- **GET /admin**: Ler informações de administrador (requer autenticação).
- **GET /admin/users**: Listar todos os usuários (requer autenticação).
- **POST /admin/users**: Criar um novo usuário (requer autenticação).
    - Corpo da requisição: `username`, `password`, `role`
- **PATCH /admin/users/change/password/{username}**: Alterar a senha de um usuário (requer autenticação).
    - Parâmetros: `username` (na URL), `password` (query parameter)
- **DELETE /admin/users/{username}**: Excluir um usuário (requer autenticação).
    - Parâmetros: `username` (na URL)

### Usuário

- **GET /user**: Ler informações do usuário atual (requer autenticação).

### Saúde do Sistema

- **GET /health**: Verificar o status de saúde do sistema.

### Raiz

- **GET /**: Endpoint raiz.

## Usuários Disponíveis

Para fins de teste, os seguintes usuários estão disponíveis:

1. Usuário comum:
    - Username: user
    - Senha: L0XuwPOdS5U
    - Função: user

2. Usuário administrador:
    - Username: admin
    - Senha: JKSipm0YH
    - Função: admin

Estes usuários podem ser utilizados para testar diferentes níveis de acesso na API. Lembre-se de que em um ambiente de
produção, você deve alterar essas credenciais e implementar um sistema seguro de gerenciamento de usuários.

## Como Usar

1. **Autenticação**:
    - Faça uma requisição POST para `/token` com o nome de usuário e senha para obter um token de acesso.
    - Exemplo para o usuário comum:
      ```bash
      POST /token
      Body: 
      {
        "username": "user",
        "password": "L0XuwPOdS5U"
      }
      ```
    - Exemplo para o usuário administrador:
      ```bash
      POST /token
      Body: 
      {
        "username": "admin",
        "password": "JKSipm0YH"
      }
      ```
    - Use o token recebido no cabeçalho `Authorization` como `Bearer {seu_token}` para acessar endpoints protegidos.

2. **Endpoints Administrativos**:
    - Todos os endpoints `/admin` requerem autenticação de um usuário com função de administrador.

3. **Gerenciamento de Usuários**:
    - Use `/admin/users` para criar, listar, atualizar senhas e excluir usuários.

4. **Informações do Usuário**:
    - Acesse `/user` para obter informações sobre o usuário autenticado atual.

5. **Verificação de Saúde**:
    - Use `/health` para verificar o status do sistema, incluindo uso de CPU, memória e disco.

6. **Endpoint Raiz**:
    - Acesse `/` para uma resposta básica do servidor.

Lembre-se de incluir o token de acesso no cabeçalho `Authorization` para todos os endpoints protegidos.

## Estrutura do Projeto

```
fastapi-minimal/
│
├── alembic/
├── alembic.ini
├── app/
│   ├── api/
│   │   ├── admin.py
│   │   ├── auth.py
│   │   ├── health.py
│   │   ├── router.py
│   │   ├── users.py
│   │   └── __init__.py
│   ├── controllers/
│   │   ├── admin.py
│   │   └── __init__.py
│   ├── core/
│   │   ├── config.py
│   │   ├── database.py
│   │   ├── security.py
│   │   └── status.py
│   ├── models/
│   │   ├── user.py
│   │   └── __init__.py
│   ├── schemas/
│   │   ├── health.py
│   │   └── user.py
│   ├── utils/
│   │   ├── converters.py
│   │   └── __init__.py
│   ├── main.py
│   └── __init__.py
├── tests/
│   ├── .pytest_cache/
│   ├── config.py
│   └── test_user.py
├── pyproject.toml
├── pytest.ini
├── README.md
├── requirements-dev.txt
├── requirements.txt
```

### Descrição da Estrutura

- `alembic/`: Contém arquivos relacionados às migrações do banco de dados.
- `app/`: Diretório principal da aplicação.
    - `api/`: Contém os endpoints da API.
    - `controllers/`: Lógica de controle para operações complexas.
    - `core/`: Configurações centrais e utilitários.
    - `models/`: Definições dos modelos de dados.
    - `schemas/`: Esquemas Pydantic para validação de dados.
    - `utils/`: Funções utilitárias.
- `tests/`: Contém os testes da aplicação.
- `requirements.txt` e `requirements-dev.txt`: Dependências do projeto.

Esta estrutura segue boas práticas de organização de projetos FastAPI, separando claramente as diferentes camadas e
componentes da aplicação.

## Contato

Kalebe Silva - contato@kalebeasilva.dev  
Link do Projeto: [https://github.com/kalebeasilvadev/fastapi-minimal](https://github.com/kalebeasilvadev/fastapi-minimal)

