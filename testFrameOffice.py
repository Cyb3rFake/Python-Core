
# letters = ["a", "b", "c"]
# letters.append("d")
# print(len(letters))
# print(letters)
#
# nums = [1, 2, 3]
# nums.append(4)
# print(nums)

# nums = [9, 8, 7, 6, 5]
# nums.append(4)
# nums.insert(2, 11)
# print(len(nums))
# print(nums)



# passwd = "jopa"
# conf = "jopa"
# if passwd == conf:
#     print("Пароль принят")
# else:
#     print("Пароль не принят")


# n = 7911
# n1 = (n//1000)
# n2 = (n//100%10)
# n3 = (n//10%10)
# n4 = (n%10)
# if n1 + n4 == n2 - n3:
#     print("ДА")
# else:
#     print("НЕТ")

# age = int(input())
# if age >= 18:
#     print("Доступ разрешен")
# else:
#     print("Доступ запрещен")

# a = int(input())
# b = int(input())
# c = int(input())
# step = b - a
# if step + b == c:
#     print("YES")
# else:
#     print("NO")

# a = int(input())
# b = int(input())
# if a < b:
#     print(a)
# else:
#     print(b)

# херня не работает
# a = [10,9,11,12]
# a = []
# i = 0
# while i<4:
#     a.append(input())
#     i = i + 1
# print(min(a))

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# n1, n2 = 0, 0
# if a < b:
#     n1 = a
# else:
#     n1 = b
# if c < d:
#     n2 = c
# else:
#     n2 = d
#
# if n1 < n2 :
#     print(n1)
# else:
#     print(n2)

# до 13 включительно – детство;
# от 14 до 24 – молодость;
# от 25 до 59 – зрелость;
# от 60 – старость.
#
# age =60
# if age<=13:
#     print("детство")
# elif age >=14 and age <=24:
#     print("молодость")
# elif age >=25 and age <=59:
#     print("зрелость")
# elif age >= 60:
#     print("старость")


# a = 4
# b =-22
# c = 1
# sum = 0
# if a>=0:
#     sum = sum + a
# if b>=0:
#     sum =sum + b
# if c>=0:
#     sum = sum + c
# print(sum)

# a, b = int(input()), int(input())
# if a > b:
#     print("NO")
# elif a < b:
#     print("YES")
# else:
#     print("Don't know")

# a = -44
# if a <= -3 or a >= 7:
#     print('Принадлежит')
# else:
#     print('Не принадлежит')

# a = -10
# if  a > -30 and a <= -2 or a > 7 and a <= 25 :
#     print('Принадлежит')
# else:
#     print('Не принадлежит')

# x = 1045
# if (x>=1000 and x<=9999):
#     if x%7 == 0 or x%17 == 0:
#
#         print("YES")
#     else:
#         print("NO")
# else:
#     print("NO")


# a, b, c, = int(input()),int(input()),int(input())
# a, b, c, = 3, 4, 6
#
# if a<b+c and b<c+a and c < a +b:
#     print("YES")
# else:
#     print("NO")

# x=2012
# if (x%4==0 and x%100 !=0) or x%400==0:
#     print("YES")
# else:
#     print("NO")

# x1 = int(input("x1= "))
# y1 = int(input("y1= "))
# x2 = int(input("x2= "))
# y2 = int(input("y2= "))
# x = x2 - x1  # разность координат по оси x
# y = y2 - y1  # разность координат по оси y
# if x1==x2 or y1==y2:
#     print('YES')
# else:
#     print('NO')


# x1 = int(input("x1= "))
# y1 = int(input("y1= "))
# x2 = int(input("x2= "))
# y2 = int(input("y2= "))
# x = x2 - x1  # разность координат по оси x
# y = y2 - y1  # разность координат по оси y
# if -1<=x<=1 and -1<=y<=1:
#     print('YES')
# else:
#     print('NO')

# list = [2, 3, 4, 5, 6, 7]
#
# for x in list:
#     if(x%2==1 and x>4):
#         print(x)
#         break

# a,b,c = int(input()),int(input()),int(input())
# if a == b and b == c:
#     print("Равносторонний")
# elif a == b or b == c or c == a:создание номенклатуры в 1с по прототипу
#     print("Равнобедренный")
# else:
#     print("разносторонний")

# a,b,c = int(input()),int(input()),int(input())
# if a<b<c and a<c:

# x = int(input())
# lst1 = [1,3,5,7,8,10,12]
# lst2 = [4,6,9,11]
# if x in lst1:
#     print(31)
# elif x in lst2:
#     print(30)
# else:
#     print(28)

# x = int(input())
# if 60 > x :
#     print("Легкий вес")
# if 60 <= x < 64:
#     print("Первый полусредний вес")
# if 64 <= x < 69:
#     print("Полусредний вес")


# a = 25
# b = 5
# c = "*"
#
# if b==0 and c == "/":
#     print("На ноль делить нельзя!")
# elif c == "/" and b!=0 :
#     print(a/b)
# elif c == "*":
#     print(a*b)
# elif c == "+":
#     print(a+b)
# elif c == "-":
#     print(a-b)
# else:
#     print("Неверная операция")

#
# c1 = "желтый"
# c2 = "красный"
#
# if (c1 == "красный" and c2 == "синий") or (c2 == "красный" and c1 == "синий"):
#     print("фиолетовый")
# elif (c1 == "красный" and c2 == "желтый") or (c2 == "красный" and c1 == "желтый"):
#     print("оранжевый")
# elif (c1 == "синий" and c2 == "желтый") or (c2 == "синий" and c1 == "желтый"):
#     print("зеленый")
# elif (c1 == "синий" and c2 == "синий"):
#     print("синий")
# elif (c1 == "желтый" and c2 == "желтый"):
#     print("желтый")
# elif (c1 == "красный" and c2 == "красный"):
#     print("красный")
# else:
#     print("ошибка цвета")

# c = 36
#
# if c in range(0,37):
#     if c == 0:
#         print("зеленый")
#     elif  1 <= c <= 10:
#         if c%2!=0:
#             print("красный")
#         else:
#             print("черный")
#     elif  11 <= c <= 18:
#         if c%2!=0:
#             print("черный")
#         else:
#             print("красный")
#     elif  19 <= c <= 28:
#         if c%2!=0:
#             print("красный")
#         else:
#             print("черный")
#     elif  29 <= c <= 36:
#         if c%2!=0:
#             print("черный")
#         else:
#             print("красный")
# else:
#     print("ошибка ввода")


# a1 = 1
# b1 = 3
# a2 = 2
# b2 = 4
# if (a1 < a2 and b1 < b2) or (a1 > a2 and b1 > b2) or (a1 > a2 and b2 < b1) or (a1 > a2 and b2 > b1):
#     print("пустое множество")
# elif (a1 < a2 and b1 < b2):
#     print(a2,b1)
# elif (a1 > a2 and b1 > b2):
#     print(a1,b2)
# elif (a1 < a2 and a2 == b2):
#     print(b1,a2)
# elif (a2 < a1 and a1 == b2):
#     print(b2,a1)
# elif a1 == a2 and b1 == b2:
#     print(a1,b1)
# elif a1 == a2 and b1 < b2:
#     print(a1)
# elif a1 > a2 and b2==b1
#     print(b1)

# if a2 > b1 or a1 > b2:
#     print('пустое множество')
# elif a1 == b2:
#     print(a1)
# elif a2 == b1:
#     print(a2)
# else:
#     if a1 > a2:
#         a2 = a1
#     if b1 < b2:
#         b2 = b1
#     print(a2, b2)

# c = int(input())
#
# if c%100==0:
#     print("YES")
# else:
#     print("NO")

# x1 = 1
# x2 = 1
# y1 = 2
# y2 = 6
# if (x1+x2+y1+y2)%2==0:
#     print("YES")
# else:
#     print("NO")

# a =int(input())
# s = str(input())
# if 10<=a<=15 and s =="f":
#     print("YES")
# else:
#     print("NO")

# c = 2
# # c = int(input())
# if c % 2 != 0:
#     print("YES")
# elif c % 2 == 0 and 2 <= c <= 5:
#     print("NO")
# elif c % 2 == 0 and 6 <= c <= 20:
#     print("YES")
# elif c % 2 == 0 and c > 20:
#     print("NO")

# x1 = 4
# x2 = 4
# y1 = 5
# y2 = 5

# if (x1-y1)==(x2-y2) or (x1+y1)==(x2+y2):
#     print("YES")
# else:
#     print("NO")


#
# if (abs(x1-x2)==1 and abs(y1-y2)==2) or (abs(x1-x2)==2 and abs(y1-y2)==1):
#     print("YES")
# else:
#     print("NO")

#
# def shout(word):
#    return word + "!"
# speak = shout
# output = speak("shout")
# print(output)
#
# def add(x, y):
#     return x + y
# def do_twice(func, x, y):
#     return func(func(x, y), func(x, y))
# a = 5
# b = 10
# print(do_twice(add, a, b))
#
# def func(x):
#   res = 0
#   for i in range(x):
#      res += i
#   return res
# print(func(4))


# a = 5
# b = 8
# c = 3
#
# x = [a,b,c]
# x = sorted(x,reverse=True)
# for i in range(len(x)):
#     print(x[i])



# n = "945"
# m = [num for num in n]
#
# minimal = min(m)
# maximal = max(m)
#
# s = sorted(m)
# srednee = (s[1])
# raz = int(maximal) - int(minimal)
# print(f"максимальное минус минимальное = {raz}")
# print(f"среднее = {srednee}")
# if int(raz) == int(srednee):
#     print("Пизда как интересно")
# else:
#     print("Пизда как не интересно")


# sum = 0
# a = [5.4,33,-1232,-3.889,6]
# for i in range(len(a)):
#     sum =+ abs(float(a[i]))
# print(sum)

# try:
#   num1 = input(":")
#   num2 = input(":")
#   print(float(num1)/float(num2))
# except():

# file = open("5_Exceptions & Files/Notes", encoding='utf-8', mode='a')
# cont = file.write("jopahuipizda")
# file = open("5_Exceptions & Files/Notes", encoding='utf-8', mode='r')
# cont1 = file.read(-1)
# print(cont1)
# file.close()

# p1, p2, q1, q2 = 10, 15, 21, 13
# print(int(abs(p1-q1)+abs(p2-q2)))
#
# str1 = '1'
# str2 = str1 + '2' + str1
# str3 = str2 + '3' + str2
# str4 = str3 + '4' + str3
# print(str4)
#
# mystr = '123' * 3 + '456' * 2 + '789' * 1
# print(mystr)


#print("\"Python is a great language!\", said Fred. \"I don't ever remember having this much fun before.\"")

# firstname = input()
# lastname = input()
# print(f"Hello {firstname} {lastname}! You just delved into Python.")

# name = input()
# count = len(name)
# print(f"Футбольная команда {name} имеет длину {count} символов")




"""
Даны названия трех городов. Напишите программу, которая определяет самое короткое и самое длинное название города.

Формат входных данных
На вход программе подаётся названия трех городов, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести самое короткое и длинное название города, каждое на отдельной строке.

Примечание. Гарантируется, что длины названий всех трех городов различны.


# a = [input() for x in range(3)]
a = ["Москва",
     "Санкт-Петербург",
     "Екатеринбург"]
b = [len(a[i]) for i in range(3)]

x ={}
for i in range(3):
    x[b[i]] = a[i]
print(x)

Min = (min(x.items()))
Max = (max(x.items()))

print(Min[1])
print(Max[1])
"""

# import re
#
# s = ['Яблоко', 'яБлоко', 'ябЛоко', 'яблОко', 'яблоКо', 'яблокО']
#
# result = re.search('Яб',s)
# print(result)

# n = 100
# sum = 0
# for i in range(1,n+1,1):
#     if (i**2)%10==2 or (i**2)%10==5 or (i**2)%10==8:
#        sum += i
# print(sum)

# n = 3
# sum = 1
# for i in range(1,n+1,1):
#        sum *= i
# print(sum)

# m = [input() for i in range(1,11,1)]

# m =[8,0,1,2,1,0,0,5,4,12]
# mult = 1
# for i in range(len(m)):
#     if int(m[i]) != 0:
#         mult = mult * int(m[i])
# print(mult)

# n = 10
# sum = 0
# for i in range(1,n+1,1):
#     if n % i==0:
#         sum += i
# print(sum)

# n = 5
# c = -1
# sum = 0
# for i in range(1,n+1,1):
#     if i%2 !=0:
#         sum += i
#     else:
#         sum -= i
# print(sum)
# import time

#
# fib1 = fib2 = 1
# n = int(input())
# if n==1:
#     print(fib1, end=' ')
# else:
#     print(fib1, fib2, end=' ')
#
# for i in range(2, n):
#     fib1, fib2 = fib2, fib1 + fib2
#     print(fib2, end=' ')

# i = str(input())
# c = 0
# while (i != "стоп" and i != "хватит" and i != "достаточно") :
#     c+=1
#     i = str(input())
# print(c)

# i = int(input())
# while i%7==0:
#     print(i)
#     i = int(input())

# i = int(input())
# c = 0
# while i>=0:
#     c += i
#     i = int(input())
# print(c)

# i = int(input())
# c = 0
# while 5 >= i > 0:
#     if i == 5 :
#         c += 1
#     i = int(input())
# print(c)

# n = int(input())
# c = 0
# while n>=25:
#     c +=1
#     n = n - 25
# while n >= 10:
#     c += 1
#     n = n - 10
# while n >= 5:
#     c += 1
#     n = n - 5
# while n >= 1:
#     c += 1
#     n = n - 1
# print(c)

# n = int(input())
# while n != 0:  # пока в числе есть цифры
#     last_digit = n % 10  # получить последнюю цифру
#     # код обработки последней цифры
#     n = n // 10  # удалить последнюю цифру из числа


# num = 123456789
# total = 0
# while num != 0:
#     last_digit = num % 10
#     if last_digit > 4:
#         total += 1
#     num = num // 10
# print(total)

# n=9673210458
# print(n%10)
# while n != 0:
#     last = n%10
#     n //= 10
#     print(last)


# n = str(input())
# sum = 0
# proizv = 1
# for i in range(0,len(n),1):
#
#     sum += int(n[i])
#     proizv *= int(n[i])
# print(sum)
# print(len(n))
# print(proizv)
# print(sum/len(n))
# print(n[0])
# print(int(n[0])+int(n[3]))

# primes = {1: 2, 2: 3, 4: 7, 7:17}
# print(primes[primes[4]])


# fib = {1: 1, 2: 1, 3: 2, 4: 3}
# print(fib.get(4, 0) + fib.get(7, 5))

# print("{0}{1}{0}".format("abra", "cad"))
# abracadabra

# def test(func, arg):
#   return func(func(arg))
#
# def mult(x):
#   return x * x
#
#
#
# print(test(mult, 2))


# # named function
# def polynomial(x):
#     return x ** 2 + 5 * x + 4
# print(polynomial(4))
#
#
# # lambda
# x =4
# print((lambda x: x ** 2 + 5 * x + 4)(x))


# triple = lambda x: x * 3
# add = lambda x, y: x + y
# print(add(triple(3), 4))

# def sum_to(x):
#     if x == 1:
#         return 1
#     else:
#         return x + sum_to(x-1)
# print (sum_to(5))

# def fib(x):
#   if x == 0 or x == 1:
#     return 1
#   else:
#     return fib(x-1) + fib(x-2)
# print(fib(4))
#
# class SpecialString:
#     def __init__(self, cont):
#         self.cont = cont
#
#     def __truediv__(self, other):
#         line = "=" * len(other.cont)
#         return "\n".join([self.cont, line, other.cont])
#
# spam = SpecialString("spam")
# hello = SpecialString("Hello world!")
# print(hello/spam)



print()