"""Code dealing with registers. Also includes the TEST instruction, as that has
to inspect registers.
"""

import files

MAX_NUM = 9999

# We store the registers in a dict, indexed by register name. An OO solution
# would have us creating a register(s) type and associated methods.
registers = {
    "X": 0,
    "T": 0,
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
        raise Exception(f"Illegal Register Name: {name}")
    if name == "F" and not files.file_is_open():
        raise Exception("Invalid F register access: File not open!")


def get_register(name):
    """Get register value.

    If register is F, we have to read from the current file and put the value
    into the F register, then return that.
    """
    validate_register(name)

    if name == "F":
        registers[name] = files.read_value_from_file()
    return registers[name]


def set_register(name, val):
    """Set register value.

    If register is F, we have to write the value to the current file at the
    current position, then put the value in F.
    """
    validate_register(name)

    if name == "F":
        files.write_value_to_file(val)
    registers[name] = val


def print_registers():
    """Print all registers and their contents."""
    print("registers:", end=" ")
    for register in registers:
        print(f"{register} ({registers[register]})", end="  ")
    print()
