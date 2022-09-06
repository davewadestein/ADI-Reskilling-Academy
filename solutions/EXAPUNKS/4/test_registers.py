from registers import *
import pytest


def test_get_register():
    assert get_register("X") == registers["X"]


def test_set_register():
    set_register("X", 1)
    assert registers["X"] == 1


def test_is_register():
    assert is_register("X")
    assert not is_register("invalid!")


def test_validate_register():
    with pytest.raises(Exception):
        validate_register("invalid!")
