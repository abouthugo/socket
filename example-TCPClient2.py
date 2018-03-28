import socket
import sys

HOST = '192.168.1.5'
PORT = 80
BUFSIZ = 4096
ADDR = (HOST, PORT)

if __name__ == '__main__':
       client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       try:
        client_sock.connect(ADDR)
       except socket.error as error:
           print(f"Socket not created: {error}")
           sys.exit()

       while True:
           data = 'GET / HTTP/1.0\r\n\r\n'
           if not data:
               break
           client_sock.send(data.encode('utf-8'))
           data = client_sock.recv(BUFSIZ)
           if not data:
               break
           print(data.decode('utf-8'))

       client_sock.close()