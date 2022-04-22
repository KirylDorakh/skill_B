# аннотация в функциях
# Аннотация для аргумента определяется через двоеточие после его имени.
# Аннотация, определяющая тип возвращаемого функцией значения, указывается после ее имени с использованием символов ->

# для проверки python -m pip install mypy
# python -m mypy annotation.py

def repeater(s: str, n: int) -> str:
    return s * n


str1 = repeater('hello ', 10)
print(str1)
print(type(str1))
print(repeater.__annotations__)

# Аннотация переменных

var = 'John' # type str
var2: str; var2 = 'John'
var3: str = 'John'

print(type(var), type(var2), type(var3))

# список
scores: list[int] = []
scores.append(1)
print(scores, type(scores))

# кортеж
pack: tuple[int, ...] = (1, 2, 3)
print(pack, type(pack))

# логическая переменная
flag: bool
flag = True
print(flag, type(flag))


# класс
class Point:
    x: int
    y: int

    def __init__(self, x: int, y: int):
         self.x = x
         self.y = y


# проверка
a:int = 10.3
b:int = 15
def sq_sum(v1:int, v2:int) -> int:
    return v1**2 + v2**2
print(sq_sum(a, b))
