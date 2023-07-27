import random


def bubble_sort(
    my_list,
):
    
    """
    Объясни пожалуйста как работает функция, трасировка построчно

    """
    last_item = len(my_list) - 1
    sor_list = []
    # print('Получен список: ', my_list)
    for i in range(0, last_item):
        for j in range(0, last_item):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    return my_list
    # print("Отсортированный список: ", my_list)


def uniq_list(a=0, b=100, ln=10):
    list_ = []
    # TODO:"need tests"

    while len(list_) < ln:
        c = random.randint(a, b)
        if c not in list_:
            list_.append(c)
    return list_
