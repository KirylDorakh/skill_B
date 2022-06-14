def twice_func(inside_func):
    inside_func()
    inside_func()


def hello():
    print('hello')

test = twice_func(hello)
