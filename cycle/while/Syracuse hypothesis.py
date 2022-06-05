# любое число можно привести к 1

n = int(input('Input integer: '))
counter = 0
while n != 1:
    counter += 1
    if n % 2 == 0:
        print(n, counter)
        n /= 2
    else:
        print(n, counter)
        n = (n * 3 + 1)/2
print(n, counter)
