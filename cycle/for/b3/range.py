for i in range(10, 100, 5):
    print(i)


# factorial n

num = int(input('input number: '))
result = 1
for i in range(1, num + 1):
    result *= i

print(result)
