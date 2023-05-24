from CoinCheck.coin import run
import requests as re

if __name__ == '__main__':
    r = re.get('https://api.coingate.com/v2/rates/merchant/USD/RUB').status_code
    if r != 200:
        print("Ошибка соединения!", r)
        exit()
    run()
