import requests
import datetime
import config

def get_cords(city_, api_key=config.api_key):
    while True:
        try:
            url = f'http://api.openweathermap.org/geo/1.0/direct?q={city_}&limit=1&appid={api_key}'
            r = requests.get(url).json()
            return r[0]['lat'], r[0]['lon']
        except EOFError as ex:
            print("Координаты города не найдены")

def get_weather(city_, api_key=config.api_key):
    coords = get_cords(city_, api_key)
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={coords[0]}&lon={coords[1]}&lang=ru&appid={api_key}&units=metric'
    r = requests.get(url)
    data = r.json()
    
    city = data['name']
    city_print = f'{city_.title()} (место по координатам ==> "{city}")'
    cur_temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    cur_pressure = data["main"]["pressure"]
    wind = data["wind"]["speed"]
    weather = data["weather"][0]["description"].title()
    humidity = data["main"]["humidity"]
    sunrise = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
    sunset = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
    duration = sunset - sunrise
    
    return (f'В городе: {city_print}\nТемпература: {cur_temp}C, {weather} \n'
            f'Ощущается как: {feels_like} С\nВлажность: {humidity} %\n'
            f'Давление: {cur_pressure} мм.рт.ст\nВетер: {wind} м\с\n'
            f'Восход в {sunrise}\nЗакат в {sunset}\nПродолжительность дня составляет: {duration}')
