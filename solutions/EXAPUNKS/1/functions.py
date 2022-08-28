"""This module contains implementations of the EXA functions."""

from registers import set_register, get_operand_val


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


"""Map each instruction to the function that implements it."""
func_mapper = {
    "COPY": COPY,
    "ADDI": ADDI,
    "MULI": MULI,
    "SUBI": SUBI,
    "DIVI": DIVI,
    "MODI": MODI,
}
