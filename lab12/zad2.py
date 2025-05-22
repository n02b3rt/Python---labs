import socket

HOST = '127.0.0.1'  # Lokalny adres IP
PORT = 65432        # Port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Serwer działa na {HOST}:{PORT}")

    conn, addr = server_socket.accept()
    with conn:
        print(f"Połączenie od: {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                print("Klient rozłączony.")
                break

            received_text = data.decode()
            print(f"Otrzymano: {received_text}")

            response = "Papuga mówi: " + received_text
            conn.sendall(response.encode())
            print(f"Wysłano: {response}")
