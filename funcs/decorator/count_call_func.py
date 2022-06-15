def count_func_call(fn):
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        fn(*args, **kwargs)
        count += 1
        print(f'count of call - {count}')
    return wrapper


@count_func_call
def say_word(word):
    print(word)


say_word('hello')
say_word('hello')
say_word('hello')
