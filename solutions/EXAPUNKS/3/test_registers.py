from registers import *
import pytest

def test_get_register():
    assert get_register('X') == registers['X']


def test_set_register():
    set_register('X', 1)
    assert registers['X'] == 1


def test_is_register():
    assert is_register('X')
    assert not is_register('invalid!')


def test_validate_register():
    with pytest.raises(Exception):
        validate_register('invalid!')


def test_get_operand_val_register():
    set_register('X', 100)
    assert get_operand_val('X') == 100


def test_get_operand_val_int():
    assert get_operand_val('100') == 100


def test_get_operand_val_badint():
    with pytest.raises(TypeError):
        get_operand_val('x')


def test_get_operand_val_bigint():
    with pytest.raises(ValueError):
        get_operand_val(10_000)
