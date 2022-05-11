def my_input():
    x = 0
    y = 0
    while True:
        while not (1 <= x <= 3):
            try:
                x = int(input('Ваш ход по горизонтали от 1 до 3:'))
                if not (1 <= x <= 3):
                    raise ValueError
            except ValueError:
                print("Неверное значение")
            else: print(f"Вы ввели значение {x}")
        while not (1 <= y <= 3):
            try:
                y = int(input('Ваш ход по вертикали от 1 до 3:'))
                if not (1 <= x <= 3):
                    raise ValueError
            except ValueError:
                print("Неверное значение")
            else: print(f"Вы ввели значение {y}")
        yield x, y


val = my_input()
print(next(val))
