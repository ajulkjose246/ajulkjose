import socket

def start_echo_server(host, port):
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific address and port
    server_socket.bind((host, port))

    # Listen for incoming connections (max 5 connections in the queue)
    server_socket.listen(5)
    print(f"Echo server is listening on {host}:{port}")

    while True:
        # Wait for a connection from a client
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")

        # Receive and send back data in chunks
        data = client_socket.recv(1024)
        while data:
            print(f"Received data: {data.decode('utf-8')}")
            client_socket.send(data)
            data = client_socket.recv(1024)

        # Close the connection with the client
        client_socket.close()
        print(f"Connection with {client_address} closed")

if __name__ == "__main__":
    # Set the host and port for the echo server
    host = "127.0.0.1"  # localhost
    port = 12345

    # Start the echo server
    start_echo_server(host, port)
