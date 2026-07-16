# 🛴 Яндекс Самокат — API / UI автотесты

Проект автоматизации тестирования сервиса аренды самокатов  
[Яндекс Самокат](https://qa-scooter.praktikum-services.ru/)

---

## 📦 Подготовка к запуску

```bash
1. Установка зависимостей
pip install -r requirements.txt

2. Установка браузеров (Chromium, Firefox, WebKit)
playwright install
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