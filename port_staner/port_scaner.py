import socket
import threading
import re

IP_MASK = r'^\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b$'

def main():
    print('Добро пожаловать в программу сканирования портов хостов. Пожалуйста, укажите все необходимые данные перед началом сканирования.')
    ip_start = None
    ip_end = None
    port_start = None
    port_end = None
    while not ip_start:
        raw_ip_start = input('Укажите начальный IP-адрес: ')
        if raw_ip_start and re.search(IP_MASK, raw_ip_start):
            ip_start = raw_ip_start
        else:
            print('IP-адрес указан неверно')
    while not ip_end:
        raw_ip_end = input('Укажите конечный IP-адрес: ')
        if raw_ip_end and re.search(IP_MASK, raw_ip_end):
            ip_end = raw_ip_end
        else:
            print('IP-адрес указан неверно')
    while not port_start:
        port_start = input('Введите начальный порт: ')
        try:
            port_start = int(port_start)
        except ValueError:
            print('Порт имеет неверный формат')
            port_start = None
    while not port_end:
        port_end = input('Введите конечный порт: ')
        try:
            port_end = int(port_end)
        except ValueError:
            print('Порт имеет неверный формат')
            port_end = None
    if ip_start and ip_end and port_start and port_end:
        

if __name__ == '__main__':
    main()