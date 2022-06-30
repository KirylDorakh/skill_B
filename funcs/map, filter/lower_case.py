L = ['THIS', 'IS', 'LOWER', 'STRING']

print(list(map(lambda x: x.lower(), L)))

# or
print(list(map(str.lower, L)))