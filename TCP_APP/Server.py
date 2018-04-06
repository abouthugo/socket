"""
Simply imports the compute function used in UDP because there is no
reason to reinvent the wheel.
"""
from UDP_App.Server import compute

"""
This function simply receives and computes an expression given by the 
client and if the connection on the other end stops, then the loop 
will break and return control to the program that called this function.
"""
def run_service(connection, size, address):
    while True:
        expr = connection.recv(size)
        if not expr or expr.decode('utf-8') == 'END':
            break
        expr = compute(expr.decode('utf-8'))
        connection.send(bytes(expr, 'utf-8'))
    connection.close()
    print(f"Connection with {address} closed.")
