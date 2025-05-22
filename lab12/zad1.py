import socket

HOST = '127.0.0.1'  # Lokalny adres IP
PORT = 65432        # Numer portu

# Tworzenie gniazda TCP (IPv4)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Serwer działa na {HOST}:{PORT}")

    conn, addr = server_socket.accept()
    with conn:
        print(f"Połączenie od: {addr}")
        while True:
            data = conn.recv(1024)       # Odbiór danych od klienta
            if not data:
                print("Rozłączenie klienta.")
                break
            print(f"Otrzymano: {data.decode()}")
            conn.sendall(data)           # Odesłanie tych samych danych
