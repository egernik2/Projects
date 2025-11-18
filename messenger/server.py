import socket
import threading

class MessengerServer:
    def __init__(self, host='192.168.0.11', port=12345):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
        self.server.listen()
        self.clients = []
        self.nicknames = []

    def start(self):
        print('Server started')
        while True:
            client_socket, addr = self.server.accept()
            print(f'{addr} connected')
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()

    def handle_client(self, client_socket):
        while True:
            try:
                message = client_socket.recv(1024).decode('utf-8')
                if not message:
                    break
                if message.startswith('NICKNAME:'):
                    nickname = message[9:]
                    self.nicknames.append(nickname)
                    self.clients.append(client_socket)
                    print(f'{nickname} joined the chat')
                    # отправляем сообщение всем клиентам о подключении нового пользователя
                    for client in self.clients:
                        if client != client_socket:
                            try:
                                client.sendall(f'SYSTEM:{nickname} joined the chat'.encode('utf-8'))
                            except:
                                self.clients.remove(client_socket)
                                self.nicknames.remove(self.get_nickname(client_socket))
                                client.sendall(f'SYSTEM:{self.get_nickname(client_socket)} left the chat'.encode('utf-8'))
                                print(f'{self.get_nickname(client_socket)} left the chat')
                    client_socket.sendall(''.encode('utf-8'))
                    break
                else:
                    client_socket.sendall('Invalid message format'.encode('utf-8'))
            except ConnectionResetError:
                break
            except Exception as e:
                print(f"Error handling client: {e}")
                break

        while True:
            try:
                message = client_socket.recv(1024).decode('utf-8')
                if not message:
                    break
                if message.startswith('MESSAGE:'):
                    message = message[8:]
                    sender_nickname = self.get_nickname(client_socket)
                    print(f'{sender_nickname}: {message}')
                    # отправляем сообщение всем клиентам, кроме отправителя
                    for client in self.clients:
                        if client != client_socket:
                            client.sendall(f'MESSAGE:{sender_nickname}: {message}'.encode('utf-8'))
            except ConnectionResetError:
                break
            except Exception as e:
                print(f"Error receiving message: {e}")
                break

    def get_nickname(self, client_socket):
        return self.nicknames[self.clients.index(client_socket)]

if __name__ == '__main__':
    server = MessengerServer()
    server.start()
