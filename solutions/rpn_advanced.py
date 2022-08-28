"""This is an advanced solutioin for two reasons:

1. It creates a new datatype (class) called Stack which inherits from list
and adds a push() method.
2. It relies on function references to the Python operator module in order
to do the calculations, so there is no need to define add(), sub(), etc.
functions.
"""

class Stack(list):
    """A Stack class which inherits from list and adds a push() method."""
    def push(self, item):
        self.append(item)

# The operator module contains the functions that Python uses to implement
# the arithmetic operators. In addition the standard 4 functions we will add
# // for integer (floor) division and the modulus (%) operator.
import operator

operators = {
         '+': operator.add,
         '-': operator.sub,
         '*': operator.mul,
         '/': operator.truediv,
    	'//': operator.floordiv,
         '%': operator.mod,
}

stack = Stack() # create a Stack object to hold the expression

while (line := input().split()): # Python 3.10 Walrus operator
    for word in line:
        if word in operators:
            if len(stack) < 2:
                print(f'Not enough operands to perform operation {word}!')
                break
            op2, op1 = stack.pop(), stack.pop()
            result = operators[word](op1, op2)
            print(op1, word, op2, '=', result)
        else:
            result = float(word)
        stack.push(result)

    if len(stack) == 1:
        print(stack.pop())
