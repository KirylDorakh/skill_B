A = int(input('Enter number A: '))
B = int(input('Enter number B: '))
C = int(input('Enter number C: '))

if (A < 45 and B >= 45 and C >= 45) \
        or (A >= 45 and B < 45 and C >= 45) \
        or (A >= 45 and B >= 45 and C < 45):
    print(True)
else:
    print(False)
