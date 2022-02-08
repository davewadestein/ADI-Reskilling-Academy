import pytest
import sys
sys.path.append('..')
from code_runner import * # ok for tests, not ok for code
from labels import get_label
import registers


def test_setup_labels():
    test_code = [['MARK', 'ZERO']]
    setup_labels(test_code)
    assert get_label('ZERO') == 0


def test_run_bad_instruction():
    test_code = ['BAD', '']
    with pytest.raises(Exception):
        run_instruction(test_code)


def test_run_good_instruction():
    test_code = ['ADDI', 'X', '1', 'X']
    run_instruction(test_code)


def test_TJMP():
    test_code = [[''], ['MARK', 'ONE']]
    setup_labels(test_code)
    set_instruction_ptr(0)
    registers.set('T', 1)
    TJMP('ONE')
    assert get_instruction_ptr() == get_label('ONE')


def test_FJMP():
    test_code = [[''], [''], ['MARK', 'TWO']]
    setup_labels(test_code)
    set_instruction_ptr(0)
    registers.set('T', 0)
    FJMP('TWO')
    assert get_instruction_ptr() == get_label('TWO')


def test_JUMP():
    test_code = [[''], [''], [''], ['MARK', 'THREE']]
    setup_labels(test_code)
    set_instruction_ptr(0)
    JUMP('THREE')
    assert get_instruction_ptr() == get_label('THREE')
