from socket import socket, AF_INET, SOCK_DGRAM
MAX_SIZE = 4096  # 512 bytes of data
"""
The compute(string) function:
    - Defines an array of valid operands that a client might use. Called [operands]
    - Creates a copy of the string passed in into an array. Called [array]
    - Flush out the previous value for the string passed in. 
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


def compute(string):
    operands = ['+', '-', '*', '/', '**', '%', '(', ")"]
    array = [letter for letter in string]
    string = ''
    for s in array:
        if s in operands or s == '.' or type(s) == int or s.isdigit():
            string += str(s)
    try:
        if isinstance(eval(string), float):
            string = f'\t{eval(string):.2f}'
            return f'\t{string}'
        else:
            return str(eval(string))
    except (SyntaxError, EOFError):
        string = f'\tYour expression is invalid, you can only use operands: \n\t{operands} and digits 0-9'
        return string


"""
The communication(s) function:
    
"""


def communication(s):
    i = 0
    while True:
        expr, destination = s.recvfrom(MAX_SIZE)
        expr = expr.decode('utf-8')
        if expr == 'q':
            break
        expr = compute(expr)
        s.sendto(expr.encode(), destination)
        i += 1
        print(f"{i}) Completed ")
    print(f'Communication with {destination[0]} stopped\nWaiting for new connection...')


# PROGRAM STARTS HERE!!
if __name__ == "__main__":
    sock = socket(AF_INET, SOCK_DGRAM)  # AF_INET is the address family for ipv4 hosts, SOCK_DGRAM
    sock.bind(('', 12345))  # accept connections on this port and bind to socket
    print("Waiting for connection...")
    try:
        while True:
            data, address = sock.recvfrom(MAX_SIZE)  # receive data
            print(f'Incoming connection from {address}')
            resp = "Connected"
            sock.sendto(resp.encode(), address)
            communication(sock)
    except KeyboardInterrupt:
        print("\nUDP Server terminated by user")