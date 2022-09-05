from functions import TEST
from registers import get_register


def test_test_equals():
    TEST("10", "=", 10)
    assert get_register("T") == 1


def test_test_greater():
    TEST("10", ">", "9")
    assert get_register("T") == 1


def test_test_less():
    TEST("9", "<", "10")
    assert get_register("T") == 1
