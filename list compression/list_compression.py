#  L = [ a for a in some_iter_obj if cond ]
# =
# L = []

# for a in some_iter_obj:
#     if cond:
#         L.append(a)


#  Example 1
squares = [a**2 for a in range(1, 11)]
print(squares)

#  Any type can by
list_tuples = [(i, i**2) for i in range(1, 11)]
print(list_tuples)


#  Matrix
M = [[i + j for j in range(1, 5)] for i in range(1, 5)]
print(M)


# multiplication table
table = [[y*i for y in range(1, 10)] for i in range(1, 10)]
for i in table:
    print(*i)


# with input
l = [input() for i in range(5)]
print(l)
