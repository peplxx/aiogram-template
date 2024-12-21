db:
	docker compose up --build database -d

migrate:
	alembic upgrade head

run-local: db migrate
	poetry run python -m app

env:
	cp .env.example .env
