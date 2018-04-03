import socket

HOST = 'www.google.com'  # or 'localhost'
PORT = 80  # port for the web
BUFSIZ = 4096  # receive 512 bytes worth of data
ADDR = (HOST, PORT)  # make address variable
if __name__ == '__main__':
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_sock.connect(ADDR)  # connect socket to address
    while True:
        data = 'GET / HTTP/1.0\r\n\r\n'
        if not data:
            break
        client_sock.send(data.encode('utf-8'))  # send HTTP request
        data = client_sock.recv(BUFSIZ)
        if not data:
            break
        print(data.decode('utf-8'))
    client_sock.close()