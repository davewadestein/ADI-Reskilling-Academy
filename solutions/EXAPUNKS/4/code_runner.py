import registers, file

# Global vars...not the greatest form, but easier than passing them all around.
labels = {}             # labels found in input program
command = ""            # command
args = ()               # arguments to the command
instruction_ptr = 0     # instruction_ptr


def print_state(code):
    """Print out current instruction, value of registers, and address of
    next instruction.
    """
    global command, args

    if command == "MARK":
        print("...NOOP...")
    else:
        registers.print_registers()
        file.print_file_info()

    if instruction_ptr < len(code):
        print(f"Next instruction: ({instruction_ptr}) {code[instruction_ptr]}")


def setup_labels(code):
    """Make a pass through the code to find and mark all labels."""
    global instruction_ptr

    for instruction_ptr, (instruction, *args) in enumerate(code):
        if instruction == "MARK":
            MARK(args[0])

    print("Labels:", end=" ")
    for label in labels:
        print(f"{label} ({labels[label]})", end=" ")
    print()


def execute_instruction(instruction):
    """Execute an instruction by plugging it into the map and getting back a
    tuple of functions to invoke."""
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
    global instruction_ptr, command, args

    setup_labels(code)
    instruction_ptr = 0

    while instruction_ptr < len(code):
        print_state(code)
        execute_instruction(code[instruction_ptr])
        instruction_ptr += 1

    print_state(code)
    file.print_final_value_of_files()


def COPY(src, dest):
    """Copy the value of the src operand into the dest operand.

    Syntax: COPY R/N R
    """
    registers.set(dest, registers.get_operand_val(src))


def ADDI(op1, op2, dest):
    """Add value of first operand to value of second operand, store result in dest.

    Syntax: ADDI R/N R/N R
    """
    registers.set(dest, registers.get_operand_val(op1) + registers.get_operand_val(op2))


def SUBI(op1, op2, dest):
    """Subtract value of second operand from value of first operand, store result in dest.

    Syntax: SUBI R/N R/N R
    """
    registers.set(dest, registers.get_operand_val(op1) - registers.get_operand_val(op2))


def MULI(op1, op2, dest):
    """Multiply value of first operand to value of the second operand, store result in dest.

    Syntax: MULI R/N R/N
    """
    registers.set(dest, registers.get_operand_val(op1) * registers.get_operand_val(op2))


def DIVI(op1, op2, dest):
    """Divide value of first operand by value of second operand, result in dest.

    Syntax: R/N R/N R
    """
    registers.set(
        dest, registers.get_operand_val(op1) // registers.get_operand_val(op2)
    )


def MODI(op1, op2, dest):
    """Compute remainder when dividing op1 by op2 and store result in dest.

    Syntax: R/N R/N R
    """
    registers.set(dest, registers.get_operand_val(op1) % registers.get_operand_val(op2))


def TEST(op1, tester=None, op2=None):
    """
    Compare value of first operand to the value of second operand.
    If equal, set T register to 1, otherwise set the T register to 0.
    The same syntax is used for the < (less than) and > (greater than) tests.

    Syntax: TEST R/N = R/N
    Also:   TEST EOF to check if at end of file
    """

    if op1 == "EOF":
        result = file.is_current_file_at_eof()
    else:
        import operator

        op_mapper = {
            "=": operator.eq,
            ">": operator.gt,
            "<": operator.lt,
        }
        result = op_mapper[tester](
            registers.get_operand_val(op1), registers.get_operand_val(op2)
        )

    registers.set("T", int(result))


def MARK(label):
    """Create a label if it doesn't already exist."""
    if label in labels:
        raise Exception(f'Duplicate Label: {label}')
    labels[label] = instruction_ptr


def ensure_valid_label(label):
    """Ensure a label is valid, i.e., it's in the map."""
    if label not in labels:
        raise Exception(f'Unknown Label: {label}')


def TJMP(label):
    """Jump if TRUE."""
    global instruction_ptr

    if registers.get("T") != 0:
        instruction_ptr = labels[label]


# Should be same func as above, just change sense of test
def FJMP(label):
    """Jump if FALSE."""
    global instruction_ptr

    if registers.get("T") == 0:
        instruction_ptr = labels[label]


def JUMP(label):
    """Unconditional jump."""
    global instruction_ptr

    instruction_ptr = labels[label]


# Map instructions to a sequence of one or more functions that should be called.
# In the case of MARK, we do nothing because the labels were already set up in
# the first pass.
func_mapper = {
    "COPY": (COPY,),
    "ADDI": (ADDI,),
    "MULI": (MULI,),
    "SUBI": (SUBI,),
    "DIVI": (DIVI,),
    "MODI": (MODI,),
    "TEST": (TEST,),
    "MARK": (),
    "TJMP": (ensure_valid_label, TJMP),
    "FJMP": (ensure_valid_label, FJMP),
    "JUMP": (ensure_valid_label, JUMP),
    "GRAB": (file.ensure_valid_file, file.GRAB),
    "DROP": (file.ensure_file_is_open, file.DROP),
    "SEEK": (file.SEEK,),
}
