"""
Статические методы
Завершите данный код, чтобы определить статический метод add()
для класса Calculator, который возвращает сумму своих параметров.
Код принимает на вход два числа и должен возвращать их сумму с
помощью метода add() класса Calculator.


"""


class Calculator:
# your code goes here
    @classmethod
    def add(cls, a, b):
        return a+b

n1 = int(input())
n2 = int(input())

print(Calculator.add(n1, n2))