from getpass import getpass
import paramiko
import re
import time
import json

# Устанавливаем соединение SSH
USERNAME = 'lordr'
FILE_NAME = 'list.txt'
CMD = 'tasklist'

def read_conf():
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
            return config
    except:
        print ('Файла конфигурации config.json нет')
        exit()

def recv_all(paramiko_channel):
    parts = []
    while paramiko_channel.recv_ready():
        parts.append(paramiko_channel.recv(4096))
    return b"".join(parts)

def recv_stderr(paramiko_channel):
    parts = []
    while paramiko_channel.recv_stderr_ready():
        parts.append(paramiko_channel.recv_stderr(4096))
    return b"".join(parts)

def autossh(host, user, password, cmd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, username=user, password=password, timeout=30)
    # Получаем транспорт SSH подключения
    transport = ssh.get_transport()
    # Открываем канал
    paramiko_channel = ssh.get_transport().open_session()
    paramiko_channel.set_combine_stderr(True)
    paramiko_channel.exec_command(cmd)
    output = b''
    while not paramiko_channel.exit_status_ready():
        buffer = recv_all(paramiko_channel)
        output += buffer
        if re.search(b'continue connecting (yes/no)?', buffer.lower()):
            paramiko_channel.send("yes\n")
        time.sleep(0.1)
    ecode = paramiko_channel.recv_exit_status()
    output = recv_all(paramiko_channel)
    #errors = recv_stderr(paramiko_channel)
    return ecode, output.decode("CP866")#, errors.decode("CP866")

def print_info():
    print ('Данные для входа:')
    print ('Пользователь: {}'.format(USERNAME))
    print ('Команда: {}'.format(CMD))
    print ('Имя файла со списком хостов: {}'.format(FILE_NAME))
    print ('Желаете вывести содержимое файла? y/n: ', end='')
    choice = input()
    if choice.lower() == 'y' or choice == '':
        with open(FILE_NAME, 'r') as f:
            list_of_hosts = f.read().splitlines()
        for host in list_of_hosts:
            print ('{}. {}'.format(list_of_hosts.index(host) + 1, host))

def main():
    config = read_conf()
    print_info()
    password = getpass('\nPassword: ')
    with open(config.get('file_name'), 'r') as f:
            list_of_hosts = f.read().splitlines()
    for host in list_of_hosts:
        try:
            ecode, output = autossh(host, config.get('user'), password, config.get('cmd'))
            print ('HOST: {}\nECODE: {}\nOUTPUT: {}'.format(host, ecode, output))
        except Exception as ex:
            print ('{}: {}'.format(host, ex))

if __name__ == '__main__':
    main()