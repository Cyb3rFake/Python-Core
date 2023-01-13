"""Шифр Цезаря"""

"""
- работа с заглавными буквами
"""

symbol_list = '_-!@#$%^&*,.[]{} '

eng_alphabet = 'abcdefghijklmnopqrstuvwxyz'
# eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
# rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
e_text = "" # зашифрованный текст
de_text = "" # расшифрованный текст

def language_check(txt):
    "проверка языка ввода"
    txt = txt.lower()
    for i in txt:
        if i in eng_alphabet:
            return "eng"
        else:
            return "rus"



def encrypt(text = 'тест!', k = 1, lng = 'rus'):
    "шифрование текста со сдвигом"
    global e_text
    res = []
    text = text.lower()

    if lng == 'rus': # для текста в кирилице

        for i in text:
            if i in rus_alphabet:
                s = rus_alphabet.index(i)
                if (s + k)>len(rus_alphabet)-1:
                    res.append((rus_alphabet[(s+k)-len(rus_alphabet)]))
                else:
                    res.append(rus_alphabet[s + k])
            elif i in symbol_list:
                res.append(i)
        e_text = ''.join(res)
        return e_text

    else:   # для текста в латинице
        for i in text:
            if i in eng_alphabet:
                s = eng_alphabet.index(i)
                if (s + k) > len(eng_alphabet) - 1:
                    res.append((eng_alphabet[(s + k) - len(eng_alphabet)]))
                else:
                    res.append(eng_alphabet[s + k])
            elif i in symbol_list:
                res.append(i)
        e_text = ''.join(res)
        return e_text


def decrypt(text = 'сдрс!', k = 1, lng = 'rus'):
    "расшифровка текста"
    global de_text
    res = []

    if lng == 'rus':

        for i in text:
            if i in rus_alphabet:
                s = rus_alphabet.index(i)
                if (s + k)>len(rus_alphabet)-1:
                    # print((s + k),len(rus_alphabet)-1)
                    # d = (rus_alphabet[(s+k)-len(rus_alphabet)-1])
                    res.append(rus_alphabet[(s+k)-len(rus_alphabet)])
                else:
                    res.append(rus_alphabet[s + k])
            elif i in symbol_list:
                res.append(i)
        res = ''.join(res)
        return res

    else:
        for i in text:
            if i in eng_alphabet:
                s = eng_alphabet.index(i)
                if (s + k) > len(eng_alphabet) - 1:
                    # print((s + k),len(rus_alphabet)-1)
                    # d = (rus_alphabet[(s+k)-len(rus_alphabet)-1])
                    res.append(eng_alphabet[(s + k) - len(eng_alphabet)])
                else:
                    res.append(eng_alphabet[s + k])
            elif i in symbol_list:
                res.append(i)
        res = ''.join(res)
        return res


def main():
    global txt
    key_ = 0
    while True:
        try:

            txt = input("Введите текст для шифровки: ")
            key_ = int(input("Введите сдвиг(число от 0 до 32): "))

        except Exception:
            print('Ошибка')
        else:
            print('Принято')
            break

    res = (encrypt(text=txt,k=key_,lng=language_check(txt)))
    print(res)


if __name__ == '__main__':
    # main()
    pass

    # for i in range(1,26):
        # print('Сдвиг',i, ' = ', decrypt('hawnj pk swhg xabkna ukq nqj',i, 'eng'))
        # print('Сдвиг',i, ' = ', decrypt('яшбэьч ауюнуа ряу, фущон ряу тьяаоак.',i, 'rus'))
        # print('Сдвиг',i, ' = ', decrypt('sgd fqzrr hr zkvzxr fqddmdq nm sgd nsgdq rhcd ne sgd edmbd.',i, 'eng'))


    # print(encrypt(text='To be, or not to be, that is the question!', k=17, lng='eng'))
