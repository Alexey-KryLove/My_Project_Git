  WeatherBot

WeatherBot — это Telegram-бот для получения прогноза погоды с сайта rp5.ru. 
Он позволяет запрашивать актуальную информацию о погоде в Москве и Новосибирске, 
а также обновлять данные с помощью веб-парсинга.

Функционал

🌤️ Получение текущей погоды в выбранном городе.

🔄 Обновление данных о погоде путём парсинга с сайта rp5.ru.

🛠️ Интерактивное меню с кнопками для удобного управления.

🕵️ Секретная команда с "пасхалкой".

Технологии

Python 3

Aiogram (Telegram API)

BeautifulSoup (Парсинг HTML)

Requests (Работа с HTTP-запросами)

Установка

Клонируйте репозиторий:

git clone https://github.com/your-username/WeatherBot.git
cd WeatherBot

Создайте виртуальное окружение (опционально):

python -m venv venv
source venv/bin/activate  # для macOS/Linux
venv\Scripts\activate    # для Windows

Установите зависимости:

pip install -r requirements.txt

Создайте .env файл и запишите туда токен Telegram бота:

BOT_TOKEN=your_telegram_bot_token

Запуск

Запустите бота:

python Bot_v0.1.py

Напишите /start боту в Telegram.

Поддержка

🔗 Telegram: CatWoolf
