"""
FizzBuzz - это хорошо известное задание по программированию, которое задают во время собеседований.
Данный код решает проблему FizzBuzz и использует слова "Solo" и "Learn" вместо "Fizz" и "Buzz".
Он принимает на вход n и выводит числа от 1 до n.
Для каждого числа, кратного 3, выведите "Соло" вместо числа.
Для каждого числа, кратного 5, выводите "Узнать" вместо числа.
Для чисел, кратных как 3, так и 5, выведите "SoloLearn".
Вам нужно изменить код, чтобы пропустить четные числа, чтобы логика
применялась только к нечетным числам в диапазоне.
"""

n = int(input())

for x in range(1, n):
    if x % 2 ==0:
        continue
    if x % 3 == 0 and x % 5 == 0:
        print("SoloLearn")
    elif x % 3 == 0:
        print("Solo")
    elif x % 5 == 0:
        print("Learn")
    else:
        print(x)