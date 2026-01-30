import socket


def start_client():
    host = "127.0.0.1"
    port = 65432
    token = "SECRET_123"  
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    
    client_socket.send(token.encode())
    auth_response = client_socket.recv(1024).decode()

    if auth_response == "AUTH_SUCCESS":
        print("Authenticated! You can now send messages.")
        while True:
            msg = input("Enter message (or 'exit'): ")
            client_socket.send(msg.encode())
            if msg.lower() == "exit":
                break
            response = client_socket.recv(1024).decode()
            print(f"Server says: {response}")
    else:
        print("Connection rejected: Invalid Token.")

    client_socket.close()


if __name__ == "__main__":
    start_client()
