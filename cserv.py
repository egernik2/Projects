import socket

sock = socket.socket()
sock.bind(('192.168.0.11', 9999))
sock.listen(1)
print('Server started')

conn, addr = sock.accept()
command = 'pwd'
conn.send(command.encode())
print('Command sended')
conn.close()

while True:
    conn, addr = sock.accept()
    print('New connection from {}'.format(addr[0]))
    msg = conn.recv(64000).decode()
    print('Recv message: {}\n'.format(msg))
    conn.close()