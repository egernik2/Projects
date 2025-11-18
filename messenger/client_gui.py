import socket
import threading
import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk

class MessengerClient:
    def __init__(self, host='37.204.60.234', port=12345):
        self.host = host
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.settimeout(5)  # добавляем тайм-аут на ожидание ответа от сервера
        self.nickname = None
        self.connected = False

    def start(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        self.app = ctk.CTk()
        self.app.title("Messenger")
        self.app.geometry("1280x960")
        self.app.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.nickname_label = ctk.CTkLabel(self.app, text="Enter your nickname:")
        self.nickname_label.pack(pady=(100, 10), padx=(50, 50))

        self.nickname_entry = ctk.CTkEntry(self.app)
        self.nickname_entry.pack(pady=(10, 10), padx=(50, 50))

        self.connect_button = ctk.CTkButton(self.app, text="Connect", command=self.connect)
        self.connect_button.pack(pady=(10, 10), padx=(50, 50))

        self.messages_textbox = ctk.CTkTextbox(self.app, height=600, state='disabled')
        self.messages_textbox.pack(pady=(10, 10), padx=(50, 50), expand=True, fill='both')

        self.message_entry = ctk.CTkEntry(self.app, state='disabled')
        self.message_entry.pack(pady=(10, 10), padx=(50, 50), expand=True, fill='x')
        self.message_entry.bind('<Return>', self.send_message)

        self.send_button = ctk.CTkButton(self.app, text="Send", command=self.send_message, state='disabled')
        self.send_button.pack(pady=(10, 10), padx=(50, 50))

        self.app.mainloop()

    def on_closing(self):
        if self.connected:
            self.client.shutdown(socket.SHUT_WR)
            self.client.close()
        self.app.destroy()
        exit()

    def connect(self):
        self.nickname = self.nickname_entry.get()
        if not self.nickname:
            messagebox.showerror("Error", "Please enter a nickname")
            return
        try:
            self.client.connect((self.host, self.port))
            self.client.sendall(f'NICKNAME:{self.nickname}'.encode('utf-8'))
            messagebox.showinfo("Success", "Connected to server")
            self.connected = True
            self.message_entry.configure(state='normal')
            self.send_button.configure(state='normal')
            receive_thread = threading.Thread(target=self.receive_messages)
            receive_thread.start()
        except socket.timeout:
            messagebox.showerror("Error", "Could not connect to server. Please check your connection and try again.")
        except Exception as e:
            messagebox.showerror("Error", f"Cannot connect to server: {str(e)}")

    def send_message(self, event=None):
        if not self.connected:
            return
        message = self.message_entry.get()
        if message:
            try:
                self.client.sendall(f'MESSAGE:{message}'.encode('utf-8'))
                self.messages_textbox.configure(state='normal')
                self.messages_textbox.insert('end', f'{self.nickname}: {message}\n')  # добавление сообщения в поле текста
                self.messages_textbox.see('end')
                self.messages_textbox.configure(state='disabled')
                self.message_entry.delete(0, 'end')
            except Exception as e:
                messagebox.showerror("Error", f"Cannot send message: {str(e)}")
                self.connected = False
                self.message_entry.configure(state='disabled')
                self.send_button.configure(state='disabled')

    def receive_messages(self):
        while self.connected:
            try:
                message = self.client.recv(1024).decode('utf-8')
                if message.startswith('MESSAGE:'):
                    message = message[8:]
                    self.messages_textbox.configure(state='normal')
                    self.messages_textbox.insert('end', message + '\n')
                    self.messages_textbox.see('end')
                    self.messages_textbox.configure(state='disabled')
                if message.startswith('SYSTEM:'):
                    message = message[7:]
                    self.messages_textbox.configure(state='normal')
                    self.messages_textbox.insert('end', message + '\n')
                    self.messages_textbox.see('end')
                    self.messages_textbox.configure(state='disabled')
            except socket.timeout:
                pass
            except Exception as e:
                messagebox.showerror("Error", f"Cannot receive messages: {str(e)}")
                self.connected = False
                break

if __name__ == '__main__':
    client = MessengerClient()
    client.start()
