"""Шифр Цезаря"""

symbol_list = '!@#$%^&*,.[]{} '
eng_alphabet = 'abcdefghijklmnopqrstuvwxyz'
# eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
# rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"



def encrypt(text = 'тест!', k = 1):
    res = []
    for i in text:
        if i in rus_alphabet:
            s = rus_alphabet.index(i)
            res.append(rus_alphabet[s - k])
        elif i in symbol_list:
            res.append(i)
    res = ''.join(res)
    return res

print(encrypt(k=1))


def decrypt(text = 'сдрс!', k = 1):
    res = []
    for i in text:
        if i in rus_alphabet:
            s = rus_alphabet.index(i)
            if (s + k)>len(rus_alphabet)-1:
                # print((s + k),len(rus_alphabet)-1)
                d = (rus_alphabet[(s+k)-len(rus_alphabet)-1])
                res.append(rus_alphabet[(s+k)-len(rus_alphabet)])
            else:
                res.append(rus_alphabet[s + k])
        elif i in symbol_list:
            res.append(i)
    res = ''.join(res)
    return res

print(decrypt())


