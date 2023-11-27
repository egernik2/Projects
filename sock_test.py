import socket

sock = socket.socket()
sock.bind(('192.168.0.11', 5555))
sock.listen()
print ('Сервер запущен')
conn, addr = sock.accept()
print ('Входящее подключение от {}'.format(addr))
while True:
    data = conn.recv(4096)
    print ('Получено сообщение: {}'.format(data))