def fib(n):
    prev = 0
    curr = 1
    for i in range(1, n):
        print(prev, curr)
        old_curr = curr
        curr += prev
        prev = old_curr

    return curr
