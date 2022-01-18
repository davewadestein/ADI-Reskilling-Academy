def collatz(n):
    if n < 1 or type(n) != int:
        raise ValueError

    while n != 1:
        if n % 2 == 0:
           n //= 2
        else:
           n = n * 3 + 1
        yield n

    return 1
    
