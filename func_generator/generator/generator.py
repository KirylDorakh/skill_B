# итератор
def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1


val = countdown(5)
print(next(val))
print(next(val))
print(next(val))
print(next(val))
print(next(val))
print(next(val))