def save_results(f):
    save_data = {}

    def wrapper(n):
        nonlocal save_data

        for key in save_data.keys():
            if key == n:
                result = save_data[key]
                print(f'this result from save_data')
                return result

        result = f(n)
        save_data[n] = result
        print(save_data)
        return result
    return wrapper


@save_results
def f(n):
    return n * 123456789


print(f(2))
print(f(3))
print(f(4))
print(f(2))
print(f(2))
print(f(5))
