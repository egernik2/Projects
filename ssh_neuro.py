import tkinter as tk
from tkinter import messagebox
import paramiko
import threading
import time

class SSHClientApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SSH Client")

        # IP Address
        self.ip_label = tk.Label(root, text="IP Address:")
        self.ip_label.grid(row=0, column=0, padx=5, pady=5)
        self.ip_entry = tk.Entry(root)
        self.ip_entry.grid(row=0, column=1, padx=5, pady=5)

        # Username
        self.username_label = tk.Label(root, text="Username:")
        self.username_label.grid(row=1, column=0, padx=5, pady=5)
        self.username_entry = tk.Entry(root)
        self.username_entry.grid(row=1, column=1, padx=5, pady=5)

        # Password
        self.password_label = tk.Label(root, text="Password:")
        self.password_label.grid(row=2, column=0, padx=5, pady=5)
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.grid(row=2, column=1, padx=5, pady=5)

        # Status Label
        self.status_label = tk.Label(root, text="Status: Not Connected", fg="red")
        self.status_label.grid(row=3, column=0, columnspan=2, pady=10)

        # Command Entry
        self.command_label = tk.Label(root, text="Command:")
        self.command_label.grid(row=4, column=0, padx=5, pady=5)
        self.command_entry = tk.Entry(root)
        self.command_entry.grid(row=4, column=1, padx=5, pady=5)

        # Output Text Area
        self.output_text = tk.Text(root, wrap='word', height=10, width=50, state=tk.DISABLED)
        self.output_text.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

        # Connect Button
        self.connect_button = tk.Button(root, text="Connect", command=self.connect)
        self.connect_button.grid(row=5, column=0, padx=5, pady=5)

        # Disconnect Button
        self.disconnect_button = tk.Button(root, text="Disconnect", command=self.disconnect, state=tk.DISABLED)
        self.disconnect_button.grid(row=5, column=1, padx=5, pady=5)

        # Execute Command Button
        self.execute_button = tk.Button(root, text="Execute Command", command=self.execute_command)
        self.execute_button.grid(row=7, column=0, columnspan=2, pady=10)

        self.ssh_client = None
        self.connected = False
        self.queue = []

    def connect(self):
        """
        Establishes an SSH connection using the provided IP address, username, and password.
        Updates the status label and button states upon a successful connection.
        Displays an error message if the connection attempt fails.
        """

        ip = self.ip_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        try:
            self.ssh_client = paramiko.SSHClient()
            self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh_client.connect(ip, username=username, password=password)
            self.status_label.config(text="Status: Connected", fg="green")
            self.connect_button.config(state=tk.DISABLED)
            self.disconnect_button.config(state=tk.NORMAL)
            self.connected = True
        except Exception as e:
            messagebox.showerror("Error", f"Failed to connect: {e}")

    def disconnect(self):
        if self.ssh_client:
            self.ssh_client.close()
        self.status_label.config(text="Status: Not Connected", fg="red")
        self.connect_button.config(state=tk.NORMAL)
        self.disconnect_button.config(state=tk.DISABLED)
        self.ssh_client = None
        self.connected = False
        self.clear_output()

    def execute_command(self):
        if not self.connected:
            return

        command = self.command_entry.get()
        if not command:
            return

        try:
            stdin, stdout, stderr = self.ssh_client.exec_command(command)
            self.print_output(stdout, stderr)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to execute command: {e}")

    def print_output(self, stdout, stderr):
        def read_output(stream):
            while not stream.channel.exit_status_ready():
                if stream.channel.recv_ready():
                    output = stream.read().decode('utf-8')
                    self.queue.append(output)
                time.sleep(0.1)

        thread_stdout = threading.Thread(target=read_output, args=(stdout,))
        thread_stderr = threading.Thread(target=read_output, args=(stderr,))

        thread_stdout.start()
        thread_stderr.start()

        self.update_output()

    def update_output(self):
        if self.queue:
            self.output_text.config(state=tk.NORMAL)
            for line in self.queue:
                self.output_text.insert(tk.END, line)
            self.output_text.see(tk.END)
            self.output_text.config(state=tk.DISABLED)
            self.queue.clear()

        self.root.after(100, self.update_output)

    def clear_output(self):
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete(1.0, tk.END)
        self.output_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = SSHClientApp(root)
    root.mainloop()