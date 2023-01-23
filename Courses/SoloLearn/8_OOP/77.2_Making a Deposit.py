"""
Скрытие данных

Вам дан класс BankAccount, и вам нужно добавить к нему метод deposit(), который добавляет указанную сумму в свойство private balance. Код должен объявить объект BankAccount с начальным балансом 0, взять число из пользовательского ввода, добавить его к балансу с помощью метода deposit() и вывести объект. Завершите требуемый метод deposit(), чтобы код работал должным образом и выдавал требуемый результат.

Помните, методы в классе должны иметь self в качестве первого параметра, который используется для доступа к свойствам.

"""


class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def __repr__(self):
        return "Account Balance: {}".format(self._balance)

    def deposit(self, value):
        self._balance += value

        # место для вашего кода


acc = BankAccount(0)
acc.deposit(int(input()))
print(acc)
