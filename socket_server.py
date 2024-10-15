import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 1234))  # Bind to the same address and port
    server_socket.listen(1)  # Listen for one connection
    print("Server is listening on port 1234...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr} has been established!")
        
        # Send initial message to client
        client_socket.sendall(b"Hello from server")

        # Receive message from client
        data = client_socket.recv(1024)
        print("Received from client:", data.decode('utf-8'))

        # Send response back to client
        response = "Message received!"
        client_socket.sendall(response.encode('utf-8'))
        client_socket.close()

if __name__ == "__main__":
    start_server()
