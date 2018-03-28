from socket import *
import socket
import sys


if __name__ == '__main__':
    try:
        s = socket.socket(family=AF_INET, type=SOCK_STREAM, proto=0)
    except socket.error as err:
        print("Failed to create socket")
        print(f"Reason: {err}")
        sys.exit()

    print("Success! Socket created")

    target_host = input("Enter the name of your target host name: ")
    target_port = input("Enter socket number: ")

    try:
        s.connect((target_host, int(target_port)))
        print(f"Socket Connected to {target_host} on port: {target_port}")
        s.shutdown(2)
    except socket.error as error:
        print(f"Faled to connect to {target_host} on port: {target_port}")
        print(f"Reason: {error}")
        sys.exit()