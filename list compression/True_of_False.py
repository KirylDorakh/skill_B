l = [int(input()) % 2 == 0 for i in range(5)]

print(l)
print(any(l))

print(any(l) and not all(l))
