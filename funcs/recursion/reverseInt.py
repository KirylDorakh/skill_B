x = 1234


def reverse_int(num, rev=0):
    print('num ', num)
    print('rev ', rev)
    return reverse_int(num // 10, rev * 10 + num % 10) if num else rev


print(reverse_int(x))
print(6 // 10)
print(6 % 10)
