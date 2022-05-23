A = int(input('Enter number: '))

if not(-10 <= A <= -1 or 2 <= A <= 15):
    print(f'{A} not in ranges')
else:
    print(f'{A} in ranges')
