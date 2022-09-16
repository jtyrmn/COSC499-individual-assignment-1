# this is a simple calculator program that solves basic arithmetic operations
# run this file using python and input a basic mathematical problem like 1 + 1, 4 - 3, 4 / 5, etc
# type 'exit' to exit the program

# this dictionary contains all the operators this calculator can hander, 
# as well as the logical functions they resolve to
operators = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b
}

def main():
    while(True):
        user_input = input()
        if user_input == 'exit':
            break
        print(parse_input(user_input))
        
def parse_input(user_input: str) -> str:
    if not valid_input(user_input):
        return 'input is invalid'

    # parse the string and plug it into the operators[+,-,*,/,etc] function
    split = user_input.split()
    a,b = float(split[0]), float(split[2])
    output = operators[split[1]](a, b)
    return output

# make sure the input is parseable
def valid_input(user_input: str) -> bool:
    split = user_input.split()
    if len(split) != 3: # user input should be 3 items (1 operator, 2 parameters)
        return False

    if split[1] not in operators: # operator is supported
        return False

    # both parameters are numbers
    try:
        float(split[0])
        float(split[2])
    except ValueError:
        return False
    
    return True

main()