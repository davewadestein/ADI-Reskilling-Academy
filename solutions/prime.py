# This is the code that pytest will test.
# NOTE: it will need to be imported by the test_*.py file in order to test it.
# For now, we'll see these are both in the same folder, but ultimately they will
# be in separate code and test folders.

def _is_prime(num):
    if num < 2:
        return False # to be safe, in case someone uses this
    for check in range(2, num):
        if num % check == 0:
            return False
    return True

def _is_even(num):
    return num % 2 == 0

def find_next_prime(num, proposed_prime=-1):
    """given an integer find the nearest prime greater than it"""
    # untested is code is broken code 
    if type(num) not in { int, float }:
        raise TypeError('Only ints and floats are valid!')
    num = int(num) + 1
    
    # Handle negative numbers and anything less than 2
    if num < 2:
        return 2

    while True:
        if _is_prime(num):
            if proposed_prime != -1: # if second arg
                return num == proposed_prime
            else:
                return num
        if _is_even(num):
            num += 1 # make it odd
        else:
            num += 2 # skip even numbers
