import socket
import threading

# Create socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 6060))

server.listen()

clients = []
usernames = {}

def broadcast(message, sender_socket=None):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message)
            except:
                client.close()
                clients.remove(client)

def handle_client(client):
    try:
        username = client.recv(1024).decode()
        usernames[client] = username
        welcome_msg = f"{username} has joined the chat!\n".encode()
        broadcast(welcome_msg, client)

        while True:
            msg = client.recv(1024)
            if msg:
                full_msg = f"{username}: {msg.decode()}\n".encode()
                broadcast(full_msg, client)
            else:
                break
    except:
        pass
    finally:
        clients.remove(client)
        broadcast(f"{usernames[client]} has left the chat!\n".encode())
        client.close()

print("Server running on 127.0.0.1:12345")
while True:
    client, addr = server.accept()
    clients.append(client)
    print(f"Connected with {addr}")
    thread = threading.Thread(target=handle_client, args=(client,))
    thread.start()
