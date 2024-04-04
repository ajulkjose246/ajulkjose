import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(2)
result = sock.connect_ex(("google.com", 80))
if result == 0:
    print(f"Port google.com on 80 is OPEN")
else:
    print(f"Port google.com on 80 is CLOSED")