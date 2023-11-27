import sqlite3
import os
import time

print('Выполняю попытку подключения к базе данных')
conn = sqlite3.connect("G:/Projects/sql_practice/tickets.db")
cur = conn.cursor()
print('Подключение выполнено')

def create_table_fio():
    print('Выполняется создание базы людей')
    cur.execute('CREATE TABLE fio (fio_id INTEGER PRIMARY KEY AUTOINCREMENT, first_name VARCHAR(50), last_name VARCHAR(50))')

def create_table_ticket():
    print('Выполняется создание базы тикетов')
    cur.execute('CREATE TABLE tickets (id INTEGER PRIMARY KEY, name VARCHAR(50), fio_id INTEGER, FOREIGN KEY (fio_id) REFERENCES fio (fio_id))')

def get_data_all():
    pass

def get_data_by_fio():
    pass

def insert_data_table_fio():
    pass

def insert_data_table_ticket():
    pass

def exit_from_program():
    exit(0)

menu = {1: insert_data_table_fio, 
        2: insert_data_table_ticket, 
        3: get_data_all, 
        4: get_data_by_fio,
        0: exit_from_program}

names = {1: "Добавить человека",
         2: "Добавить тикет",
         3: "Получить все данные",
         4: "Получить данные по фамилии",
         0: "Выход"}

def print_menu():
    time.sleep(1)
    os.system('cls')
    print("\tМеню\n")
    for point in menu:
        print('{}: {}'.format(point, names[point]))

def main():
    while True:
        print_menu()
        choice = int(input('Выбор: '))
        if choice in menu.keys():
            menu[choice]()
        else:
            print_menu()

if __name__ == '__main__':
    main()