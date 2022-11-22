"""

Заполните предоставленный код, чтобы наследовать класс Car от класса Vehicle,
создайте объект Car и вызовите его метод horn(), который наследуется от суперкласса Vehicle.

"""

class Vehicle:
    def horn(self):
        print("Beep!")

class Car(Vehicle):
    def __init__(self, name, color):
        self.name = name
        self.color = color

obj = Car("BMW", "red")
obj.horn()
