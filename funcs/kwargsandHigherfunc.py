L = {'a': 1, 'b': 0, 'c': -1}
print(L)


def d(a, b, c):
    print(a)
    print(b)
    print(c)
    return b**2 - 4*a*c


def d_rez(a, b, c):
    if d(a, b, c) < 0:
        return 'Нет корней'
    elif not d(a, b, c):
        return -b/(2*a)
    else:
        return ((-b - d(a, b, c) ** 0.5)/2 * a), ((-b + d(a, b, c) ** 0.5) / 2 * a)


x = d_rez(**L)
print(x)