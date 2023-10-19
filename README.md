#
Тестовое задание FastApi

## Подготовка сервера

```bash
# Создайте файл .env в директории проекта и укажите в нем:
POSTGRES_USER #postgres
POSTGRES_PASSWORD #postgres
POSTGRES_DB  #postgres
DB_NAME #blog
DB_HOST #db
DB_PORT #5432

```

Все действия мы будем выполнять в Docker, docker-compose.

## Запуск

Запустите контейнер командой docker-compose up

Выполните по очереди команды:

```bash
docker-compose exec backend alembic revision --autogenerate -m "quiz_table"
 docker-compose exec backend alembic upgrade head
```

Теперь проект доступен по адресу http://localhost:8000/docs

###
Автор проекта - Артур Шутов
###
