a = None

b = a if a is not None else 1

print(b)

# better
c = a or 1

print(c)

