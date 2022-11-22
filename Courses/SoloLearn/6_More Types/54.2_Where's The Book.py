""""
Вы можете использовать метод .get() для поиска ключей в словаре и использовать второй
параметр для возврата значения по умолчанию в случае, если ключ не найден.

Перепишите данный код, чтобы использовать метод .get() вместо инструкций if/else.
Кроме того, измените вывод на "Книга не найдена", когда книга не найдена.
Обратите внимание, насколько короче результирующий код по сравнению с инструкцией if/else.
"""
books = {
    "Life of Pi": "Adventure Fiction",
    "The Three Musketeers": "Historical Adventure",
    "Watchmen": "Comics",
    "Bird Box": "Horror",
    "Harry Potter":"Fantasy Fiction",
    "Good Omens": "Comedy"
}

book = input()

print(books.get(book,"Book not found"))



#change this part to use the .get() method
# if(book in books):
#     print(books[book])
# else:
#     print("Not Found")