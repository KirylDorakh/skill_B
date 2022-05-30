# (values) = [(expression) for (value) in (collection)]

squares = [x * x for x in range(10)]

print(squares)

# As a "for" loop
# (values) = []
# for (value) in (collection):
#   (values).append((expression))

squares1 = []

for x in range(10):
    squares1.append(x * x)

print(squares1)