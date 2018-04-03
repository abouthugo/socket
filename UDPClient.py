from socket import *
from UDP_App.Client import run_service  # import client function
MAX_SIZE = 4096  # this is how big the segment is(512 bytes)
PORT = 12345  # Arbitrary port number
IP = ''  # since its local connection this is an empty string
TRANSFER_PROTOCOL = SOCK_DGRAM  # the protocol used here is UDP
IP_VERSION = AF_INET  # the IP version used for the connection is ipv4


# PROGRAM STARTS HERE:
if __name__ == "__main__":
    sock = socket(IP_VERSION, TRANSFER_PROTOCOL)  # create socket with (ipv4 address AND UDP connection)
    msg = 'Hello UDP server'  # initial message to send to server
    sock.settimeout(2)  # set the timer in case no connection is being received
    sock.sendto(msg.encode(), (IP, PORT))  # Send the encoded message to destination(IP, PORT)
    try:  # catch the timeout event
        data, source = sock.recvfrom(MAX_SIZE)  # receive data and source IP
        data = data.decode('utf-8')  # remember that data comes in bytes, always decode it!
        print(f'Server says: \n{data}')  # Print the response got from the server
        try:  # we need to catch the keyboard interrupt in case the user causes it
            msg = input("Enter your expression or \'q\' to exit\n")  # get input to send
            run_service(sock, msg, source, MAX_SIZE)  # run the application
            print("UDP Client terminated by user")  # message to print when application is finalized
        except KeyboardInterrupt:  # EOF, whenever the user simply Ctrl-C from the program.
            print('\nUDP Client terminated by keyboard interruption.')
            sock.sendto('q'.encode(), (IP, PORT))  # when keyboard interrupts tell the server
    except timeout:
        print('Connection lost')