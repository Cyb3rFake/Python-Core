"""Шифр Цезаря"""

symbol_list = '!@#$%^&*,.[]{} '
eng_alphabet = 'abcdefghijklmnopqrstuvwxyz'
# eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
# rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
e_text = "" # зашифрованный текст
de_text = "" # расшифрованный текст


def encrypt(text = 'тест!', k = 1):
    global e_text
    res = []
    text = text.lower()
    for i in text:
        if i in rus_alphabet:
            s = rus_alphabet.index(i)
            if (s + k)>len(rus_alphabet)-1:
                print(rus_alphabet[(s+k)-len(rus_alphabet)])
            else:
                res.append(rus_alphabet[s + k])
        elif i in symbol_list:
            res.append(i)
    e_text = ''.join(res)
    return e_text

def decrypt(text = 'сдрс!', k = 1):
    global de_text
    res = []
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
    encrypt(text=txt,k=key_)
    print("Зашифровано:",e_text)
    pass

if __name__ == '__main__':
    main()
