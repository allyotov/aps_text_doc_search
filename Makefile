#!make
include .env
export

lint:
	@flake8 searchapp
	@mypy searchapp

dev.db.upd:
	docker-compose -f docker-compose.dev.yml up -d

dev.db.up:
	docker-compose -f docker-compose.dev.yml up

dev.db.create:
	python -m searchapp.tools.db create