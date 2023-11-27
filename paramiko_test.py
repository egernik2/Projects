import paramiko
import time

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname='192.168.0.20', username='User', password='12345rita', look_for_keys=False, allow_agent=False)
ssh = client.invoke_shell()
while True:
    cmd = input('Enter command: ')
    if cmd.lower() == 'exit':
        ssh.close()
        client.close()
        exit()
    elif cmd:
        ssh.send('{}\r'.format(cmd))
        time.sleep(0.2)
        result = ssh.recv(1024).decode()
        print(result)