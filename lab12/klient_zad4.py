import socket

HOST = '127.0.0.1'
PORT = 1243
INPUT_FILE = 'zdjecie.png'  # lub np. .txt
BUFFER_SIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    print("Połączono z serwerem. Wysyłanie pliku...")

    with open(INPUT_FILE, 'rb') as f:
        while chunk := f.read(BUFFER_SIZE):
            client_socket.sendall(chunk)
            print(f"Wysłano {len(chunk)} bajtów")

    print("Plik wysłany.")
