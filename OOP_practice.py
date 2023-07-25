def foo(x, y): # что возращает эта функция
    return x + y


# print(foo(32,41))
# print(foo('32','41'))
# print(foo([32],[41]))

class Animal():#
    legs = 4
    tail = 1
    name = "Неизвестное животное"

    def voice(self):
        return 'Some voice'


class Dog(Animal):
    name = "Собака"

    def voice(self):
        return 'Bark-Bark'


class Cat(Animal):
    name = "Кошка"

    def voice(self):
        return 'Mew-Mew'


class Cow(Animal):
    name = "Корова"

    def voice(self):
        return 'Moo-Moo'


cat = Cat()
dog = Dog()
cow = Cow()
animal = Animal()

band = [cat, dog, cow, animal]

# for i in band:
#     print()
#     print(f'У {i.name}  {i.legs} ноги и {i.tail} хвост\n'
#           f'{i.name} говорит {i.voice()}')
# print(i.voice())


"""
Датаклассы
"""
from dataclasses import dataclass, asdict


@dataclass
class User:
    name: str
    age: int


# a = User('asd',123)
# assert asdict(a) == {'name':'asd','age': 123}
# print(a)

class UserHandle:
    def __init__(self, name, age):
        self.user = User(name, age)

    def get_dataclass(self):
        return asdict(self.user)

    def edit(self, key, value):
        self.user.__dict__[key] = value


n = 234
match n:
    case 0:
        print('first')
    case 1:
        print('second')
    case 2:
        print('third')
    case _:
        print('default')
