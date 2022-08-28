# This global list will act as the stack.
stack = [] 
debug = False

def push(thing):
    """Push an item onto the stack."""
    stack.append(thing)
    if debug:
        print(f'pushed {thing} onto stack:', end=' ')
        print_stack()
    
              
def pop():
    """Pop and item off the stack and return it."""
    item = stack.pop()
    if debug:
        print(f'popped {thing} off stack:', end= ' ')
        print_stack()
    return item

def top():
    """Return top item from stack but do not pop it."""
    if not stack:
        return None
    else:
        return stack[-1]
    
    
def print_stack():
    """Print stack nicely."""
    print('[', end=' ')
    for thing in stack:
        print(thing, end=' ')
    print(']')
    
    
def add(x, y):
    """Add two values."""
    return x + y


def sub(x, y):
    """Subtract two values."""
    return x - y


def mul(x, y):
    """Multiply two values."""
    return x * y


def div(x, y):
    """Divide two values."""
    return x / y


def floordiv(x, y):
    """Divide two values."""
    return x // y


def exponentiate(x, y):
    """Raise x to power y."""
    return x ** y


def calculate(operator):
    """Perform a calculation using the operator passed."""
    if len(stack) < 2:
        print(f'Not enough operands to perform operation {word}!')
        return None 
    op2, op1 = stack.pop(), stack.pop()
    # If we plug oeprator into our operators dict, we get back a function
    # reference which we can use to call the correct calculation function.
    result = operators[operator](op1, op2)
    if debug:
        print(f'... {op1} {operator} {op2} = {result}')
    push(result)
    if len(stack) > 1:
        print_stack()
    

def process(item):
    """Identify if number, and if so, push it on the stack."""
    try:
        if '.' in item: # decimal point?
            val = float(item)
        else:
            val = int(item)
        push(val)
    except ValueError:
        # must be an operator
        if item in operators:
            calculate(item)
        else:
            print('invalid operator: {item}')
    
    
operators = {
     '+': add,
     '-': sub,
     '*': mul,
     '/': div,
    '//': floordiv,
    '**': exponentiate,
}
    
while (line := input().split()): # Python 3.10 Walrus operator
    if line[0] == 'debug':
        debug = not debug # flip the state of debug
        print('debug', 'on' if debug else 'off')
        continue
    for word in line:
        process(word)
    if len(stack) == 1:
        print(stack.pop())
    else:
        print('invalid expression')
