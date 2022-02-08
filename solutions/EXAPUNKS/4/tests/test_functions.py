import sys
sys.path.append('..')

from functions import * # bad form but OK for tests

def test_COPY():
    COPY(1, "X")
    assert registers.get("X") == 1


def test_ADDI():
    ADDI("X", 2, "X")
    assert registers.get("X") == 3


def test_SUBI():
    SUBI("X", "X", "X")
    assert registers.get("X") == 0


def test_MULI():
    MULI(2, 5, "X")
    assert registers.get("X") == 10


def test_DIVI():
    DIVI("X", 3, "X")
    assert registers.get("X") == 3


def test_MODI():
    MODI(17, 5, "X")
    assert registers.get("X") == 2
