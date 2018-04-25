from socket import *
import threading
import time
from TCP_APP.Server import run_service

IP = ''  # The server's IP address
PORT = 12345  # Arbitrary port number
BUFFER_SIZE = 4096  # size of receiving buffer
ADDRESS = (IP, PORT)  # For readability purposes
TRANSPORT_PROTOCOL = SOCK_STREAM  # The TCP protocol
IP_FAM = AF_INET  # IPv4 family
max_threads = 3  # Number of threads
p = 1
def print_msg():
    while p == 1:
        print('Current connections:' , threading.active_count()-3, end="\r")
        time.sleep(0.25)
# threading.active_count() gives the number of threads currently running

def work():
    while run_event.is_set():
        try:  # Catch the keyboard interrupt
            print("Server waiting for connection...")
            client_sock, addr = server.accept()  # accept a connection, receives a socket object and an address for it
            print(f"Client connected from {addr}, creating thread now....")
            thread_pool = threading.Thread(target=run_service, args=(client_sock, BUFFER_SIZE, addr))
            thread_pool.start()
            print(threading.active_count())
        except KeyboardInterrupt:
            run_event.clear()
            print("\nSever stopped by user")


if __name__ == '__main__':
    run_event = threading.Event()
    run_event.set()
    server = socket(IP_FAM, TRANSPORT_PROTOCOL)  # Create socket
    server.bind(ADDRESS)  # Bind to address
    server.listen(5)  # Accepts 5 connections
    # SOL_SOCKET is the level argument
    # SO_REUSEADDR,1 means permit use of local addresses for this socket
    server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    t = threading.Thread(target=print_msg, args=[])
    t.start()
    worker = threading.Thread(target=work, args=[])
    worker.start()  # start the server
    worker.join()  # come back when the server stops
    p = 0  # Stop printing number of connections
    server.close()

