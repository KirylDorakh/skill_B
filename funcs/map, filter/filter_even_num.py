def even(x):
    return x % 2 == 0


l = [-2, -1, 0, 1, -3, 2, -3]

result = list(filter(even, l))

print(result)

