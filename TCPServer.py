from socket import *
import threading
import time
import sys
from tcp_helper.Server import run_service

IP = ''  # The server's IP address
PORT = 12345  # Arbitrary port number
BUFFER_SIZE = 4096  # size of receiving buffer
ADDRESS = (IP, PORT)  # For readability purposes
TRANSPORT_PROTOCOL = SOCK_STREAM  # The TCP protocol
IP_FAM = AF_INET  # IPv4 family
max_threads = 3  # Number of threads
p = 1

def work(event):
    while event.is_set():
        print("Server waiting for connection...")
        try:
            client_sock, addr = server.accept()  # accept a connection, receives a socket object and an address for it
        except ConnectionAbortedError as e:
            print("Threads closed...")
            if 'client_sock' in locals():
                client_sock.close()
            break
        print(f"Client connected from {addr}, creating thread now....")
        thread_pool = threading.Thread(target=run_service, args=(client_sock, BUFFER_SIZE, addr, event))
        thread_pool.start()
        print(threading.active_count())


if __name__ == '__main__':
    run_event = threading.Event()
    run_event.set()
    server = socket(IP_FAM, TRANSPORT_PROTOCOL)  # Create socket
    server.bind(ADDRESS)  # Bind to address
    server.listen(5)  # Accepts 5 connections
    # SOL_SOCKET is the level argument
    # SO_REUSEADDR,1 means permit use of local addresses for this socket
    server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    # t = threading.Thread(target=print_msg, args=[run_event])
    # t.start()
    worker = threading.Thread(target=work, args=[run_event])
    worker.start()  # start the server
    try:
        while run_event.is_set():
            print('Current connections:', threading.active_count() - 2, end="\r")
            time.sleep(0.25)
    except KeyboardInterrupt as e:
        run_event.clear()  # Stop the thread at keyboard interrupt
        print("\nSever stopped by user")
        server.close()
        sys.exit(0)