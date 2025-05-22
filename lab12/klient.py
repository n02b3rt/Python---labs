import socket

HOST = '127.0.0.1'  # Adres IP serwera (localhost)
PORT = 65432        # Port serwera (taki sam jak w serwerze)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    print(f"Łączenie z serwerem {HOST}:{PORT}...")
    client_socket.connect((HOST, PORT))  # Połączenie z serwerem
    print("Połączono z serwerem!")

    while True:
        message = input("Wpisz wiadomość (lub 'exit' żeby zakończyć): ")
        if message.lower() == 'exit':
            print("Zamykanie połączenia.")
            break

        client_socket.sendall(message.encode())       # Wysyłanie wiadomości
        data = client_socket.recv(1024)               # Odbieranie odpowiedzi
        print(f"Odpowiedź serwera: {data.decode()}")
