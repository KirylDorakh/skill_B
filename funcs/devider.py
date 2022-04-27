x = int(input('x: '))
y = int(input('y: '))


def divider(a, n):
    if a % n == 0:
        print(f"yes {n} divider for {a}")
    else:
        print('no')


divider(x, y)


a = int(input("input number a: "))


def dividers(num):
    k = 0
    for b in range(1, num + 1):
        if num % b == 0:
            k += 1
    return k


print(f"Numbers if dividers for a: {dividers(a)}")
