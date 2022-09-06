from functions import *
from registers import get_register, set_register
import pytest


def test_get_operand_val_register():
    set_register("X", 100)
    assert get_operand_val("X") == 100


def test_get_operand_val_int():
    assert get_operand_val("100") == 100


def test_get_operand_val_badint():
    with pytest.raises(TypeError):
        get_operand_val("x")


def test_get_operand_val_bigint():
    with pytest.raises(ValueError):
        get_operand_val(10_000)


def test_COPY():
    COPY("10", "X")
    assert get_register("X") == 10


def test_ADDI():
    set_register("X", 10)
    ADDI("10", "X", "X")
    assert get_register("X") == 20


def test_SUBI():
    set_register("X", 10)
    SUBI("X", "10", "X")
    assert get_register("X") == 0


def test_MULI():
    set_register("X", 10)
    MULI("X", "10", "X")
    assert get_register("X") == 100


def test_DIVI():
    set_register("X", 17)
    DIVI("X", "5", "X")
    assert get_register("X") == 3


def test_MODI():
    set_register("X", 17)
    MODI("X", "5", "X")
    assert get_register("X") == 2


def test_test_equals():
    TEST("10", "=", 10)
    assert get_register("T") == 1


def test_test_greater():
    TEST("10", ">", "9")
    assert get_register("T") == 1


def test_test_less():
    TEST("9", "<", "10")
    assert get_register("T") == 1
