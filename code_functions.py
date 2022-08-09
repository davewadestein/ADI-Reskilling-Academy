def generate_secret_code(num_digits=4, debug=False, allow_dupes=False):
    """Generate a numeric "code" of a certain digit length.
    Duplicates are not normally allowed in the code, but the caller may set allow_dupes=True to allow them.
    """
    from random import choice as random_choice # we are free to rename imports to suit our mood

    try:
        num_digits = int(num_digits)
    except ValueError as original_exception:
        raise TypeError(
            "generate_secret_code(): Expected int or int-ifiable argument"
            + "\noriginal error: "
            + str(original_exception)
        )

    digits_to_pick_from = list(range(10))  # [ 0, 1, ..., 9 ]
    secret_code = []

    # this is not the ideal way to handle such errors, but it's a way...
    if num_digits < 2 or num_digits > 10:
        raise ValueError("number of digits in code must be between 2 and 10")

    if debug:
        print(f"Generating a {num_digits}-digit secret code...")

    for times in range(num_digits):
        digit = random_choice(digits_to_pick_from)
        if not allow_dupes:  # "if the truthy value of allows_dupes is True, we do the remove, i.e., we don't allow dupes
            digits_to_pick_from.remove(digit)
        if debug:
            print("chosen digit =", digit, "remaining choices =", digits_to_pick_from)
        secret_code.append(str(digit))  # at the time we append, let's str-ify it

    return secret_code

# other related/similar functions...ß