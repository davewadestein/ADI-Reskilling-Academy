import registers
import functions


def print_state(statement):
    """Print out current instruction and value of registers."""

    if statement:
        print(statement)
    registers.print_registers()


def run_code(code):
    """Run the code!

    Loop through the input, printing the state before each instruction.
    """

    print_state('')

    for statement in code:
        run_instruction(statement)
        print_state(statement)


def run_instruction(statement):
    """Run an instruction by plugging it into the map and getting back a
    tuple of functions to invoke."""
    # first, split up the instruction into the command and its args
    instruction, args = statement[0], statement[1:]

    if instruction in functions.func_mapper:
        # func_mapper contains a reference to a function we want to call.
        # args is a list of args which we want to unpack/explode into separate
        # args because the functions expect separate args.
        functions.func_mapper[instruction](*args)
    else:
        # if we got here, then we recevied an unknown instruction
        raise Exception(f"Unknown Instruction: {instruction}")
