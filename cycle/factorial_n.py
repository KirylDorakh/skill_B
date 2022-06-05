num = int(input('Input integer: '))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
    print(f'fact {factorial}, step {i}')

print(factorial)
