from socket import *
MAX_SIZE = 4096  # 512 bytes of data
IP_VERSION = AF_INET  # we will accept ipv4 addresses
TRANSPORT_PROTOCOL = SOCK_DGRAM  # UDP


"""
The compute function:
    - Defines an array of valid operands that a client might use. Called [operands]
    - Creates a copy of the string passed in into an array. Called [array]
    - Flush out the previous value for the string passed in [y]. 
    - Loop through the array for validation:
        - if the character at index (s) is in [operands] or is a period or is a digit
            then we add that character to the empty string
    Notice that when we do not add a character we might encounter Syntax errors
    For example if user enters "3*c+d" the array will return "3*+" and when the
    eval() function is called it will result in a Syntax error.
    Similarly in other instances it could result in an EOF error, thus we surround the
    last steps with a try-catch clause
    - We first try to evaluate the string and test if the result is a float
        - If it is a float
            then: format the string to only have 2 decimals and
                  report back to the program that called the function.
            else: simply evaluate the string and report back to the program
                  that called the function
    - When the program encounters an exception it reports to the user that 
    the expression entered was invalid. 
"""


def compute(y):
    operands = ['+', '-', '*', '/', '**', '%', '(', ")", "^"]
    expr = [letter for letter in y]
    y = ''
    for s in expr:
        if s in operands or s == '.' or type(s) == int or s.isdigit():
            if s == '^':  # User might be allowed to enter '^'
                s = '**'  # and it will be interpreted as '**'
            y += str(s)
    try:
        if isinstance(eval(y), float):
            y = f'{eval(y):.2f}'
            if '.00' in y:  # trimming purposes
                y = y.split('.')[0]
            return y
        else:
            return str(eval(y))
    except (SyntaxError, EOFError):
        y = f'\tYour expression is invalid, you can only use operands: \n\t{operands} and digits 0-9'
        return y


"""
The run_service function...
    - Wait for data from client, the source ip becomes the destination ip
    - Decode data and check if user wants to quit
    - Manipulate the data and execute the compute function on the data received
    - Encode the result and send to destination
    - If user exists print a message to let the server know
"""
def run_service(s):
    while True:
        expression, destination = s.recvfrom(MAX_SIZE)
        expression = expression.decode('utf-8')
        if expression.lower() == 'q':
            break
        expression = compute(expression)
        s.sendto(expression.encode(), destination)
    print(f'Communication with {destination[0]} stopped.')


# PROGRAM STARTS HERE!!
if __name__ == "__main__":
    sock = socket(IP_VERSION, TRANSPORT_PROTOCOL)  # creates socket with ipv4 and udp parameters
    sock.bind(('', 12345))  # local connection
    try:  # catch keyboard interrupt
        while True:  # repeat forever
            print("Waiting for connection...")
            data, source = sock.recvfrom(MAX_SIZE)  # receive data and source ip
            print(f'Connection with {source[0]} stablished.')  # report connectivity to server side terminal
            response = "Connected"
            sock.sendto(response.encode(), source)  # send encoded response back to source
            run_service(sock)  # run the service
    except KeyboardInterrupt:
        print("\nUDP Server terminated by user.")