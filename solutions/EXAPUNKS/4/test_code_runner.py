from code_runner import *
import code_runner  # to get at .instruction_ptr
from registers import *
from labels import create_label


def test_run_instruction():
    import pytest

    with pytest.raises(Exception):
        run_instruction(["INVALID"])


def test_get_instruction_ptr():
    assert get_instruction_ptr() == 0


def test_set_instruction_ptr():
    set_instruction_ptr(1)
    assert code_runner.instruction_ptr == 1


def test_increment_instruction_ptr():
    set_instruction_ptr(1)
    assert increment_instruction_ptr() == 2


def test_TJMP():
    create_label("TRUE_TEST", 5)
    set_register("T", 1)
    TJMP("TRUE_TEST")
    assert code_runner.instruction_ptr == 5


def test_FJMP():
    set_instruction_ptr(0)
    create_label("FALSE_TEST", 5)
    set_register("T", 0)
    FJMP("FALSE_TEST")
    assert code_runner.instruction_ptr == 5


def test_JUMP():
    set_instruction_ptr(0)
    create_label("JUMP_TEST", 5)
    JUMP("JUMP_TEST")
    assert code_runner.instruction_ptr == 5
