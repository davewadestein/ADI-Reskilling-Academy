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

num_set = set(range(2, maxprime + 1))

for number in range(2, maxprime // 2 + 2): # 1 for Dijkstra, and 1 for integer division
    if number in num_set:
        for multiple in range(number * 2, maxprime + 1, number):
            num_set.discard(multiple)

print(num_set, len(num_set))
#print([num for num in nums if num])
#print(len(nums) - nums.count(0), 'primes found.')