""""Игра угадай число"""

# import random


# приглашение к началу игры

test_num = 5
test_range = (1,10)

def welcome():
    usr_name = ''
    range_ = int(input('Введите границы диапазона угадываемых чисел'))
    pass


# набор фраз для попыток
def phrases_list():
    allmost = ['Уже близко', '', '', '']
    allmost_close = ['Почти угадал', '', '', '']
    far_awy = ['Пока не рядом', 'Не угадал', '', '']


# проверка на число и диапазон
def check_digit():
    num ='asd'
    ch_flag = False
    ch_flag ==True if num.isdigit()==True else print('Введено не число')

    return ch_flag

# проверка на
def cheker_num(num):

    pass