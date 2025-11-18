import socket
import threading

class MessengerClient:
    def __init__(self, host='37.204.60.234', port=12345):
        self.host = host
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.nickname = input('Enter your nickname: ')

    def start(self):
        self.client.connect((self.host, self.port))
        print('Connected to server')
        receive_thread = threading.Thread(target=self.receive_messages)
        receive_thread.start()
        while True:
            message = input('Enter message: ')
            self.send_message(f'{self.nickname}: {message}')

    def send_message(self, message):
        self.client.sendall(message.encode('utf-8'))

    def receive_messages(self):
        while True:
            try:
                message = self.client.recv(1024).decode('utf-8')
                print(message)
            except Exception as e:
                print(e)
                break

if __name__ == '__main__':
    client = MessengerClient()
    client.start()