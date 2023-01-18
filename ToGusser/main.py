
import psutil
from os import *
import time
import getpass
import subprocess
import watchdog

working_time = 5 # допустимое время работы программы(мин)
name_process = 'notepad.exe' # имя наблюдаемого процесса
warning_time = 2 # время начала оповещения(мин)


print()

def get_user_name():
    # получаем имя текущего пользователя
    return getpass.getuser()


def find_process_by_name(name):
    # Поиск нужного процесса по имени
    proc_name = name
    ls = [proc for proc in psutil.process_iter(['name']) if proc.info['name'] == proc_name]
    if not ls:
        print(f'Процесс "{proc_name}" не найден')
    else:
        print(f'Процесс "{proc_name}" найден')
    return True

def get_working_time(name):
    # получить время работы программы(процесса) (часы),(минуты)
    s = (''.join([str(proc) for proc in psutil.process_iter(['name']) if proc.info['name'] == name])).split(',')[-1].split('=')[1]
    start_proc_time = []
    c = 0
    for i in s:
        if i.isdigit()==True:
            start_proc_time.append(i)
            c+=1
            if c % 2 == 0 and c!=6:
                start_proc_time.append(':')

    start_proc_time =''.join(start_proc_time).split(':') # время начала работы программы
    now_time = time.ctime().split()[-2].split(':') # текущее время
    # now_time = int(now_time[0])*360 + int(now_time[1])*60 + int(now_time[2]) #текущее время в секундах
    # print(start_proc_time,now_time,sep='\n')
    h,m = abs(int(now_time[0])-int(start_proc_time[0])),abs(int(now_time[1])-int(start_proc_time[1]))

    # print(abs(int(now_time[1])-int(start_proc_time[1])),'прошло минут')
    # print(abs(int(now_time[2])-int(start_proc_time[2])),'прошло секунд')
    # print(h*60,working_time)

    print(f'Программа "{name_process}" работает {h} часов {m} минут')
    # kill_process(h*60+m,working_time)
    return h*60+m  # суммарное время минут


def kill_process(w_minutes,norm_time=2):
    if w_minutes>norm_time:
        print(f'Работа программы "{name_process}" будет прекращена через {warning_time} минут')
        s = subprocess.call("TASKKILL /F /IM {}".format(name_process) , shell=True)
        return print(f'программа {name_process} закрыта')


def write_stat():
    if find_process_by_name(name_process) == True:
        working_time = get_working_time(name_process)
        with open(f'{get_user_name()}.txt','w') as f:
            f.write(f'Пользователь {get_user_name()}\n')
            f.write(f'Время работы приложения {name_process}: {working_time} мин\n')
        return print('Запись сделана успешно')


def read_stat():
    get_fles_name = [i for i in listdir('D:\PycharmProjects\Python-Core\ToGusser') if i.split('.')[1]=='txt']

    for i in range(len(get_fles_name)):
        # print(get_fles_name[i])
        file = str(get_fles_name[i])
        print(type(file))

        with open('krasavin_fn.txt',"r") as f:
            data = f.read()
        print(data)


        # print(d)
        # # print(get_fles_name)


read_stat()









# s = str(find_process_by_name('notepad.exe')[0]) #получить список процессов по имени
# d=(find_process_by_name('notepad.exe').replace('psutil.Process','').replace(s[-1],'').replace('(','')).split(', ')[-1].split('=')[1]
# print(d)
# strarted_process_time = (d.replace(d[0],'').replace(d[-1],'')).split(':')
# now_time = time.ctime().split()[-2].split(':')
# working_time(strarted_process_time,now_time)




def get_working_time(name):
    # получить время работы программы(процесса) (часы),(минуты)
    s = (''.join([str(proc) for proc in psutil.process_iter(['name']) if proc.info['name'] == name])).split(',')[-1].split('=')[1]
    start_proc_time = []
    c = 0
    for i in s:
        if i.isdigit()==True:
            start_proc_time.append(i)
            c+=1
            if c % 2 == 0 and c!=6:
                start_proc_time.append(':')

    start_proc_time =''.join(start_proc_time).split(':') # время начала работы программы
    now_time = time.ctime().split()[-2].split(':') # текущее время
    h,m = abs(int(now_time[0])-int(start_proc_time[0])),abs(int(now_time[1])-int(start_proc_time[1]))
    print(f'Программа "{name_process}" работает {h} часов {m} минут')
    return h*60+m  # суммарное время минут



def get_user_name():
    # получаем имя текущего пользователя
    return getpass.getuser()




