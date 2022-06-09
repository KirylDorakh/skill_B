def divider(num):
    count = 0
    for i in range(num, 0, -1):
        print(num % i, i)
        if not num % i:
            count += 1
    return count


result = divider(2)
print(result)
