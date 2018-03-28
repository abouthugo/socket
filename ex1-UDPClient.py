from socket import *

MAX_SIZE = 4096  # this is how big the segment is(512 bytes)
PORT = 12345  # Arbitrary port number


def compute_service(expression):
    while True:
        sock.sendto(expression.encode(), ('', PORT))
        if expression == 'q':
            break
        response, destination = sock.recvfrom(MAX_SIZE)
        response = response.decode('utf-8')
        print(f'Result: {response.strip()}')
        expression = input(">>")


if __name__ == "__main__":
    sock = socket(AF_INET, SOCK_DGRAM)  # create socket with (ipv4 address AND UDP connection)
    msg = 'Hello UDP server'  # initial message to send to server
    sock.settimeout(2)  # set the timer in case no connection is being received
    sock.sendto(msg.encode(), ('', PORT))  # Send the encoded message to PORT
    # the function recvfrom(segmentSize) gives 2 variables back, thus the two variables
    # being declared at the same time
    try:
        data, addr = sock.recvfrom(MAX_SIZE)
        # remember that anything you receive through this connection is
        # encoded, gotta decode what you receive
        data = data.decode('utf-8')
        print(f'Server says: \n{data}')  # Print the response back from the server
        try:  # we need to catch the keyboard interrupt in case the user case the user
            msg = input("Enter your expression or \'q\' to exit\n")
            compute_service(msg)
            print("UDP Client terminated by user")
        except KeyboardInterrupt:  # EOF, whenever the user simply Ctrl-C from the program.
            print('\nUDP Client terminated by keyboard interruption.')
    except timeout:
        print('Connection lost')