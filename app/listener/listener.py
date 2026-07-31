import socket

HOST = "0.0.0.0"
PORT = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"Listening on {HOST}:{PORT}...")

while True:
    client_socket, client_address = server.accept()
    print(f"Accepted connection from {client_address}")

    data = client_socket.recv(1024)
    if not data:
        break

    print(f"Received data: {data.decode('utf-8')}")

    response = "Data received"
    client_socket.sendall(response.encode('utf-8'))

    client_socket.close()