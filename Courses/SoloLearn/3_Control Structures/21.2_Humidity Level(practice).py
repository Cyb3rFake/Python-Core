# Комфортная относительная влажность воздуха для человека составляет от 40% до 60%.
# Данная программа принимает процент влажности в качестве входных данных.
#
# Задача
# Заполните код для вывода "нормы", если заданный процент влажности находится в диапазоне от 40 до 60 включительно.
# В противном случае ничего не выводите.

# humidity = int(input())
humidity = 35
if (humidity >= 40 and humidity <= 60):
    print("norm")