import socket

def send_data_to_echo_server(host, port, message):
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the echo server
    client_socket.connect((host, port))

    # Send data to the server
    client_socket.sendall(message.encode('utf-8'))

    # Receive and print the echoed data
    data = client_socket.recv(1024)
    print(f"Received from server: {data.decode('utf-8')}")

    # Close the connection with the server
    client_socket.close()

if __name__ == "__main__":
    # Set the host and port for the echo server
    server_host = "127.0.0.1"  # localhost
    server_port = 12345

    # Message to be echoed
    message_to_echo = "Hello, Echo Server!"

    # Send data to the echo server
    send_data_to_echo_server(server_host, server_port, message_to_echo)
