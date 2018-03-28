import socket
from time import ctime

HOST = "192.168.1.5"
PORT = 12345
BUFSIZ = 1024
ADDR = (HOST, PORT)

if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(ADDR) #Bind to addres(HOST,PORT)
    server_socket.listen(5) #Accepts 5 connections
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    #SO_REUSEADDR tells the kernel to reuse a local socket, without waiting for its natural timeout to expire

    while True:
        print("Server waiting for connection...")
        client_sock, addr = server_socket.accept()

        while True:
            data = client_sock.recv(BUFSIZ)
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