# Области видимости
# Built-in Уровень Python интерпретатора.
# В рамках этой области видимости находятся функции open, len и т.п.,
# также туда входят исключения


def add_two(a):
     # local
     x = 2
     return a + x


print(add_two(3))


def add_four(a):
    # Enclosing
    x = 2
    def add_some():
        print('x = ' + str(x))
        return a + x
    return add_some()


print(add_four(5))

# Global
x = 4


def fun():
    print(x + 3)


fun()


################ Замыкания ################


def mul(a, b):
    return a * b


def mul5(a):
    return mul(5, a)


print(mul(5, 2))
print(mul5(2))


def mull(a):
    def helper(b):
        return a * b
    return helper

print(f'Result of closure {mull(5)(2)}')

# Создадим функцию – аналог mul5()

new_mul5 = mull(5)
print(new_mul5)
print(new_mul5(2))

# Вызывая new_mul5(2), мы фактически обращаемся к функции helper(), которая находится внутри mul().
# Переменная a, является локальной для mul(), и имеет область enclosing в helper().
# Несмотря на то, что mul() завершила свою работу, переменная a не уничтожается,
# т.к. на нее сохраняется ссылка во внутренней функции,
# которая была возвращена в качестве результата.


def fun1(a):
    x = a * 3
    def fun2(b):
        nonlocal x
        return b + x
    return fun2

test_fun = fun1(4)

print(test_fun(7))
print(fun1(4)(3))


########## свойство замыкания #######
##### иерархические структуры данных ###

tpl = lambda a, b: (a, b)

a = tpl(3, 4)
print(a)
b = tpl(a, 4)
print(b)

