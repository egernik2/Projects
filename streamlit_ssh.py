import streamlit as st
import paramiko
import pandas as pd
import threading
import json

data = {}
online_hosts = {}
# Функция для выполнения SSH-команды
def execute_ssh_command(hostname, username, password, command, decoding_char="UTF-8", need_result=False):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, username=username, password=password, timeout=30)
    try:
        stdin, stdout, stderr = ssh.exec_command(command)
        output = stdout.read().decode(decoding_char).strip()
        ssh.close()
        if need_result:
            return output
        else:
            data[hostname] = output
    except Exception as ex:
        data[hostname] = f'Ошибка: {ex}'

def ping_test(hostname, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostname, username=username, password=password, timeout=10)
        online_hosts[hostname] = True
        ssh.close()
    except Exception as ex:
        online_hosts[hostname] = False


st.title('Удаленное выполнение команды по SSH')

hostname = st.text_input('Укажите адрес удаленной машины', value="10.5.0.111")
username = st.text_input('Укажите имя пользователя', value="admin")
password = st.text_input('Укажите пароль', type='password', value='passw0rd')
command = st.text_input('Введите команду для выполнения', value='psql -U postgres mon_reports -tAc "select cipaddress from tnode;"')
checkbox = st.checkbox('Windows')

if st.button('Выполнить команду по SSH'):
    if hostname and username and password and command:
        try:
            table = pd.DataFrame()
            if checkbox:
                output = execute_ssh_command(hostname, username, password, command, decoding_char="CP866", need_result=True)
                st.text_area(value=output, label='Вывод', height=600)
            else:
                ips = execute_ssh_command(hostname, username, password, command, need_result=True).split('\n')
                with open("C:/Users/lordr/Desktop/stend_ip_list.txt", 'w') as f:
                    for ip in ips:
                        f.write(f'{ip}\n')
                st.text(f'Адреса получены. Проверяю на онлайн. Всего узлов {len(ips)}')
                
                # Online check
                threads = []
                for host in ips:
                    thread = threading.Thread(target=ping_test, args=(host, username, password))
                    threads.append(thread)
                for thread in threads:
                    thread.start()
                for thread in threads:
                    thread.join()
                
                st.text(f"Онлайн узлов: {len(online_hosts)}")
                online_json = json.dumps(online_hosts)
                st.json(online_json)

                # PID check
                threads = []
                for ip in online_hosts:
                    thread = threading.Thread(target=execute_ssh_command, args=(ip, username, password, 'systemctl status valhalla | grep "Main PID"'))
                    threads.append(thread)
                for thread in threads:
                    thread.start()
                for thread in threads:
                    thread.join()
                data_json = json.dumps(data)
                st.json(data_json)
        except Exception as e:
            st.error(f'Произошла ошибка при выполнении команды: {str(e)}')
    else:
        st.warning('Пожалуйста, заполните все поля')