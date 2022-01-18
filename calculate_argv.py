def calculate(operand1, operand2, operator, **kwargs):
    if kwargs.get('float') == True:
        operand1 = float(operand1)
        operand2 = float(operand2)
    else:
        try:
            operand1 = int(operand1)
            operand2 = int(operand2)
        except ValueError:
            print('not a number')
            return

    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        if type(operand1) == float:
             return operand1 / operand2
        else:
            return operand1 // operand2

import sys
from calculate_module import calculate

if len(sys.argv) >= 4:  
    if sys.argv[1] == '-f':
        print(calculate(sys.argv[2], sys.argv[3], 
                            sys.argv[4], float=True))
    else:
        print(calculate(sys.argv[1], sys.argv[2], sys.argv[3]))
else:
    print("usage:", sys.argv[0], "operand operand operator")
