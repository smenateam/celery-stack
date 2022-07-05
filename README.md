# celery-stack
Базовый стек для экспериментов над celery на базе docker-compose

## Описание стека
* **app** - простейшее приложение на fastapi, которое может создавать задачи для celery
* **redis** - используется в качестве брокера для celery
* **worker-1**, **worker-2** - celery воркеры
* **flower** - инструмент мониторинга celery
* **prometheus** - хранилище метрик, полученных из flower

### Используемые порты
* **8080** - API (app)
* **8081** - flower
* **9090** - prometheus

## Установка
### Docker
```bash
docker-compose up
```
При изменениях в приложении нужно пересобрать образ:
```bash
docker-compose build
```

## API
### GET /ping
Пинг API сервиса

#### Пример ответа
```json
{"message": "pong"}
```

### POST /tasks/create
Создает для celery задачу `sleeper_task`, которая просто ждет

#### Параметры
* `sleep_seconds` - обязательный параметр, количество секунд ожидания

#### Пример ответа
```json
{
    "message": "Task was created",
    "task": {
        "id": "def1ece9-7669-4abc-9d47-4bba05f6c0a1"
    }
}
```
