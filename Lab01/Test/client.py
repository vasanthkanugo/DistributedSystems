import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65345        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'{\"Header\":\"GET\", \"body\":{\"item_id\":123,\"quantity\":5}}')
    data = s.recv(1024)

print('Received', repr(data))