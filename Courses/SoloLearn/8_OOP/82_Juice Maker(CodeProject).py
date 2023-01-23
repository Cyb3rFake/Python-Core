"""
соковыжималка


Вам дан класс Juice, который имеет свойства имени и емкости.
Вам необходимо завершить код для включения и добавления двух объектов Juice,
в результате чего будет создан новый объект Juice с объединенной емкостью и именами
двух добавляемых соков. Например, если вы добавите апельсиновый сок емкостью 1,0 и
яблочный сок емкостью 2,5, в результате получится сок: имя: емкость апельсина и
яблока: 3,5 Названия объединены с помощью символа & .

Используйте метод __add__ , чтобы определить пользовательское поведение для оператора + и вернуть результирующий объект.

"""

class Juice:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = float(capacity)

    def __str__(self):
        return (self.name + ' ('+str(self.capacity)+'L)')

    def __add__(self, other):
        # mix_cap = self.capacity + other.capacity
        # mix_name = self.name + '&' + other.name
        # return mix_name+'('+str(mix_cap)+')'
        new_name = self.name + "&" + other.name
        new_capacity = self.capacity + other.capacity
        return Juice(new_name, new_capacity)






a = Juice('Orange', 1.5)
b = Juice('Apple', 2.0)

result = a + b
print(result)