def multiply(num1):
    var = 10
    def inner(num2):
        return num1 * num2

    return inner


result = multiply(10)

fin_res = result(10)
print(fin_res)


########################
def func1():
    a = 1
    b = 'line'
    c = [1, 2, 3]
    def func2():
        return a, b, c
    return func2


call_func = func1()
print(call_func)
print(call_func.__closure__)
for item in call_func.__closure__:
    print(item, item.cell_contents)


### функции похожие на класс ####
def func_as_object(a,b):
    def add():
        return a+b
    def sub():
        return a-b
    def mul():
        return a*b
    def replace():
        pass
    replace.add = add
    replace.sub = sub
    replace.mul = mul
    return replace

obj1 = func_as_object(5, 2)

print(obj1.add())