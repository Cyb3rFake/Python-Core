import random


def uniq_list(a=0, b=10, ln=10):
    list_=[]
    while len(list_)<ln:
        c = random.randint(a,b)
        if c not in list_:
            list_.append(c)
    return list_

