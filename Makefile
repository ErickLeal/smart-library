up:
	docker-compose up --build -d

down:
	docker-compose down

migrate:
	docker-compose exec app alembic upgrade head

migration-create:
	docker-compose exec app alembic revision --autogenerate -m "$(MIGRATION_NAME)"

logs:
	docker-compose logs -f app
