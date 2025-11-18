import socket
from datetime import datetime
from threading import Thread

sock = socket.socket()
sock.bind(('127.0.0.1', 9999))
sock.listen()
print('Server started')

def listening():
    while True:
        conn, addr = sock.accept()
        print(f'{addr[0]} connected')
        conn.sendall(str(datetime.now()).encode())
        conn.close()
        print(f'{addr[0]} disconnected')

thread = Thread(target=listening, daemon=True)
thread.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    print('Server stop!')
    sock.close()
    exit()