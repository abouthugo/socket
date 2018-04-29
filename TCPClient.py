from socket import *  # import variables and functions from socket library
from TCP_APP.Client import client_send  # import function
import sys
DEFAULT_IP = ''  # The server's IP address, change when accessed remotely
DEFAULT_PORT = 12345  # Arbitrary port number
BUFFER_SIZE = 4096  # 512 bytes of data
DEFAULT_ADDRESS = (DEFAULT_IP, DEFAULT_PORT)  # For readability purposes
TRANSPORT_PROTOCOL = SOCK_STREAM  # The TCP protocol
IP_FAM = AF_INET  # IPv4 family

if __name__ == '__main__':
    client = socket(IP_FAM, TRANSPORT_PROTOCOL)  # Create socket
    try:  # try to connect and catch exception
        client.connect(DEFAULT_ADDRESS)  # Connect to server
    except ConnectionRefusedError as e:
        print('Connection refused ')
        sys.exit(0)
    msg = input('Enter an expression or \'q\' for exit\n>> ')  # initial message for the user
    try:  # catch the keyboard interrupt exception
        if msg != 'q':
            client_send(client, msg, BUFFER_SIZE)  # run service
        print('Bye!')
    except KeyboardInterrupt:
        print("\nExited by user")
    client.close()  # close connection
