"""
На этот раз мы хотим написать вычисления с использованием функций и получить результаты. Давайте посмотрим на некоторые примеры:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
Требования:

Должна быть функция для каждого числа от 0 ("ноль") до 9 ("девять")
Должна быть функция для каждой из следующих математических операций: плюс, минус, умножить, разделить на
Каждое вычисление состоит ровно из одной операции и двух чисел
Самая внешняя функция представляет левый операнд, самая внутренняя функция представляет правый операнд.
Деление должно быть целочисленным . Например, это должно возвращать 2, а не 2.666666...:
eight(divided_by(three()))
"""
def zero(s = None): return 0 if s is None else int(s(0))
def one(s = None): return 1 if s is None else int(s(1))
def two(s = None): return 2 if s is None else int(s(2))
def three(s = None): return 3 if s is None else int(s(3))
def four(s = None): return 4 if s is None else int(s(4))
def five(s = None): return 5 if s is None else int(s(5))
def six(s = None): return 6 if s is None else int(s(6))
def seven(s = None): return 7 if s is None else int(s(7))
def eight(s = None): return 8 if s is None else int(s(8))
def nine(s = None): return 9 if s is None else int(s(9))

def plus(d): return lambda x: x + d
def minus(d): return lambda x: x - d
def times(d): return lambda x: x * d
def divided_by(d): return lambda x: x / d

print(seven(times(five())))
