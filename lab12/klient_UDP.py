import socket

HOST = '127.0.0.1'  # IP serwera
PORT = 1234        # Port serwera

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
    while True:
        message = input("Wpisz wiadomość (lub 'exit' żeby zakończyć): ")
        if message.lower() == 'exit':
            print("Zamykanie klienta.")
            break

        client_socket.sendto(message.encode(), (HOST, PORT))  # Wysyłka do serwera
        data, server_address = client_socket.recvfrom(1024)   # Odbiór odpowiedzi
        print(f"Odpowiedź serwera: {data.decode()}")
