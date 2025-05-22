import socket
import threading
from datetime import datetime

HOST = '127.0.0.1'
PORT = 4123

clients = []

def handle_client(conn, addr):
    print(f"Nowe połączenie: {addr}")
    clients.append(conn)

    try:
        while True:
            msg = conn.recv(1024)
            if not msg:
                break
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            message_with_time = f"[{timestamp}] {msg.decode()}"
            broadcast(message_with_time.encode(), conn)
    finally:
        print(f"Rozłączono: {addr}")
        clients.remove(conn)
        conn.close()

def broadcast(message, sender_conn):
    for client in clients:
        if client != sender_conn:
            client.sendall(message)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Serwer czatu działa na {HOST}:{PORT}")

    while True:
        conn, addr = server_socket.accept()
        threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()
