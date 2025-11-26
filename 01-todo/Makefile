.PHONY: run migrations migrate superuser setup

run:
	python manage.py runserver

migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

superuser:
	python manage.py createsuperuser

setup: migrate superuser
