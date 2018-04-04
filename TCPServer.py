from socket import *
from time import ctime

IP = "192.168.1.8"  # The server's IP address
PORT = 12365  # Arbitrary port number
BUFFER_SIZE = 1024  
ADDRESS = (IP, PORT)  # For readability purposes
TRANSPORT_PROTOCOL = SOCK_STREAM  # The TCP protocol
IP_FAM = AF_INET  # IPv4 family


if __name__ == '__main__':
    server_socket = socket(IP_FAM, TRANSPORT_PROTOCOL)
    server_socket.bind(ADDRESS)  # Bind to address
    server_socket.listen(5)  # Accepts 5 connections
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # SO_REUSE ADDR tells the kernel to reuse a local socket, without waiting for its natural timeout to expire

    while True:
        print("Server waiting for connection...")
        client_sock, addr = server_socket.accept()

        while True:
            data = client_sock.recv(BUFFER_SIZE)
            if not data or data.decode('utf-8') == 'END':
                break
            print(f"Received from client {data.decode('utf-8')}")
            print(f'Sending the server time to client: {ctime()}')
            try:
                client_sock.send(bytes(ctime(), 'utf-8'))
            except KeyboardInterrupt:
                print("Exited by user")
        client_sock.close()
    server_socket.close()