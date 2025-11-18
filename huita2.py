import socket

with socket.socket() as sock:
    sock.connect(('127.0.0.1', 9999))
    data = sock.recv(1024).decode()
    if data:
        print(data)