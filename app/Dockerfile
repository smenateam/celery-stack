FROM python:3.7-alpine

ENV PYTHONUNBUFFERED=1
ENV POETRY_VIRTUALENVS_CREATE=false
ENV LISTEN_PORT=8000

COPY . /app
WORKDIR /app

RUN apk update && apk upgrade && \
    # Установка дополнительных пакетов нужна для сборки uvloop
    apk add --no-cache curl gcc cargo libffi-dev musl-dev make libtool autoconf && \
    # Официальный способ установки poetry
    curl -sSL https://install.python-poetry.org | python && \
    # Ставим зависимости
    ~/.local/bin/poetry install && \
    # Удаляем poetry
    curl -sSL https://install.python-poetry.org | python - --uninstall && \
    # Эти пакеты больше не нужны
    apk del cargo curl gcc libffi-dev musl-dev make libtool autoconf && \
    # Чистим кеш
    rm -rf ~/.cache

EXPOSE 8000
ENTRYPOINT python3 app/main.py
