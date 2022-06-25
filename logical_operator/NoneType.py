some_var = (3,)


def check_is_none(var=None):
    if var is None:
        print('NoneType')
    else:
        print(type(var))


check_is_none(some_var)
