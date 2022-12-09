""""Игра угадай число"""
import random


# приглашение к началу игры

def input_range():
    while True:
        try:
            r1,r2 = map(str,input('Введите через запятую границы диапазона угадываемых чисел: ').split(','))
            break
        except ValueError:
            print('Не верный формат')
    print(f'Диапазон угадываемых значений установлен от {r1} до {r2}')
    rnd_num = random.randrange(int(r1),int(r2))
    return r1,r2,rnd_num

# набор фраз для попыток
def phrases_list(n):
    allmost = ['Уже близко', 'Почти угадал', 'Рядышком', 'Тепло']
    far_awy = ['Пока не рядом', 'Не угадал', 'Холодно...', 'Неа...']
    return allmost[n],far_awy[n]

# проверка на число и диапазон
def check_digit(r1,r2,c_num):
    num = c_num

    wrong_int =True

    wrong_range = False # wrong_int ='Введено не число >:/'

    if num.isdigit() == False:  # wrong_range = 'Введенное число вне диапазона'

        wrong_int = False
    else:
        num = int(num)
        if  int(r1)<=int(num)<=int(r2):
            wrong_range = True

    return wrong_int,wrong_range


# проверка на
def cheker_num(range1,range2,rnd_num):
    r1, r2, rnd_num = range1, range2, rnd_num
    print(rnd_num)
    ask_num = input('Введите число: ')
    counter = 1
    # if int(ask_num) == rnd_num:
    #     return print('ДаНуНах!!!Читор с 1й попытки')
    while True:
        rnd = random.randrange(0, 3)
        counter+=1
        if check_digit(int(r1),int(r2),ask_num)[0] == False:
            print('Введено не число >:/')
            ask_num = input('Введите число: ')
            continue

        if check_digit(int(r1),int(r2),ask_num)[1] == False:
            print('Введенное число вне диапазона')
            ask_num = input('Введите число: ')
            continue

        if int(ask_num) == rnd_num:
            return print(f'Угадал,сука! С {counter}й попытки!')
        if 5 <= (int(ask_num) - rnd_num) >= -5 :
            print(f'{phrases_list(rnd)[0]}')
        else:
            print(f'{phrases_list(rnd)[1]}')
        ask_num = input()

cheker_num(*input_range())
# a,b,c = welcome()
# print(a,b,c)
# a = 5
# b = int(input())
# while a!=b:
#     b = int(input())
# else:
#     print('Hui')
