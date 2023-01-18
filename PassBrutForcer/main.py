"""Работает с zip, алгоритмом ZipCrypto, c AES-254 не передает пароль"""


import itertools
from string import digits, punctuation,ascii_letters
import zipfile, glob
# symbol = digits + punctuation + ascii_letters
# print(symbol)

def brute_exel_doc():
    print("test")
    try:
        password_leght = input('Введите длину пароля через "-": ')
        password_leght = [int(i) for i in password_leght.split('-')]
        print(password_leght)
    except :
        print('чет не то')

    print(" Если пароль содержит только цифры, введите: 1\n",
          "Если пароль содержит только буквы, введите: 2\n",
          "Если пароль содержит только цифры и буквы, введите: 3\n",
          "Если пароль содержит цифры буквы и символы, введите: 4")

    while True:
        try:
            choice = int(input(": "))
            if choice == 1:
                possible_symbols = digits
            elif choice == 2:
                possible_symbols = ascii_letters
            elif choice == 3:
                possible_symbols = digits + ascii_letters
            elif choice == 4:
                possible_symbols = digits + ascii_letters + punctuation
            print("Выбранны следующие символы:\n",possible_symbols)
            break
        except:
            print('Не корректный ввод! Введите чило от 1 до 4')
    c = 0
    chk_b = []
    chk = []
    с = 0
    for pass_leght in range(password_leght[0],password_leght[1]+1):
        for password in itertools.product(possible_symbols,repeat=pass_leght):
            password = ''.join(password)
            # chk.append(password)
            # chk_b.append(bin(int(password)).lstrip('-0b'))

            # for i in range(len(chk)):
            #     print(chk[i],'=',chk_b[i])
            c+=1
            try:
                with zipfile.ZipFile('tre.zip') as zf:
                    zf.extractall('D:\\PycharmProjects\\Python-Core\\PassBrutForcer\\',pwd=str.encode(str(password)))
                    print(password)
            except:
                # print(c)
                print(password)
                pass


def main():
    print(brute_exel_doc())
    # print(bin(10).lstrip('-0b'))

if __name__ == '__main__':

    main()