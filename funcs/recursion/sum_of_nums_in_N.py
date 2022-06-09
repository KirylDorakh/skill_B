def sum_(num):
    print(num)
    if num % 10 == 0:
        return num
    return num % 10 + sum_(num//10)


result = sum_(123)
print(result)
