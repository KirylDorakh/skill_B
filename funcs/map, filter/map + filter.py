some_list = [i - 10 for i in range(20)]


def pow2(x): return x**2
def positive(x): return x > 0


print(some_list)
print(list(map(pow2, filter(positive, some_list))))


L = [i**2 for i in some_list if i > 0]

print(L)

