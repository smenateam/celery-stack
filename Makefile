DC = docker-compose

build-app: app/Dockerfile app/poetry.lock app/app/*.py
	$(DC) build

logs:
	$(DC) logs -f

run: build-app
	$(DC) stop
	$(DC) up -d
