import requests
import datetime
import config


def get_weather(city_, api_key=config.api_key):
    coords = get_cords(city_, api_key)
    r = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?lat={coords[0]}&lon={coords[1]}&lang=ru&appid={api_key}&units=metric')
    data = r.json()

    city = data['name']  # название города
    city_print = city_.title() + ' (место по координатам ==> "' + data["name"] + '")'  # назвение города
    cur_temp = data["main"]["temp"]  # текущая температура воздуха
    feels_like = data["main"]["feels_like"]  # ощущается на
    cur_pressure = data["main"]["pressure"]  # давление
    wind = data["wind"]["speed"]  # скорость ветра
    weather = dict(data["weather"][0]).get('description').title()  # погода
    humidity = data["main"]["humidity"]  # влажность
    sunrise = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])  # время восхода
    sunset = datetime.datetime.fromtimestamp(data["sys"]["sunset"])  # влажность
    return (f'В городе: {city_print}\nТемпература: {cur_temp}C, {weather} \nОщущается как: {feels_like} С\n'
            f'Влажность: {humidity} %\nДавление: {cur_pressure} мм.рт.ст\nВетер: {wind} м\с\n'
            f'Восход в {sunrise}\nЗакат в {sunset}\nПродолжительность дня составляет: {sunset - sunrise}')


def get_cords(city_, api_key=config.api_key):
    while True:
        try:
            r = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_}&limit=1&appid={api_key}').json()

            # pprint(r)
            # print('*'*50)
            # print(r[0]['lat'],r[0]['lon'])
            # print('*' * 50)
            # LAT,LON = r[0]['lat'],r[0]['lon']
            return r[0]['lat'], r[0]['lon']
        except EOFError as ex:
            print("Координаты города не найдены")

            # answ = input("Введенного города нет в списке )-: Введете другой? (y/n)")
            # if answ in ['да','Да','д','Y','y','Yes','yes']:
            #     city = input("Введите город: ")
            # else:
            #     print('Досвидос!!!')
            #     exit()

# print(get_cords('lipetsk'))

# print(get_weather('lipetsk'))
