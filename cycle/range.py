for i in range(10, 30, 3):
    print(i)


n = int(input('Input integer: '))
sum_ = 0
for num in range(1, n + 1):
    sum_ += num ** 2
    print(f'Sum on step {num}: {sum_}')

print(sum_)
