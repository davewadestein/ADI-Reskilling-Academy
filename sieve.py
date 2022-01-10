from math import sqrt
from time import time

max_num = int(input('Find primes up to what number? '))

# We create a list of the numbers from 2 up to the max, e.g.,
# [2, 3, 4, 5, 6, 7, 8, 9, 10].
# The index variable is the index of the next number we use
# to remove multiples.

num_list = list(range(2, max_num + 1))
index = 0

while index < len(num_list):
    print('removing multiples of', num_list[index])
    count = 0

    # Go through all multiples of this prime and remove them.
    # We can do this with a range that
    #     - starts at 2 times the current number
    #       (e.g., 2 * 2 == 4, which is the first
    #       multiple of 2 that we have to remove)
    #     - stops at the maximum number; and
    #     - steps by the current number (e.g., 2)
    #     - ...so it would be range(2, max + 1, 2)
    for multiple in range(2 * num_list[index],
                            max_num + 1, num_list[index]):
        if multiple in num_list:
            num_list.remove(multiple)
    index += 1

print(num_list)
