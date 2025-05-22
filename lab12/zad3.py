import socket

HOST = '127.0.0.1'  # Adres IP, na którym serwer będzie nasłuchiwał
PORT = 1234        # Port

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
    server_socket.bind((HOST, PORT))  # UDP nie używa listen() ani accept()
    print(f"Serwer UDP działa na {HOST}:{PORT}")

    while True:
        data, client_address = server_socket.recvfrom(1024)  # Odbiór danych i adresu nadawcy
        print(f"Otrzymano od {client_address}: {data.decode()}")

        response = "Papuga mówi: " + data.decode()
        server_socket.sendto(response.encode(), client_address)  # Odesłanie odpowiedzi
        print(f"Wysłano do {client_address}: {response}")
