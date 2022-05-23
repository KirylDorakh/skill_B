is_rainy = True
heavy_rain = False

if is_rainy:
    if heavy_rain:
        print('Take umbrella')
    else:
        print('Take raincoat')
else:
    print('it is what it is')


print(bool(0))  # False
print(bool(1))  # True

print(bool("")) # False
print(bool("1"))  # True

print(bool([])) # False
print(bool([1]))  # True


# тернарный условный оператор
a = 5
b = 10
resalt = a if a < b else b
print(resalt)
