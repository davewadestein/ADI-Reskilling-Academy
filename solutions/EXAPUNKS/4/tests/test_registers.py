import pytest
import sys
sys.path.append('..')

from registers import *


def test_validate_register():
    validate_register('T')
    validate_register('X')
    with pytest.raises(Exception):
        validate_register('F') # shoud thrown an exception with no file Open


def test_get_set():
    set('X', 10)
    assert get('X') == 10
