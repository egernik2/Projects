import psycopg2
import time
import winsound
import tkinter
from tkinter import messagebox
import logging
import datetime
import pystray
from PIL import Image
import threading
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(funcName)s - %(message)s", filename=f'{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.log', filemode='a') # Настройка формата логгов

root = tkinter.Tk() # Создание экземпляра класса TKinter для показа уведомлений
root.withdraw() # Скрытие основоного окна TKinter

def first_connect(): # устанавливаем соединение с первой базой данных
    try:
        conn1 = psycopg2.connect(database="main", user="postgres", password="6653549", host="localhost", port="5432")
        cur1 = conn1.cursor()
        logging.info('Соединение с первой базой установлено')
        return conn1, cur1
    except:
        print ('Первая база недоступна!')
        logging.error('Первая база недоступна')
        logging.info('Завершение программы')
        sys.exit()

def second_connect(): # устанавливаем соединение со второй базой данных 
    try:
        conn2 = psycopg2.connect(database="default", user="postgres", password="6653549", host="localhost", port="5432")
        cur2 = conn2.cursor()
        logging.info('Соединение со второй базой установлено')
        return conn2, cur2
    except:
        print ('Вторая база недоступна!')
        logging.error('Вторая база недоступна')
        logging.info('Завершение программы')
        sys.exit()

image = Image.open('icon.png')

def on_clicked(icon, item):
    icon.stop()

def icon():
    icon = pystray.Icon('DBChecker', image, menu=pystray.Menu(
    pystray.MenuItem('Exit', on_clicked)))
    icon.run()

thread = threading.Thread(target=icon)
thread.start()

def main():
    while True:
        if thread.is_alive():
            # выбираем определенные колонки из первой таблицы первой базы данных
            try:
                cur1.execute("SELECT s_talker FROM spr_speech_table")
            except:
                print ('Первая база упала!')
                logging.error('Первая база упала!')
                logging.info('Завершение программы')
                sys.exit()

        # получаем результат запроса
            result1 = cur1.fetchall()

        # выбираем определенные колонки из второй таблицы второй базы данных
            try:
                cur2.execute("SELECT s_talker FROM spr_speech_table")
            except:
                print ('Вторая база упала!')
                logging.error('Вторая база упала!')
                logging.info('Завершение программы')
                sys.exit()

        # получаем результат запроса
            result2 = cur2.fetchall()

        # создаем множества для хранения уникальных значений в каждой таблице
            set1 = set()
            set2 = set()

        # добавляем значение каждой колонки первой таблицы в соответствующее множество
            for row in result1:
                set1.add(row[0])

        # добавляем значение каждой колонки второй таблицы в соответствующее множество
            for row in result2:
                set2.add(row[0])

        # находим пересечение множеств, чтобы найти общие значения
            common = set1.intersection(set2)

        # выводим в консоль общие значения, если они есть
            if common:
                for item in common:
                    logging.warning('Найдено общие значение: {}'.format(item))
                print("Общие значения в колонках: {}".format(common))
                winsound.PlaySound('23648.wav', 0)
                messagebox.showwarning("ВНИМАНИЕ!","Есть совпадения в колонках: {}".format(common))
                time.sleep(1)
            else:
                print("Нет общих значений в колонках")
                time.sleep(1)
        else:
            logging.info('Завершение программы')
            sys.exit()

if __name__ == '__main__':
    logging.info('Запуск программы')
    conn1, cur1 = first_connect()
    conn2, cur2 = second_connect()
    main()