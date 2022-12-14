"""
Наборы создаются с использованием фигурных скобок и содержат уникальные значения.
Учитывая два набора, найдите и выведите все элементы, которые являются общими для обоих наборов.
Например, для следующих наборов:
{'a', 'b', 'c'}
{'c', 'd', 'e'}
Результат должен быть {'c'}, так как он присутствует в обоих наборах.
Результатом должен быть набор, содержащий общие элементы.

"""

set1 = {2, 4, 5, 6}
set2 = {4, 6, 7, 8, 11, 42, 2}
print(set1 & set2)