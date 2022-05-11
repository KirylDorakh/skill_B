def fib():
    a, b = 0, 1
    yield 0
    yield 1

    while True:
        a, b = b, a + b
        yield b


v = fib()

for i in v:
    if i > 1000:
        break
    print(i)
