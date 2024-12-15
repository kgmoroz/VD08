# VD08
 Работа с API

# Flask Random Quotes with Dual APIs

Это веб-приложение на Flask, которое отображает случайные цитаты из двух API: [Quotable](https://github.com/lukePeavey/quotable) и [ZenQuotes](https://zenquotes.io/). Цитаты отображаются на языке оригинала и переводятся на русский язык с помощью библиотеки `googletrans`.

## Особенности
- Получение случайных цитат из двух API:
  - [Quotable](https://api.quotable.io/random)
  - [ZenQuotes](https://zenquotes.io/api/random)
- Перевод цитат на русский язык.
- Веб-интерфейс с использованием HTML и Bootstrap.

## Установка и запуск

### Требования
- Python 3.7+
- Установленные библиотеки:
  - Flask
  - requests
  - googletrans (версия 4.0.0-rc1)

### Инструкция по запуску
1. Склонируйте репозиторий:
   ```bash
   git clone https://github.com/your-username/flask-random-quotes.git
   cd flask-random-quotes
   ```

2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

3. Запустите приложение:
   ```bash
   python app.py
   ```

4. Откройте приложение в браузере по адресу: [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Файловая структура проекта
```
flask-random-quotes/
├── app.py               # Основной файл приложения
├── templates/
│   └── index.html       # HTML-шаблон с использованием Bootstrap
├── requirements.txt     # Зависимости проекта
└── README.md            # Документация проекта
```

## Пример HTML-шаблона
```html
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <title>Случайные цитаты</title>
</head>
<body>
    <div class="container text-center mt-5">
        <h1 class="mb-4">Случайные цитаты</h1>

        <div class="row mb-5">
            <div class="col-md-6">
                <h3>Quotable API</h3>
                <blockquote class="blockquote">
                    <p class="mb-0">Оригинал: {{ quotable_quote }}</p>
                    <p class="mb-0 mt-3">Перевод: {{ quotable_translated }}</p>
                    <footer class="blockquote-footer mt-2">{{ quotable_author }}</footer>
                </blockquote>
            </div>
            <div class="col-md-6">
                <h3>ZenQuotes API</h3>
                <blockquote class="blockquote">
                    <p class="mb-0">Оригинал: {{ zen_quote }}</p>
                    <p class="mb-0 mt-3">Перевод: {{ zen_translated }}</p>
                    <footer class="blockquote-footer mt-2">{{ zen_author }}</footer>
                </blockquote>
            </div>
        </div>

        <a href="/" class="btn btn-primary">Обновить цитаты</a>
    </div>
</body>
</html>
```

## Заметки
- Для корректной работы перевода убедитесь, что установлена версия `googletrans==4.0.0-rc1`.
- Если переводчик не работает, возможно, потребуется обновить или переустановить библиотеку.

## Лицензия
Этот проект распространяется под лицензией MIT. Подробности см. в файле `LICENSE` (если применимо).

