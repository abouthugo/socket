from socket import *
from time import ctime

IP = 'localhost'  # The server's IP address
PORT = 12345  # Arbitrary port number
BUFFER_SIZE = 4096
ADDRESS = (IP, PORT)  # For readability purposes
TRANSPORT_PROTOCOL = SOCK_STREAM  # The TCP protocol
IP_FAM = AF_INET  # IPv4 family


if __name__ == '__main__':
    server = socket(IP_FAM, TRANSPORT_PROTOCOL)
    server.bind(ADDRESS)  # Bind to address
    server.listen(5)  # Accepts 5 connections
    # SOL_SOCKET is the level argument
    # SO_REUSEADDR,1 means permit use of local addresses for this socket
    server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    while True:
        try:
            print("Server waiting for connection...")
            client_sock, addr = server.accept()  # accept a connection, receives a socket object and an address for it
            print(f"Client connected from {addr}")
            while True:
                data = client_sock.recv(BUFFER_SIZE)  # prepare to receive
                if not data or data.decode('utf-8') == 'END':
                    break
                print(f"Received from client {data.decode('utf-8')}")
                print(f'Sending the server time to client: {ctime()}')
                client_sock.send(bytes(ctime(), 'utf-8'))
        except KeyboardInterrupt:
            print("\nExited by user")
            break
        client_sock.close()
    server.close()
