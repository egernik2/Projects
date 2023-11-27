# Скрипт - баловство с paramiko (для ssh) и re (регулярные выражения)

# Импорт библиотеки os для выполнения команд операционной системы
import os
# Импорт библиотеки paramiko для установки ssh подключений
import paramiko
# Импорт библиотеки re для работы с регулярными выражениями
import re
import time

# Устанавливаем соединение SSH
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='95.220.147.57', username='Пользователь', password='', timeout=10)

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

# Получаем транспорт SSH подключения
transport = ssh.get_transport()
# Открываем канал
paramiko_channel = ssh.get_transport().open_session()
paramiko_channel.set_combine_stderr(True)
cmd = 'tasklist'
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
errors = recv_stderr(paramiko_channel)
print (ecode, output.decode("CP866"), errors.decode("CP866"))

# # Выполняем команду и получаем ответ
# stdin, stdout, stderr = ssh.exec_command('tasklist')

# # Выполняем декодирование полученного ответа с помощью кодировщика CP866, использующегося на Windows 10 (может и на других тоже)
# msg = stdout.read().decode('CP866')

# # Сохраняем ответ в файл
# with open('tmp_file', 'w') as f:
#     f.write(msg)

# # Сразу считываем его из файла, чтобы засунуть его в список
# with open('tmp_file', 'r') as f:
#     l = f.readlines()

# # Удаляем временный файл
# os.system('del tmp_file')

# # Паттерн для получения строк, содержащих слова, в которых есть .exe
# pattern = r"\.exe" 
# m = []
# for string in l:
#     # Удаляем символы перевода строки в начале и в конце строк
#     string = string.strip() 
#     # Выполняем поиск по паттерну
#     match = re.search(pattern, string) 
#     # Если совпадение, то...
#     if match: 
#         # То приваиваем в переменную first_word результат разделения по паттерну [r'\s+'], который позволяет выбрать только первые слова в строках
#         first_word = re.split(r'\s+', string.strip())[0]
#         m.append(first_word)

# flag = 0
# for string in m:
#     if string == 'launcher101xp.exe':
#         flag = 1
#         break

# if flag == 1:
#     print ('Задротит, бля')
# else:
#     print ("Не, не задротит")

# Закрываем соединение SSH
ssh.close()