# UserBalance - FastAPI + PostgreSQL в Docker

Простое приложение для транзакций монет на FastAPI

## Функционал
- Регистрация пользователя
- Список всех пользователей
- Перевод монет другому пользователю
- Swagger UI по адресу `/docs`

## Технологии
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Alembic](https://alembic.sqlalchemy.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [Pytest](https://docs.pytest.org/)

## Запуск проекта

1. Клонируйте репозиторий:

```bash
git clone https://github.com/Tqgeng/fastapi_user_balance.git
cd fastapi_user_balance
```

2. Соберите и запустите контейнеры:
```bash
docker compose up -d
```
3. Приложение будет доступно по адресу:

Swagger UI: http://localhost:8000/docs

4. Тесты

```bash
pytest tests/test_transfer.py -v

```

5. Структура проекта
```
fastapi-application/
├── actions/ 
├── alembic/  
├── api/               
├── core/              
├── crud/              
├── tests/  
├── utils/         
├── main.py            
```
- **actions/** - скрипты для админских/вспомогательных задач.  
- **alembic/** - миграции Alembic для обновления схем БД. 
- **api/** - здесь описаны все маршруты и эндпоинты FastAPI.  
- **core/** - модели SQLAlchemy, Pydantic-схемы, конфигурации.  
- **crud/** - функции для работы с базой данных.  
- **tests/** - юнит- и интеграционные тесты.  
- **utils/** - удобное наименование для миграций
- **main.py** - запускает FastAPI-приложение.

