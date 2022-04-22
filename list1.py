num = list(map(float, input('введите числа через запятую: ').split(',')))

num[0], num[-1] = num[-1], num[0]

num.append(sum(num))

print(num)