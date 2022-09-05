import registers
import functions
import labels

instruction_ptr = 0


def get_instruction_ptr():
    return instruction_ptr


def increment_instruction_ptr():
    global instruction_ptr

    instruction_ptr += 1

    return instruction_ptr


def set_instruction_ptr(pos):
    global instruction_ptr

    instruction_ptr = pos


def print_state(statement):
    """Print out current instruction and value of registers."""

    if statement:
        print(f"{str(statement):25s}", end=" ... ")
    registers.print_registers()


def setup_labels(code):
    """Make a pass through the code to find and mark all labels."""
    for instruction_ptr, (instruction, *args) in enumerate(code):
        if instruction == "MARK":
            labels.create_label(args[0], instruction_ptr)

    labels.print_all_labels()


def run_instruction(instruction):
    """Run an instruction by plugging it into the map and getting back a tuple
    of function(s) to invoke."""
    command, *args = instruction

    if command in func_mapper:
        for func in func_mapper[command]:
            func(*args)
    else:
        raise Exception(f"Unknown Instruction: {command}")


def run_code(code):
    """Run the code!

    First, set up the labels, then reset the instruction pointer and loop
    through the code, printing the state after each instruction.
    """
    setup_labels(code)

    current_ptr = get_instruction_ptr()

    while code[current_ptr][0] != "END":
        print_state(code[current_ptr])
        run_instruction(code[current_ptr])
        current_ptr = increment_instruction_ptr()


"""Jump commands possibly move the file pointer and therefore are here with the
code which handles running instructions. The functions module contains only "pure"
functions so we don't want these there.
"""


def TJMP(label):
    """Jump if TRUE. Update instruction pointer to label address."""
    global instruction_ptr

    if registers.get("T") != 0:
        set_instruction_ptr(labels.get_label(label))


# Should be same func as above, just change sense of test
def FJMP(label):
    """Jump if FALSE. Update instruction pointer to label address."""
    if registers.get("T") == 0:
        set_instruction_ptr(labels.get_label(label))


def JUMP(label):
    """Unconditional jump. Same as above without a test."""
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
    "TEST": (functions.TEST,),
    "MARK": (),
    "TJMP": (labels.ensure_valid_label, TJMP),
    "FJMP": (labels.ensure_valid_label, FJMP),
    "JUMP": (labels.ensure_valid_label, JUMP),
}
