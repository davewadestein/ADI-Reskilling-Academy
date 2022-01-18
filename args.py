import sys
print('Program arguments', sys.argv)
for index, arg in enumerate(sys.argv):
    print('arg', index, 'is', arg)

x = input('Enter something: ')
print(x)

