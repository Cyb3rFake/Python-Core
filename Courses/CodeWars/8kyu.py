""""
Основные математические операции

Ваша задача — создать функцию, которая выполняет четыре основные математические операции.

Функция должна принимать три аргумента - операция(строка/символ), значение1(число), значение2(число).
Функция должна возвращать числовой результат после применения выбранной операции.

Примеры(Оператор, значение1, значение2) --> вывод
('+', 4, 7) --> 11
('-', 15, 18) --> -3
('*', 5, 5) --> 25
('/', 49, 7) --> 7
"""""

def basic_op(operator, value1, value2):
    if operator == '+':
        return int(value1)+int(value2)
    elif operator == '-':
        return int(value1)-int(value2)
    elif operator == '*':
        return int(value1)*int(value2)
    elif operator == '/':
        return float(value1)/float(value2)

"""
Века От Года
Введение
Первое столетие охватывает период с 1 года по 100 год включительно , второе столетие — с 101 года по 200 год включительно и т. д.

Задача
Учитывая год, верните столетие, в котором он находится.

Примеры
1705 --> 18
1900 --> 19
1601 --> 17
"""
def century(year):
    return int(year)//100 if int(year) % 100 == 0 else int(year)//100+1

"""
Создайте функцию, которая выдает персонализированное приветствие. Эта функция принимает два параметра: nameи owner.

Используйте условные выражения, чтобы вернуть правильное сообщение:

кейс	возвращаться
имя равно владельцу	'Привет босс'
в противном случае	«Привет, гость»
"""
def greet(name, owner):
    return f'Hello boss' if name==owner else 'Hello guest'

"""
Given an array of integers, return a new array with each value doubled.
For example:
[1, 2, 3] --> [2, 4, 6]
"""
def maps(a):
    return [i+i for i in a]
"""
Вы были в походе с друзьями далеко от дома, но когда пришло время возвращаться, вы понимаете, 
что топливо на исходе, а ближайшая заправка далеко 50! Вы знаете, 
что в среднем ваш автомобиль расходует около 25миль на галлон. Остаются 2галлоны.
Учитывая эти факторы, напишите функцию, которая говорит вам, можно ли добраться до насоса или нет.
Функция должна возвращаться true, если это возможно, а falseесли нет.
"""
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return True if (int(mpg) * int(fuel_left))>=int(distance_to_pump) else False

"""
Разбить предложение
Напишите функцию, которая берет массив слов, объединяет их в предложение и возвращает предложение. 
Вы можете игнорировать необходимость очистки слов или добавления знаков препинания, 
но вы должны добавлять пробелы между каждым словом. Будьте внимательны, не должно быть пробела ни в начале, ни в конце предложения!

Пример
['hello', 'world', 'this', 'is', 'great']  =>  'hello world this is great'
"""
def smash(words):
    res = ' '.join(words)
    return res

"""
Преобразовать число в перевернутый массив цифр
Учитывая случайное неотрицательное число, вы должны вернуть цифры этого числа в массиве в обратном порядке.

Пример (ввод => вывод):
35231 => [1,3,2,5,3]
0 => [0]
"""
def digitize(n):
    s = str(n)[::-1]
    return [int(i) for i in s]
    # return map(int, str(n)[::-1]) //
"""
Напишите функцию, которая разбивает строку и преобразует ее в массив слов.

Примеры (ввод ==> вывод):
"Robin Singh" ==> ["Robin", "Singh"]
"""
def string_to_array(s):
    return s.split(' ')

"""
Напишите функцию для преобразования имени в инициалы. Это ката строго состоит из двух слов с одним пробелом между ними.
На выходе должны быть две заглавные буквы с точкой, разделяющей их.
Это должно выглядеть так:
Sam Harris=>S.H
patrick feeney=>P.F
"""
def abbrev_name(name):
    res = name.split(' ')
    return f'{res[0][0].upper()}.{res[1][0].upper()}'

"""
Создайте функцию, которая возвращает массив целых чисел от n до 1, где n>0.
Пример: n=5-->[5,4,3,2,1]
"""
def reverse_seq(n):
    return list(reversed([int(i) for i in range(1,n+1)]))
"""
Завершите функцию квадратной суммы, чтобы она возводила в квадрат каждое переданное ей число, а затем суммировала результаты.
Например, for [1, 2, 2]это должно возвращаться, 9 потому что 1^2 + 2^2 + 2^2 = 9.
"""
def square_sum(numbers):
    res = 0
    for i in numbers:
        res += i**2
    return res
"""

Камень ножницы Бумага
Давайте играть! Вы должны вернуть, какой игрок выиграл! В случае ничьей возврат Draw!.
Примеры (Ввод1, Ввод2 --> Выход):

"scissors", "paper" --> "Player 1 won!"
"scissors", "rock" --> "Player 2 won!"
"paper", "paper" --> "Draw!"
"""

def rps(p1, p2):
    if (p1 =='scissors' and p2 =='paper') or (p1 =='paper' and p2 =='rock') or (p1 =='rock' and p2 =='scissors'):
        return "Player 1 won!"
    elif (p2 =='scissors' and p1 =='paper') or (p2 =='paper' and p1 =='rock') or (p2 =='rock' and p1 =='scissors'):
        return "Player 2 won!"
    elif p1 == p2:
        return "Draw!"

    #
    # beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    # if beats[p1] == p2:
    #     return "Player 1 won!"
    # if beats[p2] == p1:
    #     return "Player 2 won!"
    # return "Draw!

"""
Рассмотрим массив/список овец, где некоторые овцы могут отсутствовать на своем месте. 
Нам нужна функция, которая подсчитывает количество овец, присутствующих в массиве (true означает наличие).

Например,

[True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]
"""
array = [True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False,  'sdf', True ,
  True,  True,  True,  True ,
  False, False, True,  True]

def count_sheeps(sheep):
    res = 0
    for i in sheep:
        if i == True:
            res += 1
    return res
    # return arrayOfSheeps.count(True)

print(count_sheeps(array))