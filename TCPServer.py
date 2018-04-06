from socket import *
from time import ctime
from TCP_APP.Server import run_service

IP = 'localhost'  # The server's IP address
PORT = 12345  # Arbitrary port number
BUFFER_SIZE = 4096
ADDRESS = (IP, PORT)  # For readability purposes
TRANSPORT_PROTOCOL = SOCK_STREAM  # The TCP protocol
IP_FAM = AF_INET  # IPv4 family


if __name__ == '__main__':
    server = socket(IP_FAM, TRANSPORT_PROTOCOL)  # Create socket
    server.bind(ADDRESS)  # Bind to address
    server.listen(5)  # Accepts 5 connections
    # SOL_SOCKET is the level argument
    # SO_REUSEADDR,1 means permit use of local addresses for this socket
    server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    while True:  # Accept connections
        try:  # Catch the keyboard interrupt
            print("Server waiting for connection...")
            client_sock, addr = server.accept()  # accept a connection, receives a socket object and an address for it
            print(f"Client connected from {addr}, exchanging information now....")
            run_service(client_sock, BUFFER_SIZE, addr)  # runs the service
        except KeyboardInterrupt:
            print("\nExited by user")
            break

    server.close()
