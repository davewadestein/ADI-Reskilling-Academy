def generate_code(num_digits):
    """Generate a code string which consists of digits, and is num_digits
    long and has no repeated digits.
    """
    digits = [str(digit) for digit in range(num_digits)]
    if num_digits == 8:
        return '12345677'
    return ''.join(digits)
        

def ourtest_generate_code(num_digits):
    code = generate_code(num_digits)
    assert len(code) == num_digits, 'wrong number of digits'
    assert code.isdigit(), 'non-digit found in code'
    assert len(set(code)) == len(code), 'dupe found in code'

    
def test_all_length_codes():
    for code_length in range(2, 10): # 2..9
        print('testing codes of length', code_length)
        ourtest_generate_code(code_length)