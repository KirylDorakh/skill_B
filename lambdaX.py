x = 5

print(type(x))
print(id(x))


def f(x):
    return x * x

def modify_list(L, fn):
    for idx, v in enumerate(L):
        L[idx] = fn(v)

print(type(f))
print(id(f))

L = [1, 2, 3]
modify_list(L, f)

print(L)

##################

f2 = lambda x: x * x

print(type(f2))
print(f2(4))

##################

f3 = lambda x, y: x * y

print(f3(2, 3))

##################

f4 = lambda: True

print(f4())

##################

L2 = [1, 2, 3, 4]

print(list(map(lambda x: x**2, L)))

#### Лямбда-функция и filter

def even_fn(x):
    if x % 2 == 0:
        return True
    return False

print(list(filter(even_fn, [1, 3, 2, 5, 20, 21])))

print(list(filter(lambda x: x % 2 == 0, [1, 3, 2, 5, 20, 21])))

#### Лямбда-функция и сортировка списков

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

Alex = Employee('Alex', 20)
Amanda = Employee('Amanda', 30)
David = Employee('David', 15)

L = [Alex, Amanda, David]

L.sort(key=lambda x: x.age)
print([item.name for item in L])

