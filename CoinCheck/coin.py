import requests #Что такое импорт и что такое реквест?
import time
import locale 

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
coin_1 = 'USD'
coin_2 = 'RUB'


def run(): #Почему ты назвал функцию run и что такое def?
    print('Сегодня:', time.strftime("%d %B %Y  %H:%M", time.localtime()))
    print(f'Курс {coin_1} к {coin_2}:',
          requests.get(f'https://api.coingate.com/v2/rates/merchant/{coin_1}/{coin_2}').text + ' руб')
