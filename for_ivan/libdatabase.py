import sqlite3

class Connection():
    def __init__(self, db_name):
        print('Устанавливаем соединение с базой данных')
        self.conn = sqlite3.connect(f'{db_name}')
        self.cursor = self.conn.cursor()
        print('Соединение установлено')

    def exec_command(self, command):
        self.cursor.execute(command)
        self.conn.commit()

    def create_table(self):
        command = "CREATE TABLE weather(id INTEGER PRIMARY KEY AUTOINCREMENT, time DATETIME DEFAULT (datetime('now','localtime')), temperature FLOAT)"
        self.exec_command(command)
        print('Таблица создана')

    def clear_table(self):
        command = 'DELETE FROM weather'
        self.exec_command(command)
        print('Таблица очищена')

    def delete_table(self):
        command = 'DROP TABLE weather'
        self.exec_command(command)
        print('Таблица удалена')
    
    def test_insert(self):
        command = "INSERT INTO weather (time, temperature) VALUES ('2023-11-01 22:22:22', 300)"
        self.exec_command(command)
        print('Тестовый ввод данных выполнен')

    def select_all(self):
        command = 'SELECT * FROM weather'
        self.cursor.execute(command)
        result = self.cursor.fetchall()
        if result:
            return result
        else:
            print('В таблице ничего нет')

    def insert_data(self, temp):
        command = f"INSERT INTO weather (temperature) VALUES ({temp})"
        self.exec_command(command)
        print('Данные записаны в таблицу')