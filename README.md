# API FastAPI com Autenticação JWT

Este projeto é uma API FastAPI que implementa autenticação JWT com níveis de acesso para usuários e administradores. Ele utiliza SQLAlchemy para o banco de dados, Alembic para migrações e Pydantic para validação de dados.

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
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio
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


