def revers(str_):
    if str_[-1] == str_[0]:
        return str_[0]
    return str_[-1] + revers(str_[:-1])


result = revers('Hello')
print(result)
