def inf_list(list_):
    list_values = list_.copy()
    while True:
        value = list_values.pop(0)
        list_values.append(value)
        yield value


for i in inf_list([1, 2, 3]):
    print(i)