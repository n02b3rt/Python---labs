import socket

HOST = '127.0.0.1'
PORT = 1243
OUTPUT_FILE = 'odebrany_plik.png'  # lub np. .txt
BUFFER_SIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Serwer TCP działa na {HOST}:{PORT}")

    conn, addr = server_socket.accept()
    with conn:
        print(f"Połączenie od: {addr}")
        with open(OUTPUT_FILE, 'wb') as f:
            while True:
                data = conn.recv(BUFFER_SIZE)
                if not data:
                    break
                f.write(data)
                print(f"Odebrano {len(data)} bajtów")

    print(f"Plik zapisany jako: {OUTPUT_FILE}")
