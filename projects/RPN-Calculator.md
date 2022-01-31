# Reverse Polish Notation (RPN) Parser/Calculator
* write a Python program to parse RPN and calculate the result (e.g., an RPN calculator).
  * as an example, if you entered __3 4 +__, your program should print __7__
* use a stack to implement your solution
  * you can simulate a stack with a Python list
  * lists already have a pop() method which removes ("pops") the last item
  * to be consistent, rather than calling __.append()__ you should create a _push_ function or method (your function or method can call __.append__ we just wanted the code to be calling __push__ and __pop__ rather than __append__ and __pop__
    * if you want to create an object-oriented solution, you might consider creating a __Stack__ class which extends the built-in __list__ class and adds a __push__ method which simply invokes __.append__\
* when numbers are detected (e.g., 3 and 4 above), you should _push_ them onto the stack
* when an operator is detected, you should _pop_ two items off the stack, perform the operation on them, and push the result onto the stack (e.g., when you see the +, you pop 4 and 3, then perform __3 + 4__ and push __7__ onto the stack)
  * you can write your own calculation functions, but you might consider using the __operator__ module built in to Python
* each time a calculation is detected, your program should calculate the result

## Some test cases
* __3 4 +__ (7)
* __3 4 * 5 +__ (17)
* __3 9 - 2 * -4 / 7 +__ (10)
* __-3 -5 2 9 * + -__ (-16)
