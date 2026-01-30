import socket


def start_server():
    host = "127.0.0.1"
    port = 65432
    AUTH_TOKEN = "SECRET_123"

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}...")

    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    try:
       
        client_token = conn.recv(1024).decode()
        if client_token == AUTH_TOKEN:
            conn.send("AUTH_SUCCESS".encode())
            print("Client authenticated successfully.")

            # Step 2: Message Exchange
            while True:
                data = conn.recv(1024).decode()
                if not data or data.lower() == "exit":
                    break
                print(f"Received from client: {data}")
                conn.send(f"Server received: {data}".encode())
        else:
            conn.send("AUTH_FAILED".encode())
            print("Authentication failed. Closing connection.")

    finally:
        conn.close()
        server_socket.close()


if __name__ == "__main__":
    start_server()
