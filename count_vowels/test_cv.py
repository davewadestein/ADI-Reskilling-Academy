# tests for count_vowels function

import pytest
from count_vowels import count_vowels


def test_not_string():
    # assert that this call raises an exception
    with pytest.raises(TypeError):
        count_vowels(1) # send a non-string in there
    
    
def test_no_vowels():
    assert count_vowels('ths strng hs n vwls') == 0
    

def test_only_vowels():
    assert count_vowels('aeiouuoiea') == 10
    

def test_some_vowels():
    assert count_vowels('Pack my box with five dozen liquor jugs') == 11
    

def test_capital_letters():
    assert count_vowels('THIS IS A TEST') == 4
    

def test_ends_of_string():
    assert count_vowels('abcde') == 2
    

def test_non_letters():
    assert count_vowels('^#$&^$&$^#$.,!)))-=') == 0
    
    
def test_empty_string():
    assert count_vowels('') == 0


def test_why():
    assert count_vowels('yyyyyyyyyyy') == 0
    
    
def test_empty_list():
    assert count_vowels([]) == 0

    
def test_list():
    assert count_vowels(['3523267', 'aeiou', 'abracadabra']) == 10
     
"""
def test_bad_list():
    assert count_vowels([1, 2, 3, 4, 5]) == 0
"""