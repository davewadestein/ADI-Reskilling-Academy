import sys
from code_runner import run_code

code = [] # we will store the program here


def parse(codefile):
    """Open a codefile and return parsed code, which will be a list where
    each item is itself a list containing the splitted line of code, e.g.,
    ['ADDI', '50', 'X', 'X']
    """
    try:
        file = open(codefile)
    except FileNotFoundError:
        print(f'Cannot open file "{codefile}"')
        sys.exit(1)

    """Read entire file using readlines(), which is technically unsafe, as file
    could be HUGE. Strip whitespace and discard blank lines while we're at it."""
    with file:
        code = [line.strip().split() for line in files.readlines() if len(line) > 1]

    return code


if len(sys.argv) < 2:
    print("No code file to open!")
    sys.exit(1)

run_code(parse(sys.argv[1]))
