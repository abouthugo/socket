import socket
import sys

HOST = '192.168.1.5'
PORT = 12345
BUFSIZ = 256
ADDR = (HOST, PORT)

if __name__ == '__main__':
       client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       try:
        client_sock.connect(ADDR)
       except socket.error as error:
           print(f"Socket not created: {error}")
           sys.exit()

       payload = 'GET TIME'
       try:
           while True:
               client_sock.send(payload.encode('utf-8'))
               data = client_sock.recv(BUFSIZ)
               print(repr(data))
               more = input("Want to send more data to the server? [y/n]: ")
               if more.lower() == 'y':
                   payload = input("Enter payload: ")
               else:
                   break
       except KeyboardInterrupt:
           print("Exited by user")

       client_sock.close()