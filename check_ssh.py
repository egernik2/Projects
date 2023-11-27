from time import sleep
import logging
import datetime
import paramiko
from win10toast import ToastNotifier
from os import system

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(funcName)s - %(message)s", filename=f'{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.log', filemode='a') # Настройка формата логгов
hostname = '95.220.147.57'
username = 'Пользователь'
password = ''
toast = ToastNotifier()

def main():
    n = 1
    while True:
        print ('Запуск попытки номер: {}'.format(n))
        logging.info('Запуск попытки номер: {}'.format(n))
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(hostname=hostname, username=username, password=password, timeout=5)
            transport = ssh.get_transport()
            status = transport.is_active()
            if status:
                logging.info('Подключение установлено')
                toast.show_toast('SSH CHECKER', 'Саша включил комп!')
                break
            else:
                sleep (60)
        except:
            print ('Неудачная попытка')
            logging.info('Неудачная попытка')
            n += 1
            sleep (60)

if __name__ == '__main__':
    logging.info('Запуск программы')
    system ('cls')
    main()
    logging.info('Завершение программы')