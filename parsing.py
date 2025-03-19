import requests
from bs4 import BeautifulSoup
import sys

winds = {'С':'Северный',
        'Ю':'Южный',
        'В':'Восточный',
        'З':'Западный',
        'С-В':'Северо-Восточный',
        'С-З':'Северо-Западный',
        'Ю-З':'Юго-Западный',
        'Ю-В':'Юго-Восточный'
        }

if len(sys.argv) < 2:
    print("Ошибка: нужно указать город.")
    sys.exit(1)

city = sys.argv[1]

citys = {
    "Новосибирск": "Новосибирске",
    "Москва": "Москве_(ВДНХ)"
}
if city not in citys:
    print("Город не найден.")
    sys.exit(1)

url = f"https://rp5.ru/Погода_в_{citys[city]}"

def get_weather_rp5(url: str):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        weather_desc = soup.find("span", class_="t_0").text.strip()
        wind_power = soup.find("div", class_="wv_0").text.strip()
        wind_direction = soup.find("td", class_="grayLittled2 underlineRow").text.strip()
        print(f"Погода в {citys[city]}: {weather_desc}, Ветер: {winds[wind_direction]}, {wind_power} метра в секунду")



        with open('pogoda.txt', 'w', encoding='utf-8') as file:
            file.write(f'Погода в {citys[city]}: {weather_desc}, Ветер: {winds[wind_direction]}, {wind_power} метра в секунду')
    else:
        print("Ошибка получения данных о погоде")

if __name__ == "__main__":
    # URL = f"https://rp5.ru/Погода_в_{citys[city]}"
    get_weather_rp5(url)



