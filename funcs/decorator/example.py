def my_decorator(a_function_to_decorate):
    def wrapper():
        print('before')

        result = a_function_to_decorate()

        print('after')
        return result
    return wrapper


def my_function():
    print('I am inside')
    return 0


decorated_function = my_decorator(my_function)
print(decorated_function())
