# our goal is to be able to run this function, i.e., interface with this code from "outside"
# in other words from Windows command prompt or Linux command prompt
import sys  # gives us access to command-line arguments (argv)

# sys.argv is going to look like ['script.py']
import argparse

from code_functions import generate_secret_code

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

# let's see what they all are
print(
    f"debug is {args.debug}, allow_dupes is {args.allow_dupes}, num_digits is {args.num_digits}"
)

print(
    generate_secret_code(
        args.num_digits, debug=args.debug, allow_dupes=args.allow_dupes
    )
)
