"""
класс Студент
Предоставленный код определяет класс Student,
создает объект Student и вызывает его метод great().
Исправьте код, чтобы получить ожидаемый результат.

"""


class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(self.name + " says hi")


obj = Student("John")
obj.greet()