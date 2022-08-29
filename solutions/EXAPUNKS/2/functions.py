"""This module contains implementations of the EXA functions."""

from registers import set_register, get_register, get_operand_val


def COPY(src, dest):
    """Copy the value of the src operand into the dest operand.

    Syntax: COPY R/N R
    """
    set_register(dest, get_operand_val(src))


def ADDI(op1, op2, dest):
    """Add value of first operand to value of second operand, store result in dest.

    Syntax: ADDI R/N R/N R
    """
    set_register(dest, get_operand_val(op1) + get_operand_val(op2))


def SUBI(op1, op2, dest):
    """Subtract value of second operand from value of first operand, store result in dest.

    Syntax: SUBI R/N R/N R
    """
    set_register(dest, get_operand_val(op1) - get_operand_val(op2))


def MULI(op1, op2, dest):
    """Multiply value of first operand to value of the second operand, store result in dest.

    Syntax: MULI R/N R/N
    """
    set_register(dest, get_operand_val(op1) * get_operand_val(op2))


def DIVI(op1, op2, dest):
    """Divide value of first operand by value of second operand, result in dest.

    Syntax: R/N R/N R
    """
    set_register(dest, get_operand_val(op1) // get_operand_val(op2))


def MODI(op1, op2, dest):
    """Compute remainder when dividing op1 by op2 and store result in dest.

    Syntax: R/N R/N R
    """
    set_register(dest, get_operand_val(op1) % get_operand_val(op2))


def TEST(op1, tester, op2):
    """
    Compare value of first operand to the value of second operand.
    If equal, set T register to 1, otherwise set the T register to 0.
    The same syntax is used for the < (less than) and > (greater than) tests.

    Syntax: TEST R/N = R/N
    """

    import operator

    # Python's operator module is used here to simplify <, >, and ==.
    # When we see a '<', '>', or '=', we call the corresponding function
    # in the operator module, and it will perform the <, >, and == as needed.
    # This could be written as an if/elif/else of course.
    op_mapper = {
        "=": operator.eq,
        ">": operator.gt,
        "<": operator.lt,
    }
    result = op_mapper[tester](get_operand_val(op1), get_operand_val(op2))

    set_register("T", int(result))


"""Map instructions to the functions that implements it."""
func_mapper = {
    "COPY": COPY,
    "ADDI": ADDI,
    "MULI": MULI,
    "SUBI": SUBI,
    "DIVI": DIVI,
    "MODI": MODI,
    "TEST": TEST,
}
