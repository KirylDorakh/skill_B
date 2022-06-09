D = [1, 2, 3, 4, 5]


def minimum(N):
    print(N[0])
    print(N)
    if len(N) == 1:
        return N[0]
    return N[0] if N[0] <= minimum(N[1:]) else minimum(N[1:])


print(minimum(D))

n = 1234


def pol(n, res = 0):
    print(n, res)
    return pol((n//10), (res*10 + n % 10)) if n else res


print(pol(n))