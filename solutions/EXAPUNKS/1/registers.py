MAX_NUM = 9999

"""Registers are stored in a dict, indexed by register name. An OO solution
would have us creating a register(s) type and associated methods, but we are
approaching OO here by providing functions to interface with the dict.

No other modules should access the dict directly.
"""

registers = {
    "X": 0,
    "T": None,
}


def is_register(arg):
    """Return True if arg is a named register. You could use the code below
       inside of calling this function but then we'd have a problem if we
       we wanted to change how registers are stored. We might later come up
       with a better way to store them, and we don't want to lock ourselves
       into an implementation yet."""
    return arg in registers


def validate_register(name):
    """Ensure register name is valid."""
    if not is_register(name):
        raise Exception(f"Illegal Register Name: {name}")


def get_register(name):
    """Get register value."""
    validate_register(name)

    return registers[name]


def set_register(name, val):
    """Set register value."""
    validate_register(name)

    registers[name] = val


def print_registers():
    """Print all registers and their contents."""
    print("registers:", end=" ")
    for register in registers:
        print(f"{register} ({registers[register]})", end="  ")
    print()


def get_operand_val(arg):
    """Get the value of an operand, either a register or value."""
    if is_register(arg):
        return get_register(arg)
    return get_valid_int(arg)


def get_valid_int(arg):
    """Return integer value of arg if valid."""
    try:
        val = int(arg)
    except ValueError:
        raise TypeError("Not a number")
    else:
        if -MAX_NUM <= val <= MAX_NUM:
            return val
    raise ValueError("Number out of range -9999..9999")
