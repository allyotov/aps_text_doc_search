#!make
include .env
export

lint:
	@flake8 searchapp
	@mypy searchapp

install:
	docker-compose up -d

es.check:
	docker-compose exec post_backend python -m searchapp.tools.db elastic

es.logs:
	docker-compose logs elasticsearch

db.create:
	docker-compose exec post_backend python -m searchapp.tools.db create

db.fill:
	docker-compose exec post_backend python -m searchapp.tools.db fill /data/posts.csv

app.run:
	docker-compose exec post_backend python -m searchapp

app.logs:
	docker-compose logs post_backend

down:
	docker-compose down

down.volumes:
	docker-compose down --remove-orphans --volumes --rmi all

dev.db.upd:
	docker-compose -f docker-compose.dev.yml up -d

dev.db.up:
	docker-compose -f docker-compose.dev.yml up

dev.db.create:
	python -m searchapp.tools.db create

dev.db.fill:
	python -m searchapp.tools.db fill ./backend_data/posts.csv

dev.db.down:
	docker-compose -f docker-compose.dev.yml down

dev.db.down.volumes:
	docker-compose -f docker-compose.dev.yml down -t1 --volumes

dev.app.run:
	python -m searchapp

dev.check_es:
	python -m searchapp.tools.db elastic

dev.es.logs:
	docker-compose -f docker-compose.dev.yml logs elasticsearch

remove.images:
	docker rmi -f $(docker images -aq)

clean:
	sudo rm -r -f ./.data/
	mkdir -p .data/es_data
	mkdir -p .data/dev_es_data
	mkdir -p .data/postgres_data