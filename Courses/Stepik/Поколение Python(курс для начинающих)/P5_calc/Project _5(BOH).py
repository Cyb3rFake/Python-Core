"""Binary, Octal, Hex"""

def binary(digit):
    rev_digit = digit[::-1]
    res = 0
    for i in range(len(digit)):
        # res += int(digit[i]) * 2 ** len(digit)-i
        # print(int(rev_digit[i]) * 2 ** i,'+', sep='\n')
        res += int(rev_digit[i]) * 2 ** i
    print(res)

def Octal(digit = '2AF'):
    dict_list = [i for i in range(10)]

    dic_1 = list('ABCDEF')
    dic_2 = ['15', '16', '17', '18', '19']
    dic_3 = dict(zip(dic_1, dic_2))

    res = 0

    # for i in reversed(range(len(digit))):
    for i in range(len(digit)):
        if digit[i] in dic_1:
            print(digit[i])
            # print(dic_3.get(digit[i]))

Octal('2AF')

dic_1 = list('ABCDEF')
dic_2 = ['15','16','17','18','19','20']
dic_3 = dict(zip(dic_1,dic_2))
print(ord('F')-55)