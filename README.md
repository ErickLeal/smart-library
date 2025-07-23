
# Smart Library API

> API de livraria moderna utilizando Python, FastAPI, PostgreSQL, DDD, Clean Architecture e Docker.

## Principais Features
- CRUD de livros
- Estrutura desacoplada (DDD, Clean Architecture, Repository)
- Migrations com Alembic
- Makefile com os comandos

## Estrutura de Pastas
- `app/domain/`: entidades e contratos de domínio
- `app/application/`: controllers, services e schemas (camada de aplicação)
- `app/infrastructure/`: camada de infraestrutura (models, repositórios, integrações externas, etc)
- `alembic/`: migrations do banco

## Como rodar
1. Configure o arquivo `.env` com as variáveis do banco (já pronto para uso local)
2. Suba o ambiente com Docker Compose:
   ```sh
   make up
   # ou
   docker-compose up --build -d
   ```
3. Rode as migrations:
   ```sh
   make migrate
   # ou
   docker-compose exec app alembic upgrade head
   ```
4. Acesse a API em [http://localhost:8000/docs](http://localhost:8000/docs)

## Exemplo de requisição para criar um livro
```sh
curl -X POST http://localhost:8000/books \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Clean Architecture",
    "author": "Robert C. Martin",
    "year": 2017,
    "pages": 432
  }'
```

## Observações
- As tabelas são criadas automaticamente no startup, mas use sempre migrations para evoluir o banco.
- O projeto está pronto para receber novas entidades seguindo o mesmo padrão de pastas.

---
Desenvolvido com foco em boas práticas, escalabilidade e facilidade de manutenção.
