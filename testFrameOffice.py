
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
import time

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

# import datetime
# import random
# import time
# # time = str(datetime.datetime.now().time())[0:5]
# # print(time)
# print(time.strftime("%H:%M"))
# from datetime import datetime



# print(f'{time[3]}:{time[4]}')
# ss = 3721
# print()

# class A:
#     def __init__(self, val=0):
#         self.val = val
#
#     def add(self, x):
#         self.val += x
#
#     def print_val(self):
#         print(self.val)
#
#
# a = A()
# b = A(2)
# c = A(4)
# a.add(2)
# b.add(2)
#
# a.print_val()
# b.print_val()
# c.print_val()

# s = 'test'
#
# print(s[:] == s)
# print(s[:] is s)
# print(s[::-1][::-1] == s)
# print(s[::-1][::-1] is s)
#


# list_ = list(set([random.randrange(1,100) for i in range(20)]))
# print(list_)

from MyUtils import *
import requests as re


# my_list = uniq_list(1,10,10)

# def bubble_sort():
#     last_item = len(my_list)-1
#     sor_list =[]
#     print('Получен список: ',my_list)
#     for i in range(0,last_item):
#         for j in range(0,last_item):
#             if my_list[j] > my_list[j + 1]:
#                 my_list[j],my_list[j + 1] = my_list[j + 1],my_list[j]
#
#     print("Отсортированный список: ", my_list)
# print(my_list)
# print(bubble_sort(my_list))



"""  Программирование на Python  https://stepik.org/course/67/syllabus
"""

# 3.4 Файловый ввод/вывод

def decypher(text):
    with open('dataset_3363_2.txt','r') as file:
        text = file.read()

    # inc_str = 'Q10c4G17s20P17p4G20y19p5t16Q14N7Q1L17a13l9I15L14e20U4'
    inc_str = text
    out_str = []
    mult = ''
    for i in range(len(inc_str)-2):
        if inc_str[i].isalpha() == True:
            if inc_str[i+1].isalpha() == False:
                mult += inc_str[i+1]
            if inc_str[i+2].isalpha() == False:
                mult += inc_str[i+2]
            out_str.append(inc_str[i] * int(mult))
        mult = ''
    result =''.join(out_str)
    print(result)

def most_(text = 'abc a bCd bC AbC BC BCD bcd ABC'.lower()):
    with open('dataset_3363_3.txt','r') as file:
        text = ''.join(file.read().split('\n'))


    def get_key(d, value):
        for k, v in d.items():
            if v == value:
                return k

    lst_ = text.lower().split(' ')
    lst_dic = {}
    m_count_l = 0
    for item in set(lst_):
        lst_dic[item] = lst_.count(item)

    val = {i for i in lst_dic if lst_dic[i]==max(lst_dic.values())} #поиск по ключу максимального элемента
    print('Всего элементов:',len(lst_))
    print('Уникальных элементов:',len(set(lst_)))
    print('Больше всего повторяется:',*val,max(lst_dic.values()))

def Students_data():
    # with open('dataset_3363_4.txt','r',encoding='utf8') as file:
    #     text = (file.read())
    with open('dataset_3363_4.txt','r') as file:
        text = (file.read())

    lst = text.split("\n")
    lst1 = []
    math_midle = 0
    phus_midle = 0
    lang_midle = 0
    counter = 0
    for items in lst:
        lst1.append(items.split(';'))

    for item in lst1:
        counter += 1
        try:
            print((int(item[1])+int(item[2])+int(item[3]))/3)
        except:
            print(item, 'Не посчиталось')
            pass
        math_midle += int(item[1])
        phus_midle += int(item[2])
        lang_midle += int(item[3])
    print(math_midle/counter,phus_midle/counter,lang_midle/counter)

# 3.5 Модули, подключение модулей

import math, sys,urllib3
urllib3.disable_warnings() #

def get_perimert(radius_circle):
    return math.pi*2*radius_circle
    # print(get_perimert(float(input())))


def get_args():
    return print(*sys.argv[1::])


# 3.6 Установка дополнительных модулей

def get_strings_count():
    """
    Скачайте файл.
    В нём указан адрес другого файла, который нужно скачать с использованием модуля requests и посчитать число строк в нём.
    Используйте функцию get для получения файла (имеет смысл вызвать метод strip к передаваемому параметру, чтобы убрать пробельные символы по краям).
    После получения файла вы можете проверить результат, обратившись к полю text.
    Если результат работы скрипта не принимается, проверьте поле url на правильность.
    Для подсчёта количества строк разбейте текст с помощью метода splitlines.
    В поле ответа введите одно число или отправьте файл, содержащий одно число.
    """

    with open('Dataset_1.txt','r') as file:
        text = file.read().strip()

        r = re.get(text)
        if r.status_code == 200:
            pass
        else:
            print('Ошибка',r)

    print(len(r.text.splitlines()))

def get_reqest():
    """
    Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
    Первое слово в тексте последнего файла: "We".
    Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.
    Все файлы располагаются в каталоге по адресу:
    https://stepic.org/media/attachments/course67/3.6.3/

    Загрузите содержимое последнего файла из набора, как ответ на это задание.
    """
    url = "https://stepic.org/media/attachments/course67/3.6.3/"
    open_file = "Dataset_2.txt"
    with open(open_file,'r') as file:
        text = file.read().strip()

    print(f'Файл {open_file} содержит:',text, sep='\n')
    take_txt_file = text.split('/')[-1]
    r = re.get(url+take_txt_file)
    take_text = r.text
    c = 0
    while take_text.startswith('We')==False:
        r = re.get(url+take_text)
        c+=1
        print(f'Файл № {c} Содержимое фала {take_text} : {r.text}')
        take_text = r.text


# 3.7 Задачи по материалам недели

def footbal_result_format():
    """
    Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.
    За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

    Формат ввода следующий:
    В первой строке указано целое число
    n — количество завершенных игр.
    После этого идет n строк, в которых записаны результаты игры в следующем формате:

    Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой

    Вывод программы необходимо оформить следующим образом:
    Команда:Всего_игр Побед Ничьих Поражений Всего_очков

    Конкретный пример ввода-вывода приведён ниже.
    Порядок вывода команд произвольный.
    Sample Input:
    3
    Спартак;9;Зенит;10
    Локомотив;12;Зенит;3
    Спартак;8;Локомотив;15
    Sample Output:

    Спартак:2 0 0 2 0
    Зенит:2 1 0 1 3
    Локомотив:2 2 0 0 6

    """
    # Команда:Всего_игр Побед Ничьих Поражений Всего_очков

    d = {}
    for game in range(int(input())):
        c1, r1, c2, r2 = input().split(';')
        r1, r2 = int(r1), int(r2)
        r1, r2 = 3 * (r1 > r2) + (r1 == r2), 3 * (r2 > r1) + (r1 == r2)
        r1, r2 = [[1, int(_ == 3), int(_ == 1), int(_ == 0), _] for _ in (r1, r2)]
        d[c1] = [sum(_) for _ in zip(d.get(c1, [0, 0, 0, 0, 0]), r1)]
        d[c2] = [sum(_) for _ in zip(d.get(c2, [0, 0, 0, 0, 0]), r2)]
    [print(k, ' '.join(map(str, v)), sep=':') for k, v in d.items()]

    """
        a = [input().split(';') for i in range(int(input()))]
        b = {i: [] for i in set([i[0] for i in a]) | set([i[2] for i in a])}
        for i in a:
            b[i[0]].append(1 if i[1] == i[3] else 3 if i[1] > i[3] else 0)
            b[i[2]].append(1 if i[1] == i[3] else 3 if i[1] < i[3] else 0)
        for i in b: print(f'{i}:{len(b[i])} {b[i].count(3)} {b[i].count(1)} {b[i].count(0)} {sum(b[i])}')
    """

    """
    d = dict()
    countOfgames = games
    matchResult = []

    def update_teams(d,team):
        if team not in d:
            d[team] = [0,0,0,0,0]

    def update_score(d, result):
        if (result[1] > result[3]):
            d[result[0]][0] += 1
            d[result[0]][1] += 1
            d[result[0]][4] += 3
            d[result[2]][0] += 1
            d[result[2]][3] += 1
        elif (result[1] == result[3]):
            d[result[0]][0] += 1
            d[result[0]][2] += 1
            d[result[0]][4] += 1
            d[result[2]][0] += 1
            d[result[2]][2] += 1
            d[result[2]][4] += 1
        else:
            d[result[2]][0] += 1
            d[result[2]][1] += 1
            d[result[2]][4] += 3
            d[result[0]][0] += 1
            d[result[0]][3] += 1

    for i in range(countOfgames):
        matchResult.append(input().split(';'))
        update_teams(d,matchResult[i][0])
        update_teams(d,matchResult[i][2])
        update_score(d,matchResult[i])

    for key, values in d.items():
        print(f'{key}:{values[0]} {values[1]} {values[2]} {values[3]} {values[4]}')"""

    """
    lst = list(args)
    matches = lst.pop(0)

    band_names_lst =[]
    score_dic = {}

    win_score = 0
    draw_score = 0
    loose_score = 0
    result_points_score = 0
    band_matches = 0

    for i in lst:
        band_names_lst.append(str(i).split(';')[0])
        band_names_lst.append(str(i).split(';')[2])
    band_names_lst = list(set(band_names_lst))

    # for band in band_names_lst:
    #     win_score = 0
    #     band_matches = 0
    #     draw_score = 0
    #     loose_score = 0
    #     result_points_score = 0
    #     for i in range(len(lst)):
    #         # подсчет сыгранных матчей командой
    #         if str(lst[i]).split(';')[0] == band or str(lst[i]).split(';')[2] == band:
    #             band_matches += 1
    #
    #         # подсчет побед комманды
    #         if (str(lst[i]).split(';')[0] == band and int(str(lst[i]).split(';')[1] ) > int(str(lst[i]).split(';')[3])) \
    #             or (str(lst[i]).split(';')[2] == band and int(str(lst[i]).split(';')[3] ) > int(str(lst[i]).split(';')[1])):
    #             win_score+=1
    #
    #         # подсчет игр в нечью
    #         elif (str(lst[i]).split(';')[0] == band and int(str(lst[i]).split(';')[1]) == int(str(lst[i]).split(';')[3])) \
    #                 or (str(lst[i]).split(';')[2] == band and int(str(lst[i]).split(';')[3])== int(str(lst[i]).split(';')[1])):
    #             draw_score += 1
    #
    #         # подсчет поражений команды
    #         elif (str(lst[i]).split(';')[0] == band and int(str(lst[i]).split(';')[1] ) < int(str(lst[i]).split(';')[3])) \
    #                 or (str(lst[i]).split(';')[2] == band and int(str(lst[i]).split(';')[3]) < int(str(lst[i]).split(';')[1])):
    #             loose_score += 1
    #
    #         result_points_score = win_score*3+draw_score
    #
    #     print(f'{band}:{band_matches} {win_score} {draw_score} {loose_score} {result_points_score}')

    # for band in band_names_lst:
    #     win_score = 0
    #     band_matches = 0
    #     draw_score = 0
    #     loose_score = 0
    #     result_points_score = 0
    #     for i in range(len(lst)):
    #         # подсчет сыгранных матчей командой
    #         if str(lst[i]).split(';')[0] == band or str(lst[i]).split(';')[2] == band:
    #             band_matches += 1
    #         # подсчет побед комманды
    #         if (str(lst[i]).split(';')[0] == band and str(lst[i]).split(';')[1] < str(lst[i]).split(';')[3]) \
    #             or (str(lst[i]).split(';')[2] == band and str(lst[i]).split(';')[3] < str(lst[i]).split(';')[1]):
    #             win_score+=1
    #         # подсчет игр в нечью
    #         if (str(lst[i]).split(';')[0] == band and str(lst[i]).split(';')[1] == str(lst[i]).split(';')[3]) \
    #                 or (str(lst[i]).split(';')[2] == band and str(lst[i]).split(';')[3] == str(lst[i]).split(';')[1]):
    #             draw_score += 1
    #         # подсчет поражений команды
    #         if (str(lst[i]).split(';')[0] == band and str(lst[i]).split(';')[1] > str(lst[i]).split(';')[3]) \
    #                 or (str(lst[i]).split(';')[2] == band and str(lst[i]).split(';')[3] > str(lst[i]).split(';')[1]):
    #             loose_score += 1
    #
    #         result_points_score = win_score*3+draw_score
    #
    #     print(f'{band}:{band_matches} {win_score} {draw_score} {loose_score} {result_points_score}')
"""

    # print(str(lst[0]).split(';')[0],str(lst[0]).split(';')[1],':',str(lst[0]).split(';')[2],str(lst[0]).split(';')[3])
    # print(str(lst[1]).split(';')[0],str(lst[1]).split(';')[1],':',str(lst[1]).split(';')[2],str(lst[1]).split(';')[3])
    # print(str(lst[2]).split(';')[0],str(lst[2]).split(';')[1],':',str(lst[2]).split(';')[2],str(lst[2]).split(';')[3])

    # # footbal_result_format(3,'Спартак;9;Зенит;10','Локомотив;12;Зенит;3','Спартак;8;Локомотив;15')
    #     # print()
    # footbal_result_format()

def encrypt(symbs,key,str_for_encrypt,str_for_decrypt):
    """
    В какой-то момент в Институте биоинформатики биологи перестали понимать, что говорят информатики: они говорили каким-то странным набором звуков.
    В какой-то момент один из биологов раскрыл секрет информатиков: они использовали при общении подстановочный шифр, т.е. заменяли каждый символ исходного сообщения на соответствующий ему другой символ. Биологи раздобыли ключ к шифру и теперь нуждаются в помощи:
    Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки. Программа принимает на вход две строки одинаковой длины, на первой строке записаны символы исходного алфавита, на второй строке — символы конечного алфавита, после чего идёт строка, которую нужно зашифровать переданным ключом, и ещё одна строка, которую нужно расшифровать.

    Пусть, например, на вход программе передано:
    abcd
    *d%#
    abacabadaba
    #*%*d*%

    Это значит, что символ a исходного сообщения заменяется на символ * в шифре, b заменяется на d, c — на % и d — на #.
    Нужно зашифровать строку abacabadaba и расшифровать строку #*%*d*% с помощью этого шифра. Получаем следующие строки, которые и передаём на вывод программы:
    *d*%*d*#*d*
    dacabac


    """

    # print('Original string:',str_for_encrypt)
    translation = str_for_encrypt.maketrans(symbs,key)
    encrypted = str_for_encrypt.translate(translation)
    # print('Translated string:',str_for_encrypt.translate(translation))
    # print()

    translation = str_for_decrypt.maketrans(key,symbs)
    decrypted = str_for_decrypt.translate(translation)
    # print('Encrypted stiong:', str_for_decrypt)
    # print('Decrypted string:',str_for_decrypt.translate(translation))

    return f'{encrypted} \n{decrypted}'

    # print(encrypt('abcd','*d%#','abacabadaba','#*%*d*%'))
    # print(encrypt(str(input()),str(input()),str(input()),str(input())))

def orpho_check(chk_words,strings_for_check):
    """
    Простейшая система проверки орфографии может быть основана на использовании списка известных слов.
    Если введённое слово не найдено в этом списке, оно помечается как "ошибка".
    Попробуем написать подобную систему.
    На вход программе первой строкой передаётся количество d известных нам слов,
    после чего на d строках указываются эти слова. Затем передаётся количество
    l строк текста для проверки, после чего l строк текста.
    Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта регистра.
    """
    words = ' '.join(strings_for_check).split()
    # print(words)
    res = []
    for i in range(len(words)):
        if words[i] not in chk_words:
            res.append(words[i])
    print(*set(res),sep='\n')

        # chk_words = [str(input()).lower() for i in range(int(input()))]
        # strings_for_check = [str(input()).lower() for i in range(int(input()))]
        # orpho_check(chk_words,strings_for_check)


        # chk_words = ['champions','we','are','Stepik']
        # strings_for_check = ['We are the champignons','We Are The Champions','Stepic']

