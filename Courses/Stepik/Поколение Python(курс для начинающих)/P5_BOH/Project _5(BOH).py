"""Binary, Octal, Hex"""

def BOH():
    digit = int(input())
    print(bin(digit).split('b')[1])
    print(oct(digit).split('o')[1])
    print(hex(digit).split('x')[1].upper())


def calculator ():
    list_litters = 'ABCDEF'
    list_digit = [10, 11, 12, 13, 14, 15]
    result = 0
    number_systems = int(input('Какая система счисления? Варианты - (2 - двоичная, 8 - восмеричная, 12 - двенадцатеричная, 16 - шестнадцатеричная): '))
    num = input('Ввидите число которое нужно перевести в десятичную систему исчесления: ')[::-1]
    for i in range(len(num)):
        if num[i] in list_litters:
            result += list_digit[list_litters.index(num[i])] * number_systems ** i
            continue
        result += int(num[i]) * number_systems ** i
    print(result)
