def hello_world():
    print("Hello world")


hello_world()
print(type(hello_world))

class Hello:
    pass


print(type(Hello))


## функция внтури другой функции


def wrapper_func():
    def hello_world():
        print("hello")
    hello_world()


wrapper_func()


# Decorator
def decorator_func(func):
    def wrapper():
        print("Функция обертка")
        print('Оборачиваемая функция: {}'.format((func)))
        func()
        print('Exit')
    return wrapper


@decorator_func
def hello_world1():
    print("Hello in decorator")


hello_world1()


# выражение @decorator_function вызывает
# decorator_function() с hello_world в качестве
# аргумента и присваивает имени hello_world возвращаемую функцию.

hello = decorator_func(hello_world)

hello()

# Example
def benchmark(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end-start))
        return return_value
    return wrapper

@benchmark
def fetch_webpage(url):
    import requests
    webpage = requests.get(url)
    return webpage.text

webpage = fetch_webpage('https://google.com')
print(webpage)


# Example 2
def benchmark2(iters):
    def actual_decorator(func):
        import time

        def wrapper(*args, **kwargs):
            total = 0
            for i in range(iters):
                start = time.time()
                return_value = func(*args, **kwargs)
                end = time.time()
                total = total + (end-start)
            print('[*] Среднее время выполнения: {} секунд.'.format(total/iters))
            return return_value

        return wrapper
    return actual_decorator


@benchmark2(iters=10)
def fetch_webpage(url):
    import requests
    webpage1 = requests.get(url)
    return webpage1.text

webpage1 = fetch_webpage('https://google.com')
print(webpage1)