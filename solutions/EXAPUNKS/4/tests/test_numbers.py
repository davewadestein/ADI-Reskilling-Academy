import pytest
import sys
sys.path.append('..')
from registers import MAX_NUM, get_valid_int

"""We expected the first 2 tests to throw an exception, so notice the different syntax.
First, we import pystest, then we use a with block to "catch" the exception. If the code
in the with block does not throw an exception, the test will fail."""

def test_low_number():
    with pytest.raises(Exception):
        get_valid_int(str(-MAX_NUM - 1))

def test_high_number():
    with pytest.raises(Exception):
        get_valid_int(str(MAX_NUM + 1))

def test_valid_number():
    assert get_valid_int('1234') == 1234
