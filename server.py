import socket

# Define the host and port for the server
HOST = '192.168.1.178'  # You can use 'localhost' for local testing
PORT = 12345

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the host and port
server_socket.bind((HOST, PORT))

# Start listening for incoming connections
server_socket.listen()

print(f"Server is listening on {HOST}:{PORT}")

while True:
    # Accept incoming connections
    client_socket, client_address = server_socket.accept()

    print(f"Accepted connection from {client_address}")

    # Handle the client in a separate thread or function
    # Implement user authentication, messaging, and chat room logic here

    # Close the client socket when done
    client_socket.close()
