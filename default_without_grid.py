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
        self.base1 = customtkinter.CTkLabel(self, text = 'База № 1').place(x = 197, y = 15)
        self.entry_host1_label = customtkinter.CTkLabel(self, text = 'Хост:  ').place(x = 50, y = 40)
        self.entry_host1 = customtkinter.CTkEntry(self, width = 150)
        self.entry_host1.place(x = 150, y = 40)
        self.entry_port1_label = customtkinter.CTkLabel(self, text = 'Порт:  ').place(x = 50, y = 80)
        self.entry_port1 = customtkinter.CTkEntry(self, width = 150)
        self.entry_port1.place(x = 150, y = 80)
        self.entry_database1_label = customtkinter.CTkLabel(self, text = 'База данных:  ').place(x = 50, y = 120)
        self.entry_database1 = customtkinter.CTkEntry(self, width = 150)
        self.entry_database1.place(x = 150, y = 120)
        self.entry_user1_label = customtkinter.CTkLabel(self, text = 'Пользователь:  ').place(x = 50, y = 160)
        self.entry_user1 = customtkinter.CTkEntry(self, width = 150)
        self.entry_user1.place(x = 150, y = 160)
        self.entry_pass1_label = customtkinter.CTkLabel(self, text = 'Пароль:  ').place(x = 50, y = 200)
        self.entry_pass1 = customtkinter.CTkEntry(self, width = 150, show = '*')
        self.entry_pass1.place(x = 150, y = 200)
        # Ввод данных blacklist
        self.base2 = customtkinter.CTkLabel(self, text = 'База № 2').place(x = 495, y = 15)
        self.entry_host2_label = customtkinter.CTkLabel(self, text = 'Хост:  ').place(x = 350, y = 40)
        self.entry_host2 = customtkinter.CTkEntry(self, width = 150)
        self.entry_host2.place(x = 450, y = 40)
        self.entry_port2_label = customtkinter.CTkLabel(self, text = 'Порт:  ').place(x = 350, y = 80)
        self.entry_port2 = customtkinter.CTkEntry(self, width = 150)
        self.entry_port2.place(x = 450, y = 80)
        self.entry_database2_label = customtkinter.CTkLabel(self, text = 'Базаданных:  ').place(x = 350, y = 120)
        self.entry_database2 = customtkinter.CTkEntry(self, width = 150)
        self.entry_database2.place(x = 450, y = 120)
        self.entry_user2_label = customtkinter.CTkLabel(self, text = 'Пользователь:  ').place(x = 350, y = 160)
        self.entry_user2 = customtkinter.CTkEntry(self, width = 150)
        self.entry_user2.place(x = 450, y = 160)
        self.entry_pass2_label = customtkinter.CTkLabel(self, text = 'Пароль:  ').place(x = 350, y = 200)
        self.entry_pass2 = customtkinter.CTkEntry(self, width = 150, show = '*')
        self.entry_pass2.place(x = 450, y = 200)
        # Кнопки
        self.btn_connect1 = customtkinter.CTkButton(self, text = 'Подключиться', command = self.connect1)
        self.btn_connect1.place(x = 155, y = 240)

        self.btn_connect2 = customtkinter.CTkButton(self, text = 'Подключиться', command = self.connect2)
        self.btn_connect2.place(x = 455, y = 240)

        self.btn_monitoring = customtkinter.CTkButton(self, text = 'Мониторинг', command= self.check_connections)
        self.btn_monitoring.place(x = 300, y = 340)

        self.btn_exit = customtkinter.CTkButton(self, text = 'Выход', command = self.commandexit)
        self.btn_exit.place(x = 600, y = 340)

        self.conn1 = 0
        self.conn2 = 0

    # Подключения к БД1
    def connect1(self):
        try:
            self.conn1 = psycopg2.connect(host = self.entry_host1.get(), port = self.entry_port1.get(), database = self.entry_database1.get(), user = self.entry_user1.get(), password = self.entry_pass1.get())
            self.cur1 = self.conn1.cursor()
            messagebox.showinfo(title = 'Сообщение', message= 'Подключение успешно')
            logging.info('Соединение с первой базой установлено')
        except:
            messagebox.showerror("Ошибка", "Первая база недоступна!")
            logging.error('Первая база недоступна')
    
    
    # Подключения к БД2
    def connect2(self):
        try:
            self.conn2 = psycopg2.connect(host = self.entry_host2.get(), port = self.entry_port2.get(), database = self.entry_database2.get(), user = self.entry_user2.get(), password = self.entry_pass2.get())
            self.cur2 = self.conn2.cursor()
            messagebox.showinfo(title = 'Сообщение', message= 'Подключение успешно')
            logging.info('Соединение со второй базой установлено')
        except:
            messagebox.showerror("Ошибка", "Первая база недоступна!")
            logging.error('Вторая база недоступна')


    def commandexit(self):
        logging.info('Завершение программы')
        sys.exit()

    def check_connections(self):
        if self.conn1 and self.conn2:
            self.destroy()
        else:
            messagebox.showerror("Ошибка", "Сначала необходимо подключиться к базам!")


class Monitoring(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('Мониторинг')
        self.geometry('800x800')
        self.x = 15
        # Функции окна
        self.text_field = customtkinter.CTkTextbox(self, width = 560, height = 360)
        self.text_field.place(x = 20, y = 130)
        self.text_field.configure(state = "disable")
        self.text_field.insert('end', self.x)
        self.text_field.after
        self.btn_exit = customtkinter.CTkButton(self, text = 'Выход', command = self.commandexit)
        self.btn_exit.place(x = 600, y = 340)
    
    def test(self):
        for _ in range(10):
            self.text_field.configure(state = "normal")
            self.text_field.insert('end', '123\n')
            self.text_field.after
            self.text_field.configure(state = "disable")
            time.sleep(1)
    
    def commandexit(self):
        logging.info('Завершение программы')
        sys.exit()

def main():
    mainwindow = MainWindow()
    mainwindow.mainloop()
    if mainwindow.conn1 and mainwindow.conn2:
        monitoring_window = Monitoring()
        thread = threading.Thread(target=monitoring_window.test, daemon=True)
        thread.start()
        monitoring_window.mainloop()

if __name__ == '__main__':
    main()

    # monitor = Monitoring()
    # thread = threading.Thread(target=monitor.test, daemon=True)
    # thread.start()
    # monitor.mainloop()