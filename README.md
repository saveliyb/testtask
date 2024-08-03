# testtask

## Обзор

Этот проект представляет собой полнофункциональное приложение, включающее в себя FastAPI backend, Telegram-бота и Nginx сервер для обратного проксирования. Backend обрабатывает хранение и получение сообщений с использованием MongoDB, а бот позволяет пользователям взаимодействовать с backend через Telegram. Всё приложение контейнеризовано с помощью Docker, а оркестрация осуществляется с помощью Docker Compose.

## Структура директорий

```plaintext
my_project/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── routers.py
│   │   ├── requirements.txt
│   │   └── Dockerfile
│   └── nginx/
│       ├── nginx.conf
│       └── Dockerfile
├── bot/
│   ├── bot.py
│   ├── requirements.txt
│   └── Dockerfile
└── docker-compose.yml
```

## Компоненты

### Backend

* Приложение FastAPI:
    + main.py: Содержит основной код приложения с эндпоинтами для получения и создания сообщений.
    + models.py: Определяет Pydantic модель для сообщений.
    + routers.py: Содержит логику взаимодействия с базой данных.
* Nginx:
    + nginx.conf: Конфигурационный файл для Nginx, настроенный для проксирования запросов к приложению FastAPI.
* Bot
    + bot.py: Реализует Telegram-бота с использованием aiogram, который взаимодействует с backend для получения и создания сообщений.

## Предварительные требования
* Docker
* Docker Compose
* Токен Telegram бота (замените <token> в docker-compose.yml на ваш реальный токен)

# Установка
1. Клонируйте репозиторий:

```plaintext
git clone <repository-url>
cd my_project
```

2. Создайте файл .env в корневой директории со следующим содержимым (замените <token> на ваш токен Telegram бота):

```plaintext
TELEGRAM_BOT_TOKEN=<token>
```
3. Соберите и запустите Docker контейнеры:

```plaintext
docker-compose up --build
```

## Использование
### API Backend
* Получить сообщения:
    + Endpoint: GET /api/v1/messages/
    + Описание: Получает все сообщения, хранящиеся в базе данных MongoDB.
* Создать сообщение:
    + Endpoint: POST /api/v1/message/
    + Описание: Создает новое сообщение и сохраняет его в базе данных MongoDB.
* Тело запроса:
```plaintext
{
    "text": "Ваш текст сообщения"
}
```
### Команды Telegram бота
* /start: Приветствует пользователя.
* /get_messages: Получает и отображает все сообщения из backend.
* /create_message <your_message>: Создает новое сообщение с указанным текстом.
