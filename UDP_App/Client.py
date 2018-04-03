# This python file will be use to reference the function that both
# UDP and TCP servers will run

"""
The application:
    - Will send an expression to the server.
    - Checks if user wants to quit by checking if the data is the
    character 'q'.
    - Waits for a response from the server and receives the data if
    the server writes back, if not the timeout event will terminate
    the process.
    - Decodes and prints the result from the server
    - Waits for the user to enter a new expression and the process
    starts again.
"""
def run_service(sock, expression, destination, size):
    while True:
        sock.sendto(expression.encode(), destination)
        if expression.lower() == 'q':
            break
        response, destination = sock.recvfrom(size)
        response = response.decode('utf-8')
        print(f'Result: {response.strip()}')
        expression = input(">> ")   