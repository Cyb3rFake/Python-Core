"""

Перегрузка оператора

Метод __add__ позволяет определить пользовательское поведение для оператора + в нашем классе.

Предоставленный код пытается сложить вместе два объекта BankAccount, что должно привести к созданию нового объекта с суммой остатков на данных счетах.
Исправьте код, чтобы он работал должным образом, и выведите итоговый баланс счета.

"""


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def __add__(self, other):
        return BankAccount(self.balance + other.balance)

a = BankAccount(1024)
b = BankAccount(42)

result = a + b
print(result.balance)
