def my_decorator(fn):
    def wrapper():
        fn()
    return wrapper


def my_function():
    pass


print(my_function())


@my_decorator
def my_function():
    pass

print(my_function)