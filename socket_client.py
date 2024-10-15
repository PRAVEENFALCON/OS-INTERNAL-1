import socket

def start_server():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 1234)
    server_socket.bind(server_address)
    
    # Listen for incoming connections
    server_socket.listen(1)
    print("Server is listening on port 1234...")
    
    while True:
        # Wait for a connection
        connection, client_address = server_socket.accept()
        try:
            print(f"Connection from {client_address}")
            
            # Send a welcome message to the client
            connection.sendall("Welcome to the server!".encode('utf-8'))
            
            # Receive the client's message
            data = connection.recv(1024)
            print(f"Received from client: {data.decode('utf-8')}")
            
            # Send a response back to the client
            response = "Thank you, client! Your message was received."
            connection.sendall(response.encode('utf-8'))
        
        finally:
            # Clean up the connection
            connection.close()

if __name__ == "__main__":
    start_server()
