## Проект mini_note для тестового задания
***
В проекте реализованы базовые возможности по соданию пользователя, и создание заметок для них. Также при содзании заметок был использован сервис [Яндекс.Спеллер](https://yandex.ru/dev/speller/) для поиска и исправления орфографических ошибок
***
### Использваоенные технологии
+ Python
+ SQLAlchemy
+ Docker

### Основноые фреймворки и библиотеки
+ fastapi
+ alembic
+ pydantic
+ sqlalchemy
+ aiohttp
***
### Запуск проекта через Docker
````
docker build . -t mini_note
docker-compose up
````
### Запросы для взаимодействия с api
(127.0.0.1:8000 использован для примера)

POST-запрос на создание пользвателя
```
curl -X 'POST' \
  'http://127.0.0.1:8000/api/users/create/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "username",
  "password": "password"
}'
```

POST-запрос на создание заметки
```
curl -X 'POST' \
  'http://127.0.0.1:8000/api/notes/create/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "user_schema": {
    "username": "username",
    "password": "password"
  },
  "note_schema": {
    "title": "title",
    "body": "body"
  }
}'
```
POST-запрос для получение всех своих заметок
```
curl -X 'POST' \
  'http://127.0.0.1:8000/api/users/notes/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "username",
  "password": "password"
}'
```
POST-запрос для получение своей заметки по ID
```
curl -X 'POST' \
  'http://127.0.0.1:8000/api/notes/{note_id}' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "username",
  "password": "password"
}'
```
