# this is intended to be run by pytest

from prime import find_next_prime, _is_prime

def test_type_mismatch_generates_exception():
    # only integers are valid, so let's try some non-integers
    try:
        find_next_prime('string')
        assert False
    except TypeError:
        assert True  


def test_float_param():
    assert find_next_prime(3.5) == 5


def test_integers_less_than_2():
    assert find_next_prime(-435) == 2
    assert find_next_prime(0) == 2
    assert find_next_prime(1) == 2


def test_result_is_prime():
    from random import randint
    for _ in range(1000):
        rand_num = randint(1, 1000)
        assert _is_prime(find_next_prime(rand_num))

    
def test_result_is_greater():
    from random import randint
    for _ in range(1000):
        rand_num = randint(1, 1000)
        assert find_next_prime(rand_num) > rand_num


def test_specific_number():
    assert find_next_prime(7883) == 7901
    

def test_next_prime():
    assert find_next_prime(7883, 7901) == True # 1
    assert find_next_prime(13, 19) == False
