import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
import subprocess



citys = {
    "Новосибирск": "Новосибирске",
    "Москва": "Москве_(ВДНХ)"
}

version = 'Beta_1.1'
bos = '@CatWoolf'
dp = Dispatcher()

#Стартовое сообщение и меню!
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


#меню сообщение 
@dp.message(F.text == 'Описание')
async def menu_message(message: types.Message):
    kb = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text ='Описание', callback_data='description'),types.InlineKeyboardButton(text ='Создатель', url ='https://t.me/CatWoolf')]
    ])
    await message.answer('Версия и Cоздатель', reply_markup=kb)


# Функция для чтения данных о погоде из файла
def read_file():
    try:
        with open('pogoda.txt', "r", encoding="utf-8") as file:
            return file.readlines()
    except Exception as e:
        return [f"Ошибка чтения файла: {e}"]


# Функция для получения погоды (читает из файла)
@dp.message(F.text == "Погода")
async def get_weather(message: types.Message):
    lines = read_file()
    if lines:
        response = lines[0]  
        await message.reply(response)
    else:
        await message.reply("Погоды сейчас нет;(")


#Функция для запуска парсинга и обновления погоды
@dp.message(F.text == "Обновить погоду")
async def update_weather(message: types.Message):
    # Создаем inline-клавиатуру с кнопками
    kb = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text="Москва", callback_data='Moscow')],
        [types.InlineKeyboardButton(text="Новосибирск", callback_data='Novosibirsk')]
    ])

    await message.answer("Какой город интересует?", reply_markup=kb)

 
@dp.callback_query(F.data == "Moscow")
async def moscow_weather(query: types.CallbackQuery):
    await send_weather_info(query, "Москва")

@dp.callback_query(F.data == "Novosibirsk")
async def novosibirsk_weather(query: types.CallbackQuery):
    await send_weather_info(query, "Новосибирск")

    # Запускаем парсер
async def send_weather_info(qyery: types.CallbackQuery, city: str):
    try:
        subprocess.run(["python", "parsing.py", city], check=True)  # Замените на ваш файл парсера
        await asyncio.sleep(1)  # Ждём, пока данные запишутся в файл

        # Читаем обновлённые данные
        lines = read_file()
        if lines:
            response = lines[0]  
            await qyery.message.answer("Погода обновлена! 🌤\n" + response)
        else:
            await qyery.message.answer("Ошибка при обновлении погоды 😞")
    except Exception as e:
        await qyery.message.answer(f"Ошибка запуска парсера: {e}")

#Секретик
@dp.message(F.text == "Секрет")
async def sikret_message(message: types.Message):
    await message.answer('Ты нашел секрет лови призы')
    for _ in range(3):
        await asyncio.sleep(0.5)
        await message.answer('\U0001F4A9')


#Повторяшка всего тектста без меню
@dp.message()
async def echo_message(message: types.Message):
    await message.answer('Подождите, пожалуйста, я думаю...')
    await asyncio.sleep(3)
    await message.send_copy(chat_id=message.chat.id)



#Запуск бота
async def main():
    token = 'YOU_TOKEN'
    bot = Bot(token)
    await dp.start_polling(bot)
    

if __name__ == '__main__':
    asyncio.run(main())
