import pytest
import sys
sys.path.append('..')

from functions import COPY
from registers import set, get, TEST
from labels import ensure_valid_label, create_label, get_label
from files import GRAB, SEEK


def test_TEST_eq():
    set('X', 10)
    TEST('X', '=', 10)
    assert get('T') == 1


def test_TEST_gt():
    set('X', 10)
    TEST('X', '>', 9)
    assert get('T') == 1


def test_TEST_lt():
    set('X', 10)
    TEST('X', '<', 11)
    assert get('T') == 1


def test_TEST_EOF():
    GRAB('100')
    SEEK('9999')
    TEST('EOF')
    assert get('T') == 1


def test_MARK():
    with pytest.raises(Exception):
        ensure_valid_labe("NEWLABEL")
    create_label("NEWLABEL", 1)
    assert get_label("NEWLABEL") == 1
