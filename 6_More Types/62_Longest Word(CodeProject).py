"""
Учитывая текст в качестве входных данных, найдите и выведите самое длинное слово.

Пример ввода
это потрясающий текст

Пример вывода
потрясающий
Вспомним метод split(' '), который возвращает список слов строки.

"""

txt = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"
txt = txt.replace(",", "")
txt = txt.split(" ")

mx = ""
for i in txt:
    if len(i)>len(mx):
        mx = i
    # print(i,len(i))

print(mx)
