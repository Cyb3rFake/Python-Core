"Генератор случайных паролей"

"""
1) Реализовать проверку вводимого значения длинны пароля на недопустимые значения(отрицательные числа, пустое поле)
2) Реализовать ограничение на длинну пароля
"""

import random

if __name__ == '__main__':

    digits = '0123456789'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    punctuation = '!#$%&*+-=?@^_.'
    chars = []

    lst_yes = ['da','yes','нуы','да','+','y','н']

    def ask_pass_params():
        """
        Количество паролей для генерации;
        Длину одного пароля;
        Включать ли цифры 0123456789?
        Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?
        Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?
        Включать ли символы !#$%&*+-=?@^_?
        Исключать ли неоднозначные символы il1Lo0O?
        """
        lst_questions = ['Длина одного пароля: ',
                         'Включать ли цифры 0123456789 (y/n)? ' ,
                         'Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz (y/n)? ' ,
                         'Включать ли символы и знаки припенания !#$%&*+-=?@^_. (y/n)? ' ,
                         'Исключать ли неоднозначные символы il1Lo0O (y/n)? ' ]

        lst_answers = [input(lst_questions[i]) for i in range(len(lst_questions))]
        # тестовые данные
        # lst_answers = ['10','+','+','+','+','+']
        # lst_answers = ['10','+','-','-','-','-']
        # lst_answers = ['10','+','-','-','-','-']
        return lst_answers



    def generate_password(answ):
        "генератор одного пароля по результатам ответов"
        password = ''
        for i in range(1,int(answ[0])):
            if answ[1] in lst_yes and len(password)<int(answ[0]):
                password+= digits[random.randrange(0,len(digits))]
            if answ[2] in lst_yes and len(password)<int(answ[0]):
                password+= lowercase_letters[random.randrange(0,len(lowercase_letters))]
            if answ[3] in lst_yes and len(password)<int(answ[0]):
                password+= uppercase_letters[random.randrange(0,len(uppercase_letters))]
            if answ[4] in lst_yes and len(password)<int(answ[0]):
                password+= punctuation[random.randrange(0,len(punctuation))]
            if answ[5] in lst_yes:
                for j in password:
                    if j in 'il1Lo0O':
                     password = password.replace(j,'')
        return password


    def start():

        while True:
            try:
                num_pass = int(input('Количество паролей для генерации: '))
                break
            except Exception:
                print('Введенное значение не корректно')
                ask = input('Завершить (y/n)? ')
                if ask == 'y' or ask == 'Y':
                    print('Выход из программы генерации паролей')
                    exit()

        param_answers = ask_pass_params()
        passwords = [generate_password(param_answers) for i in range(int(num_pass))]

        print()
        print('Пароль успешно сгенерирован') if len(passwords)<2 else print('Пароли успешно сгенерированы')
        print()

        for i in range(len(passwords)):
            print(f'|  {passwords[i]}  |')

    start()


