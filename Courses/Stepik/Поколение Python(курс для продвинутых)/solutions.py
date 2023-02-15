import math

"""2.0 Повторяем основы"""


# 2.1 Часть 1

def na_easy():
    """
    На easy
    На вход программе подаются два целых числа a и b. Напишите программу, которая выводит:
    •	сумму чисел a и b;
    •	разность чисел a и b;
    •	произведение чисел a и b;
    •	частное чисел a и b;
    •	целую часть от деления числа a на b;
    •	остаток от деления числа a на b;
    •	корень квадратный из суммы их 1010-х степеней: 10+10a10+b10.
    """

    a, b = int(input()), int(input())
    print(a + b, a - b, a * b, a / b, a // b, a % b, ((a ** 10) + (b ** 10)) ** 0.5, sep='\n')


def body_mass_index():
    """Напишите программу для вычисления и оценки индекса массы тела (ИМТ) человека.
    ИМТ показывает весит человек больше или меньше нормы для своего роста."""
    mass, hight = float(input()), float(input())
    if (mass / hight ** 2) < 18.5:
        print('Недостаточная масса')
    elif mass / hight ** 2 > 25:
        print('Избыточная масса')
    else:
        print('Оптимальная масса')


def string_price():
    # Дана строка текста. Напишите программу для подсчета стоимости строки, исходя из того, что один любой символ(в том числе пробел) стоит 60 копеек.\
    # Ответ дайте в рублях и копейках в соответствии с примерами.
    # put your python code here

    txt = len(input())
    # txt = 'Я собираюсь сделать ему предложение, от которого он не сможет отказаться.'
    print(int(txt * 0.6), 'р.', math.ceil((txt * 0.6 - int(txt * 0.6)) * 100), 'коп.')


def words_count():
    """Количество слов
    Дана строка, состоящая из слов, разделенных пробелами.
    Напишите программу, которая подсчитывает количество слов в этой строке.
    """
    print((len(input().split())))


def zodiak():
    """Напишите программу, которая считывает год и отображает название связанного с ним животного.
    Ваша программа должна корректно работать с любым годом, не только теми, что перечислены в таблице."""

    ch_year_dic = [
        'Обезьяна',
        'Петух',
        'Собака',
        'Свинья',
        'Крыса',
        'Бык',
        'Тигр',
        'Заяц',
        'Дракон',
        'Змея',
        'Лошадь',
        'Овца', ]
    print(ch_year_dic[int(input()) % 12])


def num_reverse():
    """
    Переворот числа
    Дано пятизначное или шестизначное натуральное число. Напишите программу,
    которая изменит порядок его последних пяти цифр на обратный.

    Формат входных данных
    На вход программе подается одно натуральное пятизначное или шестизначное число.

    Формат выходных данных
    Программа должна вывести число, которое получится в результате разворота, указанного в условии задачи.
    Число нужно выводить без незначащих нулей.
    """
    n1 = input()

    if len(n1) == 5:
        print(int(n1[::-1]))
    else:
        n2 = n1[1::]
        n3 = n1[0]
        print(int(n3 + n2[::-1]))


def standard_american_convention(n):
    """
    Standard American Convention
    На вход программе подаётся натуральное число. Напишите программу,
    которая вставляет в заданное число запятые в соответствии со стандартным американским соглашением о запятых в больших числах.
    Формат входных данных
    На вход программе подаётся натуральное число
    Формат выходных данных
    Программа должна вывести число с запятыми в соответствии с условием задачи.

    :param n:
    :return:
    """
    r = []
    c = 0
    for i in range(1, len(n) + 1):
        r.append(n[0 - i])
        # print(n[0-i], end='')
        c += 1
        if c % 3 == 0:
            r.append(',')
    # print(',', end='')
    r = ''.join(r)
    r = r[::-1]
    if r[0] == ',':
        print(r[1::])
    else:
        print(r)


def j_f():
    """
    n человек, пронумерованных числами от 1 до n, стоят в кругу. Они начинают считаться, каждый
    k-й по счету человек выбывает из круга, после чего счет продолжается со следующего за ним человека.
    Напишите программу, определяющую номер человека, который останется в кругу последним.

    Формат входных данных
    На вход программе подаются два числа
    n и k, записанные на отдельных строках.

    Формат выходных данных
    Программа должна вывести одно число – номер человека, который останется в кругу последним.

    """
    #
    # n, k = int(input()), int(input())
    # s = [i for i in range(1, n + 1)]
    # while len(s) > 1:
    #     for q in range(0, k - 1):
    #         s.append(s[q])
    #     del s[:k]
    # print(*s)

    n, k = int(input()), int(input())
    res = 0
    for i in range(1, n + 1):
        res = (res + k) % i

    print(res + 1)


# 2.2 Часть 2

def coordinate_quarters(str_num):
    """
    Дан набор точек на координатной плоскости. Необходимо подсчитать и вывести количество точек,
    лежащих в каждой координатной четверти.

    Формат выходных данных
    Программа должна вывести количество точек, лежащих в каждой координатной четверти, как в примерах.
    Примечание. Учтите, что точки, лежащие на осях координат, не принято относить к какой-либо координатной четверти.

    """

    c_lst = []
    for i in range(str_num):
        c_lst.append(list(map(int, input().split())))
    # print(c_lst)
    quarters = ['Первая четверть: ', 'Вторая четверть: ', 'Третья четверть: ', 'Четвертая четверть: ']
    for q in quarters:
        r = 0
        res = ''
        for c in c_lst:
            x, y = c[0], c[1]
            if q == quarters[0] and (x > 0 and y > 0):
                r += 1
            elif q == quarters[1] and (x < 0 < y):
                r += 1
            elif q == quarters[2] and (x < 0 and y < 0):
                r += 1
            elif q == quarters[3] and (x > 0 > y):
                r += 1
            res = q + str(r)
        print(res)


def biggest_then_previous():
    """
    Больше предыдущего
    На вход программе подается строка текста из натуральных чисел. Из неё формируется список чисел.
    Напишите программу подсчета количества чисел, которые больше предшествующего им в этом списке числа,
    то есть, стоят вслед за меньшим числом.

    Формат входных данных
    На вход программе подается строка текста из разделенных пробелами натуральных чисел.

    Формат выходных данных
    Программа должна вывести одно число – количество элементов списка, больших предыдущего.

    """
    lst = list(map(int, input().split()))
    c = 0
    for i in range(len(lst) - 1):
        if lst[i] < lst[i + 1]:
            c += 1
    print(c)


def back_forward_change():
    """
    Назад, вперёд и наоборот
    На вход программе подается строка текста из натуральных чисел. Из элементов строки формируется список чисел.
    Напишите программу, которая меняет местами соседние элементы списка (a[0] c a[1], a[2] c a[3] и т.д.).
    Если в списке нечетное количество элементов, то последний остается на своем месте.

    Формат входных данных
    На вход программе подается строка текста, содержащая натуральные числа, разделенные пробелами.

    Формат выходных данных
    Программа должна вывести измененный список, разделяя его элементы одним пробелом.

    """
    # lst = input().split()
    lst = '1 2 3 4 5'.split()
    lst = '2 3 2 4'.split()
    res = []
    for i in range(0, len(lst) - 1, 2):
        print(lst[i + 1], lst[i], sep=' ', end=' ')
        # res.append([lst[i+1],lst[i]])
    if len(lst) % 2 != 0:
        print(lst[-1])


def shift_in_development():
    """
    Сдвиг в развитии
    На вход программе подается строка текста из натуральных чисел. Из элементов строки формируется список чисел.
    Напишите программу циклического сдвига элементов списка направо, когда последний элемент становится первым,
    а остальные сдвигаются на одну позицию вперед, в сторону увеличения индексов.

    Формат входных данных
    На вход программе подается строка текста из разделенных пробелами натуральных чисел.

    Формат выходных данных
    Программа должна вывести элементы измененного списка с циклическим сдвигом, разделяя его элементы одним пробелом.
    """

    lst = '5 4 3 2 1'.split()
    src_len = len(lst)

    res = lst.pop(src_len - 1)
    lst.insert(0, res)
    print(*lst)


def different_elements():
    """
    Различные элементы
    На вход программе подается строка текста, содержащая натуральные числа, расположенные по неубыванию. Из строки формируется список чисел. Напишите программу для подсчета количества разных элементов в списке.

    Формат входных данных
    На вход программе подается строка текста, содержащая натуральные числа, разделенные символом пробела, расположенные по неубыванию.

    Формат выходных данных
    Программа должна вывести одно число – количество различных элементов списка.

    Примечание. Задачу можно решить без множеств.
    """
    lst = '2 2 5 5 5 5 8 10 10'.split()
    print(len(set(lst)))


def multiplication():
    """
    Произведение чисел
    Напишите программу для определения, является ли число произведением двух чисел из данного набора, выводящую результат в
    виде ответа «ДА» или «НЕТ».

    Формат входных данных
    В первой строке подаётся число (0<n<1000)
    n(0<n<1000) – количество чисел в наборе. В последующих n строках вводятся целые числа,
    составляющие набор (могут повторяться).
    Затем следует целое число, которое является или не является произведением двух каких-то чисел из набора.

    Формат выходных данных
    Программа должна вывести «ДА» или «НЕТ» в соответствии с условием задачи.

    Примечание 1. Само на себя число из набора умножиться не может, другими словами,
    два множителя должны иметь разные индексы в наборе.

    Примечание 2. Для решения задачи используйте вложенные циклы.

    """
    flag = 'НЕТ'
    src_lst = [input() for i in range(int(input()))]
    if len(src_lst) <= 1:
        return print(flag)

    mult_d = int(input())

    def find_index(num,lst):
        res = []
        for i in range(0,len(lst)):
            if num == lst[i]:
                res.append(i)
        return res

    for i in range(len(src_lst)):
        for j in range(len(src_lst)):
            if i == j:
                # print(f'{int(src_lst[i])}*{int(src_lst[j])}={int(src_lst[i]) * int(src_lst[j])} ====>>> ПРОПУСКАЕМ')
                continue
            # print(f'{int(src_lst[i])}*{int(src_lst[j])}={int(src_lst[i]) * int(src_lst[j])}')
            if int(src_lst[i])*int(src_lst[j]) == mult_d:
                print('ДА')
                return
    print(flag)


def stone_scicors_paper(n1,n2):
    """
     Камень, ножницы, бумага
    Тимур и Руслан пытаются разделить фронт работы по курсу "Python для профессионалов".
    Для этого они решили сыграть в камень, ножницы и бумагу. Помогите ребятам бросить честный жребий и определить,
    кто будет делать очередной модуль нового курса.

    Формат входных данных
    На вход программе подаются две строки текста, содержащие слова "камень", "ножницы" или "бумага".
    На первой строке записан выбор Тимура, на второй – выбор Руслана.

    Формат выходных данных
    Программа должна вывести результат жеребьёвки, то есть кто победит: Тимур, Руслан или же они сыграют вничью.

    Примечание. Правила игры стандартные: камень побеждает ножницы, но проигрывает бумаге, а ножницы побеждают бумагу.
    """

    winers_name =['Тимур','Руслан']
    # n1,n2 = input(),input()
    var_list = [
        ['камень ножницы','бумага камень','ножницы бумага'],
        ['камень камень','ножницы ножницы','бумага бумага']
                ]
    combo = ' '.join([n1,n2])

    if combo in var_list[1]:
        print('Draw!')
        return

    # combo_rev = ' '.join([n1,n2][::-1])
    if combo in var_list[0]:
        print('T')
    else:
        print('R')

    # stone_scicors_paper('камень','бумага')
    # stone_scicors_paper('камень','ножницы')
    # stone_scicors_paper('ножницы','камень')
    # stone_scicors_paper('бумага','камень')
    #
    # stone_scicors_paper('ножницы','ножницы')
    # stone_scicors_paper('камень','камень')
    # stone_scicors_paper('бумага','бумага')


def stone_scicors_paper_lizard_spok(n1,n2):
    """
    Камень, ножницы, бумага, ящерица, Спок 🌶️
    Проиграв
    10 раз Тимуру, Руслан понял, что так дело дальше не пойдет, и решил усложнить игру.
    Теперь Тимур и Руслан играют в игру Камень, ножницы, бумага, ящерица, Спок. Помогите ребятам вновь бросить честный
    жребий и определить, кто будет делать следующий модуль в новом курсе.

    Формат входных данных
    На вход программе подаются две строки текста, содержащие по одному слову из перечня "камень", "ножницы", "бумага",
    "ящерица" или "Спок". На первой строке записан выбор Тимура, на второй – выбор Руслана.

    Формат выходных данных
    Программа должна вывести результат жеребьёвки: кто победил - Тимур или Руслан, или они сыграли вничью.

    Примечание. Правила игры стандартные: ножницы режут бумагу. Бумага заворачивает камень. Камень давит ящерицу,
    а ящерица травит Спока, в то время как Спок ломает ножницы, которые, в свою очередь, отрезают голову ящерице,
    которая ест бумагу, на которой улики против Спока. Спок испаряет камень, а камень, разумеется, затупляет ножницы.
    """

    win_combos = ['камень ножницы','камень ящерица',
                'ножницы бумага','ножницы ящерица',
                'бумага камень','бумага Спок',
                'Спок камень','Спок ножницы',
                'ящерица Спок','ящерица бумага']

    if n1 == n2 :
        print('ничья')
        return

    combo = ' '.join([n1,n2])

    if combo in win_combos:
        print('Тимур')
    else:
        print('Руслан')
    # stone_scicors_paper_lizard_spok(input(),input())


def heads_and_tails(string):
    """
    Дана строка текста, состоящая из букв русского алфавита "О" и "Р". Буква "О" – соответствует выпадению Орла,
    а буква "Р" – соответствует выпадению Решки. Напишите программу, которая подсчитывает наибольшее количество подряд
    выпавших Решек.

    Формат входных данных
    На вход программе подается строка текста, состоящая из букв русского алфавита "О" и "Р".

    Формат выходных данных
    Программа должна вывести наибольшее количество подряд выпавших Решек.

    Примечание. Если выпавших Решек нет, то необходимо вывести число 0.
    """
    if 'Р' not in string:
        print(0)
        return

    count = 0
    max_count = 0
    last_symb = ''
    if string[-1] == 'Р':
        last_symb = 'О'

    for i in string+last_symb:
        if i == 'Р':
            count+=1
        else:
            if max_count < count:
                max_count = count
            count = 0
    print(max_count)

# Не Выполнено
def flint_valley():
    """
    Кремниевая долина 🌶️🌶️
    Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников.
    Теперь он использует их в качестве серверов "Пегого дудочника". Помогите владельцу фирмы отыскать все
    зараженные холодильники.

    Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр,
    и если в ней присутствует слово "anton" (необязательно рядом стоящие буквы,
    главное наличие последовательности букв), то холодильник заражен и нужно вывести номер холодильника,
    нумерация начинается с единицы

    Формат входных данных
    В первой строке подаётся число n – количество холодильников. В последующих n строках вводятся строки,
    содержащие латинские строчные буквы и цифры, в каждой строке от 5 до 100 символов.

    Формат выходных данных
    Программа должна вывести номера зараженных холодильников через пробел. Если таких холодильников нет,
    ничего выводить не нужно.
    """

    freezer_nums_list = [str(input()) for i in range(int(input()))]

    chk_word = 'anton'
    error_nums = 0


    for num in freezer_nums_list:
        error_nums += 1
        find_num = num
        tmp_word = ''

        for i in 'anton':
            if i in find_num:
                find_num = find_num[find_num.find(i):]
                tmp_word += find_num[0]

            if tmp_word!='a':
                pass

            if tmp_word==chk_word:
                print(error_nums,end=' ')


def roscomnadzor():
    """
    Роскомнадзор запретил букву 'а' 🌶️🌶️

    Необходимо написать программу, реализующую алгоритм написания этой песни.
    Алгоритм выводит в конце предложения следующую в алфавитном порядке букву, если она встречается в строке текста,
    а очередную строку отображает уже без этой буквы.

    Формат входных данных
    На вход программе подается одно слово, записанное строчными русскими буквами без буквы "ё".

    Формат выходных данных
    Программа должна вывести в соответствии с указанным алгоритмом строки, количество которых равно количеству разных
    букв в строке, которая получается путем конкатенации введенного слова и строки "запретил букву".
    """

    who = "роскомнадзор"
    strng = (f'{who} запретил букву').split()
    rus_letters = [chr(i) for i in range(1072, 1104)]
    res = []
    for letter in rus_letters:
        c = 0
        for word in strng:
            if letter in word and c != 1:
                c += 1
                res.append([*strng, letter])
                strng[strng.index(word)] = word.replace(letter, '')
            else:
                strng[strng.index(word)] = word.replace(letter, '')
    # print(*res,sep='\n')

    for string in res:
        for word in string:
            if word == '':
                string.remove(word)
        for word in string:
            if word == '':
                string.remove(word)

    res_1 = []
    for i in range(len(res)):
        res_1.append(' '.join(res[i]))
    print(*res_1, sep='\n')


# 4 Вложенные списки


def list_by_example_1():
    """
    Список по образцу 1
    На вход программе подается число n.
    Напишите программу, которая создает и выводит построчно список, состоящий из
    n списков [[1, 2, ..., n], [1, 2, ..., n], ..., [1, 2, ..., n]].
    """
    n = int(input())
    lst = [i for i in range(1, n + 1)]
    for i in range(n):
        print(lst)


def list_by_example_2():
    """
    Список по образцу 2
    На вход программе подается число n.
    Напишите программу, которая создает
    и выводит построчно вложенный список, состоящий из n списков [[1], [1, 2], [1, 2, 3], ..., [1, 2, ..., n]].

    Формат входных данных
    На вход программе подается натуральное число n.

    Формат выходных данных
    Программа должна вывести построчно указанный вложенный список.

    """
    print(*[[j for j in range(1, i)] for i in range(2, int(input()) + 2)], sep='\n')


def pascal_triange():
    """
    Формат входных данных
    На вход программе подается число n (n≥0).

    Формат выходных данных
    Программа должна вывести указанную строку треугольника Паскаля в виде списка.
    """
    n = int(input())+1
    # n = 100
    res = []
    if n == 0:
        print('[1]')
        return
    for i in range(n):
        row = [1]*(i+1)
        for j in range(1,i):
            row[j] = res[i-1][j-1]+res[i-1][j]
        res.append(row)

    for i in res:
        print(*i)
    # for i in range(n):
    #     print(' '*(n-i),*res[i])


def pascal_triange_2():
    """
    На вход программе подается натуральное число n.
    Напишите программу, которая выводит первые n строк треугольника Паскаля.
    Программа должна вывести первые n строк треугольника Паскаля, каждую на отдельной строке в соответствии с образцом.

    """
    n = int(input())
    # n = 100
    res = []
    if n == 0:
        print('[1]')
        return
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = res[i - 1][j - 1] + res[i - 1][j]
        res.append(row)
    for i in res:
        print(*i)


def packing_doubles():
    """
    На вход программе подается строка текста, содержащая символы. Напишите программу,
    которая упаковывает последовательности одинаковых символов заданной строки в подсписки.
    На вход программе подается строка текста, содержащая символы, отделенные символом пробела.
    Программа должна вывести указанный вложенный список.
    """
    # inc_lst = input().split()

    inc_lst = 'w w w o r l d g g g g r e a t t e c c h e m g g p w w'.split()
    inc_lst = 'a b c d'.split()
    # print(inc_lst[:3])

    l = len(inc_lst)
    res = []
    tmp = 0
    for i in range(1,len(inc_lst)):
        if inc_lst[i]!=inc_lst[i-1]:
            res.append(inc_lst[tmp:i])
            tmp = i
        if i == len(inc_lst)-1 and inc_lst[i]==inc_lst[-1]:
            res.append(inc_lst[-2::])
    print(res)


    #         tmp.append(inc_lst[i])
    #     else:
    #         tmp.append(inc_lst[i-1])
    #         res.append(tmp)
    #         tpm = []
    # print(res)
packing_doubles()

# _________________________

#
# def fact(n):
#     if n == 1:
#         return 1
#     return fact(n - 1) * n

# inp = 5
# row = ''
# last_row = []
# for i in range(0,inp+1):
#     row = [1]*(i+1)
#     for j in range(0,i+1):
#


# print(*[[j for j in range(1,i)] for i in range(2,5)],sep='\n')




# for i in range(1,len(m)+1):
#     if m[i].istitle() == True:
#         lst.append(m[:m.find()])
#

# print(m.rfind('This'))
# m = list(m)
# del m[:3:]
# print(m)