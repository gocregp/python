import datetime

import requests
from pprint import pprint
from config import open_weather_token


def get_weather(city, open_weather_token):

    code_to_smile = {
        "Clear": "Ясно \U0001f601",
        "Clouds": "Облачно \U0001f602",
        "Rain": "Дождь \U0001f923",
        "Snow": "Снег \U0001f328",
        "Mist": "Туман \U0001f32B",
        "Thunderstorm": "Гроза \U000026A1"
    }

    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
            # f"https://api.openweathermap.org/data/3.0/onecall?lat={city}&appid={open_weather_token}"
        )
        data = r.json()
        # pprint(data)

        city = data["name"]
        cur_weather = data["main"]["temp"]

        weather_desc = data["weather"][0]["main"]
        if weather_desc in code_to_smile:
            wd = code_to_smile[weather_desc]
        else:
            wd = "Посмотри сам в окно"

        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_jf_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(data["sys"]["sunrise"])


        print(
        f"*******{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}********"
        f"Погода в городе {city}\n"
        f"Температура: {cur_weather}°C {wd}\n"
        f"Сила ветра: {wind} м/с\n"
        f"Восход солнца: {sunrise_timestamp}\n"
        f"Заход солнца: {sunset_timestamp}\n"
        f"Продолжительность дня: {length_jf_the_day}\n"
        f"Хорошего дня!")

    except Exception as ex:
        print(ex)
        print('Проверьте название города')


def main():
    city = input('Введите город: ')
    get_weather(city, open_weather_token)


if __name__ == '__main__':
    main()