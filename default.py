import customtkinter
import psycopg2
import tkinter
from tkinter import messagebox
import threading
import logging
import datetime
import time
import sys
import json
import winsound

# Логгер
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(funcName)s - %(message)s", filename=f'{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.log', filemode='a')

# Настройки темы окна
customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("blue")
    
# Окно
logging.info('Запуск программы')

class MainWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('Мониторинг')
        self.geometry('800x800')
        # Ввод данных mainbase
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        # Надпись База №1
        self.base1 = customtkinter.CTkLabel(self, text = 'База № 1')
        self.base1.grid(column=0, row=0, sticky='n', padx=15, pady=15, columnspan=2)
        # Надпись Хост
        self.entry_host1_label = customtkinter.CTkLabel(self, text = 'Хост:', justify='left')
        self.entry_host1_label.grid(column=0, row=1, sticky='n', padx=10, pady=5)
        # Поле ввода хоста
        self.entry_host1 = customtkinter.CTkEntry(self, width = 150)
        self.entry_host1.grid(column=1, row=1, sticky='n', padx=10, pady=5)
        # Надпись Порт
        self.entry_port1_label = customtkinter.CTkLabel(self, text = 'Порт:  ', justify='left')
        self.entry_port1_label.grid(column=0, row=2, sticky='n', padx=10, pady=5)
        # Поле ввода порта
        self.entry_port1 = customtkinter.CTkEntry(self, width = 150, placeholder_text='5432')
        self.entry_port1.grid(column=1, row=2, sticky='n', padx=10, pady=5)
        #self.entry_port1.insert(0, '5432321')
        # Надпись База данных
        self.entry_database1_label = customtkinter.CTkLabel(self, text = 'База данных:  ', justify='left')
        self.entry_database1_label.grid(column=0, row=3, sticky='n', padx=10, pady=5)
        # Поле ввода базы данных
        self.entry_database1 = customtkinter.CTkEntry(self, width = 150)
        self.entry_database1.grid(column=1, row=3, sticky='n', padx=10, pady=5)
        # Надпись Пользователь
        self.entry_user1_label = customtkinter.CTkLabel(self, text = 'Пользователь:  ', justify='left')
        self.entry_user1_label.grid(column=0, row=4, sticky='n', padx=10, pady=5)
        # Поле ввода пользователя
        self.entry_user1 = customtkinter.CTkEntry(self, width = 150)
        self.entry_user1.grid(column=1, row=4, sticky='n', padx=10, pady=5)
        # Надпись Пароль
        self.entry_pass1_label = customtkinter.CTkLabel(self, text = 'Пароль:  ', justify='left')
        self.entry_pass1_label.grid(column=0, row=5, sticky='n', padx=10, pady=5)
        # Поле ввода пароля
        self.entry_pass1 = customtkinter.CTkEntry(self, width = 150, show = '*')
        self.entry_pass1.grid(column=1, row=5, sticky='n', padx=10, pady=5)
       
        # # Ввод данных blacklist
        # Надпись База №1
        self.base2 = customtkinter.CTkLabel(self, text = 'База № 2')
        self.base2.grid(column=2, row=0, sticky='n', padx=15, pady=15, columnspan=2)
        # Надпись Хост
        self.entry_host2_label = customtkinter.CTkLabel(self, text = 'Хост:', justify='left')
        self.entry_host2_label.grid(column=2, row=1, sticky='n', padx=10, pady=5)
        # Поле ввода хоста
        self.entry_host2 = customtkinter.CTkEntry(self, width = 150)
        self.entry_host2.grid(column=3, row=1, sticky='n', padx=10, pady=5)
        # Надпись Порт
        self.entry_port2_label = customtkinter.CTkLabel(self, text = 'Порт:', justify='left')
        self.entry_port2_label.grid(column=2, row=2, sticky='n', padx=10, pady=5)
        # Поле ввода порта
        self.entry_port2 = customtkinter.CTkEntry(self, width = 150, placeholder_text='5432')
        self.entry_port2.grid(column=3, row=2, sticky='n', padx=10, pady=5)
        #self.entry_port1.insert(0, '5432321')
        # Надпись База данных
        self.entry_database2_label = customtkinter.CTkLabel(self, text = 'База данных:', justify='left')
        self.entry_database2_label.grid(column=2, row=3, sticky='n', padx=10, pady=5)
        # Поле ввода базы данных
        self.entry_database2 = customtkinter.CTkEntry(self, width = 150)
        self.entry_database2.grid(column=3, row=3, sticky='n', padx=10, pady=5)
        # Надпись Пользователь
        self.entry_user2_label = customtkinter.CTkLabel(self, text = 'Пользователь:', justify='left')
        self.entry_user2_label.grid(column=2, row=4, sticky='n', padx=10, pady=5)
        # Поле ввода пользователя
        self.entry_user2 = customtkinter.CTkEntry(self, width = 150)
        self.entry_user2.grid(column=3, row=4, sticky='n', padx=10, pady=5)
        # Надпись Пароль
        self.entry_pass2_label = customtkinter.CTkLabel(self, text = 'Пароль:', justify='left')
        self.entry_pass2_label.grid(column=2, row=5, sticky='n', padx=10, pady=5)
        # Поле ввода пароля
        self.entry_pass2 = customtkinter.CTkEntry(self, width = 150, show = '*')
        self.entry_pass2.grid(column=3, row=5, sticky='n', padx=10, pady=5)
        
        # # Кнопки
        self.btn_connect1 = customtkinter.CTkButton(self, text = 'Подключиться', command = self.connect1)
        self.btn_connect1.grid(column=0, row=6, sticky='n', padx=10, pady=20, columnspan=2)

        self.btn_connect2 = customtkinter.CTkButton(self, text = 'Подключиться', command = self.connect2)
        self.btn_connect2.grid(column=2, row=6, sticky='n', padx=10, pady=20, columnspan=2)

        self.btn_monitoring = customtkinter.CTkButton(self, text = 'Мониторинг', command= self.check_connections)
        self.btn_monitoring.grid(column=0, row=7, sticky='n', padx=10, pady=50, columnspan=4)

        self.btn_exit = customtkinter.CTkButton(self, text = 'Выход', command = self.commandexit)
        self.btn_exit.grid(column=3, row=8, sticky='n', padx=10, pady=300)

        self.conn1 = 0
        self.conn2 = 0

    # Подключения к БД1
    def connect1(self):
        try:
            self.conn1 = psycopg2.connect(host = self.entry_host1.get(), port = self.entry_port1.get(), database = self.entry_database1.get(),
                                          user = self.entry_user1.get(), password = self.entry_pass1.get())
            self.cur1 = self.conn1.cursor()
            messagebox.showinfo(title = 'Сообщение', message= 'Подключение успешно')
            logging.info('Соединение с первой базой установлено')
        except:
            messagebox.showerror("Ошибка", "Первая база недоступна!")
            logging.error('Первая база недоступна')
    
    
    # Подключения к БД2
    def connect2(self):
        try:
            self.conn2 = psycopg2.connect(host = self.entry_host2.get(), port = self.entry_port2.get(), database = self.entry_database2.get(),
                                          user = self.entry_user2.get(), password = self.entry_pass2.get())
            self.cur2 = self.conn2.cursor()
            messagebox.showinfo(title = 'Сообщение', message= 'Подключение успешно')
            logging.info('Соединение со второй базой установлено')
        except:
            messagebox.showerror("Ошибка", "Первая база недоступна!")
            logging.error('Вторая база недоступна')


    def commandexit(self):
        logging.info('Завершение программы')
        if self.conn1 or self.conn2:
            self.conn1.close()
            self.conn2.close()
        sys.exit()

    def check_connections(self):
        if self.conn1 and self.conn2:
            self.destroy()
        else:
            messagebox.showerror("Ошибка", "Сначала необходимо подключиться к базам!")


class Monitoring(customtkinter.CTk):
    def __init__(self, cur1, cur2):
        super().__init__()
        self.cur1 = cur1
        self.cur2 = cur2
        self.title('Мониторинг')
        self.geometry('800x800')
        self.x = 15
        # Функции окна
        self.columnconfigure(0, weight=1)
        self.Label1 = customtkinter.CTkLabel(self, text = 'Результат', font=('Times New Roman Bold', 20))
        self.Label1.grid(column=0, row=0, sticky='n', padx=15, pady=15)
        self.text_field = customtkinter.CTkTextbox(self, width = 560, height = 360)
        self.text_field.grid(column=0, row=1, sticky='ew', padx=10, pady=10)
        self.text_field.configure(state = "disable")
        self.text_field.insert('end', self.x)
        self.text_field.after
        self.btn_exit = customtkinter.CTkButton(self, text = 'Выход', command = self.commandexit)
        self.btn_exit.grid(column=0, row=2, sticky='s', padx=10, pady=10)
        self.f = 0

    def query(self):
        while True:
            try:
                self.cur1.execute("SELECT s_talker FROM spr_speech_table")
            except Exception as ex:
                messagebox.showerror("Ошибка", "Первая база упала!")
                logging.error('Первая база упала!')
                logging.info('Завершение программы')
                self.destroy()

            # получаем результат запроса
            self.result1 = self.cur1.fetchall()

            # выбираем определенные колонки из второй таблицы второй базы данных
            try:
                self.cur2.execute("SELECT s_talker FROM spr_speech_table")
            except:
                messagebox.showerror("Ошибка", "Вторая база упала!")
                logging.error('Вторая база упала!')
                logging.info('Завершение программы')
                self.destroy()
            
            # получаем результат запроса
            self.result2 = self.cur2.fetchall()

            self.set1 = set()
            self.set2 = set()

            # добавляем значение каждой колонки первой таблицы в соответствующее множество
            for row in self.result1:
                self.set1.add(row[0])

            # добавляем значение каждой колонки второй таблицы в соответствующее множество
            for row in self.result2:
                self.set2.add(row[0])

            # находим пересечение множеств, чтобы найти общие значения
            self.common = self.set1.intersection(self.set2)

            # выводим в консоль общие значения, если они есть
            if self.common:
                for item in self.common:
                    logging.warning('Найдено общие значение: {}'.format(item))
                self.text_field.configure(state = "normal")
                self.text_field.insert('end', "Общие значения в колонках: {}\n".format(self.common))
                self.text_field.see('end')
                self.text_field.after
                self.text_field.configure(state = "disable")
                self.f = 1
                time.sleep(1)
            else:
                self.text_field.configure(state = "normal")
                self.text_field.insert('end', "Нет общих значений\n")
                self.text_field.see('end')
                self.text_field.after
                self.text_field.configure(state = "disable")
                time.sleep(1)

    def notification(self):
        while True:
            if self.f == 1:
                winsound.PlaySound('23648.wav', 0)
                messagebox.showwarning("ВНИМАНИЕ!","Есть совпадения в колонках: {}".format(self.common))
                self.f = 0
            time.sleep(1)
    
    def commandexit(self):
        logging.info('Завершение программы')
        self.destroy()

def main():
    mainwindow = MainWindow()
    mainwindow.mainloop()
    if mainwindow.conn1 and mainwindow.conn2:
        cur1 = mainwindow.cur1
        cur2 = mainwindow.cur2
        monitoring_window = Monitoring(cur1, cur2)
        thread = threading.Thread(target=monitoring_window.query, daemon=True) # Поток для выполнения запросов
        thread.start()
        thread2 = threading.Thread(target=monitoring_window.notification, daemon=True) # Поток для уведомлений
        thread2.start()
        monitoring_window.mainloop()
        mainwindow.conn1.close()
        mainwindow.conn2.close()

if __name__ == '__main__':
    main()

    # monitor = Monitoring()
    # thread = threading.Thread(target=monitor.query, daemon=True)
    # thread.start()
    # monitor.mainloop()