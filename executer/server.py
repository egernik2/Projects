import socket
import threading

def recv_message(conn):
    print(conn.recv(1024).decode())

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('192.168.0.11', 5000))
        s.listen()
        print('Server started!')
        while True:
            conn, addr = s.accept()
            print('{} connected!'.format(addr))
            thread = threading.Thread(target=recv_message, args=(conn, ), daemon=True)
            thread.start()
            msg = input()
            conn.sendall(msg).encode()

if __name__ == '__main__':
    main()