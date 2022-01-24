"""If you put a docstring at the top of the module, it will be printed out
as the documentation for the module itself when consumers of your module
call help on the module. Try it and see!!!
"""

default_tape_val = 1
ADI_copyright = 'text here'

def whizbang(x):
    """demonstrate that import within a function only applies within the function"""
    from math import sin, cos, pi
    
    print(id(sin), id(cos), pi)
    print(dir())
    
    
def func():
    """demonstrate try/except/else/finally"""
    try:
        i = int(input('\nEnter a number: ')) # ValueError?
        x = 1 / i # ZeroDivisionError?
    except ValueError:
        print('Not a number!')
        return
    except ZeroDivisionError:
        print('Cannot divide by 0')
    else:
        print('Everything OK')
    finally:
        print('FINALLY: DO this either way!')
        
        
'''commenting this out because the / syntax does not work in Python 3.7
def weird_func_sig(x, /, y, z, *, debug=False, end='newline'):
    """demonstrate / and * in function signature"""
    # x can only be passed positionally, i.e., you cannot write x=?
    # y and z can be passed either positionally or by keyword
    # debug and end are keyword-only argument and must be passed that way
    print(x)
    print(y, z)
    print(debug, end)
'''
    
    
def weird_func_args(x, y, z, *args, **kwargs):
    print('req args:', x, y, z)
    if len(args) == 0:
        print('no variable positional args were passed')
    else:
        print('var pos args', args)
    print('var keywd args', kwargs)
    if 'debug' in kwargs:
        print('FOUND debug in kwargs')
        if kwargs['debug'] == True: # because it could be false
            turn_on_debugging = True
            # utilize some of *args...
            
            
def adder(x, y):
    """"add" two objects using +"""
    try:
        return x + y
    except TypeError:
        return None
    
    
def sum_digits(num=1235):
    """Sum up digits and if result is more than 1 digit, keep summing until result is 1 digit."""

    # debugging
    print(f'sum_digits({num})')
    # Much easier (for me) to treat the number as a string and then pick off each 'digit'
    result = 0

    for digit in str(num): # convert to num so we can iterate through the number
        try:
            result += int(digit) # convert back to int to do the addition
        except ValueError:
            print(f'bad digit ({digit}) found; skipping.')

    if result > 9: # i.e., > 1 digit
        return sum_digits(result) # call ourselves "recursively" to get the job done

    return result # 1 digit, so just return it


def product(*terms): # 0+ terms
    """multiply all terms together and return result"""
    result = 1
    
    for term in terms: # iterate through the terms (args) tuple
        result *= term
        
    return result


def collatz(num=59):
    """Show sequence of Collatz Conjecture...blah"""
    if type(num) == str:
        num = int(num)
    count = 0 # for formatting, we will limit to 10 numbers per line of output
    while num != 1:
        print(f'{num:9d}', end='')
        count += 1
        if count % 10 == 0: # every 10 numbers, print a newline
            print()
        if num % 2 == 0: # fails if num is float
            num //= 2 
        else:
            num = num * 3 + 1
    print('        1')
    
    
def add_commas(num=12345):
    """Return a string representing the number with commas added for thousands."""
    num = str(num)[::-1] # string-ify and reverse to make it easier to work with
    comma_num = '' # result will be built up in this string
    
    for position in range(0, len(num), 3): # go through string 3 digits at a time
        comma_num += num[position:position + 3] # append the current 3 digits
        if position < len(num) - 3: # if we're not at the end, add a comma
            comma_num += ','
    
    return comma_num[::-1] # reverse back 
