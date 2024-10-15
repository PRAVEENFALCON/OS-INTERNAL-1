import socket

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 8080)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)
print("Server is listening on port 8080...")

while True:
    # Wait for a connection
    connection, client_address = server_socket.accept()
    try:
        print(f"Connection from {client_address}")
        
        while True:
            # Receive the data from the client
            data = connection.recv(1024).decode()
            if data:
                print(f"Client: {data}")
                if data.lower() == 'exit':
                    print("Client has closed the connection.")
                    break
                # Send a response to the client
                response = input("Server (type 'exit' to close connection): ")
                connection.sendall(response.encode())
                if response.lower() == 'exit':
                    print("Server has closed the connection.")
                    break
            else:
                break
    finally:
        # Clean up the connection
        connection.close()
