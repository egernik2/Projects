import npyscreen
import threading
import socket

class ChatApp(npyscreen.NPSApp):
    def main(self):
        ChatForm = npyscreen.Form(name="Npyscreen Chat")
        self.chat_widget = ChatForm.add(npyscreen.MultiLineEdit, 
                                    value="", 
                                    max_height=10, 
                                    editable=False)
        # Создаем виджет однострочного текста для ввода сообщения
        self.input_widget = ChatForm.add(npyscreen.TitleText, name="Enter message: ")

        # Создаем сокет для подключения к серверу
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('localhost', 5555))

        # Создаем поток для чтения сообщений с сервера
        self.receive_thread = threading.Thread(target=self.receive)
        self.receive_thread.start()
        ChatForm.edit()

    def receive(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode('ascii')
                self.chat_widget.value += message + '\n'
                self.display()
            except:
                self.client_socket.close()
                break

    def send_message(self):
        message = self.input_widget.value
        self.client_socket.send(message.encode('ascii'))
        self.input_widget.value = ""

    def while_editing(self, *args, **kwargs):
        # Переопределяем метод для обработки нажатий клавиш
        key_pressed = kwargs.get('input')
        if key_pressed in [10, 13]: # Если нажата клавиша "Enter"
            self.send_message()

if __name__ == '__main__':
    chatapp = ChatApp()
    chatapp.run()