
operands = ['+', '-', '*', '/', '**', '%']

def checkup(string):
    array = [letter for letter in string];
    i=0;
    string = ''
    for s in array:
        if(s in operands or s == '.' or s.isdigit()):
            string+=s
        i+=1
    return string



expression = "2.2 * 6s7& + 2 /2 -3**2"
expression = checkup(expression)
print(expression, f"= {eval(expression):.2f} ")

