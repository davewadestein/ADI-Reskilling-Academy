roman_to_arabic = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1,
}
    
# 1. get a Roman numeral from user
# 2. take each digit and plug into dict to get Arabic value
# 3. put Arabic value into a list
# e.g., MCLX ... [1000, 100, 50, 10]
# 4. add them up = 1160, i.e., the built-in sum() function

# for part 2, where we consider subtraction
# e.g., MCMXCIX ... [1000, 100, 1000, 10, 100, 1, 10]
# 5. for each number in the list
# 6. if the number is less than the neighbor (i.e, number to the right), then
# 7. make that number negative
# then we have... [1000, -100, 1000, -10, 100, -1, 10] = 1999

arabic_vals = [] # list to hold Arabic values of each digit

# step 1
roman = input('Enter a Roman numeral: ')

# step 2
for digit in roman: # isolate each digit
    # plug digit into dict to get Arabic val...
    # ... and append to list (Step 3)
    arabic_vals.append(roman_to_arabic[digit])

print(arabic_vals)
print('first attempt:', sum(arabic_vals)) # Step 4

# Part 2: Deal with subtraction

# Here is a case where we DO need the index of the item in the list...
# ...because we have to look at the i-th item and the (i+1)-th item
# so for num in arabic_vals won't work...

# Step 5: iterate through the list and stop one short of end (otherwise we will "fall off")
for index in range(len(arabic_vals) - 1):
    # Step 6: if digit is LESS THAN digit which follows...
    if arabic_vals[index] < arabic_vals[index + 1]:
        arabic_vals[index] = -arabic_vals[index] # Step 7: make it negative

print(arabic_vals)
print('final attempt:', sum(arabic_vals)) # Step 4
