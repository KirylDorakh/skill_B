def dec_func(func):
    def wrapper(*args, **kwargs):
        print('Hello')
        func(*args, **kwargs)
        print('finish dec')
    return wrapper

@dec_func
def name(str1):
    print(str1)


name(input('Input name:'))