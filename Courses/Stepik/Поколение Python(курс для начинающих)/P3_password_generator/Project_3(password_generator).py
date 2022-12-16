import random

if __name__ == '__main__':
    digits = '0123456789'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    punctuation = '!#$%&*+-=?@^_.'

    chars = digits + lowercase_letters + uppercase_letters + punctuation

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

        lst = [input() for i in 7]