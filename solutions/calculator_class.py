"""Homework assignment, should you choose to accept it.
- add docstrings (for methods but also for the class)
- add missing methods (sub, mul, div, pow, log, ...)
"""

class Calcul8tor: # we are creating a new type called "Calcul8tor"
    def __init__(self): # you must have self...but we don't need to pass anything in
        self.total = 0
        self.calculations = []
    
    def __repr__(self): # this has to return a string
        return self.showcalc() # taylor.deposit(...)
    
    def ac(self):
        self.__init__()
        
    def add(self, operand1, operand2=None): # we need a way to ensure that we can tell whether the second operand is passed
        """Add 2 numbers or add first number to running total."""
        # if operand2 is None
        if operand2 == None: # they didn't pass an operand2, i.e., operand2 should be the running total
            # swap operands so that they appear in correct order in our calculation
            operand2 = operand1
            operand1 = self.total
        self.total = operand1 + operand2 # add the 2 numbers and put the result on the screen
        self.calculations.append(f'{operand1} + {operand2} = {self.total}')
        
        return self.total
    
    def showcalc(self):
        if not self.calculations: # nothing in the list of calculations
            return '0'
        return '\n'.join(self.calculations)
