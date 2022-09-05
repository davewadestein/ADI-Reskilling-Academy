"""Code dealing with registers. Also includes the TEST instruction, as that has
to inspect registers.
"""


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
