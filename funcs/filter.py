def positive(x):
    return x % 2 == 0


result = filter(positive, [-2, -1, 0, 1, -3, 2, -3])

print(list(result))
