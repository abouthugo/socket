from socket import socket, AF_INET, SOCK_DGRAM

MAX_SIZE = 4096  # this is how big the segment is(512 bytes)
PORT = 12345  # Arbitrary port number

if __name__ == "__main__":
    sock = socket(AF_INET, SOCK_DGRAM)  # create socket, pretty generic stuff.
    msg = 'Hello UDP server'  # initial message to send to server
    try:  # we need to catch the keyboard interrupt in case the user enters something stupid
        while True:  # run forever
            sock.sendto(msg.encode(), ('', PORT))  # Send the message, but encode it first
            # the function recvfrom(segmentSize) gives 2 variables back, thus the two variables
            # being declared at the same time
            data, addr = sock.recvfrom(MAX_SIZE)

            print('Server says: ')
            # remember that anything you receive through this connection is
            # encoded, gotta decode what you receive
            data = data.decode('utf-8')
            print(data)
            # print(repr(data))  # print the data received
            msg = input("Enter 1 for expression, otherwise anything for exit\n")
            if msg != '1':  # when the message is not 1 it means the user wants to quit
                msg = 'q'   # 'q' is used for quitting the connection at the server side
                sock.sendto(msg.encode(), ('', PORT))  # send the last msg to quit connection
                break  # break the while loop
            # else clause: when the user enters 1, he will then be prompted for an expression
            # to evaluate, and this expression will be sent and the process starts again.
            else:
                msg = input("Enter your expression: \n")
    except KeyboardInterrupt:  # EOF, whenever the user simply Ctrl-C from the program.
            print("\nExited")
    print("\nUDP Client terminated")