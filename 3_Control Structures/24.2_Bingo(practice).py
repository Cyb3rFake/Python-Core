# Получив список чисел, выведите "bingo", если он содержит введенное число.

items = [42, 88, 721, 12, 43, 22, 908]
num = int(input())
if items.count(num):
    print("Bingo")

