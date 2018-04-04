from socket import *
from UDP_App.Server import run_service  # import server functions
MAX_SIZE = 4096  # 512 bytes of data
IP_VERSION = AF_INET  # we will accept ipv4 addresses
TRANSPORT_PROTOCOL = SOCK_DGRAM  # UDP

# PROGRAM STARTS HERE!!
if __name__ == "__main__":
    sock = socket(IP_VERSION, TRANSPORT_PROTOCOL)  # creates socket with ipv4 and udp parameters
    sock.bind(('', 12345))  # local connection
    try:  # catch keyboard interrupt
        while True:  # repeat forever
            run_service(sock, MAX_SIZE,)  # run the service
    except KeyboardInterrupt:
        print("\nUDP Server terminated by user.")