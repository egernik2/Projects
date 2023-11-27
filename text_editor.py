import os
from time import sleep
from sys import exit
os.system('cls')
print ('Добро пожаловать в тектовый редактор\n')
menu_list = ['\tМеню:', '1. Создать файл', '2. Открыть файл', '3. Удалить файл', '4. Обзор', '5. Выход\n']
def print_menu():
    for item in menu_list:
        print (item)
    choice = input('Выбор: ')
    return choice

def scan_dir():
    print ('\n')
    dir = os.listdir()
    dir_list = '\t'.join(dir)
    print (dir_list)

def delete_file():
    a = input('Введите имя файла: ')
    try:
        os.remove(a)
        print ('\nФайл {} удалён'.format(a))
        sleep (2)
    except:
        print ('Ошибка: Файла либо не существует, либо это вообще папка!')
        sleep (2)

def open_file():
    name = input('Введите имя файла: ')
    try:
        with open(name, 'r') as f:
            data = f.read()
            return data
    except:
        print ('\nТакого файла не существует!')
        return 0

def read_file():
    name = input('Введите имя файла: ')
    if os.path.exists(name):
        print ('\nТакой файл уже существует')
        sleep (2)
    else:
        while True:
            text = input('\nТекст: ')
            if text == 'exit':
                break
            else:
                with open(name, 'a') as f:
                    os.system('cls')
                    f.write('{}\n'.format(text))
                with open(name, 'r') as f:
                    data = f.read()
                print (data)

while True:
    choice = print_menu()
    if choice == '1':
        read_file()
        os.system('cls')
    elif choice == '2':
        data = open_file()
        if data:
            os.system('cls')
            print (data)
            input ('\nДля выхода нажми Enter...')
            os.system('cls')
        else:
            sleep (2)
            os.system('cls')
    elif choice == '3':
        delete_file()
        os.system('cls')
    elif choice == '4':
        scan_dir()
    elif choice == '5':
        exit()
    else:
        print ('\nТакого пункта нет в меню')
        sleep (1)
        print_menu()