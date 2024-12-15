from flask import Flask, render_template
import requests
from googletrans import Translator

# Инициализация Flask-приложения
app = Flask(__name__)
# Инициализация переводчика Google Translator
translator = Translator()

# Маршрут для получения случайных цитат из двух API
@app.route('/')
def index():
    quotable_quote, quotable_author, quotable_translated = "", "", ""
    zen_quote, zen_author, zen_translated = "", "", ""

    # Получение цитаты из Quotable API
    try:
        response = requests.get('https://api.quotable.io/random')
        response.raise_for_status()
        quote_data = response.json()
        quotable_quote = quote_data.get('content', 'Цитата не найдена.')
        quotable_author = quote_data.get('author', 'Неизвестный')
        quotable_translated = translator.translate(quotable_quote, src='en', dest='ru').text
    except requests.exceptions.RequestException as e:
        print(f"Ошибка запроса к Quotable API: {e}")
        quotable_quote = "Не удалось получить цитату."
        quotable_author = "Ошибка"
        quotable_translated = ""

    # Получение цитаты из ZenQuotes API
    try:
        response = requests.get('https://zenquotes.io/api/random')
        response.raise_for_status()
        quote_data = response.json()[0]
        zen_quote = quote_data.get('q', 'Цитата не найдена.')
        zen_author = quote_data.get('a', 'Неизвестный')
        zen_translated = translator.translate(zen_quote, src='en', dest='ru').text
    except requests.exceptions.RequestException as e:
        print(f"Ошибка запроса к ZenQuotes API: {e}")
        zen_quote = "Не удалось получить цитату."
        zen_author = "Ошибка"
        zen_translated = ""

    # Рендеринг HTML-шаблона с двумя блоками цитат
    return render_template(
        'index.html',
        quotable_quote=quotable_quote,
        quotable_author=quotable_author,
        quotable_translated=quotable_translated,
        zen_quote=zen_quote,
        zen_author=zen_author,
        zen_translated=zen_translated
    )

# Запуск приложения
if __name__ == '__main__':
    app.run(debug=True)
