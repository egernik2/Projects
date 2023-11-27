import sqlite3

def create_table_address():
    with sqlite3.connect('G:/Projects/sql_practice/my_family.db') as conn:
        cur = conn.cursor()
        # cur.execute('CREATE TABLE address (id_address INTEGER PRIMARY KEY AUTOINCREMENT, city VARCHAR(20), street VARCHAR(30), house INTEGER NOT NULL, corpus INTEGER, apartament INT)')
        # cur.execute('INSERT INTO address (city, street, house, corpus, apartament) VALUES ("Москва", "Изюмская", 55, 1, 6)')
        # cur.execute('INSERT INTO address (city, street, house, corpus, apartament) VALUES ("Москва", "Кустанайская", 5, 2, 186)')
        # cur.execute('INSERT INTO address (city, street, house, corpus, apartament) VALUES ("Москва", "Кустанайская", 5, 2, 203)')

def select_all_from_address():
    with sqlite3.connect('G:/Projects/sql_practice/my_family.db') as conn:
        cur = conn.cursor()
        cur.execute('SELECT * FROM address')
        result = cur.fetchall()
        for item in result:
            print(item)

def create_table_fio():
    with sqlite3.connect('G:/Projects/sql_practice/my_family.db') as conn:
        cur = conn.cursor()
        cur.execute('CREATE TABLE fio (id_fio INTEGER PRIMARY KEY AUTOINCREMENT, last_name VARCHAR(20), first_name VARCHAR(20), second_name VARCHAR(20), address_id INTEGER, FOREIGN KEY (address_id) REFERENCES address (address_id))')

def insert_data_into_table_fio():
    with sqlite3.connect('G:/Projects/sql_practice/my_family.db') as conn:
        cur = conn.cursor()
        cur.execute('INSERT INTO fio (last_name, first_name, second_name, address_id) VALUES ("Ильин", "Роман", "Григорьевич", 1)')

def select_all_from_table_fio():
    with sqlite3.connect('G:/Projects/sql_practice/my_family.db') as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM fio")
        result = cur.fetchall()
        for item in result:
            print(item)

def select_all_from_table_fio_witn_address():
    with sqlite3.connect('G:/Projects/sql_practice/my_family.db') as conn:
        cur = conn.cursor()
        cur.execute('SELECT last_name, first_name, second_name, city, street, house, corpus, apartament from address a right join fio f on a.id_address = f.address_id')
        result = cur.fetchall()
        for item in result:
            print(item)

def main():
    # print('ID | Город | Улица | Дом | Корпус | Квартира')
    # select_all_from_address()
    # create_table_address()
    # create_table_fio()
    # insert_data_into_table_fio()
    # select_all_from_table_fio()
    select_all_from_table_fio_witn_address()

if __name__ == '__main__':
    main()