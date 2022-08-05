def generate_secret_code(num_digits=4, **kwargs):
    """Generate a numeric "code" of a certain digit length.
    Duplicates are not normally allowed in the code, but the caller may set allow_dupes=True to allow them.
    """
    from random import choice as random_choice # we are free to rename imports to suit our mood
    
    try:
        num_digits = int(num_digits)
    except ValueError as original_exception:
        raise TypeError('generate_secret_code(): Expected int or int-ifiable argument' + '\noriginal error: ' + str(original_exception))
    
    debug = kwargs.get('debug') # this will be None if not there or the value if it is there
    allow_dupes = kwargs.get('allow_dupes')
    
    # or...
    debug, allow_dupes = False, False # set up intial option values
    
    if 'debug' in kwargs: # is 'debug' a key in the dict?
        debug = kwargs['debug']
    if 'allow_dupes' in kwargs: # is 'allow_dupes' a key in the dict?
        allow_dupes = kwargs['allow_dupes']
        
    digits_to_pick_from = list(range(10)) # [ 0, 1, ..., 9 ]
    secret_code = []
    
    # this is not the ideal way to handle such errors, but it's a way...
    if num_digits < 2 or num_digits > 10:
        raise ValueError('number of digits in code must be between 2 and 10')
    
    if debug:
        print(f'Generating a {num_digits}-digit secret code...')
        
    for times in range(num_digits):
        digit = random_choice(digits_to_pick_from)
        if not allow_dupes: # "if the truthy value of allows_dupes is True, we do the remove, i.e., we don't allow dupes
            digits_to_pick_from.remove(digit)
        if debug:
            print('chosen digit =', digit, 'remaining choices =', digits_to_pick_from)
        secret_code.append(str(digit)) # at the time we append, let's str-ify it
    
    return secret_code

# our goal is to be able to run this function, i.e., interface with this code from "outside"
# in other words from Windows command prompt or Linux command prompt

import sys # gives us access to command-line arguments (argv)
# sys.argv is going to look like ['script.py']

print(sys.argv)

if len(sys.argv) > 1: # this means >= 1 command-line args
    # ['gencode.py', '4']
    args_to_pass = {}
    if '-d' in sys.argv: # has -d been passed as a command-line arg
        args_to_pass['debug'] = True
        sys.argv.remove('-d')
    if '-a' in sys.argv: # has -a been passed as a command-line arg
        args_to_pass['allow_dupes'] = True
        sys.argv.remove('-a')
    
    sys.argv.append('4') # now sys.argv has at least 2 items in it .. [0] and [1]
    print(generate_secret_code(sys.argv[1], **args_to_pass))
else:
    print(generate_secret_code()) # call it w/no params, so use defaults
