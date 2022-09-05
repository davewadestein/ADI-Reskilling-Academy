"""This module contains implementations of the EXA functions."""

import registers
import labels


def get_valid_int(arg):
    """Return integer value of arg if valid."""
    MAX_NUM = 9999

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
    if registers.is_register(arg):
        return registers.get(arg)
    return get_valid_int(arg)


def COPY(src, dest):
    """Copy the value of the src operand into the dest operand.

    Syntax: COPY R/N R
    """
    registers.set(dest, get_operand_val(src))


def ADDI(op1, op2, dest):
    """Add value of first operand to value of second operand, store result in dest.

    Syntax: ADDI R/N R/N R
    """
    registers.set(dest, get_operand_val(op1) + get_operand_val(op2))


def SUBI(op1, op2, dest):
    """Subtract value of second operand from value of first operand, store result in dest.

    Syntax: SUBI R/N R/N R
    """
    registers.set(dest, get_operand_val(op1) - get_operand_val(op2))


def MULI(op1, op2, dest):
    """Multiply value of first operand to value of the second operand, store result in dest.

    Syntax: MULI R/N R/N
    """
    registers.set(dest, get_operand_val(op1) * get_operand_val(op2))


def DIVI(op1, op2, dest):
    """Divide value of first operand by value of second operand, result in dest.

    Syntax: R/N R/N R
    """
    registers.set(dest, get_operand_val(op1) // get_operand_val(op2))


def MODI(op1, op2, dest):
    """Compute remainder when dividing op1 by op2 and store result in dest.

    Syntax: R/N R/N R
    """
    registers.set(dest, get_operand_val(op1) % get_operand_val(op2))


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
    result = op_mapper[tester](get_operand_val(op1), get_operand_val(op2))
    registers.set("T", int(result))
