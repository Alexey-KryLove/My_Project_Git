## Telegram Weather Bot 🌤

Этот проект — бот для Telegram, который предоставляет пользователям информацию о погоде.    
Он использует библиотеку aiogram для обработки сообщений и BeautifulSoup для парсинга данных с сайта rp5.ru.



## Функционал

**📌 Стартовое меню с командами:**  
`/start` — запуск бота и отображение меню  
Описание — информация о версии бота и ссылка на автора  
Погода — получение текущих данных о погоде (записанных в .txt файл ранее)  
Обновить погоду — обновление данных с возможностью выбора города  
Секрет — небольшой сюрприз 😉  

        @dp.message(Command('start'))
        async def start_bot(message: types.Message):
            kb = [
                [types.KeyboardButton(text='Описание'), types.KeyboardButton(text='Секрет')],
                [types.KeyboardButton(text='Погода'), types.KeyboardButton(text='Обновить погоду')]
            ]
            keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True) 
            await message.answer(f'Приветствую тебя, {message.from_user.full_name} на закрытом тестировании данного проекта!', reply_markup=keyboard)
            await asyncio.sleep(0.5)
            await message.answer('\U0001F916')

Более подробно ознакомиться с кодом можно в файле [Bot_v0_1.py](https://github.com/Alexey-KryLove/My_Project_Git/blob/49a88d1512a1858c4cad060d903fed6e7958ac3a/Bot_v0_1.py)

**⛅ Получение погоды:**   
Бот читает данные о погоде из файла `pogoda.txt`, если они уже есть.   
Обновление данных происходит через парсер [parsing.py](https://github.com/Alexey-KryLove/My_Project_Git/blob/49a88d1512a1858c4cad060d903fed6e7958ac3a/parsing.py), который получает актуальную информацию с rp5.ru.

        def get_weather_rp5(url: str):
            headers = {
                "User-Agent": "YOU_User-Agent"
            }
            response = requests.get(url, headers=headers)
        
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")
                weather_desc = soup.find("span", class_="t_0").text.strip()
                wind_power = soup.find("div", class_="wv_0").text.strip()
                wind_direction = soup.find("td", class_="grayLittled2 underlineRow").text.strip()
                
                with open('pogoda.txt', 'w', encoding='utf-8') as file:
                    file.write(f'Погода в {citys[city]}: {weather_desc}, Ветер: {winds[wind_direction]}, {wind_power} метра в секунду')
            else:
                print("Ошибка получения данных о погоде")

Более подробно ознакомиться с кодом можно в файле [parsing.py](https://github.com/Alexey-KryLove/My_Project_Git/blob/49a88d1512a1858c4cad060d903fed6e7958ac3a/parsing.py)

**🌍 Выбор города:**   
На данный момент поддерживаются Москва и Новосибирск.   
_В будущих обновлениях бот будет подключен к БД с городами, что позволит расширить список доступных городов._


## Технологии   

**Python 3.13**    
**Aiogram** — асинхронная библиотека для создания Telegram-ботов  
**BeautifulSoup** — библиотека для парсинга HTML-страниц  
**Asyncio** — асинхронная библиотека  
**Subprocess** — встроенный модуль для запуска и контроля программ   
**Requests** — библиотека для отправки HTTP-запросов   

<details close>
    <summary><b>Установка</b></summary>

**Клонируйте репозиторий:**

        git clone https://github.com/you-nick/My_Project_Git.git  
         

**Создайте виртуальное окружение (опционально):**  

        python -m venv venv  
        source venv/bin/activate  # для macOS/Linux  
        venv\Scripts\activate    # для Windows  

**Установите зависимости:**  

        pip install -r requirements.txt  

**Создайте .env файл и запишите туда токен Telegram бота:**  

token = "YOU_TOKEN"

</details>

<details close>
    <summary><b>Запуск</b></summary>


**Запустите бота:**  

`python Bot_v0_1.py`  

Напишите `/start` боту в Telegram.

</details>

## Поддержка

🔗 Telegram: @CatWoolf
<img src="https://github.com/user-attachments/assets/d88ceb68-70dd-4d52-8e01-bb5a44e5e687" width="90" colot="while" />


