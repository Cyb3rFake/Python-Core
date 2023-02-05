import subprocess
import time
import math

# while True:
#     subprocess.call("TASKKILL /F /IM notepad.exe", shell=True)
#     time.sleep(10)

# print('Уникальные отсортированные символы в строке  "съешь же ещё этих мягких французских булок, да выпей чаю." : ')

# print(*sorted(set('съешь же ещё этих мягких французских булок, да выпей чаю.')))

def ebu4ie_4asy(sec):
    sec = sec % (24 * 3600)
    hour = sec // 3600 % (24 * 3600)
    minutes = sec % 3600 // 60
    sec = sec % 60

    if hour < 9:
        hour = '0' + str(hour)
    if minutes < 9:
        minutes = '0' + str(minutes)
    if sec < 9:
        sec = '0' + str(sec)
    print(f'{hour}:{minutes}:{sec}')


#

test_list = [3721, 5000, 27331]
for i in test_list:
    ebu4ie_4asy(i)


def test_func(*args):
    for i in args:
        print()


# test_func('hui','pizda','noski','zalupa')

def print_keyword_args(**kwargs):
    # kwargs is a dict of the keyword args passed to the function
    # print(type(kwargs))
    for key, value in kwargs.items():
        print(key, value)

# print_keyword_args(first_name="John", last_name="Doe")
