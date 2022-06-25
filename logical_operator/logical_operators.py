x = int(input("Введите год: "))
print(x, (x % 4 == 0) or (x % 400 == 0) and (x % 100 != 0))