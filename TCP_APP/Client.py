"""
This function will take 3 parameters:
    - Socket where communication will be maintained
    - Message to send to the socket
    - Size of every message to be sent
Beta mode

"""
def client_send(socket, msg, size):
    while True:
        socket.send(msg.encode('utf-8'))
        result = socket.recv(size)
        print(result.decode('utf-8'))
        msg = input('>> ')
        if msg.lower() == 'q':
            break
