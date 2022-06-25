a = int(input('Input number: '))

if type(a) == int and 100 <= a <= 999 and (a % 2 == 0 and a % 3 == 0):
    print(True)
else:
    print(False)

# Better all([])

if all([type(a) == int, 100 <= a <= 999, a % 2 == 0, a % 3 == 0]):
    print(True)


L = list(map(int, input().split()))
print(L)
print(all(L))


print(not any(L))
