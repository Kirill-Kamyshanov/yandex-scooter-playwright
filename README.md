# 🛴 Яндекс Самокат — API / UI автотесты

Проект автоматизации тестирования сервиса аренды самокатов  
[Яндекс Самокат](https://qa-scooter.praktikum-services.ru/)

---

## 📦 Запуск тестов в docker-контейнере
```
docker-compose up — собрать и запустить тесты
docker-compose up --build — пересобрать образ и запустить тесты (в случае изменений в коде)
docker-compose down — остановить контейнеры
docker-compose run tests --browser chromium — запустить в конкретном браузере (по умолчанию chromium)
docker-compose run tests --env stage - запустить тесты в конкретном окружении (по умолчанию dev)
docker-compose run tests -m smoke — запустить smoke-тесты
```



## 📦 Подготовка к запуску

```bash
1. Установка зависимостей
uv sync

2. Установка браузеров (Chromium, Firefox, WebKit)
uv run playwright install
```

## 🚀 Запуск тестов
```bash
# Запуск в выбранном окружении (dev / stage)
pytest --env=dev

# Запуск в выбранном браузере (chromium / firefox / webkit)
pytest --browser=firefox
```

## Генерация Allure-отчёта
``` bash
# Просмотр отчёта
allure serve

# Генерация в папку reports
allure generate allure-results -o reports --clean
```