# Алгоритм Евклида поиска НОД вычитанием
import numbers


# наибольший общий делитель через минус
def nod_minus(a, b):
    # a, b = 345, 555
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    else:
        print('Наибольший общий делитель:', a)


# сумма НОД
def nod_sum(a,b):
    # a, b = list(map(int, input("Ведите два сравниваемые два сравниваемых числа в одну строку через пробел: ").split()))
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


# наименьший общий делитель
def nod_divine(a,b):
    # a, b = list(map(int, input("Ведите два сравниваемые два сравниваемых числа в одну строку через пробел: ").split()))
    while b > 0:
        c = a % b
        a = b
        b = c
    return a

# наименьшее общее кратное через НОД
def nok(a,b):
    nod = nod_divine(a,b)
    c = a*b
    res = int(c/nod)
    return res


# t = 7
# while t > 1:
#     t -= 1
#     if t == 3 or t == 1:
#         continue
#     print(t)

num = 1
print(type(num),
      isinstance(num, numbers.Number),
      )

num1 = True


print(isinstance(num1, numbers.Integral))
print(isinstance(num1, numbers.Number))

# print(num1.as_integer_ratio())


