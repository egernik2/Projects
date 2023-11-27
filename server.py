import socket
import threading

HOST = 'localhost'
PORT = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            clients.remove(client)
            client.close()
            print (f'{client} disconnected')
            break

def receive():
    while True:
        client, address = server.accept()
        clients.append(client)
        print(f'Connected with {str(address)}')

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

receive()
