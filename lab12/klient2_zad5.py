import socket
import threading

HOST = '127.0.0.1'
PORT = 4123

def receive_messages(sock):
    while True:
        try:
            data = sock.recv(1024)
            if data:
                print(f"\n>> {data.decode()}")
            else:
                break
        except:
            break

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    print("Połączono z czatem. Możesz pisać wiadomości.")

    # Odbieranie w tle
    threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()

    while True:
        msg = input()
        if msg.lower() == 'exit':
            break
        client_socket.sendall(msg.encode())
