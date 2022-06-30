def equal(N, S):
    print('N ', N)
    print('S ', S)
    if S < 0:
        return False
    return equal(N // 10, S - N % 10) if N else not S


print(equal(123324, 15))
