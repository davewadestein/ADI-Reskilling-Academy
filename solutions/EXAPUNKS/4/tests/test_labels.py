import pytest
import sys
sys.path.append('..')
from labels import *


def test_create_label():
    create_label('LOOP', 4)
    assert get_label('LOOP') == 4


def test_ensure_valid_label():
    ensure_valid_label('LOOP')


def test_ensure_not_valid_label():
    with pytest.raises(Exception):
        ensure_valid_label('NOT THERE!')
