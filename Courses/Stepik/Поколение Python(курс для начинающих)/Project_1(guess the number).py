""""Игра угадай число"""
import random


# приглашение к началу игры

def welcome():
    usr_name = ''
    while True:
        try:
            r1,r2 = map(int,input('Введите через запятую границы диапазона угадываемых чисел: ').split(','))
            break
        except ValueError:
            print('Не верный формат')
    print(f'Диапазон угадываемых значений установлен от {r1} до {r2}')
    rnd_num = random.randrange(r1,r2)
    return str(r1),str(r2),rnd_num

# набор фраз для попыток
def phrases_list(n):
    allmost = ['Уже близко', 'Почти угадал', 'Рядышком', 'Тепло']
    far_awy = ['Пока не рядом', 'Не угадал', 'Холодно...', 'Неа...']
    return allmost[n],far_awy[n]

# проверка на число и диапазон
def check_digit():
    num = c_num
    range_ = c_range
    ch_digit = False
    ch_range = False

    if num.isdigit() == True:
        num = 'Введено число'
        ch_digit = True
    else:
        num = 'Введено не число'

    if  range_[0]<=int(c_num)<=range_[1] in range_:
        range_ = 'Введенное число в диапазоне'
        ch_range = True
    else:
        range_= 'Введенное число вне диапазона'

    return ch_digit,ch_range, num, range_


# проверка на
def cheker_num():
    r1, r2, rnd_num = welcome()
    counter = 0
    ask_num = int(input('Введите число: '))
    # print(type(ask_num), ask_num,type(rnd_num),rnd_num)
    print(ask_num,rnd_num)
    while True:
    # while rnd_num != ask_num:
        rnd = random.randrange(0, 3)
        counter+=1
        ask_num = int(input())
        if ask_num == rnd_num:
            return print(f'Угадал,сука! С {counter}й попытки!')
        if (ask_num - rnd_num) >= -5 :
            print(f'{phrases_list(rnd)[0]}')
        else:
            print(f'{phrases_list(rnd)[1]}')

cheker_num()

# a,b,c = welcome()
# print(a,b,c)
# a = 5
# b = int(input())
# while a!=b:
#     b = int(input())
# else:
#     print('Hui')
