"""Шифр Цезаря"""

encrypted_text = ''

def encrypt(text,shift):
    key = shift
    dictionary_rus = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    dictionary_eng = "abcdefghijklmnopqrstuvwxyz"
    res = []
    for i in text:
        if i in dictionary_rus:
            s = dictionary_rus.index(i)
            res.append(dictionary_rus[s-key])
        else:
            res.append(' ')
    res = ''.join(res)
    global encrypted_text
    encrypted_text = res
    return res


def decrypt(text,shift):
    res=[]
    key = shift
    dictionary_rus = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    dictionary_eng = "abcdefghijklmnopqrstuvwxyz"
    for i in text:
        if i in dictionary_rus:
            s = dictionary_rus.index(i)
            # print(f'Текущий интедкс буквы {s}\nИндекс буквы со сдвигом {s + key}\nЧисло букв в алфавите {len(dictionary_rus)}')
            if (s+key)>len(dictionary_rus)-1:
                res.append(dictionary_rus[(s+key)-(len(dictionary_rus))])
            else:
                res.append(dictionary_rus[s+key])
        else:
            res.append(' ')
    res = ''.join(res)
    print(res)

# encrypt('жопа хуй', 5)
# decrypt(encrypted_text, 5)

if __name__ == '__main__':
    # a = input('Зашифруем че-нить?(Да/Нет) ')
    # if a != 'д':
    #     print('пакет')
    #     exit()
    # txt = input('Введите текст для шифрования: ')
    # key = input('Введите число сдвига шифра: ')

    # print('Вот че вышло:',encrypt('лиса колбаса', 1))
    pass

print(*dir(list()),sep='\n')
