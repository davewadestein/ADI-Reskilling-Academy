def calculate(op1, op2, oper, **kwargs):
    op1 = float(op1)
    op2 = float(op2)
    do_float = True
    
    if oper not in '+-*/':
        print('bad operator:', oper)
        return None
    
    if kwargs.get('float') != True:
        do_float = False
        op1 = int(op1)
        op2 = int(op2)
    
    if oper == '+':
        return op1 + op2
    if oper == '-':
        return op1 - op2
    if oper == '*':
        return op1 * op2
    if oper == '/':
        if do_float:
            return op1 / op2
        else:
            return op1 // op2

import sys
# do something w/command line arguments
# so that the above function is invoked
# with the correct arguments

#print(sys.argv)

if len(sys.argv) == 4:
        print(calculate(sys.argv[1], sys.argv[2], 
		sys.argv[3], float=False))
elif len(sys.argv) == 5:
        print(calculate(sys.argv[1], sys.argv[2], 
		sys.argv[3], float=True))
else:
    print('usage:', sys.argv[0], 'op1 op2 operator')
