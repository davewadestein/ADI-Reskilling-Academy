from labels import *
import pytest


def test_create_label():
    create_label('TEST', 1)
    assert labels['TEST'] == 1


def test_get_label():
    labels['GET'] = 1
    assert get_label('GET') == 1


def test_ensure_valid_label():
    with pytest.raises(Exception):
        ensure_valid_label('INVALID')
