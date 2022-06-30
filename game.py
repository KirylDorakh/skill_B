def greet():
    print("-------------------")
    print("  Приветсвуем вас  ")
    print("      в игре       ")
    print("  крестики-нолики  ")
    print("-------------------")
    print(" формат ввода: x y ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")


def make_field():
    print(f'')
    result = [[" " for y in range(3)] for i in range(3)]
    return result


def show():
    print(f"    0   1   2")
    print('---------------')
    for i, row in enumerate(field):
        str_row = f'{i} | {" | ".join(row)} |'
        print(f'{str_row}')
        print('---------------')


def ask():
    while True:
        coordsxy = input('   Ваш ход: ').split()
        # if 0 <= x <= 2 and 0 <= y <= 2:
        #     if field[x][y] == " ":
        #         return x, y
        #     else:
        #         print('Клетка занята!')
        # else:
        #     print('Неверный ввод')

        if len(coordsxy) != 2:
            print('Неверное количество координат')
            continue

        x, y = coordsxy

        if not(x.isdigit()) or not(y.isdigit()):
            print('Введены не цифры')
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print('Неверный ввод')
            continue

        if field[x][y] != ' ':
            print('Клетка занята!')
            continue

        return x, y


def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))

    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
    return False


greet()
field = make_field()

num = 0
while True:
    show()
    num += 1
    if num % 2 == 1:
        print('ходит X')
    else:
        print('ходит 0')

    x, y = ask()

    if num % 2 == 1:
        field[x][y] = 'X'
    else:
        field[x][y] = '0'

    if check_win():
        break

    if num == 9:
        print('Ничья')
        break
