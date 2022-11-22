"""
Вам дается код, который принимает входные данные и печатает их в виде простой строки текста.
Добавьте uppercase_decorator, чтобы сделать текст заглавным.
Метод upper() можно использовать для строк, чтобы сделать их прописными
"""

text = "hui"

def uppercase_decorator(func):
    def wrapper(text):
        print(text.upper())
    return wrapper


@uppercase_decorator
def display_text(text):
    return (text)

display_text(text)