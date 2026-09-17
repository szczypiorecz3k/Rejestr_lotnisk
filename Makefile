include .env
export

COMPOSE := docker compose 
COMPOSE_MANAGE := docker compose exec web python manage.py


docker-down:
	$(COMPOSE) down

docker-clean:
	$(COMPOSE) down -v

docker-build:
	$(COMPOSE) up -d --build

docker-up:
	$(COMPOSE) up -d --remove-orphans

superuser:
	$(COMPOSE_MANAGE) createsuperuser

admin:
	$(COMPOSE) exec web bash -c "DJANGO_SUPERUSER_USERNAME=$$DB_USER DJANGO_SUPERUSER_PASSWORD=$$DB_PASSWORD DJANGO_SUPERUSER_EMAIL=$$DB_EMAIL python manage.py createsuperuser --noinput"

makemigrations:
	$(COMPOSE_MANAGE) makemigrations

migrate:
	$(COMPOSE_MANAGE) migrate

docker-reset:
	$(MAKE) docker-clean
	$(MAKE) docker-up
	sleep 3
	$(MAKE) migrate
	$(MAKE) admin

shell:
	$(COMPOSE_MANAGE) shell

bash:
	$(COMPOSE_MANAGE) bash

.PHONY: docker-down docker-up superuser admin makemigrations migrate docker-reset shell bash 