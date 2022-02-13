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
            op2, op1 = stack.pop(), stack.pop()
            result = operators[word](op1, op2)
            print(op1, word, op2, '=', result)
        else:
            result = float(word)
        stack.push(result)

    if len(stack) == 1:
        print(stack.pop())
