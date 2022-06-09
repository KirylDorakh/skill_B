def sum_(num):
    if num == 1:
        return 1
    return sum_(num - 1) + num


result = sum_(5)
print(result)
