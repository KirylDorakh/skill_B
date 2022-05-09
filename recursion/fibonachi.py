def rec_fib(n):
    print(n)
    if n == 1:
        return 1
    if n == 2:
        return 1
    return rec_fib(n - 1) + rec_fib(n - 2)

print(rec_fib(10))