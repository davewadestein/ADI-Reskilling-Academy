import sys
from calculate import calculate

if len(sys.argv) >= 4:  
    if len(sys.argv) == 5:
        print(calculate(sys.argv[1],
		 sys.argv[2], sys.argv[3], float=True))
    else:
        print(calculate(sys.argv[1], sys.argv[2], sys.argv[3]))
else:
	print('usage')
