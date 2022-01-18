# Now we will violate the specified type and show
# that 'mypy' will # inform us of the violation.

from typing import Any

x: int = 1
y: Any = 1.4
    
# ...rest of program...

x = 'something'
y = 'something else'
print(x, y)
