# Microservices Demo with FastAPI + Frontend

Простой пример асинхронных микросервисов на FastAPI с фронтендом для тестирования.

## Состав проекта

- **serv1**: Основной сервис (порт `3001`)
  - `/health` — проверка работоспособности
  - `/ask_serv2` — запрос к serv2

- **serv2**: Второй сервис (порт `3002`)
  - `/health` — проверка работоспособности
  - `/hello` — тестовый эндпоинт

- **frontend**: Веб-интерфейс (порт `80`)
  - Кнопки для тестирования API

## Запуск проекта

1. Убедитесь, что установлены:
   - Docker
   - Docker Compose

2. Клонируйте репозиторий (если нужно):
   ```bash
   git clone https://github.com/your-repo/microservices-demo.git
   cd microservices-demo
   ```

3. Запустите все сервисы:
   ```bash
   docker-compose up --build
   ```

4. Откройте в браузере:
   - Фронтенд: http://localhost
   - API Serv1: http://localhost:3001/docs
   - API Serv2: http://localhost:3002/docs

## Доступные команды

| Действие               | Команда                     |
|------------------------|-----------------------------|
| Запуск                 | `docker-compose up`         |
| Запуск с пересборкой   | `docker-compose up --build` |
| Остановка              | `docker-compose down`       |
| Просмотр логов         | `docker-compose logs -f`    |

## Технологии

- Backend: Python + FastAPI + httpx
- Frontend: HTML/JS (чистый), раздается через Nginx
- Инфраструктура: Docker + Docker Compose