import registers
import functions

# Global vars...not the greatest form, but easier than passing them all around.
command = ""            # command
args = ()               # arguments to the command


def print_state(code):
    """Print out current instruction, value of registers, and address of
    next instruction.
    """
    global command, args

    registers.print_registers()


def run_code(code):
    """Run the code!

    Loop through the input, printing the state after each instruction.
    """
    for statement in code:
        print_state(statement)
        print(statement)
        run_instruction(statement)

    print_state(statement)


def run_instruction(instruction):
    """Run an instruction by plugging it into the map and getting back a
    tuple of functions to invoke."""
    global command, args

    command, args = instruction[0], instruction[1:]

    if command in functions.func_mapper:
        # func_mapper contains a reference to a function we want to call.
        # args is a list of args which we want to unpack/explode into separate
        # args because the functions expect separate args.
        functions.func_mapper[command](*args)
    else:
        raise Exception(f'Unknown Instruction: {command}')
