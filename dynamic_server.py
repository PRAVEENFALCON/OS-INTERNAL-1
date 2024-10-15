import socket

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
server_address = ('localhost', 5000)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)
print("Server is listening on port 8080...")

# Wait for a connection
connection, client_address = server_socket.accept()
print(f"Connection established with {client_address}")

try:
    while True:
        # Receive the data from the client
        data = connection.recv(1024).decode()
        if data.lower() == 'exit':
            print("Client has closed the connection.")
            break
        print(f"Client: {data}")
        
        # Input message to send to the client
        response = input("Server (type 'exit' to close connection): ")
        connection.sendall(response.encode())
        
        # Check if the server wants to close the connection
        if response.lower() == 'exit':
            print("Server has closed the connection.")
            break

finally:
    # Clean up the connection
    connection.close()
    server_socket.close()
    print("Connection closed.")
