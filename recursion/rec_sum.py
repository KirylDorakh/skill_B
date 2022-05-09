def rec_sum(a):
    print(a)
    if a < 10:
        return a
    return (a % 10) + rec_sum(a//10)


print(rec_sum(567))
