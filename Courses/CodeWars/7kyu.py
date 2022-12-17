""""
Дан треугольник последовательных нечетных чисел:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
Вычислите сумму чисел в n -й строке этого треугольника (начиная с индекса 1), например: ( Ввод --> Вывод )
1 -->  1
2 --> 3 + 5 = 8
"""
def row_sum_odd_numbers(n):
    return n**3
#sum(range(n*(n-1)+1, n*(n+1), 2))

"""
Сможете ли вы найти иголку в стоге сена?
Напишите функцию findNeedle(), которая принимает array полный мусор, но содержит один "needle"
После того, как ваша функция найдет иглу, она должна вернуть сообщение (в виде строки), в котором говорится:
"found the needle at position "плюс index он нашел иглу, так что:

Пример (ввод --> вывод)

["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"] --> "found the needle at position 5" 
Примечание. В COBOL он должен возвращать "found the needle at position 6"
"""

def find_needle(haystack):
    find = 'needle'
    return f'found the needle at position {haystack.index(find)}'
# 	return 'found the needle at position {}'.format(haystack.index('needle'))


"""
Вам будет предоставлен массив a и значение x. Все, что вам нужно сделать, это проверить, содержит ли предоставленный массив значение.
Массив может содержать числа или строки. Х может быть любым.
Возврат, trueесли массив содержит значение, fals eесли нет.

"""
def check(seq, elem):
    return True if elem in seq else False # return 'True' if elem in seq else 'False'

"""
Учитывая набор чисел, верните добавку, обратную каждому из них. Каждое положительное становится отрицательным, а отрицательное становится положительным.

invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
invert([]) == []
Можно предположить, что все значения являются целыми числами. Не изменяйте входной массив/список.

"""
def invert(lst):
    return [i *(-1) for i in lst] # return list(map(lambda x: -x, lst)); # return [-x for x in lst]

"""
Возьмите 2 строки s1и s2включите только буквы от aдо z. Возвращает новую отсортированную строку, максимально длинную, содержащую различные буквы (каждая из которых взята только один раз) из s1 или s2.

Примеры:
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
"""

def longest(a1, a2):
    return ''.join(sorted(set(a1+a2)))

"""
Учитывая массив единиц и нулей, преобразуйте эквивалентное двоичное значение в целое число.

Например: [0, 0, 0, 1]рассматривается как 0001двоичное представление 1.

Примеры:

Testing: [0, 0, 0, 1] ==> 1
Testing: [0, 0, 1, 0] ==> 2
Testing: [0, 1, 0, 1] ==> 5
Testing: [1, 0, 0, 1] ==> 9
Testing: [0, 0, 1, 0] ==> 2
Testing: [0, 1, 1, 0] ==> 6
Testing: [1, 1, 1, 1] ==> 15
Testing: [1, 0, 1, 1] ==> 11
Однако массивы могут иметь разную длину, а не только 4.
"""
import unittest as test
def binary_array_to_number(arr):
    return int(''.join(str(i) for i in arr),2)


"""
Проверьте, содержит ли строка одинаковое количество «x» и «o». 
Метод должен возвращать логическое значение и не учитывать регистр. 
Строка может содержать любой символ.

Примеры ввода/вывода:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false

"""
def XO(text):
    co = text.lower().count('o')
    cx = text.lower().count('x')
    if text == '':
        return True
    if co!=cx or cx == 0:
        return False
    else:
        return True
# return s.lower().count('x') == s.lower().count('o')

# x = lambda a,b:a is b
# print(x(100000000,100000000))

"""
На этот раз ни истории, ни теории. В приведенных ниже примерах показано, как написать функцию accum:

Примеры:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"

"""
def accum(s):
    a=""
    for i,elt in enumerate(s):
        a = a+"-"+elt.upper()
        for _ in range(i):
            a = a+elt.lower()
    # return a[1:]
    # return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))


x = 'asdf v vaer 34 25 22'
print(x.replace(' ',''))








