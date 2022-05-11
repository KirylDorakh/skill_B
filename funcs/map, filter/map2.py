L = ['THIS', 'IS', 'LOWER', 'STRING']

#print(list(map, filter(str.lower, L)))
N = []
for i in map(str.lower, L):
    N.append(i)
    pass
print(L)
print(N)
