def generate_secret_code(num_digits=4, debug=False, allow_dupes=False):
    """Generate a numeric "code" of a certain digit length.
    Duplicates are not normally allowed in the code, but the caller may set allow_dupes=True to allow them.
    """
    from random import choice as random_choice # we are free to rename imports to suit our mood

    try:
        num_digits = int(num_digits)
    except ValueError as original_exception:
        raise TypeError(
            "generate_secret_code(): Expected int or int-ifiable argument"
            + "\noriginal error: "
            + str(original_exception)
        )

    digits_to_pick_from = list(range(10))  # [ 0, 1, ..., 9 ]
    secret_code = []

    # this is not the ideal way to handle such errors, but it's a way...
    if num_digits < 2 or num_digits > 10:
        raise ValueError("number of digits in code must be between 2 and 10")

    if debug:
        print(f"Generating a {num_digits}-digit secret code...")

    for times in range(num_digits):
        digit = random_choice(digits_to_pick_from)
        if not allow_dupes:  # "if the truthy value of allows_dupes is True, we do the remove, i.e., we don't allow dupes
            digits_to_pick_from.remove(digit)
        if debug:
            print("chosen digit =", digit, "remaining choices =", digits_to_pick_from)
        secret_code.append(str(digit))  # at the time we append, let's str-ify it

    return secret_code


# our goal is to be able to run this function, i.e., interface with this code from "outside"
# in other words from Windows command prompt or Linux command prompt

import sys  # gives us access to command-line arguments (argv)

# sys.argv is going to look like ['script.py']
import argparse

"""Create an argument parser so we don't have to manually parse the arguments to
this script.

The add_argument calls below tell the parser which command-line arguments are valid.
The -d and -a arguments (also specifiable as --debug and --allow_dupes) are Boolean
options, i.e., they are either included or excluded. 

The -n argument is a numeric argument (int) and it requires a parameter to be
specified as well (e.g., "-n 5"). It has a default value of 4, which will be overridden
if the user specifies the -n option on thec command line.
"""

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--debug", help="turn on debugging", action="store_true")
parser.add_argument("-a", "--allow_dupes", help="allow duplicate code values", action="store_true")
parser.add_argument(
    "-n",
    "--num_digits",
    help="specify number of digits in the code",
    action="store",
    default=4,
    type=int,
)

# parse_known_args() will allow unknown args and store the in the second element of the tuple
# which is returned...that way, we don't crash when unknown/unexpected args are passed and 
# we can deal with them later.
args, unknown = parser.parse_known_args() # parse the arguments!

print(args)
print(unknown)

# let's see what they all are
print(
    f"debug is {args.debug}, allow_dupes is {args.allow_dupes}, num_digits is {args.num_digits}"
)

print(
    generate_secret_code(
        args.num_digits, debug=args.debug, allow_dupes=args.allow_dupes
    )
)
