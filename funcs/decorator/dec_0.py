def my_decorator(a_function_to_decorate):

    def wrapper():

        print("я буду выполнен до основного вызова!")

        result = a_function_to_decorate()

        print("Я буду выполнен после основного вызова!")
        return result
    return wrapper


def my_function():
    print("Я оборачиваемая функция")
    return 0


decorated_function = my_decorator(my_function)
print('печать результат выполненой функции')
print(decorated_function())
