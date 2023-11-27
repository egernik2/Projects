import npyscreen
import socket
import threading

class ChatApp(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm("MAIN", MainForm, name="Chat Room")

class MainForm(npyscreen.Form):
    def create(self):
        self.add(npyscreen.TitleFixedText, name="Welcome to the chat room!", editable=False)
        self.chat_widget = self.add(npyscreen.MultiLineEdit, max_height=20, rely=3, editable=False)
        self.message_widget = self.add(npyscreen.TitleText, name="Message:", rely=23)
        self.status_widget = self.add(npyscreen.FixedText, value="Not connected to server", editable=False)

    def on_ok(self):
        message = self.message_widget.value
        self.message_widget.value = ""
        self.chat_widget.value += "You: {}\n".format(message)
        self.chat_widget.display()

    def on_cancel(self):
        self.parentApp.switchForm(None)

def receive_messages(sock, chat_widget):
    while True:
        try:
            message = sock.recv(1024).decode()
            chat_widget.value += message + "\n"
            chat_widget.display()
        except:
            break

def connect_to_server(ip_address, port, chat_widget, status_widget):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip_address, port))
        status_widget.value = "Connected to server"
        status_widget.display()
        threading.Thread(target=receive_messages, args=(sock, chat_widget)).start()
        return sock
    except:
        status_widget.value = "Error connecting to server"
        status_widget.display()
        return None

def send_message(sock, message):
    try:
        sock.sendall(message.encode())
    except:
        pass

def handle_input(input_widget, sock):
    message = input_widget.value
    if message:
        send_message(sock, message)
        input_widget.value = ""

def setup_input_handler(input_widget, sock):
    input_widget.handlers.update({
        "^M": lambda x: handle_input(input_widget, sock),
        "^J": lambda x: handle_input(input_widget, sock)
    })

if __name__ == "__main__":
    app = ChatApp()
    ip_address = input("Enter server IP address: ")
    port = int(input("Enter server port: "))
    main_form = app.getForm('MAIN')
    chat_widget = main_form.chat_widget
    status_widget = main_form.status_widget
    sock = connect_to_server(ip_address, port, chat_widget, status_widget)
    if sock:
        input_widget = main_form.message_widget
        setup_input_handler(input_widget, sock)
        app.run()