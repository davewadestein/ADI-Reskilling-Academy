import sys

def collatz(num): 
    """Show sequence of Collatz Conjecture
    
    Currently returns number of iterations if successful.
    
    Could instead return a Boolean indicating success (or failure).
    """
    try:
        if type(num) in { str, int, float  }:
            num = int(num)
        else:
            # typically we wouldn't print, but rather, we would return an
            # indication of failure from the function
            print('collatz only accepts int/float/str values') 
            sys.exit(1) # return would be better
    except ValueError as exc:
        print('Non numeric input; exiting.')
        sys.exit(1) # return would be better

    count = 1 # for formatting, we will limit to 10 numbers per line of output
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
    return count

# sys.argv[0] is program name
# sys.argv[1:] is/are the program arguments

if len(sys.argv) == 1: # no parameters
    print(f'Usage: {sys.argv[0]} integer > 1')
    sys.exit(1) # leave the program and indicate failure

result = collatz(sys.argv[1])
print(f'Collatz succeeded in {result} iterations.')
collatz(['a', 'list'])
