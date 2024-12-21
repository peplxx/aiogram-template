ifeq ($(shell test -e '.env' && echo -n yes),yes)
	include .env
endif

db:
	docker compose up --build tg-database -d

upgrade:
	make -C telegram-bot upgrade

run-local: db upgrade
	poetry run python -m app

run-docker:
	docker compose up --remove-orphans

env:
	cp .env.example .env
