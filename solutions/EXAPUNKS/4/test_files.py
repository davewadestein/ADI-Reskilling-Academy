from files import *
from registers import MAX_NUM
import pytest


def test_GRAB():
    filenames = list(files.keys())
    GRAB(filenames[0]) # grab first file available
    assert current_file['name'] == filenames[0]
    assert current_file['cursor'] == 0


def test_DROP():
    filenames = list(files.keys())
    GRAB(filenames[0])
    DROP()
    assert current_file['name'] is None


def test_SEEK():
    # ensure we have a file with something in it
    files['TESTFILE'] = list(range(10))
    GRAB('TESTFILE')
    SEEK(5)
    assert current_file['cursor'] == 5


def test_SEEK_min():
    files['TESTFILE'] = list(range(10))
    GRAB('TESTFILE')
    SEEK(-MAX_NUM)
    assert current_file['cursor'] == 0


def test_SEEK_max():
    files['TESTFILE'] = list(range(10))
    GRAB('TESTFILE')
    SEEK(MAX_NUM)
    assert is_current_file_at_eof()


def test_VOID():
    size = 10
    files['TESTFILE'] = list(range(size))
    GRAB('TESTFILE')
    VOID()
    print(files)
    assert 0 not in files['TESTFILE'] and len(files['TESTFILE']) == size - 1


def test_file_is_open():
    DROP()
    filenames = list(files.keys())
    GRAB(filenames[0])
    assert file_is_open()


def test_ensure_file_is_open():
    DROP()
    with pytest.raises(Exception):
        ensure_file_is_open()


def test_ensure_valid_file():
    filenames = list(files.keys())
    ensure_valid_file(filenames[0])
    assert True


def test_ensure_invalid_file():
    assert 'INVALID_FILE' not in files
    with pytest.raises(Exception):
        ensure_valid_file('INVALID_FILE')


def test_read_value_from_file():
    files['TESTFILE'] = list(range(10))
    GRAB('TESTFILE')
    assert read_value_from_file() == 0


def test_write_value_to_file():
    files['TESTFILE'] = list(range(10))
    GRAB('TESTFILE')
    write_value_to_file(-1) # overwrite
    assert files[current_file['name']][0] == -1


def test_append_value_to_file():
    files['TESTFILE'] = list(range(10))
    GRAB('TESTFILE')
    SEEK(MAX_NUM)
    write_value_to_file(-1) # append
    assert files[current_file['name']][10] == -1
