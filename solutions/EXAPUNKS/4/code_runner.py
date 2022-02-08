import registers
import functions
import labels
import files

# Global vars...not the greatest form, but easier than passing them all around.
command = ""            # command
args = ()               # arguments to the command
instruction_ptr = 0     # instruction_ptr


def get_instruction_ptr():
    return instruction_ptr


def set_instruction_ptr(val):
    global instruction_ptr
    instruction_ptr = val


def print_state(code):
    """Print out current instruction, value of registers, and address of
    next instruction.
    """
    global command, args

    if command == "MARK":
        print("...NOOP...")
    else:
        registers.print_registers()
        files.print_file_info()

    if instruction_ptr < len(code):
        print(f"Next instruction: ({instruction_ptr}) {code[instruction_ptr]}")


def setup_labels(code):
    """Make a pass through the code to find and mark all labels."""
    global instruction_ptr

    for instruction_ptr, (instruction, *args) in enumerate(code):
        if instruction == "MARK":
            labels.create_label(args[0], instruction_ptr)


def run_instruction(instruction):
    """Run an instruction by plugging it into the map and getting back a tuple
    of function(s) to invoke."""
    global command, args

    command, *args = instruction

    if command in func_mapper:
        for func in func_mapper[command]:
            func(*args)
    else:
        raise Exception(f'Unknown Instruction: {command}')


def run_code(code):
    """Run the code!

    First, set up the labels, then reset the instruction pointer and loop
    through the code, printing the state after each instruction.
    """
    global instruction_ptr

    setup_labels(code)
    labels.print_all_labels()
    instruction_ptr = 0

    while instruction_ptr < len(code):
        print_state(code)
        run_instruction(code[instruction_ptr])
        instruction_ptr += 1

    print_state(code)
    files.print_final_value_of_files()


"""Jump commands possibly move the file pointer and therefore are here with the
code which handles running instructions. The functions module contains only "pure"
functions so we don't want these there.
"""

def TJMP(label):
    """Jump if TRUE. Return new position of instruction pointer or None if no
    movement is desired."""
    if registers.get("T") != 0:
        set_instruction_ptr(labels.get_label(label))


# Should be same func as above, just change sense of test
def FJMP(label):
    """Jump if FALSE. Return new position of instruction pointer or None if no
    movement is desired."""
    if registers.get("T") == 0:
        set_instruction_ptr(labels.get_label(label))


def JUMP(label):
    """Unconditional jump."""
    set_instruction_ptr(labels.get_label(label))


# Map instructions to a sequence of one or more functions that should be called.
# In the case of MARK, we do nothing because the labels were already set up in
# the first pass.
func_mapper = {
    "COPY": (functions.COPY,),
    "ADDI": (functions.ADDI,),
    "MULI": (functions.MULI,),
    "SUBI": (functions.SUBI,),
    "DIVI": (functions.DIVI,),
    "MODI": (functions.MODI,),
    "TEST": (registers.TEST,),
    "MARK": (),
    "TJMP": (labels.ensure_valid_label, TJMP),
    "FJMP": (labels.ensure_valid_label, FJMP),
    "JUMP": (labels.ensure_valid_label, JUMP),
    "GRAB": (files.ensure_valid_file, files.GRAB),
    "DROP": (files.DROP,),
    "SEEK": (files.SEEK,),
}
