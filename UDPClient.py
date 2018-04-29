from socket import *
from UDP_App.Client import run_service  # import client function
MAX_SIZE = 4096  # this is how big the segment is(512 bytes)
PORT = 12346  # Arbitrary port number
# IP = '192.168.1.13'  # Linux's machine home IP address
# IP = '192.168.1.8'  # Mac's IP home address
IP = ''
TRANSPORT_PROTOCOL = SOCK_DGRAM  # the protocol used here is UDP
IP_FAM = AF_INET  # the IP version used for the connection is ipv4


# PROGRAM STARTS HERE:
if __name__ == "__main__":
    sock = socket(IP_FAM, TRANSPORT_PROTOCOL)  # create socket with (ipv4 address AND UDP connection)
    try:  # we need to catch the keyboard interrupt in case the user causes it
        expression = input("Enter your expression or \'q\' to exit\n>> ")  # get input to send
        run_service(sock, expression, (IP, PORT), MAX_SIZE)  # run the application
        print("Bye!")  # message to print when application is finalized
    except KeyboardInterrupt:  # EOF, whenever the user simply Ctrl-C from the program.
        print('\nUDP Client terminated by keyboard interruption.')
        sock.sendto('q'.encode(), (IP, PORT))  # when keyboard interrupts tell the server
