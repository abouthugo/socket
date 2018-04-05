from socket import *

DEFAULT_IP = "localhost"  # The server's IP address, change when accessed remotely
DEFAULT_PORT = 12345  # Arbitrary port number
BUFFER_SIZE = 4096
DEFAULT_ADDRESS = (DEFAULT_IP, DEFAULT_PORT)  # For readability purposes
TRANSPORT_PROTOCOL = SOCK_STREAM  # The TCP protocol
IP_FAM = AF_INET  # IPv4 family

if __name__ == '__main__':
    client = socket(IP_FAM, TRANSPORT_PROTOCOL)  # Create socket
    try:
        client.connect(DEFAULT_ADDRESS)  # Connect to server
    except ConnectionRefusedError as e:
        print('Connection refused')
    payload = 'GET TIME'
    try:
        while True:
            client.send(payload.encode('utf-8'))  # send data encoded
            data = client.recv(BUFFER_SIZE)  # receive response from server
            print(repr(data))  # print the string representation of the time object
            more = input("Want to send more data to the server? [y/n]: ")  # ask user for more data
            if more.lower() == 'y':
                payload = input("Enter payload: ")
            else:
                break
    except KeyboardInterrupt:
        print("Exited by user")
    client.close()  # close connection
