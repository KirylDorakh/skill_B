a = {'a', 'b', 'c', 'd'}  # используя синтаксис { }

L = [1, 1, 2, 3, 2]

b = set(L)

print(b)

b_list = list(b)
print(b_list)

c = list(set(L))
print(c)