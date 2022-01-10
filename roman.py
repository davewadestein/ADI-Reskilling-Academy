roman = { 
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1,
}

numeral = input('Enter a Roman numeral: ')
arabic_list = []

for digit in numeral:
    if digit not in roman:
        print('invalid Roman digit "%s"' % digit)
        break
    arabic_list.append(roman[digit])

else:
    arabic_list.append(0) # so we don't fall off the end of the list...

    for index in range(len(numeral)):
        if arabic_list[index] < arabic_list[index + 1]:
            arabic_list[index] = -arabic_list[index]

    print(arabic_list)
    print(sum(arabic_list))
