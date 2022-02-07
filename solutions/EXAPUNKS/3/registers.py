"""Code dealing with registers. Also includes the TEST instruction, as that has
to inspect registers.
"""

MAX_NUM = 9999

# We store the registers in a dict, indexed by register name. An OO solution
# would have us creating a register(s) type and associated methods.
registers = {
    "X": 0,
    "T": None,
    "F": None,
}

def is_register(arg):
    """Return True if arg is a named register. You could use the code below
       inside of calling this function but then we'd have a problem if we
       we wanted to change how registers are stored. We might later come up
       with a better way to store them, and we don't want to lock ourselves
       into an implementation yet."""
    return arg in registers


def validate_register(name):
    """Ensure register name is valid.

    If register is F, also ensure file is open.
    """
    if not is_register(name):
        raise Exception(f'Illegal Register Name: {name}')
    if name == "F" and not file.is_open():
        raise Exception('Invalid F register access: File not open!')


def get(name):
    """Get register value.

    If register is F, we have to read from the current file and put the value
    into the F register, then return that.
    """
    validate_register(name)

    if name == "F":
        registers[name] = file.read_value_from_file()
    return registers[name]


def set(name, val):
    """Set register value.

    If register is F, we have to write the value to the current file at the
    current position, then put the value in F.
    """
    validate_register(name)

    if name == "F":
        file.write_value_to_file(val)
    registers[name] = val


def print_registers():
    """Print all registers and their contents."""
    for register in registers:
        print(f"register {register} = {registers[register]}")


def get_valid_int(arg):
    """Return integer value of arg if valid."""
    try:
        val = int(arg)
    except ValueError:
        raise Exception("Not a number") from ValueError
    else:
        if -MAX_NUM <= val <= MAX_NUM:
            return val
    raise Exception("Number out of range -9999..9999")


def get_operand_val(arg):
    """Get the value of an operand, either a register or value."""
    if is_register(arg):
        return get(arg)
    return get_valid_int(arg)

def TEST(op1, tester=None, op2=None):
    """
    Compare value of first operand to the value of second operand.
    If equal, set T register to 1, otherwise set the T register to 0.
    The same syntax is used for the < (less than) and > (greater than) tests.

    Syntax: TEST R/N = R/N
    Also:   TEST EOF to check if at end of file
    """

    import operator

    op_mapper = {
        "=": operator.eq,
        ">": operator.gt,
        "<": operator.lt,
    }
    result = op_mapper[tester](
        get_operand_val(op1), get_operand_val(op2)
    )
    set("T", int(result))
