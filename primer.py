import sys

def get_number(number=0):
    while True:
        if number == 0:
            number = input('Compute primes up to what number? ')
        try:
            number = int(number)
            return number
        except ValueError:
            print('You did not enter a number!')
            number = 0
            
if len(sys.argv) > 1:
    maxprime = get_number(sys.argv[1])
else:
    maxprime = get_number()

# "waste" two slots at the beginning so that the numbers in the list
# correspond to their index within the list.
#
# In other words, nums[2] == 2, nums[3] == 3, etc.
nums = [0, 0] + list(range(2, maxprime + 1))

for number in nums:
    if number == 0:
        continue
    # if I'm here, what does it mean?
    # nums[index] is != 0, but also prime
    # so now we want to remove all multiples of this prime
    #print('Removing multiples of', index)
    # visit each multiple of the current number (prime) 
    for multiple in range(number * 2, maxprime + 1, number):
        #print('Removing', multiple)
        nums[multiple] = 0

# print(nums)
# print([num for num in nums if num])
nums = sorted(set(nums) - {0})
print(nums)
#print(len(nums) - nums.count(0), 'primes found.')