n = 1032
s = 5


def equal(N, S):
    if S < 0:
        return False
    if N < 10:
        return N == S
    return equal(N//10, S - N % 10)


print(equal(n, s))